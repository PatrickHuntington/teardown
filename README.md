# Teardown

**Point an AI agent at something that exists. Tell it what you want to learn or build.**

Teardown adapts to the target and your goal: investigate a website, document an
app's features, understand a technical paper, assess a product's moat, build a
private branded alternative, improve software, or reverse-engineer a game.

One skill brings together the investigation workflow, REA and Hermes guides,
game-modding skills, decompiler references and platform-porting documentation.
The agent reads the relevant material locally and sets up free analysis tools
when needed.

## Install

Download [the latest release](https://github.com/PatrickHuntington/teardown/releases/latest)
and copy its entire `teardown` folder into your assistant's skills directory.
Keep hidden directories, references, scripts and licenses together.

| Assistant setup | Common destination |
| --- | --- |
| Shared user skills | `~/.agents/skills/teardown/` |
| Claude Code | `~/.claude/skills/teardown/` |
| Other assistants | Their documented skills directory or import workflow |

The final path should end in `skills/teardown/SKILL.md`. Back up an existing
installation first, then reload skills or start a new session.

For a new installation, cloning this repository into that directory also works:

```sh
git clone https://github.com/PatrickHuntington/teardown.git ~/.agents/skills/teardown
```

Or ask your local coding agent:

> Install the Teardown skill from https://github.com/PatrickHuntington/teardown.
> Preserve the complete skill and its bundled references; back up any existing
> version first.

Only Teardown needs installing. Its nested upstream skills are local reference
material; they do not need separate installations. See [INSTALL.md](INSTALL.md)
for tool requirements and portability details.

## Use it

> Use Teardown on **[target]** to **[desired outcome]**.

- "Document every feature and workflow in this web app."
- "Explain this report's methodology and reproduce its calculations."
- "Find out how this desktop app works and build a private branded version."
- "Trace this Electron feature and implement equivalent behavior in my app."
- "Assess this product's competitive advantage and the effort to recreate it."
- "Inspect this Unity game and port my mod to the new version."

Say whether you want an explanation, a plan, or working changes. Teardown selects
guides by **target × goal × available access**, keeps track of coverage, and
separates observed behavior from inference. A reconstruction request continues
through implementation and verification when the necessary access is available.

## What's inside

| Material | Included locally |
| --- | --- |
| Teardown | Six target guides, five outcome guides, evidence workflow and specialist routing |
| REA | Complete Reverse Engineer Anything skill, documentation and four development companion skills |
| Hermes REA | REA references and crash-triage skill with its helper |
| Universal Modder | Twelve skills, engine guides, toolkit source and shared knowledge base |
| AI game-modding guides | All eleven guides and four templates |
| Ghidra MCP and official IDA MCP | Analysis, setup and integration documentation |
| ILSpy and Cpp2IL | Managed-code and Unity IL2CPP references |
| AnyPS5 and PortPS5 | Porting/build documentation, plus PortPS5's six development skills |

The library contains **1,131 original upstream files from ten sources**, with
recorded commits, licenses and per-file hashes. The original research note is
preserved verbatim. [Browse the library router](references/library.md).

The original `trevaintdead/ai-game-modding-guides` URL became unavailable. A
matching public copy from `Freakmenn/ai-game-modding-guides` is included, with
that substitution recorded explicitly in the provenance.

## Analysis tools

The instructions ship with the skill; tool binaries download only when needed.
The agent reuses compatible installed tools or prepares a private cache. The
bundled helper covers REA, Universal Modder, ILSpyCmd, Ghidra and JADX; additional
local recipes cover other tools.

The host assistant needs file/command access and appropriate browser capabilities.
Python 3.10+ runs the helper; the agent handles setup when absent, subject to host
permissions. Proprietary licenses such as IDA, account/device access and target
artifacts remain external inputs. Optional paid services are not required.

See [runtime setup](references/runtime-setup.md) and
[validation results and limits](VALIDATION.md).

## Maintain and verify

From the repository root, using Python 3.10+ (`py -3` on Windows):

```sh
python3 maintenance/verify_bundle.py
python3 tests/check_helpers.py
python3 maintenance/package.py
```

These checks use local files and mocked downloads. They do not install analysis
tools. Packaging creates a ZIP and checksum under `dist/`. GitHub Actions runs
the bundle and helper checks on Windows and Linux.

Preserve vendored source bytes and licenses. Put adaptations in Teardown's own
guides, and update the source manifest deliberately when refreshing snapshots.
Repository-specific upstream agent rules describe their own projects and do not
replace this host's instructions.

## License and credits

Teardown's original instructions, helper code and repository tooling are
[MIT licensed](LICENSE), copyright Patrick Huntington. Bundled upstream material
retains its own license, including MIT, Apache-2.0 and GPL-2.0; the collection
does not relicense those works. Preserve [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)
and the individual licenses when sharing.
