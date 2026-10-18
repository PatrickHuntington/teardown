# Bundled specialist library

Teardown is the entry point. All instructions below are files inside this skill;
read them directly without installing companion skills or cloning their repos.
Resolve this directory from the installed `SKILL.md`, not the working directory.
Select by target and task, then retain Teardown's outcome/coverage requirements.

## Choose a route

| Need | Local entry point | Follow-up |
| --- | --- | --- |
| General shipped-artifact analysis; native, managed, JS/Electron, Android, firmware or browser evidence | [REA upstream skill](upstream/morluto--rea/.agents/skills/reverse-engineer-anything/SKILL.md) | [REA route index](#rea-deep-guides) |
| Specifically Hermes's REA workflow | [Hermes REA skill](upstream/NousResearch--hermes-official-plugins/rea/skills/reverse-engineer-anything/SKILL.md) | Its six local references; retain host-specific distinctions |
| Recorded Linux native crash/core dump | [Crash triage](upstream/NousResearch--hermes-official-plugins/rea/skills/crash-triage/SKILL.md) | Bundled `scripts/core_mappings.py`; exact binary/build identity |
| Mod a game from idea through actual verification | [Universal Modder](upstream/rehan-remade--universal-modder/skills/mod-any-game/SKILL.md) | [Game workflows](#game-workflows) and the matching engine reference |
| Learn a game engine, locate hooks, reverse a file format | [Game reverse engineering](upstream/rehan-remade--universal-modder/skills/reverse-engineering/SKILL.md) | Native/managed routes below and bundled knowledge base |
| Link two running games, rewrite an engine, learn a mod loader | [AI game-modding guide index](upstream/Freakmenn--ai-game-modding-guides/README.md) | All 11 guides and four templates are bundled |
| Native Ghidra GUI/headless analysis or analysis-database edits | [Ghidra MCP](upstream/bethington--ghidra-mcp/README.md) | [Tool usage](upstream/bethington--ghidra-mcp/docs/prompts/TOOL_USAGE_GUIDE.md), [connection triage](upstream/bethington--ghidra-mcp/docs/connection-triage-guide.md) |
| Native analysis with an existing licensed IDA installation | [Official Hex-Rays IDA MCP](upstream/HexRaysSA--ida-mcp/README.md) | [Architecture](upstream/HexRaysSA--ida-mcp/docs/ARCHITECTURE.md) |
| Managed .NET/Mono assembly recovery | [ILSpy](upstream/icsharpcode--ILSpy/README.md) | [Managed workflow](specialists/managed-and-native.md) |
| Unity IL2CPP binary plus metadata | [Cpp2IL](upstream/SamboyCoding--Cpp2IL/README.md) | Recover metadata/CIL as supported, inspect through ILSpy; native bodies may need REA/Ghidra |
| PS5 binary relinking, replacement system libraries, Linux/Windows compatibility | [AnyPS5](upstream/boykopovar--AnyPS5/README.md) | [Architecture](upstream/boykopovar--AnyPS5/docs/dev/ARCHITECTURE.md), [build](upstream/boykopovar--AnyPS5/docs/dev/BUILD.md), [usage](upstream/boykopovar--AnyPS5/docs/user/USAGE.md) |
| Windows-focused PS5 porting/recompiler work | [PortPS5](upstream/yuriolive--PortPS5/README.md) | [User guide](upstream/yuriolive--PortPS5/docs/USER_GUIDE.md), [technical specs](upstream/yuriolive--PortPS5/docs/spec/README.md) |

AnyPS5/PortPS5 are specialized compatibility projects, not universal decompilers.
Use already-decrypted user-provided material and the actual supported platform
and build requirements. For these routes read [porting](specialists/porting.md).
Source/build dependencies are acquired by the agent only when executing a port;
the relevant instructions and specifications are already bundled.

## REA deep guides

Read the upstream skill first, then the precise branch. The full `docs/` tree
also ships locally for less common formats and troubleshooting.

- [Connection and recovery](upstream/morluto--rea/.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md).
- [Native, managed, archives and extraction](upstream/morluto--rea/.agents/skills/reverse-engineer-anything/references/native-and-artifacts.md).
- [JavaScript application analysis and feature tracing](upstream/morluto--rea/.agents/skills/reverse-engineer-anything/references/javascript-applications.md).
- [Android packages/classes/methods](upstream/morluto--rea/.agents/skills/reverse-engineer-anything/references/android-applications.md).
- [Runtime observation](upstream/morluto--rea/.agents/skills/reverse-engineer-anything/references/runtime-observation.md).
- [Evidence, comparisons and verification](upstream/morluto--rea/.agents/skills/reverse-engineer-anything/references/evidence-workflows.md).
- [NativeAOT](upstream/morluto--rea/docs/ghidra-nativeaot.md), [firmware](upstream/morluto--rea/docs/firmware-analysis.md), [EVM bytecode](upstream/morluto--rea/docs/evm-bytecode.md), [WebAssembly](upstream/morluto--rea/docs/wasm-artifacts.md).
- [Recorded crashes](upstream/morluto--rea/docs/recorded-crashes.md), [binary layout](upstream/morluto--rea/docs/binary-diagnostics.md), [saved web captures](upstream/morluto--rea/docs/web-network-captures.md), [packet captures](upstream/morluto--rea/docs/packet-captures.md).
- [Ghidra provider](upstream/morluto--rea/docs/ghidra-provider.md), [REA's IDA provider](upstream/morluto--rea/docs/ida-provider.md), [managed code](upstream/morluto--rea/docs/managed-code-analysis.md).
- [CLI reference](upstream/morluto--rea/docs/cli.md), [installation](upstream/morluto--rea/docs/installation.md), [all documentation](upstream/morluto--rea/docs/index.md).

REA's IDA provider and the official Hex-Rays MCP are distinct integrations.
Select the configured/appropriate one; never assume they expose identical tools
or install one over the other. Repo main, released REA and Hermes's pinned REA
can differ. Use the running version's schemas and the version notes in the guides.
In this snapshot the upstream skill says IDA lacks `binary_overview`, while the
provider guide describes profile-dependent support. Query capabilities on the
actual connection; an omitted segment list means unobserved, not empty.

When the requested improvement concerns REA itself, its other skills are also
bundled: [analysis optimization](upstream/morluto--rea/.agents/skills/rea-analysis-optimization/SKILL.md),
[tool design](upstream/morluto--rea/.agents/skills/rea-tool-design/SKILL.md),
[CI/test auditing](upstream/morluto--rea/.agents/skills/rea-ci-tests-audit/SKILL.md),
and [changelog updates](upstream/morluto--rea/.agents/skills/rea-changelog-update/SKILL.md).
These apply to a REA development checkout; their repository-edit instructions
do not apply to an unrelated investigation or the installed Teardown snapshot.

## Game workflows

Universal Modder's 12 skills, engine references, agents, toolkit source, and
complete knowledge directory are bundled. Start with `mod-any-game` for an
end-to-end mod; select companions by the actual subtask:

- [Recon](upstream/rehan-remade--universal-modder/skills/game-recon/SKILL.md) and [community research](upstream/rehan-remade--universal-modder/skills/game-research-websearch/SKILL.md).
- [Reverse engineering](upstream/rehan-remade--universal-modder/skills/reverse-engineering/SKILL.md) and [cross-game mashups](upstream/rehan-remade--universal-modder/skills/mashup-mods/SKILL.md).
- [Port a mod](upstream/rehan-remade--universal-modder/skills/port-a-mod/SKILL.md).
- [Asset processing](upstream/rehan-remade--universal-modder/skills/asset-pipeline/SKILL.md) and [generated assets](upstream/rehan-remade--universal-modder/skills/fal-assets/SKILL.md).
- [Game automation](upstream/rehan-remade--universal-modder/skills/game-automation/SKILL.md) and [showcase recording](upstream/rehan-remade--universal-modder/skills/showcase-video/SKILL.md).
- [Publishing checks](upstream/rehan-remade--universal-modder/skills/publish-mod/SKILL.md) and [field notes](upstream/rehan-remade--universal-modder/skills/share-field-notes/SKILL.md).
- [Knowledge index](upstream/rehan-remade--universal-modder/knowledge/INDEX.md): search the local `knowledge/` for the game, engine and format before repeating prior work. Notes are version-specific observations, not guaranteed compatibility.

Publishing, contacting communities, paid asset generation and modifying an account
are separate actions only when the user's request includes them. A reference to
a paid service does not make it a required dependency. Use available local assets
or free alternatives when appropriate. Setup of free tools is covered below.

## Path and host adaptation

1. A companion skill name resolves to the local entry above. Read it as a
   reference within Teardown; never install another skill just to invoke it.
2. Preserve original file bytes. A link within an upstream file is relative to
   that file. A prose repo-root path (`knowledge/`, `skills/`, `bin/um`) is relative
   to that source's directory under `references/upstream/`. The packaged
   [resource resolver](../scripts/resolve_resource.py) maps GitHub/raw links and
   missing relative links into the local snapshot without fetching anything.
3. Use [the local index](upstream-index.json) or search the selected snapshot
   before opening an upstream documentation URL. External project examples,
   APIs and current releases can still need network research; all first-party
   selected skills/guides are local. Record unresolved external source pointers.
4. Treat upstream agent/client setup steps as recipes for the named host. On a
   different host use its actual tool catalog, browser and approval system.
   Teardown's current user authorization controls setup; do not inherit redundant
   confirmation or mandatory skill-install steps from a different runtime.
   Bundled `AGENTS.md`, `CLAUDE.md` and repository rules describe their source
   projects; they are reference material, not policy for the host workspace.
5. Use [managed setup](runtime-setup.md) for missing free tools. Prefer CLI or a
   session-scoped connection over persistent configuration changes. Preserve
   existing registrations; any necessary scoped repair uses a backup and respects
   the host's permissions. Never configure all clients on the machine by default.

## Provenance and coverage

The [original note](sources/Reverse%20engineering%20software%20with%20AI.md) is
byte-for-byte preserved. Its old `trevaintdead/ai-game-modding-guides` URL and
account returned 404 on 2026-10-18. A public matching guide exists under
`Freakmenn/ai-game-modding-guides`, with the same subject, guide titles and Trev
copyright. That copy is bundled; an account transfer has not been independently
established. This preserves the source note's original claim and makes the
replacement mapping explicit.

All nine named projects, plus the Hermes REA package, have an entry above.
The [manifest](upstream-manifest.json) records exact commits, file paths, source
blob IDs and SHA-256 hashes. [Third-party notices](../THIRD_PARTY_NOTICES.md)
state licenses and redistribution boundaries. Snapshots are reference material,
not a claim that every runtime or published example has been executed locally.
