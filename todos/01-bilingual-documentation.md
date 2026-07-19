---
id: "01"
title: Implement bilingual documentation for Traditional Chinese and English readers
status: planning
requirement: ../docs/requirements/02-bilingual-documentation.md
owner: Leon Li
created: 2026-07-19
---

# Bilingual documentation implementation plan

## Planning-only checkpoint

This file is the requested detailed todo. Creating this requirement/todo pair and
repairing their index backlinks is the complete scope of the current checkpoint.
Do **not** begin translation, rewrite user documentation, alter source, push,
open a PR, merge, tag, publish a release, or update Overleaf until Leon reviews
this plan and explicitly authorizes implementation.

Current local planning base:

```text
branch: feat/docs-consolidation
parent commit: b17543305565f8d2a074e075e9a2ec2ee03aae27
upstream: none
remote branch: absent
```

## Owner-confirmed direction

- Write the plan before implementation and make it as detailed as practical.
- Serve Taiwan Traditional-Chinese readers and English/international readers.
- Use a hybrid model rather than mechanically duplicating every internal file.
- Give complete bilingual instructions to public/student journeys.
- Give maintainer feature records a Traditional-Chinese summary and an English
  technical body.
- Keep commands, paths, LaTeX macros, logs, identifiers, and release asset names
  in their exact source form.
- Keep institution selection separate from documentation/cover language.
- Continue the local-only boundary unless Leon gives a later publication order.

## Intent

Deliver one coherent documentation system in which a reader can choose a
language without choosing the wrong institution profile, degree type, or content
mode. The smallest useful implementation slice must first make the packaged
student journey independently complete in both languages, then expand the same
policy to migration, public routing, customization, and maintainer summaries.

## Expectations

### Done means

- The language model and terminology are written into current documentation
  policy and repo-local agent guidance.
- Root `README.md`, packaged `thesis/README.md`, the packaged configuration guide,
  migration guide, and customization guide support complete Traditional-Chinese
  and English journeys.
- `docs/README.md` routes both languages and all audiences.
- Current maintainer feature records include concise, accurate
  Traditional-Chinese executive summaries without duplicating the English
  evidence body.
- V2/current changelog content has a stable bilingual format; historical 1.x
  entries are preserved without unnecessary retro-translation.
- The exact `thesis/conf/conf.tex` v1.8.2 hash and all 18 migration inputs remain
  unchanged.
- Mechanical checks enforce structure and terminology without pretending to
  prove translation quality.
- Human semantic review verifies commands, warnings, and policy parity.
- Exact staged-tree CI, release packaging, student ZIP read-back, direct build,
  and canonical output identity pass.
- Requirement and todo are removed only after durable bilingual policy and
  shipped behavior are consolidated into current docs.

### Done does not mean

- every internal comment is translated;
- every historical commit or 1.x changelog entry is translated;
- every page of the 271-page teaching example is translated;
- deprecated runtime diagnostics are silently changed;
- a new release or Overleaf revision is published automatically.

## Evidence baseline

The current post-consolidation documentation is intentionally compact but has an
inconsistent language distribution:

```text
README.md                              CJK-heavy/mixed public landing
thesis/README.md                       almost entirely English
thesis/conf/conf.tex                   student comments mainly Chinese
docs/README.md                         English
docs/v1-to-v2-migration.md             English
docs/features/v2-modernization.md      English
docs/features/validation-and-performance.md  English
docs/features/release-and-distribution.md    English
```

Measured 2026-07-19 character distribution before bilingual implementation:

```text
README.md                              CJK share 0.433
thesis/README.md                       CJK share 0.025
docs/README.md                         CJK share 0.000
docs/v1-to-v2-migration.md             CJK share approximately 0.000
docs/features/v2-modernization.md      CJK share 0.000
docs/features/validation-and-performance.md  CJK share 0.000
docs/features/release-and-distribution.md    CJK share approximately 0.000
```

Character ratios are context only, not acceptance targets. A document can be
semantically complete without a 50/50 character ratio.

## Non-negotiable compatibility constraint

`tests/v1-project-migration.json` pins `thesis/conf/conf.tex` byte-for-byte:

```text
size:   24780
sha256: ca7232190705e4dbc6ff1f6fe2613c0ce1cfdb6dcd6486ee15df6a07b195b4e0
source: v1.8.2.260715154703
commit: 2c9557a74983023bba7a8f0cf233e1eb812edec7
```

Therefore:

- do not translate or edit comments in `thesis/conf/conf.tex` during 2.x;
- add `thesis/conf/README.md` as the bilingual field-by-field companion guide;
- link the companion from `thesis/README.md` and relevant public/migration docs;
- include it automatically in the exact `HEAD:thesis` student package;
- update package verification to assert that the guide exists and links resolve;
- keep `python3 scripts/test/check-v1-project-migration.py` passing unchanged.

