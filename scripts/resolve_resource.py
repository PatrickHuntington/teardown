"""Resolve an upstream pointer to bundled files. No network or dependencies."""
from pathlib import Path
from urllib.parse import unquote, urlparse
import argparse
import json

SKILL = Path(__file__).resolve().parents[1]

def resolve(pointer, source=None):
    index = json.loads((SKILL / 'references/upstream-index.json').read_text(encoding='utf-8'))
    pointer = unquote(pointer.split('#')[0])
    parsed = urlparse(pointer)
    if parsed.scheme in ('https', 'http'):
        bits = parsed.path.strip('/').split('/')
        if parsed.netloc == 'github.com' and len(bits) >= 5 and bits[2] in ('blob', 'tree'):
            repo, relative = '/'.join(bits[:2]), '/'.join(bits[4:])
        elif parsed.netloc == 'raw.githubusercontent.com' and len(bits) >= 4:
            repo, relative = '/'.join(bits[:2]), '/'.join(bits[3:])
        else:
            return {'status':'external', 'pointer':pointer}
        repo = index.get('aliases', {}).get(repo, repo)
        root = index['repos'].get(repo)
        candidates = [SKILL / root / relative] if root else []
    else:
        candidates=[]
        if source:
            origin=Path(source).resolve()
            if not origin.is_relative_to(SKILL):
                return {'status':'outside-skill','pointer':pointer}
            candidates.append(origin.parent / pointer)
            for root in index['repos'].values():
                local=(SKILL/root).resolve()
                if origin.is_relative_to(local):
                    candidates.append(local/pointer)
        candidates.append(SKILL/'references'/pointer)
    for candidate in candidates:
        resolved=candidate.resolve()
        if not resolved.is_relative_to(SKILL):
            continue
        if resolved.is_file():return {'status':'local','path':str(resolved)}
        if resolved.is_dir():return {'status':'local-directory','path':str(resolved),'entries':sorted(x.name for x in resolved.iterdir())}
    return {'status':'not-bundled','pointer':pointer,'note':'External code/example/runtime may require agent-managed acquisition; do not invent its contents.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pointer');parser.add_argument('--from-file',dest='source')
    args=parser.parse_args()
    print(json.dumps(resolve(args.pointer,args.source),indent=2))
