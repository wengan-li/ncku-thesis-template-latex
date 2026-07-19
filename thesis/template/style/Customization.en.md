<!-- doc-pair: style-customization; lang: en; topics: architecture-boundary,load-order-and-customization-consequences,create-a-new-profile,required-profile-contract,institution-names-and-watermark,generic-and-ncku-department-apis,illustrative-ntu-wiring,cover-wording-and-date-tokens,certificate-wording-and-semantic-degree,committee-size-policy,date-policy-and-raw-resolved-state,2-x-compatibility-adapter,verification,troubleshooting -->

[繁體中文](Customization.md) | [English](Customization.en.md)

# Institution style customization

The template separates reusable thesis helpers from institution policy so students from other institutions can retain template capabilities while creating their own institution format. Documentation language, cover language, and institution profile are independent decisions.

## Architecture boundary

Student thesis data remains in `conf/conf.tex`. Institution geometry, date rules, names, cover/certificate wording, department catalogues, and watermark policy belong under `template/style/<profile>/`; do not create `conf/style.tex`. `template/style/style.tex` loads exactly one profile. The template does not load NCKU first and then override it with a custom file.

```text
template/command/        reusable public helpers, state, and renderer mechanisms
template/compat/v1.tex   1.x compatibility adapter throughout 2.x
template/cover/          shared cover renderer
template/oral/           shared certificate renderer
template/style/base/     profile contract and wording tokens
template/style/ncku/     NCKU data, geometry, date policy, and watermark asset
template/style/custom/   directly buildable other-institution skeleton
```

## Load order and customization consequences

`template/configure.tex` uses the following fixed order. This is a behavioral contract, not only a file-organization choice:

```text
template/configure.tex
1. template/command/command.tex
   - generic public setters, state, and renderer mechanisms
   - template/compat/v1.tex -> generic/deprecated adapters only
2. template/style/style.tex
   - template/style/base/base.tex
   - exactly one selected institution profile
     - ncku/ncku.tex -> NCKU college/department catalogue and policy
     - custom/custom.tex -> neutral policy with no NCKU catalogue
3. \TemplateConfigurationFile (default: ./conf/conf)
   - student metadata selects one profile-owned catalogue entry
4. \FillInPDFData and remaining metadata/render initialization
```

Generic commands load first so a profile can call the portable setters and register its policy. The selected profile loads before student configuration so `conf/conf.tex` can call that profile's catalogue commands; an unchanged NCKU configuration can therefore still call `\SetDeptCSIE`. The NCKU catalogue must not load from `compat/v1.tex` before profile selection, because that would leak NCKU institution data into `custom`.

The profile **defines** a reusable catalogue; student configuration **selects** one entry. Do not hard-code one student's department in the profile. A profile for another institution replaces the original NCKU `\SetDept...` call in its own `conf/conf.tex` with generic `\SetDeptName` or an institution-prefixed command. If the NCKU call remains, the custom build fails early with an undefined command rather than silently producing data for the wrong institution.

`\TemplateConfigurationFile` still defaults to `./conf/conf`. Only full-repository custom fixtures override that path with an isolated generic test configuration, preserving the byte-pinned V1 `conf/conf.tex`. Do not reorder configuration before the profile, and do not move the NCKU catalogue back into the generic command or compatibility layer. `\FillInPDFData` and later initialization remain after student configuration so they consume the resolved metadata.

## Create a new profile

The following example uses `UnivAbc`. Copy the neutral `custom` skeleton, rename the profile file, register the same name, and select it through `\TemplateStyleName`. Profile name and path casing must match exactly.

```bash
cp -R template/style/custom template/style/UnivAbc
mv template/style/UnivAbc/custom.tex template/style/UnivAbc/UnivAbc.tex
```

In `UnivAbc.tex`:

```tex
\RegisterTemplateStyle{UnivAbc}
```

In an institutional fork's `template/style/style.tex`:

```tex
\providecommand{\TemplateStyleName}{UnivAbc}
```

For a focused test, define the profile before `\input{./template/configure}`:

```tex
\def\TemplateStyleName{UnivAbc}
```

Modify institution geometry, names, wording tokens, date policy, and watermark style in `UnivAbc.tex`. Keep student metadata in `conf/conf.tex`.

## Required profile contract

Every profile must call `\RegisterTemplateStyle{<name>}` exactly once, set body geometry, define cover-page geometry enable/disable hooks, set institution names and cover/oral tokens, choose watermark behavior explicitly, and override policy hooks only when institution rules differ. Do not override public metadata setters.

```tex
\geometry{a4paper,top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,nohead}

\newcommand{\EnableCoverPageStyle}{%
  \newgeometry{top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,nohead,nofoot}%
}
\newcommand{\DisableCoverPageStyle}{\restoregeometry}
```

