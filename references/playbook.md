# Evidence and deliverables

Shared conventions for every Teardown route. Scale the record to the task;
one answered question can use inline citations, while a multi-agent investigation
needs stable IDs and saved artifacts.

## Evidence that survives a handoff

Give important records IDs such as E01 and findings IDs such as F01. Record:

- Target identity and version/build/date; a digest for local artifacts when
  comparing, decompiling, or modifying them. Use a local path or stable URL.
- Locator: document page/section/cell, source file and symbol/line, binary
  address/module, screen and state, request/capture ordinal, or tool Evidence ID.
- What was actually obtained: a short excerpt, observation, data/result, or
  a link to a saved trace. Keep huge dumps outside the main report.
- Collection method and date; relevant role, configuration, environment, and
  tool warnings. A dated screenshot establishes only that recorded state.
- The supported claim and its limit. Protect secrets in stored artifacts too,
  not only in the final response.

Classify findings by evidence type:

| Label | Meaning |
| --- | --- |
| Observed | Actually seen in the supplied artifact, source, or a recorded interaction; state which |
| Documented | A source explicitly asserts it; identify vendor, author, or independent source |
| Inferred | Reasoned from evidence; show the reasoning and plausible alternatives |
| Unknown | Not established by the available evidence |

Confidence is separate from type. A vendor statement can be accurately quoted
yet weak support for real-world quality. A decompiled branch may have uncertain
types. Absence from a bounded search is not proof of absence from the product.
Resolve conflicts by checking version, plan, role, platform, date, and source
proximity. Preserve unresolved disagreement instead of averaging it away.

## Coverage and completion

Use a compact ledger when breadth matters:

`Item | Scope/role/state | Evidence IDs | Status | Finding | Gap/next check`

Status distinguishes inspected, documented-only, inferred, inaccessible, and
out-of-scope. Track both discovered areas and requested areas that remain unknown.
For a full catalog, enumerate navigation/docs/package entry points, follow each
discovered feature family, and reconcile uncovered items before finishing.
For one mechanism, stop once the relevant path and consequential alternatives
are supported or the precise remaining unknown is established.

## Current components and costs

When recommending a dependency, verify its official documentation/repository
and the required capability for this run. Record relevant release/version,
license and deployment terms, maintenance signals, interfaces, limitations, and
pricing date/units. Popularity or a reachable homepage does not establish fitness.
If a source cannot be reached, retain the candidate as unverified; do not promote
it to a confirmed architectural dependency. Reuse checked evidence within a run.

For cost estimates state workload, pricing units, assumptions, and excluded
costs. Include integration, data preparation, inference/retries, human review,
hosting and operations where relevant. Separate prototype and production needs.

## Output shapes

Create only useful artifacts; these names are conventions, not mandatory files:

- `report.md`: answer first, scope/access, selected outcome's findings, evidence,
  coverage and limitations. Omit unrelated business or implementation sections.
- `evidence.md` and `coverage.md`: larger ledgers reused by workers or future runs.
- `features.md`: actors, workflows, state transitions, constraints and acceptance
  criteria, each linked to evidence; include unanswered areas.
- `architecture.md`: observed architecture separately from proposed architecture.
- `rebuild-spec.md`: parity scope, data contracts, choices, dependency gaps,
  slices, acceptance criteria and deployment requirements.
- `improvements.md`: concrete friction/failure, evidence, change, expected effect,
  effort/dependency, and validation method.
- `artifacts/`: sanitized samples, screenshots, diagrams, traces, or evidence
  exports. Reference them by stable paths; do not require proprietary raw dumps
  merely to understand the report.

When updating an earlier teardown, preserve its identity and evidence date,
record changed findings, and distinguish a product change from better evidence.
For a recreation, parity tests must come from the target contract or independently
observed examples, not from the new implementation's own assumptions.
