<!-- doc-pair: writing-figures-and-tables; lang: zh-Hant-TW; topics: single-figure,multi-figure,tables -->

[繁體中文](figures-and-tables.md) | [English](figures-and-tables.en.md)

# 圖片與表格

## 單張圖片與路徑

在章節內使用 `\InsertFigure[選項]{圖片路徑}`，最小範例見[完整寫作章節](project-and-chapters.md)。先取得授權使用的圖片，按專案根目錄填寫相對路徑。`scale=1.0` 是原始大小的預設值，`angle=0` 不旋轉；caption 與 label 預設空白。圖說包含逗號時須用大括號包住。

圖框預設 `opacity=0.4`。figure 固定使用 `[H]`；`pos`、`align` 雖可接受，但不改變位置或對齊。圖片過寬須調低 scale；找不到檔案時核對路徑、大小寫及副檔名。標籤配合圖說使用，否則沒有可可靠引用的圖片編號。

## 多張圖片

`\InsertFigures[選項]{第一張規格}{第二張規格}...` 最多八張，每個規格是包住 `[子選項]{圖片路徑}` 的一組大括號。`perrow` 支援 1、2、3、4，預設 1；總圖說及標籤預設空白，opacity 預設 0.4。子圖 scale 預設 1.0、angle 預設 0，caption/label 預設空白。外層及子圖 align 不控制對齊，外層仍是 `[H]`。

<!-- student-snippet: multi-figure -->
```latex
\InsertFigures[perrow=2,caption={Two supplied views},label={fig:pilot-views}]
  {[scale=0.2,caption={First view},label={fig:pilot-first}]{./context/pilot/figure.png}}
  {[scale=0.2,caption={Second view},label={fig:pilot-second}]{./context/pilot/figure.png}}
See Figure \RefFigure{fig:pilot-views}.
```

## 表格與圖說位置

`\InsertTable[選項]{表格內容}` 接受 tabular 等內容。scale 預設 0.0，保留自然寬度；非零時以紙寬比例縮放。tabcolsep 預設 6pt、arraystretch 預設 1、opacity 預設 0.4，caption/label/nomtitle 預設空白。`pos=top` 將圖說放上方，其他值放下方；此選項不控制浮動位置，表格仍使用 `[H]`。一般編號表格用 caption；nomtitle 是不編號標題，不適合需要表格編號引用的情況。

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
