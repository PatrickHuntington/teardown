# Source, APIs, protocols, datasets and captures

## Source repositories and libraries

Read applicable project instructions. Record repository revision and local
changes. Inspect manifests, dependency locks, entry points, build/runtime
configuration and tests; trace the requested behavior through actual code.
Separate direct dependencies from transitive ones, declared from executed paths,
and test mocks from deployed services. Look at data migrations, background jobs,
authorization and integration boundaries where they affect the question.

Use source directly. Introduce binary analysis only when shipped behavior, a
closed dependency or a source/binary mismatch requires it. For architectural
understanding, identify modules, responsibilities, state and dependency flow.
For changes, find the seam and existing validation workflow before implementing.
Execute project code/tests only in the appropriate authorized environment.

## APIs and protocols

Establish the selected version, endpoint/service boundary and access. Start with
published specifications, SDKs, examples and supplied captures. Map requests,
responses, schemas, auth requirements, state transitions, errors, limits,
pagination, ordering, retries/idempotency and webhooks as relevant.

Use small authorized probes to resolve consequential ambiguity. Record exact
inputs/outputs with credentials removed, and distinguish a declared contract
from observed behavior. Live requests that create resources, incur charges,
send messages or alter records need authorization already covering that effect.
Do not invent a backend implementation from an external API shape.

For compatibility work, create independent contract cases covering successful,
invalid and boundary inputs. Record version negotiation, encoding/serialization,
timing and failure semantics when they matter. Treat undocumented interfaces
as unstable unless evidence establishes otherwise.

## Data and learned systems

Identify provenance, schema, size, version, units, missingness and license/access
conditions. Inspect representative samples and distributions, including edge
cases. Trace transformations, joins, labels and outputs. Distinguish correlations
from causal explanations, and data/model availability from reproducibility.

For a model or notebook, examine preprocessing, inference/training boundaries,
evaluation data, metrics and environment. If replication is requested, identify
which data/weights/configuration are actually obtainable. Test on independent
representative examples; a successful toy example cannot establish production
quality or proprietary training history.

## Saved traffic and execution evidence

HAR/packet captures, logs, core dumps and traces establish historical events for
the recorded target/configuration. Preserve timestamps, record ordinals,
module/process identity and completeness limits. Parse before drawing conclusions;
exclude secrets and unrelated traffic from exported reports. Recorded URLs,
PIDs and commands do not select live targets or authorize replay/attachment.

Compare captures or versions using matched scenarios. Separate changed behavior
from changed data, environment, instrumentation and incomplete recording. If a
requested explanation cannot be established, name the next discriminating
observation rather than supply a plausible internal implementation.
