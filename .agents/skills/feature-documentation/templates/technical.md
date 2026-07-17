<!--
TEMPLATE: technical.md — for engineers and future agents.
Copy to docs/features/<module>/technical.md and fill each section.
Anchor claims as `thesis/template/libs/<file>.sty` → `symbol` (:line).
-->

# <Feature Name> — Technical Documentation

> **Status:** <Shipped | In progress | MVP> ·
> **Related:** [User guide](./user-guide.md) · [Contracts](./api.md) ·
> **Requirement:** `docs/requirements/<NN>-<slug>.md` ·
> **Requirement:** `docs/requirements/<NN>-<slug>.md` (where one applies)

## Overview

One or two sentences: what this capability is and why it exists.

## Architecture

The dataflow: caller (agent/UI/gateway) → crate/service → storage
(SQL/memory) → response/event. A numbered flow or small mermaid flowchart
beats prose.

## Status lifecycle

Diagram real state machines only, grounded in actual states, citations
underneath.

## Files

| File | Role |
| --- | --- |
| `apps/<app>/src/<x>.rs` | Service / binary |
| `thesis/conf/<x>.tex` | Template configuration |
| `sql/<x>.sql` | Tables / functions |
| `justfile` → `<recipe>` | Entry point |

## Key decisions

Non-obvious choices and *why*.

## Gotchas & traps

Concurrency/ordering requirements, restart behavior, platform edges,
places where the obvious change breaks something else.

## Known limitations

Stated plainly. Bugs found while documenting also get a todo.

## How to extend

Likely next changes and where to make them safely. Name the gates to run.
