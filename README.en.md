<!-- doc-pair: root-readme; lang: en; topics: project-overview,release-and-overleaf-status,choose-the-correct-setup,quick-start,downloads-and-examples,migrate-from-1-x,other-institution-profiles,submission-watermark-and-certificate,documentation-and-maintenance,other-community-alternatives,licence -->

[繁體中文](README.md) | [English](README.en.md)

# NCKU Thesis and Dissertation Template for LaTeX

[**Open as Template in Overleaf](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)

## Project overview

This community-maintained XeLaTeX template supports Chinese, English, and mixed-language NCKU master's theses and doctoral dissertations. It generates the cover, contents, figure/table lists, and other front matter, and provides student configuration, reusable LaTeX helpers, a 1.x compatibility adapter, and institution profiles for maintained ports.

This is not official NCKU software and does not represent current endorsement by the university, library, degree-examination system, or any department. Verify the current rules before use; official requirements always take precedence.

Official guidance last checked on `2026-07-12`:

- [NCKU thesis system](https://thesis.lib.ncku.edu.tw/)
- [Submission guidance](https://thesis.lib.ncku.edu.tw/help/aboutedit/)
- [Curriculum Division thesis-format guidance](https://cid-acad.ncku.edu.tw/p/412-1042-1378.php?Lang=zh-tw)

## Release and Overleaf status

The latest production source and student package are available from [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases/latest). The current production release is `v2.0.1.260719010734`. V2 preserves the complete machine-audited 1.x public API and direct XeLaTeX student workflow while organizing profiles, compatibility, tests, and downloads.

The existing Overleaf Gallery page remains public. The maintainer has confirmed that V2 was uploaded to the original Overleaf project and resubmitted for Gallery update review. Until Overleaf approves it and the public page is independently read back, “submitted” must not be treated as “approved”; GitHub Releases remains canonical for the latest V2 package.

Detailed state：[`docs/features/release-and-distribution.md`](docs/features/release-and-distribution.md#recorded-gallery-state)

## Choose the correct setup

Documentation language, institution profile, cover language, degree, and content mode are separate decisions. An international student at NCKU still uses the `ncku` profile; a Taiwan maintainer porting the template to another institution uses `custom` or another maintained profile. Do not equate “English” with “non-NCKU.”

| Decision | Choices |
| --- | --- |
| Institution | default `ncku`; maintained custom profile for another institution |
| Cover language | `\DisplayCoverInChi` or `\DisplayCoverInEng` |
| Degree | `\MasterDegree` or `\PhdDegree` |
| Content | own `context/context.tex` or `\ExampleMode` teaching example |

Historical checks in 2015 and reports from individual departments are provenance only, not current approval. CSIE is the only department with documented historical use in this repository; every student must still verify current department rules.

## Quick start

1. Download `ncku-thesis-template-latex-<version>.zip` from [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases).
2. Extract it and read [`README.en.md`](thesis/README.en.md) and [`conf/README.en.md`](thesis/conf/README.en.md) at the package root.
3. Disable `\ExampleMode` in `conf/conf.tex` and enter thesis information.
4. Select chapters in `context/context.tex` and write content under `context/`.
5. Run the following command from the directory containing `thesis.tex`.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Use `thesis.tex` as the root/master document. `latexmk` handles XeLaTeX, BibTeX, and required reruns automatically.

## Downloads and examples

Each production release provides two versioned downloads. The student package contains only the directly editable `thesis/` project tree, excluding `justfile`, CI, tests, and release scripts. The examples package contains six PDFs built and verified from the same immutable source revision for preview and regression evidence. GitHub's automatic Source code ZIP contains the complete repository.

```text
ncku-thesis-template-latex-<version>.zip
ncku-thesis-template-latex-examples-<version>.zip
```

Examples package:

```text
README.md
cover.pdf
thesis-chi.pdf
thesis-eng.pdf
thesis-full.pdf
defense-certificate-master.pdf
defense-certificate-phd.pdf
```

The generated certificate PDFs are unofficial demonstrations. Use current official documents for submission.

## Migrate from 1.x

Commit or archive the complete 1.x project and save its latest PDF before migrating. Preserve `conf/conf.tex`, `context/`, figures, bibliography data, and local certificate files; replace template-owned files with V2 and deliberately merge local changes to `thesis.tex`. V2 preserves the audited 1.x helper surface throughout 2.x, so the compatibility-first path requires no helper renaming.

Complete guide: [`docs/v1-to-v2-migration.en.md`](docs/v1-to-v2-migration.en.md)

## Other institution profiles

V2 separates shared rendering, NCKU policy, and other-institution ports into `base`, `ncku`, and `custom`. Student thesis data remains in `conf/conf.tex`; institution geometry, names, date policy, wording, and assets belong under `template/style/<profile>/`. Non-NCKU maintainers start from `template/style/custom/` rather than editing the shared renderer or loading NCKU before overriding it.

Guide: [`thesis/template/style/Customization.en.md`](thesis/template/style/Customization.en.md)

## Submission, watermark, and certificate

Final output defaults to no cover Draft marker, diagonal `DRAFT` text, or institution-logo watermark. These are three independent opt-ins; do not add them to a submission PDF merely because APIs exist. Follow the current university-system workflow, which may apply its own watermark to the approved electronic copy.

Use the official degree-examination-system defense certificate when required. Template-generated certificates are legacy/example and regression outputs. Historical checks from 2015/2018 do not constitute current authorization or endorsement.

Policy record：[`docs/features/release-and-distribution.md`](docs/features/release-and-distribution.md#draft-and-watermark-policy)

## Documentation and maintenance

Students start from the packaged README and configuration guide. Maintainers use [`docs/README.en.md`](docs/README.en.md) to find architecture, validation, release, and Overleaf records. The full repository uses [`just`](https://just.systems/) for maintainer commands; the student package does not depend on `just`.

```bash
just          # list commands
just thesis   # build canonical PDF and SyncTeX
just watch    # continuous incremental rebuild, no extra viewer
just test     # full regression gate
just ci       # canonical CI gate
just clean    # remove rebuildable artifacts
```

Version history: [`CHANGELOG.md`](CHANGELOG.md)

## Other community alternatives

The following community projects are maintained by their respective authors and are neither affiliated with nor endorsed by this project. Verify their versions, licences, and current university rules before use.

- [`Haouo/NCKU-Thesis-Typst`](https://github.com/Haouo/NCKU-Thesis-Typst) — Typst
- [`lycsjm/nckuthesis`](https://github.com/lycsjm/nckuthesis) — LaTeX
- [`windwalker661/Thesis-NCKU`](https://github.com/windwalker661/Thesis-NCKU) — LaTeX
- [`nckuasrlab/ASRLab_Thesis_Template`](https://github.com/nckuasrlab/ASRLab_Thesis_Template) — LaTeX

## Licence

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International licence; see [`LICENSE`](LICENSE). NCKU watermarks, logos, official certificates, and other institution assets may remain owned by their respective rights holders, and the repository-wide licence does not automatically authorize unrelated use or redistribution. Verify provenance and rights before reuse.

<p align="center">
  <img src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" alt="Creative Commons BY-NC-SA 4.0" />
</p>
