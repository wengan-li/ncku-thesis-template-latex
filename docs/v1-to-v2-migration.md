<!-- bilingual:complete -->

# 成大論文範本1.x至2.x升級指南 / NCKU Thesis Template 1.x-to-2.x Migration Guide

Production target / 正式目標：[`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734)

V2透過完整2.x line的相容層，保留machine-audited 1.x LaTeX/xparse及literal `\def` declarations。既有專案可先升級template implementation、驗證NCKU輸出，再逐步採用native V2 profile架構。

V2 preserves the machine-audited 1.x LaTeX/xparse and literal `\def` declaration surfaces through the complete 2.x line. Existing projects can migrate template implementation first, verify NCKU output, and adopt native V2 profiles gradually.

## 開始前 / Before you start

**繁體中文**

1. Commit或封存完整、可正常建置的1.x專案。
2. 再建置一次1.x PDF並保留作文字及視覺reference。
3. 記錄XeLaTeX版本、頁數、紙張、封面／口試日期及所有刻意啟用的Draft／浮水印設定。
4. 分清學生資料、template implementation及主文件；不要覆寫尚未commit的論文目錄後再依賴Git猜測原值。

**English**

1. Commit or archive the complete working 1.x project.
2. Build the 1.x PDF once more and retain it as a text/visual reference.
3. Record the XeLaTeX version, page count, paper size, cover/oral dates, and every deliberately enabled Draft/watermark option.
4. Separate student data, template implementation, and the root document. Do not overwrite an uncommitted thesis directory and expect Git to reconstruct it later.

```text
Student-owned / 學生資料:
  conf/conf.tex
  context/
  figures/
  bibliography data
  local certificate files

Template-owned / 範本實作:
  template/
  fonts/
  build configuration
  packaged examples

Root document / 主文件:
  thesis.tex (merge local edits deliberately / 有意識地merge本地修改)
```

## 相容優先路徑 / Compatibility-first path

**繁體中文**

此路徑適用於正在撰寫中的NCKU論文。保留`conf/conf.tex`、內容、圖片、書目資料及本地證明書；以V2學生套件替換template-owned檔案，並手動merge `thesis.tex`的本地修改。保留現有helper calls；V1 adapter會自動載入。每完成一小步便建置，最後逐項比較保存的1.x PDF。

**English**

Use this path for an NCKU thesis already in progress. Preserve `conf/conf.tex`, content, figures, bibliography data, and local certificate files; replace template-owned files with the V2 student package and manually merge local changes to `thesis.tex`. Keep existing helper calls; the V1 adapter loads automatically. Build after each small step and compare the result with the saved 1.x PDF.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```

No helper rename is required / 不需要重新命名helper。

## Native V2路徑 / Native V2 path

**繁體中文**

此路徑適用於新論文或長期維護的institutional fork。由V2學生套件開始，複製論文內容、圖片、書目及證明書，再於`conf/conf.tex`重新輸入或有意識地merge metadata。成大專案保留預設`ncku` profile；其他學校依照[`thesis/template/style/Customization.md`](../thesis/template/style/Customization.md)建立並選擇一個profile。2.x期間可繼續使用相容helpers，不需要一次改寫全部source。

**English**

Use this path for a new thesis or a maintained institutional fork. Start from the V2 student package, copy content, figures, bibliography data, and certificate files, then re-enter or deliberately merge metadata in `conf/conf.tex`. Keep the default `ncku` profile for NCKU work; another institution creates and selects exactly one profile by following [`thesis/template/style/Customization.md`](../thesis/template/style/Customization.md). Compatibility helpers may remain throughout 2.x; a source-wide rewrite is not required.

Build after every migration step / 每一個升級步驟後都要建置。

## 穩定專案邊界 / Stable project boundaries

**繁體中文**

2.x保持下列學生路徑穩定。`conf/`只存放學生論文資料。學校geometry、文字、catalogue、日期規則及assets放在`template/style/`；V2不新增`conf/style.tex`。文件語言、學校profile、封面語言、學位及內容模式是獨立決定。

**English**

The following student-facing paths remain stable in 2.x. `conf/` stores student thesis data only. Institution geometry, wording, catalogues, date rules, and assets remain under `template/style/`; V2 does not introduce `conf/style.tex`. Documentation language, institution profile, cover language, degree, and content mode are independent decisions.

```text
thesis.tex
conf/conf.tex
context/
example/
template/
```

| Axis / 維度 | Choices / 選項 |
| --- | --- |
| Institution / 學校 | `ncku`, `custom`, or another maintained profile |
| Cover language / 封面語言 | `\DisplayCoverInChi`, `\DisplayCoverInEng` |
| Degree / 學位 | `\MasterDegree`, `\PhdDegree` |
| Content / 內容 | own context or `\ExampleMode` teaching example |

## Public helper相容性 / Public helper compatibility

**繁體中文**

完整Git repository的`tests/v1-public-api.json`記錄597個runtime-visible 1.x LaTeX/xparse commands/environments及65個literal `\def`-style declarations；其名稱及完整argument shape在2.x均保留。另有22個declarations只存在於runtime-dead LaTeX `comment` environments，並由獨立audit記錄；它們不是被移除的public API。Native V2 internals可將舊helper委派到profile hooks，但相容層只保留正確contract，不重現已驗證的defect。

**English**

The full Git repository's `tests/v1-public-api.json` records 597 runtime-visible 1.x LaTeX/xparse commands/environments plus 65 literal `\def`-style declarations. Their names and complete argument shapes remain available throughout 2.x. A separate audit records 22 declarations found only inside runtime-dead LaTeX `comment` environments; they are not removed public APIs. Native V2 internals may delegate old helpers to profile hooks, but compatibility preserves correct contracts rather than verified defects.

Maintainer-only check / 僅完整儲存庫可用：

```bash
python3 scripts/test/check-v1-api.py
```

The checker and manifest are intentionally absent from the student ZIP.

## Byte-identical V1專案gate / Byte-identical V1 project gate

**繁體中文**

`tests/v1-project-migration.json`將18個student-owned files、合共296,726 bytes，pin至immutable release `v1.8.2.260715154703`。範圍包括`thesis.tex`、`conf/conf.tex`、學生內容、書目資料及口試證明assets。Runtime evidence分為兩條：unchanged entry/configuration經V2 adapter、base及NCKU profile建置271頁A4 canonical result；StudentMode fixture則從`.fls`及`.blg`確認active content及三個bibliography databases。

未被該V1 configuration載入的alternate abstracts及external certificate PDFs只作source pin，不會被誤稱為runtime-loaded。

**English**

`tests/v1-project-migration.json` pins 18 student-owned files totalling 296,726 bytes to immutable release `v1.8.2.260715154703`. It covers `thesis.tex`, `conf/conf.tex`, student content, bibliography data, and oral-certificate assets. Runtime evidence is split: the unchanged entry/configuration builds a 271-page A4 canonical result through the V2 adapter, base contract, and NCKU profile; the StudentMode fixture uses `.fls` and `.blg` records to prove active content and all three bibliography databases.

Alternate abstracts and external certificate PDFs disabled by that V1 configuration remain source-pinned but are not falsely claimed as runtime-loaded.

```text
tests/v1-project-migration.json
scripts/test/check-v1-project-migration.py
```

## V1 adapter佈局 / V1 adapter layout

**繁體中文**

V1 adapter即使在custom profile亦會載入，使舊NCKU college／department presets保持defined。`template/compat/deprecated.tex`保存23個已於1.x停用的commands；它們仍使用原名、原diagnostic及`\stop`，避免變成undefined-control-sequence。有效的一參數`\RefTo{label}`仍然可用，歷史comment-only零參數tombstone則不屬public API。Custom profile不會載入NCKU geometry、日期policy或浮水印asset；只保留source-level compatibility cost。

**English**

The V1 adapter loads even for a custom profile so old NCKU college/department presets remain defined. `template/compat/deprecated.tex` preserves 23 commands already unsupported during 1.x with the same names, diagnostics, and `\stop` behavior instead of undefined-control-sequence failures. The active one-argument `\RefTo{label}` remains available; its historical comment-only zero-argument tombstone is not public API. A custom profile does not load NCKU geometry, date policy, or watermark assets; only the intentional source-level compatibility cost remains.

```text
template/compat/v1.tex
  template/command/cmd-college.tex      compatibility wrapper
  template/command/cmd-department.tex   compatibility wrapper
  template/compat/deprecated.tex        23 deprecated-command tombstones
  template/style/ncku/college.tex       NCKU-owned data
  template/style/ncku/department.tex    NCKU-owned data
```

## 已修正行為 / Corrected behaviors

**繁體中文**

下表是normative migration contract；每一個observable helper correction都必須同步更新中英文說明。相容性保留public API，不會保留已驗證的錯誤。

**English**

This table is the normative migration contract and must be updated in both languages for every observable helper correction. Compatibility preserves public APIs, not verified defects.

| 1.x behavior / 1.x行為 | 2.x behavior / 2.x行為 | User action / 使用者動作 |
| --- | --- | --- |
| `\StartSubSubSection{title}{label}`在預設隱藏number時寫出空reference。<br><br>It wrote an empty reference when the default heading hid its number. | 標題仍不顯示number，但label保存如`1.1.1.1`的穩定階層值，並拒絕empty-link warnings。<br><br>The heading remains visually unnumbered while the label records a stable hierarchy such as `1.1.1.1`; empty-link warnings are rejected. | 無需改source；既有reference會恢復可用。<br><br>No source change; existing references become usable. |
| `\GetOralYearInTaiwanYear`會經thesis state重算並可能改動thesis year。<br><br>The oral-year getter could mutate thesis-year state. | Getter只讀oral state；`\SetOralEngDate`同步oral Taiwan-year state。<br><br>The getter reads oral state without mutating thesis state; `\SetOralEngDate` keeps oral Taiwan-year state synchronized. | 無。 / None. |
| `\SetDeptName{chi}{short}{full}`第二參數被丟棄。<br><br>The English abbreviation was discarded. | Short name保存在`\GetDeptEngShortName`；`\GetDeptEngName`仍回傳full name。<br><br>The abbreviation is available through `\GetDeptEngShortName`; the full-name getter is unchanged. | 可選擇使用新getter。<br><br>Optionally adopt the new getter. |
| `\SetDeptDPS`輸出`Departmment of Photonics`。<br><br>The catalogue contained a spelling error. | 修正為`Department of Photonics`。<br><br>The catalogue value is corrected. | 重新build。 / Rebuild. |
| English oral certificate混用oral day及cover month/year。<br><br>The English certificate mixed oral day with cover month/year. | 全部使用oral day/month/year。<br><br>English oral output consistently uses oral metadata. | Distinct-date non-NCKU projects automatically receive the correct oral date. / 非NCKU專案自動取得正確日期。 |
| Doctoral English cover從oral metadata借day，雖然`\SetCoverDate`只有year/month。<br><br>The Doctoral English cover borrowed an oral day not owned by `\SetCoverDate`. | Master/Doctoral date tokens由profile擁有；generic/custom只render cover-owned month/year，NCKU明確保留既有oral-day policy。<br><br>Date tokens are profile-owned; generic/custom uses cover-owned month/year while NCKU explicitly retains its oral-day policy. | NCKU無需動作；其他profile可自訂date tokens。<br><br>No NCKU action; other profiles may customize date tokens. |
| `\SetCommitteeSize`對所有degree接受generic 2–9，與NCKU教學文字不一致。<br><br>Every degree accepted the generic 2–9 range. | Policy由profile擁有；NCKU Master為3–5、Doctoral為5–9，neutral/custom保留2–9。<br><br>Profile policy clamps NCKU Master to 3–5 and Doctoral to 5–9; neutral/custom remains 2–9. | 先呼叫`\MasterDegree`／`\PhdDegree`再設定size。<br><br>Select degree before committee size. |
| Theorem `label` option以錯誤braces傳遞，label key出現在正文且無label；mutable title亦令`\nameref`變空。<br><br>The theorem label option leaked into visible text and mutable title metadata became blank. | 保留optional signature，正確寫label，並在`\label`前freeze title；`\ref`及`\nameref`均可用。<br><br>The optional signature is preserved, labels are written correctly, and title metadata is frozen. | 無需改source，重新build。<br><br>No source change; rebuild. |
| Figure/subfigure/table caption把mutable temporary寫入nameref metadata。<br><br>Captions wrote mutable temporary tokens to metadata. | 所有caption wrappers在寫label前freeze rendered caption；`\ref`number不變，`\nameref`回傳literal caption。<br><br>Rendered captions are frozen before labels; reference numbers remain unchanged. | 重建足夠次數更新auxiliary files。<br><br>Rebuild until auxiliary files converge. |
| Numbering getters保留shared scratch aliases，後續setup可改寫先前getter；repeated appendix equation setup亦會append。<br><br>Reusable scratch aliases let later setup rewrite earlier numbering and repeated setup appended state. | Prefix、separator及counter names被freeze，counter values保持dynamic；general/appendix setup可重複且idempotent。<br><br>Configuration is frozen while counter values remain dynamic; repeated setup is idempotent. | Custom numbering users should rebuild generated labels/lists. / 自訂編號使用者應重新build。 |
| Forward/multi-hop theorem `FollowCounter`受initializer order影響，cycles可recursive overflow。<br><br>Counter chains depended on initializer order and cycles could overflow recursively. | Chains遞迴resolve至frozen terminal；numbered／optional／starred syntax一致，cycles以deterministic package error停止。<br><br>Chains resolve to frozen terminals and cycles stop with a deterministic package error. | 無需改source，重新build。<br><br>No source change; rebuild. |

## 日期升級 / Date migration

**繁體中文**

Public setters不變。V2將raw input與profile-resolved display policy分開：`\GetRequestedCoverYear`／`\GetRequestedCoverMonth`回傳`\SetCoverDate`原始值，`\GetThesisYear`／`\GetThesisMonth`回傳profile解決後的封面值，oral getters保持獨立。NCKU profile仍以oral date作封面authoritative date，因此NCKU輸出不變。Non-NCKU profile預設使用explicit cover year/month，不借用oral day。

**English**

Public setters are unchanged. V2 separates raw input from profile-resolved display policy: `\GetRequestedCoverYear` / `\GetRequestedCoverMonth` expose raw `\SetCoverDate` input, `\GetThesisYear` / `\GetThesisMonth` expose profile-resolved cover values, and oral getters remain independent. NCKU still makes the oral date authoritative for the cover, preserving NCKU output. A non-NCKU profile uses explicit cover year/month and does not borrow an oral day.

```tex
\SetOralDate{2023}{12}{31}
\SetCoverDate{2024}{7}
```

Institutional forks override `\ApplyOralDatePolicy`, `\ApplyCoverDatePolicy`, and profile-owned Master/Doctoral date tokens—not the public setters.

## 非NCKU Style Port升級 / Migrate a non-NCKU style port

**繁體中文**

1. 以`template/style/custom/`作新profile base；不要先copy/load NCKU再撤銷policy。
2. 將舊custom file內的institution geometry、校名、watermark及date behavior移到`<profile>/<profile>.tex`。
3. 恰好呼叫一次`\RegisterTemplateStyle{<profile>}`。
4. 透過`template/style/style.tex`的`\TemplateStyleName`選擇profile。
5. 將舊`\SetOralDate`／`\SetCoverDate` overrides改成policy hooks。
6. 只有institution有degree-specific committee ranges時才override `\ApplyCommitteeSizePolicy`；保持`\SetCommitteeSize`不變。
7. 將cover/oral wording及English cover-date formats移到profile token setters。
8. 使用`\SetCollName`／`\SetDeptName`，或在profile內維護institution catalogue。
9. 以故意不同的oral／cover dates建置cover及certificate，證明policy separation。
10. 確認`.fls`沒有載入非預期institution asset。

**English**

1. Start from `template/style/custom/`; do not copy/load NCKU merely to undo it.
2. Move institution geometry, names, watermark, and date behavior from the old custom file into `<profile>/<profile>.tex`.
3. Call exactly one `\RegisterTemplateStyle{<profile>}`.
4. Select the profile with `\TemplateStyleName` in `template/style/style.tex`.
5. Replace old `\SetOralDate` / `\SetCoverDate` overrides with policy hooks.
6. Override `\ApplyCommitteeSizePolicy` only for degree-specific institution ranges; keep `\SetCommitteeSize` unchanged.
7. Move cover/oral wording and English cover-date formats to profile token setters.
8. Use `\SetCollName` / `\SetDeptName`, or maintain an institution catalogue inside the profile.
9. Build cover/certificate cases with deliberately different oral and cover dates to prove policy separation.
10. Confirm through `.fls` that no unintended institution asset is loaded.

Detailed guide / 詳細指南：[`thesis/template/style/Customization.md`](../thesis/template/style/Customization.md)

The executable `tests/custom-style.tex` fixture exists only in the full repository and is intentionally absent from the student ZIP.

## Portable驗證 / Portable verification

**繁體中文**

在解壓student ZIP或任何包含`thesis.tex`的migrated project root執行下列commands。檢查A4及預期頁數、學校／學院／系所／題目／作者／指導教授文字、cover/oral dates、目錄及references、書目收斂、Draft／watermark狀態，以及cover、front matter、正文及最後頁rendering。

**English**

Run these commands from an extracted student ZIP or any migrated project root containing `thesis.tex`. Verify A4 and expected pages; university, college, department, title, author, and advisor text; cover/oral dates; contents and references; bibliography convergence; Draft/watermark state; and representative cover, front-matter, body, and final pages.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

Use the saved 1.x PDF as the comparison reference / 以保存的1.x PDF作比較reference。

## Maintainer驗證 / Maintainer verification

**繁體中文**

下列commands需要完整Git checkout並從repository root執行，student ZIP不提供。Acceptance evidence包括597/597 runtime-visible declarations、65/65 literal-def declarations、22個dead-comment audit entries、18個byte-identical student inputs、exact-tree student archive、direct build、neutral/custom six-page fixture，以及canonical 271-page NCKU output identity。

**English**

The following commands require the complete Git checkout and run from the repository root; they are unavailable in the student ZIP. Acceptance evidence includes 597/597 runtime-visible declarations, 65/65 literal-def declarations, 22 dead-comment audit entries, 18 byte-identical student inputs, exact-tree student archive, direct build, the six-page neutral/custom fixture, and canonical 271-page NCKU output identity.

```bash
just _test-custom-style
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
just ci
git diff --check
```

Current canonical contract / 現行canonical contract：

```text
pages:                 271
paper:                 A4
normalized bbox words: 40823
text:                  identical
fonts:                 identical
raster:                271/271 identical at 120 DPI
```

## 回復與故障處理 / Recovery and troubleshooting

**繁體中文**

如升級後輸出不符預期，停止繼續修改，不要刪除舊專案或baseline PDF。確認改動屬student data、template-owned files或本地`thesis.tex`merge；回到上一個可建置commit，然後一次重新套用一個變更。切換BibTeX style或遇到stale intermediates時，以`latexmk -C thesis.tex`清除後再build。不要修改compatibility manifests、降低expected counts或停用tests來隱藏差異。

**English**

If migrated output differs unexpectedly, stop adding changes and retain the old project and baseline PDF. Classify the change as student data, template-owned files, or a local `thesis.tex` merge; return to the last buildable commit and reapply one change at a time. When changing BibTeX style or encountering stale intermediates, run `latexmk -C thesis.tex` before rebuilding. Do not edit compatibility manifests, lower expected counts, or disable tests to hide a difference.

A verified behavior correction belongs in the normative table above; an undocumented output change is a blocker.