Changing this boundary requires a separate owner-approved compatibility decision,
not a documentation convenience edit.

## Audience and decision matrix

| Reader | Institution | Preferred docs | Required journey |
| --- | --- | --- | --- |
| Taiwan NCKU student | `ncku` | Traditional Chinese | download, configure, build, submit |
| English-reading NCKU student | `ncku` | English | same journey, no Chinese dependency |
| Taiwan non-NCKU maintainer | `custom` or another profile | Traditional Chinese | profile creation and validation |
| English non-NCKU maintainer | `custom` or another profile | English | same profile journey |
| Existing 1.x user | unchanged first, then v2 | either | backup, replace template files, compare output |
| Repository maintainer | any | Chinese summary plus English body | architecture, tests, release, Overleaf |

Public docs must explicitly teach four independent axes:

```text
documentation language: Traditional Chinese | English
institution profile:    ncku | custom/other
cover language:         \DisplayCoverInChi | \DisplayCoverInEng
degree:                 \MasterDegree | \PhdDegree
content mode:            own context | \ExampleMode teaching example
```

## Scope

### Included surfaces

- `README.md`
- `thesis/README.md`
- new `thesis/conf/README.md`
- `docs/README.md`
- `docs/v1-to-v2-migration.md`
- `thesis/template/style/Customization.md`
- `docs/features/README.md`
- `docs/features/v2-modernization.md`
- `docs/features/validation-and-performance.md`
- `docs/features/release-and-distribution.md`
- current/future V2 section format in `CHANGELOG.md`
- `.agents/skills/documentation-management/SKILL.md`
- relevant `AGENTS.md` documentation policy
- package verifier and deterministic documentation checker where required
- `justfile` wiring only if a new checker is accepted

### Excluded surfaces

- byte-pinned `thesis/conf/conf.tex` and the other 17 pinned inputs;
- template macro implementations and public API signatures;
- runtime error messages and deprecated-command diagnostics;
- all 271 pages of `thesis/example/` teaching content;
- internal implementation comments with no student-facing role;
- immutable release/tag contents;
- current public Overleaf Gallery project;
- new release publishing or GitHub branch publication.

## Target content model

### Complete bilingual surfaces

Use complete adjacent Traditional-Chinese and English blocks for:

- root public overview and quick start;
- packaged student start/configure/build/preview/submission guide;
- packaged configuration companion;
- v1-to-v2 migration;
- non-NCKU customization;
- safety-critical Draft/watermark/certificate warnings.

Each topic has one shared command/link/code block after both prose blocks. Do not
copy the same command into two language-specific blocks.

### Bilingual router surfaces

`docs/README.md` and `docs/features/README.md` use bilingual headings, audience
labels, and short descriptions. They must route readers; they must not duplicate
the underlying records.

### Summary-plus-body surfaces

Each maintainer feature record begins with:

```markdown
## 繁體中文摘要

- five to ten durable, non-speculative bullets

## English technical record

...existing complete technical body...
```

Chinese summaries must include safety/release caveats but need not repeat every
run ID, hash, benchmark row, or command transcript.

### English-only surfaces

Internal agent/process details and source comments may remain English when they
are not part of a student or public user journey. The documentation-management
skill remains English but owns the bilingual policy and checks.

## Writing standard

### Traditional Chinese

Use formal Taiwan Traditional Chinese (`zh-Hant-TW`), not Cantonese chat prose,
Mainland Simplified Chinese, or sentence fragments assembled around unexplained
English nouns.

Target replacements include:

```text
呢個       -> 此／這個
只係       -> 僅／只
唔         -> 不
嘅         -> 的
喺         -> 在
production -> 正式發行／正式環境（according to context）
repository -> 儲存庫（first use may include repository）
```

Do not run blind global replacements. Search hits must be reviewed in context,
especially code, quotations, immutable names, URLs, and historical evidence.

### English

Use natural technical English rather than literal word-order translation. Keep
sentences direct, explain NCKU-specific policy at first use, and distinguish
observed historical acceptance from current official requirements.

### Product and tool casing

Use these exact forms:

```text
LaTeX
XeLaTeX
BibTeX
latexmk
SyncTeX
GitHub
Overleaf
NCKU
```

Ban new user-facing `LaTex`, `XeLatex`, and `Latex` spellings except inside an
immutable external title or quoted historical artifact.

### Project noun

Use `論文範本` in new Taiwan-facing prose and `thesis template` in English. Do not
silently rewrite immutable repository names, external titles, release asset names,
URLs, or quoted historical records. Where the existing public title retains a
legacy spelling for identity/SEO continuity, pair it with correct prose rather
than changing URLs.

### Preferred terminology

