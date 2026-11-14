<!-- language: zh-Hant-TW; summary-of: validation-and-performance.en.md -->

[繁體中文摘要](validation-and-performance.md) | [English technical record](validation-and-performance.en.md)

# 驗證與效能

本專案的驗證涵蓋既有指令相容性、論文輸出、學校設定及學生套件。完整檢查方式見英文技術頁；學生依套件內指南建置即可。

- `just test` 建置教學文件並執行重點測試；`just ci` 加上儲存庫檢查。CI 也須通過 `just test`，但本機通過不代表遠端驗證或發行已完成。
- 正式教學文件應為 261 頁 A4，具備 PDF 與 SyncTeX，且沒有未解決的引用、文獻或重跑警告。既有指令、日期、學校資料隔離、圖表、定理及字型亦受檢查。
- 學生套件解壓後可直接用 `latexmk` 建置；Overleaf 與編輯器同樣使用 XeLaTeX 及主文件 `thesis.tex`。學生不需要儲存庫測試工具，產生 PDF 也不等於內容已檢查完成。
- 封裝檢查比較學生 ZIP 與已提交 `HEAD:thesis` 的檔案及內容，並檢查必要檔案與相對連結。未提交來源的本機驗證不能代替這項檢查。
- 影響版面時須比對頁數、文字、座標、字型及頁面圖片，並人工檢視受影響頁面。不同系統、TeX Live 或字型環境下，不保證 PDF 逐位元相同；判斷未載入某資產前，須先確認 `.fls` 載入記錄存在且非空。
- 撰寫自己的論文時，關閉 `\ExampleMode` 可避免重建教學內容；`latexmk` 依修改內容決定重跑步驟，`just watch` 提供持續預覽。耗時仍受文件、圖片、工具與負載影響，不保證通用加速或 Overleaf 完成時限；必要測試及發行仍須乾淨建置。

寫作與專案複製見[學生寫作與代理技能](student-writing-and-agent-skills.md)，封裝及公開驗證見[發行與分發](release-and-distribution.md)。測試清單、錯誤案例與細部程序保留在英文技術頁。
