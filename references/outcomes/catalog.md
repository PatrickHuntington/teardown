# Catalog features and behavior

Produce a navigable, testable specification of the requested surface. The unit
is a user-visible capability or meaningful system behavior, not a marketing
adjective, screen count or list of buttons.

## Discover and reconcile coverage

Build an inventory from available navigation, documentation, menus/commands,
package/source entry points, APIs, examples, settings and observed workflows.
Group into feature families and actors. Include background processes, integrations,
imports/exports, permissions and administration when they belong to scope.

For each capability record:

`ID | Actor/role | Trigger/preconditions | Inputs | Steps/state transitions |
Outputs/side effects | Rules/limits/errors | Evidence | Coverage status`

Follow end-to-end paths, not just static screens. Cover applicable empty, success,
error, permission and recovery states; document which were observed versus merely
documented or inferred. Distinguish plan/platform/version variations and optional
features. Package code can reveal a candidate feature without proving it reachable.

For a document/process, adapt these fields to sections, methods, calculations,
decision rules, handoffs and exceptions. For an API, use endpoints/operations,
schemas, auth, errors and state semantics. Preserve the same evidence discipline.

## Depth and completeness

"All features" means systematically covering every discovered area and explicitly
accounting for inaccessible areas. Maintain the frontier of unexplored routes,
roles, commands and feature families. Reconcile docs against observed UI or code,
record discrepancies, and inspect newly discovered relevant paths. Sampling is
acceptable only when requested or clearly labeled as a limitation.

If access is limited, deliver the catalog with per-item evidence status and
remaining access needs. Do not call it exhaustive for the product when only the
public site, a single role, screenshots, or one platform was available.

## Deliverable and done

Provide a feature index, workflow/state descriptions, relevant visual references,
and acceptance criteria tied to the behavior. Record exclusions and unanswered
questions alongside coverage. When another outcome follows, reuse the same IDs
for parity decisions, architecture, improvement tasks and tests.
