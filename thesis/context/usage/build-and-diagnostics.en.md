<!-- doc-pair: writing-build-and-diagnostics; lang: en; topics: build,diagnostics -->

[繁體中文](build-and-diagnostics.md) | [English](build-and-diagnostics.en.md)

# Build and diagnostics

## Build from the student project root

In a terminal, enter the student project directory containing `thesis.tex`, `conf/` and `template/configure.tex`, then run:

<!-- student-snippet: direct-build -->
```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

In Overleaf, select `thesis.tex` as the main document and XeLaTeX as the compiler; recompile from scratch when necessary. In TeXstudio or Texmaker, set the same root document and use a latexmk chain with XeLaTeX and BibTeX. If tools are absent, use the complete project README to prepare the environment. An agent must not install tools or change global settings on its own. A context-only copy needs a matching complete thesis template first.

## Read errors and verify output

Start with the first error in the log. For `File ... not found`, check the root directory, path and case. For `Undefined control sequence`, check spelling and template compatibility. For `Missing $ inserted`, check unescaped underscores and math mode. See the [bibliography page](references-and-bibliography.en.md) for citation errors. If teaching content still appears, check ExampleMode.

Require an actual PDF and SyncTeX file. The final log must contain no unresolved/undefined citations, undefined references or rerun requests. Check the new text, captions, images, reference numbers and bibliography, then inspect affected PDF pages for clipping and pagination. Report the actual command and result; editing success is not compilation success. Current official certificate and layout requirements still apply before submission.

For an agent session at repository root, verify the root and check its thesis/ child for the three required runtime markers. When a content target is supplied, use that path and its ancestors. If no matching runtime exists, report the missing complete template instead of borrowing an unrelated project.
