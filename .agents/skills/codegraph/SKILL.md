---
name: codegraph
description: Use for maintainer source lookup and CodeGraph readiness in this repository; not for student thesis writing.
---

# Maintainer CodeGraph lookup

## Scope and authority

CodeGraph is optional local assistance for maintained Python validation tooling
and file-level YAML discovery. It is not a LaTeX macro/include graph, a required
student dependency, or a selective-test correctness oracle. Ordinary writing
uses the [portable student skill](../../../thesis/.agents/skills/ncku-thesis-writing/SKILL.md).

Read root `AGENTS.md` and the [repository maintenance skill](../repo-maintenance/SKILL.md)
first. Root `codegraph.json` excludes student content, templates, fixtures,
documentation, agent instructions and generated output. Preserve those
exclusions; empty results outside this scope are expected, not proof of absence.

## Verify and use

From the repository root, inspect the installed implementation and readiness:

```bash
codegraph --version
DO_NOT_TRACK=1 CODEGRAPH_TELEMETRY=0 CODEGRAPH_NO_UPDATE_CHECK=1 codegraph status --json
DO_NOT_TRACK=1 CODEGRAPH_TELEMETRY=0 CODEGRAPH_NO_UPDATE_CHECK=1 codegraph files --json
```

If an existing index is healthy, synchronize at session entry and after material
changes before trusting its responses:

```bash
DO_NOT_TRACK=1 CODEGRAPH_TELEMETRY=0 CODEGRAPH_NO_UPDATE_CHECK=1 codegraph sync
DO_NOT_TRACK=1 CODEGRAPH_TELEMETRY=0 CODEGRAPH_NO_UPDATE_CHECK=1 codegraph explore check_guide_pair check_active_work_directory
```

Compare returned symbols with current source. Record actual version and indexed
paths rather than assuming every file is covered. For `InsertFigure` or other
TeX questions, use focused source reads under `thesis/template/command/`, the
existing public-API manifest and regression fixtures. Runtime `.fls` records
prove loaded dependencies; they do not turn the graph into TeX semantic analysis.

## Setup and recovery boundary

A missing index is not permission to initialize, upgrade, unlock, alter hooks,
change watch policy, register MCP clients or restart a daemon. Obtain applicable
setup authority; inspect the selected installed `init --help` and its write paths
before initialization. In particular, noninteractive initialization can install
Git sync hooks when watching is disabled. Preserve existing instruction, hook,
client and settings bytes. Report a blocked/busy/stale index and continue with
ordinary source tools instead of broadening permissions or ignoring a live lock.

Keep `.codegraph/` ignored, including database/WAL/SHM/locks and local metadata.
Never include graph state in student or Overleaf archives. Do not map `.tex` to
an unrelated language parser to manufacture coverage. CLI query readiness does
not establish MCP registration or a client's runtime discovery.

Current coverage boundaries and supported feature behavior belong in
[the feature description](../../../docs/features/student-writing-and-agent-skills.en.md).
Keep execution receipts, index snapshots and session chronology out of current
feature documentation; Git history preserves prior versions.
