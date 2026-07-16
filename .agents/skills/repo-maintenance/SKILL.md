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
3. [`docs/v2-modernization.md`](../../../docs/v2-modernization.md) — active v2
   intent, expectations, evidence, and progress.
4. [`docs/v2-public-api-compatibility.md`](../../../docs/v2-public-api-compatibility.md)
   — 1.x helper compatibility policy and machine-checked baseline.
5. [`docs/source-optimization-review.md`](../../../docs/source-optimization-review.md)
   — prioritized modernization, performance, and CI evidence.
6. [`docs/release-versioning.md`](../../../docs/release-versioning.md) — release
   version, packaging, promotion, and public-verification contract.
7. [`docs/sample-repository-migration.md`](../../../docs/sample-repository-migration.md)
   — generated-example provenance and migration record.
8. [`docs/overleaf-distribution.md`](../../../docs/overleaf-distribution.md) —
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

- XeLaTeX remains the supported v2 engine; do not silently migrate engines.
- Preserve `thesis.tex`, `conf/conf.tex`, every entry in
  `tests/v1-public-api.json`, and the visible NCKU layout unless a focused
  fixture and authoritative evidence justify a documented correction.
- Keep `tests/v1-project-migration.json` passing. It pins the v1.8.2
  student-owned inputs byte-for-byte; `just test` separately proves the unchanged
  entry/configuration path and active StudentMode content/BibTeX dependencies.
- Keep generic command/renderer layers free of NCKU assets, Taiwan-year policy,
  and institution-specific degree-submission wording. The selected profile owns
  these values, while Master/Doctoral branching follows numeric degree state
  rather than localized display strings.
- Keep student data in `conf/` and institution-level style ports under
  `template/style/`; never introduce `conf/style.tex`.
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

The student archive extracts to stable `ncku-thesis-template-latex/`; its regular
files must exactly equal the tracked `HEAD:thesis` tree, including the migration
guide, v1 adapter, and base/NCKU/custom profiles. Keep a focused negative test
that deletes one required migration file and proves the archive checker fails.
When this gate runs inside `xu-cheng/texlive-action`, configure
`$GITHUB_WORKSPACE` as a Git safe directory before `git archive`/`git ls-tree`
and install full Info-ZIP `unzip`/`zip`; BusyBox `unzip` does not support
`unzip -Z1`, and the negative mutation requires `zip -d`. A local macOS pass
is not sufficient evidence for this container-specific path.
The examples archive extracts to stable `ncku-thesis-template-latex-examples/`
and contains exactly:

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
python3 scripts/test/check-v1-project-migration.py
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

## Development Branch and Hosted Test Gate

The Test workflow push filter covers `main` and `feat/**`. Use the `feat/**`
namespace for development branches (for example, `feat/v2.x`) so every pushed
update automatically enters the required hosted test gate. A bare
version-shaped branch such as `v2.x` does not match that filter.

After every feature-branch push:

1. find the Test run whose `headSha` exactly matches the pushed commit;
2. wait for that run to complete successfully;
3. inspect annotations and the expected test artifact when relevant;
4. call the update hosted-tested only after those checks pass.

If no run appears, inspect the workflow branch trigger before treating the push
as tested. A successful run for an older SHA is not evidence for the latest
update.

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
