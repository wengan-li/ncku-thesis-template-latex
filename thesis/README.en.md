<!-- doc-pair: student-readme; lang: en; topics: start-writing,choose-independent-settings,configure-thesis-information,migrate-from-1-x,build-the-final-document,continuous-preview-and-editors,use-overleaf,draft-watermark-and-certificate,common-errors,before-submission,other-community-alternatives -->

[繁體中文](README.md) | [English](README.en.md)

# NCKU thesis-template student project

This directory is the complete student project. The versioned GitHub Release student package places these files directly under one `ncku-thesis-template-latex/` directory; repository tests, release scripts, and repository-only tooling are intentionally excluded. The package licence is in [`LICENSE`](LICENSE).

## Start writing

1. Open `conf/conf.tex`. Comment out `\ExampleMode` for your own thesis; when enabled, it builds the complete teaching example.
2. Follow [`conf/README.en.md`](conf/README.en.md) to enter the title, names, degree, dates, department, advisors, and other thesis information.
3. Select chapters in `context/context.tex` and write your content under `context/`.
4. Always use `thesis.tex` as the root document.

`conf/conf.tex` ships configured for the teaching example. Change the following lines to your own data (line numbers are fixed, so jump straight to them):

| Item | `conf/conf.tex` line | What to do | If left unchanged |
| --- | --- | --- | --- |
| Content mode | 13 | Put `%` in front of `\ExampleMode` | Builds the 271-page teaching document instead of your thesis |
| Cover language | 44 | Keep `\DisplayCoverInEng` or switch to `\DisplayCoverInChi` | Cover language does not match the department rule |
| Title | 71–73 | `\SetTitle{中文題目}{English Title}`; the library requires both titles | Cover prints the template's own name |
| Degree | 99 | Master's students switch to `\MasterDegree`; doctoral students keep `\PhdDegree` | Cover and certificate show the wrong degree |
| Name | 111 | `\SetMyName{中文姓名}{English Name}` | Cover prints "Your name" |
| Oral exam date | 125 | `\SetOralDate{year}{month}{day}` in the Gregorian calendar | Cover date stays at December 2023 |
| Cover date | 138 | NCKU students leave it; the `ncku` setup derives it from the oral date | — |
| Department | 148 | Replace with your department command; search the Chinese name in [`template/style/ncku/README.md`](template/style/ncku/README.en.md) | Cover shows the shipped computer-science department |
| Advisors | 166–168 | Fill in `\SetAdvisorNameA`; with one advisor **delete** the B and C lines | Cover gains "Dr. B" and "Dr. C" |
| Certificate | 204–206 | Put the certificate PDF from the university system in `context/oral/`, uncomment, and enter the file name | The certificate page is silently omitted |
| Keywords | 224, 246–248 | Replace with your keywords | PDF metadata and abstracts show the template's keywords |

For a Chinese-language thesis, also uncomment the Chinese abstract, the extended English abstract, and the Chinese acknowledgements `\input` lines in `context/context.tex`; only the English versions are enabled as shipped.

The teaching example is useful as a reference but rebuilds more slowly than a normal thesis.

## Choose independent settings

Documentation language, institution profile, cover language, degree, and content mode are independent. An international student may use the NCKU `ncku` profile, while students from other institutions can create a profile for their own school. Do not select an institution profile from the reader's language.

| Decision | Choices |
| --- | --- |
| Institution | default `ncku` for NCKU students; custom profile for students from another institution |
| Cover language | `\DisplayCoverInChi` or `\DisplayCoverInEng` |
| Degree | `\MasterDegree` or `\PhdDegree` |
| Content | own `context/context.tex` or `\ExampleMode` teaching example |

The default project selects the NCKU profile in `template/style/style.tex`. Students from other institutions can follow [`template/style/Customization.en.md`](template/style/Customization.en.md) to create their own institution profile.

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

The electronic submission needs only `thesis.pdf`, which already contains the inner cover. A printed copy (hardback or paperback) also needs the cover file for the print shop, built from `cover.tex`:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode cover.tex
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

## Use Overleaf

To avoid installing TeX, use the [public template on Overleaf](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn):

1. Open the template page and choose "Open as Template" to copy it into your account.
2. In the Menu, confirm Compiler is XeLaTeX and Main document is `thesis.tex`.
3. Recompile; choose "Recompile from scratch" when a full rebuild is needed.

