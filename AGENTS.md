<!-- CODEGRAPH_START -->
## CodeGraph

In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE grep/find or reading files when you need to understand or locate code:

- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops grep can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.

If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
<!-- CODEGRAPH_END -->

Run `codegraph sync` at the start of a session and after large changes. The
index goes stale when its daemon idles, and a stale index answers from old code
without saying so.

# Repository instructions

Before implementation on every repository task, read
[IDSD](.agents/skills/idsd-workflow/SKILL.md), then
[repository maintenance](.agents/skills/repo-maintenance/SKILL.md).
Repository maintenance is the mandatory operating owner for compatibility,
validation, packaging, releases and action authority. Gather the current source
and the task's Intent, Expectations and Context before making changes.

Read the following owners whenever their tasks apply:

| Task | Required instructions |
| --- | --- |
| Documentation, requirements, todos, translation or path changes | [Documentation management](.agents/skills/documentation-management/SKILL.md) |
| Student-facing READMEs, defaults, teaching, release notes or packages | [Student first run](.agents/skills/student-first-run/SKILL.md) |
| Maintainer source lookup and graph readiness | [CodeGraph](.agents/skills/codegraph/SKILL.md) |
| Writing or revising conversational, documentation or commit prose | [Unslop](.agents/skills/unslop/SKILL.md), with the public voice rules in documentation management |

The [skill index](.agents/skills/README.md) routes these responsibilities.
For ordinary thesis writing, use the student project's
[writing skill](thesis/.agents/skills/ncku-thesis-writing/SKILL.md).

Work in the existing checkout and current branch. Branch/worktree creation,
switching, deletion or handoff to another checkout requires an explicit request
in the current conversation; a dirty/shared checkout is not authorization.
Preserve unrelated changes. If the work cannot proceed safely, stop before a
Git topology change and ask. Use subagents only when explicitly requested by
the user. Detailed Git and publication rules are mandatory in
[maintenance](.agents/skills/repo-maintenance/SKILL.md#git-and-external-actions).

AGENTS.md is canonical. Keep root CLAUDE.md as its relative symlink. Student
instructions grant no maintenance or publication authority; their package
[topology](.agents/skills/repo-maintenance/SKILL.md#student-package-topology)
and [audience rules](.agents/skills/student-first-run/SKILL.md#human-and-agent-guidance)
remain separate.
