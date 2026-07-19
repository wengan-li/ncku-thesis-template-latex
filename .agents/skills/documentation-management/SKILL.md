---
name: documentation-management
description: Use for repository documentation lifecycle and consolidation.
---

# Documentation management

## When to use

Use for creating, reorganizing, consolidating, or validating repository
documentation; creating requirements or todos; documenting shipped behavior; and
repairing documentation paths after a source or release change.

Load the sibling [`idsd-workflow`](../idsd-workflow/SKILL.md) first. Load
[`repo-maintenance`](../repo-maintenance/SKILL.md) when source, tests, packaging,
CI, releases, or public distribution are involved.

## Canonical surfaces

| Surface | Role |
| --- | --- |
| [`docs/README.md`](../../../docs/README.md) | Maintainer documentation index and lifecycle. |
| [`docs/v1-to-v2-migration.md`](../../../docs/v1-to-v2-migration.md) | Current 1.x to 2.x user migration contract. |
| [`docs/features/`](../../../docs/features/) | Consolidated shipped architecture, evidence, and operating decisions. |
| `docs/requirements/<NN>-<slug>.md` | Active owner-approved what/why promise only. |
| `todos/<NN>-<slug>.md` | Active implementation progress only. |
| [`thesis/README.md`](../../../thesis/README.md) | Instructions that ship inside the student ZIP. |
| [`CHANGELOG.md`](../../../CHANGELOG.md) | Release index and user-visible changes. |
| [`README.md`](../../../README.md) | Public project overview and audience routing. |

Current source, tests, scripts, and immutable release assets win on drift.
Historical commits and removed implementation notes explain decisions but do not
reopen work.

## Requirements and todos

1. Start from an owner-approved Intent; do not convert ideas or deferred
   experiments into active requirements.
2. Read `docs/README.md` and the relevant current feature record.
3. If a real promise is active, create the next
   `docs/requirements/<NN>-<slug>.md` with Intent, constraints, failure
   conditions, acceptance boundary, and links to active todos.
4. Use root `todos/<NN>-<slug>.md` for implementation sequence and progress. Keep
   requirement and todo backlinks synchronized.
5. When no active requirement exists, keep `docs/requirements/` empty except for
   `.gitkeep`; do not add a README just to explain emptiness.

## Completion lifecycle

When all acceptance and validation gates pass:

1. update every current user surface reached by the change;
2. consolidate durable knowledge into an existing topical file under
   `docs/features/` whenever possible;
3. create a new feature record only for a genuinely new capability family, not
   for each branch, commit, parser, or bugfix;
4. update `docs/features/README.md` and `docs/README.md`;
5. remove completed requirement and todo files;
6. let Git history retain checklists, temporary branch boundaries, per-commit run
   IDs, and superseded implementation narratives.

## Heavy consolidation

Classify every source document before deleting it:

- **current user contract** — preserve in student README, migration guide, or
  changelog;
- **current maintainer contract** — preserve in a topical feature/operation
  record and repo-maintenance skill;
- **durable shipped evidence** — summarize in the owning feature record;
- **measured rejected/deferred decision** — retain the conclusion and reopening
  gate, not the whole progress log;
- **implementation chronology** — leave to Git history after durable knowledge is
  promoted;
- **stale duplicate** — remove after repairing backlinks.

Do not create one giant catch-all file merely to reduce file count. Prefer a
small topical set with one owner per fact. Do not retain the same release command,
compatibility number, or publication status in several active documents unless
one is a short link/routing sentence.

## Audience and package boundary

- Students receive the exact `thesis/` subtree as their package. Direct compiler,
  editor, configuration, and migration-start instructions must be available
  there without repository-only tooling.
- Maintainer commands, tests, benchmarks, workflow details, and internal evidence
  stay outside the student ZIP.
- Root README routes audiences; `docs/README.md` owns the internal index.
- GitHub Release state and Overleaf state are independent. Never turn submitted
  into approved without live public read-back.

## Validation

For documentation-only changes:

```bash
git diff --check
git status --short
```

Also validate mechanically:

- every relative Markdown link resolves from its owning file;
- every removed/renamed path has zero stale first-party references;
- `docs/requirements/` contains exactly `.gitkeep` when no requirement is active;
- `docs/features/README.md` indexes every current feature record;
- repo instructions and local skills name the new canonical paths;
- student-package links point to public repository paths that exist on `main`;
- no generated artifact, secret-like file, or local tool state is staged.

Run `just test`/`just ci` when repository policy requires the exact committed tree
or when package-facing paths, scripts, tests, or source are touched. If a gate
reads `HEAD`, validate the staged tree in a temporary commit/worktree before the
real commit rather than weakening the gate.

## Non-blocking reminder

[`hooks/check-documentation.sh`](hooks/check-documentation.sh) is wired through
`.agents/hooks/check-documentation.sh` and `.claude/settings.json`. It emits one
non-blocking reminder when a new template source file is added without a docs,
requirements, or todo update. It is a prompt, not proof that documentation is
complete.
