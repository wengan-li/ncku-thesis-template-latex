You must follow Intent-Driven Software Development (IDSD) for every task: clarify intent, expectations, and context first, and use the repo-local IDSD and repository-maintenance skills before implementation.

IDSD skill: `.agents/skills/idsd-workflow/SKILL.md`
Repository maintenance skill: `.agents/skills/repo-maintenance/SKILL.md`

# AGENTS.md

## Project

`ncku-thesis-template-latex` is a community-maintained XeLaTeX thesis/dissertation template for National Cheng Kung University.

- It is not an officially endorsed NCKU software project.
- Current department and university rules override template guidance.
- Preserve existing `thesis.tex`, `conf/conf.tex`, public commands, and visible layout unless a verified bug or official rule requires a documented change.
- XeLaTeX remains the supported engine for the 2.x line.

## V2 modernization outcome

The `feat/v2.x` branch is the only planned development branch after v1.8. It
skips a separate v1.9 release and delivers a compatibility-preserving v2
architecture that:

1. keeps the visible NCKU layout and top-level student project structure;
2. preserves every explicitly declared v1 command/environment throughout 2.x;
3. fixes proven helper defects with focused regression fixtures;
4. separates generic mechanisms from NCKU policy and institutional data;
5. restores the v1.5.0 non-NCKU customization boundary under
   `template/style/`, not `conf/`;
6. ships documented and tested 1.x-to-2.x migration steps;
7. keeps direct XeLaTeX and Overleaf builds authoritative.

Implement this outcome as small validated commits. A v2 version line does not
authorize a one-shot rewrite or an unverified visual redesign.

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
- Keep `tests/v1-public-api.json` passing; old commands may delegate to new
  internals, but their names and argument shapes remain available throughout
  2.x.
- Correct proven bugs rather than preserving them; document behavior changes in
  `thesis/MIGRATION-1.x-TO-2.x.md`.
- Keep `conf/` for student thesis data. Institution-level ports and style
  profiles remain under `template/style/`.
- Do not migrate bibliography systems as part of the v2 profile extraction.
- Do not claim tagged PDF or PDF/UA compliance; current output is untagged.
- The ETDS upload path should not add internal watermark, DOI overlay, encryption, or security when current official guidance says the school system applies required processing.
- Prefer inserting the school-system defense certificate as an external file; keep generated certificate templates explicitly legacy/example only.
- Record official policy URL and checked date for any compliance change.

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
- Repo-local skills are `.agents/skills/idsd-workflow/` and `.agents/skills/repo-maintenance/`.
- `.claude/skills` is a symlink to `../.agents/skills`.
- `.claude/settings.json` contains only repo-safe Claude Code settings; never store credentials.

## Documentation Standard

- `docs/requirements/` = what is wanted and WHY (the promise) — spec-grade,
  written even before code catches up.
- shipped-state docs (`thesis/README.md`, `CHANGELOG.md`, `docs/` records) = what actually SHIPPED and HOW it works (the
  receipt) — claims line-anchored to code; code wins on drift.
- `todos/` = how/progress only; a completed todo's durable knowledge
  graduates into requirements/features, then the todo file is removed
  (git history keeps the narrative).
- Skills: `create-todo` (requirements-first), `feature-documentation`.
