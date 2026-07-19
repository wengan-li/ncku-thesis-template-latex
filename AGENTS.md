You must follow Intent-Driven Software Development (IDSD) for every task: clarify intent, expectations, and context first, and use the repo-local IDSD and repository-maintenance skills before implementation.

IDSD skill: `.agents/skills/idsd-workflow/SKILL.md`
Repository maintenance skill: `.agents/skills/repo-maintenance/SKILL.md`
Documentation management skill: `.agents/skills/documentation-management/SKILL.md`

# AGENTS.md

## Project

`ncku-thesis-template-latex` is a community-maintained XeLaTeX thesis/dissertation template for National Cheng Kung University.

- It is not an officially endorsed NCKU software project.
- Current department and university rules override template guidance.
- Preserve existing `thesis.tex`, `conf/conf.tex`, public commands, and visible layout unless a verified bug or official rule requires a documented change.
- XeLaTeX remains the supported engine for the 2.x line.

## V2 modernization outcome

V2 skipped a separate v1.9 release and delivered a compatibility-preserving
architecture that:

1. keeps the visible NCKU layout and top-level student project structure;
2. preserves every explicitly declared v1 command/environment throughout 2.x;
3. fixes proven helper defects with focused regression fixtures;
4. separates generic mechanisms from NCKU policy and institutional data;
5. restores the v1.5.0 other-institution customization boundary under
   `template/style/`, not `conf/`;
6. ships documented and tested 1.x-to-2.x migration steps;
7. keeps direct XeLaTeX and Overleaf builds authoritative.

Implement this outcome as small validated commits. A v2 version line does not
authorize a one-shot rewrite or an unverified visual redesign.

Post-release maintenance uses short-lived `feat/<short-name>` branches created
from current `main`. Merge each validated branch through a pull request, then
delete its local and remote refs after proving it has no commits unique to
`main`. `main` is the only persistent development branch; do not retain a
long-lived version integration branch.

## Canonical commands

Use `just`, not Makefile or ad-hoc public shell commands:

```bash
just                 # list recipes
just thesis          # build canonical thesis PDF + SyncTeX
just watch           # continuously rebuild changed thesis dependencies
just example         # build full teaching example document
just test            # required local and CI test gate
just check           # build and verify canonical artifacts
just ci              # complete local CI gate
just clean            # remove generated build output
```

`latexmk` is the internal XeLaTeX/BibTeX/rerun orchestrator behind `just`.

GitHub Actions must run:

```bash
just test
```

before a maintenance change or release is considered valid.

## Release asset contract

Every release must package artifacts from the exact tagged source. The intended custom public assets are exactly:

```text
ncku-thesis-template-latex-<version>.zip
ncku-thesis-template-latex-examples-<version>.zip
```

The custom release ZIP is the student-ready contents of `thesis/`, not a duplicate full-repository archive. It extracts to one `ncku-thesis-template-latex/` directory with `thesis.tex`, `conf/`, `context/`, `example/`, and `template/` directly inside. Repository tooling, tests, and a redundant `thesis/` wrapper must not be included; GitHub already provides automatic full-source archives.

The examples ZIP extracts to one stable `ncku-thesis-template-latex-examples/` directory containing its public README and the six verified PDFs. The outer archive carries the version; inner filenames remain stable and omit a redundant `example-` prefix. Loose generated PDFs are build intermediates and must not also be published as Release assets.

Generated master/doctoral defense-certificate examples may be published only inside the clearly documented generated-examples package. School-system-produced certificates are external official artifacts: do not regenerate, alter, or imply endorsement/ownership. The package README must tell current students to use the university degree-examination system's official files.

Do not commit generated PDFs or release ZIPs to the source tree. Build them under ignored output directories and upload them as GitHub Release assets.

## Sample repository migration

Source repository to retire:

```text
https://github.com/wengan-li/ncku-thesis-template-latex-sample
```

Before archive/deletion:

- record final sample commit and artifact SHA-256 values;
- replace main README links with release-asset links;
- verify every replacement PDF is generated from current tagged source;
- never merge unrelated sample history into the main source lineage;
- do not treat generated sample PDFs as source files;
- explicitly acknowledge that deletion breaks old URLs and changes the public fork-network root.

Archiving is safer than deletion. If deletion remains the explicit owner decision, complete every preservation and link-verification gate first.

## Build and output rules

- Source lives under `thesis/`.
- Generated local output lives under ignored `build/` or release staging directories.
- PDF and SyncTeX are required canonical outputs.
- A complete build must have no unresolved citations/references or rerun-required warning.
- Out-of-tree build paths must support TeX, BibTeX, figures, includes, and external PDFs.
- The full teaching document is integration coverage; small focused fixtures should be the normal fast test gate.
- Do not claim byte-identical PDFs across operating systems, TeX Live versions, or font installations.

## Compatibility and policy boundaries

- Do not silently switch to LuaLaTeX.
- Keep `tests/100-v1-public-api.json` passing; old commands may delegate to new
  internals, but their names and argument shapes remain available throughout
  2.x.
