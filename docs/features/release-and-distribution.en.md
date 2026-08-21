<!-- language: en; summary: release-and-distribution.md -->

[繁體中文摘要](release-and-distribution.md) | [English technical record](release-and-distribution.en.md)

# Release and distribution

Status: GitHub production release verified; Overleaf Gallery V2 update approved
and independently read back from the public page, source, and PDF on 2026-07-21.

- Public Overleaf template:
  <https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn>

This record explains how a release is built, what the two public packages
contain, how a published release is verified after the fact, and how the
Overleaf listing relates to GitHub. The two distribution channels are
independent states: a GitHub change does not update Overleaf, and an Overleaf
submission is not an approval.

## Version contract

Release tags use:

```text
vMAJOR.MINOR.PATCH.YYMMDDhhmmss
```

The final 12 digits are a valid UTC timestamp (`YYMMDDhhmmss`). This is a
repository convention rather than strict three-component Semantic Versioning.
Candidate strings can be generated with, for example:

```bash
date -u +v2.0.2.%y%m%d%H%M%S
```

Tags are annotated and immutable. Never move a published tag to a different
commit.

## How a release is built and promoted

The Release workflow has two stages:

1. **Build** — a tag push or manual dispatch runs `just release <version>`.
   Its declared `test` dependency runs the complete required gate once, then
   the job uploads two verified ZIPs as a temporary workflow artifact.
2. **Promote** — only a matching Git tag event downloads that exact workflow
   artifact and attaches it to a GitHub Release.

A manual dispatch is build-only and must not publish a release. A clean
worktree is required so compiled PDFs and archives come from one committed
source revision.

The workflow owns environment and promotion only. TeX case entry points live
in `scripts/release/*.tex`, and `just release` owns the build and verification
logic; case behavior is not duplicated in workflow YAML.

## Public asset contract

Every release promotes exactly two custom assets:

```text
ncku-thesis-template-latex-<version>.zip
ncku-thesis-template-latex-examples-<version>.zip
```

GitHub's automatic source archives are separate contributor artifacts and are
not part of this custom allowlist.

### Student package

The student ZIP:

- expands to stable `ncku-thesis-template-latex/`;
- contains exactly the tracked regular files from `HEAD:thesis`;
- places `thesis.tex`, `conf/`, `context/`, `example/`, and `template/`
  directly inside that root;
- includes the student README with offline migration steps, the licence text,
  the compatibility adapter, and the base/NCKU/custom profiles;
- excludes `justfile`, `AGENTS.md`, CI, tests, scripts, internal docs, and a
  redundant `thesis/` directory layer;
- builds directly with the packaged canonical command
  `latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex` outside
  repository tooling.

The exact-tree checker has a negative mutation test: removing a required
packaged file such as `README.md` must make verification fail.

### Examples package

The examples ZIP expands to stable `ncku-thesis-template-latex-examples/` and
contains exactly:

```text
README.md
LICENSE
cover.pdf
thesis-chi.pdf
thesis-eng.pdf
thesis-full.pdf
defense-certificate-master.pdf
defense-certificate-phd.pdf
```

The outer archive carries the version, so inner names stay stable. Loose PDFs
are build intermediates, not separate release assets. The package README
records the source revision and version and clearly labels the generated
defense certificates as unofficial demonstrations and regression outputs.

## Public verification

A green workflow is not sufficient release proof. After publication:

1. download the public assets again;
2. require the exact two-asset allowlist and ZIP integrity;
3. compare public bytes with the promoted workflow artifact;
4. compare the student regular-file list with the tagged `thesis/` tree;
5. verify the pinned V1 student inputs;
6. extract and directly build the downloaded student project;
7. verify A4 dimensions, page count, SyncTeX, convergence, default
   Draft/watermark state, example allowlist, README, and six PDF page
   contracts.