| English | Taiwan Traditional Chinese |
| --- | --- |
| thesis template | 論文範本 |
| student package | 學生套件 |
| production release | 正式發行版 |
| source code | 原始碼 |
| build / compile | 建置／編譯，按語境選擇 |
| compatibility adapter | 相容層 |
| maintainer | 維護者 |
| fixture | 測試案例（fixture）on first use |
| institution profile | 學校樣式設定檔（profile）on first use |
| release asset | 發行附件 |
| deprecated | 已棄用 |
| migration | 升級／遷移；student steps prefer 升級 |
| oral defense | 口試／學位考試，按NCKU context |
| defense certificate | 學位考試合格證明書 |
| watermark | 浮水印 |
| bibliography | 參考文獻／書目資料，按context |
| root document | 主文件 |

Add the approved glossary to the documentation policy so later edits do not
reintroduce mixed terminology.

### Section template for complete bilingual topics

````markdown
## 開始撰寫 / Start writing

**繁體中文**

開啟 `conf/conf.tex`，填寫論文資料。撰寫自己的論文時，請停用
`\ExampleMode`。

**English**

Open `conf/conf.tex` and enter your thesis information. Disable
`\ExampleMode` when writing your own thesis.

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
```
````

Rules:

- Chinese first on Taiwan/student surfaces; English follows immediately.
- Use bold language labels within a topic instead of multiplying table-of-content
  entries with repeated `###` headings.
- Keep code blocks, tables of commands, and links shared.
- If only one language changes semantically, update both before completing the
  slice.
- Do not hide either language in `<details>` blocks.
- Avoid side-by-side prose tables because they are difficult on mobile and create
  inaccessible long cells.

### Warning template

Safety/submission warnings use visually equal blocks:

```markdown
> **繁體中文：** 正式上傳前，請依當年度學校及系所規定確認PDF；不要因範本保留浮水印API而自行加入浮水印。
>
> **English:** Before final submission, verify the PDF against the current university and department rules. Do not add a watermark merely because the template retains a watermark API.
```

Neither language may soften official-policy, Draft, watermark, certificate, or
licensing caveats.

## File ownership and intended changes

| File | Role | Planned treatment |
| --- | --- | --- |
| `README.md` | Public landing | Shorten; full bilingual overview, setup matrix, download, build, warnings, routes |
| `thesis/README.md` | Offline student guide | Full paired bilingual rewrite; link config companion |
| `thesis/conf/README.md` | New offline config guide | Full paired bilingual field-by-field explanation; no macros redefined |
| `thesis/conf/conf.tex` | Byte-pinned config | Read-only; zero-byte-diff requirement |
| `docs/README.md` | Maintainer router | Bilingual audience/task index and language policy |
| `docs/v1-to-v2-migration.md` | User migration | Complete paired bilingual migration contract |
| `Customization.md` | Other institutions | Complete paired bilingual profile workflow |
| `docs/features/README.md` | Feature router | Bilingual labels and summaries only |
| `v2-modernization.md` | Technical record | Chinese executive summary plus existing English body |
| `validation-and-performance.md` | Evidence record | Chinese executive summary plus existing English body |
| `release-and-distribution.md` | Operations record | Chinese executive summary plus existing English body |
| `CHANGELOG.md` | Version history | Bilingual V2/current summary format; preserve historical 1.x text |
| documentation skill | Policy | Add language model, glossary, parity and lifecycle rules |
| `AGENTS.md` | Active instructions | Point docs work to bilingual policy; avoid duplicating full glossary |
| package verifier | Release contract | Assert packaged bilingual guides and public links |
| optional checker | Structural lint | Validate required blocks, casing, selected terms, and links |

## Work breakdown

### BIL-00 — Planning checkpoint (current slice)

**Purpose:** make Intent, constraints, sequencing, validation, and stop boundary
durable before implementation.

Tasks:

- [x] confirm current branch and local-only state;
- [x] inspect current language distribution;
- [x] inspect actual public selectors and profile boundary;
- [x] discover the byte-pinned `conf/conf.tex` constraint;
- [x] create requirement `02-bilingual-documentation.md`;
- [x] create this detailed todo;
- [x] repair `docs/README.md` and `docs/features/README.md` active-requirement links;
- [x] validate requirement/todo backlinks and Markdown links;
- [x] create a planning-only local commit;
- [x] stop and request owner review before BIL-01.

Acceptance:

- Planning commit contains no translation or behavior implementation.
- Requirement is `active`; todo is `planning`.
- Worktree is clean after local commit.
- No remote branch, upstream, push, PR, merge, tag, release, or Overleaf change.

### BIL-01 — Establish bilingual governance and deterministic structure

**Dependencies:** owner approves BIL-00 plan.

Files:

- `docs/README.md`
- `.agents/skills/documentation-management/SKILL.md`
- `AGENTS.md`
- optional `scripts/test/check-bilingual-docs.py`
- optional `justfile` recipe wiring

