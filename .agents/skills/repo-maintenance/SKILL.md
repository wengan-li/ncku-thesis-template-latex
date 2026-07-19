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
Load [`documentation-management`](../documentation-management/SKILL.md) for
requirements, todos, documentation lifecycle, consolidation, or path repair.

## Source of Truth

Read only the focused sources needed for the task:

1. [`AGENTS.md`](../../../AGENTS.md) — canonical project rules and boundaries.
2. [`justfile`](../../../justfile) — canonical maintainer command surface.
3. [`docs/README.md`](../../../docs/README.md) — public documentation index and
   release/evidence routing.
4. [`docs/features/v2-modernization.en.md`](../../../docs/features/v2-modernization.en.md)
   — shipped architecture and compatibility boundary.
5. [`docs/features/validation-and-performance.en.md`](../../../docs/features/validation-and-performance.en.md)
   — current gates, artifact proof, benchmarks, and rejected/deferred decisions.
6. [`docs/features/release-and-distribution.en.md`](../../../docs/features/release-and-distribution.en.md)
   — release, package, Overleaf, sample-retirement, and watermark contracts.
7. [`docs/v1-to-v2-migration.md`](../../../docs/v1-to-v2-migration.md) — current
   user migration and institution-port contract.

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
  `tests/100-v1-public-api.json`, and the visible NCKU layout unless a focused
  fixture and authoritative evidence justify a documented correction.
- Keep `tests/102-v1-project-migration.json` passing. It pins the v1.8.2
  student-owned inputs byte-for-byte; `just test` separately proves the unchanged
  entry/configuration path and active StudentMode content/BibTeX dependencies.
- Keep generic command/renderer layers free of NCKU assets, Taiwan-year policy,
  and institution-specific degree-submission wording. The selected profile owns
  these values, while Master/Doctoral branching follows numeric degree state
  rather than localized display strings. Cover date formats are profile tokens:
  generic/custom output must not borrow an oral day that `\SetCoverDate` does
  not own; an institution profile may inject that policy explicitly.
- Keep committee renderer capacity separate from institution rules.
  `\SetCommitteeSize` delegates to the selected profile's policy hook; NCKU
  clamps Master to 3--5 and Doctoral to 5--9, while neutral/custom retains 2--9.
- Keep student data in `conf/` and institution-level style ports under
  `template/style/`; never introduce `conf/style.tex`.
- Institution-name APIs are generic: `\SetUniversityName{chi}{eng}`,
  `\SetCollName{chi}{eng}`, and
  `\SetDeptName{chi}{English abbreviation}{English full name}`. The NCKU-owned
  catalogue currently contains 9 college presets and 110 department presets
  spanning departments, graduate institutes, degree programs, and centers under
  `template/style/ncku/`; every preset also selects one NCKU college. A shared
  abbreviation does not make names or mappings portable—for example, the current
  NCKU `CSIE` preset is an institute while the documented NTU wiring is a
  department. The selected `ncku` profile alone loads those NCKU commands;
  unchanged 1.x NCKU projects retain them through the default profile, while
  `custom` exposes only the generic institution API. A reusable new catalogue
  uses institution-prefixed commands rather than reusing NCKU `\SetDept...`
  names. The profile
  defines catalogue entries; each student's `conf/conf.tex` selects one entry and
  replaces the original NCKU department call, so the profile does not hard-code
  a particular department.
- Keep `\TemplateConfigurationFile` defaulted to `./conf/conf`. Repository-only
  custom-profile fixtures may override it with a generic test configuration so
  they do not mutate the byte-pinned V1 `conf/conf.tex`. Require every negative
  `.fls` assertion to first prove that the recorder file exists and is non-empty.
- Preserve `template/configure.tex` load order as a behavior contract: generic
  commands plus compatibility, base plus exactly one selected profile, student
  configuration, then `\FillInPDFData` and remaining initialization. This keeps
  generic setters available to profiles, profile-owned catalogue commands
  available to student configuration, NCKU data absent before profile selection,
  and PDF metadata based on resolved student values. Profiles define catalogue
  entries; student configuration selects one.
- `template/style/custom/custom.tex` is a neutral, buildable skeleton—not an
  NTU or universal ready-to-submit profile. A named-school walkthrough may prove
  generic API wiring, but it remains illustrative until current official
  geometry, cover/spine, wording, date/calendar, certificate, department,
  submission-processing, and asset-rights rules are implemented and tested.
- Preserve direct XeLaTeX and Overleaf compatibility; `just` is maintainer
  orchestration, not a student requirement.
- Keep the full teaching document as integration coverage and add focused
  fixtures before changing output-sensitive macros.
