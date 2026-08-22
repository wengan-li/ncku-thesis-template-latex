<!-- doc-pair: student-readme; lang: zh-Hant-TW; topics: start-writing,choose-independent-settings,configure-thesis-information,migrate-from-1-x,build-the-final-document,continuous-preview-and-editors,use-overleaf,draft-watermark-and-certificate,common-errors,before-submission,other-community-alternatives -->

[繁體中文](README.md) | [English](README.en.md)

# 成大論文範本學生專案

此目錄是可直接使用的學生專案。版本化的GitHub Release學生套件會將這些檔案放在單一`ncku-thesis-template-latex/`目錄內；完整儲存庫的測試、發行腳本及維護工具不會包含在學生套件中。本套件的授權條款見[`LICENSE`](LICENSE)。

## 開始撰寫

1. 開啟`conf/conf.tex`。撰寫自己的論文時，請將`\ExampleMode`註解；啟用時會編譯完整教學範例。
2. 按照[`conf/README.md`](conf/README.md)填寫題目、姓名、學位、日期、系所、指導教授及其他論文資料。
3. 在`context/context.tex`選擇章節，並於`context/`內撰寫內容。
4. 始終以`thesis.tex`作為主文件。

`conf/conf.tex`出廠時是教學範例的設定，以下各行必須改成自己的資料（行號固定，可直接跳到該行）：

| 項目 | `conf/conf.tex`行 | 要做的事 | 不改會怎樣 |
| --- | --- | --- | --- |
| 內容模式 | 13 | 在`\ExampleMode`行首加`%` | 建置出271頁教學文件，不是自己的論文 |
| 封面語言 | 44 | 保留`\DisplayCoverInEng`或改為`\DisplayCoverInChi` | 封面語言不符系所要求 |
| 題目 | 71–73 | `\SetTitle{中文題目}{English Title}`；圖書館要求中英文題目都要有 | 封面印出本範本的名稱 |
| 學位 | 99 | 碩士改為`\MasterDegree`；博士保留`\PhdDegree` | 封面與證明書顯示錯誤學位 |
| 姓名 | 111 | `\SetMyName{中文姓名}{English Name}` | 封面印出「你的名字」 |
| 口試日期 | 125 | `\SetOralDate{年}{月}{日}`，使用西元 | 封面日期停在2023年12月 |
| 封面日期 | 138 | 成大同學不用改；`ncku`設定由口試日期自動推算 | — |
| 系所 | 148 | 改成自己系所的指令；在[`template/style/ncku/README.md`](template/style/ncku/README.md)用中文系名搜尋 | 封面顯示出廠設定的資訊工程系所 |
| 指導教授 | 166–168 | 填寫`\SetAdvisorNameA`；只有一位指導教授時**刪除**B與C兩行 | 封面多出「B 博士」「C 博士」 |
| 證明書 | 204–206 | 把學校系統產出的證明書PDF放入`context/oral/`，取消註解並填入檔名 | 證明書頁不會出現，也沒有錯誤提示 |
| 關鍵字 | 224、246–248 | 改成自己的關鍵字 | PDF屬性與摘要顯示範本的關鍵字 |

撰寫中文論文時，另外在`context/context.tex`取消中文摘要、英文延伸摘要及中文誌謝的`\input`註解；出廠設定只啟用英文版。

## 選擇設定

文件語言、學校樣式設定檔、封面語言、學位及內容模式互相獨立。國際學生可以使用成大`ncku` profile；其他學校的同學亦可建立自己學校的profile。不要因讀者語言而選擇學校profile。

| 決定 | 選項 |
| --- | --- |
| 學校 | 成大同學使用預設`ncku`；其他學校的同學可使用custom profile |
| 封面語言 | `\DisplayCoverInChi`或`\DisplayCoverInEng` |
| 學位 | `\MasterDegree`或`\PhdDegree` |
| 內容 | 自己的`context/context.tex`或`\ExampleMode`教學範例 |

## 設定論文資料

`conf/conf.tex`是從v1.8.2保留的相容設定檔。為確保既有1.x專案可安全升級，該檔案在2.x保持byte-identical，因此原有註解主要為中文。請使用套件內的繁中[`conf/README.md`](conf/README.md)逐項查閱設定；不要為了翻譯而更改macro名稱或新增`conf/style.tex`。

## 由1.x升級

V2透過相容層保留完整、經machine audit的1.x helper surface。升級進行中的論文前，先commit或封存完整1.x專案並保存最新PDF。保留`conf/conf.tex`、`context/`、圖片、書目資料及本地證明書檔案；以V2替換template-owned檔案，並有意識地merge對`thesis.tex`的本地修改。完成後，使用下方direct build command，逐項比較封面、日期、目錄、引用、參考文獻、正文及最後頁。

