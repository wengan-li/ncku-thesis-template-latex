<!-- doc-pair: writing-equations-and-theorems; lang: zh-Hant-TW; topics: equations,theorems -->

[繁體中文](equations-and-theorems.md) | [English](equations-and-theorems.en.md)

# 公式、定理與證明

## 公式及引用

在章節內使用 `\EquationBegin{標籤}` 與 `\EquationEnd`。標籤是可省略的大括號參數，不是方括號；省略時仍會編號。內部已有 aligned，使用 & 對齊、雙反斜線換行，勿再包一層數學環境。`\RefEquation` 只顯示編號，`\RefEquationB` 會加括號。行內公式可用一般 `$...$`。

<!-- student-snippet: equations-theorems -->
```latex
\EquationBegin{eq:pilot-identity}
  x &= x
\EquationEnd
See Equation \RefEquationB{eq:pilot-identity}.
\InsertTheorem[title={Identity},label={thm:pilot-identity}]{For every $x$, $x=x$.}
\InsertProof{Both sides denote the same object.}
See Theorem \RefTo{thm:pilot-identity}.
```

## 定理與證明

以上定理採 `\InsertTheorem[title={標題},label={標籤}]{內容}`，title 與 label 預設空白。`\InsertLemma`、`\InsertDefinition` 等公開包裝也接受相同選項；本頁只示範定理。`\InsertProof{內容}` 只有一個必填參數，結尾自動加入證明結束符號。編號與標題依既有設定，不要為新增一個定理重設全篇計數器。未知選項會報錯，先核對拼字；`??` 則檢查標籤並重新完成建置。證明內容須由研究者提供，示範恆等式不代表研究結論。