- Correct proven bugs rather than preserving them; document behavior changes in
  `docs/v1-to-v2-migration.md` and keep concise offline migration guidance in
  the packaged `thesis/README.md`.
- Keep `conf/` for student thesis data. Institution-level ports and style
  profiles remain under `template/style/`.
- NCKU college and department presets are runtime-owned by the selected `ncku`
  profile. Unchanged 1.x NCKU projects keep those commands through the default
  profile; `custom` and other institution profiles load only the generic
  institution metadata contract and must not inherit NCKU catalogue data.
- Do not migrate bibliography systems as part of the v2 profile extraction.
- Do not claim tagged PDF or PDF/UA compliance; current output is untagged.
- The ETDS upload path should not add internal watermark, DOI overlay, encryption, or security when current official guidance says the school system applies required processing.
- Prefer inserting the school-system defense certificate as an external file; keep generated certificate templates explicitly legacy/example only.
- Record official policy URL and checked date for any compliance change.

## Test source layout

- [`tests/000-test-suite.md`](tests/000-test-suite.md) is the test-inventory index.
- Keep every tracked test artifact directly under `tests/` with a unique
  three-digit sparse prefix. Use the documented `100–899` concern ranges for
  executable fixtures and manifests.
- The `900–999` range contains historical standalone investigation inputs. Those
  files are reference evidence, not automatic `just test` entrypoints.
- Keep semantic `just` recipe and output job names unnumbered. When a source file
  moves, update every script, document, and recipe path in the same change, then
  run `python3 scripts/test/check-test-layout.py` and `just test`.

## Verification

For source/build changes, run at minimum:

```bash
just test
just ci
git diff --check
```

For PDF-affecting changes also verify:

```bash
pdfinfo build/thesis.pdf
pdftotext build/thesis.pdf -
```

Render and inspect affected pages when cover, margins, pagination, front matter, certificate placement, or other visual layout can change.

## Git and artifact hygiene

- Check `git status --short` before staging.
- Stage only intended source/config/docs files.
- Do not commit generated PDFs, ZIPs, logs, SyncTeX, auxiliary files, local caches, secrets, or machine-specific config.
- Use Conventional Commits.
- Keep visible-output fixes separate from pure tooling/refactor commits.
- Push verified completed slices to the feature branch.

## Agent setup

- `AGENTS.md` is canonical.
- `CLAUDE.md` points here and stays short.
- Repo-local skills are `.agents/skills/idsd-workflow/`,
  `.agents/skills/repo-maintenance/`, and
  `.agents/skills/documentation-management/`.
- `.claude/skills` is a symlink to `../.agents/skills`.
- `.claude/settings.json` contains only repo-safe Claude Code settings; never store credentials.

## Documentation Standard

- `docs/README.md` is the public project-documentation index and audience router.
- `docs/v1-to-v2-migration.md` is the current 1.x-to-2.x migration guide;
  `thesis/README.md` keeps concise offline steps and `thesis/conf/README.md`
  keeps field-by-field configuration guidance inside the student ZIP.
- `docs/features/` contains consolidated shipped architecture, validation, and
  operating decisions. Do not keep one active document per branch, commit, todo,
  parser, or bugfix; Git history preserves that chronology.
- `docs/requirements/` contains active owner-approved what/why promises only.
  When none are active, it contains exactly `.gitkeep`.
- `todos/` contains active how/progress only. On completion, promote durable
  knowledge into the owning feature record and remove the requirement/todo.
- Current source and tests win on drift. Deferred experiments are not active
  requirements without a new owner-approved Intent.
- Student/public journeys are complete in formal Taiwan Traditional Chinese and
  natural technical English. Use one predominant language per file with a
  top-of-page text switcher to the equivalent language file; do not use repeated
  per-section language labels or flags.
- Public project actions use third-person `本模版` / `本專案` and `the template` /
  `the project` wording. General processes use role-neutral wording. Chinese references
  to cross-institution readers use `其他學校的同學`; English uses `students from
  other institutions`.
- Paired user guides carry hidden stable topic IDs. Keep paired executable code
  blocks identical and validate links in both files so split-language pages do
  not silently drift.
- Maintainer feature records use a canonical English technical record plus a
  separate Traditional-Chinese executive-summary companion. Do not duplicate
  hashes, run IDs, or benchmark transcripts merely to claim line-by-line
  translation.
- Documentation language, institution profile, cover language, degree, and
  content mode are independent axes. Do not map English readers to `custom` or
  Traditional-Chinese readers to `ncku`.
- Use exact `LaTeX`, `XeLaTeX`, `BibTeX`, `latexmk`, and `SyncTeX` casing and
  `論文範本` in new Chinese prose. Run
  `python3 scripts/test/check-bilingual-docs.py`; its structural result does not
  replace human semantic-parity review.
- Load `documentation-management` for documentation creation, consolidation,
  requirements, todos, path repair, or lifecycle changes.
