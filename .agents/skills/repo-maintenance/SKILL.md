---
name: repo-maintenance
description: Use for maintaining and releasing this repository.
---

# Repository Maintenance

## When to Use

Use for source changes, tests, documentation, generated examples, CI, releases,
and compatibility reviews in this repository.

For every task, load the sibling [`idsd-workflow`](../idsd-workflow/SKILL.md)
first. Keep general LaTeX knowledge outside this repository; this skill contains
only project-specific rules and pointers.

## Source of Truth

Read only the focused sources needed for the task:

1. [`AGENTS.md`](../../../AGENTS.md) — canonical project rules and boundaries.
2. [`justfile`](../../../justfile) — canonical maintainer command surface.
3. [`docs/source-optimization-review.md`](../../../docs/source-optimization-review.md)
   — prioritized modernization, performance, and CI decisions.
4. [`docs/release-versioning.md`](../../../docs/release-versioning.md) — release
   version, packaging, promotion, and public-verification contract.
5. [`docs/sample-repository-migration.md`](../../../docs/sample-repository-migration.md)
   — generated-example provenance and migration record.
6. [`docs/overleaf-distribution.md`](../../../docs/overleaf-distribution.md) —
   unofficial-template policy, import package limits, and publication blockers.

Inspect current source and Git state before trusting historical notes. When a
rule changes, update its canonical repository source in the same slice.

## Canonical Commands

Use `just`; do not introduce a Makefile or duplicate orchestration in CI:

```bash
just
just thesis
just watch
just example
just test
just check
just ci
just overleaf <version>
just release <version>
just clean
```

`latexmk` is the XeLaTeX/BibTeX/rerun orchestrator underneath `just`. Keep the
student project directly buildable without repository tooling:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

## Compatibility Boundary

- XeLaTeX remains the supported v1.8 engine; do not silently migrate engines.
- Preserve `thesis.tex`, `conf/conf.tex`, public commands, and visible layout
  unless a focused fixture and authoritative evidence justify a change.
- Preserve direct XeLaTeX and Overleaf compatibility; `just` is maintainer
  orchestration, not a student requirement.
- Keep the full teaching document as integration coverage and add focused
  fixtures before changing output-sensitive macros.
- Do not claim tagged PDF or PDF/UA compliance from metadata alone.
- Current university and department requirements override template guidance.

## Documentation and Package Boundaries

Keep audiences separate:

- maintainer commands, CI, release scripts, benchmarks, and architectural
  decisions belong in root/internal documentation;
- direct compiler, editor, configuration, and writing guidance belongs in the
  packaged `thesis/` project and teaching content;
- root `README.md` routes both audiences without exposing unnecessary internals;
- the student ZIP must not contain `justfile`, `AGENTS.md`, CI, tests, scripts,
  internal docs, or a redundant `thesis/` wrapper.

Generated defense-certificate PDFs are unofficial demonstrations and regression
outputs. Current students must use files produced by the university
degree-examination system and follow current university/department guidance.

## Release Contract

A release promotes exactly two custom, versioned packages from one verified
source revision:

```text
ncku-thesis-template-latex-<version>.zip
ncku-thesis-template-latex-examples-<version>.zip
```

The student archive extracts to stable `ncku-thesis-template-latex/`. The
examples archive extracts to stable `ncku-thesis-template-latex-examples/` and
contains exactly:

```text
README.md
cover.pdf
thesis-chi.pdf
thesis-eng.pdf
thesis-full.pdf
defense-certificate-master.pdf
defense-certificate-phd.pdf
```

The outer archives carry the version. Inner names remain stable and omit a
redundant `example-` prefix. Loose generated PDFs are build intermediates, not
public Release assets.

Do not move an immutable tag or rebuild old tagged PDFs during an asset-only
migration. Follow `docs/release-versioning.md` for download, digest, public
read-back, byte-comparison, and exact-allowlist gates.

## Verification

For source or build changes, run at minimum:

```bash
just test
just ci
git diff --check
git status --short
```

For release changes, run a clean-worktree release build with an explicit version
and inspect both archives. For PDF-affecting changes, inspect metadata and text,
render affected pages, and check new warnings separately from inherited ones:

```bash
pdfinfo build/thesis.pdf
pdftotext build/thesis.pdf -
```

After pushing, verify the exact GitHub Actions run. After publishing or changing
Release assets, download them from their public URLs and verify the public state;
a local or workflow artifact alone is insufficient.

For GitHub Actions dependency maintenance, enumerate every repository-owned
`uses:` reference across all workflow files and check each action's official
latest stable release plus `action.yml` runtime. After pushing, run the normal
Test workflow and a manual build-only Release workflow, then inspect job
annotations; a green status alone does not prove runtime deprecation warnings
are gone. Manual Release dispatch must not promote a GitHub Release.

## Pitfalls

- Mixing student instructions with maintainer-only `just` or CI commands.
- Treating the 271-page teaching document as the normal student rebuild cost.
- Caching LaTeX auxiliary state in required clean test/release lanes.
- Switching to an Arm runner while the selected TeX container is amd64-only.
- Treating Overleaf's accepted community-maintained Gallery listing as NCKU
  endorsement. Keep the unofficial label, and update only through the original
  Overleaf project followed by resubmission and reapproval.
- Publishing loose example PDFs in addition to the examples ZIP.
- Using `legacy` in a public filename when `generated` plus a clear package
  notice communicates the institutional-document boundary more accurately.
- Using `pdftotext ... | grep -q` under `pipefail`; write text to a file first to
  avoid producer SIGPIPE failures in Alpine CI.
