## National Cheng Kung University (NCKU) Thesis/Dissertation Template in LaTex ##
### 台灣國立成功大學碩博士用畢業論文LaTex模版 ###

這是國立成功大學碩博士用畢業論文的LaTex模版. 這模版是以'102.5.14日101學年第2次教務會議通過'的畢業論文要求來設計, 請留意學校的最新所訂的要求能否使用這樣板.

### Main feature 主要功能
  1. 能同時讓你編寫中英文內容 (建基於XeLaTex)
  2. 主要資料能自動產生
     (只留下要填寫的部份, 其他都由模版自動產生: 如封面, 目錄, 口試合格證明文件樣板等)
  3. 內含非常基本的LaTex使用教學手冊
  4. 提供簡易的語法去使用一些複雜的LaTex功能

### Available to use 已被學校負責單位接受

這模版的
* 格式/設計: 已經經過 '成大圖書館 系統管理組-數位論文小組' 所檢查和接受.
* 口試合格證明文件: 已經經過 '教務處-課務組' 所檢查和接受.

即是可使用本模版來編寫你畢業論文, 並能交給圖書館收藏存放.

**注意**: 是'接受', 而不是'認可', 即是不屬於學校認可, 但可以使用並且不會有任何問題.

但是因為各系所有各自的格式, 故請先留意自己的系所有沒有格式要求.
如果沒有, 則這模版應該可以使用的.
否則要看系所上的格式, 是否跟這模版有相同的寫法.

而如果這表名單中沒有顯示你的系所, 但你已經知道是否能使用, 請告知以供更新.

已知可用的系所:
* 資訊工程學系 Department of Computer Science and Information Engineering

