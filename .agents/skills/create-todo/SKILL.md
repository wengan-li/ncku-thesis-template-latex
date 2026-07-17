---
name: create-todo
description: Use whenever creating a new todo tracker in this repo. Enforces the requirements-first rule — review docs/requirements/ and update or create the matching requirement file before writing the todo —
---

# Create Todo (repo workflow)

Owns the local paths and the requirements-first rule for this repo.

## Non-negotiable: review requirements first

1. Review `docs/requirements/` (start from its `README.md` index).
2. If a requirement covers this work, **update** it (scope, constraints,
   status).
3. If none covers it, **create** `docs/requirements/<NN>-<requirement>.md`
   before writing the todo.
4. Cross-link both ways: todo names its requirement file, requirement names
   its todo(s).

A requirement records *what* is wanted and *why*; the todo records *how* and
progress. Active requirements stay in `docs/requirements/`; completed
requirements and durable todo knowledge graduate into `docs/features/`.
Current user-facing state lives in `thesis/README.md`,
`docs/MIGRATION-1.x-TO-2.x.md`, and `CHANGELOG.md`.

## Local paths and numbering

- Todos: `todos/<NN>-<slug>.md` — two-digit sequence for active work. Create the
  directory when the next active todo starts.
- Requirements: `docs/requirements/<NN>-<slug>.md` — independent sequence.

## Completion lifecycle

When all acceptance and validation gates pass:

1. move the completed requirement and durable todo knowledge into one indexed
   `docs/features/<feature>/` record;
2. keep current usage/migration/release surfaces synchronized;
3. remove the completed todo and its active requirement entry;
4. let Git history preserve the chronological implementation narrative.

## Validate the mapping

```bash
grep -rhoE '`todos/[^`]+\.md`' docs/requirements/ | tr -d '`' | sort -u > /tmp/mapped
if [ -d todos ]; then
  (cd todos && find . -name '*.md' | sed 's|^\./|todos/|') | sort > /tmp/actual
else
  : > /tmp/actual
fi
comm -23 /tmp/mapped /tmp/actual   # broken refs — want empty
comm -13 /tmp/mapped /tmp/actual   # unmapped todos — want empty
```
