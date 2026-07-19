<!-- language: zh-Hant-TW; summary-of: v2-modernization.en.md -->

[繁體中文摘要](v2-modernization.md) | [English technical record](v2-modernization.en.md)

# V2現代化

狀態：正式使用

- 基礎架構版本：[`v2.0.0.260717130231`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.0.260717130231)

## 摘要

- V2保持XeLaTeX、學生project shape、direct `latexmk` path及完整經audit的1.x public API。
- 597個runtime-visible LaTeX/xparse declarations、65個literal-def declarations及18個V1 student inputs由machine gates保護。
- 共用renderer、NCKU policy及其他學校ports分別由`base`、`ncku`及`custom` profiles負責；文件／封面語言不會選擇profile。
- 通用institution API設定校名、學院及系所metadata；NCKU profile另保存9個學院及110個涵蓋系、研究所、學位學程與中心的presets，每個shortcut亦會選擇一個NCKU學院。
- NCKU presets只由`ncku` profile載入；未修改的1.x NCKU專案透過預設profile保持相容，`custom`只載入generic institution API。本專案目前沒有NTU profile，NTU walkthrough只示範API wiring。
- 已驗證的theorem、caption、numbering、date、committee及catalogue defects在不改public signatures下修正，詳情由migration table擁有。
- Repository-owned generic command parsing使用19個native `l3keys` families，direct `pgfkeys` parser references及explicit package load為零。
- PGF/TikZ並非完全移除；`mdframed`的TikZ framing仍可transitively載入runtime dependency。
- V2完成狀態不會自動啟用P3 architecture experiments；新工作需要新的owner-approved Intent。

完整英文technical record：[v2-modernization.en.md](v2-modernization.en.md)
