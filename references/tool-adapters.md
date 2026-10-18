# Tool selection and REA

For complete operational instructions use the [bundled library router](library.md).
REA's full upstream skill, specialist references and documentation, the Hermes
variant and crash-triage skill, and all repositories in the original note are
available locally. This file is a compact tool selector, not their replacement.

Select tools from the evidence needed. Discover available tools and inspect their
current schemas; tool names below are examples from the sources at the end, not
promises that a server or engine is installed. Honor the host's tool preferences.

## Prefer a direct inspection path

- Complete source: normal search, language tooling, tests, and dependency/config
  inspection. A decompiler adds no value merely because the project is software.
- Browser: use the host's supported browser, session ownership and profile rules.
  Inspect the current tab before navigation when the user points to an open page.
  Use an available browser skill only when it is the appropriate host workflow.
- Documents/data: format-aware readers, page rendering/OCR, spreadsheet formulas,
  archive inventories, and small local scripts. Read the actual target, not an
  external summary substituted for it.
- Packages/binaries: metadata and format inventory, then a compatible analyzer.
  Managed code, JavaScript, native code, and Android bytecode use different paths.
- Runtime: scoped browser/device/process observation when behavior requires it
  and target execution/interactions fit the user's authorization.

## Optional REA integration

REA can supply artifact graphs, code analysis, and runtime evidence. Discover its
MCP tools through the host's tool catalog/search only when this route benefits
from them. Existing Ghidra, IDA, ILSpy, JADX, platform tools or ordinary file
readers can serve the same evidence needs. REA is not a mandatory installation.

Candidate routes to verify against the installed schema:

| Evidence needed | REA operations to look for |
| --- | --- |
| JavaScript/Electron/ASAR structure | `analyze_javascript_application`, `trace_application_feature` |
| Native code | `open_binary`, focused function/string/caller analysis |
| Managed assemblies | `inspect_managed_artifact` |
| Android package/code | `inspect_android_package` and focused class/method tools |
| Package member inventory | `open_binary` / `inspect_artifact`, where supported |
| Saved web traffic | `inspect_web_network_capture` |
| Firmware/layout/resources | `inspect_firmware_regions`, `inspect_binary_layout`, `inspect_pe_resources` |
| Existing browser/Electron runtime | `list_browser_targets`, `list_electron_targets`, supported observation tools |
| Retained evidence | `inspect_analysis_view`, `get_evidence_bundle`, evidence export |

Resolve required engines and runtime prerequisites from actual availability
results and current documentation. Do not assume a registered MCP server implies
that its native decompiler, Android device, or GUI connection is usable. Report
the exact missing prerequisite and continue supported work. Installation/setup
is handled by Teardown's [managed runtime workflow](runtime-setup.md) when needed
and within current authorization. Set up free tools locally; avoid duplicate
servers and install only components required by the selected route.

For large analyses, request a summary/inventory, retain the returned Evidence ID,
and page into relevant modules/functions. Reuse the active analysis session;
opening a binary is not proof that expensive analysis finished. A timeout or
truncated response calls for state/evidence inspection, not duplicate imports.
Preserve warnings, target hashes and source locations in your own evidence ledger.
Close sessions you own when finished, without closing a user's pre-existing app.

Decompiled pseudocode approximates behavior. Corroborate consequential branches
with callers, references, assembly or runtime evidence; identify inferred names
and types. Treat runtime execution, device modification, and export overwrites
according to the user's existing scope and host permissions. A skill does not
grant new authorization, and it need not ask again for already-authorized steps.

## Design sources

Read on 2026-10-17; consult current docs when actually choosing or installing tools:

- [Hermes REA catalog](https://hermes-agent.nousresearch.com/docs/plugins/rea).
- [Hermes's pinned REA skill](https://github.com/NousResearch/hermes-official-plugins/blob/6dacaaddbfd8e98dfc524096c44f712f743246b8/rea/skills/reverse-engineer-anything/SKILL.md).
- [REA upstream](https://github.com/morluto/rea).
- User-provided *Reverse engineering software with AI.md*, dated 2026-10-06,
  supplied the broader landscape: artifact analysis, managed/native tooling,
  game modding and porting. Its repository descriptions were research leads,
  not tools tested or installed as part of this skill update.

Teardown combines its own target-and-outcome workflow with complete local
upstream guides. Read the selected originals through the library router;
apply its host and path adaptations instead of assuming the Hermes environment.
