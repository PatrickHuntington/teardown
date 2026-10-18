# Teardown v3.0

One entry point for investigating websites, web apps, documents, desktop/mobile
software, binaries, games, firmware, source, APIs and unfamiliar artifacts.
It adapts to your goal: understand the stack, catalog features, assess the moat,
recreate or privately white-label a product, port a feature, or improve it.

## Install once

1. Extract `teardown-v3.0.zip`.
2. Copy the **entire `teardown` folder**, including hidden subdirectories, into
   your assistant's skills directory. Common locations:
   - Shared user skills: `~/.agents/skills/teardown/`
   - Claude Code: `~/.claude/skills/teardown/`
   - Other hosts: their documented skills directory or import workflow.
3. Reload skills or start a new session if needed.

The final path ends in `skills/teardown/SKILL.md`. Keep `references/`, `scripts/`
and the license notices together. Back up an existing Teardown folder before
replacing it. Do not install the nested upstream skills separately.

You can give a local coding agent this instruction:

> Install Teardown from this ZIP into my user-level skills directory. Preserve
> the entire folder, including hidden files, references, scripts and notices.
> Back up any previous version first.

## Use

> Use Teardown on [URL, file, app, repository, or target] to [desired outcome].

Examples:

- "Document all features and workflows in this web app."
- "Explain this report's methodology and reproduce its calculations."
- "Build a private, branded version of this tool with these improvements."
- "Trace this Electron feature and implement equivalent behavior in my app."
- "Inspect this Unity game and port my mod to the new version."

Specify whether you want an explanation, a plan, or working changes. Teardown
chooses the relevant target, outcome and specialist guides.

## What is bundled

- The original research note, byte-for-byte.
- REA's complete reverse-engineer-anything skill and guides, its four development
  companion skills, and Hermes's REA and crash-triage skills.
- Universal Modder's 12 skills, engine references, toolkit source and knowledge base.
- All AI game-modding guides and templates.
- Ghidra MCP, official IDA MCP, ILSpy, Cpp2IL, AnyPS5 and PortPS5 documentation,
  including PortPS5's six development skills and rules.
- Teardown's target/outcome workflows, local resource resolver and free-tool helper.
- Source commits, per-file hashes and original licenses/notices.

The old `trevaintdead/ai-game-modding-guides` link is unavailable. Its original
mention is preserved; the matching public `Freakmenn/ai-game-modding-guides`
copy is bundled, with the substitution recorded in the library router.

## Tools and portability

**Users install only Teardown.** All skills/guides are local. When an analysis
needs a free tool, the agent checks available capabilities and prepares the
missing components in a private cache. The helper supports REA, Universal Modder,
ILSpyCmd, Ghidra and JADX; local recipes cover the other routes. Downloads are
allowed. This ZIP does not include preinstalled tool binaries or promise offline
analysis of every target.

The host assistant provides file/command access and browser capabilities.
Python 3.10+ runs the helper; the agent handles its setup if absent. Existing
host permissions still apply. Windows Ghidra/JADX batch launchers use prepared
paths with provider configuration rather than the helper's generic `run` action.

Proprietary licenses such as IDA, account/device access and the target artifacts
come from the user when required. Free alternatives are preferred when suitable.
Optional paid services in upstream examples are not mandatory dependencies.

Actual Windows validation covered REA setup and static JavaScript analysis,
Universal Modder setup and local knowledge search, plus offline helper and
routing checks. Every tool/OS combination has not been exercised. Copying the
folder uses the standard SKILL.md layout; individual hosts' ZIP import UIs have
not been tested.

Keep `THIRD_PARTY_NOTICES.md` and upstream licenses when sharing. The package
contains separate MIT, Apache-2.0 and GPL-2.0 material under its original terms.