The Overleaf template ships with `\ExampleMode` and the draft marker already off, so fill in `conf/conf.tex` directly. The free plan has a compile time limit; do not enable `\ExampleMode` on Overleaf to build the 271-page teaching document. The Overleaf template and GitHub Releases are updated independently and the Overleaf copy may be older; for the newest fixes, download the student package from GitHub Releases and build locally.

## Draft, watermark, and certificate

Final output defaults to no `(初稿)` / `(Draft)` cover marker, no diagonal `DRAFT` text, and no institution-logo watermark. Enable `\DisplayDraft` in `conf/conf.tex` only when deliberately required during writing or review. Diagonal text and institution-logo watermarks are two separate explicit opt-ins; do not add either to a submission PDF merely because the APIs exist. The university system may apply its own watermark to the approved electronic copy.

For final submission, use the defense-certificate document produced by the official degree-examination system when required. Template-generated certificates are legacy/example and regression outputs, not official documents.

## Common errors

| What you see | Cause | Fix |
| --- | --- | --- |
| A 271-page teaching document is built | `\ExampleMode` on line 13 of `conf/conf.tex` is still active | Put `%` in front of that line and rebuild |
| `! LaTeX Error: File 'xxx.sty' not found.` | The TeX distribution lacks a package | MiKTeX: install it in MiKTeX Console or enable automatic installation; TeX Live/MacTeX: `tlmgr install <package>`, or install the full scheme |
| `! Undefined control sequence.` followed by a `\SetDept...` line | The department command is misspelled or does not exist | Look up the command in [`template/style/ncku/README.md`](template/style/ncku/README.en.md) |
| `! fontspec error: "font-not-found"` | `template/fonts/` is incomplete, or the build did not run from the directory containing `thesis.tex` | Re-extract the package and run the build command from the project root |
| Citations show `[?]` and the log says `Citation ... undefined` | A `.bib` key does not match `\cite{}`, or a new citation has not converged yet | Check the key and run the final-build command once more; if the warning persists, run `latexmk -C thesis.tex` first |
| The build fails after changing `BibStyle` | Old `.aux`/`.bbl` files are incompatible with the new style | Run `latexmk -C thesis.tex` and rebuild |
| The certificate page does not appear | `\SetOralImageChi`/`\SetOralImageEng` are still commented out, or the file name does not match a file in `context/oral/` | Uncomment and enter the correct file name |
| Chinese text shows as garbage or boxes | The file is not saved as UTF-8 | Re-save with a UTF-8 capable editor (older Windows Notepad defaults to ANSI) |
| Overleaf reports a compile timeout | The teaching example is being built on Overleaf, or a full rebuild is needed | Keep `\ExampleMode` off; choose "Recompile from scratch" |

## Before submission

1. Stop any continuous-preview process and run the final-build command again.
2. Confirm that the log contains no unresolved references, citations, or rerun warnings.
3. Confirm that the PDF has no unexpected Draft marker, text watermark, or logo watermark.
4. Cover: both titles present, name and degree correct, cover date consistent with the oral exam date, and only the real advisors listed (unused B and C lines deleted).
5. The certificate page appears and is the version produced by the university system.
6. Abstracts: local and overseas Chinese students need Chinese and English abstracts, and a Chinese-language thesis also needs the extended English abstract; international students may omit the Chinese abstract under university rules.
7. Review pagination, contents, figure/table lists, bibliography, fonts, and final pages.
8. Check the current NCKU, library, and department requirements; current official rules always take precedence.
9. Use the official certificate and submission workflow required by the university system.

## Other community alternatives

If this template does not meet your needs, evaluate the following independently maintained community projects. They are not maintained by this project; verify their versions, licences, and current university requirements before use.

- [`Haouo/NCKU-Thesis-Typst`](https://github.com/Haouo/NCKU-Thesis-Typst) — Typst
- [`lycsjm/nckuthesis`](https://github.com/lycsjm/nckuthesis) — LaTeX
- [`windwalker661/Thesis-NCKU`](https://github.com/windwalker661/Thesis-NCKU) — LaTeX
- [`nckuasrlab/ASRLab_Thesis_Template`](https://github.com/nckuasrlab/ASRLab_Thesis_Template) — LaTeX