- Keep `tests/500-theorem-contract.tex` in the test gate before consolidating theorem
  internals. Its label option must create an auxiliary label without visible key
  leakage, and titled labels must freeze nameref metadata before temporary pgf
  key state is reused. Introduce registry behavior in bounded slices: first let
  one private ordered type list drive aggregate initialization and setter
  dispatch while preserving every per-type public wrapper, initializer, key
  family, style, and counter implementation. Preserve unknown-type no-op
  behavior explicitly and cover every registered route plus an unknown sentinel.
  The completed registry owns type order, style/numbering policy, default
  metadata, key families, membership, aggregate initialization, and default
  application. Keep every v1 insertion/initializer declaration literal as a
  compatibility adapter. Resolve forward and multi-hop counter chains to a
  frozen terminal value, including an existing non-registry LaTeX counter,
  before choosing `\newtheorem`; optional types with a
  configured parent become numbered, and cycles must fail with the package
  diagnostic rather than recursive overflow. Keep both theorem fixtures and the
  negative cycle fixture in the gate. Generic initializer scratch values must be
  frozen into each environment declaration so headings cannot leak from the
  final registry row. Keep the 13 numbered-counter getter declarations literal:
  the v1 source manifest historically discovered them through repeated
  `\renewcommand` branches even though registry-owned keys now populate values.
- Float compatibility: caption text stored in pgf temporaries must be frozen
  into `\@currentlabelname` after `\caption`/`\caption*` and before `\label`.
  Test `\nameref` after a later key parse and after subfigure scope exit, and
  require literal caption text rather than temporary macros in the auxiliary
  file. Extract only the exact minipage/mdframed/opacity wrapper shared by
  figure, multi-figure, and table paths; keep `[H]` and no-op compatibility
  placement/alignment keys unchanged.
- Numbering compatibility: freeze parsed title prefixes, separators, and counter
  names into each format getter, but keep the counter formatter/value dynamic.
  Exercise all general/appendix title and F/T/E paths after later setup calls and
  counter mutations, and require repeated setup to be idempotent.
- Source-manifest cleanup: remove `comment`-environment blocks only after the
  scanner strips them, the runtime baseline is corrected, and every comment-only
  or overlapping declaration is retained in the separate audit artifact; compare
  names and signatures.
- Do not claim tagged PDF or PDF/UA compliance from metadata alone.
- Current university and department requirements override template guidance.

## Documentation and Package Boundaries

Keep audiences separate:

- repository commands, CI, release scripts, benchmarks, and architectural
  decisions belong in internal documentation;
- `docs/README.md` routes readers to current guides and shipped feature records;
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
files must exactly equal the tracked `HEAD:thesis` tree, including the
student-facing README with concise offline migration guidance, v1 adapter, and
base/NCKU/custom profiles. Keep a focused negative test that deletes the required
student README and proves the archive checker fails. The full migration reference
lives at `docs/v1-to-v2-migration.md` in the complete repository.
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
migration. Follow `docs/features/release-and-distribution.en.md` for download,
digest, public read-back, byte-comparison, and exact-allowlist gates.

## Test Source Layout

- [`tests/000-test-suite.md`](../../../tests/000-test-suite.md) owns the flat,
  numerically grouped test inventory.
- Every tracked file under `tests/` has a unique three-digit sparse prefix and no
  subdirectory. Use the documented `100–899` concern ranges for executable
  fixtures/manifests and reserve `900–999` for historical standalone reference
  inputs that are not automatic `just test` entrypoints.
- Keep semantic `just` recipe names and build job names unnumbered. The numeric
  prefix organizes source inventory only.
- Rename test sources with exact path-reference repair across `justfile`, scripts,
  instructions, skills, and feature records. Run
  `python3 scripts/test/check-test-layout.py`, focused affected tests, and the full
  gate before committing.

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

The Test workflow push filter covers `main` and `feat/**`. Create short-lived
development branches as `feat/<short-name>` from current `main` so every pushed
update automatically enters the required hosted test gate. Merge through a pull
request, then delete local and remote feature refs after proving that the branch
has no commits unique to `main`. Keep `main` as the only persistent development
branch. A bare version-shaped branch such as `v2.x` does not match the workflow
filter and a long-lived version integration branch is not part of the current
post-release policy.

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
- Letting imported Python test modules leave unignored `__pycache__`/`*.pyc`
  files. The release recipe intentionally checks for a clean worktree after its
  test dependency; ignore interpreter bytecode instead of weakening that guard.
- Using `pdftotext ... | grep -q` under `pipefail`; write text to a file first to
  avoid producer SIGPIPE failures in Alpine CI.