The v2.0.2 release hashes and read-back evidence are recorded in
[`validation-and-performance.en.md`](validation-and-performance.en.md#v202-production-release-read-back).

## Overleaf profiles

Overleaf packages are repository/import artifacts under ignored build storage;
they are not additional GitHub Release assets.

```bash
just overleaf <version>
just overleaf-gallery <version>
```

- The editable package keeps StudentMode and the student project surface.
- The Gallery package loads an independent publication overlay, clears the
  cover Draft marker, diagonal text layer, and figure watermark, removes
  unused institutional/example PDFs, and retains dummy metadata.
- Both packages contain one unambiguous root `thesis.tex` with an active
  `\documentclass`; nested configuration must not be auto-detected as the
  main document.
- Both are extracted and cold-built with XeLaTeX before use.
- The Gallery overlay is injected immediately after
  `\input{\TemplateConfigurationFile}` so it stays compatible with the
  default-preserving configuration seam. The required `just test` gate
  cold-builds the generated Gallery package so this source/package contract
  cannot drift silently.

Required Overleaf settings:

```text
Main document: thesis.tex
Compiler:      XeLaTeX
TeX Live:      latest compatible version
Editor:        Code Editor recommended
```

A ZIP cannot carry the Overleaf compiler setting. A successful local build
proves source portability, but not main-document auto-detection, project
settings, or plan-specific timeout behavior.

### Recorded Gallery state

- The community-maintained template was submitted on 2026-07-12 and the
  initial public listing was approved and published on 2026-07-15.
- On 2026-07-18 the verified V2 Gallery package was reported as uploaded to
  the original Overleaf project and resubmitted for review.
- On 2026-07-21 the owner supplied Overleaf's approval notice and the public
  listing was independently read back. The public `View Source` entry point
  has one direct root `\documentclass` and loads `./template/configure`,
  matching the generated V2 Overleaf entry-point contract.
- The public `Open as Template` route specifies XeLaTeX, root `thesis.tex`,
  and TeX Live 2025.1. The isolated verification browser reached the Overleaf
  login before project creation, so this checkpoint verifies the public route
  parameters without claiming an authenticated fresh-project compile.
- The public PDF read back on 2026-07-21 is 95,410 bytes, SHA-256
  `4797e63c70f8a76c0dea6bd0142b039b0280151d1fb12e48c53c01b09f1e1c6c`,
  11 A4 pages, with a recorded creation time of 2026-07-18 09:42:38 HKT.
  Rendered inspection of the cover, abstract, and acknowledgements found
  complete readable content with no clipping, overlap, Draft marker, or
  institutional watermark.
- The durable state is therefore **approved and publicly read back**. GitHub
  Releases remains the canonical versioned download path, while the Gallery
  is the approved public Overleaf editing route.

Before reporting a newer Overleaf state, inspect the live page, public PDF,
and `Open as Template` route. Preserve the original project as the update
identity; do not submit a replacement project to work around moderation.

### Overleaf limits and licensing

The packaging verifier uses the limits checked from Overleaf documentation on
2026-07-12: 180 files per upload, 2,000 files per project, 50 MB per
individual upload, 7 MB editable project data, and 2 MB per editable text
file. Recheck live official limits before changing the verifier.

The repository declares CC BY-NC-SA 4.0. That project-level declaration does
not prove redistribution rights for every third-party font, logo, certificate,
or watermark asset. The Gallery profile removes the institutional logo
watermark and example oral PDFs but still depends on bundled fonts. Do not
claim institutional endorsement or silently relicense those files. Any
requested font/licensing change needs a separate output-regression-tested
decision.

## Draft and watermark policy

Three independent mechanisms exist:

1. `\DisplayDraft` controls only `(Draft)` / `(初稿)` on the cover.
2. `\SetWatermarkText{...}` controls the third-party diagonal text layer.
3. `\UseWatermarkFigureStyle` registers the bundled NCKU seal/logo PDF as a
   page background.

Normal StudentMode and teaching/example builds are final-ready by default:
all three are off. Each API remains an explicit opt-in, and the Gallery
overlay clears all three again as defence in depth. Tests assert package
state and `.fls` asset absence because graphical watermark text may not
appear reliably in `pdftotext`.

`v1.8.2.260715154703` was the first immutable release with these corrected
safe defaults. Current students must follow current
university/library/department instructions rather than historical template
watermark behavior.

## Retired sample repository

The old generated-sample repository
`wengan-li/ncku-thesis-template-latex-sample` had an independent history and
was deleted by the owner on 2026-07-12 after replacement assets were publicly
built and verified. The owner accepted broken old links and rejected extra
bundle, NAS, off-machine archive, redirect, or grace-period requirements.

The source repository and timestamped GitHub Releases are now the only
maintained sources for editable projects and generated examples. Historical
school-system certificate PDFs from the retired repository were not adopted
as generated release assets; students must obtain current official documents
from the school system.

## Operational sources

- `justfile` — canonical local command surface.
- `scripts/release/` — maintained release cases and package verification.
- `.github/workflows/release.yml` — build/promote environment boundary.
- `scripts/overleaf/` — Overleaf package generation and verification.
- `thesis/README.md` — student-facing package instructions.
- [`v1-to-v2-migration.en.md`](../v1-to-v2-migration.en.md) — full migration
  contract.
- [`validation-and-performance.en.md`](validation-and-performance.en.md) —
  release hashes, direct-build proof, and engineering gates.
