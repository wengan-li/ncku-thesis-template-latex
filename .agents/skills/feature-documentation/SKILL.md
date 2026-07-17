---
name: feature-documentation
description: |-
  A thesis-template capability just got built, changed, or asked about — capture its
  lasting record. Use this skill to write or refresh a feature's three docs:
  technical notes, user/operator guide, and contract reference. Trigger when
  someone finished/shipped a template macro/environment, class option, build recipe, or packaged sample and wants it written up; asks whether something is
  documented; says "document this" / "update the docs"; or changed code that
  existing docs describe. Skip pure code hygiene (comments, tests,
  formatting).
---

# Feature Documentation Standard

This repo's shipped-state docs are `thesis/README.md` (template usage),
`thesis/MIGRATION-1.x-TO-2.x.md`, `CHANGELOG.md`, and the decision/policy
records under `docs/`. Keep them true to the shipped template — update
whichever a change reaches; no separate `docs/features/` tree here.

| Doc | Role |
| --- | --- |
| `thesis/README.md` | Template usage — options, macros, build. |
| `thesis/MIGRATION-1.x-TO-2.x.md` | v1→v2 migration contract. |
| `docs/<record>.md` | Decision/policy/history records (versioning, watermark, Overleaf, API compatibility). |

## Rules

- **Ground truth = code**: LaTeX sources under `thesis/` (`.tex`,
  `.sty`, conf), plus `justfile`/`scripts/` recipes and `tests/`. When a
  record contradicts the source, document the source and note the gap.
  Anchor claims as `` `thesis/template/libs/file.sty` → `\\macro` (:line) ``.
- Scope from the **diff**, not the task title; grep `docs/` for
  every changed symbol/flag/table name and update every doc a change reaches.
- Diagram real state machines only (`mermaid stateDiagram-v2`), grounded in
  actual states, citations underneath.
- Preserve troubleshooting tables (symptom → cause) through rewrites.
- State known limitations plainly; bugs found while documenting also get a
  todo (via `create-todo`).
- Match the existing docs' voice; update `docs/README.md` when a doc is
  added or renamed.
- Requirements (`docs/requirements/`) record what/why; feature docs record
  what shipped.

## The guardrail hook (wired repo-wide)

[`hooks/check-feature-docs.sh`](hooks/check-feature-docs.sh) runs as a
non-blocking Stop hook via the committed `.claude/settings.json` (command path: the tool-neutral `.agents/hooks/` registry symlink): new LaTeX source
under `thesis/` with no `docs/`, `docs/requirements/`, or `todos/` update → one reminder. Never blocks.
