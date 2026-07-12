# IDSD Brief Template

Use existing repository conventions when they carry automation meaning.

```markdown
# <Outcome>

Status:
Owner:
Last updated:
Method: IDSD

## Intent

### Goal

### Constraints

### Failure Conditions

## Expectations

### Done Means

### Success Scenarios

### Recovery Plan

### Review Checkpoints

### Validation

## Context

### Current Evidence

### Connections

### Source Links

### Assumptions And Open Questions

## Progress

## Learnings
```

Keep ceremony proportional to risk:

- Trivial work needs no durable brief.
- Non-trivial work should update the existing planning system.
- High-risk work needs explicit checkpoints, rollback or recovery, and evidence.
- A document already named spec may keep its name; separate new Intent,
  Expectations, and Context inside it.
- Keep implementation detail in Context unless user requires it as outcome.
- Update progress during work, not only at final handoff.
