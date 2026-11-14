# Shared writing source implementation

[Requirement](../docs/requirements/04-shared-writing-source.md) · [Feature](../docs/features/student-writing-and-agent-skills.en.md)

## Intent

Replace the duplicate handbook with a deterministic projection of existing teaching code.

## Expectations

Preserve visible teaching output with comment-only marker seams. Compile the projected snippets and retain current safety, discovery, alias and language checks. Return a byte/mode manifest for the owner; no staging or commits.

## Context and progress

- Read approved handoff and required local context; clean source baseline confirmed.
- Existing English verbatim examples and runtime front matter/BibTeX provide a bounded shared seam. Markers outside verbatim add no displayed text.
- Baseline canonical check and PDF/text/geometry/fonts retained privately before source edits.
- Projection, consolidation, routes, current feature descriptions, 802 manifest and required drift gate implemented. The only generated artifact is references/template-usage.md; the duplicate usage tree is removed.
- Generation/drift mutations pass, including changed source flowing into actual reference bytes. Missing payload, language, alias, path, runtime, ownership and corrupted reference/citation cases are retained.
- Focused source/build/API/float/theorem/reference gates pass. The canonical 261-page teaching PDF retains exact text, normalized word geometry and meaningful fonts; four affected page rasters match. All teaching edits are comments only, and recorded inputs include every shared source.
- A mode/content-authenticated working-tree candidate ZIP passes extraction, direct default build, exact-fragment own-thesis and whole-context-copy builds. This is explicitly not committed-tree proof.
- Full just test and just ci both finish with exit 1 in the old HEAD package lanes: the committed ZIP lacks the new generated reference and its Overleaf copy still contains the removed usage handbook. Do not weaken those checks.
- Protected root subject-skill edits are prepared for the parent. Generic IDSD, runtime macros, entry/configuration and the real Git index remain unchanged.

## Remaining acceptance

Parent applies the protected subject-skill wording, checkpoints the exact candidate, then reruns just test/just ci and actual committed student/Overleaf package checks. Remove this todo and requirement only after that committed-source acceptance; current feature docs contain capabilities and procedures, not this execution record.
