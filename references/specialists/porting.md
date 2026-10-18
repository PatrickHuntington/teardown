# Engine rewrites and platform ports

Start with the user's desired compatibility: feature, file format, engine,
mod-loader/version, operating system, or console executable. Load the
[recreate outcome](../outcomes/recreate.md) and the matching local source:

- [Rust rewrites and ports](../upstream/Freakmenn--ai-game-modding-guides/guides/03-rust-rewrites-and-ports.md).
- [Passthrough mods](../upstream/Freakmenn--ai-game-modding-guides/guides/02-passthrough-mods.md) and [worked example](../upstream/Freakmenn--ai-game-modding-guides/guides/09-worked-example-passthrough-mod.md).
- [Port an existing mod](../upstream/rehan-remade--universal-modder/skills/port-a-mod/SKILL.md).
- [AnyPS5 architecture](../upstream/boykopovar--AnyPS5/docs/dev/ARCHITECTURE.md), [build](../upstream/boykopovar--AnyPS5/docs/dev/BUILD.md), [usage](../upstream/boykopovar--AnyPS5/docs/user/USAGE.md).
- [PortPS5 user guide](../upstream/yuriolive--PortPS5/docs/USER_GUIDE.md), [build toolchain](../upstream/yuriolive--PortPS5/docs/spec/build-toolchain.md), [relinker](../upstream/yuriolive--PortPS5/docs/spec/relinker.md), [verification](../upstream/yuriolive--PortPS5/docs/spec/verification.md).

An engine rewrite reconstructs contracts; a relinker changes executable/platform
bindings; an emulator and a two-process passthrough mod solve different problems.
Choose based on the target and requirements, not the popularity of an example.
For PS5 routes, establish already-decrypted supplied inputs, supported host/CPU,
GPU/API requirements, replaced system libraries and documented compatibility.
Do not treat a title's presence in a compatibility list as proof it works on the
user's exact build/hardware.

Two snapshot discrepancies need explicit handling. PortPS5's user guide says
CMake 3.20+, but its README and preset schema 6 require **CMake 3.25+**; use the
latter minimum. The passthrough worked example sends Minecraft player position
to Skyrim in step 5, then reverses its generic A/B direction in step 7. Define
authority and message direction for each state field explicitly from the chosen
architecture; do not implement both contradictory directions as competing owners.

The agent acquires the selected project's pinned source/build dependencies only
when executing the port. Read the local build guide first; set up free toolchains
in an isolated work directory through the managed setup workflow. Keep build
sources and target/game data outside the installed skill. Preserve upstream
licenses and notices for code incorporated into a distributable.

For changes to PortPS5 itself, its repository-specific skills are bundled:
[start a task](../upstream/yuriolive--PortPS5/.agents/skills/start-task/SKILL.md),
[build and test](../upstream/yuriolive--PortPS5/.agents/skills/build-and-test/SKILL.md),
[implement a PRX function](../upstream/yuriolive--PortPS5/.agents/skills/implement-prx-function/SKILL.md),
[record compatibility](../upstream/yuriolive--PortPS5/.agents/skills/compat-result/SKILL.md),
[milestone planning](../upstream/yuriolive--PortPS5/.agents/skills/milestone-seed/SKILL.md),
and [update a specification](../upstream/yuriolive--PortPS5/.agents/skills/update-spec/SKILL.md).
Use these against the selected development checkout and its current rules,
adapting host-specific commands. Their tracker and git operations still follow
the user's requested scope; never apply them to the installed skill directory.

Define milestones with observable outputs: parse/load, initialize required
services, first frame or meaningful operation, input/state, save/load, audio,
and the requested playable/usable scope. Validate on the real target when access
permits; report unsupported services and placeholders separately from successful
behavior. An executable that links or produces one frame is not a completed port.
