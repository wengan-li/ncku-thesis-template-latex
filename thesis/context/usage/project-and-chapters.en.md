<!-- doc-pair: writing-project-and-chapters; lang: en; topics: own-thesis,chapters,text,front-matter -->

[繁體中文](project-and-chapters.md) | [English](project-and-chapters.en.md)

# Project and chapters

## Select own-thesis content

In the complete student project, `thesis.tex` is the root document, `conf/conf.tex` holds student data and `context/context.tex` selects content and order. Comment out `\ExampleMode` in `conf/conf.tex` to load your own content; leaving it active builds the teaching document. Complete the data listed in the project README and conf/README first. Keep template internals intact. Documentation language does not select institution, cover language or degree.

## Add and order chapters

Create `context/pilot/pilot.tex` with the complete chapter below. First supply your own image at `context/pilot/figure.png` and add the existing real source listed in the bibliography reference. Demonstration text is not a research result. All paths are relative to the student project root. Add `\input{./context/pilot/pilot}` before the bibliography input in `context/context.tex`; reorder input lines to reorder chapters.

The second braced argument in `\StartChapter{title}{label}` and `\StartSection{title}{label}` is optional, not a square-bracket option. `\StartSubSection` and `\StartSubSubSection` use the same form. End a chapter with `\EndChapter`. Labels must be unique; use `\RefTo{label}` or `\RefPage{label}` instead of typing numbers.

<!-- student-snippet: pilot-chapter -->
```latex
\StartChapter{Writing pilot}{chap:writing-pilot}
\StartSection{Supplied material}{sec:writing-pilot}
This demonstration cites \RefBib{testpage:bib:paper:mapreduce}.
The source is MapReduce: Simplified Data Processing on Large Clusters.
\InsertFigure[scale=0.4,caption={Supplied pilot image},label={fig:writing-pilot}]
  {./context/pilot/figure.png}
See Figure \RefFigure{fig:writing-pilot} and Section \RefTo{sec:writing-pilot}.
\EndChapter
```

See [figures and tables](figures-and-tables.en.md) for image details and [references and bibliography](references-and-bibliography.en.md) for source preparation.

## Text and lists

Use ordinary LaTeX for paragraphs, inline mathematics and lists. A blank line starts a paragraph. Escape special text characters; otherwise `Missing $ inserted` or a comment may hide content.

<!-- student-snippet: basic-text -->
```latex
An escaped percentage is 50\%; write \&, \_ and \# as text.
\begin{itemize}
  \item A supplied observation.
\end{itemize}
\begin{enumerate}
  \item An ordered step.
\end{enumerate}
```

## Abstracts, acknowledgments, nomenclature and appendices

`context/context.tex` selects the existing `abstract/`, `acknowledgments/` and `nomenclature/` files. Keep their opening/closing commands and replace their content; select the needed language. Current department and university rules determine abstract and extended-abstract requirements. The example shows the paired English abstract, acknowledgment and nomenclature commands. Do not duplicate sections already enabled.

<!-- student-snippet: front-matter -->
```latex
\StartAbstract
Supplied abstract text.
\EndAbstract
\StartAcknowledgments
Supplied acknowledgments.
\EndAcknowledgments
\StartNomChapter{Nomenclature}{chap:pilot-nomenclature}
Supplied notation: $x$ is a variable.
\EndNomChapter
```

Place appendices after the bibliography. `\StartAppendix` takes no arguments and switches subsequent chapter numbering. `\EndAppendix` ends the page without restoring ordinary chapter mode, so keep appendices last.

<!-- student-snippet: appendix -->
```latex
\StartAppendix
\StartChapter{Supplement}{chap:pilot-appendix}
Supplied supplementary material.
\EndAppendix
```
