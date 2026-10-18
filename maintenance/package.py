"""Package the skill, preserving hidden paths and verifying every ZIP entry."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
OUTPUT = DIST / 'teardown-v3.0.zip'
required = ['SKILL.md', 'README.md', 'INSTALL.md', 'VALIDATION.md',
            'LICENSE', 'THIRD_PARTY_NOTICES.md']
files = [ROOT / name for name in required]
for folder in ('references', 'scripts', 'maintenance', 'tests'):
    files.extend(p for p in (ROOT / folder).rglob('*')
                 if p.is_file() and '__pycache__' not in p.parts
                 and p.suffix not in ('.pyc', '.pyo'))
entries = [(p, 'teardown/' + p.relative_to(ROOT).as_posix()) for p in sorted(files)]
entries.append((ROOT / 'INSTALL.md', 'INSTALL.md'))
for path, name in entries:
    assert not path.is_symlink(), path
    assert not set(PurePosixPath(name).parts) & {'__pycache__', 'node_modules', '.venv'}, name
    assert not PurePosixPath(name).is_absolute() and '..' not in PurePosixPath(name).parts
assert len({name.casefold() for _, name in entries}) == len(entries), 'Case-colliding paths'

DIST.mkdir(exist_ok=True)
with zipfile.ZipFile(OUTPUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
    for path, name in entries:
        bundle.write(path, name)
with zipfile.ZipFile(OUTPUT) as bundle:
    assert bundle.testzip() is None, 'ZIP CRC failure'
    assert set(bundle.namelist()) == {name for _, name in entries}
    for path, name in entries:
        assert bundle.read(name) == path.read_bytes(), name

digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
OUTPUT.with_suffix('.zip.sha256').write_text(digest + '  ' + OUTPUT.name + '\n', encoding='ascii')
print(json.dumps({'archive': str(OUTPUT), 'bytes': OUTPUT.stat().st_size,
                  'entries': len(entries), 'sha256': digest,
                  'crc': 'pass', 'source_equality': 'byte-identical'}, indent=2))
