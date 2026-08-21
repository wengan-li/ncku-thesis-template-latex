<!-- language: zh-Hant-TW; summary-of: v2-modernization.en.md -->

[繁體中文摘要](v2-modernization.md) | [English technical record](v2-modernization.en.md)

# V2現代化

狀態：正式使用

- 基礎架構版本：[`v2.0.0.260717130231`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.0.260717130231)

## 摘要

V2重新整理了範本的內部架構，但同學看到的東西不變：同樣的成大論文版面、同樣的專案目錄、同樣的XeLaTeX加`latexmk`建置方式，所有1.x指令也繼續可用。改造的核心是把「每份論文都需要的通用機制」與「成大的規定」分開——這讓其他學校的同學能建立自己的profile，也讓已證實的錯誤可以修正而不影響既有專案。

- 通用機制放在`template/command/`與`template/style/base/`；成大的版面、文字、日期政策、浮水印資產，以及9個學院與110個系所preset，只屬於`ncku` profile。`custom`是給其他學校起步的中性骨架，不會載入任何成大資料。
- 載入順序是行為契約：先載入通用指令，再載入唯一選定的profile，然後才讀學生的`conf/conf.tex`，最後填入PDF metadata。未修改的1.x成大專案因此照樣能呼叫`\SetDeptCSIE`等preset指令。
- 相容性由機器把關：597個runtime可見的LaTeX/xparse宣告、65個literal `\def`宣告與18個v1.8.2學生檔案全部鎖定；23個已停用指令保留原本的錯誤訊息與`\stop`行為。整個2.x期間，公開指令的名稱與參數形狀都不會改變。
- 已證實的錯誤（theorem label、編號重複設定、DPS英文拼字、封面日期組合、委員人數範圍、自訂字型載入等）在不改公開簽名的前提下修正；完整的前後對照與使用者動作記錄在[升級指南](../v1-to-v2-migration.md)。
- 範本自有的指令解析全部改用19個`l3keys` family；`pgfkeys`不再用於指令解析，只會經由`mdframed`的TikZ框線間接載入。`xparse`仍明確保留，因為受保護的公開簽名使用kernel未提供的`G{...}`參數型態。
- V2到此為止：class重寫、引擎更換、tagged PDF等項目都未啟動，需要新的owner核准Intent才會展開。

完整英文technical record：[v2-modernization.en.md](v2-modernization.en.md)