Tasks:

- [ ] add the independent language/institution/degree/content-mode model;
- [ ] add the complete-bilingual versus summary-plus-English-body rule;
- [ ] add the approved terminology table and product casing list;
- [ ] define which surfaces are package-facing and must work offline;
- [ ] define translation parity as a human semantic obligation;
- [ ] implement a deterministic checker for structure only;
- [ ] add checker to an existing `just check`/`just test` path only if it is fast,
      dependency-free, and does not duplicate another checker;
- [ ] document checker limitations explicitly.

Candidate mechanical checks:

- required language labels exist on complete bilingual surfaces;
- feature records contain `繁體中文摘要` and `English technical record`;
- targeted active docs contain no incorrect `LaTex`/`XeLatex` casing;
- targeted user prose contains no selected Cantonese-only tokens outside an
  allowlist;
- required relative links and local anchors resolve;
- package-facing docs link to the bilingual configuration guide;
- neither checker nor policy requires a meaningless 50/50 character ratio.

Acceptance:

- Checker runs with repository-provided Python only.
- Checker never claims that translations are semantically equivalent.
- Existing CI remains green before any content rewrite.
- Policy has one owner and is linked rather than copied across agent files.

### BIL-02 — Rewrite packaged student entry points

**Dependencies:** BIL-01 policy accepted and checker available or intentionally
deferred with rationale.

Files:

- `thesis/README.md`
- new `thesis/conf/README.md`
- `scripts/release/verify-student-archive.sh`
- public links that route directly to these files

Student README topics, each complete in both languages:

- [ ] package boundary and what is intentionally absent;
- [ ] disable `\ExampleMode` and select own context;
- [ ] configure metadata through `conf/conf.tex`;
- [ ] choose cover language independently of institution profile;
- [ ] choose degree;
- [ ] understand `ncku` versus custom institution profile;
- [ ] compatibility-first migration route;
- [ ] final build command;
- [ ] continuous preview command;
- [ ] Texmaker/TeXstudio root-document setup;
- [ ] cleanup command;
- [ ] Draft, text watermark, and institution watermark distinctions;
- [ ] official certificate and submission warnings;
- [ ] final pre-submission checklist;
- [ ] links to migration and customization docs;
- [ ] external-project disclaimer, if retained.

Configuration companion topics:

- [ ] explain that `conf.tex` remains byte-pinned and comments may be Chinese;
- [ ] map each user-editable section in file order;
- [ ] `\ExampleMode`;
- [ ] line stretch;
- [ ] cover language and people-name display;
- [ ] Chinese/English titles;
- [ ] Draft and watermark controls;
- [ ] degree;
- [ ] student name;
- [ ] oral and cover dates;
- [ ] department/institute;
- [ ] advisor names;
- [ ] certificate image/template choices;
- [ ] committee members;
- [ ] keywords and PDF metadata;
- [ ] abstracts, acknowledgments, references, and context selection where
      configured later in the file;
- [ ] common invalid combinations and which call wins when options repeat;
- [ ] link to customization rather than teaching non-NCKU policy inside `conf/`.

Package-verifier updates:

- [ ] assert `ncku-thesis-template-latex/conf/README.md` exists;
- [ ] assert packaged `README.md` links to it;
- [ ] retain exact-tree equality with tagged/committed `HEAD:thesis`;
- [ ] retain rejection of repository-only tooling;
- [ ] retain direct-build and migration-link checks.

Acceptance:

- A Chinese-only and an English-only reviewer can independently execute the
  student journey.
- `thesis/conf/conf.tex` remains exactly 24780 bytes with the pinned SHA-256.
- Student ZIP includes both guides directly under the expected package tree.
- Commands are shared and identical across language prose.

### BIL-03 — Rewrite the public root landing page

**Dependencies:** packaged student journey is stable, so root routes to real
content rather than promises.

Tasks:

- [ ] replace the mixed-language title with correct `LaTeX` branding and clear
  Traditional-Chinese/English naming;
- [ ] add a top language/navigation line;
- [ ] provide equal project overview and unofficial-community disclaimer;
- [ ] explain official rules and last-checked dates in both languages;
- [ ] present V2 release and Overleaf state without conflating them;
- [ ] add a concise independent setup matrix;
- [ ] route NCKU users and custom-profile maintainers separately from language;
- [ ] provide one shared download/build command block;
- [ ] preserve student package/examples package distinction;
- [ ] preserve submission, watermark, and certificate safety meaning;
- [ ] shorten or relocate long 2015/2018 historical narratives;
- [ ] preserve durable history in the owning release/operations record or Git
  history before removing duplicate root prose;
- [ ] retain external-template links with a bilingual non-endorsement disclaimer;
- [ ] keep license wording and NCKU watermark rights accurate.

Target root structure:

