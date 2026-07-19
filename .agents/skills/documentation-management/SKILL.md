---
name: documentation-management
description: Use for repository documentation lifecycle and consolidation.
---

# Documentation management

## When to use

Use for creating, reorganizing, consolidating, or validating repository
documentation; creating requirements or todos; documenting shipped behavior; and
repairing documentation paths after a source or release change.

Load the sibling [`idsd-workflow`](../idsd-workflow/SKILL.md) first. Load
[`repo-maintenance`](../repo-maintenance/SKILL.md) when source, tests, packaging,
CI, releases, or public distribution are involved.

## Canonical surfaces

| Surface | Role |
| --- | --- |
| [`docs/README.md`](../../../docs/README.md) | Project documentation index and lifecycle. |
| [`docs/v1-to-v2-migration.md`](../../../docs/v1-to-v2-migration.md) | Current 1.x to 2.x user migration contract. |
| [`docs/features/`](../../../docs/features/) | Consolidated shipped architecture, evidence, and operating decisions. |
| `docs/requirements/<NN>-<slug>.md` | Active owner-approved what/why promise only. |
| `todos/<NN>-<slug>.md` | Active implementation progress only. |
| [`thesis/README.md`](../../../thesis/README.md) | Instructions that ship inside the student ZIP. |
| [`CHANGELOG.md`](../../../CHANGELOG.md) | Release index and user-visible changes. |
| [`README.md`](../../../README.md) | Public project overview and audience routing. |

Current source, tests, scripts, and immutable release assets win on drift.
Historical commits and removed implementation notes explain decisions but do not
reopen work.

## Requirements and todos

1. Start from an owner-approved Intent; do not convert ideas or deferred
   experiments into active requirements.
2. Read `docs/README.md` and the relevant current feature record.
3. If a real promise is active, create the next
   `docs/requirements/<NN>-<slug>.md` with Intent, constraints, failure
   conditions, acceptance boundary, and links to active todos.
4. Use root `todos/<NN>-<slug>.md` for implementation sequence and progress. Keep
   requirement and todo backlinks synchronized.
5. When no active requirement exists, keep `docs/requirements/` empty except for
   `.gitkeep`; do not add a README just to explain emptiness.

## Completion lifecycle

When all acceptance and validation gates pass:

1. update every current user surface reached by the change;
2. consolidate durable knowledge into an existing topical file under
   `docs/features/` whenever possible;
3. create a new feature record only for a genuinely new capability family, not
   for each branch, commit, parser, or bugfix;
4. update `docs/features/README.md` and `docs/README.md`;
5. remove completed requirement and todo files;
6. let Git history retain checklists, temporary branch boundaries, per-commit run
   IDs, and superseded implementation narratives.

## Heavy consolidation

Classify every source document before deleting it:

- **current user contract** — preserve in student README, migration guide, or
  changelog;
- **current project contract** — preserve in a topical feature/operation
  record and repo-maintenance skill;
- **durable shipped evidence** — summarize in the owning feature record;
- **measured rejected/deferred decision** — retain the conclusion and reopening
  gate, not the whole progress log;
- **implementation chronology** — leave to Git history after durable knowledge is
  promoted;
- **stale duplicate** — remove after repairing backlinks.

Do not create one giant catch-all file merely to reduce file count. Prefer a
small topical set with one owner per fact. Do not retain the same release command,
compatibility number, or publication status in several active documents unless
one is a short link/routing sentence.

## Audience and package boundary

- Students receive the exact `thesis/` subtree as their package. Direct compiler,
  editor, configuration, and migration-start instructions must be available
  there without repository-only tooling.
- Repository-only commands, tests, benchmarks, workflow details, and internal evidence
  stay outside the student ZIP.
- Root README routes audiences; `docs/README.md` owns the internal index.
- GitHub Release state and Overleaf state are independent. Never turn submitted
  into approved without live public read-back.

## Bilingual documentation model