Build a minimal profile before adding institution-specific refinements. A missing profile or registration-name mismatch must fail rather than silently falling back to NCKU.

## Institution names and watermark

Use generic setters for Chinese and English institution, college, and department names. Keep watermark styles empty when no redistributable institution asset is available. `\SetWatermaskFigureStyle` / `\SetWatermaskTextStyle` define styles; `\UseWatermarkFigureStyle` / `\UseWatermarkTextStyle` enable them. Follow the institution's current submission rules and do not add a watermark merely because an API exists.

```tex
\SetUniversityName{範例大學}{Example University}
\SetCollName{範例學院}{Example College}
\SetDeptName{測試學系}{TEST}{Department of Testing}

% Safe neutral defaults / 安全neutral defaults
\SetWatermaskFigureStyle{}
\SetWatermaskTextStyle{}
```

The second `\SetDeptName` argument is the English abbreviation returned by `\GetDeptEngShortName`; the third is the full name returned by `\GetDeptEngName`.

## Generic and NCKU department APIs

The portable contract is `\SetUniversityName{Chinese}{English}`, `\SetCollName{Chinese}{English}`, and `\SetDeptName{Chinese}{English abbreviation}{English full name}`. Their getters are `\GetUniversityChiName` / `\GetUniversityEngName`, `\GetCollChiName` / `\GetCollEngName`, and `\GetDeptChiName` / `\GetDeptEngShortName` / `\GetDeptEngName`.

The template also preserves 9 NCKU college presets and 110 NCKU department presets; the department slot covers departments, graduate institutes, degree programs, and centers. A shortcut such as `\SetDeptCSIE` writes department values and calls one NCKU college preset. See the source-checked [`ncku/README.en.md`](ncku/README.en.md) catalogue. Only the `ncku` profile loads these commands; `custom` does not define them. A reusable new catalogue uses an institution prefix such as `\SetNTUDept...` instead of reusing NCKU `\SetDept...` names.

The same abbreviation does not imply the same data. The current NCKU `\SetDeptCSIE` source stores `資訊工程研究所` and `Institute of Computer Science and Information Engineering`; the NTU example below uses `資訊工程學系` and `Department of Computer Science and Information Engineering`. A shared `CSIE` abbreviation therefore does not make the preset portable.

## Illustrative NTU wiring (not a complete NTU profile)

