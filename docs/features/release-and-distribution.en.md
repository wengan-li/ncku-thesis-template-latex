<!-- language: en; summary: release-and-distribution.md -->

[繁體中文摘要](release-and-distribution.md) | [English technical record](release-and-distribution.en.md)

# Release and distribution

Status: GitHub production release verified; Overleaf Gallery V2 update last
recorded as owner-confirmed submitted and pending public approval/read-back.

- Latest production release:
  [`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734)
- Public Overleaf template:
  <https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn>

GitHub source/release state and Overleaf publication state are independent. A
GitHub change does not update Overleaf, and an Overleaf submission is not an
approval.

## Version contract

Release tags use:

```text
vMAJOR.MINOR.PATCH.YYMMDDhhmmss
```

The final 12 digits are a valid UTC timestamp (`YYMMDDhhmmss`). This is a
repository convention rather than strict three-component Semantic Versioning.
Candidate strings can be generated with, for example:

```bash
date -u +v2.0.1.%y%m%d%H%M%S
```

Tags are annotated and immutable. Never move a published tag to a different
commit.

## Build and promotion boundary

The Release workflow has two stages:

1. **Build** — a tag push or manual dispatch runs `just release <version>`. Its
   declared `test` dependency runs the complete required gate once, then the job
   uploads two verified ZIPs as a temporary workflow artifact.
2. **Promote** — only a matching Git tag event downloads that exact workflow
   artifact and attaches it to a GitHub Release.

A manual dispatch is build-only and must not publish a release. A clean worktree
is required so compiled PDFs and archives are built from one committed source
revision.

The workflow owns environment and promotion only. TeX case entry points live in
`scripts/release/*.tex`; `just release` owns build and verification logic. Do not
duplicate case behavior in workflow YAML.

## Public asset contract

Every release promotes exactly two custom assets:

```text
ncku-thesis-template-latex-<version>.zip
ncku-thesis-template-latex-examples-<version>.zip
```

GitHub's automatic source archives are separate contributor artifacts and are not
part of this custom allowlist.

### Student package

The student ZIP:

- expands to stable `ncku-thesis-template-latex/`;
- contains exactly the tracked regular files from `HEAD:thesis`;
- places `thesis.tex`, `conf/`, `context/`, `example/`, and `template/` directly
  inside that root;
- includes the student README with offline migration steps, compatibility adapter,
  and base/NCKU/custom profiles;
- excludes `justfile`, `AGENTS.md`, CI, tests, scripts, internal docs, and a
  redundant `thesis/` directory layer;
- builds directly with `latexmk -xelatex thesis.tex` outside repository tooling.

The exact-tree checker and its negative mutation test must fail if a required
packaged surface such as `README.md` is removed.

### Examples package

The examples ZIP expands to stable
`ncku-thesis-template-latex-examples/` and contains exactly:

```text
README.md
cover.pdf
thesis-chi.pdf
thesis-eng.pdf
thesis-full.pdf
defense-certificate-master.pdf
defense-certificate-phd.pdf
```

The outer archive carries the version, so inner names stay stable. Loose PDFs are
build intermediates and are not separate release assets. The package README
records source/version and clearly labels generated defense certificates as
unofficial demonstrations/regression outputs.

## Public verification

A green workflow is not sufficient release proof. After publication:

1. download the public assets again;
2. require the exact two-asset allowlist and ZIP integrity;
3. compare public bytes with the promoted workflow artifact;
4. compare the student regular-file list with the tagged `thesis/` tree;
5. verify the pinned V1 student inputs;
6. extract and directly build the downloaded student project;
7. verify A4 dimensions, page count, SyncTeX, convergence, default Draft/watermark
   state, example allowlist, README, and six PDF page contracts.

The current release hashes and read-back evidence are recorded in
[`validation-and-performance.en.md`](validation-and-performance.en.md#current-production-release-read-back).

## Overleaf profiles

Overleaf packages are repository/import artifacts under ignored build storage;
they are not additional GitHub Release assets.

```bash
just overleaf <version>
just overleaf-gallery <version>
```

- The editable package keeps StudentMode and the student project surface.
- The Gallery package loads an independent publication overlay, clears the cover
  Draft marker, diagonal text layer, and figure watermark, removes unused
  institutional/example PDFs, and retains dummy metadata.
- Both packages contain one unambiguous root `thesis.tex` with an active
  `\documentclass`; nested configuration must not be auto-detected as the main
  document.
- Both are extracted and cold-built with XeLaTeX before use.

Required Overleaf settings:

```text
Main document: thesis.tex
Compiler:      XeLaTeX
TeX Live:      latest compatible version
Editor:        Code Editor recommended
```

A ZIP cannot carry the Overleaf compiler setting. A successful local build proves
source portability but not main-document auto-detection, project settings, or
plan-specific timeout behavior.

### Recorded Gallery state

- The community-maintained template was submitted on 2026-07-12 and the initial
  public listing was approved/published on 2026-07-15.
- On 2026-07-18 the verified V2 Gallery package was reported as uploaded to the
  original Overleaf project and resubmitted for review.
- The authenticated project settings and compile result were not independently
  read back at that checkpoint. The public page still exposed the earlier copy.
- Therefore the durable state is **owner-confirmed submitted**, not independently
  approved V2. GitHub Releases remains canonical until the V2 Gallery copy is
  publicly approved and independently read back.

Before reporting a newer Overleaf state, inspect the live page, public PDF, and
`Open as Template` result. Preserve the original project as the update identity;
do not submit a replacement project to work around moderation.

### Overleaf limits and licensing

The packaging verifier uses the limits checked from Overleaf documentation on
2026-07-12: 180 files per upload, 2,000 files per project, 50 MB per individual
upload, 7 MB editable project data, and 2 MB per editable text file. Recheck live
official limits before changing the verifier.

The repository declares CC BY-NC-SA 4.0. That project-level declaration does not
prove redistribution rights for every third-party font, logo, certificate, or
watermark asset. The Gallery profile removes the institutional logo watermark and
example oral PDFs but still depends on bundled fonts. Do not claim institutional
endorsement or silently relicense those files. Any requested font/licensing change
needs a separate output-regression-tested decision.

## Draft and watermark policy

Three independent mechanisms exist:

1. `\DisplayDraft` controls only `(Draft)` / `(初稿)` on the cover.
2. `\SetWatermarkText{...}` controls the third-party diagonal text layer.
3. `\UseWatermarkFigureStyle` registers the bundled NCKU seal/logo PDF as a page
   background.

Normal StudentMode and teaching/example builds are final-ready by default: all
three are off. Each API remains an explicit opt-in. The Gallery overlay clears all
three again as defence in depth. Tests assert package state and `.fls` asset
absence because graphical watermark text may not appear reliably in
`pdftotext`.

`v1.8.2.260715154703` was the first immutable release with these corrected
safe defaults. Current students must follow current university/library/department
instructions rather than historical template watermark behavior.

## Retired sample repository

The old generated-sample repository
`wengan-li/ncku-thesis-template-latex-sample` had an independent history and was
deleted by the owner on 2026-07-12 after replacement assets were publicly built
and verified. The owner accepted broken old links and rejected extra bundle, NAS,
off-machine archive, redirect, or grace-period requirements.

The source repository and timestamped GitHub Releases are now the only maintained
sources for editable projects and generated examples. Historical school-system
certificate PDFs from the retired repository were not adopted as generated
release assets; students must obtain current official documents from the school
system.

## Operational sources

- `justfile` — canonical local command surface.
- `scripts/release/` — maintained release cases and package verification.
- `.github/workflows/release.yml` — build/promote environment boundary.
- `scripts/overleaf/` — Overleaf package generation and verification.
- `thesis/README.md` — student-facing package instructions.
- [`v1-to-v2-migration.en.md`](../v1-to-v2-migration.en.md) — full migration contract.
- [`validation-and-performance.en.md`](validation-and-performance.en.md) — current
  release hashes, direct-build proof, and engineering gates.
