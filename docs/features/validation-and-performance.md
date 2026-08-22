<!-- language: zh-Hant-TW; summary-of: validation-and-performance.en.md -->

[繁體中文摘要](validation-and-performance.md) | [English technical record](validation-and-performance.en.md)

# 驗證與效能

狀態：正式證據已整合

## 摘要

本記錄說明範本如何測試、正式輸出必須長什麼樣子，以及哪些效能決定有實際量測依據。歷史數字與現行測試不一致時，以現行測試與source為準。

- 正式的整合輸出是XeLaTeX建置的271頁A4教學文件。輸出敏感的修改除了比對頁數與文字，還要比對正規化的文字座標、字型表、固定DPI點陣圖，並人工檢視受影響的頁面。
- `just test`與`just ci`保護公開API、v1鎖定專案、profile隔離、theorem、float、編號、metadata與診斷預算等契約；測試檔案以三位數字首平放在`tests/`，由layout checker拒絕未編號或巢狀的路徑。
- 學生ZIP必須與committed `HEAD:thesis`的檔案清單完全一致，並能在解壓後的目錄直接以`latexmk`建置完成。
- v2.0.2、v2.0.5與v2.0.6發行的公開資產都已重新下載並核對SHA-256，與workflow artifact完全相同；下載的學生ZIP直接建置出271頁A4 PDF與SyncTeX，v2.0.5起兩個套件並附有授權條款檔案。
- 效能數字屬於單一主機的當時量測：學生模式的小幅改善（清冷建置約-2.5%）是實測結果；整份271頁文件的建置時間受背景負載影響太大，不作全面加速的宣稱。寫作期間真正有效的加速是StudentMode與`latexmk -pvc`。
- 量測後被否決的實驗（非TikZ框線、章節預覽模式、CI快取`build/`、TeX container image快取、Arm runner）與延後項目（class重寫、`l3build`、引擎更換、tagged PDF）維持不啟用，重啟需要新的owner核准Intent。

完整英文technical record：[validation-and-performance.en.md](validation-and-performance.en.md)
