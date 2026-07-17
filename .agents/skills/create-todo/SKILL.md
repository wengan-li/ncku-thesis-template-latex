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
progress; shipped-state docs are `thesis/README.md` + `CHANGELOG.md` + `docs/`
records.

## Local paths and numbering

- Todos: `todos/<NN>-<slug>.md` — two-digit sequence for new todos;
  existing `v2-<slug>.md` files are grandfathered.
- Requirements: `docs/requirements/<NN>-<slug>.md` — independent sequence.

## Validate the mapping

```bash
grep -rhoE '`todos/[^`]+\.md`' docs/requirements/ | tr -d '`' | sort -u > /tmp/mapped
(cd todos && find . -name '*.md' | sed 's|^\./|todos/|') | sort > /tmp/actual
comm -23 /tmp/mapped /tmp/actual   # broken refs — want empty
comm -13 /tmp/mapped /tmp/actual   # unmapped todos — want empty
```
