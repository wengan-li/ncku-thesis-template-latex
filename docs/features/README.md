# Shipped feature records

This directory contains the consolidated, maintained record of production
behavior. Current source and machine-checked tests remain authoritative.

## V2 production records

- [`v2-modernization.md`](v2-modernization.md) — product intent, compatibility
  boundary, architecture, hardened subsystems, and completion boundary.
- [`validation-and-performance.md`](validation-and-performance.md) — test and
  artifact contracts, release read-back evidence, benchmarks, and accepted,
  rejected, or deferred engineering decisions.
- [`release-and-distribution.md`](release-and-distribution.md) — versioning,
  package contents, GitHub Release promotion, Overleaf operation, retired sample
  repository, and Draft/watermark policy.

User migration instructions live in
[`../v1-to-v2-migration.md`](../v1-to-v2-migration.md). Student build and editing
instructions live in the packaged [`thesis/README.md`](../../thesis/README.md).

## Record policy

Feature records describe the released system, not the implementation queue.
Branch names, temporary no-push boundaries, checkbox progress, per-commit run IDs,
and duplicated validation narratives are intentionally left to Git history.
Durable compatibility numbers, architecture decisions, rejected experiments, and
publication boundaries remain here because they constrain future maintenance.

There are currently no active requirements. `docs/requirements/` therefore
contains only `.gitkeep`.
