from pathlib import Path
from urllib.parse import unquote
import ast
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT
manifest=json.loads((SKILL/'references/upstream-manifest.json').read_text(encoding='utf-8'))
assert not manifest['errors'], manifest['errors']
count=0
for source in manifest['sources']:
    base=SKILL/'references/upstream'/source['repo'].replace('/','--')
    for entry in source['files']:
        data=(base/entry['path']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==entry['sha256'], entry['path']
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==entry['git_blob']
        count+=1
assert len(manifest['sources'])==10
expected={
 'rehan-remade/universal-modder','morluto/rea','Freakmenn/ai-game-modding-guides',
 'bethington/ghidra-mcp','HexRaysSA/ida-mcp','icsharpcode/ILSpy','SamboyCoding/Cpp2IL',
 'boykopovar/AnyPS5','yuriolive/PortPS5','NousResearch/hermes-official-plugins'}
assert {x['repo'] for x in manifest['sources']}==expected

# Authored routing files must have working links. Original upstream bytes stay
# untouched; their URL/repo-root pointers are handled by the bundled resolver.
checked=0
for doc in SKILL.rglob('*.md'):
    if 'upstream' in doc.relative_to(SKILL).parts or 'sources' in doc.relative_to(SKILL).parts:continue
    body=doc.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)',body):
        target=unquote(target.split('#')[0])
        if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
        resolved=(doc.parent/target).resolve()
        assert resolved.is_relative_to(SKILL.resolve()),(str(doc),target)
        assert resolved.exists(),(str(doc),target)
        checked+=1
for script in (SKILL/'scripts').glob('*.py'):ast.parse(script.read_text(encoding='utf-8'),filename=str(script))
note=SKILL/'references/sources/Reverse engineering software with AI.md'
assert hashlib.sha256(note.read_bytes()).hexdigest()=='437f874e64346154225d3bd1dccb525b1013d17a13b252a61ee89a91d7fc4f5f'
print(json.dumps({'upstream_sources':len(expected),'verbatim_files_checked':count,'authored_local_links_checked':checked,'original_note':'byte-identical','python_helpers':'parsed'}))
