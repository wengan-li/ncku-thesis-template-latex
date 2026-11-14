<!-- language: zh-Hant-TW; summary-of: validation-and-performance.en.md -->

[繁體中文摘要](validation-and-performance.md) | [English technical record](validation-and-performance.en.md)

# 驗證與效能

本專案以現行原始碼、測試案例與 `justfile` 定義驗證契約，涵蓋相容性、輸出、學生使用及套件。

- `just test` 建置正式教學文件並執行重點案例，`just ci` 包含完整測試及儲存庫檢查；CI 同樣執行 `just test`。本機通過不代表遠端執行或發行完成。
- 正式整合文件的契約為 261 頁 A4、PDF 與 SyncTeX，引用及文獻須收斂。公開指令、相容層、學校設定隔離、日期、定理、圖表、字型及診斷預算均有檢查。
- 測試來源依[測試索引](../../tests/000-test-suite.md)以唯一三位數字首平放在 `tests/`；一般驗證以重點案例為主，完整教學文件提供整合覆蓋。反向案例必須因預期原因失敗。
- Markdown 探索在進入子目錄前排除 `build/`、`.git/` 及符號連結目錄，並略過符號連結檔案；隱藏的來源文件仍須檢查。文件測試模擬排除目錄於掃描時被刪除，同時確認來源文件的錯誤仍會回報，避免平行封裝清理造成探索競爭。
- 學生 ZIP 的清單與內容須等於已提交的 `HEAD:thesis`，並驗證必要檔案與符號連結。未提交的學生來源不會成為封裝檢查的輸入，不能把兩種檢查混為一談。
- 影響版面時應比對文字、正規化座標、字型及固定解析度的頁面圖片，並人工檢視受影響頁面。不宣稱不同系統、TeX Live 或字型下的 PDF 逐位元相同。判斷未載入某資產前，須先確認 `.fls` 存在且非空。
- 解壓後可直接用 `latexmk` 建置；Overleaf 與編輯器同樣指定 XeLaTeX 及 `thesis.tex`。學生不需要儲存庫測試工具，PDF 存在也不代表引用已完成。
- 寫作時關閉 `\ExampleMode`，避免重建整份教學內容；`latexmk` 依依賴關係重跑，`just watch` 提供持續預覽。建置時間受文件、圖片、環境與負載影響，不提供通用加速或 Overleaf 時限保證；必要測試及發行保留乾淨建置。
- 寫作片段、英文代理指示、完整專案複製與根目錄辨識的檢查見[學生寫作與代理技能](student-writing-and-agent-skills.md)，公開資產驗證見[發行與分發](release-and-distribution.md)。
