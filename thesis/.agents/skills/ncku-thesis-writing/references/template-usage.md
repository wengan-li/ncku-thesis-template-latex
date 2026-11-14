<!-- generated: shared teaching projection; do not edit -->

# Template usage fragments

These fragments are generated from the teaching code, not a second handbook. Replace illustrative titles, labels and data with supplied thesis material. Paths are relative to the matching student project root. Supply an image at `./context/pilot/figure.png` before using the figure fragments. Read the skill for assembly, edit boundaries, compilation and recovery. The teaching corpus and generator are not needed to read or compile this reference.

## Chapter open

<!-- student-snippet: chapter-open -->
```latex
\StartChapter{ Title }{shared:chapter-open}
```

## Sections

<!-- student-snippet: sections -->
```latex
\StartSection{ Title }{shared:section}
\StartSubSection{ Title }{shared:subsection}
\StartSubSubSection{ Title }{shared:subsubsection}
```

## Chapter close

<!-- student-snippet: chapter-close -->
```latex
\EndChapter
```

## Front matter

<!-- student-snippet: front-matter -->
```latex
\StartAbstract


Write your abstract here.

Enjoy this template.




\EndAbstract
\StartAcknowledgments


Thanks someone you want in here.


\EndAcknowledgments
\StartNomChapter{ NAME }{shared:nomenclature}
\EndNomChapter
```

## Appendix

<!-- student-snippet: appendix -->
```latex
\StartAppendix
\StartChapter{ Title }{shared:appendix}
\EndAppendix
```

## Basic text

<!-- student-snippet: basic-text -->
```latex
\begin{enumerate}
\item Item1

\item Item2

\item
{
  Item3

  Item3's context
}

\item
{
  Item4

  Item4's context
}
\end{enumerate}
\begin{itemize}
\item Item1

\item Item2

\item
{
  Item3

  Item3's context
}

\item
{
  Item4

  Item4's context
}
\end{itemize}
```

## Figure

<!-- student-snippet: figure -->
```latex
\InsertFigure
  [caption={Little man No.1},
    label={fig:little-man-no.1}]
  {./context/pilot/figure.png}
```

## Multi figure

<!-- student-snippet: multi-figure -->
```latex
\InsertFigures
[perrow = 2,
  caption = {4 figures and 2 figures per row},
  label = {fig:example:mi3:mfig}]
{
  [caption = {Caption}, label = {fig:example:mi3:fig1}]
  {./context/pilot/figure.png}
}
{
  [caption = {Caption}, label = {fig:example:mi3:fig2}]
  {./context/pilot/figure.png}
}
{
  [caption = {Caption}, label = {fig:example:mi3:fig3}]
  {./context/pilot/figure.png}
}
{
  [caption = {Caption}, label = {fig:example:mi3:fig4}]
  {./context/pilot/figure.png}
}
```

## Table

<!-- student-snippet: table -->
```latex
\InsertTable
  [caption={Hello World in C}]
  {
    \begin{tabular}{ll}
    \hline
    1. & \#include \textless stdio.h\textgreater \\
    2. &  \\
    3. & int main(void) \\
    4. & \{ \\
    5. & \ \ \ \ \ \ \ \ printf("hello, world"); \\
    6. & \} \\ \hline
    \end{tabular}
  }
```

## Equation

<!-- student-snippet: equation -->
```latex
\EquationBegin{eq:example:eq1}
  E = mc^2
\EquationEnd
```

## Theorems

<!-- student-snippet: theorems -->
```latex
\InsertTheorem{Theorem here.}
\InsertProof{Proof here.}
```

## References

<!-- student-snippet: references -->
```latex
\RefEquation{eq:example:eq1}
\RefEquationB{eq:example:eq1}
\RefBib{testpage:bib:paper:mapreduce}
\RefPage{shared:chapter-open}
\RefTo{fig:little-man-no.1}
```

## Citation

<!-- student-snippet: citation -->
```latex
MapReduce: \RefBib{testpage:bib:paper:mapreduce}\\
```

## Bibliography entry

<!-- student-snippet: bibliography-entry -->
```bibtex
@article{testpage:bib:paper:mapreduce,
 author = {Dean, Jeffrey and Ghemawat, Sanjay},
 title = {MapReduce: Simplified Data Processing on Large Clusters},
 journal = {Commun. ACM},
 issue_date = {January 2008},
 volume = {51},
 number = {1},
 month = jan,
 year = {2008},
 issn = {0001-0782},
 pages = {107--113},
 numpages = {7},
 url = {http://doi.acm.org/10.1145/1327452.1327492},
 doi = {10.1145/1327452.1327492},
 acmid = {1327492},
 publisher = {ACM},
 address = {New York, NY, USA},
}
```

## Bibliography registration

<!-- student-snippet: bibliography-registration -->
```latex
\ReferencesFiles{context/references/paper}{context/references/misc}{context/references/book}
```

## Direct build

<!-- student-snippet: direct-build -->
```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```
