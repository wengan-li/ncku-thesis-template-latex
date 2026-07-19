<!-- language: zh-Hant-TW; canonical-history: CHANGELOG.en.md -->

[繁體中文 V2](CHANGELOG.md) | [English and complete history](CHANGELOG.en.md)

# V2變更記錄

本文件記錄V2正式版本及使用者可見修正。完整歷史記錄保留在[`CHANGELOG.en.md`](CHANGELOG.en.md)，最新學生套件及examples可從[GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases)下載。現行學校及系所規定永遠優先於本範本說明。

## 2.x

### [v2.0.2.260719120024](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.2.260719120024) — 2026-07-19

- 將學生及public documentation整理成8組完整繁中／英文guides與3組繁中摘要／英文technical records；繁中使用default `.md`，英文使用`.en.md`，不再保留`.zh-TW.md` paths。
- 保留generic institution metadata APIs，同時由`ncku` profile獨立擁有9個學院及110個系所presets；`custom` profile不再載入NCKU catalogue。
- 記錄並machine-check commands／selected profile／student configuration／metadata initialization載入順序，讓其他學校的同學由neutral custom skeleton建立自己的profile。
- 保持597個LaTeX／xparse及65個literal def-style V1 declarations、byte-pinned V1 migration inputs、271頁A4 canonical output與直接學生ZIP build contract。

### [v2.0.1.260719010734](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734) — 2026-07-19

- 將repository-owned generic `pgfkeys` command parsers全部替換為19個native `l3keys` families，同時保留完整經audit的1.x public API。
- 保留parser defaults、macro expansion、repeated-call resets、omission behavior、unknown-key failures、theorem registries、numbering及float routes。
- Canonical NCKU教學文件維持271頁A4，text、normalized word geometry、font table及271/271 fixed-DPI page rasters完全一致。
- 移除多餘的explicit `pgfkeys` load；PGF/TikZ仍可由既有visual framing transitively載入，但不再用於command parsing。

### [v2.0.0.260717130231](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.0.260717130231) — 2026-07-17

V2在保留XeLaTeX、既有NCKU輸出、學生project shape及完整經audit的1.x public API下，更新template architecture。詳細contract及evidence見[1.x → 2.x升級指南](docs/v1-to-v2-migration.md)及[V2 modernization record](docs/features/v2-modernization.md)。

- 透過compatibility adapter保留既有1.x projects，不要求helper renames。
- 將generic rendering、NCKU policy及custom institution ports分成base、`ncku`及`custom` style profiles。
- 修正theorem labels/counter chains、caption `\nameref` metadata及repeatable numbering setup。
- 移除legacy `fp` runtime dependency，同時保留public command signatures。
- Canonical NCKU教學文件維持271頁A4，並驗證text、geometry、raster及font identity。
- 從immutable release tag發佈一個editable student ZIP及一個six-PDF examples ZIP。
