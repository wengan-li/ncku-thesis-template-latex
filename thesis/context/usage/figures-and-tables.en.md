<!-- doc-pair: writing-figures-and-tables; lang: en; topics: single-figure,multi-figure,tables -->

[繁體中文](figures-and-tables.md) | [English](figures-and-tables.en.md)

# Figures and tables

## Single images and paths

Use `\InsertFigure[options]{image path}` inside a chapter; the [complete writing chapter](project-and-chapters.en.md) supplies a minimal example. Supply an image you have permission to use and give its path relative to the project root. The default `scale=1.0` keeps its natural size and `angle=0` applies no rotation. Caption and label default to empty. Brace a caption containing commas.

The frame defaults to `opacity=0.4`. The figure uses `[H]`; accepted `pos` and `align` keys do not change placement or alignment. Reduce scale for an oversized image. For a missing file, check the path, letter case and extension. Use a label with a caption so the image has a reliable figure number to reference.

## Multiple images

`\InsertFigures[options]{first specification}{second specification}...` accepts up to eight images. Each specification is a braced group containing `[sub-options]{image path}`. Supported perrow values are 1, 2, 3 and 4; the default is 1. Overall caption and label default to empty; opacity defaults to 0.4. Subimages default to scale 1.0, angle 0 and empty caption/label. Outer and subimage align keys do not control alignment. The outer float still uses `[H]`.

<!-- student-snippet: multi-figure -->
```latex
\InsertFigures[perrow=2,caption={Two supplied views},label={fig:pilot-views}]
  {[scale=0.2,caption={First view},label={fig:pilot-first}]{./context/pilot/figure.png}}
  {[scale=0.2,caption={Second view},label={fig:pilot-second}]{./context/pilot/figure.png}}
See Figure \RefFigure{fig:pilot-views}.
```

## Tables and caption position

`\InsertTable[options]{table content}` accepts content such as tabular. The default scale 0.0 keeps natural width; a nonzero scale uses a fraction of paper width. Defaults are tabcolsep 6pt, arraystretch 1, opacity 0.4 and empty caption/label/nomtitle. `pos=top` places the caption above; another value places it below. It does not control float placement: the table uses `[H]`. Use caption for a numbered table. Nomtitle is an unnumbered heading and is unsuitable when a table-number reference is needed.

<!-- student-snippet: table -->
```latex
\InsertTable[caption={Illustrative symbols},label={tab:pilot-symbols},pos=top]{
  \begin{tabular}{ll}
    Symbol & Meaning \\
    $x$ & Variable \\
  \end{tabular}
}
See Table \RefTable{tab:pilot-symbols}.
```
