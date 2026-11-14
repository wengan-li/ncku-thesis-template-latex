<!-- doc-pair: writing-references-and-bibliography; lang: en; topics: entries,citations,registration -->

[繁體中文](references-and-bibliography.md) | [English](references-and-bibliography.en.md)

# References and BibTeX

## Add a real source

Put verified metadata in a file such as `context/references/paper.bib`. This existing Dean and Ghemawat entry from the project is supplied for the writing demonstration. Keep it in a thesis only if the research actually cites it. Check existing keys first: duplicates cause BibTeX errors. Request missing metadata instead of inventing authors, years or DOIs.

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

## Cite in the text

Use `\RefBib{testpage:bib:paper:mapreduce}`, which delegates to `\cite{key}`. Keep the existing bibliography style and system. The complete chapter demonstrates the citation. Preserve real citation keys when adding sources.

## Register files and converge

`context/references/references.tex` already registers these three databases; adding an entry does not require another registration. `\ReferencesFiles` accepts up to nine optional braced database paths without .bib. It also prints the bibliography, so place it after the main text. Do not supply blank or missing database paths.

<!-- student-snippet: bibliography-registration -->
```latex
\ReferencesFiles{context/references/paper}{context/references/misc}{context/references/book}
```

For `Citation ... undefined`, compare the key and check database registration. `I couldn't open database file` means the path is wrong. [Build and diagnostics](build-and-diagnostics.en.md) explains the XeLaTeX/BibTeX reruns. A PDF alone does not prove citation convergence.
