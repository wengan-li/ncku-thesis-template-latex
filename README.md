## National Cheng Kung University (NCKU) Thesis/Dissertation Template in XeLaTex ##
### 台灣國立成功大學碩博士用畢業論文XeLaTex模板 ###

這是國立成功大學碩博士用畢業論文的 LaTex 模板. 這模板是以'102.5.14日101學年第2次教務會議通過'的畢業論文要求來設計, 請留意學校的最新所訂的要求能否使用這樣版.

### Main feature 主要功能
  1. 能同時讓你編寫中英文內容
  2. 主要資料能自動產生
     (只留下要填寫的部份, 其他都由模板自動產生: 如封面, 目錄, 口試合格證明文件樣板等)
  3. 內含非常基本的Latex使用教學手冊
  4. 提供簡易的語法去使用一些複雜的Latex功能

### Available to use 已被學校負責單位接受

這模板的
* 格式/設計: 已經經過 '成大圖書館 系統管理組-數位論文小組' 所檢查和接受.
* 口試合格證明文件: 已經經過 '教務處-課務組' 所檢查和接受.

即是可使用本模板來編寫你畢業論文, 並能交給圖書館收藏存放.

**注意**: 是'接受', 而不是'認可', 即是不屬於學校認可, 但可以使用並且不會有任何問題.

但是因為各系所有各自的格式, 故請先留意自己的系所有沒有格式要求. 如果沒有, 則這模版應該用來使用. 否則要看系所上的格式, 是否跟這模版有相同的寫法.

而如果這表名單中沒有顯示你的系所, 但你已經知道是否能使用, 請告知以供更新.

已知可用的系所:
* 資訊工程學系 Department of Computer Science and Information Engineering

應該不可使用的系所:
* [生物科技研究所 Institute of Biotechnology](http://www.biotech.ncku.edu.tw/files/archive/331_4b79187a.doc)
* [體育健康與休閒研究所 Institute of Physical Education, Health and Leisure Studies](http://www.ncku.edu.tw/~deprb/docs/Thesis%20Regulation%20.doc)

### Example 樣板/範例
[有關 樣板/範例 請到這邊 <--](https://github.com/wengan-li/ncku-thesis-template-release)

### License 授權條款
本著作採用創用 CC 姓名標示-非商業性-相同方式分享 4.0 授權條款

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

![CC-BY-NC-SA](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png "CC Attribution-NonCommercial-ShareAlike License")

### Other 其他
如果對本模板沒有興趣, 有[另一位同學提供的模板](https://github.com/lycsjm/nckuthesis)可使用.

### ChangeLog
* v1.3.0: 重大改版 (如果是使用直接取代舊版檔案的升級方式, 請注意以下所修改的部份有沒有影響自身的內容)
    + **封面**:
        a. 更改 '學生' -> '研究生'
        b. 更改 '教授' -> '博士', 'Prof.' -> 'Dr.' (因為要去除職稱上的差別)
        c. 修正錯字, 'Co-advisor' -> 'Co-Advisor'
        d. 更正 'Master's Dissertation' -> 'Master's Thesis'
        e. 增加封面內頁和修改封面的學校Logo. 封面是顯示所有封面內容, 但沒有學校Logo. 而內頁是顯示所有封面內容, 但有學校Logo. 在'context.tex'中使用'\DisplayInsideCover'來使用.
        f. 更名API 'SetThesisDate' -> 'SetCoverDate', 底層轉到'\SetCoverDate'來保留這API
        g. 更新在conf.tex和編寫介紹中, 有關封面日期設定的說明.
    + **書脊**:
        a. 修正英文版的日期會因月份的長度, 而造成年份的位置不是跟月份對齊
    + **功能**:
        a. 增加可設定初稿, 會顯示 '(初稿)' (中文版) 和 '(Draft)' (英文版) 在封面和書脊 在'conf.tex'中使用'\DisplayDraft'來使用.
    + **Appendix**:
        a. Appendix 更新2015版的 '口試注意事項' 和 '學位論文上傳說明'
        b. 補上引用文件的URL
    + **其他**:
        a. 更新CONTRIBUTE中的名單和使用的稱號
        b. 修正檔名, 應該是'misc.bib', 而不是'msic.bib' \([Issue \#4](https://github.com/wengan-li/ncku-thesis-template-latex/issues/4)\)
        c. 修正錯字 'Templete' -> 'Template', 受影響的API為 '\DisplayOralTemplate' (原為 '\DisplayOralTemplete', 底層轉到'\DisplayOralTemplate'來保留這API) \([Issue \#7](https://github.com/wengan-li/ncku-thesis-template-latex/issues/7)\)
        d. 删除 '封面' 和 '口試証明文件' 出現在目錄
        e. 修正封面和口試証明上的日期因轉換時造成的奇怪空格.

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
 4. 正式得到學校有關部門對這模板的接受

* v1.0.1: 修改少量錯誤的內容和URL連接

* <= v1.0.0: 正式完成版本
