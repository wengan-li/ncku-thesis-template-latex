<!-- doc-pair: student-readme; lang: en; topics: start-writing,choose-independent-settings,configure-thesis-information,migrate-from-1-x,build-the-final-document,continuous-preview-and-editors,draft-watermark-and-certificate,before-submission,other-community-alternatives -->

[繁體中文](README.md) | [English](README.en.md)

# NCKU thesis-template student project

This directory is the complete student project. The versioned GitHub Release student package places these files directly under one `ncku-thesis-template-latex/` directory; repository tests, release scripts, and maintainer tooling are intentionally excluded.

## Start writing

1. Open `conf/conf.tex`. Comment out `\ExampleMode` for your own thesis; when enabled, it builds the complete teaching example.
2. Follow [`conf/README.en.md`](conf/README.en.md) to enter the title, names, degree, dates, department, advisors, and other thesis information.
3. Select chapters in `context/context.tex` and write your content under `context/`.
4. Always use `thesis.tex` as the root document.

The teaching example is useful as a reference but rebuilds more slowly than a normal thesis.

## Choose independent settings

Documentation language, institution profile, cover language, degree, and content mode are independent. An international student may use the NCKU `ncku` profile, while a Taiwan reader may maintain another institution profile. Do not select an institution profile from the reader's language.

| Decision | Choices |
| --- | --- |
| Institution | default `ncku`; maintained custom profile for another institution |
| Cover language | `\DisplayCoverInChi` or `\DisplayCoverInEng` |
| Degree | `\MasterDegree` or `\PhdDegree` |
| Content | own `context/context.tex` or `\ExampleMode` teaching example |

The default project selects the NCKU profile in `template/style/style.tex`. Follow [`template/style/Customization.en.md`](template/style/Customization.en.md) only when maintaining a non-NCKU institutional fork.

## Configure thesis information

`conf/conf.tex` is the compatibility-preserved configuration file from v1.8.2. It remains byte-identical throughout 2.x so existing projects can migrate safely, and its original comments are therefore mainly Chinese. Use the packaged English [`conf/README.en.md`](conf/README.en.md) for a field-by-field guide. Do not rename macros or add `conf/style.tex` merely for translation.

Student metadata belongs in `conf/`; institution geometry, wording, date policy, and assets belong under `template/style/<profile>/`.

## Migrate from 1.x

V2 preserves the complete machine-audited 1.x helper surface through a compatibility adapter. Before migrating a thesis in progress, commit or archive the complete 1.x project and save its latest PDF. Preserve `conf/conf.tex`, `context/`, figures, bibliography data, and local certificate files; replace template-owned files with V2 and deliberately merge local edits to `thesis.tex`. Then run the direct build command below and compare the cover, dates, contents, citations, bibliography, body, and final pages.

The complete compatibility-first and native-v2 paths are maintained at [`docs/v1-to-v2-migration.en.md`](https://github.com/wengan-li/ncku-thesis-template-latex/blob/main/docs/v1-to-v2-migration.en.md). Existing 1.x helper calls do not require renaming during 2.x.

## Build the final document

Install a TeX distribution containing XeLaTeX, BibTeX, and `latexmk`. The minimum LaTeX2e format is 2020-10-01; TeX Live 2021 or newer is recommended, and release CI currently uses TeX Live 2026. Run the following canonical final-build command from the project root containing `thesis.tex`.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

`latexmk` automatically runs XeLaTeX and BibTeX until the table of contents, bibliography, references, and PDF outline converge. Do not guess a manual sequence of compiler runs.

To remove generated files:

```bash
latexmk -C thesis.tex
```

## Continuous preview and editors

Keep the following command running while writing. Whenever a tracked TeX, bibliography, figure, or included file changes, `latexmk` runs only the required compiler passes. `-view=none` prevents a second PDF viewer from opening; let Texmaker, TeXstudio, or another viewer reload the existing `thesis.pdf`. Stop with `Ctrl-C`.

```bash
latexmk -xelatex -pvc -view=none -synctex=1 -interaction=nonstopmode thesis.tex
```

Texmaker/TeXstudio compiler command:

```text
latexmk -xelatex -synctex=1 -interaction=nonstopmode %.tex
```

Set `thesis.tex` as the root/master document.

## Draft, watermark, and certificate

Final output defaults to no `(初稿)` / `(Draft)` cover marker, no diagonal `DRAFT` text, and no institution-logo watermark. Enable `\DisplayDraft` in `conf/conf.tex` only when deliberately required during writing or review. Diagonal text and institution-logo watermarks are two separate explicit opt-ins; do not add either to a submission PDF merely because the APIs exist. The university system may apply its own watermark to the approved electronic copy.

For final submission, use the defense-certificate document produced by the official degree-examination system when required. Template-generated certificates are legacy/example and regression outputs, not official documents.

## Before submission

1. Stop any continuous-preview process and run the final-build command again.
2. Confirm that the log contains no unresolved references, citations, or rerun warnings.
3. Confirm that the PDF has no unexpected Draft marker, text watermark, or logo watermark.
4. Review pagination, contents, figure/table lists, bibliography, fonts, and final pages.
5. Check the current NCKU, library, and department requirements; current official rules always take precedence.
6. Use the official certificate and submission workflow required by the university system.

## Other community alternatives

If this template does not meet your needs, evaluate the following independently maintained community projects. They are not maintained by this project; verify their versions, licences, and current university requirements before use.

- [`Haouo/NCKU-Thesis-Typst`](https://github.com/Haouo/NCKU-Thesis-Typst) — Typst
- [`lycsjm/nckuthesis`](https://github.com/lycsjm/nckuthesis) — LaTeX
- [`windwalker661/Thesis-NCKU`](https://github.com/windwalker661/Thesis-NCKU) — LaTeX
- [`nckuasrlab/ASRLab_Thesis_Template`](https://github.com/nckuasrlab/ASRLab_Thesis_Template) — LaTeX
