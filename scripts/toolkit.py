"""Prepare private free-tool runtimes or run a tool. Standard-library Python 3.10+."""
from pathlib import Path
from urllib.parse import urlencode
import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
import venv
import zipfile

SKILL = Path(__file__).resolve().parents[1]
LOCK = json.loads((SKILL / 'references/runtime-lock.json').read_text(encoding='utf-8'))
TOOLS = ('rea', 'universal-modder', 'ilspy', 'ghidra', 'jadx')

def host():
    system = {'Windows':'win', 'Linux':'linux', 'Darwin':'osx'}.get(platform.system())
    arch = {'AMD64':'x64', 'x86_64':'x64', 'aarch64':'arm64', 'arm64':'arm64', 'ARM64':'arm64'}.get(platform.machine())
    if not system or not arch:
        raise RuntimeError('Unsupported automatic bootstrap host; use the bundled agent-managed setup recipes.')
    return system, arch

def get(url):
    if not url.startswith('https://'):
        raise ValueError('Downloads require HTTPS')
    request=urllib.request.Request(url,headers={'User-Agent':'Teardown-Toolkit/3.0'})
    with urllib.request.urlopen(request,timeout=90) as response:
        return response.read()

def get_json(url):
    return json.loads(get(url))

def checked_download(url, output, expected, algorithm='sha256'):
    if not url.startswith('https://'):
        raise ValueError('Downloads require HTTPS')
    if not expected or not re.fullmatch(r'[a-fA-F0-9]+', expected):
        raise ValueError('Missing publisher integrity digest')
    output=Path(output)
    if not output.exists():
        request=urllib.request.Request(url,headers={'User-Agent':'Teardown-Toolkit/3.0'})
        partial=output.with_name(output.name+'.partial')
        with urllib.request.urlopen(request,timeout=90) as response, partial.open('wb') as dest:
            shutil.copyfileobj(response,dest)
        partial.replace(output)
    digest=hashlib.new(algorithm)
    with output.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):digest.update(block)
    if digest.hexdigest().lower()!=expected.lower():
        raise ValueError(f'Integrity mismatch: {output}; do not execute it')
    return output

def safe_extract(archive, destination):
    destination=Path(destination).resolve()
    def check(name):
        # ZIP path syntax is POSIX even on Windows; reject both separator forms.
        name=name.replace('\\','/')
        if name.startswith('/') or ':' in name or '..' in name.split('/'):
            raise ValueError('Unsafe archive path: '+name)
        if not (destination/name).resolve().is_relative_to(destination):
            raise ValueError('Archive path escapes destination')
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as bundle:
            for item in bundle.infolist():
                check(item.filename)
                if stat.S_ISLNK(item.external_attr>>16):raise ValueError('Archive symlink rejected')
            bundle.extractall(destination)
            if os.name!='nt':
                for item in bundle.infolist():
                    mode=(item.external_attr>>16)&0o777
                    if mode and not item.is_dir():os.chmod(destination/item.filename,mode)
    else:
        with tarfile.open(archive) as bundle:
            members=bundle.getmembers()
            for item in members:
                check(item.name)
                if not (item.isfile() or item.isdir()):
                    # Node and JDK archives can contain links; materialize safe in-tree
                    # links later instead of allowing archive-created filesystem links.
                    if item.issym() or item.islnk():continue
                    raise ValueError('Unsupported archive member')
            for item in members:
                if item.isfile() or item.isdir():bundle.extract(item,destination)
            pending=[item for item in members if item.issym() or item.islnk()]
            while pending:
                remaining=[]
                for item in pending:
                    base=(destination/item.name).parent if item.issym() else destination
                    target=(base/item.linkname).resolve()
                    if not target.is_relative_to(destination):
                        raise ValueError('Unsafe archive link: '+item.name)
                    if not target.is_file():
                        remaining.append(item)
                        continue
                    dest=destination/item.name;dest.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copy2(target,dest)
                if len(remaining)==len(pending):
                    raise ValueError('Unresolved archive links: '+', '.join(x.name for x in remaining))
                pending=remaining