```text
Project title
Language/navigation
Overview / 簡介
Status and official-policy disclaimer
Quick start / 快速開始
Choose setup / 選擇設定
Download / 下載
Build / 編譯
Submission warnings / 提交注意事項
Documentation routes / 文件導覽
Alternatives / 其他方案
Changelog
License
```

Acceptance:

- Root README is a router and quick start, not a second maintainer runbook.
- Both languages contain the same current release and Overleaf caveat.
- No public paragraph mixes Cantonese grammar with unexplained English prose.
- Historical acceptance is never presented as current NCKU endorsement.

### BIL-04 — Make migration complete in both languages

**Dependencies:** language policy and student terminology are stable.

Files:

- `docs/v1-to-v2-migration.md`
- `thesis/README.md` migration excerpt/link
- root migration route

For every existing topic, provide paired semantics:

- [ ] production target and compatibility statement;
- [ ] backup/commit/archive prerequisites;
- [ ] user-owned versus template-owned boundaries;
- [ ] compatibility-first path for an in-progress NCKU thesis;
- [ ] native-v2 path for a new thesis or maintained fork;
- [ ] stable paths;
- [ ] public helper compatibility and audited declaration counts;
- [ ] unchanged v1.8.2 project gate;
- [ ] independent profile, cover-language, degree, and content decisions;
- [ ] correctness-change table;
- [ ] Draft, watermark, date, chapter, numbering, theorem, float, and certificate
      behavior notes;
- [ ] direct build and validation procedure;
- [ ] PDF comparison checklist;
- [ ] rollback/recovery path;
- [ ] known limits and links to technical evidence.

Translation rule for tables:

- keep macro names and old/new values in shared columns;
- use bilingual prose in the explanation column or adjacent language blocks;
- do not duplicate one large correctness table into two independently maintained
  copies unless Markdown readability proves impossible;
- verify every warning and default manually across languages.

Acceptance:

- Both reviewers can migrate without reading the other prose language.
- Commands, paths, counts, release target, and behavior corrections match exactly.
- Student README excerpt is shorter but does not contradict the full guide.
- No migration text promises a helper removal during 2.x.

### BIL-05 — Make non-NCKU customization complete in both languages

**Dependencies:** independent-axis terminology is stable.

Files:

- `thesis/template/style/Customization.md`
- root setup matrix
- student/config guides

Tasks:

- [ ] explain `base`, `ncku`, and `custom` responsibilities in both languages;
- [ ] explain `\TemplateStyleName` and exact-one-profile loading;
- [ ] explain how to copy/rename `custom` safely;
- [ ] separate institution policy from student metadata in `conf/`;
- [ ] explain institution names, dates, geometry, typography, department lists,
      and assets as profile concerns;
- [ ] provide the same example paths and commands once;
- [ ] describe validation and failure messages;
- [ ] explain that documentation/cover language does not choose a profile;
- [ ] remove Cantonese-only explanatory prose from this user-facing guide;
- [ ] preserve the current NCKU default and no-fallback policy.

Acceptance scenarios:

- Chinese-reading custom-profile maintainer can create and select a profile.
- English-reading custom-profile maintainer can perform the same steps.
- Neither path tells users to edit the shared renderer or NCKU profile directly.
- No customization instruction changes the default package behavior.

### BIL-06 — Add bilingual routing and maintainer summaries

**Dependencies:** student/public language conventions are settled.

Files:

- `docs/README.md`
- `docs/features/README.md`
- `docs/features/v2-modernization.md`
- `docs/features/validation-and-performance.md`
- `docs/features/release-and-distribution.md`

Router tasks:

- [ ] translate audience/task labels and directory/lifecycle summary;
- [ ] show which documents are complete bilingual and which use summary-plus-body;
- [ ] link the active requirement and todo while work remains active;
- [ ] keep source-of-truth order clear in both languages;
- [ ] keep current production/release/Overleaf state factual and non-duplicative.

V2 modernization Chinese summary must cover:

- [ ] production status and release target;
- [ ] preserved V1 public surface and unchanged project gate;
- [ ] NCKU/base/custom profile architecture;
- [ ] explicit behavior corrections versus compatibility;
- [ ] 19 native `l3keys` families and zero direct parser references;
- [ ] transitive PGF/TikZ caveat;
- [ ] where full machine contracts live.

Validation/performance Chinese summary must cover:

- [ ] canonical 271-page A4 output contract;
- [ ] normalized bbox word and raster identity evidence;
- [ ] latest public release read-back;
- [ ] student ZIP direct-build requirement;
- [ ] benchmark interpretation and no unsupported speed claim;
- [ ] rejected/deferred decisions remain inactive.

Release/distribution Chinese summary must cover:

