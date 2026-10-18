# Improve, redesign, optimize, extend or modify

Anchor improvements in the target's actual behavior and the user's objective.
Establish the baseline before choosing changes. Determine whether the request
asks for recommendations, a prototype, or implementation; continue through the
authorized action rather than substituting a critique for requested fixes.

## Find the useful change

Trace the relevant workflow or mechanism with the target guide. Identify concrete
friction, missing capability, error, inconsistency or measured performance issue.
For each opportunity record evidence, affected users/state, proposed change,
expected benefit, effort/dependencies and how success will be checked. Keep
observed problems separate from design hypotheses.

Use the available access to choose an implementation seam:

- Source available: locate the owning module/interface and existing conventions.
- Supported plugin/API/configuration: extend through that seam when it can deliver
  the requested result; check its real constraints.
- Artifact-only: investigate supported extension or compatible replacement;
  use controlled patching only within the authorized scope and with rollback.
- Hosted third-party product without write access: deliver concrete recommendations,
  a local prototype or an independent implementation when requested. Do not claim
  to have changed the live product.
- Document/method: revise structure, rules, calculations or presentation and
  validate the affected conclusions and examples.

## Implement and validate

Follow the destination's instructions and appropriate domain skill. For interface
work, use available design guidance and inspect actual interactions/states. For
performance, measure the relevant path and compare the same workload/environment.
For behavior changes, exercise the original failure or requirement and meaningful
regression cases. For document changes, check references, formulas and rendered
output as relevant. Avoid tests that merely repeat the new implementation.

Keep intended compatibility and necessary migrations explicit. Make reversible
edits, preserve the source artifact when patching, and document how to run/use the
result. Compare before and after on the target outcome, including any tradeoff.

## Deliverable and done

For recommendations, provide prioritized concrete changes and their evidence,
implementation seam and validation method. For implementation, deliver the changes,
actual verification and remaining constraints. When user testing or production
measurement is still needed, label it as future validation rather than a result.
