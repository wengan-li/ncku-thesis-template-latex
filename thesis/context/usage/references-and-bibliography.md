<!-- doc-pair: writing-references-and-bibliography; lang: zh-Hant-TW; topics: entries,citations,registration -->

[繁體中文](references-and-bibliography.md) | [English](references-and-bibliography.en.md)

# 引用與 BibTeX 文獻

## 加入真實文獻

將經查證的資料放入 `context/references/paper.bib` 等檔。以下是專案既有的 Dean 與 Ghemawat 文獻，供寫作示範使用；只有研究確實引用時才保留。重複的 key 會造成 BibTeX 錯誤，先檢查現有資料。資料不足時要求提供，不能補造作者、年份或 DOI。

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

## 在正文引用

使用 `\RefBib{testpage:bib:paper:mapreduce}`，其行為是 `\cite{key}`。沿用既有文獻樣式，不遷移至其他文獻系統。完整章節已示範引用；新增來源須保留真實的 citation key。

## 註冊檔案與完成建置

`context/references/references.tex` 已包含以下三個資料庫，不必為新增一筆文獻再次註冊。`\ReferencesFiles` 接受最多九組可省略的大括號路徑，省略 .bib；此指令同時輸出文獻列表，放在正文之後。不要將空白或缺檔路徑當作有效資料庫。

<!-- student-snippet: bibliography-registration -->
```latex
\ReferencesFiles{context/references/paper}{context/references/misc}{context/references/book}
```

`Citation ... undefined` 時先比對 key，再確認資料庫已註冊；`I couldn't open database file` 表示路徑錯誤。[建置與診斷](build-and-diagnostics.md) 說明如何完成 XeLaTeX/BibTeX 重跑。PDF 存在不代表引用已收斂。