- [ ] version/tag and two-asset contract;
- [ ] student versus examples package;
- [ ] GitHub Release as current canonical package;
- [ ] Overleaf submitted-versus-approved distinction;
- [ ] sample-repository retirement;
- [ ] Draft, watermark, certificate, and licensing cautions.

Acceptance:

- Chinese summaries contain conclusions and cautions, not speculative new work.
- English bodies remain complete and are not mechanically duplicated.
- Shared release facts still have one detailed owner.
- Feature index links every current record and no removed path returns.

### BIL-07 — Define bilingual changelog practice

**Dependencies:** terminology and root summary are stable.

Tasks:

- [ ] preserve all immutable release headings, versions, links, dates, and hashes;
- [ ] give current V2/current release entries a concise Traditional-Chinese
  summary and matching English summary;
- [ ] avoid retro-translating every historical 1.x entry unless needed for a
  current migration warning;
- [ ] define the format for future release entries in documentation policy;
- [ ] keep machine details linked to feature records rather than repeated;
- [ ] ensure user-visible changes, breaking corrections, migration action, and
  deprecation state are present in both languages.

Candidate format:

```markdown
## Version

### 繁體中文

- 使用者可觀察的變更。

### English

- The same user-visible change.
```

Acceptance:

- Release facts are equivalent across summaries.
- No historical version or release URL changes.
- Changelog remains scannable rather than doubling every internal detail.

### BIL-08 — Repair links, package integration, and repository policy

**Dependencies:** content paths finalized.

Tasks:

- [ ] update all first-party links to bilingual entry points;
- [ ] repair student-package absolute GitHub links;
- [ ] verify links from root, docs index, migration, changelog, student guide,
  configuration guide, and customization guide;
- [ ] update release verifier expected paths/content assertions;
- [ ] update documentation-management skill lifecycle and validation list;
- [ ] update `AGENTS.md` only with short active policy/link statements;
- [ ] keep `docs/requirements/02-bilingual-documentation.md` and this todo linked;
- [ ] search for old language labels, incorrect product casing, stale path names,
  and mixed active-document terminology;
- [ ] check that no generated PDF, ZIP, log, local editor state, or secret-like
  artifact is staged.

Acceptance:

- All relative links and local anchors resolve.
- Student package has no repository-only links where an offline file should exist.
- Repository policy has one canonical detailed owner.
- Requirements directory contains `.gitkeep` plus this one active requirement
  until completion.

## Human semantic review

Mechanical lint cannot establish translation quality. Complete these reviews
before final validation.

### Parity review checklist

For each paired section, compare:

- [ ] intent and user action;
- [ ] commands and argument values;
- [ ] paths and filenames;
- [ ] defaults and last-call-wins behavior;
- [ ] version and release facts;
- [ ] official-policy disclaimer;
- [ ] Draft/watermark/certificate warning severity;
- [ ] compatibility versus corrected-behavior distinction;
- [ ] rollback/recovery instruction;
- [ ] links and audience assumptions.

### Traditional-Chinese review checklist

- [ ] formal Taiwan prose, not Cantonese chat grammar;
- [ ] Traditional characters;
- [ ] NCKU terminology matches official context where known;
- [ ] `論文範本` used consistently in new prose;
- [ ] English technical noun explained on first use when retained;
- [ ] punctuation and spacing are readable around code identifiers;
- [ ] no claim of current official endorsement from historical 2015 evidence.

### English review checklist

- [ ] natural English rather than literal translation;
- [ ] NCKU-specific terms explained;
- [ ] international reader is not assumed to be non-NCKU;
- [ ] certificate/submission steps do not assume Taiwan institutional knowledge;
- [ ] commands can be copied exactly;
- [ ] warnings are not weaker or less visible than Chinese counterparts.

### Owner review checkpoints

Request Leon review at these boundaries rather than interrupting once per file:

1. governance/glossary plus one representative bilingual section;
2. complete packaged student journey;
3. root/migration/customization user journeys;
4. maintainer summaries/changelog;
5. final diff and validation evidence before any publication decision.

Aggregate questions within each checkpoint. Do not request repeated intervention
for wording that follows an already approved glossary.

### BIL-09 — Static and semantic validation

**Dependencies:** all intended content slices are present.

#### Repository and path checks

- [ ] `git diff --check` passes;
- [ ] no unstaged or untracked unintended files;
- [ ] final manifest contains only approved source/docs/test changes;
- [ ] every relative Markdown link resolves from its owning file;
- [ ] every local anchor resolves;
- [ ] every removed/renamed path has zero first-party references;
- [ ] docs and feature indexes link every current record;
- [ ] requirement and todo link each other;
- [ ] package-facing links work from the extracted student ZIP root;
- [ ] no generated artifacts or secret-like files are staged.

#### Language-structure checks

- [ ] all complete bilingual surfaces contain the required Chinese and English
  blocks for every mandatory topic;
