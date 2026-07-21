<!-- language: zh-Hant-TW; summary-of: release-and-distribution.en.md -->

[繁體中文摘要](release-and-distribution.md) | [English technical record](release-and-distribution.en.md)

# 發行與分發

狀態：GitHub production release已驗證；Overleaf Gallery V2更新已獲批准，並於`2026-07-21`完成public page、source及PDF read-back。

- [公開Overleaf範本](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)

## 摘要

- 每次production release只promote一個student ZIP及一個six-PDF examples ZIP。
- Student ZIP等於tagged `thesis/` tree、直接解壓可用，且不包含repository tooling或多餘`thesis/`wrapper。
- GitHub Release build／promotion及public read-back由immutable source revision及checksums連結；v2.0.2 public assets已與workflow artifact byte-identical，舊tag不會重建或移動。
- Overleaf Gallery V2更新已公開；public source顯示root `thesis.tex`直接宣告`\documentclass`並載入`template/configure`，公開PDF為11頁A4，封面及前置頁未見clipping、Draft marker或institution watermark。
- `Open as Template`公開路由保留XeLaTeX、root `thesis.tex`及TeX Live 2025.1設定；隔離browser於建立project前要求登入，因此今次read-back沒有聲稱完成authenticated fresh-project compile。
- 舊sample repository已退役，generated examples由release assets取代，不再是canonical source。
- Draft cover marker、diagonal text watermark及institution logo watermark是三個獨立opt-ins，正式輸出全部default-off。
- Template-generated defense certificates是unofficial demonstrations；正式提交使用學校系統文件並遵守asset/licensing boundary。

完整英文technical record：[release-and-distribution.en.md](release-and-distribution.en.md)
