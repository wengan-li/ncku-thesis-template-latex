<!-- bilingual:summary-plus-english -->

# V2 modernization

Status: production

- Base architecture release:
  [`v2.0.0.260717130231`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.0.260717130231)
- Current production release:
  [`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734)

## 繁體中文摘要

- V2保持XeLaTeX、學生project shape、direct `latexmk` path及完整經audit的1.x public API。
- 597個runtime-visible LaTeX/xparse declarations、65個literal-def declarations及18個V1 student inputs由machine gates保護。
- 共用renderer、NCKU policy及其他學校ports分別由`base`、`ncku`及`custom` profiles負責；文件／封面語言不會選擇profile。
- 已驗證的theorem、caption、numbering、date、committee及catalogue defects在不改public signatures下修正，詳情由雙語migration table擁有。
- Repository-owned generic command parsing使用19個native `l3keys` families，direct `pgfkeys` parser references及explicit package load為零。
- PGF/TikZ並非完全移除；`mdframed`的TikZ framing仍可transitively載入runtime dependency。
- V2完成狀態不會自動啟用P3 architecture experiments；新工作需要新的owner-approved Intent。

## English technical record

V2 modernizes the XeLaTeX template while preserving the established NCKU output,
student project shape, direct compiler workflow, and complete audited 1.x public
surface throughout the 2.x line.

## Shipped outcome

V2 delivers one maintained production line with these boundaries:

- `thesis.tex`, `conf/conf.tex`, `context/`, `example/`, and `template/` remain
  stable student-facing project paths.
- XeLaTeX remains the supported production engine. Students can build directly
  with `latexmk`; repository `just` commands are maintainer orchestration, not a
  package requirement.
- Existing 1.x projects keep their command and environment names and migrate
  through `template/compat/v1.tex` without a helper-renaming campaign.
- Generic renderers own reusable mechanics. Institution rules, wording, dates,
  catalogues, and assets belong to one selected profile under `template/style/`.
- The default `ncku` profile preserves NCKU behavior. The neutral `custom`
  profile proves another institution can start without loading NCKU geometry,
  visible policy, dates, or watermark assets.
- Correctness bugs are fixed behind unchanged public signatures and recorded in
  the [migration guide](../v1-to-v2-migration.md).

## Compatibility contract

### Declaration surface

[`tests/v1-public-api.json`](../../tests/v1-public-api.json) is generated only
from immutable pre-V2 commit
`f80a2649232dd25761276ccf7043cf3f3a79e031`. It protects:

- 597 runtime-visible LaTeX/xparse commands and environments;
- 65 literal `\def`-style declarations;
- complete audited argument shapes, including balanced nested xparse defaults and
  optional-first LaTeX declarations.

[`tests/v1-comment-environment-artifacts.json`](../../tests/v1-comment-environment-artifacts.json)
separately records 22 declarations found in runtime-dead LaTeX `comment`
environments. They are historical scanner artifacts, not public APIs. The source
checker refuses to regenerate the compatibility baseline from current V2 merely
to make a deletion pass.

### Unchanged project surface

[`tests/v1-project-migration.json`](../../tests/v1-project-migration.json) pins 18
student-owned files (296,726 bytes) to immutable release
`v1.8.2.260715154703`. Source integrity and runtime behavior are deliberately
separate:

- the unchanged 1.x entry point and configuration build through the V2 adapter,
  base layer, and NCKU profile;
- StudentMode separately proves active content inputs through exact `.fls`
  records and all three bibliography databases through `.blg` records;
- files disabled by the historical configuration remain source-pinned without
  being misreported as runtime-loaded.

The representative compatibility output is the canonical 271-page A4 thesis.

### Adapter boundary

```text
1.x command/environment
  -> template/compat/v1.tex
  -> V2 mechanism/state
  -> selected template/style profile policy
  -> existing renderer/output
```

The adapter owns legacy college/department wrappers and loads
`template/compat/deprecated.tex`, which keeps 23 literal zero-argument tombstones
with their exact diagnostics and `\stop` behavior. The active one-argument
`\RefTo{label}` remains a live helper; its old commented zero-argument tombstone
is not revived.

Because 1.x did not mark a reliable private API, the compatibility baseline is
conservative. Removing or changing a protected declaration requires a later
major-version decision and an explicit migration contract.

## Profile architecture

`template/style/style.tex` selects exactly one registered profile.

```text
template/style/base/       reusable profile contract and rendering hooks
template/style/ncku/       NCKU geometry, wording, catalogues, dates, assets
template/style/custom/     neutral starting profile for another institution
template/compat/           1.x and deprecated-command adapters
```

Public setters retain their signatures. Profiles customize hooks and resolved
display tokens instead of replacing raw metadata storage:

```text
SetOralDate       -> ApplyOralDatePolicy
SetCoverDate      -> ApplyCoverDatePolicy
SetOralChiDate    -> ApplyOralChiYearPolicy
SetCommitteeSize  -> ApplyCommitteeSizePolicy
```

Generic/custom Chinese dates remain Gregorian. The NCKU profile explicitly owns
Taiwan-year rendering and its established cover-date policy. Generic committee
renderer capacity is 2--9; the NCKU profile enforces Master 3--5 and Doctoral
5--9 from numeric degree state.

Institution ports remain under `template/style/`; V2 does not introduce
`conf/style.tex`. See
[`thesis/template/style/Customization.md`](../../thesis/template/style/Customization.md).

## Hardened subsystems

### API inventory and dead-source boundary

The source scanner now handles balanced TeX groups, optional defaults, parity-aware
`%` comments, and LaTeX `comment` environments. Only audited runtime-dead blocks
were removed; the separate artifact manifest preserves why the old count was
wrong.

### Deprecated commands

All 23 runtime deprecated command tombstones are literal declarations in one V1
compatibility module. A focused fixture checks every diagnostic and intercepted
`\stop`, preventing a cleanup from turning bounded migration errors into undefined
commands.

### Numbering

Focused contracts cover all general/appendix title selectors, seven counter
styles, references, figure/table/equation formats, unknown/empty no-ops, dynamic
counter values, and repeated setup. Parsed prefixes, separators, and counter
names are frozen while counter values remain dynamic. Repeated appendix equation
setup is idempotent instead of accumulating output.

### Theorems

One 21-row registry owns theorem order, style/numbering policy, defaults,
membership, key parsing, initialization, and default application. Literal public
insertion and initializer wrappers remain compatibility adapters. Counter chains
resolve forward and multi-hop references to a frozen terminal counter; empty,
unknown, self, arbitrary existing counters, optional numbering, and deterministic
cycle failure are all fixture-protected. Title and label metadata are frozen so
`\ref` and `\nameref` survive later parses.

### Figures and tables

Figure, multi-figure, subfigure, and table captions freeze literal label names
before writing auxiliary data. One private helper owns the identical minipage,
frame, and opacity wrapper without changing public commands, forced `[H]`
placement, compatibility no-op keys, table caption position, scaling, labels, or
visible output.

### Repository-owned key parsers

Nineteen command parser families were moved in eleven independently validated
slices from direct `pgfkeys` use to namespaced `l3keys` families. Every call
restores complete defaults and preserves expanded storage, omission sentinels,
unknown-key failure, scratch-state behavior, and public signatures.

Active student source now has:

- zero direct `\pgfkeys` or `\pgfkeysvalueof` parser references;
- zero `l3keys2e` references;
- no explicit `pgfkeys` package load.

This is not a claim that PGF/TikZ disappeared: `mdframed[framemethod=tikz]` still
loads the visual stack and its transitive `pgfkeys` dependency. Explicit `xparse`
is also retained because protected public signatures still use `G{...}` argument
types that the kernel interface deliberately does not provide.

## Corrected behavior

Compatibility preserves APIs, not verified defects. The normative before/after
and required-user-action table is in
[`v1-to-v2-migration.md`](../v1-to-v2-migration.md#已修正行為-corrected-behaviors). It covers:

- stable subsubsection references;
- oral/Taiwan-year state separation;
- department short-name storage and the DPS spelling correction;
- oral and profile-owned cover-date composition;
- profile-owned committee ranges;
- theorem labels/titles and caption `nameref` metadata;
- repeatable numbering state;
- theorem counter-chain resolution and cycle diagnostics.

Every correction keeps the public name and argument shape, has a focused fixture,
and retains integration proof for unrelated NCKU output.

## Completion boundary

The V2 modernization and repository-owned command-parser migration are complete.
There are no active requirements under `docs/requirements/`.

The following are explicitly inactive and require a new owner-approved Intent:

- a formal `nckuthesis.cls` or broad class/package redesign;
- repository-wide `ifthen` conversion;
- broad unrelated `expl3` rewriting;
- `l3build` replacing the current gate;
- engine migration;
- tagged-PDF or PDF/UA claims.

Current output is not claimed to be tagged or PDF/UA compliant. Future work must
start from measured need and a bounded compatibility fixture, not parser or
package reference counts.

See [validation and performance](validation-and-performance.md) for the active
gates and measured decisions, and [release and distribution](release-and-distribution.md)
for public package contracts.
