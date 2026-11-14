<!-- language: zh-Hant-TW; summary-of: release-and-distribution.en.md -->

[繁體中文摘要](release-and-distribution.md) | [English technical record](release-and-distribution.en.md)

# 發行與分發

[GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases)提供版本化下載；[Overleaf Gallery](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)是獨立的編輯入口。原始碼、本機套件、上傳、送審與公開核准不能互相推定。

- 每次發行僅有學生 ZIP 與包含六份 PDF 的範例 ZIP 兩個自訂資產；完整原始碼封存另由 GitHub 提供，零散 PDF 不另行發佈。可下載版本以 Releases 為準，變更見[變更記錄](../../CHANGELOG.md)。
- 學生 ZIP 等於發行來源的 `thesis/` 檔案樹，解壓後直接放置 `thesis.tex`、`conf/`、`context/`、`example/` 與 `template/`。儲存庫工具不隨包提供；學生專用 `AGENTS.md`、內容目錄路由、相鄰 `CLAUDE.md -> AGENTS.md` 及單一寫作技能是明確例外。
- 範例 ZIP 固定包含 README、授權條款與封面、中英文論文、完整教學文件、兩種產生的證明書 PDF。產生的證明書僅供示範，不代表校方正式文件；學生應使用學校學位考試系統檔案及[當前官方指引](https://thesis.lib.ncku.edu.tw/help/aboutedit/)。
- 發行流程先從乾淨、已提交的來源建置並測試，再由對應 Git tag 事件推廣同一份產物。手動執行只建置；兩份變更記錄須包含該版條目，已發佈標籤不得移動。
- 發行後重新下載公開資產，核對完整性、資產清單、SHA-256 與實際內容，並直接建置學生專案。工作流程通過不等於公開內容已驗證；本機建置也不代表已上傳。
- 兩種 Overleaf 套件均省略教學內容及第二主文件，保留寫作知識與相對別名。Gallery 另外套用發佈設定並移除不需的學校資產；兩者皆須本機冷建置，並設定 XeLaTeX 與 `thesis.tex`。本機結果不能保證帳號設定、遠端時限或用戶端別名行為。
- 儲存庫與發行套件使用 CC BY-NC-SA 4.0，Gallery 版本使用 CC BY 4.0。專案授權不代表所有第三方字型或學校資產可重新授權，本專案也不主張學生原創論文內容及 PDF 的權利。更新沿用原 Overleaf 專案，核對公開頁面及 PDF 後才能描述發佈狀態。
- 封面初稿字樣、斜向文字及 logo 浮水印是三個獨立選項，正常輸出預設皆關閉。ETDS 輸出不內加浮水印、DOI、加密或安全處理，依當前校方指示辦理。

套件驗證與遠端限制詳見英文頁，寫作知識契約見[學生寫作與代理技能](student-writing-and-agent-skills.md)。
