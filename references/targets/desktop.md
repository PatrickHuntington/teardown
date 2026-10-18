# Desktop software, packages and native artifacts

## Identify before choosing an engine

Establish the exact app/path, platform/architecture, version, signature/metadata
and digest. Inventory files and formats without running the target. Distinguish
launchers, installers, application modules, plugins and bundled dependencies.
Use disposable extraction/output directories; preserve the original artifact.

Route by what is actually present:

| Layer | Inspection approach |
| --- | --- |
| Electron/JavaScript/ASAR | Package metadata, entry points, modules, IPC and bundled web UI |
| Managed .NET | Assembly metadata, references, resources and compatible managed decompiler |
| Native PE/ELF/Mach-O | Headers/imports/symbols/resources, then focused native analysis |
| Java/JVM or other bytecode | Runtime/package identification and compatible bytecode tooling |
| Installer/archive/app bundle | Member inventory and selected extraction, then route each relevant member |
| Game/engine package | Engine/build evidence, scripts/assets/plugins, then managed/native paths |
| Firmware | Region/filesystem inventory, embedded binaries/configuration, platform constraints |

Hybrid apps can require several paths. An Electron frontend may delegate the
important computation to a native library or hosted service. Unity-style managed
metadata and native compilation need different analysis; do not promise original
source recovery from packaged or decompiled output. Use the optional
[tool adapters](../tool-adapters.md) when choosing REA or other engines.

## Trace the requested feature

Find an entry point from a menu label, command registration, file type, exported
symbol, resource, string cross-reference or observed event. Trace input parsing,
state/model updates, core transformation, persistence or network boundary, and
result/output. Inspect configuration and resources alongside code. A string is
a search seed, not proof that a feature is reachable or enabled.

For Electron, distinguish main process, renderer, preload/bridge and IPC handlers.
For native code, record module, procedure/address, callers and interpretation
limits. Keep recovered names/types separate from original symbols. Cross-check
load-bearing decompiler interpretations with references, assembly or authorized
runtime observations. Use matching-version source if supplied, clearly labeling
which findings came from source rather than recovered artifacts.

When behavior needs observation, use an appropriate test environment and the
authorized installed app/runtime. Record OS, data/configuration and scenario.
Observe UI, file/database changes, outputs and relevant process/network activity.
Do not execute an unknown installer simply to discover its contents. If execution
or a platform/tool is unavailable, continue static investigation and identify
the unobserved behavior. Avoid broad code dumps: query the path needed to answer
the question and retain reusable analysis state.

## Specialized goals

- Feature inventory: menus, commands, settings, import/export formats, shortcuts,
  plugins, automation hooks and background jobs, with reachability/role evidence.
- Porting/interoperability: observable file/protocol contracts, byte order/encoding,
  platform services, OS/library calls, replacement interfaces and golden samples.
- Modding/improvement: prefer supported extension/configuration seams; for
  authorized patching use a copy, original/new digests, precise change locations,
  rollback and behavioral checks. Separate signing/packaging constraints from code.
- Recreation: implement the behavior contract with original code and permitted
  dependencies/assets. Preserve required compatibility, not decompiler artifacts
  or vendor branding by default.

Native analysis can be slow. Reuse one matching session and retained evidence;
report observed progress or blockers without invented percentages or restarting
an import merely to check whether it is alive.
