# Make the first-time student path obvious

Status: active
Owner: wengan-li
Last updated: 2026-08-22
Method: IDSD

## Intent

### Goal

A graduate student who has never seen this repository can go from the GitHub
page to a correct first build of their own thesis without reading anything
written for maintainers, and can tell at every step what to change, where, and
what happens if they do not.

### Constraints

- `thesis/thesis.tex`, `thesis/conf/conf.tex`, and `thesis/context/**` stay
  byte-identical to v1.8.2 (owner decision recorded on 2026-08-21). Fix the
  student experience around those files, not inside them.
- Public documentation keeps the third-person voice and bilingual pair rules
  in `AGENTS.md`; `python3 scripts/test/check-bilingual-docs.py` must pass.
- The root `README.md` historical bilingual H1 and protected headings stay.
- Teaching-example text edits are PDF-affecting: keep the canonical example at
  271 A4 pages and re-run the release asset verification.
- No new `conf/style.tex`; no profile talk on the NCKU student path.

### Failure Conditions

- A student-facing page explains byte pins, profiles, regression evidence, or
  immutable revisions before telling the student what to edit.
- A shipped default that prints wrong cover data (placeholder advisors B and C,
  2023 dates, the template's own title) is not listed with its line number and
  consequence.
- A new section exists in one language of a guide pair only.

## Expectations

### Done Means

- P0 below is merged on green checks and the changed teaching text is visible
  in the rebuilt example PDF.
- The `student-first-run` skill exists, is registered, and every later
  student-facing change loads it.
- P1 and P2 either have their own follow-up slices or an explicit owner
  decision recorded here.

### Success Scenarios

1. A student reads `thesis/README.md`, edits the listed `conf/conf.tex` lines,
   builds, and the cover shows their title, name, degree, department, oral date,
   and exactly their advisors.
2. A student on Overleaf opens the Gallery template, sets XeLaTeX and
   `thesis.tex`, and builds without touching `\ExampleMode`.
3. A student hitting one of the listed errors finds the cause and fix in
   `thesis/README.md` without opening an issue.
4. A student on the Releases page knows which ZIP to download from the release
   notes alone.

### Recovery Plan

- Revert a documentation slice if the bilingual gate or link validation fails
  after merge; the example PDF contract is checked by `just release` before any
  tag.
- If a release tag is pushed without a changelog entry, the build job now
  fails before promote; fix the changelog, delete the dead tag, re-tag.

### Review Checkpoints

- Each PR merges only with green push and pull-request checks, verified by
  explicit exit status (no `| head`, no reliance on `set -e`).
- Visible-output fixes (example `.tex`) stay in commits separate from tooling.

### Validation

- `python3 scripts/test/check-bilingual-docs.py`
- `just ci`
- `just release dev` (asserts the 271-page example contract after text edits)
- `pdftotext build/thesis.pdf - | grep` for each corrected teaching sentence
- `git diff --check`

## Context

### Current Evidence

Walk-through on 2026-08-22 at `main` `9dd13c9`, reading exactly what a student
sees in order: GitHub page, Releases, unzipped package, `README.md`,
`conf/conf.tex`, `context/`, the teaching PDF, Overleaf.

Shipped `conf/conf.tex` defaults a student must change (line numbers are stable
because the file is byte-pinned): `\ExampleMode` 13, `\DisplayCoverInEng` 44,
`\SetTitle` 71–73, `\PhdDegree` 99, `\SetMyName` 111, `\SetOralDate` 125,
`\SetCoverDate` 138 (ignored by the `ncku` profile, `ncku.tex:196`),
`\SetDeptCSIE` 148, advisors A/B/C 166–168 (the cover prints any non-empty
advisor, `template/cover/cover-chi.tex:102-110`), `\DisplayOralImage` 204–206
(enabled with the file names commented out, so the certificate page silently
disappears), keywords 224 and 246–248.

### Connections

- Skill: `.agents/skills/student-first-run/SKILL.md`
- Student entry pages: `README.md`, `thesis/README.md`, `thesis/conf/README.md`
- Teaching example: `thesis/example/how-to/**`
- Release notes: `.github/workflows/release.yml`,
  `scripts/release/release-notes.py`, `CHANGELOG.md`, `CHANGELOG.en.md`

### Source Links

- `docs/features/release-and-distribution.en.md`
- `docs/features/validation-and-performance.en.md`
- `thesis/template/style/ncku/README.md`

### Assumptions And Open Questions

- Licence scope wording for a student's own thesis content (B5) needs an owner
  decision before it is written down.
- Restructuring the teaching example (E1) changes the 271-page contract and
  needs an owner go-ahead.

## Progress

### P0 — immediate, no pinned file touched

- [x] E4 Fix `\\DisplayCoverPeoplesBothNames` in
      `thesis/example/how-to/use/conf.tex` and `./content/references` in
      `thesis/example/how-to/write/bib/bib.tex`.
- [x] E6 Replace the "no need to read the official rules" sentence in
      `thesis/example/introduction/introduction.tex`.
- [x] A5 Release notes composed from both changelog entries plus a download
      guide (`scripts/release/release-notes.py`); `just release <version>`
      fails for a release version without a changelog entry; `just test`
      covers the script.
- [x] B3 `cover.tex` print-cover step in `thesis/README.md` / `.en.md`.
- [x] B4 Common errors section in `thesis/README.md` / `.en.md`.
- [x] B6 Pre-submission checklist: advisors, dates, certificate page, both
      titles, abstract selection.
- [x] C1 Must-change table with `conf/conf.tex` line numbers and consequences
      in `thesis/README.md` / `.en.md`, including the `context/context.tex`
      Chinese abstract and acknowledgements switch (D3).
- [x] A1/A4 Three build paths (Overleaf, terminal, editor) named in the root
      quick start, both languages.
- [x] F2 Overleaf steps in `thesis/README.md` / `.en.md`.
- [x] A6 Repository topics set by the owner on 2026-08-22 (`tachikoma-agent`
      has push only; the topics endpoint returned 404): dissertation, latex,
      ncku, taiwan, thesis, thesis-template, xelatex.
- [x] Skill `student-first-run` written and registered in `AGENTS.md`,
      `.agents/skills/README.md`, `repo-maintenance`, and
      `documentation-management`.

### P1 — documentation restructure

- [x] A2/A3 Root README: overview, setup, downloads, upgrade, and
      other-institution sections rewritten in student terms; the NCKU path no
      longer mentions profiles, immutable revisions, or regression evidence.
- [x] B1/B2 `thesis/README.md`: byte-pin rationale replaced by "change only the
      values"; the 1.x upgrade section moved to the end and rewritten as steps.
- [x] C4 `thesis/conf/README.md`: every section opens with a required/optional
      line citing the `conf/conf.tex` line numbers; profile wording replaced by
      plain NCKU statements.
- [x] C5 Department lookup hint (search the Chinese name, copy the left
      column) in `conf/README.md` and the must-change table.
- [x] A7 `本範本` throughout the root README body and `conf/README.md`
      (headings and the historical H1 untouched); the gate's third-person
      markers updated to the new sentences.
- [x] G2 `thesis/README.md` says `example/` can be deleted once `\ExampleMode`
      stays commented out.

### P2 — owner decisions

- [x] E1 Teaching document reordered (2026-08-22): introduction, usage
      tutorial, writing tutorial, "words from professors" (kept in the body
      as the last chapter by owner decision); origin story moved to the
      appendix. 271 → 261 pages; `justfile` pin and records updated.
- [x] E2/E3 MiKTeX 2.9 / Texmaker screenshot chapter replaced by a three-path
      section (Overleaf, terminal, editor) with a short "when it fails"
      pointer to the README; 23 screenshots removed; figure conversion reduced
      to "export PDF, crop with `pdfcrop`".
- [x] F1 Gallery source and refresh cadence recorded; the owner refreshed the
      Gallery from `v2.0.7.260822120950` on 2026-08-22 and the public PDF was
      read back on 2026-08-23 (text identical to the local package build).
      The listing's CC BY 4.0 licence field is deliberate dual licensing
      (owner decision 2026-08-23; Overleaf offers no other option).
- [x] B5 Licence scope stated in the root README, the student README, and the
      teaching introduction: the licence covers the template files; the
      student's thesis content and generated PDF belong to the student.
- [ ] D1/D2 `relatd` typo and the Chinese abstract placeholder live in pinned
      `context/` files. Fixing them means moving the v1.8.2 pin to fixture
      copies, which reverses the 2026-08-21 decision to keep the live files
      unchanged; left for an explicit owner go-ahead.
- [x] G1 Issue form `.github/ISSUE_TEMPLATE/student-question.yml` (Chinese
      and English, asks for the build method, version, steps, and the first
      `!` line of the log) plus contact links to the README and the NCKU
      thesis system.

## Learnings

- The bilingual gate protects structure (topic IDs, H2 counts, code blocks),
  not audience. Maintainer rules copied from `AGENTS.md` pass it unchanged, so
  the student lens has to be applied by a person or by the
  `student-first-run` skill.
- The byte pin has a concrete cost: three active advisor placeholders and a
  cover that prints any non-empty slot. Documentation has to carry that cost
  when the file cannot.