def call(argv, extra_env=None, cwd=None):
    env=os.environ.copy();env.update(extra_env or {})
    subprocess.run([str(x) for x in argv],env=env,cwd=cwd,check=True)

class Toolkit:
    def __init__(self, cache):
        self.cache=Path(cache).expanduser().resolve()
        self.system,self.arch=host()

    def archive(self, name, url, digest, algorithm='sha256'):
        self.cache.mkdir(parents=True,exist_ok=True)
        output=self.cache/name
        marker=output/'.teardown-archive.json'
        if marker.exists():
            saved=json.loads(marker.read_text())
            if saved['digest']!=digest:raise RuntimeError('Cached version identity changed: '+name)
            return output
        if output.exists():raise RuntimeError('Unrecognized existing cache directory: '+str(output))
        with tempfile.TemporaryDirectory(prefix='download-',dir=self.cache) as scratch:
            scratch=Path(scratch).resolve()
            if not scratch.is_relative_to(self.cache):raise RuntimeError('Invalid cache boundary')
            downloaded=checked_download(url,scratch/'archive',digest,algorithm)
            staged=scratch/'unpacked';staged.mkdir()
            safe_extract(downloaded,staged)
            (staged/'.teardown-archive.json').write_text(json.dumps({'url':url,'digest':digest,'algorithm':algorithm}),encoding='utf-8')
            staged.rename(output)
        return output

    def node(self):
        candidate=shutil.which('node')
        if candidate:
            try:
                result=subprocess.run([candidate,'--version'],capture_output=True,text=True,check=True,timeout=20)
                match=re.fullmatch(r'v(\d+)\.(\d+)\.(\d+)\s*',result.stdout)
            except (OSError, subprocess.SubprocessError):
                match=None
            compatible=bool(match and ((int(match[1])==22 and int(match[2])>=19) or (int(match[1])==24 and int(match[2])>=11) or int(match[1])>=26))
            roots=[Path(candidate).resolve().parent]
            npm=shutil.which('npm')
            if npm:roots.append(Path(npm).parent)
            for root in roots:
                scripts=[root/'node_modules/npm/bin/npm-cli.js',root.parent/'lib/node_modules/npm/bin/npm-cli.js']
                for script in scripts:
                    if compatible and script.is_file():return Path(candidate),script
        version=LOCK['node_version']
        system={'win':'win','linux':'linux','osx':'darwin'}[self.system]
        ext='zip' if self.system=='win' else 'tar.gz'
        stem=f'node-{version}-{system}-{self.arch}'
        filename=f'{stem}.{ext}'
        base=f'https://nodejs.org/dist/{version}/'
        sums=get(base+'SHASUMS256.txt').decode()
        matches=[line.split()[0] for line in sums.splitlines() if line.split()[-1]==filename]
        if len(matches)!=1:raise RuntimeError('Node publisher checksum not found for this host')
        root=self.archive(stem,base+filename,matches[0])/stem
        if self.system=='win':return root/'node.exe',root/'node_modules/npm/bin/npm-cli.js'
        return root/'bin/node',root/'lib/node_modules/npm/bin/npm-cli.js'

    def java(self):
        binary_name='java.exe' if self.system=='win' else 'java'
        compiler_name='javac.exe' if self.system=='win' else 'javac'
        candidates=[]
        if os.environ.get('JAVA_HOME'):
            candidates.append(Path(os.environ['JAVA_HOME'])/'bin'/binary_name)
        installed=shutil.which('java')
        if installed:candidates.append(Path(installed))
        for candidate in candidates:
            try:
                result=subprocess.run([str(candidate),'-XshowSettings:properties','-version'],capture_output=True,text=True,check=True,timeout=20)
                details=result.stdout+'\n'+result.stderr
                version=re.search(r'java.specification.version\s*=\s*(\d+)\s*$',details,re.MULTILINE)
                root=re.search(r'java.home\s*=\s*(.+)',details)
                if version and int(version[1])==21 and root:
                    existing=Path(root[1].strip())
                    if (existing/'bin'/compiler_name).is_file():return existing
            except (OSError, subprocess.SubprocessError):
                pass
        system={'win':'windows','linux':'linux','osx':'mac'}[self.system]
        architecture={'arm64':'aarch64','x64':'x64'}[self.arch]
        query=urlencode({'architecture':architecture,'image_type':'jdk','os':system,'vendor':'eclipse'})
        releases=get_json('https://api.adoptium.net/v3/assets/feature_releases/21/ga?'+query)
        if not releases:raise RuntimeError('No compatible JDK 21 release for this host')
        binary=releases[0]['binaries'][0]
        package=binary['package'];identity=releases[0]['release_name'].replace('+','_')
        root=self.archive('java-'+identity+'-'+system+'-'+self.arch,package['link'],package['checksum'])
        found=[p for p in root.rglob(binary_name) if p.parent.name=='bin']
        if not found:raise RuntimeError('JDK executable not found after extraction')
        return found[0].parent.parent

    def dotnet(self):
        candidate=shutil.which('dotnet')
        if candidate:
            try:
                r=subprocess.run([candidate,'--list-sdks'],capture_output=True,text=True,check=True,timeout=20)
                if any(line.startswith('10.') for line in r.stdout.splitlines()):return Path(candidate).resolve()
            except (OSError, subprocess.SubprocessError):
                pass
        releases=get_json('https://builds.dotnet.microsoft.com/dotnet/release-metadata/10.0/releases.json')
        sdk=releases['releases'][0]['sdk']
        rid=self.system+'-'+self.arch
        files=[x for x in sdk['files'] if x['rid']==rid and x['url'].endswith(('.zip','.tar.gz'))]
        if len(files)!=1:raise RuntimeError('No unambiguous portable .NET SDK for '+rid)
        asset=files[0]
        root=self.archive('dotnet-'+sdk['version']+'-'+rid,asset['url'],asset['hash'],'sha512')
        return root/('dotnet.exe' if self.system=='win' else 'dotnet')

    def prepare(self, tool):
        receipts=self.cache/'receipts';receipt=receipts/(tool+'.json')
        if receipt.exists():
            saved=json.loads(receipt.read_text())
            if saved.get('lock_digest')!=hashlib.sha256((SKILL/'references/runtime-lock.json').read_bytes()).hexdigest():
                raise RuntimeError('Tool lock changed; choose a new cache or review the existing receipt')
            if all(Path(p).exists() for p in saved.get('required_paths',[])):
                return saved
        self.cache.mkdir(parents=True,exist_ok=True)
        env={};command=[];required=[];version=''
        if tool=='rea':
            node,npm=self.node();version=LOCK['rea_version']
            prefix=self.cache/('rea-'+version)
            env['PATH']=str(node.parent)+os.pathsep+os.environ.get('PATH','')
            env['npm_config_cache']=str(self.cache/'npm-cache')
            call([node,npm,'install','--prefix',prefix,'--no-audit','--no-fund',f'rea-agents@{version}'],env)
            script=prefix/'node_modules/rea-agents/scripts/rea.mjs'
            command=[str(node),str(script)];required=[str(node),str(script)]
            call(command+['--version'],env)
        elif tool=='universal-modder':
            root=SKILL/'references/upstream/rehan-remade--universal-modder'
            folder=self.cache/'universal-modder-venv'
            python=folder/('Scripts/python.exe' if self.system=='win' else 'bin/python')
            if not python.exists():venv.EnvBuilder(with_pip=True).create(folder)
            call([python,'-m','pip','install','--disable-pip-version-check','--no-cache-dir',*LOCK['universal_dependencies']])
            env={'PYTHONPATH':str(root),'UM_KB':str(root/'knowledge'),'PYTHONDONTWRITEBYTECODE':'1'}
            command=[str(python),'-m','um'];required=[str(python),str(root/'um/cli.py')];version='0.2.0-bundled'
            call(command+['--help'],env)
        elif tool=='ilspy':
            dotnet=self.dotnet();version=LOCK['ilspy_version']
            root=self.cache/('ilspy-'+version)
            exe=root/('ilspycmd.exe' if self.system=='win' else 'ilspycmd')
            env={'DOTNET_ROOT':str(dotnet.parent),'PATH':str(dotnet.parent)+os.pathsep+os.environ.get('PATH',''),'DOTNET_CLI_TELEMETRY_OPTOUT':'1','DOTNET_CLI_HOME':str(self.cache/'dotnet-home'),'NUGET_PACKAGES':str(self.cache/'nuget-packages')}
            if not exe.exists():call([dotnet,'tool','install','ilspycmd','--version',version,'--tool-path',root],env)
            command=[str(exe)];required=[str(dotnet),str(exe)];call(command+['--version'],env)
        elif tool in ('ghidra','jadx'):
            java=self.java();asset=LOCK[tool]
            root=self.archive(tool+'-'+asset['version'],asset['url'],asset['sha256'])
            env={'JAVA_HOME':str(java),'PATH':str(java/'bin')+os.pathsep+os.environ.get('PATH','')}
            version=asset['version'];required=[str(java)]
            if tool=='ghidra':
                matches=list(root.rglob('analyzeHeadless.bat' if self.system=='win' else 'analyzeHeadless'))
                if not matches:raise RuntimeError('Ghidra headless launcher missing')
                env['GHIDRA_INSTALL_DIR']=str(matches[0].parent.parent)
                required.append(str(matches[0]));command=[str(matches[0])]
            else:
                matches=list(root.rglob('jadx.bat' if self.system=='win' else 'jadx'))
                if not matches:raise RuntimeError('JADX launcher missing')
                required.append(str(matches[0]));command=[str(matches[0])]
            # Windows batch launchers are returned as paths, never composed into
            # a shell command with target-controlled arguments by this helper.
            if self.system!='win' and tool=='jadx':call(command+['--version'],env)
        else:raise ValueError(tool)
        data={'tool':tool,'version':version,'command':command,'environment':env,'required_paths':required,
              'lock_digest':hashlib.sha256((SKILL/'references/runtime-lock.json').read_bytes()).hexdigest(),
              'verified':'launcher/help where invoked; target analysis still required'}
        # Store PATH additions only, rather than a machine's complete search path.
        if 'PATH' in data['environment']:
            inherited=os.environ.get('PATH','')
            if inherited and data['environment']['PATH'].endswith(os.pathsep+inherited):
                data['path_prefix']=data['environment'].pop('PATH')[:-(len(inherited)+1)]
        receipts.mkdir(parents=True,exist_ok=True)
        receipt.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
        return data

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache',default=os.environ.get('TEARDOWN_TOOL_CACHE',str(Path.home()/'.cache/teardown-tools/v3')))
    sub=parser.add_subparsers(dest='action',required=True)
    sub.add_parser('status')
    for action in ('prepare','run'):
        p=sub.add_parser(action);p.add_argument('tool',choices=TOOLS)
        if action=='run':p.add_argument('args',nargs=argparse.REMAINDER)
    args=parser.parse_args();toolkit=Toolkit(args.cache)
    if args.action=='status':
        print(json.dumps({'host':host(),'cache':str(toolkit.cache),'available_commands':{x:shutil.which(x) for x in ('node','npm','dotnet','java','ghidra','jadx','rea','ilspycmd')},'receipts':[str(p) for p in (toolkit.cache/'receipts').glob('*.json')]},indent=2));return
    receipt=toolkit.prepare(args.tool)
    if args.action=='prepare':print(json.dumps(receipt,indent=2));return
    if receipt['command'][0].lower().endswith(('.bat','.cmd')):
        raise RuntimeError('Prepared Windows batch launcher: use its receipt with the documented provider configuration or a host-native invocation after inspecting help.')
    env=receipt['environment'].copy()
    if receipt.get('path_prefix'):env['PATH']=receipt['path_prefix']+os.pathsep+os.environ.get('PATH','')
    extra=args.args[1:] if args.args[:1]==['--'] else args.args
    call(receipt['command']+extra,env)

if __name__=='__main__':
    try:main()
    except (RuntimeError,ValueError,OSError,subprocess.SubprocessError) as exc:
        print('Teardown toolkit: '+str(exc),file=sys.stderr);sys.exit(1)
