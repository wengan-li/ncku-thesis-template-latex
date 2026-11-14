<!-- language: zh-Hant-TW; summary-of: student-writing-and-agent-skills.en.md -->

[繁體中文摘要](student-writing-and-agent-skills.md) | [English technical record](student-writing-and-agent-skills.en.md)

# 學生寫作與可攜式代理技能

本專案讓學生與代理共用 `thesis/context/` 內的寫作知識。[寫作入口](../../thesis/context/README.md)依任務導向指南，代理則由單一技能載入英文用法。功能描述以現行來源為準，發行套件內容以 [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases) 為準。

- `thesis/context/usage/` 保存繁中及英文人用指南與可執行範例。代理的 `AGENTS.md`、`SKILL.md` 及技能附帶參考檔僅用英文，不放語言切換器或重複手冊。
- 學生專案及 `context/` 各有一份精簡路由；相鄰別名必須為 `CLAUDE.md -> AGENTS.md`。用戶端未自動辨識巢狀技能時，明確讀取指定技能檔。
- 代理先從指定內容檔案或目錄向上尋找執行環境；未指定時才從工作目錄向上找。在已確認的儲存庫根目錄，另僅檢查 `thesis/`。相符專案須同時有 `thesis.tex`、`conf/` 及 `template/configure.tex`，不能把孤立內容接到無關專案。
- 複製完整 `context/` 時須保留隱藏 `.agents/` 與相對符號連結，並先保存目的地既有內容。內容目錄不含範本執行環境；閱讀指南不需要教學範例、網路、CodeGraph 或儲存庫技能。
- 代理保留研究主張、標籤及文獻，只修改要求的學生資料；不能虛構輸入、引用、編譯成功或機構核可。寫作不授予安裝、發行、上傳或帳號操作權限；證明書使用學校系統正式檔案。
- 驗證直接編譯指南片段，檢查圖說、標籤、引用、文獻收斂與整份內容複製。反向案例涵蓋缺檔、不安全路徑、語言、別名、執行環境及錯誤引用；繁中人用指南則為有效正向案例。
- ZIP 檢查分別驗證符號連結模式、目標字串及解壓後內容。辨識失敗時先明確載入技能；缺少執行環境時取得完整範本，不自行產生替代環境。
- CodeGraph 僅輔助儲存庫 Python／YAML 查詢，不提供原生 LaTeX 語意圖，也不是學生需求。TeX 問題使用原始碼、API 契約、重點案例及非空 `.fls`；索引與用戶端整合是不同事項。

操作、檢查命令與限制詳見英文頁，學生建置排錯見[人用指南](../../thesis/context/usage/build-and-diagnostics.md)。
