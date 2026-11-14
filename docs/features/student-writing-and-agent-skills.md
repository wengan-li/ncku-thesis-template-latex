<!-- language: zh-Hant-TW; summary-of: student-writing-and-agent-skills.en.md -->

[繁體中文摘要](student-writing-and-agent-skills.md) | [English technical record](student-writing-and-agent-skills.en.md)

# 學生寫作與可攜式代理技能

寫作教學見[內容指南](../../thesis/context/README.md)及教學 PDF；需要 AI 協助時，請代理先讀取[寫作技能](../../thesis/.agents/skills/ncku-thesis-writing/SKILL.md)。可下載套件以 [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases) 為準。

- 完整教學保留在既有教學來源與 PDF。技能中的 `references/template-usage.md` 取自教學實際使用的程式碼，不另維護一份用法手冊。一般學生建置不需要產生器或教學目錄。
- 英文技能說明章節組織、圖表、引用、建置及排錯。代理路由及參考檔也只使用英文；學生專案與內容指南維持雙語。
- 搬移時先保存目的地資料，再複製完整專案，包含隱藏 `.agents/`、`.claude/` 及相對連結。兩個學生路由保留 `CLAUDE.md -> AGENTS.md`；Claude 技能別名指向專案根目錄的同一份技能。若用戶端沒有自動找到技能，請明確提供 SKILL.md 路徑。
- 從含有 `thesis.tex` 的目錄建置。相符專案須同時包含 `conf/` 及 `template/configure.tex`；只有 `context/` 內容並不足夠，代理不得借用無關專案。
- 建置須產生 PDF 與 SyncTeX，並確認引用及文獻已完成更新。參考片段、專案複製、缺檔及不安全連結均有檢查；詳細程序及復原方式由英文技術頁說明。檔案連結可用不代表已驗證所有用戶端的自動呼叫。
- 代理須保留研究主張及已提供的來源，不得虛構資料、引用或建置成功。寫作不授予安裝、改寫範本、發行或上傳權限；正式證明書及提交仍依學校規定。
- CodeGraph 只協助查找儲存庫內的 Python／YAML 維護工具，不分析 LaTeX 語意，也不是學生寫作的必要工具。封裝驗證與未提交來源的檢查分開處理，不能以本機建置宣稱已正式發行。
