# Agent-managed free-tool setup

Users install only Teardown. The agent reads all skills/guides locally and owns
any necessary free-tool acquisition, configuration and verification. Network
downloads are allowed when needed; this is not an offline executable bundle.
Do not send the user a list of tools to install when the agent can do the setup.
Keep downloads task-specific and avoid global PATH or shell-profile changes.

## Common bootstrap

The bundled standard-library Python helper installs into a private user cache,
outside the skill and target repository. An explicit `--cache` selects a project
scratch cache instead. On Windows use an installed `py -3`; on other hosts use
`python3`. If no Python exists, the agent provisions a compatible user-space
Python through a verified official distribution or available package manager,
within host permissions, then continues. The helper never installs other skills.

```text
python3 <teardown>/scripts/toolkit.py status
python3 <teardown>/scripts/toolkit.py prepare rea
python3 <teardown>/scripts/toolkit.py run rea -- --help
python3 <teardown>/scripts/toolkit.py run rea -- analyze-javascript-application /absolute/app --format json
python3 <teardown>/scripts/toolkit.py prepare universal-modder
python3 <teardown>/scripts/toolkit.py run universal-modder -- kb search "Unity"
python3 <teardown>/scripts/toolkit.py prepare ilspy
python3 <teardown>/scripts/toolkit.py prepare ghidra
python3 <teardown>/scripts/toolkit.py prepare jadx
```

`status` is local and does not download. `prepare` acquires only that route's
dependencies and writes a receipt. `run` prepares the selected tool if needed,
then passes the remaining arguments literally. Inspect that installed version's
help before using flags from a different snapshot. On Windows, Ghidra/JADX use
batch launchers: use `prepare` and the receipt's paths/environment with the
documented REA provider or a host-native invocation. The generic `run` command
intentionally declines batch wrappers; it supports REA, Universal Modder and
ILSpy on Windows, and executable launchers on other hosts. The agent completes
the provider configuration and analysis rather than handing setup to the user.
The helper can bootstrap:

- **REA:** pinned npm package, with a compatible portable Node if necessary.
  It runs the CLI directly without separate skill installation or MCP setup.
- **Universal Modder:** bundled toolkit source and local knowledge base, with
  Python dependencies in a private virtual environment. No repository clone.
  Search/show the bundled knowledge in place. For new field notes, indexing or
  synchronization, copy the knowledge directory to the working area and invoke
  the receipt's Python command with `UM_KB` pointing to that writable copy;
  preserve the installed snapshot. Sharing notes still requires user scope.
- **ILSpyCmd:** pinned tool and a private .NET SDK/runtime if needed.
- **Ghidra/JADX:** portable official releases and a compatible JDK. Ghidra is
  a large download; explain the size when planning it. A receipt supplies paths
  for the selected REA provider or headless command; this does not itself verify
  that a particular binary imports successfully.

Archives are checked against publisher hashes and unpacked with path/link guards.
Package managers verify registry packages through their native integrity checks.
Receipts record selected versions/paths; preserve successful caches between runs.
Never count a launcher starting as successful target analysis. Verify a small
real operation appropriate to the target after setup.

## Specialized routes

- **REA engines and capabilities:** consult the bundled [installation guide](upstream/morluto--rea/docs/installation.md)
  and the chosen provider/format guide. Point REA at the prepared Java/Ghidra/JADX
  paths using the running version's documented settings. Use CLI when a new MCP
  connection would require a session restart. If MCP is necessary, configure only
  the current host/profile, omit companion skill installation (`--skill=false`
  when supported), back up touched config, and verify actual tool availability.
  Never replace Hermes's pinned plugin registration with a second server.
- **Crash triage:** create a private Python environment for the versions in the
  bundled crash guide (`pwntools`, `pyelftools`, `unicorn`) and set the required
  process environment. Use a supported Linux environment when the libraries need
  it. A Windows host alone does not establish native compatibility.
- **Cpp2IL:** consult [the bundled README](upstream/SamboyCoding--Cpp2IL/README.md),
  identify the game's Unity version, and acquire a compatible official build.
  The repository's old stable release and current development tool have different
  flags; inspect `--help`, processors and output formats. The agent downloads a
  pinned artifact or builds a pinned commit into its cache and records provenance.
- **Direct Ghidra MCP:** use the included [GUI installation](upstream/bethington--ghidra-mcp/docs/INSTALL_GUI.md)
  and [README](upstream/bethington--ghidra-mcp/README.md). Acquire/build the matching
  bridge release in the cache and configure its loopback connection. Preserve
  existing analysis projects and avoid attaching a different target silently.
- **Official Hex-Rays IDA MCP:** if an appropriate licensed IDA/idalib already
  exists, let the agent set up the free bridge from the [local README](upstream/HexRaysSA--ida-mcp/README.md).
  The bridge license does not provide IDA. Prefer free Ghidra if no IDA is present
  and the task does not require IDA-specific output.
- **AnyPS5/PortPS5:** let the agent acquire a pinned source checkout and the free
  toolchain/submodules required by its bundled build guide in the chosen build
  workspace. This runtime source checkout is agent-managed; the user does not
  install another skill. Keep original game/data inputs separate from sources.
- **Other engines and tooling named in a guide:** use installed capabilities
  first, inspect the project's current official release/build requirements, then
  provision the necessary free components locally. Record version, origin and
  integrity evidence. Use the host's package system only when a portable option
  is insufficient and that system modification is authorized.

## Scope and recovery

The user's choice to automate free-tool setup covers routine user-local setup;
existing sandbox, network and execution permissions still apply. Use available
approval mechanisms when a concrete action needs them, without repeating already
settled preferences. Paid licenses, API spending, target execution, real-device
changes, publication and account actions follow the task's actual authorization.

If a download or provider fails, diagnose the specific error, reuse completed
components, try a compatible free alternative, and continue independent work.
Do not loop on a failed setup or claim the tool exists because its docs ship.
Explain an unavoidable user-only input precisely, such as a license, account
login, device access or target artifact. No universal skill can manufacture those.
