<!-- language: zh-Hant-TW; summary-of: validation-and-performance.en.md -->

[繁體中文摘要](validation-and-performance.md) | [English technical record](validation-and-performance.en.md)

# 驗證與效能

狀態：正式證據已整合至最新production release。

Production evidence已整合至[`v2.0.2.260719120024`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.2.260719120024)。

## 摘要

- Canonical production contract是XeLaTeX、271頁A4、40,823個normalized bbox words及271/271頁120-DPI raster identity。
- `just test`／`just ci`保護public API、V1 byte-pinned project、profile、theorem、float、numbering、metadata及diagnostic contracts。
- `tests/`採用flat三位數分組；[`tests/000-test-suite.md`](../../tests/000-test-suite.md)定義ranges，layout checker會拒絕未編號、nested path或重複編號。
- Student ZIP必須等於committed `HEAD:thesis`完整regular-file tree，並在解壓project root以direct `latexmk -xelatex`成功建置。
- `v2.0.2.260719120024`兩個public assets已重新下載、核對SHA-256並與workflow artifact byte-identical；fresh student ZIP以package內canonical command直接建置271頁A4 PDF及SyncTeX。
- Performance數字屬dated、same-host evidence；isolated/student改善不會被誇大為full-corpus speedup。
- Rejected renderer/cache/preview experiments及P3 candidates保持inactive，除非新證據及owner Intent重開。
- Current tests及source永遠優先於historical benchmark或一次性run ID。

完整英文technical record：[validation-and-performance.en.md](validation-and-performance.en.md)
