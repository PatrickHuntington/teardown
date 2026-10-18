# Managed and native analysis handoff

Identify the artifact format before acquiring tooling. Use the complete bundled
guides through [the library](../library.md), and [managed setup](../runtime-setup.md)
for any missing free dependency.

## .NET and Mono

Read [ILSpy's README](../upstream/icsharpcode--ILSpy/README.md) and the relevant
REA [managed-code guide](../upstream/morluto--rea/docs/managed-code-analysis.md).
Use existing `ilspycmd`, or let the runtime helper install a pinned version into
its private cache. Inspect `--help` from that version before using its arguments.
Decompile to a new output folder; keep assembly identity, framework, references,
and warnings. Recovered C# is an explanation of the assembly, not original source.
Check the relevant IL/callers when reconstructed control flow or types matter.

## Unity IL2CPP

Read the bundled [Cpp2IL usage and development notes](../upstream/SamboyCoding--Cpp2IL/README.md).
Match the Unity build, platform, native binary and metadata file. The old stable
release and development builds have materially different flags and supported
versions; select a compatible published artifact or pinned source build rather
than blindly choosing a release labeled latest. Run its help and list processors
and output formats. Recover supported metadata/CIL and inspect through ILSpy.
If method bodies remain native or incomplete, hand those addresses to native
analysis; dummy DLLs do not prove recovered implementations.

## Native code

Use REA's [native skill reference](../upstream/morluto--rea/.agents/skills/reverse-engineer-anything/references/native-and-artifacts.md)
for evidence-driven queries. For a Ghidra database and tool-specific annotation
workflows, use [bethington/ghidra-mcp](../upstream/bethington--ghidra-mcp/README.md)
and its local `docs/prompts/`. This Apache-licensed bridge is distinct from
REA's Ghidra provider. Choose one suitable connection and retain its database.

The [official Hex-Rays IDA MCP](../upstream/HexRaysSA--ida-mcp/README.md)
requires an appropriate existing IDA/idalib installation. Its bridge is open
source; the IDA runtime is not bundled or licensed by Teardown. If absent, use
free Ghidra when it can answer the question; ask for an IDA license only when
the user's requested workflow actually depends on that product.

For analysis modifications (names/types/comments), save to a user-selected copy
or owned analysis database. Distinguish an analysis-database change from a binary
patch, and confirm target identity before either. Use original binary hashes and
specific symbol/address evidence when handing results between tools.