- [ ] all maintainer records contain Chinese summary and English-body markers;
- [ ] no active user-facing prose uses unapproved `LaTex`/`XeLatex` casing;
- [ ] selected Cantonese-only terms are absent outside documented exceptions;
- [ ] no checker uses raw character ratio as quality proof;
- [ ] all shared commands occur in one canonical block per topic;
- [ ] a human parity matrix records review completion.

#### Compatibility checks

Run:

```bash
python3 scripts/test/check-v1-project-migration.py
python3 scripts/test/check-v1-api.py
```

Assert independently:

```text
thesis/conf/conf.tex
size   = 24780
sha256 = ca7232190705e4dbc6ff1f6fe2613c0ce1cfdb6dcd6486ee15df6a07b195b4e0
```

- [ ] all 18 pinned inputs remain byte-identical;
- [ ] all 597 LaTeX/xparse and 65 literal-def declarations remain preserved;
- [ ] no runtime diagnostic or macro implementation changed in the docs slice.

#### Manual user-journey review

Execute as documentation walkthroughs before relying on CI:

1. Chinese NCKU student, English cover, master degree;
2. English NCKU student, English cover, PhD degree;
3. Chinese NCKU student, Chinese cover;
4. Chinese non-NCKU maintainer creating a custom profile;
5. English non-NCKU maintainer creating the same profile;
6. Chinese compatibility-first v1 migration;
7. English compatibility-first v1 migration;
8. extracted student package build and submission checklist.

For each walkthrough, record:

- first document opened;
- links followed;
- commands copied;
- configuration choices;
- ambiguity or missing prerequisite;
- successful end state;
- wording correction needed.

Acceptance:

- Static checks and human review agree on the same final paths and commands.
- No unresolved ambiguity is deferred without being recorded as a new requirement.

### BIL-10 — Exact staged-tree build, release package, and output validation

**Dependencies:** static and semantic reviews pass; only intended paths are staged.

Because release checks use committed `HEAD:thesis`, validate the staged tree in an
unreachable temporary commit/worktree before the real local commit:

```bash
git diff --cached --check
test -z "$(git diff --name-only)"
test -z "$(git ls-files --others --exclude-standard)"

tree=$(git write-tree)
temporary_commit=$(printf 'temporary bilingual docs validation\n' |
  git commit-tree "$tree" -p HEAD)
git worktree add --detach /tmp/ncku-bilingual-validation "$temporary_commit"
(
  cd /tmp/ncku-bilingual-validation
  just ci
  just release bilingual-review
)
```

Required staged-tree gates:

- [ ] `just ci` passes;
- [ ] `just release bilingual-review` passes;
- [ ] generated student ZIP passes archive integrity;
- [ ] exact archive file list equals committed `HEAD:thesis` tree;
- [ ] student ZIP contains `README.md` and `conf/README.md`;
- [ ] package contains no repository tooling or wrapper nesting error;
- [ ] migration/customization links point to existing public main paths;
- [ ] examples ZIP allowlist and PDF checks remain unchanged.

Direct package read-back:

- [ ] extract generated student ZIP to a clean directory;
- [ ] change into extracted package root;
- [ ] run documented direct command:

  ```bash
  latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
  ```

- [ ] verify `thesis.pdf` and `thesis.synctex.gz` exist;
- [ ] verify 271 pages and A4;
- [ ] verify no unresolved references/citations or rerun warnings;
- [ ] verify cover has no unexpected Draft marker;
- [ ] verify no template-added institutional watermark by default.

Canonical identity:

Because bilingual changes are documentation/comments outside byte-pinned TeX
inputs, output must remain identical to the accepted production baseline:

```text
pages:                 271
paper:                 A4
normalized bbox words: 40823
text:                  identical
fonts:                 identical
raster:                271/271 identical at 120 DPI
```

- [ ] compare PDF text to canonical baseline;
- [ ] compare normalized bbox words/count;
- [ ] compare embedded fonts;
- [ ] compare raster pages at 120 DPI;
- [ ] treat any PDF difference as a blocker, not a documentation exception.

Cleanup and identity check:

- [ ] remove temporary worktree and generated artifacts outside repository;
- [ ] verify current index tree equals validated temporary commit tree;
- [ ] verify branch/HEAD remained at the pre-commit checkpoint;
- [ ] verify no remote or upstream was created;
- [ ] create the intended local commit only after exact-tree validation.

## Proposed implementation commit boundaries

Keep commits locally reviewable. Exact boundaries may collapse when a smaller
slice is clearer, but do not combine unrelated behavior changes.

### Commit 0 — Planning only

```text
docs: plan bilingual documentation
```

Contains only requirement, todo, and active-index backlinks. Stop afterward.

### Commit 1 — Governance and checker

```text
docs: define bilingual documentation policy
```

