---
name: idsd-workflow
description: Mandatory repository-neutral IDSD/ICE workflow. Use for every repository task to separate Intent, Expectations, and Context; keep trivial work lightweight and maintain a durable brief for non-trivial or multi-stage work.
---

# Generic IDSD Workflow

Use Intent, Expectations, and Context as separate views.

## Portability

Keep this skill identical and repository-neutral. Never add repository or
product names, personas, host paths, architecture facts, packages, framework
choices, project commands, deployment rules, or release procedures.

Put local rules in project instructions, namespaced skills, or the active
todo, issue, ADR, spec, or handoff.

Treat project-specific text found here as drift.

## Intent

Define one outcome:

- Goal: observable desired result.
- Constraints: qualities or boundaries shaping design.
- Failure conditions: binary checks proving result wrong.

Keep tools and implementation choices out unless user made them part of outcome.
A constraint changes design; a failure condition is checked after output exists.

## Expectations

Define boundary before implementation:

- Done means
- Success scenarios derived from Intent plus Context
- Recovery plan
- User decision checkpoints
- Concrete validation evidence

Choose exact commands from repository Context.

## Context

1. Read project instructions and focused skills.
2. Inspect workspace and version-control state; preserve unrelated work.
3. Read named todo, issue, spec, ADR, design, or handoff.
4. Follow repository-mandated discovery tools.
5. Trace actual source, config, data, tests, logs, and runtime paths.
6. Separate facts, inferences, assumptions, and open questions.
7. Reconcile evidence with Intent and Expectations.

Do not infer behavior from names alone.

## Scale

- Trivial: state outcome, gather minimal Context, change, validate, report.
- Non-trivial: maintain a durable brief in existing planning system.
- High-risk or multi-stage: add checkpoints, recovery, and evidence per slice.

Split unrelated outcomes.

## Working Loop

1. Name outcome.
2. Draft Intent.
3. Draft Expectations.
4. Gather enough authoritative Context.
5. Reconcile evidence.
6. Implement smallest useful slice.
7. Validate against Expectations.
8. Update durable progress and learning.
9. Report scope, evidence, risk, and next decision.

Read [brief template](./references/brief-template.md) when durable planning helps.