The following demonstrates generic API wiring and command names only; it is **not a submission-ready NTU format**. This repository currently has no NTU profile. The official NTU [Chinese thesis/dissertation format guide](https://www.lib.ntu.edu.tw/doc/cl/THESISSAMPLE.pdf), [English format guide](https://www.lib.ntu.edu.tw/doc/CL/thesissample_en.pdf), and [NTU CSIE page](https://www.csie.ntu.edu.tw/en/AboutUs), checked on 2026-07-19, show that a real port must still implement cover/spine, title page, approval certificate, body margins, fonts/spacing, dates, and additional college/department rules. Replacing only university, college, and department names does not prove compliance.

An NTU fork can copy `custom` to `template/style/ntu/ntu.tex`, change the registration and `TemplateStyleName` to `ntu`, and then replace every skeleton policy with sourced NTU rules. Department shortcuts use an NTU prefix so they cannot collide with the retained NCKU namespace:

```tex
% template/style/ntu/ntu.tex
% Illustrative API wiring only. This is not a complete NTU profile.
\SetUniversityName{國立臺灣大學}{National Taiwan University}
\newcommand{\SetNTUDeptCSIE}{%
  \SetDeptName{資訊工程學系}{CSIE}{Department of Computer Science and Information Engineering}%
  \SetCollName{電機資訊學院}{College of Electrical Engineering and Computer Science}%
}

% conf/conf.tex: replace the existing NCKU department selection.
\SetNTUDeptCSIE
```

The profile defines the reusable catalogue; each student selects a department in `conf/conf.tex`. Do not hard-code one department in the profile or retain the original NCKU `\SetDept...` selection. After wiring names, verify body/cover geometry, spine, Master/Doctoral wording, oral certificate, Gregorian/Taiwan-year display, watermark/DOI processing, and asset redistribution rights. Each institution difference belongs in the `ntu` profile, not the shared renderer.

## Cover wording and date tokens

The shared renderer obtains student/advisor labels, prefixes/suffixes, and Master/Doctoral English date formats from profile token setters. `\SetCoverDate{year}{month}` owns no day, so a neutral Doctoral cover must not borrow one from independent oral metadata. If institution policy requires the oral day, the profile must explicitly include `\GetOralEngDay` in its Doctoral date token.

```tex
\SetCoverStudentChiBothText{學生}
\SetCoverStudentChiText{研究生}
\SetCoverStudentEngText{Student}
\SetCoverAdvisorChiText{指導老師}
\SetCoverAdvisorEngText{Advisor}
\SetCoverCoAdvisorChiText{共同指導}
\SetCoverCoAdvisorEngText{Co-Advisor}
\SetCoverAdvisorChiSuffix{博士}
\SetCoverAdvisorEngPrefix{Dr.}
\SetCoverDateChiPrefix{西元}
\SetCoverMasterDateEng{\GetThesisMonthInEng \thinspace \GetThesisYear}
\SetCoverDoctoralDateEng{\GetThesisMonthInEng \thinspace \GetThesisYear}
```

Use explicit `\space` where a control-word getter meets following text and the old contract included a visible space.

## Certificate wording and semantic degree

The profile provides location, approval, committee, advisor, chair, and Master/Doctoral submission wording. The English certificate renderer selects its branch from numeric `\GetFlagDegreeType`, not customizable display degree text. A profile may therefore rename degrees without selecting the wrong branch. Even if only an English certificate is currently used, define the complete bilingual contract to avoid blank labels after a later language switch.

```tex
\SetInstitutionLocationEng{Example City, Example Country}
\SetOralApprovalChiText{本論文業經審查及口試合格特此證明}
\SetOralApprovedByEngText{Approved by}
\SetOralCommitteeChiText{論文考試委員}
\SetOralAdvisorChiText{指導教授}
\SetOralChairChiText{系(所)主管}
\SetOralChairEngText{Chair}
\SetOralDateChiPrefix{西元}
\SetOralAuthorByEngText{prepared by}
\SetOralMasterSubmissionEngText{Example master's submission in}
\SetOralDoctoralSubmissionEngText{Example doctoral submission in}
```

Template-generated certificates are demonstrations/regression outputs, not official institution documents.

## Committee-size policy

The generic renderer supports 2–9 signature fields and neutral/custom keeps that range by default. The public `\SetCommitteeSize{n}` signature remains unchanged. If an institution has degree-specific limits, override only `\ApplyCommitteeSizePolicy{n}` and branch on semantic `\GetFlagDegreeType`, never display text.

NCKU clamps Master requests to 3–5 and Doctoral requests to 5–9. Users select the degree before committee size. Another profile needs no hook override when it has no degree-specific rule.

Keep renderer capacity and institution policy separate.

## Date policy and raw/resolved state

Public commands remain `\SetOralDate{year}{month}{day}` and `\SetCoverDate{year}{month}`. Generic policy keeps them as independent metadata and uses Gregorian years in Chinese renderers. NCKU hooks make the oral date authoritative for the cover and select Taiwan-year display. Students from another institution with the same rule override policy hooks and display getters, not public setters.

`\GetRequestedCoverYear` / `\GetRequestedCoverMonth` expose raw user input; `\GetThesisYear` / `\GetThesisMonth` expose profile-resolved display values.

```tex
\renewcommand{\ApplyOralDatePolicy}[3]{%
  \SetThesisTaiwanYear{#1}%
  \renewcommand{\ThesisYear}{#1}%
  \renewcommand{\ThesisMonth}{#2}%
}
\renewcommand{\ApplyCoverDatePolicy}[2]{}
```

If Taiwan-year display is required, explicitly override its policy/display getters in the profile. Do not leave Taiwan-calendar conversion inside generic setters.

## 2.x compatibility adapter

`template/compat/v1.tex` loads generic/deprecated adapters throughout 2.x. Only the `ncku` profile loads NCKU college/department presets; an unchanged 1.x NCKU project still selects that default profile and retains its commands. The old `template/command/cmd-college.tex` and `cmd-department.tex` paths remain dormant direct-path compatibility wrappers and do not enter a custom runtime graph automatically. `template/compat/deprecated.tex` preserves 23 commands already unsupported during 1.x with the same names, diagnostics, and `\stop`. The valid one-argument `\RefTo{label}` remains active and is not replaced by a historical comment-only tombstone.

A custom profile loads only the generic institution metadata contract. It does not define or load NCKU presets, geometry, date policy, or watermark assets.

Compatibility preserves correct contracts, not verified defects.

## Verification

Run direct XeLaTeX/latexmk from the project root containing `thesis.tex`:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
```

Confirm that the PDF is A4, then check profile registration, institution and department names, dates, committee ranges, Master/Doctoral branches, and Chinese/English output. A custom profile must not show NCKU wording or watermarks. Finally, confirm converged references and inspect the cover and certificate pages for missing, clipped, or overlapping content.

## Troubleshooting

For `Template style file ... was not found`, check directory, filename, and `\TemplateStyleName` casing. For `did not register itself`, ensure the profile file calls exactly one matching `\RegisterTemplateStyle`. If custom output shows NCKU wording or assets, check for a direct NCKU-profile input, copied NCKU policy left in the new profile, or institution values hard-coded into a generic renderer.
