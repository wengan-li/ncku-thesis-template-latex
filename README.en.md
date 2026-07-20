<!-- doc-pair: root-readme; lang: en; topics: project-overview,start-by-need,quick-start,choose-the-correct-setup,downloads-and-examples,migrate-from-1-x,other-institution-profiles,historical-acceptance,thesis-upload-and-printing,defense-certificate-faq,documentation-and-project-work,other-community-alternatives,licence -->

[繁體中文](README.md) | [English](README.en.md)

# NCKU Thesis and Dissertation Template for LaTeX

[Open as Template in Overleaf](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)

## Project overview

This XeLaTeX template supports Chinese, English, and mixed-language NCKU master's theses and doctoral dissertations. It generates the cover, contents, figure/table lists, and other front matter, and provides student configuration, reusable LaTeX helpers, a 1.x compatibility adapter, and profiles that students from other institutions can adapt.

This is not official NCKU software and does not represent current endorsement by the university, library, degree-examination system, or any department. Verify the current rules before use; official requirements always take precedence.

Official guidance last checked on `2026-07-12`:

- [NCKU thesis system](https://thesis.lib.ncku.edu.tw/)
- [Submission guidance](https://thesis.lib.ncku.edu.tw/help/aboutedit/)
- [Curriculum Division thesis-format guidance](https://cid-acad.ncku.edu.tw/p/412-1042-1378.php?Lang=zh-tw)

## Start by need

| What you want to do | Start here |
| --- | --- |
| Start writing a thesis now | [Quick start](#quick-start) and the student-package [`README.en.md`](thesis/README.en.md) |
| Enter names, titles, degree, and department | [`conf/README.en.md`](thesis/conf/README.en.md) |
| Upgrade a 1.x project | [1.x-to-2.x migration guide](docs/v1-to-v2-migration.en.md) |
| Create a style for another institution | [`Customization.en.md`](thesis/template/style/Customization.en.md) |
| Upload, print, and choose the official certificate | [Thesis upload and printing](#thesis-upload-and-printing) |
| Review architecture, validation, releases, and Overleaf records | [`docs/README.en.md`](docs/README.en.md) |

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

## Choose the correct setup

Documentation language, institution profile, cover language, degree, and content mode are separate settings. NCKU students use the `ncku` profile whether they write in Chinese or English; students from other institutions can use `custom` or another institution profile.

| Decision | Choices |
| --- | --- |
| Institution | default `ncku` for NCKU students; custom profile for students from another institution |
| Cover language | `\DisplayCoverInChi` or `\DisplayCoverInEng` |
| Degree | `\MasterDegree` or `\PhdDegree` |
| Content | own `context/context.tex` or `\ExampleMode` teaching example |

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

The template separates shared rendering, NCKU policy, and other-institution ports into `base`, `ncku`, and `custom`. Student thesis data remains in `conf/conf.tex`; institution geometry, names, date policy, wording, and assets belong under `template/style/<profile>/`. `custom` is a neutral skeleton, not a ready-to-submit profile for any named institution; this repository currently has no NTU profile. Students from other institutions start from `template/style/custom/` rather than editing the shared renderer or loading NCKU before overriding it.

NCKU students can use the complete [`9-college / 110-department preset catalogue`](thesis/template/style/ncku/README.en.md). Students from other institutions use the generic institution APIs and can follow the explicitly illustrative NTU wiring in [`Customization.en.md`](thesis/template/style/Customization.en.md).

Guide: [`thesis/template/style/Customization.en.md`](thesis/template/style/Customization.en.md)

## Available to use / historical acceptance

According to records preserved by the project, the template's format/design was checked by the NCKU Library's digital-thesis team in 2015. The Curriculum Division also checked the Chinese and English defense certificates generated at that time. In 2018, the Division separately stated that the template-generated Chinese certificate was unauthorized.

These are historical checks, not evidence that the university, library, degree-examination system, or any department currently accepts every template setting. CSIE is the only department for which the project preserves documented historical use, and that record is not current approval. Verify the rules for the current year and department before use.

## Thesis upload and printing

The following summary follows the NCKU thesis system's [submission guidance](https://thesis.lib.ncku.edu.tw/help/aboutedit/) (last checked by the project on `2026-07-19`). The process may change; follow the current official system and department notices when submitting.

1. Create the PDF from the final version that meets department requirements and has the advisor's approval for printing.
2. Combine the cover, defense certificate, Chinese and English abstracts, contents, figure/table lists, main text, references, and appendices into one PDF. Check pagination, figures, tables, and layout.
3. Do not add a watermark or security restrictions to the uploaded PDF; the system processes the approved full-text copy.
4. Sign in to the [NCKU thesis system](https://thesis.lib.ncku.edu.tw/), complete the metadata and upload steps, and submit the record for review.
5. After receiving the approval email, sign in again and use step 5 to print the authorization form and download the approved full-text PDF. Confirm paper-copy counts, signatures, and graduation procedures with the department and library.

## FAQ: template and degree-examination-system defense certificates

Project records show that the relevant Chinese and English certificates were checked by the Curriculum Division in 2015; the response at that time was not formal university approval. In 2018, the Division stated that the template-generated Chinese certificate was unauthorized. See [Issue #30: the template certificate differs from the NCKU degree-examination-system certificate](https://github.com/wengan-li/ncku-thesis-template-latex/issues/30) for the historical discussion.

Current usage principles:

1. Prefer the official Chinese defense certificate generated by the degree-examination system, and follow the current university and department requirements.
2. Template-generated certificates are for legacy/example use and layout preview only; they are not official documents or evidence of current authorization.
3. Departments may set separate requirements for an English certificate. Confirm its version, wording, and signature requirements before use.
4. If anything is uncertain before the defense, signature collection, or submission, obtain the current official system version rather than relying only on a template-generated certificate.

Policy record: [release, certificate, and watermark policy](docs/features/release-and-distribution.en.md#draft-and-watermark-policy).

## Documentation and project work

If you only need to write a thesis, start from the packaged README and configuration guide. Project architecture, validation, release, and Overleaf evidence are recorded in [`docs/README.en.md`](docs/README.en.md). The full repository uses [`just`](https://just.systems/) for project commands; the student package does not depend on `just`.

```bash
just          # list commands
just thesis   # build canonical PDF and SyncTeX
just watch    # continuous incremental rebuild, no extra viewer
just test     # full regression gate
just ci       # canonical CI gate
just clean    # remove rebuildable artifacts
```

Version history: [`CHANGELOG.en.md`](CHANGELOG.en.md)

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
