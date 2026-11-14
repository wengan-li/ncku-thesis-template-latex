<!-- doc-pair: writing-project-and-chapters; lang: zh-Hant-TW; topics: own-thesis,chapters,text,front-matter -->

[繁體中文](project-and-chapters.md) | [English](project-and-chapters.en.md)

# 專案與章節

## 切換自己的論文

在完整學生專案內，`thesis.tex` 是根文件，`conf/conf.tex` 保存學生資料，`context/context.tex` 決定內容與順序。將 `conf/conf.tex` 中的 `\ExampleMode` 註解掉，才會載入自己的內容；保留該行會建置教學文件。先完成學生專案的 README 與 conf/README 所列資料，勿改寫範本內部。文件語言不決定學校、封面語言或學位。

## 新增及排列章節

建立 `context/pilot/pilot.tex`，放入以下完整章節。此示範須先取得自己的圖片，放在 `context/pilot/figure.png`，並依文獻參考頁加入所列既有真實文獻；示範文字不代表研究結果。所有路徑均由學生專案根目錄計算。再於 `context/context.tex` 的參考文獻輸入行之前加入 `\input{./context/pilot/pilot}`；調整 input 行順序即可排列章節。

`\StartChapter{標題}{標籤}`、`\StartSection{標題}{標籤}` 的第二組大括號可省略，不能改成方括號。`\StartSubSection` 與 `\StartSubSubSection` 也採相同形式。章節結尾用 `\EndChapter`，標籤須唯一；引用用 `\RefTo{標籤}` 或 `\RefPage{標籤}`，不要手打編號。

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

圖片與表格的細節見[圖表](figures-and-tables.md)，文獻準備見[引用與文獻](references-and-bibliography.md)。

## 文字與清單

一般段落、行內數學及清單可用標準 LaTeX；空白行分段。文字中的特殊符號須跳脫，否則可能出現 `Missing $ inserted` 或註解吃掉內容。

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

## 摘要、誌謝、符號與附錄

既有 `abstract/`、`acknowledgments/`、`nomenclature/` 由 `context/context.tex` 選擇。保留各檔現有的開始與結束指令，只替換內容；選擇所需語言。摘要與延伸摘要需求以當前系所及校方規定為準。以下展示英文摘要、誌謝與符號章的配對指令，勿重複插入已啟用的部分。

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

附錄放在參考文獻之後；`\StartAppendix` 無參數，會切換後續章節編號，`\EndAppendix` 結束頁面而不恢復一般章節模式。因此附錄應保持在正文最後。

<!-- student-snippet: appendix -->
```latex
\StartAppendix
\StartChapter{Supplement}{chap:pilot-appendix}
Supplied supplementary material.
\EndAppendix
```
