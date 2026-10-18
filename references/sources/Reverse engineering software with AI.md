---
tags:
  - AI/resources
  - tools
  - reverse-engineering
created: 2026-10-06
links_verified: 2026-10-06
---

# Reverse engineering software with AI

Reverse engineering means working out how software behaves when its source code is unavailable. AI agents can inspect files, call analysis tools, explain decompiled code, and help build or modify software based on what they find. Decompilers recover a readable approximation of the compiled program; they do not guarantee the original source code.

MCP, the Model Context Protocol, connects an AI agent to tools such as Ghidra or IDA. This lets the agent query the actual analysis database and record findings there. Check its conclusions against code, cross-references, and observed behavior.

## Repositories

The links below use the full repository names verified through GitHub. Descriptions summarize the projects' own READMEs. The tools have not been installed or tested for this note.

| Repository | What it does | Role in an AI workflow |
| --- | --- | --- |
| [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) | Skills, tools, and shared game-modding knowledge for AI coding agents. Covers game and engine discovery, reverse engineering, mod creation, generated assets, and in-game testing. | A game-focused starting point for agent-assisted modding. |
| [morluto/rea](https://github.com/morluto/rea) | REA, Reverse Engineer Anything, connects agents to inspection tools for native binaries, JavaScript and Electron apps, .NET assemblies, and websites. | Investigate how an app feature works, collect evidence, and use the findings to implement a feature in another project. |
| [trevaintdead/ai-game-modding-guides](https://github.com/trevaintdead/ai-game-modding-guides) | Draft guides for AI-assisted game mods, linking two running games, Rust engine rewrites and ports, mod loaders, prompting, and troubleshooting. | Practical workflow reference rather than a decompiler or MCP server. |
| [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | An MCP bridge to Ghidra with GUI and headless operation. Supports inspection and changes such as renaming symbols, assigning types, and adding comments. | Give an agent access to Ghidra's binary analysis tools and database. |
| [HexRaysSA/ida-mcp](https://github.com/HexRaysSA/ida-mcp) | The official Hex-Rays IDA MCP server, with headless operation and optional GUI integration. Requires an appropriate IDA installation with idalib. | Give an agent access to IDA for binary analysis. |
| [icsharpcode/ILSpy](https://github.com/icsharpcode/ILSpy) | Open-source .NET assembly browser and decompiler, including C# and whole-project decompilation. Includes the ILSpyCmd command-line tool. | Recover readable .NET code for an agent to inspect. ILSpy itself is a decompiler, not an AI agent. |
| [SamboyCoding/Cpp2IL](https://github.com/SamboyCoding/Cpp2IL) | A work-in-progress tool for reversing Unity's IL2CPP compilation process and recovering managed DLLs and metadata. Its README recommends ILSpy for inspecting recovered CIL. | Prepare Unity IL2CPP output for further analysis. Recovery quality and available features depend on the build. |
| [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | Ports PS5 executables to Linux and Windows through binary relinking and replacement system libraries. | A case study in executable formats, platform APIs, and compatibility work. It is a porting tool rather than an AI integration. |
| [yuriolive/PortPS5](https://github.com/yuriolive/PortPS5) | A Windows-focused fork of AnyPS5 that converts already-decrypted PS5 game dumps into native Windows executables using relinking, replacement system libraries, and Vulkan. | A related porting and compatibility case study. It is not a general-purpose AI reverse engineering tool. |

## Where to start

For general software investigation, start with REA. For direct access to a native binary analysis database, use the Ghidra or IDA MCP integration that matches your installed tools. For .NET assemblies, start with ILSpy; for Unity IL2CPP builds, investigate Cpp2IL first. For game modding, read the guides and compare their workflow with universal-modder. AnyPS5 and PortPS5 are useful references for porting compiled software across platforms.

## Link verification

All nine repository names and README descriptions were checked against GitHub on October 6, 2026. The supplied paths `rehan-remade/unive` and `trevaintdead/ai-ga` returned 404s. The owners' public repository lists identified the matching full names as `rehan-remade/universal-modder` and `trevaintdead/ai-game-modding-guides`. GitHub reports the canonical capitalization of ILSpy as `icsharpcode/ILSpy`. `morluto/rea` was already the complete repository path.

Related: [[AI Code Editors]]