應該不可使用的系所:
* [生物科技研究所 Institute of Biotechnology](http://www.biotech.ncku.edu.tw/files/archive/331_4b79187a.doc)
* [體育健康與休閒研究所 Institute of Physical Education, Health and Leisure Studies](http://www.ncku.edu.tw/~deprb/docs/Thesis%20Regulation%20.doc)

### Sample 樣板/範例
[有關 樣板/範例 請到這邊 <--](https://github.com/wengan-li/ncku-thesis-template-latex-sample)

### Other 其他
如果對本模版沒有興趣, 有[另一位同學提供的模版](https://github.com/lycsjm/nckuthesis)可使用.

### License 授權條款
本著作採用創用 CC 姓名標示-非商業性-相同方式分享 4.0 授權條款

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

<p align="center">
  <img src='https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png' alt="CC-BY-NC-SA-4.0"/>
</p>

### ChangeLog 版本修改
* v1.3.1:
    1. 增加Nomenclatures功能, 同時增加相關的說明例子
    2. 把這模版的名字由'XeLaTex模版'改回'LaTex模版'. 基於當時原本Google對'XeLaTex'這字沒有相對的對應到去'LaTex', 故才把部份名字回成'LaTex' (如GitHub的URL). 但現在在'主要功能'有提到是使用XeLaTex技術即可 (因為對一般同學基本不知道差異性).
    3. 在章節'圖片 Figure'中, 新增'小知識'和'轉換格式'的一些應對同學們有用的內容.
    4. 修正部份內容的斷行位置.
    5. 修正在章節'產生論文'舊有沒處理的書脊資料, 更換成新的有關封面內容.
    6. 修正並統一使用'模版', 而不是'模板'.
    7. 刪去一些沒再使用的檔案和內容.
    8. 修正'README.md'中範例的URL \([Issue \#7](https://github.com/wengan-li/ncku-thesis-template-latex/issues/7)\).
    9. 修正'README.md'中一些文字說明 \([Issue \#7](https://github.com/wengan-li/ncku-thesis-template-latex/issues/7)\).
    10. Table增加設定和功能, 同時增加相關的說明例子

* v1.3.0: **重大改版**
    由於所修改的內容影響全部內容和排版, 故比較推薦以重新編寫的方式來升級.
    + **排版**:
        1. 使用原本'utdiss.sty'來重構'ncku.sty'. 保留有用的內容, 其他都盡量刪去.
        2. 修正內頁邊界錯誤, 原本排版為大約上3.8cm、下4.3cm(含頁碼)、左3.5cm、右3.4cm. 現修正為上2.3cm、下3.5cm(含頁碼)、左2.5cm、右3cm, 以符合學校的格式.
        3. 更新封面邊界的使用方式, 產出效果跟舊版效果是一樣
        4. 調整Chapter和Section的字體大小, 除了Chapter字體比較大, Section跟內容的字體是一樣, 但以粗體來顯示
        5. 更新Acknowledgments的標題位置
        6. 更新Abstract的標題位置
    + **封面**:
        1. 更改 '學生' -> '研究生'
        2. 更改 '教授' -> '博士', 'Prof.' -> 'Dr.' (因為要去除職稱上的差別)
        3. 修正錯字, 'Co-advisor' -> 'Co-Advisor'
        4. 更正 'Master's Dissertation' -> 'Master's Thesis'
        5. 增加內頁. 封面主要用在印刷版, 如精裝版 或 平裝版. 而內頁主要用在電子版 + 印刷版. 在'context.tex'中使用'\DisplayInsideCover'來使用.
        6. 更名API 'SetThesisDate' -> 'SetCoverDate', 底層轉到'\SetCoverDate'來保留這API
        7. 更新在conf.tex和編寫介紹中, 有關封面日期設定的說明.
        8. 更新在context.tex中, 有關要使用哪種封面的說明.
        9. 增加可設定初稿, 會顯示 '(初稿)' (中文版) 和 '(Draft)' (英文版) 在封面在conf.tex中使用'\DisplayDraft'來使用.
        10. 在conf.tex可使用'\CDBothName'以控制在封面上的學生和老師名字要只顯示中文, 英文或中英文同時顯示.
        11. 在conf.tex可使用'\DisplayCoverInChi'或'\DisplayCoverInEng'以控制封面以中文或是英文顯示.
    + **書脊**:
        1. 移除書脊功能, 移除任何相關檔案和說明. 基於有影印店說, 就算我們有提供書脊檔案給他們, 他們都會自己使用一些工具重新弄一個書脊出來以給影印機所印出來, 故模版不再需要提供書脊功能.
    + **Appendix**:
        1. 更新2015版的 '口試注意事項' 和 '學位論文上傳說明'
        2. 補上引用文件的URL
    + **目錄**:
        1. 删除 '封面' 和 '口試証明文件' 出現在目錄
        2. 更正 '致謝' 在目錄顯示正確
        3. 更正 '摘要' 在目錄顯示正確
        4. 目錄使用新的style以壓縮內容
        5. 目錄可在conf.tex中使用'\IndexChiMode'或'\IndexEngMode'來控制所顯示的標題的文字語言.
        6. 更新'\DisplayIndex', 並新增'\DisplayTablesIndex' 和 '\DisplayFiguresIndex' 在'context.tex'以控制需要顯示的索引內容, 以免得沒有相關的內容, 但多了一頁沒意義的索引頁.
        7. 提供'\SetIndexTitleText', '\SetTablesIndexTitleText' 和 '\SetFiguresIndexTitleText'在conf.tex以讓同學們可以自行設定目錄中的標題文字.
    + **摘要**:
        1. 修正英文顯示 'Key words' -> 'Keyword'
        2. 更名API 'StartChiAbstract' -> 'StartAbstractChi', 底層轉到'\StartAbstractChi'來保留這API
        3. 更名API 'EndChiAbstract' -> 'EndAbstractChi', 底層轉到'\EndAbstractChi'來保留這API
        4. 在conf.tex可使用'\SetAbstractChiKeywords' 或 '\SetAbstractEngKeywords' 來設定中英文版摘要中的關鍵字
        5. 在content.tex可手動控制顯示中英文版摘要和英文延伸摘要
    + **口試証明文件**:
        1. 範例的中英文版本可單獨顯示 \([來自Issue \#5的提醒](https://github.com/wengan-li/ncku-thesis-template-latex/issues/5)\)
        2. 口試圖檔可單獨使用中/英文版, 或同時使用. \([來自Issue \#5的提醒](https://github.com/wengan-li/ncku-thesis-template-latex/issues/5)\)
        3. 調整了一下範例的設計, 以讓'指導教授'和'系 (所) 主管'中間的空間比較分開
        4. 調整了一下範例中口試委員簽署的空間, 以讓口試委員數量最多可放9位
    + **圖片/表格**:
        1. 更新相關的說明文件
        2. 更名API '\InsertImage' -> '\InsertFigure', 底層轉到'\InsertFigure'來保留這API
        3. 圖片和標題背後現在會有白色背景, 讓圖片和標題更加清晰
        4. 更名API '\InsertMultiImages' -> '\InsertFigures', 底層轉到'\InsertFigures'來保留這API
        5. 更新改寫'\InsertFigures'的做法, 使用鎖死格式方式來取代計算的方式來調整圖片的位置和大小, 去掉LaTex在計算上的困難和潛在的計算錯誤.
        6. 增加 '\InsertTable' 來幫忙插入表單, 並加有白色背景, 讓表單內容更加清晰
        7. 增加斜線功能給表單, 同時增加相關的說明例子
    + **其他**:
        1. 更新CONTRIBUTE中的名單和使用的稱號
        2. 修正檔名, 應該是'misc.bib', 而不是'msic.bib' \([Issue \#4](https://github.com/wengan-li/ncku-thesis-template-latex/issues/4)\)
        3. 修正錯字 'Templete' -> 'Template', 受影響的API為 '\DisplayOralTemplate' (原為 '\DisplayOralTemplete', 底層轉到'\DisplayOralTemplate'來保留這API) \([Issue \#6](https://github.com/wengan-li/ncku-thesis-template-latex/issues/6)\)
        4. 修正封面和口試証明上的日期因轉換時造成的奇怪空格.
        5. 更新README.md中, CC Logo改使用HTML方式來對齊
        6. 更新README.md中, 畢業論文要求補上引用的URL
        7. 更正 '資訊工程系' -> '資訊工程研究所'
        8. 修正引用的API '\RefXXX' 系列所引用的內容前面會有多餘的空白
        9. 在conf.tex使用'\SetKeywords'可設定所產出來的PDF中的Keyword項目
        10. 在content.tex可手動控制顯示中英文版誌謝
        11. 在conf.tex使用'\ChapterSectionTitleInChi'可設定章節標題為中文版或是英文版 \([來自Issue \#5的提醒](https://github.com/wengan-li/ncku-thesis-template-latex/issues/5)\)

* v1.2.8: 修正日期在英文書脊中, 會因月份文字的長度而影響位置不一樣的問題

* v1.2.7:
 1. 增加可放置論文題目的長度. 修正在封面和Oral的樣板中, 會在題目沒有很長情況下, 被強迫斷行. 長度控制交由同學自己斷行, 以造出比較漂亮題目
 2. 修正書脊中題目跟學位不是同一個高度的問題
 3. 修正英文Oral文件的樣板會出現頁碼的問題

* v1.2.5: 修正在'Objective'和'Acknowledgments'的錯誤內容

* v1.2.4: 增加英文封面可同時顯示中英文 \([Issue \#3](https://github.com/wengan-li/ncku-thesis-template-latex/issues/3)\)

* v1.2.3: 
 1. 修正統一使用'Fig'去取代'Fig.', 因為當使用'Fig.'時會產生更大的空格
 2. 修正在'表格 Table'中的圖片位置
 3. 移除在'圖片 Image'的'多張'中舊API的說明文字
 4. 修正在'圖片 Image'中插入多張的圖片時, 不管是主圖或子圖片都推薦使用'align = center'來進行置中, 除非是為了特殊的原因

* v1.2.2: 修正在'Induection'中的'ChangeLog'和'License'中一些奇怪多餘的空白

* v1.2.1: 修正中文書脊文字位置錯誤問題

* v1.2.0:
 1. Appendix新增'常見問題Q&A'
 2. 把'Induection'中的'ChangeLog'改使用為單一'.tex'檔去存放
 3. 增加字眼'共同指導'或'Co-advisor'在封面上 \([Issue \#2](https://github.com/wengan-li/ncku-thesis-template-latex/issues/2)\)
 4. 重新調整中文封面中的中英文名字2邊的中間空間的大小, 以防止中文名字有4個字時, 出現overlap的問題.

* v1.1.6: 刪除'Induection'和'README.md'中的'版本 Version'

* v1.1.5: 修正每個Chapter的第一頁的頁碼位置跟其他頁面不同的問題 \([Issue \#1](https://github.com/wengan-li/ncku-thesis-template-latex/issues/1)\)

* v1.1.4: 修正目錄自己沒有在目錄的Linking中出現

* v1.1.3: 修正README.md中內容的位置錯誤

* v1.1.2:
 1. 重寫有關figure API的code, 增加和優化那些功能 (如增加align)
 2. 更新README.md的內容
 3. 增加ChangeLog

* v1.1.1:
 1. 把'Abstract'的中文版本是以'摘要'來顯示
 2. 修改和改良有關oral文件的一些path位置

* v1.1.0:
 1. 增加版權資料到一些核心檔案
 2. 修改和增加一些圖書館要求的內容
 3. 修改有關abstract的一些path位置
 4. 正式得到學校有關部門對這模版的接受

* v1.0.1: 修改少量錯誤的內容和URL連接

* <= v1.0.0: 正式完成版本