Contains policy, glossary, structure, and deterministic checker/wiring if
accepted. No large content rewrite.

### Commit 2 — Student package journey

```text
docs: add bilingual student guidance
```

Contains student README, packaged config companion, and package-verifier updates.
Must pass staged-tree release package verification independently.

### Commit 3 — Public, migration, and customization journeys

```text
docs: add bilingual public and migration guides
```

Contains root README, migration, and customization changes.

### Commit 4 — Maintainer summaries and changelog

```text
docs: add Traditional Chinese maintainer summaries
```

Contains docs indexes, feature summaries, and changelog policy/content.

### Commit 5 — Closure only if validation requires source/check fixes

Use only for narrowly scoped validation repairs. Do not create an empty
"cleanup" commit. Final requirement/todo removal belongs to a separate closure
commit after all evidence passes and durable policy is already current.

## Risk register

| Risk | Consequence | Prevention | Recovery |
| --- | --- | --- | --- |
| Editing pinned `conf.tex` | breaks V1 migration contract | companion guide; hash assertion | revert file; rerun checker |
| Translation drift | different user behavior | shared commands; paired review | block slice; reconcile both blocks |
| Language/profile conflation | wrong institution setup | independent-axis matrix/examples | rewrite routing before merge |
| Mixed formal/Cantonese prose | poor Taiwan documentation quality | glossary and targeted lint | human edit; no global replace |
| Wrong product casing | search/brand inconsistency | deterministic casing check | correct active prose |
| Root README remains too long | poor discovery | route, summarize, relocate history | restore durable facts to owner doc |
| Historical endorsement overstated | institutional/reputation risk | preserve dates/disclaimer | revert claim; cite current official source |
| Warning loses force in translation | submission failure | parity checklist for safety blocks | block completion |
| Duplicate commands diverge | build failure | one shared code block | collapse to canonical block |
| Checker claims semantic proof | false confidence | document structural limits | remove/relax invalid claim |
| New guide missing from ZIP | English/Chinese journey incomplete | package verifier assertion | fix tree/link; rebuild |
| External link changes | stale navigation | verify live where required | state last-checked date; use canonical root |
| Overleaf status inferred | false publication claim | separate submitted/approved/read-back | restore last verified status |
| PDF output changes | hidden source/package regression | canonical identity gate | revert slice; investigate source diff |
| Generated files staged | repository pollution | explicit manifest review | unstage/remove artifact |
| Accidental push | violates owner boundary | no upstream/remote; local checks | stop; report immediately |

## Recovery procedure

If a slice fails:

1. stop at the first failing gate;
2. preserve failing log outside the repository;
3. identify whether failure is prose parity, path/package, source integrity, or
   output identity;
4. revert only the failing local commit or patch;
5. keep requirement/todo active and mark the failed task with evidence;
6. do not edit compatibility manifests, lower expected counts, or disable checks;
7. rerun the smallest focused gate;
8. rerun full staged-tree validation before declaring recovery.

If translation wording is disputed rather than technically wrong, record the
exact phrase and both candidate renderings in the owner checkpoint; do not fork
two undocumented conventions across files.

## Definition of ready for implementation

BIL-01 may start only when:

- [ ] Leon has reviewed this planning commit;
- [ ] the hybrid content model is accepted;
- [ ] the `conf.tex` companion-guide constraint is accepted;
- [ ] `論文範本` and the terminology table are accepted or amended once;
- [ ] runtime diagnostics and full teaching-corpus translation remain explicitly
  out of scope;
- [ ] local-only versus publication boundary is explicit;
- [ ] current worktree is clean at the planning commit.

## Definition of done

The requirement is complete only when:

- [ ] BIL-01 through BIL-10 acceptance criteria pass;
- [ ] both-language human walkthroughs pass;
- [ ] all exact staged-tree and canonical identity gates pass;
- [ ] current source/docs contain no active contradiction;
- [ ] durable language policy is in current docs and skill;
- [ ] release/Overleaf facts remain accurate;
- [ ] Leon reviews the final local diff/evidence;
- [ ] shipped knowledge is consolidated into current docs;
- [ ] this requirement and todo are removed in closure;
- [ ] `docs/requirements/` returns to `.gitkeep` only;
- [ ] no publication occurs without separate approval.

## Completion report contract

The final report must state, with real tool evidence:

- files and journeys made bilingual;
- files intentionally left summary-plus-English or English-only;
- exact pinned-input hash result;
- language/link/checker results;
- `just ci` and release-review results;
- student ZIP file/read-back results;
- direct-build page/paper/SyncTeX/reference results;
- canonical text/bbox/font/raster identity results;
- local commits and branch state;
- explicit push/PR/merge/release/Overleaf status.

It must not claim translation quality solely from a script, claim Overleaf
approval without public read-back, or claim completion while this requirement or
todo remains active.
