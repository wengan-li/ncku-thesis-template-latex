# Documentation

This directory is the maintainer documentation for the released NCKU Thesis
Template. The current production release is
[`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734).

## Start here

| Audience or task | Canonical document |
| --- | --- |
| Students building or editing a thesis | [`thesis/README.md`](../thesis/README.md) |
| Existing 1.x projects moving to 2.x | [`v1-to-v2-migration.md`](v1-to-v2-migration.md) |
| Maintainers reviewing shipped architecture | [`features/v2-modernization.md`](features/v2-modernization.md) |
| Maintainers reviewing tests, output proof, or performance decisions | [`features/validation-and-performance.md`](features/validation-and-performance.md) |
| Maintainers building releases or handling Overleaf | [`features/release-and-distribution.md`](features/release-and-distribution.md) |
| Version history and user-visible changes | [`CHANGELOG.md`](../CHANGELOG.md) |
| Active bilingual-documentation work | [Requirement 02](requirements/02-bilingual-documentation.md) and [Todo 01](../todos/01-bilingual-documentation.md) |

The root [`README.md`](../README.md) is the public project overview. It routes
users to the student package and latest release; it is not the maintainer
runbook.

## Directory model

```text
docs/
  README.md
  v1-to-v2-migration.md
  features/
    README.md
    v2-modernization.md
    validation-and-performance.md
    release-and-distribution.md
  requirements/
    .gitkeep
    02-bilingual-documentation.md
```

- `v1-to-v2-migration.md` is the current user-facing migration contract.
- `features/` contains consolidated records of shipped behavior and durable
  engineering decisions. It does not preserve one file per branch, commit, todo,
  or implementation slice; Git history keeps that chronology.
- `requirements/` contains only active owner-approved what/why promises. The
  current bilingual-documentation requirement is linked to its implementation
  todo; `.gitkeep` retains the directory after active requirements graduate.
- Active implementation progress, when needed, belongs in root-level `todos/` and
  is removed after completion.

## Documentation lifecycle

1. Start from an owner-approved Intent.
2. Add `docs/requirements/<NN>-<slug>.md` only while a real promise remains
   active; do not create speculative backlog documents.
3. Use `todos/<NN>-<slug>.md` for active implementation progress and link it to
   the requirement.
4. When the work ships, update the appropriate current user surface and
   consolidate durable knowledge into an existing topical record under
   `docs/features/` (or create one only for a genuinely new capability family).
5. Remove the completed requirement and todo. Git history retains the work
   sequence and superseded branch-specific constraints.
6. Keep `docs/features/README.md`, this index, the migration guide, changelog, and
   packaged student README synchronized with the source they describe.

## Source-of-truth order

When documents disagree, resolve the difference in this order:

1. current tracked source, tests, scripts, and `justfile`;
2. immutable release tag and publicly re-downloaded release assets;
3. current user and maintainer documentation;
4. historical Git commits, PRs, and removed implementation notes.

Historical evidence explains why a decision was made, but it must not override
current tested behavior or reopen completed work. Deferred experiments are not
active requirements without a new owner-approved Intent.

## Current state

- Production source line: V2, XeLaTeX, direct `latexmk` student build.
- Latest immutable release: `v2.0.1.260719010734`.
- Active requirement: [bilingual documentation for Traditional-Chinese and
  English readers](requirements/02-bilingual-documentation.md), with progress
  tracked in [Todo 01](../todos/01-bilingual-documentation.md).
- Persistent development branch: `main` only; work uses short-lived
  `feat/<short-name>` branches.
- GitHub Releases is the canonical latest package while any Overleaf Gallery
  update remains unapproved or not independently read back.
