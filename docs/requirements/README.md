# Requirements

Durable product/engineering requirements. A requirement records *what* is
wanted and *why*; todos under `todos/` record *how* and progress.
Shipped-state docs: `thesis/README.md`, `thesis/MIGRATION-1.x-TO-2.x.md`,
`CHANGELOG.md`. Decision/policy/history records stay under `docs/`
(watermark policy, Overleaf distribution, release versioning, sample-repo
migration, optimization review, the v2 IDSD brief, v1-API compatibility).
Every todo maps to exactly one primary requirement.

Conventions (owned by `.agents/skills/create-todo/SKILL.md`):

- File: `docs/requirements/<NN>-<requirement>.md` — next number = highest
  existing + 1.
- Creating a todo starts with reviewing this tree — update the matching
  requirement or create a new one, then cross-link both ways.

| # | Requirement |
| --- | --- |
| [01](01-v2-modernization.md) | V2 template modernization |
