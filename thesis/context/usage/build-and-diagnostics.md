<!-- doc-pair: writing-build-and-diagnostics; lang: zh-Hant-TW; topics: build,diagnostics -->

[繁體中文](build-and-diagnostics.md) | [English](build-and-diagnostics.en.md)

# 建置與診斷

## 從學生專案根目錄建置

終端機先切換至含 `thesis.tex`、`conf/` 與 `template/configure.tex` 的學生專案根目錄，再執行：

<!-- student-snippet: direct-build -->
```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

Overleaf 選 `thesis.tex` 為主文件、XeLaTeX 為編譯器，必要時從頭重新編譯。編輯器如 TeXstudio 或 Texmaker 同樣指定根文件，使用 XeLaTeX 與 BibTeX 的 latexmk 建置鏈。工具不存在時先依完整學生專案 README 準備所需環境；代理不得自行安裝或更改全域設定。只有 context/ 時須先取得相符的完整論文範本。

## 讀取錯誤與確認結果

先找記錄中的第一個錯誤。`File ... not found` 檢查根目錄、路徑與大小寫；`Undefined control sequence` 檢查指令拼字與相符範本；`Missing $ inserted` 檢查未跳脫的底線與數學模式。引用錯誤見[文獻頁](references-and-bibliography.md)。若仍顯示教學內容，回查 ExampleMode。

確認實際產生 PDF 與 SyncTeX，最終記錄不得有 unresolved/undefined citations、undefined references 或要求重跑的警告。核對新增文字、圖說、圖片、引用編號及文獻列表，並開啟受影響頁面檢查裁切與分頁。報告實際命令及結果，不能將編輯成功稱為編譯成功。提交前仍須按當前官方規定檢查證明書及版面。

從儲存庫根目錄使用代理時，應先確認該根目錄，再檢查 `thesis/` 內的三項必要檔案與目錄。指定內容路徑時，以該路徑的祖先為準；若找不到相符執行環境，應回報缺少完整論文範本，不能借用無關專案。
