<!-- language: zh-Hant-TW; summary-of: student-writing-and-agent-skills.en.md -->

[繁體中文摘要](student-writing-and-agent-skills.md) | [English technical record](student-writing-and-agent-skills.en.md)

# 學生寫作與可攜式代理技能

完整的人用教學由既有 `thesis/example/how-to/` 來源及教學 PDF 提供；學生專案與[內容入口](../../thesis/context/README.md)保持精簡雙語路由，不另維護重複語法手冊。可下載內容以 [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases) 為準。

- 代理的工作流程、執行環境辨識、編輯界線、驗證與復原集中在英文 `SKILL.md`；代理路由及所有附帶參考檔僅用英文。
- `references/template-usage.md` 是唯一產生的可攜式參考。標記區段取自教學實際使用的程式碼，產生器只選取英文或 LaTeX、移除註解並綁定示範標籤與資料路徑，不自動翻譯教學文字。
- 教學來源同時提供章節、前置頁、圖表、公式、定理、引用、真實 BibTeX 資料及建置命令。`just writing-reference` 更新參考檔；`--check` 遇到過期輸出會失敗，不自行覆寫。一般學生建置不需要產生器。
- 兩個學生路由保留 `CLAUDE.md -> AGENTS.md` 相對別名。複製完整 context/ 時包含隱藏 .agents/ 與產生的參考檔，並先保存目的地內容；缺少教學目錄也能閱讀及使用參考。
- 指定內容的祖先須能找到 thesis.tex、conf/ 及 template/configure.tex。在已確認的儲存庫根目錄另僅檢查 thesis/，孤立內容不能借用無關專案；內容目錄本身不含完整範本或編譯器。
- 測試直接編譯產生的參考片段，驗證 PDF、SyncTeX、文字、標籤、文獻收斂及整份內容複製；修改共用來源須反映在新參考中。既有圖表、定理與引用案例繼續保護選項及中繼資料行為。
- 反向案例保留缺檔、不安全路徑、語言、別名、執行環境及錯誤引用。封裝仍以已提交的 HEAD:thesis 為準，不能以未提交來源的建置宣稱正式封裝已通過。
- 代理不得虛構研究資料、引用或建置成功，也不取得安裝、發行、上傳或機構授權。CodeGraph 僅用於儲存庫 Python／YAML，TeX 語意仍以來源、API 契約及重點案例為準。

建置排錯與操作見[寫作技能](../../thesis/context/.agents/skills/ncku-thesis-writing/SKILL.md)，技術責任與驗證程序詳見英文頁。