完整指南：[`docs/v1-to-v2-migration.md`](https://github.com/wengan-li/ncku-thesis-template-latex/blob/main/docs/v1-to-v2-migration.md)

## 建置正式文件

安裝包含XeLaTeX、BibTeX及`latexmk`的TeX發行版。最低要求為LaTeX2e format 2020-10-01；建議使用TeX Live 2021或更新版本，發行CI目前使用TeX Live 2026。在包含`thesis.tex`的專案根目錄執行以下唯一正式建置指令。

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

清除產生的檔案：

```bash
latexmk -C thesis.tex
```

電子版只需要`thesis.pdf`，它已包含封面內頁。印刷版（精裝或平裝）另外需要交給影印店的封面檔，由`cover.tex`產生：

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode cover.tex
```

## 持續預覽與編輯器

撰寫期間可保持下方指令運行。每次儲存追蹤中的TeX、書目、圖片或included file時，`latexmk`只執行所需的compiler passes。`-view=none`避免開啟第二個PDF viewer；請讓Texmaker、TeXstudio或其他viewer重新載入現有`thesis.pdf`。按`Ctrl-C`停止。

```bash
latexmk -xelatex -pvc -view=none -synctex=1 -interaction=nonstopmode thesis.tex
```

```text
latexmk -xelatex -synctex=1 -interaction=nonstopmode %.tex
```

Set `thesis.tex` as the root/master document / 將`thesis.tex`設為主文件。

## 在Overleaf使用

不想安裝TeX的同學可直接使用[Overleaf上的公開範本](https://www.overleaf.com/latex/templates/national-cheng-kung-university-thesis-and-dissertation-template-xelatex/kzgwjvvptktn)：

1. 開啟範本頁面並按「Open as Template」，複製到自己的帳號。
2. 在Menu確認Compiler為XeLaTeX、Main document為`thesis.tex`。
3. 按Recompile；需要完整重建時選「Recompile from scratch」。

Overleaf範本已關閉`\ExampleMode`與初稿標記，直接填寫`conf/conf.tex`即可。免費方案有編譯時間限制，不要在Overleaf開啟`\ExampleMode`建置271頁教學文件。Overleaf範本與GitHub Releases是兩個獨立更新的來源，Overleaf的版本可能較舊；需要最新修正時請下載GitHub Releases的學生套件在本機建置。

## 初稿、浮水印與證明書

正式輸出預設不顯示封面`(初稿)`／`(Draft)`、斜向`DRAFT`文字或學校logo浮水印。只有在撰寫或審閱期間確實需要時，才於`conf/conf.tex`啟用`\DisplayDraft`。斜向文字浮水印及學校logo浮水印是另外兩個明確opt-in功能；不要因API存在就加入正式提交PDF。學校系統可能會對核准後的電子全文加入自己的浮水印。

正式提交時，應按學校規定使用學位考試系統產出的證明書。本範本產生的證明書只供legacy/example及regression用途，並非官方文件。

## 常見錯誤

| 看到的情況 | 原因 | 解法 |
| --- | --- | --- |
| 建置出271頁的教學文件 | `conf/conf.tex`第13行的`\ExampleMode`仍然啟用 | 在該行行首加`%`後重新建置 |
| `! LaTeX Error: File 'xxx.sty' not found.` | TeX發行版缺少套件 | MiKTeX：在MiKTeX Console安裝或開啟自動安裝；TeX Live／MacTeX：`tlmgr install <套件名>`，或安裝完整scheme |
| `! Undefined control sequence.`，下一行顯示`\SetDept...` | 系所指令打錯或不存在 | 在[`template/style/ncku/README.md`](template/style/ncku/README.md)查正確指令 |
| `! fontspec error: "font-not-found"` | `template/fonts/`不完整，或不是在包含`thesis.tex`的目錄建置 | 重新解壓套件，並在專案根目錄執行建置指令 |
| 引用顯示`[?]`，log出現`Citation ... undefined` | `.bib`內的key與`\cite{}`不符，或新增引用後尚未收斂 | 核對key後再執行一次正式建置指令；仍有警告時先`latexmk -C thesis.tex`再建置 |
| 改了`BibStyle`後建置失敗 | 舊的`.aux`／`.bbl`與新格式不相容 | `latexmk -C thesis.tex`後重新建置 |
| 證明書頁沒有出現 | `\SetOralImageChi`／`\SetOralImageEng`仍是註解，或檔名與`context/oral/`內的檔案不符 | 取消註解並填入正確檔名 |
| 中文變成亂碼或方格 | 檔案不是以UTF-8儲存 | 用支援UTF-8的編輯器重新儲存（Windows記事本的舊版本預設ANSI） |
| Overleaf顯示compile timeout | 在Overleaf建置教學範例，或需要完整重建 | 保持`\ExampleMode`關閉；選「Recompile from scratch」 |

## 提交前檢查

1. 停止任何continuous-preview process，重新執行正式建置指令。
2. 確認log沒有未解決的references、citations或rerun warnings。
3. 確認PDF沒有非預期的初稿標記、文字浮水印或logo浮水印。
4. 封面：中英文題目都有、姓名與學位正確、封面日期與口試日期一致、只列出實際的指導教授（未用的B、C已刪除）。
5. 證明書頁已出現，而且是學校系統產出的版本。
6. 摘要：本地生與僑生有中文及英文摘要，中文論文另有英文延伸摘要；外籍生依學校規定可免填中文摘要。
7. 完整檢查頁碼、目錄、圖表清單、參考文獻、字型及最後頁。
8. 核對當年度成大、圖書館及所屬系所的最新要求；現行官方規定永遠優先。
9. 使用學校系統要求的正式證明書與提交流程。

## 其他社群方案

如本範本不符合需要，可評估下列不定期更新的社群專案。它們並非由本專案維護；使用前請自行核對版本、授權及學校規定。

- [`Haouo/NCKU-Thesis-Typst`](https://github.com/Haouo/NCKU-Thesis-Typst) — Typst
- [`lycsjm/nckuthesis`](https://github.com/lycsjm/nckuthesis) — LaTeX
- [`windwalker661/Thesis-NCKU`](https://github.com/windwalker661/Thesis-NCKU) — LaTeX
- [`nckuasrlab/ASRLab_Thesis_Template`](https://github.com/nckuasrlab/ASRLab_Thesis_Template) — LaTeX
