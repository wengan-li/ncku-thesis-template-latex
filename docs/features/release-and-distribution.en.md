<!-- language: en; summary: release-and-distribution.md -->

[繁體中文摘要](release-and-distribution.md) | [English technical record](release-and-distribution.en.md)

# Release and distribution

[GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases) is the authority for versioned downloads. The [public Overleaf Gallery listing](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn) is a separate editing route. Repository source, a locally generated package, an upload, a submission and public approval are distinct states. A GitHub update does not update the Gallery or prove that its source matches the repository.

## Version and publication contract

Release tags use an immutable annotated tag with a valid UTC timestamp:

```text
vMAJOR.MINOR.PATCH.YYMMDDhhmmss
```

Never move a published tag. Use the [changelog](../../CHANGELOG.en.md) for version changes and GitHub Releases for available artifacts, rather than inferring publication from source documentation.

The Release workflow builds with `just release <version>` from clean committed source. Its test dependency runs the required gate. Only a matching Git tag event promotes the exact workflow artifact to a Release; manual dispatch is build-only. Both changelogs must contain the exact version entry. `scripts/release/release-notes.py` composes those entries with the student download guide. The workflow owns environment and promotion; `justfile` and `scripts/release/` own case builds and verification.

## Public asset contract

Each release has exactly two custom public assets:

```text
ncku-thesis-template-latex-<version>.zip
ncku-thesis-template-latex-examples-<version>.zip
```

GitHub's automatic full-source archives are separate. Loose generated PDFs are intermediates, not additional Release assets.

### Student package

The student ZIP extracts to one `ncku-thesis-template-latex/` directory with `thesis.tex`, `conf/`, `context/`, `example/` and `template/` directly inside. Its complete member inventory and bytes equal `HEAD:thesis`; for publication, that source is the release tag. It includes the student README, licence, compatibility adapter and base/NCKU/custom profiles.

Repository tests, scripts, CI and maintenance instructions stay outside the package. The precise student-instruction exceptions are `AGENTS.md`, `context/AGENTS.md`, adjacent relative `CLAUDE.md -> AGENTS.md` aliases and the single project-root writing skill with `.claude/skills -> ../.agents/skills`. [Student knowledge](student-writing-and-agent-skills.en.md) defines the payload and copy contract. There is no redundant `thesis/` wrapper.

`scripts/release/verify-student-archive.sh` checks inventory, bytes, required content and extracted symlink mode/target/content. Missing-member mutations must fail. The extracted project builds directly with XeLaTeX/BibTeX through `latexmk`, without repository tooling; Overleaf and editors select `thesis.tex` and XeLaTeX.

### Examples package

The examples ZIP extracts to `ncku-thesis-template-latex-examples/` with exactly:

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

The outer filename carries the version; inner filenames stay stable. `scripts/release/example-assets.sh` owns this list. The README identifies source and licence and labels generated certificates as unofficial demonstrations. Generated examples come only from Release assets; they are not source files.

## Verify publication

After an authorized publication, download the public assets, check ZIP integrity and the exact two-asset allowlist, and compare SHA-256 digests and bytes with the promoted workflow artifacts. Compare the student package with the tagged thesis tree, extract it, and run the direct student build. Check A4, expected pages, SyncTeX, references/citations, default Draft/watermark state, licence and the six example-PDF contracts. A green workflow alone does not establish the public bytes.

Do not change tags or rebuild old tagged PDFs to repair an asset-only distribution issue. A local package check is not an upload or public verification.

## Overleaf profiles

```bash
just overleaf <version>
just overleaf-gallery <version>
```

These import packages live under ignored build storage and are not extra GitHub Release assets. Both omit `example/` and `cover.tex`, default to StudentMode, preserve the hidden writing payload and relative aliases, and provide one root `thesis.tex` with a direct documentclass declaration. Both are extracted and cold-built locally.

The student profile keeps the editable project surface. The Gallery profile adds a publication overlay immediately after `\input{\TemplateConfigurationFile}`, clears every Draft/watermark layer and omits unused institutional/example PDFs while retaining dummy student metadata. `just test` checks that generated Gallery path.

Overleaf must use `thesis.tex`, XeLaTeX and a compatible TeX Live version. A ZIP cannot carry all account/compiler settings. Local cold builds do not establish hosted timeout behavior, authenticated fresh-project compilation or client handling of agent aliases. Verify those separately when needed.

The verifier enforces an upload budget of 180 files, 50 MiB per archive/file, 2 MiB per editable file and 7 MiB total editable text. Consult the official [upload guidance](https://docs.overleaf.com/managing-projects-and-files/uploading-a-project) and [plan limits](https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits) before changing limits. Platform limits and the verifier's configured budget are distinct.

Update the original Overleaf project rather than creating a replacement listing. Source/runtime or student-build-path releases require a fresh Gallery package; documentation-only releases do not. Confirm the live listing, PDF and Open as Template route before reporting a publication change. Submission does not imply approval or institutional endorsement.

## Licensing and institutional documents

The repository and custom Release packages use CC BY-NC-SA 4.0. The Gallery copy is offered under CC BY 4.0. These project-level licences do not grant rights to third-party fonts, logos, certificates or watermark assets. Keep that distinction when redistributing files; do not silently relicense bundled assets. The project claims no rights in students' original thesis text, figures, data or PDF.

Students must use current school-system degree-examination certificate files and follow current university/department rules. The template-generated certificate PDFs are examples, not official documents or substitutes for the university system. See the [student guide](../../thesis/README.en.md) and [official ETDS guidance](https://thesis.lib.ncku.edu.tw/help/aboutedit/).

## Draft and watermark policy

Three independent APIs remain opt-in:

- `\DisplayDraft` adds the cover Draft marker.
- `\SetWatermarkText{...}` controls diagonal text.
- `\UseWatermarkFigureStyle` registers the NCKU logo background.

Normal StudentMode and teaching builds leave all three off; the Gallery overlay clears them again. ETDS output adds no internal watermark, DOI overlay, encryption or security processing. Follow current official upload instructions for school-system processing. Tests check state and nonempty recorder files because PDF text extraction alone cannot establish graphical watermark absence.

[Validation](validation-and-performance.en.md) describes the live gates; [migration](../v1-to-v2-migration.en.md) covers existing student projects.
