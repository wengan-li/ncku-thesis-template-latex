<!--
TEMPLATE: api.md — the CONTRACT reference: MCP tools, gateway endpoints, SQL
tables/functions, crate public APIs, message shapes.
Copy to docs/features/<module>/api.md. Contract shape only — not
implementation (technical.md), not workflow (user-guide.md). If the feature
owns no contract surface, omit this file and say so in technical.md.
-->

# <Feature Name> — Contract Reference

> **Related:** [User guide](./user-guide.md) · [Technical](./technical.md)

## Surface summary

| Contract | Kind | Consumer(s) | Purpose |
| --- | --- | --- | --- |
| `<tool_name>` | MCP tool | agents | … |
| `<METHOD /path>` | gateway endpoint | edge/portal | … |
| `<table / fn_*>` | SQL | services | … |
| `<pub fn / trait>` | crate API | other crates | … |

---

## `<contract>` — <kind>

- **Definition:** `thesis/template/libs/<file>.sty` → `<symbol>` (:line), or
  `sql/<file>.sql` → `<name>`.
- **Auth / tenancy:** who may call it; how identity is carried.
- **Shape:** params/fields, types, invariants; note streaming/pagination.
- **Errors / rejection:** exact error shape the caller sees.

Repeat per contract. Exact names verified against code, not memory.
