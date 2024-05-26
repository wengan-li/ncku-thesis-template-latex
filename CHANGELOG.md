#### v1.7.0 [May 26, 2024]:

由於多年以前意外更新了`conf.tex`，改變了章節標題的設定很多年。故新修正回到原本的設計，由於這算是大變動，推薦同學們更新到這一版本或之後。

- **更新**:

  1.更新 tocstyle 到最新版本 \([感謝 tenyang1999 的 Issue \#61](https://github.com/wengan-li/ncku-thesis-template-latex/issues/61)\).

  2. 由於以前意外更新了`conf.tex`，改變了章節標題的設定很多年，故新修正回到原本的設計.

#### v1.6.0 [Jan 29, 2023]:

- **更新**:
  1. 移除國立成功大學版本的模版內頁不需要浮水印 \([感謝 Josh-WANGJS 的 Issue \#59](https://github.com/wengan-li/ncku-thesis-template-latex/issues/59)\).
  2. 更新國立成功大學博碩士學位論文格式規範 (Guidelines on Writing Dissertations for PhD and Master’s Students) 的版本到 110.01.06 (109 學年度版本), (來源: [成功大學法規彙編系統](https://www.cc.ncku.edu.tw/rule/content.php?sn=684) 和 [教務處課務組](https://cid-acad.ncku.edu.tw/p/412-1042-1378.php?Lang=zh-tw)).
  3. 在`README.md`新增`學位論文上傳和列印說明`, 提供同學快速知道當年的上傳和列印的基本流程.

#### v1.5.13 [Jul 16, 2022]:

- **修正錯誤**:
  修正封面的中文日期沒有置中 \([感謝 kevinmaura 和 maglili 的 Issue \#57](https://github.com/wengan-li/ncku-thesis-template-latex/issues/57)\)

#### v1.5.12 [Jun 14, 2021]:

- **修正錯誤**:
  修正 bug 在使用`\InsertFigures`並使用 perrow ＝ 3 配 3 張圖出現 error \([感謝 Ting199708 的 Issue \#52](https://github.com/wengan-li/ncku-thesis-template-latex/issues/52)\)

#### v1.5.11 [Jun 14, 2021]:

- **修正錯誤**:
  Missing tocstyle.sty \([Issue \#53](https://github.com/wengan-li/ncku-thesis-template-latex/issues/53)\)

- **提供的 APIs**:

  [感謝 kuangyoli 在 Issue \#51 中提議](https://github.com/wengan-li/ncku-thesis-template-latex/issues/51), 故新增以下 APIs:

  - `\SetDeptIDS`

#### v1.5.10 [Mar 25, 2020]:

- **修正錯誤**:
  部份系所英文名稱在產生封面時會出現 error \([感謝 medicalwei 的 Issue \#47](https://github.com/wengan-li/ncku-thesis-template-latex/issues/47)\)

#### v1.5.9 [Nov 27, 2019]:

- **更新**:
  增加使用 IEEEtran style \([感謝 yusie1978 的 Issue \#37](https://github.com/wengan-li/ncku-thesis-template-latex/issues/37)\)

#### v1.5.8 [Nov 27, 2019]:

- **修正錯誤**:
  封面日期的產出問題 \([感謝 MOHOAzure 的 Issue \#44](https://github.com/wengan-li/ncku-thesis-template-latex/issues/44)\)

#### v1.5.7 [Jun 23, 2019]:

- **更新**:
  根據[論文上傳要求](http://etds.lib.ncku.edu.tw/files/2012050003.pdf), 在 2018 年下學期時，開始需要插入 DOI 碼，故在`conf.tex`中加入`\ShowDOI{}`. \([感謝 ChampDBG 提供 Pull request \#35](https://github.com/wengan-li/ncku-thesis-template-latex/pull/35)\)

- **修正錯誤**:
  修正編譯\*.bib 時會出現的 bug. \([感謝 ygLinc9012 提供 Pull request \#38](https://github.com/wengan-li/ncku-thesis-template-latex/pull/38)\)

#### v1.5.6 [Sep 23, 2018]:

- **更新**:

  增加`模版和學位考試系統的學位考試論文證明書的FAQ`.

- **修正錯誤**:
  跟隨[學位考試系統](https://campus4.ncku.edu.tw/wwwmenu/program/mou/)中, `口試証明文件 (Oral presentation document)` 改為 `學位考試論文證明書 (Defense Certificate)`.

#### v1.5.5 [Jul 28, 2018]:

- **修正錯誤**:

  [感謝 abby50066 在 Issue \#31 中的回報](https://github.com/wengan-li/ncku-thesis-template-latex/issues/31), 修正`Institute of Computer Science and Information Engineering` 而不是 `Insitute of Computer Science and Information Engineering`.

#### v1.5.4 [Jul 19, 2018]:

- **修正錯誤**:

  [感謝 hirokiht 在 Issue \#29 中的回報](https://github.com/wengan-li/ncku-thesis-template-latex/issues/29), 修正英文口試的學校地址.

#### v1.5.3 [Jul 11, 2018]:

- **修正錯誤**:

  [感謝 abby50066 在 Issue \#28 中的回報](https://github.com/wengan-li/ncku-thesis-template-latex/issues/28), 修正學校的最新所訂的[\[105.12.15 105 學年度第 2 次教務會議修正過的國立成功大學博碩士學位論文格式規範\]](http://cid.acad.ncku.edu.tw/ezfiles/56/1056/img/730/degree4-1.pdf)漏掉修正的內頁邊界:

  - 舊版: 上 2.3cm、下 3.5cm(含頁碼)、左 2.5cm、右 3cm
  - 新版: 上 23mm、下 35mm（含頁碼）、左 30mm、右 25mm

#### v1.5.2 [Jan 14, 2017]:

- **更新原因**:

  得到 '成大圖書館 系統管理組-數位論文小組' 的通知, 以跟隨學校的最新所訂的[\[105.12.15 105 學年度第 2 次教務會議修正過的國立成功大學博碩士學位論文格式規範\]](http://cid.acad.ncku.edu.tw/ezfiles/56/1056/img/730/degree4-1.pdf). 新的論文格式規範更新內容為：

  - 舊版: 在封面上, 碩士班跟博士班是顯示不同的日期 (年、月、(日)).
  - 新版: 封面日期是統一使用學位考試合格(口試合格單)單為主要參考日期 (年、月(學位考試通過日期)). 例如 105 年 7 月口試，則封面日期為 中華民國 105 年 7 月 或 2016 年 7 月.

- **更新**:
  1. 更新 Appendix 中'國立成功大學博碩士學位論文格式規範'的說明文件.
  2. 更新 Appendix 中'2016 論文提交說明簡報檔'的簡報檔.
  3. 在`conf.tex`中關掉`\SetCoverDate`, 因為封面日期直接使用口試日期, 故不需再另設定. 但是不知道其他的學校所定的規範是否要分開, 故保留這功能.
  4. 中文封面的日期由`年月日`變成`年月`.
  5. 拿掉 Extended Abstract 中紅字的顏色.
  6. 更新模版有關論文格式規範變更的內容說明.
  7. 更新封面日期固定為口試日期.
  8. 更新.gitignore 會無視掉內文中所使用的 PDF 檔的問題.
  9. 更新 CONTRIBUTE 名單

#### v1.5.1 [Nov 26, 2016]:

- **更新**:

  修正微量在`conf.tex`中的`章節標題的設定`提到的例子的說明錯誤.

- **提供的 APIs**:

  [感謝 yusie1978 在 Issue \#18 中提議](https://github.com/wengan-li/ncku-thesis-template-latex/issues/20), 故新增以下 APIs:

  - `\InsertDefinition`
  - `\InsertCondition`
  - `\InsertProblem`
  - `\InsertExample`
  - `\InsertTheorem`
  - `\InsertLemma`
  - `\InsertCorollary`
  - `\InsertProposition`
  - `\InsertConjecture`
  - `\InsertCriterion`
  - `\InsertAssertion`
  - `\InsertQuestion`
  - `\InsertHypothesis`
  - `\InsertProof`
  - `\InsertNote`
  - `\InsertAnnotation`
  - `\InsertClaim`
  - `\InsertCase`
  - `\InsertAcknowledgment`
  - `\InsertConclusion`
  - `\InsertSummary`

- **已知問題**:

  Table/Equation/Figure/Theorem 在 Appendix(附錄)中的 Numbering 顯示正常, 但沒法轉換成正確的英文符號. \([定為 Issue 22](https://github.com/wengan-li/ncku-thesis-template-latex/issues/22#issue-191855677)\)

#### v1.5.0 [Sep 11, 2016]:

**這版的更新是為了讓非成大的同學或人士都能建基於這模版以改成自己所需的模版. 故任何同學如已經在使用這模版, 同時要準備用來交出最終版給學校的話, 是不用更新到這一版的.**

- **更新**:
  1. 重構模版的設定檔的檔案路徑和一些模版的 APIs 名字, 這變動是為了讓非成大的同學或人士都能建基於這模版以建立出自己所需的模版, 同時保留能使用本模版提供的功能. 詳細[請看 Customization.md](https://github.com/wengan-li/ncku-thesis-template-latex/blob/master/thesis/template/style/Customization.md)這檔案中的內容.
  2. 在 README.md 中補上學校對論文要求的 URL.

#### v1.4.9 [Jule 29, 2016]:

- **更新**:
  1. 在`conf.tex`中增加圖書館對封面的日期要求說明. \([由 loveakai 在 Issue \#18 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/18#issue-168091165)\)
  2. 由於圖書館的人員認為英文延伸摘要部分的浮水印太過淡, 幾乎看不到, 故把所有使用到的預設透明值調回高一點. \([由 loveakai 在 Issue \#18 中提出](https://github.c址om/wengan-li/ncku-thesis-template-latex/issues/18#issue-168091165)\)
  3. 修正了一些在 README.md 中的說明文字.

#### v1.4.8 [Jule 20, 2016]:

- **修正錯誤**:

  修正圖書館要求中/英文摘要是由羅馬數字頁碼`i`開始, 而非由封面算起. \([由 spotdy 在 Issue \#12 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/12#issuecomment-233812581)\)

- **更新**:

  重新對所有檔案進行編碼成 UTF-8, 並修改行尾是使用\*nix 系統的的`\n`, 而非 Windows 的`\r\n`, 以增加對所有平台的相容性. \([感謝 KuoE0 提供 Pull request \#15](https://github.com/wengan-li/ncku-thesis-template-latex/pull/15)\)

#### v1.4.7 [Jule 6, 2016]:

**緊急修正**

- **修正錯誤**:

  修正英文延伸摘頁碼顯示問題. \([由 ujmyhn 在 Issue \#12 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/12#issuecomment-230395774)\)

#### v1.4.6 [June 7, 2016]:

- **修正錯誤**:

  修正 Figure/Table/Equation 預設使用阿拉伯數字, 即使用 [1.2] 這種格式來顯示. \([由 loveakai 在 Issue \#10 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/10#issuecomment-223983366)\)

- **提供/移除的 APIs**:
  放棄使用

  1. \SetChapterReferenceTitle
  2. \ChapterReferenceTitleInChi
  3. \ChapterReferenceTitleInEng
  4. \BibStyleUseAbbrv
  5. \BibStyleUsePlain
  6. \BibStyleUseAlpha
  7. \BibStyleUseApacite

  統一使用`\SetupReference`, 修改的想法和理由跟`v1.4.5`中改使用`\SetNumberingFormat`是幾乎相同的, 主要都是原有使用方式過於複雜, 增加同學的困擾. 並舊有方式不方便提供新格式.

- **更新**:
  更新相關的說明文件.

#### v1.4.5 [June 2, 2016]:

**緊急修正 v1.4.4 所產生的問題.**
**重新設計更新了模版的排版底層使用方式, 故建議升級到這一版.**
**這版影響到部份`conf.tex`的內容, 如同學不需要使用在 conf.tex 的新功能則不受影響.**

- **修正錯誤**:

  1. 修正`\StartSection`, `\StartSubSection`和`\StartSubSubSection`前如果沒有 `\\\\` 符號或空行的話, 標題會接續在前段後面出現. 同樣錯誤都有出現在 Extended Abstract, 故連同修正. \([由 loveakai 在 Issue \#10 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/10#issuecomment-222079658)\)

- **提供/移除的 APIs**:

  1. 放棄使用由`v1.4.4`提供的
     1. \ChapterTitleNumFormat
     2. \SectionTitleNumFormat
     3. \SubSectionTitleNumFormat
     4. \SubSubSectionTitleNumFormat
     5. \AppendixChapterTitleNumFormat
     6. \AppendixSectionTitleNumFormat
     7. \AppendixSubSectionTitleNumFormat
     8. \AppendixSubSubSectionTitleNumFormat
     9. 以及相關的\StyleXXXXX 所有 APIs

  理由為: 1. 使用方式過於複雜, 增加同學的困擾. 2. 使用方式不直覺, 如同一種的數字類型會因應用在哪, 必須使用對應的 API. 故產生同一個位置 (如 Chapter) 卻有 7 種對應的 API 去使用 7 種的數字類型. 3. [由 ujmyhn 在 Issue \#12 中的回報](https://github.com/wengan-li/ncku-thesis-template-latex/issues/12#issuecomment-221553312)才發現, 之前的在`v1.4.4`的底層新設計方式令到沒法提供因不同的數字類型在引用時保持使用所設定的數字類型, 同時發現沒法修改原有的 API 來修正這問題. 故只好完全重新設計. 4. 正由於這個的使用方式和底層設計方式複雜, 對維護這模版造成很大的困擾和難度.

  一律改使用新的`\SetNumberingFormat`去對應以上的功能和提供更多的設定. 並能在未來增加功能時, 不必增加同學的重新學習的麻煩.

  2. 在`\SetNumberingFormat`中提供`TextAlign`去設定章節題目的位置 (Left: 左, Center: 中, Right: 右), 但對固定位置的章題目無效. \([由 loveakai 在 Issue \#13 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/13#issue-157839778)\).

- **更新**:
  1. 在目錄中, 在`章節號碼`跟`章節題目`中增加了一些空白, 以提高可閱讀性.
  2. 更新相關的說明文件.
  3. 重新編寫`v1.4.4`的 ChangeLog 部份內容, 以更清楚的方式來說明.

#### v1.4.4 [May 25, 2016]:

**修正由`v1.3.4`到`v1.4.3`所產生出來的錯誤, 並新增/修正/移除了一些的使用方式, 和更新了整個模版的排版和設計. 故建議升級到這一版.**
**這版影響到`conf.tex`的內容, 如同學不需要使用在 conf.tex 的新功能則不受影響.**

- **修正錯誤**:

  1. [由 ujmyhn 在 Issue \#12 中的回報](https://github.com/wengan-li/ncku-thesis-template-latex/issues/12#issue-156131650)而發現, 太容易因修改章節數字的格式而影響其他大量事物, 故重新設計`ncku.sty`的格式.
  2. 在 Appendix 中, 章節號碼的錯誤, 如'6.1'卻不是'A.1' \([由 ujmyhn 在 Issue \#12 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/12#issue-156131650)\).
  3. 使用 equation 時, equation 的號碼受新的格式而影響 \([由 loveakai 在 Issue \#12 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/12#issuecomment-220825783)\).
  4. 使用 table 時, table 的號碼受新的格式而影響 \([由 ujmyhn 在 Issue \#12 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/12#issue-156131650)\).
  5. 修正英文延伸摘要中的 Table 和 Figure 都不會顯示在目錄中.
  6. 修正由`v1.1.2`跟[Issue \#6](https://github.com/wengan-li/ncku-thesis-template-latex/issues/6)提到的一直殘下來的錯字(templete -> template).

- **提供/移除的 APIs**:

  1. 因修改和出現功能重複的關係, 故拿掉了原本正在提供的 APIs: `\ChapterTitleInChi` -> 請改使用`\ChapterTitleNumFormat`, 並以 Error 方式進行提醒.
  2. 重新設計行距的使用方式, 故`ThesisWroteInChi`由這版被移除, 改以 Error 方式進行提醒.
  3. 在`conf.tex`中新增提供`\SetLineStretch`來自定行距.
  4. 新增可使用`\ChapterTitleNumFormat`或`\AppendixChapterTitleNumFormat`同時自定號碼和旁邊的一些內容, 相關的使用方式請看`conf.tex`和說明文件 \([由 ujmyhn 在 Issue \#12 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/12#issue-156131650)\).
  5. 更新`\InsertFigure`, `\InsertTable`, Table/Figure 可以新增`opacity`的設定, 以控制背景白底的透明度 \([由 ujmyhn 在 Issue \#12 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/12#issue-156131650)\).
  6. 在`conf.tex`提供`\SetCustomFigureName`和`\SetCustomTableName`以自定圖表的文字, 如 Table 2.1 -> 表 2.1 或 Figure 2.1 -> 圖 2.1 \([由 ujmyhn 在 Issue \#12 中提出](https://github.com/wengan-li/ncku-thesis-template-latex/issues/12#issue-156131650)\).

- **更新**:
  1. 因應`ncku.sty`的新修改, 故同時對部份底層的 APIs 進行重新設計.
  2. 更新了`ncku.sty`中的內容說明.
  3. 更新核心檔案的版權資料的說明.
  4. 重新調整整份模版說明文件的排版.
  5. 更新所有範例相關的文件到這一版.

#### v1.4.3 [May 21, 2016]:

1. 提供可自定章節`參考文獻`的題目, 而非固定的`References`. 請參考`conf.tex`中的`\ChapterReferenceTitleInChi`, `\ChapterReferenceTitleInEng`, `\SetChapterReferenceTitle`.

#### v1.4.2 [May 21, 2016]:

**緊急修正 v1.4.1 所產生的錯誤**

1. 修正中文數字格式的`\StyleCNumChiNum`, `\StyleSNumChiNum`, `\StyleSSNumChiNum`和`\StyleSSSNumChiNum`只有零的錯誤 \([Issue \#10](https://github.com/wengan-li/ncku-thesis-template-latex/issues/10)\).
2. 修正天干數字格式的`\StyleCNumTiangan`, `\StyleSNumTiangan`, `\StyleSSNumTiangan`和`\StyleSSSNumTiangan`沒法使用的問題.
3. 修正當使用了`\ChapterTitleInChi`, 章節的數字都會同時馬上自動轉成中文, 但這應該是交由同學自行決定.

#### v1.4.1 [May 19, 2016]:

**建議升級到這一版, 因為要修改部份`ncku.sty`和`英文延伸摘要(Extended Abstract)`的內容**

**由於 package `zhnumber`已改成模版所使用的基礎 package 之一, 故更新 MiKTeX 是必須的. 故請看有關`'3.3.3 更新MiKTeX'`章節 (但如果是最近才下載 MiKTeX 的話, 理應不用更新).**

- **更新**:

  1. 增加檢查必須要使用 XeLaTex 來使用這模版, 否則以 Error 方式進行提醒.
  2. 重新編寫字型相關的使用方式, 以保證不會因引用 packages 時影響到我們想要的字型設定.
  3. 修正`v1.3.4`後所影響的到清單和段距的空間.
  4. 在`conf.tex`中提供可自行設定章節數字的格式 (中文, 阿拉伯數字, 羅馬字等)
  5. 以下過去的 API 由這版開始被移除, 改以 Error 方式進行提醒.
  6. `\ChapterTitleNumInChi` -> 停用
  7. `\InsertMultiImages` -> 請改使用`\InsertFigures`
  8. `\InsertCenterImage` -> 請改使用`\InsertFigure`
  9. `\InsertImage` -> 請改使用`\InsertFigure`
  10. 刪除`example/abstract/extended.tex`, 直接共用`context/abstract/extended.tex`, 以減少多餘的檔案.
  11. 對`英文延伸摘要(Extended Abstract)`進行重新設計和排版, 提供以更方便的編寫和正常的顯示. 但同時保留以前的使用方式, 以能無痛升級.
  12. 在`conf.tex`中新增`\ThesisWroteInChi`, 以控制要使用為中文或英文而設計的段距.
  13. 修正中文封面的論文題目會跟英文版的一樣位置.
  14. 重新設計封面和口試証明文件的空間和位置, 去掉因內容變更而同時造成位置有所變動的問題.
  15. 變更 Reference 引用的預設格式由`abbrv`轉為`plain`, 以使用作者的全名, 方便讀者進行查詢時使用.
  16. 把部份模版底層所使用的檔案進行了更名, 所以如想直接刪除來更新`ncku`以減少垃圾的檔案都是可推薦的.
  17. 修正`ncku.sty`中目錄顯示圖表和圖片互換了的錯誤.
  18. 更新相關的說明文件.

- **發現情況**:
  1. 意外發現學校提供的`英文延伸摘要(Extended Abstract)撰寫格式說明`中所寫的`建議字型 Times New Roman`這一條, 但發現範例中最上面的論文題目和名字**根本不是**`Times New Roman`字型. 對比`論文題目`中跟`SUMMARY`中的`T`這個字即可, 橫的那條線一個是平滑, 但另一個不是的便是真正的`Times New Roman`. 故無視範例中所顯示的效果, 直接統一使用要求所定出的`Times New Roman`.
  2. 同樣範例應該是`段落為單行間距`, 但發現如果直接拿模版弄出來的 PDF 跟 Word 在同樣 100%大小時作對比時, 卻發現是一樣的. 但卻沒法跟範例有同樣的效果. 故直接統一使用 Latex 使用的單行間距的預設設定.

#### v1.4.0 [May 9, 2016]:

**極度推薦升級到這一版**

1. 重新繪製圖書館所提供的浮水印, 並得到 '成大圖書館 系統管理組-數位論文小組' 所檢查和接受. 故模版和圖書館會提供全新無損版的浮水印.
2. 重新調整整份模版說明文件的排版.
3. 更新所有範例相關的文件到這一版.

#### v1.3.5 [May 5, 2016]:

1. Appendix 新增由 xeCJK 的 v3.3.4(2016/02/10)版本中提供的 50 頁有關所有 Symbol 的寫法, 極度值得同學們閱讀或在這邊找你所需的 Symbols.
2. 新增介紹章節 '3.3.3 更新 MiKTeX' 去介紹如何更新 MiKTeX

#### v1.3.4 [May 4, 2016]:

某些更新可能會影響同學們的排版 (理應會更好看), 故推薦請檢查更新後的新樣子, 否則可提出回報以讓幫你修改. 另外某些功能可需要更新 MiKTex 到最新版才能使用.

如更新後有任何的錯誤訊息出現, 請重新 rebuild 幾次 thesis.tex 和.bib 應該就能解決.

- **更新**:

  1. 在 conf.tex 中新增\ChapterTitleNumInChi 來控制章節題目呈現中文數字, 可顯示成[第一章]而非[第 1 章] \([Issue \#10](https://github.com/wengan-li/ncku-thesis-template-latex/issues/10)\) (推薦更新 MiKTex 和 Texmaker 到最新版).
  2. 修正把清單(itemize, enumerate 和 description)的行距收緊, 同時都叫內文收緊, 以讓整篇論文的行距都是相同 \([Issue \#10](https://github.com/wengan-li/ncku-thesis-template-latex/issues/10)\).
  3. 更名 conf.tex 中的 API 'ChapterSectionTitleInChi' -> 'ChapterTitleInChi', 底層轉到'\ChapterTitleInChi'來保留這 API.
  4. 更新對 conf.tex 的使用說明.
  5. 新增 package{inputenc}來控制任何在.tex 檔的文字或符號都能正常使用 (.tex 檔案都必須是 UTF-8 格式), 否則有潛在的可能性把文字或符號轉成其他能顯示的內容. 這包括全形和半形的符號.
  6. 更名 conf.tex 中的 API 'CDBothName' -> 'DisplayCoverPeoplesBothNames', 底層轉到'\DisplayCoverPeoplesBothNames'來保留這 API.
  7. 修正字型 Times New Roman 的問題, 使用 package{newtxtext}方式去使用這字型, 這應能處理 Windows 跟 Linux 或 Mac OS 需要使用不同檔名去使用這字型的問題.
  8. 新增使用 package{newtxmath}去讓數學公式的字型更圓滑.

- **發現情況**:
  1. 寫編寫模版時, 大約是 v1.0.0 或更早時, 所使用的 package 和 Texmaker 已是 2 年前左右. 而在編寫這版時為了使用一些新功能, 故把所有 package 和 Texmaker 更新到最新版. 發現符號 ( &#x0027; ) 會產出 ( &#x055A; ), 但經過檢查['大家來學 LaTeX'中的'3.3.3 針對標點符號的遊戲規則'](http://www.cs.pu.edu.tw/~wckuo/doc/latex123/node4.html#SECTION00433000000000000000)卻發現產出 ( &#x055A; ) 才是正常, 而( &#x0027; )則換成要使用 '\textprimstress' 才能顯示. 而為什麼發生這情況則原因不明.

#### v1.3.3 [April 19, 2016]:

1. 修正 ChangeLog 中 v1.3.1 和 v1.3.0 的說明排版錯誤.
2. 修改 README.md 中有關可使用系所的說明, 並增加對應的 URL.

#### v1.3.2 [April 08, 2016]:

1. 新增控制 Reference 和引用時的格式的相關功能和說明 \([Issue \#9](https://github.com/wengan-li/ncku-thesis-template-latex/issues/9)\).
2. 把 ChangeLog 抽出成獨立的檔案.

#### v1.3.1 [March 14, 2016]:

1. 增加 Nomenclatures 功能, 同時增加相關的說明例子.
2. 把這模版的名字由'XeLaTex 模版'改回'LaTex 模版'. 基於當時原本 Google 對'XeLaTex'這字沒有相對的對應到去'LaTex', 故才把部份名字回成'LaTex' (如 GitHub 的 URL). 但現在在'主要功能'有提到是使用 XeLaTex 技術即可 (因為對一般同學基本不知道差異性).
3. 在章節'圖片 Figure'中, 新增'小知識'和'轉換格式'的一些應對同學們有用的內容.
4. 修正部份內容的斷行位置.
5. 修正在章節'產生論文'舊有沒處理的書脊資料, 更換成新的有關封面內容.
6. 修正並統一使用'模版', 而不是'模板'.
7. 刪去一些沒再使用的檔案和內容.
8. 修正'README.md'中範例的 URL \([Issue \#7](https://github.com/wengan-li/ncku-thesis-template-latex/issues/7)\).
9. 修正'README.md'中一些文字說明 \([Issue \#7](https://github.com/wengan-li/ncku-thesis-template-latex/issues/7)\).
10. Table 增加設定和功能, 同時增加相關的說明例子

#### v1.3.0 [Oct 26, 2016]: **重大改版**

由於所修改的內容影響全部內容和排版, 故比較推薦以重新編寫的方式來升級.

- **排版**:

  1. 使用原本'utdiss.sty'來重構'ncku.sty'. 保留有用的內容, 其他都盡量刪去.
  2. 修正內頁邊界錯誤, 原本排版為大約上 3.8cm、下 4.3cm(含頁碼)、左 3.5cm、右 3.4cm. 現修正為上 2.3cm、下 3.5cm(含頁碼)、左 2.5cm、右 3cm, 以符合學校的格式.
  3. 更新封面邊界的使用方式, 產出效果跟舊版效果是一樣
  4. 調整 Chapter 和 Section 的字體大小, 除了 Chapter 字體比較大, Section 跟內容的字體是一樣, 但以粗體來顯示
  5. 更新 Acknowledgments 的標題位置
  6. 更新 Abstract 的標題位置

- **封面**:

  1. 更改 '學生' -> '研究生'
  2. 更改 '教授' -> '博士', 'Prof.' -> 'Dr.' (因為要去除職稱上的差別)
  3. 修正錯字, 'Co-advisor' -> 'Co-Advisor'
  4. 更正 'Master's Dissertation' -> 'Master's Thesis'
  5. 增加內頁. 封面主要用在印刷版, 如精裝版 或 平裝版. 而內頁主要用在電子版 + 印刷版. 在'context.tex'中使用'\DisplayInsideCover'來使用.
  6. 更名 API 'SetThesisDate' -> 'SetCoverDate', 底層轉到'\SetCoverDate'來保留這 API
  7. 更新在 conf.tex 和編寫介紹中, 有關封面日期設定的說明.
  8. 更新在 context.tex 中, 有關要使用哪種封面的說明.
  9. 增加可設定初稿, 會顯示 '(初稿)' (中文版) 和 '(Draft)' (英文版) 在封面在 conf.tex 中使用'\DisplayDraft'來使用.
  10. 在 conf.tex 可使用'\CDBothName'以控制在封面上的學生和老師名字要只顯示中文, 英文或中英文同時顯示.
  11. 在 conf.tex 可使用'\DisplayCoverInChi'或'\DisplayCoverInEng'以控制封面以中文或是英文顯示.

- **書脊**:

  1. 移除書脊功能, 移除任何相關檔案和說明. 基於有影印店說, 就算我們有提供書脊檔案給他們, 他們都會自己使用一些工具重新弄一個書脊出來以給影印機所印出來, 故模版不再需要提供書脊功能.

- **Appendix**:

  1. 更新 2015 版的 '口試注意事項' 和 '學位論文上傳說明'
  2. 補上引用文件的 URL

- **目錄**:

  1. 删除 '封面' 和 '口試証明文件' 出現在目錄
  2. 更正 '致謝' 在目錄顯示正確
  3. 更正 '摘要' 在目錄顯示正確
  4. 目錄使用新的 style 以壓縮內容
  5. 目錄可在 conf.tex 中使用'\IndexChiMode'或'\IndexEngMode'來控制所顯示的標題的文字語言.
  6. 更新'\DisplayIndex', 並新增'\DisplayTablesIndex' 和 '\DisplayFiguresIndex' 在'context.tex'以控制需要顯示的索引內容, 以免得沒有相關的內容, 但多了一頁沒意義的索引頁.
  7. 提供'\SetIndexTitleText', '\SetTablesIndexTitleText' 和 '\SetFiguresIndexTitleText'在 conf.tex 以讓同學們可以自行設定目錄中的標題文字.

- **摘要**:

  1. 修正英文顯示 'Key words' -> 'Keyword'
  2. 更名 API 'StartChiAbstract' -> 'StartAbstractChi', 底層轉到'\StartAbstractChi'來保留這 API
  3. 更名 API 'EndChiAbstract' -> 'EndAbstractChi', 底層轉到'\EndAbstractChi'來保留這 API
  4. 在 conf.tex 可使用'\SetAbstractChiKeywords' 或 '\SetAbstractEngKeywords' 來設定中英文版摘要中的關鍵字
  5. 在 content.tex 可手動控制顯示中英文版摘要和英文延伸摘要

- **口試証明文件**:

  1. 範例的中英文版本可單獨顯示 \([來自 Issue \#5 的提醒](https://github.com/wengan-li/ncku-thesis-template-latex/issues/5)\)
  2. 口試圖檔可單獨使用中/英文版, 或同時使用. \([來自 Issue \#5 的提醒](https://github.com/wengan-li/ncku-thesis-template-latex/issues/5)\)
  3. 調整了一下範例的設計, 以讓'指導教授'和'系 (所) 主管'中間的空間比較分開
  4. 調整了一下範例中口試委員簽署的空間, 以讓口試委員數量最多可放 9 位

- **圖片/表格**:

  1. 更新相關的說明文件
  2. 更名 API '\InsertImage' -> '\InsertFigure', 底層轉到'\InsertFigure'來保留這 API
  3. 圖片和標題背後現在會有白色背景, 讓圖片和標題更加清晰
  4. 更名 API '\InsertMultiImages' -> '\InsertFigures', 底層轉到'\InsertFigures'來保留這 API
  5. 更新改寫'\InsertFigures'的做法, 使用鎖死格式方式來取代計算的方式來調整圖片的位置和大小, 去掉 LaTex 在計算上的困難和潛在的計算錯誤.
  6. 增加 '\InsertTable' 來幫忙插入表單, 並加有白色背景, 讓表單內容更加清晰
  7. 增加斜線功能給表單, 同時增加相關的說明例子

- **其他**:
  1. 更新 CONTRIBUTE 中的名單和使用的稱號
  2. 修正檔名, 應該是'misc.bib', 而不是'msic.bib' \([Issue \#4](https://github.com/wengan-li/ncku-thesis-template-latex/issues/4)\)
  3. 修正錯字 'Templete' -> 'Template', 受影響的 API 為 '\DisplayOralTemplate' (原為 '\DisplayOralTemplete', 底層轉到'\DisplayOralTemplate'來保留這 API) \([Issue \#6](https://github.com/wengan-li/ncku-thesis-template-latex/issues/6)\)
  4. 修正封面和口試証明上的日期因轉換時造成的奇怪空格.
  5. 更新 README.md 中, CC Logo 改使用 HTML 方式來對齊
  6. 更新 README.md 中, 畢業論文要求補上引用的 URL
  7. 更正 '資訊工程系' -> '資訊工程研究所'
  8. 修正引用的 API '\RefXXX' 系列所引用的內容前面會有多餘的空白
  9. 在 conf.tex 使用'\SetKeywords'可設定所產出來的 PDF 中的 Keyword 項目
  10. 在 content.tex 可手動控制顯示中英文版誌謝
  11. 在 conf.tex 使用'\ChapterSectionTitleInChi'可設定章節標題為中文版或是英文版 \([來自 Issue \#5 的提醒](https://github.com/wengan-li/ncku-thesis-template-latex/issues/5)\)

#### v1.2.8:

1. 修正日期在英文書脊中, 會因月份文字的長度而影響位置不一樣的問題

#### v1.2.7:

1. 增加可放置論文題目的長度. 修正在封面和 Oral 的樣板中, 會在題目沒有很長情況下, 被強迫斷行. 長度控制交由同學自己斷行, 以造出比較漂亮題目
2. 修正書脊中題目跟學位不是同一個高度的問題
3. 修正英文 Oral 文件的樣板會出現頁碼的問題

#### v1.2.5:

1. 修正在'Objective'和'Acknowledgments'的錯誤內容

#### v1.2.4:

1. 增加英文封面可同時顯示中英文 \([Issue \#3](https://github.com/wengan-li/ncku-thesis-template-latex/issues/3)\)

#### v1.2.3:

1. 修正統一使用'Fig'去取代'Fig.', 因為當使用'Fig.'時會產生更大的空格
2. 修正在'表格 Table'中的圖片位置
3. 移除在'圖片 Image'的'多張'中舊 API 的說明文字
4. 修正在'圖片 Image'中插入多張的圖片時, 不管是主圖或子圖片都推薦使用'align = center'來進行置中, 除非是為了特殊的原因

#### v1.2.2:

1. 修正在'Induection'中的'ChangeLog'和'License'中一些奇怪多餘的空白

#### v1.2.1:

1. 修正中文書脊文字位置錯誤問題

#### v1.2.0:

1. Appendix 新增'常見問題 Q&A'
2. 把'Induection'中的'ChangeLog'改使用為單一'.tex'檔去存放
3. 增加字眼'共同指導'或'Co-advisor'在封面上 \([Issue \#2](https://github.com/wengan-li/ncku-thesis-template-latex/issues/2)\)
4. 重新調整中文封面中的中英文名字 2 邊的中間空間的大小, 以防止中文名字有 4 個字時, 出現 overlap 的問題.

#### v1.1.6:

1. 刪除'Induection'和'README.md'中的'版本 Version'

#### v1.1.5:

1. 修正每個 Chapter 的第一頁的頁碼位置跟其他頁面不同的問題 \([Issue \#1](https://github.com/wengan-li/ncku-thesis-template-latex/issues/1)\)

#### v1.1.4:

1. 修正目錄自己沒有在目錄的 Linking 中出現

#### v1.1.3:

1. 修正 README.md 中內容的位置錯誤

#### v1.1.2:

1. 重寫有關 figure API 的 code, 增加和優化那些功能 (如增加 align)
2. 更新 README.md 的內容
3. 增加 ChangeLog

#### v1.1.1:

1. 把'Abstract'的中文版本是以'摘要'來顯示
2. 修改和改良有關 oral 文件的一些 path 位置

#### v1.1.0:

1. 增加版權資料到一些核心檔案
2. 修改和增加一些圖書館要求的內容
3. 修改有關 abstract 的一些 path 位置
4. 正式得到學校有關部門對這模版的接受

#### v1.0.1:

1. 修改少量錯誤的內容和 URL 連接

#### <= v1.0.0:

1. 正式完成版本