- Student/public journeys are complete in formal Taiwan Traditional Chinese
  (`zh-Hant-TW`) and natural technical English. Use one predominant language per
  file and a top-of-page text switcher to the equivalent page. Default `*.md`
  user journeys are Traditional Chinese; English companions use `*.en.md`.
- Do not repeat visible `繁體中文` / `English` labels inside every section and do
  not use flags as language controls. Each language link uses its native name.
- Paired guides carry one hidden `doc-pair`, `lang`, and stable `topics` marker.
  The deterministic checker requires pair metadata, reciprocal switchers,
  equivalent topic IDs, valid local links, and identical fenced code blocks.
- Project feature records use a canonical English technical record plus a
  separate `*.zh-TW.md` executive-summary companion. This is intentionally not a
  line-by-line translation of hashes, run IDs, benchmarks, or evidence
  transcripts.
- `CHANGELOG.md` remains the canonical complete release history. Current localized
  V2 notes live in `CHANGELOG.zh-TW.md`; historical mixed-language entries are
  retained rather than rewritten.
- Documentation language, institution profile, cover language, degree, and
  content mode are independent. An English reader can use `ncku`; a
  Traditional-Chinese reader can maintain another profile.
- Public project actions use the owner's first-person `我` / `I` voice; general
  workflow uses role-neutral project or repository wording. Refer to Chinese
  cross-institution readers as `其他學校的同學` and English readers as `students
  from other institutions`.
- Use exact `LaTeX`, `XeLaTeX`, `BibTeX`, `latexmk`, and `SyncTeX` casing. Use
  `論文範本` in new Chinese prose. Avoid Cantonese-only wording in shipped docs.
- Keep `thesis/conf/conf.tex` byte-identical throughout 2.x. Its bilingual
  companion is `thesis/conf/README.md`; never refresh the V1 migration baseline
  merely to translate comments.
- Mechanical checks prove structure, links, casing, and selected terminology
  only. Human review must still verify that warnings, actions, defaults, and
  exceptions mean the same thing in both languages.

This model follows authoritative public patterns:

- [W3C internationalization techniques](https://www.w3.org/International/techniques/authoring-html)
  recommend linking users to each localized page even when language negotiation
  exists.
- [USWDS two-language guidance](https://designsystem.digital.gov/patterns/select-a-language/two-languages/)
  uses a prominent text language selector that opens an equivalent page and
  explicitly advises against flags.
- [GitHub Docs translation guidance](https://docs.github.com/en/contributing/writing-for-github-docs/writing-content-to-be-translated)
  treats translations as locale-specific documentation and recommends clear,
  translation-friendly source prose.
- [WCAG 2.2 language-of-page guidance](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html)
  requires a programmatically determinable predominant page language; separate
  Markdown files approximate that model better than paragraph-by-paragraph
  alternation.

## Validation

For documentation-only changes:

```bash
python3 scripts/test/check-bilingual-docs.py
git diff --check
git status --short
```

Also validate mechanically:

- every relative Markdown link resolves from its owning file;
- every removed/renamed path has zero stale first-party references;
- `docs/requirements/` contains exactly `.gitkeep` when no requirement is active;
- `docs/features/README.md` indexes every current feature record;
- repo instructions and local skills name the new canonical paths;
- student-package links point to public repository paths that exist on `main`;
- no generated artifact, secret-like file, or local tool state is staged.

Run `just test`/`just ci` when repository policy requires the exact committed tree
or when package-facing paths, scripts, tests, or source are touched. If a gate
reads `HEAD`, validate the staged tree in a temporary commit/worktree before the
real commit rather than weakening the gate.

## Non-blocking reminder

[`hooks/check-documentation.sh`](hooks/check-documentation.sh) is wired through
`.agents/hooks/check-documentation.sh` and `.claude/settings.json`. It emits one
non-blocking reminder when a new template source file is added without a docs,
requirements, or todo update. It is a prompt, not proof that documentation is
complete.
