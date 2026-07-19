<!-- language: zh-Hant-TW; summary-of: release-and-distribution.md -->

[繁體中文摘要](release-and-distribution.zh-TW.md) | [English technical record](release-and-distribution.md)

# 發行與分發

狀態：GitHub production release已驗證；Overleaf Gallery V2更新仍記錄為owner-confirmed submitted，等待public approval及read-back。

- 最新production release：[`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734)
- [公開Overleaf範本](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)

## 摘要

- 最新production release是`v2.0.1.260719010734`，每個release只promote一個student ZIP及一個six-PDF examples ZIP。
- Student ZIP等於tagged `thesis/` tree、直接解壓可用，且不包含repository tooling或多餘`thesis/`wrapper。
- GitHub Release build／promotion及public read-back由immutable source revision及checksums連結；舊tag不會重建或移動。
- 既有Overleaf Gallery頁面仍公開；V2狀態只可寫成owner-confirmed submitted及pending approval/read-back，不能推論已批准。
- 舊sample repository已退役，generated examples由release assets取代，不再是canonical source。
- Draft cover marker、diagonal text watermark及institution logo watermark是三個獨立opt-ins，正式輸出全部default-off。
- Template-generated defense certificates是unofficial demonstrations；正式提交使用學校系統文件並遵守asset/licensing boundary。

完整英文technical record：[release-and-distribution.md](release-and-distribution.md)
