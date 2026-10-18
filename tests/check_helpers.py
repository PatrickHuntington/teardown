"""Independent, offline behavior checks; no tools are downloaded or installed."""
from contextlib import redirect_stdout, redirect_stderr
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tarfile
import tempfile
import traceback
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT
HERE = ROOT / '.artifacts/helper-checks'
HERE.mkdir(parents=True, exist_ok=True)
sys.dont_write_bytecode = True

def module(name):
    spec = importlib.util.spec_from_file_location(name, SKILL / 'scripts' / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

t = module('toolkit')
r = module('resolve_resource')
RESULTS = []

def check(name, func):
    try:
        evidence = func()
        row = {'check': name, 'status': 'pass', 'evidence': evidence}
    except Exception as exc:
        row = {'check': name, 'status': 'fail', 'error': type(exc).__name__ + ': ' + str(exc), 'traceback': traceback.format_exc()}
    RESULTS.append(row)
    print(row['status'].upper(), name, row.get('error', ''))

def expect_raises(kind, fn):
    try:
        fn()
    except kind as exc:
        return str(exc)
    raise AssertionError('Expected ' + kind.__name__)

def zip_data(entries):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w') as z:
        for name, content in entries:
            z.writestr(name, content)
    return stream.getvalue()

def tar_data(entries):
    stream = io.BytesIO()
    with tarfile.open(fileobj=stream, mode='w') as tar:
        for name, kind, content, mode in entries:
            item = tarfile.TarInfo(name)
            item.type, item.mode = kind, mode
            if kind == tarfile.REGTYPE:
                item.size = len(content)
                tar.addfile(item, io.BytesIO(content))
            else:
                item.linkname = content
                tar.addfile(item)
    return stream.getvalue()

def extract(payload, directory):
    archive = directory / 'input.archive'
    archive.write_bytes(payload)
    out = directory / 'out'
    out.mkdir(exist_ok=True)
    t.safe_extract(archive, out)
    return out

def check_status_offline():
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        out = io.StringIO()
        with patch.object(sys, 'argv', ['toolkit.py', '--cache', str(Path(temp) / 'cache'), 'status']), patch.object(t.urllib.request, 'urlopen', side_effect=AssertionError('Unexpected network')), redirect_stdout(out):
            t.main()
        payload = json.loads(out.getvalue())
        assert not Path(payload['cache']).exists()
        return payload['host']

def check_download_integrity():
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        target = Path(temp) / 'download'
        content = b'publisher archive bytes'
        digest = hashlib.sha256(content).hexdigest()
        with patch.object(t.urllib.request, 'urlopen', return_value=io.BytesIO(content)) as fetch:
            assert t.checked_download('https://example.invalid/archive', target, digest) == target
            assert fetch.call_count == 1
        with patch.object(t.urllib.request, 'urlopen', side_effect=AssertionError('Duplicate download')):
            t.checked_download('https://example.invalid/archive', target, digest)
        target.write_bytes(b'changed')
        return expect_raises(ValueError, lambda: t.checked_download('https://example.invalid/archive', target, digest))

def check_download_https():
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        payload = b'bytes'
        with patch.object(t.urllib.request, 'urlopen', return_value=io.BytesIO(payload)) as fetch:
            expect_raises(ValueError, lambda: t.checked_download('http://example.invalid/insecure', Path(temp) / 'out', hashlib.sha256(payload).hexdigest()))
            assert fetch.call_count == 0

def check_zip_traversal():
    rejected = []
    for name in ('../outside', '..\\outside', '/absolute', 'C:/absolute', 'folder/../../outside', 'C:relative'):
        with tempfile.TemporaryDirectory(dir=HERE) as temp:
            rejected.append(expect_raises(ValueError, lambda: extract(zip_data([(name, b'escape')]), Path(temp))))
            assert not (Path(temp) / 'outside').exists()
    return rejected

def check_tar_traversal():
    rejected = []
    for name in ('../outside', '..\\outside', '/absolute', 'C:/absolute'):
        with tempfile.TemporaryDirectory(dir=HERE) as temp:
            rejected.append(expect_raises(ValueError, lambda: extract(tar_data([(name, tarfile.REGTYPE, b'escape', 0o644)]), Path(temp))))
    return rejected

def check_zip_symlink():
    link = zipfile.ZipInfo('link')
    link.create_system = 3
    link.external_attr = (stat.S_IFLNK | 0o777) << 16
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        return expect_raises(ValueError, lambda: extract(zip_data([(link, b'../outside')]), Path(temp)))

def check_tar_external_link():
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        location = Path(temp)
        (location / 'outside').write_text('protected')
        payload = tar_data([('link', tarfile.SYMTYPE, '../outside', 0o777)])
        error = expect_raises(ValueError, lambda: extract(payload, location))
        assert (location / 'outside').read_text() == 'protected'
        return error

def check_tar_safe_links():
    payload = tar_data([
        ('jdk/bin/original', tarfile.REGTYPE, b'java-fixture', 0o755),
        ('jdk/bin/java', tarfile.SYMTYPE, 'original', 0o777),
        ('jdk/bin/hard', tarfile.LNKTYPE, 'jdk/bin/original', 0o755),
    ])
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        out = extract(payload, Path(temp))
        for leaf in ('original', 'java', 'hard'):
            assert (out / 'jdk/bin' / leaf).read_bytes() == b'java-fixture'
            assert not (out / 'jdk/bin' / leaf).is_symlink()
        return 'Safe file symlink and hardlink materialized without filesystem links'

def check_tar_link_chain():
    payload = tar_data([
        ('jdk/bin/java', tarfile.SYMTYPE, 'java-link', 0o777),
        ('jdk/bin/java-link', tarfile.SYMTYPE, 'java-real', 0o777),
        ('jdk/bin/java-real', tarfile.REGTYPE, b'java-fixture', 0o755),
    ])
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        out = extract(payload, Path(temp))
        assert (out / 'jdk/bin/java').read_bytes() == b'java-fixture'

def check_archive_repeat_and_failure_cleanup():
    payload = zip_data([('node/bin/node', b'executable fixture')])
    digest = hashlib.sha256(payload).hexdigest()
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        toolkit = t.Toolkit(Path(temp) / 'cache')
        with patch.object(t.urllib.request, 'urlopen', return_value=io.BytesIO(payload)) as fetch:
            first = toolkit.archive('node-version', 'https://example.invalid/fixture', digest)
            second = toolkit.archive('node-version', 'https://example.invalid/fixture', digest)
            assert first == second and fetch.call_count == 1
        expect_raises(RuntimeError, lambda: toolkit.archive('node-version', 'https://example.invalid/fixture', 'a' * 64))
        with patch.object(t.urllib.request, 'urlopen', return_value=io.BytesIO(payload)):
            expect_raises(ValueError, lambda: toolkit.archive('bad', 'https://example.invalid/fixture', 'a' * 64))
        assert not (toolkit.cache / 'bad').exists()
        assert not list(toolkit.cache.glob('download-*'))
        return 'Cached archive reused; different digest rejected; failed digest leaves no published output/staging'

def check_java_arm64():
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        toolkit = t.Toolkit(temp)
        toolkit.system, toolkit.arch = 'osx', 'arm64'
        java = Path(temp) / 'jdk/Contents/Home/bin/java'
        java.parent.mkdir(parents=True)
        java.write_bytes(b'java fixture')
        def api(url):
            architecture = parse_qs(urlparse(url).query)['architecture'][0]
            assert architecture == 'aarch64', 'Adoptium architecture must be aarch64; helper sends ' + architecture
            return [{'release_name': 'jdk-21.0.1+1', 'binaries': [{'package': {'link': 'https://example.invalid/jdk', 'checksum': 'a' * 64}}]}]
        with patch.dict(os.environ, {'JAVA_HOME': ''}), patch.object(t.shutil, 'which', return_value=None), patch.object(t, 'get_json', side_effect=api), patch.object(toolkit, 'archive', return_value=Path(temp)):
            assert toolkit.java() == java.parent.parent

def check_java_existing_jdk_reuse():
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        toolkit = t.Toolkit(temp)
        toolkit.system = 'win'
        root = Path(temp) / 'installed JDK 21'
        (root / 'bin').mkdir(parents=True)
        (root / 'bin/java.exe').touch()
        (root / 'bin/javac.exe').touch()
        details = 'Property settings:\n    java.home = ' + str(root) + '\n    java.specification.version = 21\n'
        result = subprocess.CompletedProcess([], 0, stdout='', stderr=details)
        with patch.dict(os.environ, {'JAVA_HOME': str(root)}), patch.object(t.shutil, 'which', return_value=None), patch.object(t.subprocess, 'run', return_value=result) as probe, patch.object(t, 'get_json', side_effect=AssertionError('Installed compatible JDK must avoid network')), patch.object(toolkit, 'archive', side_effect=AssertionError('Installed compatible JDK must avoid extraction')):
            actual = toolkit.java()
        assert actual == root
        assert probe.call_count == 1
        return 'Existing JDK 21 with javac accepted; no API lookup or archive extraction'

def check_existing_broken_node_fallback():
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        toolkit = t.Toolkit(temp)
        toolkit.system, toolkit.arch = 'linux', 'x64'
        def command(*args, **kwargs):
            raise subprocess.CalledProcessError(127, args[0], stderr='missing libstdc++.so')
        stem = 'node-' + t.LOCK['node_version'] + '-linux-x64'
        sums = ('a' * 64 + '  ' + stem + '.tar.gz\n').encode()
        with patch.object(t.shutil, 'which', return_value='/usr/bin/node'), patch.object(t.subprocess, 'run', side_effect=command), patch.object(t, 'get', return_value=sums), patch.object(toolkit, 'archive', return_value=Path(temp) / 'portable') as archive:
            node, npm = toolkit.node()
            assert archive.call_count == 1
            assert 'portable' in str(node)

def check_existing_broken_dotnet_fallback():
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        toolkit = t.Toolkit(temp)
        toolkit.system, toolkit.arch = 'linux', 'x64'
        releases = {'releases': [{'sdk': {'version': '10.0.1', 'files': [{'rid': 'linux-x64', 'url': 'https://example.invalid/dotnet.tar.gz', 'hash': 'a' * 128}]}}]}
        with patch.object(t.shutil, 'which', return_value='/usr/bin/dotnet'), patch.object(t.subprocess, 'run', side_effect=OSError('broken executable')), patch.object(t, 'get_json', return_value=releases), patch.object(toolkit, 'archive', return_value=Path(temp) / 'portable') as archive:
            result = toolkit.dotnet()
            assert archive.call_count == 1 and 'portable' in str(result)

def check_receipt_repeat():
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        toolkit = t.Toolkit(temp)
        node = Path(temp) / 'node.exe'
        node.touch()
        script = Path(temp) / ('rea-' + t.LOCK['rea_version']) / 'node_modules/rea-agents/scripts/rea.mjs'
        script.parent.mkdir(parents=True)
        script.write_text('fixture')
        with patch.object(toolkit, 'node', return_value=(node, Path(temp) / 'npm-cli.js')), patch.object(t, 'call') as call:
            first = toolkit.prepare('rea')
            assert call.call_count == 2
        with patch.object(toolkit, 'node', side_effect=AssertionError('Repeated runtime setup')), patch.object(t, 'call', side_effect=AssertionError('Repeated package setup')):
            second = toolkit.prepare('rea')
        assert first == second
        assert first['path_prefix'] == str(node.parent)
        assert 'PATH' not in first['environment']
        return 'Second prepare consumes receipt without installation or network'

def check_run_literal_args():
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        directory = Path(temp)
        recorder = directory / 'record.py'
        result = directory / 'result.json'
        recorder.write_text('import json, os, sys\nfrom pathlib import Path\nPath(sys.argv[1]).write_text(json.dumps({"args":sys.argv[2:],"path":os.environ["PATH"],"extra":os.environ["FIXTURE"]}))\n')
        args = ['space in path', '& echo UNSAFE', '$(whoami)', 'semi;colon', 'quoted"value', '--switch']
        receipt = {'command': [sys.executable, str(recorder), str(result)], 'environment': {'FIXTURE': 'present'}, 'path_prefix': str(directory)}
        with patch.object(t.Toolkit, 'prepare', return_value=receipt), patch.object(sys, 'argv', ['toolkit.py', '--cache', str(directory), 'run', 'rea', '--', *args]):
            t.main()
        actual = json.loads(result.read_text())
        assert actual['args'] == args
        assert actual['path'].startswith(str(directory) + os.pathsep)
        assert actual['extra'] == 'present'
        return actual['args']

def check_windows_batch_run():
    receipt = {'command': ['C:/private-cache/jadx/bin/jadx.bat'], 'environment': {'JAVA_HOME': 'C:/private-cache/jdk'}}
    with patch.object(t.Toolkit, 'prepare', return_value=receipt), patch.object(t, 'call') as call, patch.object(sys, 'argv', ['toolkit.py', '--cache', str(HERE / 'unused-cache'), 'run', 'jadx', '--', '--version']):
        message = expect_raises(RuntimeError, t.main)
        assert call.call_count == 0, 'Uninspected batch launcher must not receive target-controlled arguments'
        return message

def check_resolver_all_guides():
    index = json.loads((SKILL / 'references/upstream-index.json').read_text())
    counts = {}
    for repo, folder in index['repos'].items():
        root = SKILL / folder
        files = list(root.rglob('*.md'))
        counts[repo] = len(files)
        for file in files:
            relative = file.relative_to(root).as_posix()
            for base in ('https://github.com/' + repo + '/blob/main/', 'https://raw.githubusercontent.com/' + repo + '/main/'):
                result = r.resolve(base + relative + '#section')
                assert result['status'] == 'local', (relative, result)
                assert Path(result['path']) == file.resolve()
    return counts

def check_resolver_context_and_alias():
    source = SKILL / 'references/upstream/morluto--rea/.agents/skills/reverse-engineer-anything/SKILL.md'
    relative = r.resolve('references/android-applications.md', source)
    root_relative = r.resolve('docs/installation.md', source)
    assert relative['status'] == root_relative['status'] == 'local'
    alias = r.resolve('https://github.com/trevaintdead/ai-game-modding-guides/blob/main/README.md')
    assert alias['status'] == 'local' and 'Freakmenn' in alias['path']
    source_note = r.resolve('sources/Reverse%20engineering%20software%20with%20AI.md')
    assert source_note['status'] == 'local'
    assert r.resolve('../../../../../../../../outside', source)['status'] == 'not-bundled'
    assert r.resolve('README.md', ROOT.parent / 'outside-fixture.md')['status'] == 'outside-skill'
    return {'file_relative': relative, 'repo_root': root_relative, 'alias': alias, 'encoded_space': source_note}

def collect_link_inventory():
    unresolved = []
    counts = {}
    for source in (SKILL / 'references').rglob('*.md'):
        text = source.read_text(encoding='utf-8', errors='replace')
        for match in re.finditer(r'\[[^\]\n]*\]\(([^\s)]+)\)', text):
            pointer = match[1]
            if pointer.startswith('#'):
                continue
            result = r.resolve(pointer, source)
            counts[result['status']] = counts.get(result['status'], 0) + 1
            if result['status'] == 'not-bundled':
                unresolved.append({'source': str(source.relative_to(SKILL)), 'pointer': pointer})
    (HERE / 'unresolved-links.json').write_text(json.dumps(unresolved, indent=2) + '\n')
    return counts

if __name__ == '__main__':
    for name, test in [
        ('status is local and non-mutating', check_status_offline),
        ('download hashes and cache reuse', check_download_integrity),
        ('artifact download enforces HTTPS', check_download_https),
        ('ZIP traversal guard', check_zip_traversal),
        ('TAR traversal guard', check_tar_traversal),
        ('ZIP symlink rejection', check_zip_symlink),
        ('TAR external link rejection', check_tar_external_link),
        ('TAR safe file links', check_tar_safe_links),
        ('TAR safe forward link chain', check_tar_link_chain),
        ('archive repeat and failure cleanup', check_archive_repeat_and_failure_cleanup),
        ('macOS ARM64 Adoptium query', check_java_arm64),
        ('existing JDK 21 avoids download', check_java_existing_jdk_reuse),
        ('broken installed Node falls back to private runtime', check_existing_broken_node_fallback),
        ('broken installed .NET falls back to private runtime', check_existing_broken_dotnet_fallback),
        ('receipt skips completed installation', check_receipt_repeat),
        ('run executes real harmless command with literal arguments', check_run_literal_args),
        ('Windows batch run declines safely; prepare/provider route required', check_windows_batch_run),
        ('every bundled Markdown file resolves through GitHub and raw URLs', check_resolver_all_guides),
        ('resolver context, root fallback, alias, encoded path, containment', check_resolver_context_and_alias),
        ('bundled Markdown link inventory', collect_link_inventory),
    ]:
        check(name, test)
    summary = {'python': sys.version, 'platform': sys.platform, 'checks': len(RESULTS), 'passed': sum(x['status'] == 'pass' for x in RESULTS), 'failed': sum(x['status'] == 'fail' for x in RESULTS), 'results': RESULTS}
    (HERE / 'results.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: summary[k] for k in ('checks', 'passed', 'failed')}))
    sys.exit(bool(summary['failed']))
