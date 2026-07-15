# NCKU thesis template — student project

This directory is the complete student project. The versioned GitHub Release ZIP contains these files directly under one `ncku-thesis-template-latex/` directory; repository development tools, tests, and release scripts are intentionally excluded.

## Start writing

1. Open `conf/conf.tex` and comment out `\ExampleMode` when writing your own thesis.
2. Fill in thesis metadata and options in `conf/conf.tex`.
3. Write and select your chapters in `context/context.tex` and the files under `context/`.
4. Use `thesis.tex` as the main document.

The large document selected by `\ExampleMode` is the complete teaching example. It is useful as a reference but is slower to rebuild than a normal thesis using `context/context.tex`.

## Draft and institutional watermark

The student project defaults to final-ready output: no `(Draft)` / `(初稿)` cover marker, no diagonal `DRAFT` text layer, and no institutional logo watermark. During writing or review, uncomment `\DisplayDraft` in `conf/conf.tex` only when you deliberately want the cover marked as a draft; keep it disabled for final output. A diagonal text watermark is a separate `draftwatermark` package feature and must also be enabled explicitly.

The template retains `\UseWatermarkFigureStyle` and `\UseWatermarkTextStyle` as explicit compatibility/customization APIs, but it does not enable either one by default. Do not add a template watermark to the submission PDF merely because the API exists. Follow the current university, library, and department instructions; the school system may apply its own watermark to the approved electronic copy.

## Build the final document

Install a distribution with XeLaTeX, BibTeX, `latexmk`, and LaTeX2e format 2020-10-01 or newer. TeX Live 2021 or newer is recommended; release CI uses TeX Live 2026. Then run this command from the project directory:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

`latexmk` automatically runs XeLaTeX and BibTeX as many times as required for the table of contents, bibliography, references, and PDF outline to converge. Do not guess or hard-code a manual sequence of compiler runs.

To remove generated build files:

```bash
latexmk -C thesis.tex
```

## Continuous preview while writing

Keep the following command running in a terminal:

```bash
latexmk -xelatex -pvc -view=none -synctex=1 -interaction=nonstopmode thesis.tex
```

Whenever a tracked TeX, bibliography, figure, or included file changes, `latexmk` rebuilds only the required compiler passes. `-view=none` prevents it from opening a second viewer; keep the PDF open in Texmaker, TeXstudio, or another viewer that automatically reloads changed PDFs.

Stop continuous preview with `Ctrl-C`.

## Texmaker and TeXstudio

Set the document compiler or user command to:

```text
latexmk -xelatex -synctex=1 -interaction=nonstopmode %.tex
```

Use `thesis.tex` as the root/master document. For an external continuous-preview command, run:

```text
latexmk -xelatex -pvc -view=none -synctex=1 -interaction=nonstopmode thesis.tex
```

The exact menu name differs by editor version. The important behavior is that the editor invokes `latexmk` with XeLaTeX and opens/reloads `thesis.pdf`; it should not require you to run XeLaTeX and BibTeX manually in a guessed order.

## Other 其他

如果對本模版沒有興趣，也可以參考其他同學提供、但不定期更新的社群模版：

- [`Haouo/NCKU-Thesis-Typst`](https://github.com/Haouo/NCKU-Thesis-Typst) — 使用 Typst 的成大論文模版
- [`lycsjm/nckuthesis`](https://github.com/lycsjm/nckuthesis) — 使用 LaTeX 的成大論文模版
- [`windwalker661/Thesis-NCKU`](https://github.com/windwalker661/Thesis-NCKU) — 使用 LaTeX 的成大論文模版
- [`nckuasrlab/ASRLab_Thesis_Template`](https://github.com/nckuasrlab/ASRLab_Thesis_Template) — 使用 LaTeX 的成大論文模版

以上外部專案並非由本專案維護；使用前請自行核對其版本、授權及學校最新規定。

## Before submission

1. Stop any continuous-preview process.
2. Run the normal final build command again.
3. Check the log for unresolved references or citations.
4. Confirm that the final PDF has no `(Draft)` / `(初稿)` marker, diagonal `DRAFT` text, or template-added institutional logo watermark unless a current official requirement explicitly asks for one.
5. Review the complete PDF, page numbering, contents, lists, bibliography, fonts, and official school requirements.
6. Use the official school-generated defense-certificate document when required; template-generated demonstrations are not official documents.
