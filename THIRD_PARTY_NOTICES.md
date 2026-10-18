# Third-party material in Teardown v3

Teardown's authored routing/workflow files are separate from the unmodified
upstream material under `references/upstream/`. The latter retains its original
copyright and license. This collection does not relicense upstream works.
Distribute each snapshot together with its included license/notice files.

| Snapshot | License | Included material |
| --- | --- | --- |
| rehan-remade/universal-modder | [MIT](references/upstream/rehan-remade--universal-modder/LICENSE) | Skills, references, agents, complete knowledge directory, toolkit Python source, launchers and documentation |
| morluto/rea | [MIT](references/upstream/morluto--rea/LICENSE); [third-party notices](references/upstream/morluto--rea/THIRD_PARTY_NOTICES.md) | Complete reverse-engineer-anything skill/reference tree, documentation, license texts and package metadata |
| NousResearch/hermes-official-plugins, REA package | [MIT notices for Nous Research, morluto and mingleiw](references/upstream/NousResearch--hermes-official-plugins/rea/LICENSE) | REA skill/reference tree, crash-triage skill and helper, plugin descriptors and README |
| Freakmenn/ai-game-modding-guides | [MIT covering repository text](references/upstream/Freakmenn--ai-game-modding-guides/LICENSE) | All guides, templates, README and contribution instructions; matching public copy for the unavailable trevaintdead URL |
| bethington/ghidra-mcp | [Apache-2.0](references/upstream/bethington--ghidra-mcp/LICENSE), [NOTICE](references/upstream/bethington--ghidra-mcp/NOTICE) | Documentation/prompts and Ghidra helper scripts |
| HexRaysSA/ida-mcp | [MIT](references/upstream/HexRaysSA--ida-mcp/LICENSE) | README, architecture and package metadata; no IDA executable or license |
| icsharpcode/ILSpy | [MIT](references/upstream/icsharpcode--ILSpy/LICENSE) | Documentation, package usage notes and SDK metadata |
| SamboyCoding/Cpp2IL | [MIT](references/upstream/SamboyCoding--Cpp2IL/LICENSE) | README, core/library documentation and SDK metadata |
| boykopovar/AnyPS5 | [GPL-2.0](references/upstream/boykopovar--AnyPS5/LICENSE) | Original README, contribution guide and complete docs directory, supplied in their original editable source form |
| yuriolive/PortPS5 | [GPL-2.0](references/upstream/yuriolive--PortPS5/LICENSE) | Original README, contribution guide and complete docs directory, supplied in their original editable source form |

The GPL snapshots are included as separate, unmodified works in this aggregate;
their complete corresponding documentation source is the included Markdown.
No compiled AnyPS5/PortPS5 executable is distributed here. Runtime acquisition
and subsequent modifications/distribution must follow the selected project's
license, including its source obligations where applicable.

Exact source repository, commit, file path, Git blob ID and SHA-256 are recorded
in [upstream-manifest.json](references/upstream-manifest.json). Upstream files
are byte-for-byte preserved; adaptations exist only in Teardown's wrapper guides.
The user-supplied [research note](references/sources/Reverse%20engineering%20software%20with%20AI.md)
is also preserved byte-for-byte. Its links to other projects do not transfer
rights to their software, game assets, models or extracted data.

The snapshots also include first-party guides outside the main documentation
directories, REA's four development companion skills, and PortPS5's six skills
and repository rules. Included dependency notices keep their individual terms;
repository agent instructions are reference text, not active host configuration.

The runtime helper downloads free tools from official sources as needed. Those
tools retain their own licenses; their binaries are not part of this skill ZIP.
Paid services, proprietary engines and user-owned targets are not licensed by
this package. Upstream plugin descriptors are reference material, not active
auto-registration files for Teardown's host.
