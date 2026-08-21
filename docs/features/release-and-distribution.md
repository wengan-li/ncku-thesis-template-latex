<!-- language: zh-Hant-TW; summary-of: release-and-distribution.en.md -->

[繁體中文摘要](release-and-distribution.md) | [English technical record](release-and-distribution.en.md)

# 發行與分發

狀態：GitHub正式發行已驗證；Overleaf Gallery V2更新已獲批准，並於`2026-07-21`完成公開頁面、source與PDF的read-back。

- [公開Overleaf範本](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)

## 摘要

本記錄說明一次發行如何建置、兩個公開套件各包含什麼、發行後如何驗證，以及Overleaf與GitHub兩個通路的關係。兩者狀態互相獨立：GitHub的變更不會更新Overleaf，Overleaf的送審也不代表任何認可。

- 每次正式發行只上架兩個公開資產：學生ZIP與含六個PDF的examples ZIP；兩個套件都附授權條款檔案，鬆散的PDF只是建置中間產物，不另行發佈。
- 學生ZIP等於tagged `thesis/`檔案樹，解壓即可直接建置，不含repository工具、測試或多餘的`thesis/`外層。
- 發行流程分兩段：build階段跑完整測試並產生已驗證的ZIP；promote階段只在對應的Git tag事件把同一份workflow artifact附加到GitHub Release。手動dispatch只build、不發行；已發佈的tag永不移動。
- 發行後仍要重新下載公開資產，核對SHA-256並與workflow artifact逐位元比對；v2.0.2的read-back證據記錄在[驗證與效能](validation-and-performance.md)。
- Overleaf Gallery是獲批准的公開編輯入口，GitHub Releases是版本化下載的正式來源；Gallery套件會清除Draft標記與學校浮水印資產，且`just test`會冷建置產生的Gallery套件防止契約漂移。
- 封面`(初稿)`標記、斜向文字浮水印與學校logo浮水印是三個互相獨立的opt-in，正式輸出預設全部關閉；學位考試證明書應使用學校系統產出的正式檔案，範本產生的版本只是示範與regression輸出。
- 舊的sample repository已於2026-07-12由owner刪除退役，generated examples改由同一source revision建置的release assets提供。

完整英文technical record：[release-and-distribution.en.md](release-and-distribution.en.md)
