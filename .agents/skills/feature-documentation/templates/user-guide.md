<!--
TEMPLATE: user-guide.md — the task-oriented guide for whoever USES the
feature: a student using the template, or an agent driving it.
Copy to docs/features/<module>/user-guide.md and fill each section.
Steps/commands verified against the shipped code; contracts live in api.md.
-->

# <Feature Name> — User Guide

> **Related:** [Contracts](./api.md) · [Technical](./technical.md)

## What you can do

Two or three sentences: the job this capability does and the typical flow.

## Prerequisites

- **Runtime:** which binary/service must run (`just <recipe>` /
  `apps/<app>`), and any daemon/tray state.
- **Configuration:** env vars, paths, credentials source.

## <Task 1 — e.g. "Search memory from the portal">

1. Exact command or UI steps.
2. What success looks like (output, UI state, rows).

## <Task 2 — the next task in the flow>

## Good to know

Restart/resume behavior, idempotency, eventual consistency, offline
behavior.

## Troubleshooting

| Symptom | Likely cause | Where to look |
| --- | --- | --- |

## Known limitations

In user terms — so people plan around gaps instead of filing them as bugs.
