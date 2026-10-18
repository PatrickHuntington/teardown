# Recreate, privately white-label, port or replace

Translate observed behavior into an implementable contract and, when requested,
deliver a working result. Rebuilding can mean an independent equivalent, an
authorized fork/rebrand, a compatible client, a platform port, a document template,
or extraction of one feature. Choose from the request and available materials.

## Set the parity contract

Identify the destination repository/output and intended users. Reuse known
constraints; ask only for choices that would change the implementation materially.
For an underspecified private white-label request, clarify whether the user needs
their own branding, self-hosting, offline/local processing, multiple tenants,
data ownership, or merely a private equivalent. These are separate requirements;
"private" alone does not establish all of them.

Build a feature/workflow parity matrix:

`Target behavior ID | Preserve/change/defer | Required fidelity | Evidence |
Acceptance example | Dependencies/unknowns`

Distinguish behavioral, visual, data-format, API and operational compatibility.
Use the level requested. Preserve original functionality without silently adding
every competitor feature. A complete replacement must account for all scoped
workflows; a prototype may have explicit exclusions.

Choose the permitted implementation route: independently written code from
behavioral contracts, a licensed/authorized source fork, supported extension or
plugin, or compatible integration. Use original or authorized branding/assets,
and check the reuse terms of code, data, models and SDKs that the plan depends on.
Access to a product does not establish redistribution rights to its internals.

## Design the equivalent

Keep the observed architecture separate from the proposed one. Research current
building blocks only for capabilities that need them, verifying the official
source and actual fit. Compare an integrated approach with a custom pipeline
when it could simplify the implementation. Respect constraints before choosing.

Specify inputs/outputs, data schemas, state, errors, configuration, service
boundaries and selected dependencies. Trace every critical dependency to its
capability and the evidence that it is suitable. For inaccessible vendor services,
identify a replacement, a feasible original implementation, or an explicit gap;
a stub is not feature parity.

For private deployments, account for identity/roles, secret handling, data
import/export and migration, backups, updates, licensing, remote dependencies,
telemetry and deployment packaging as applicable. If offline use is required,
verify the entire workflow's dependency boundary, including models/assets,
authentication and updates; a local UI can still depend on a remote service.
For a port, include platform APIs, file/protocol compatibility and distribution.
For a document/method, specify template structure, formulas/data and reproducibility.

## Plan or implement according to the request

For a plan: provide dependency-ordered slices, tradeoffs, estimated effort with
assumptions, unresolved questions and acceptance checks. The first slice should
test the uncertainty most likely to invalidate the approach; do not guarantee
a weekend implementation without evidence.

For a build: inspect the destination and its instructions, implement the smallest
useful end-to-end slice, test it against independent target examples, then
complete the remaining authorized scope. Follow relevant coding/design skills
for implementation. Save findings/specification as useful supporting artifacts;
do not stop after writing them. Use representative success, failure and boundary
cases. For visual parity, compare the specified screens at matching states and
viewports; for algorithms, compare outputs with documented tolerances.

Record differences intentionally introduced, workarounds, actual test results
and remaining gaps. Distinguish demonstration, MVP and production readiness.
If something essential is inaccessible, complete independent work and explain
the precise blocker; never report an untested substitute as a verified replica.

## Deliverable and done

A plan is done when another builder can implement and validate the agreed scope
without guessing its consequential contracts. A build is done when the requested
behavior is implemented and its relevant checks pass, with any residual limits
explicit. Include run/deployment instructions appropriate to the delivered work.
Production deployment, publication and external integrations follow the user's
actual authorization, not an assumption that "build" includes launching a service.
