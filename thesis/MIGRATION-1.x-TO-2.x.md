# Migrating NCKU Thesis Template Projects from 1.x to 2.x

V2 preserves the machine-audited 1.x LaTeX/xparse and literal `\def` declaration surfaces through the complete 2.x line. Existing projects can therefore migrate the template implementation first, verify unchanged NCKU output, and adopt native v2 profile structure gradually.

## Before You Start

1. Commit or archive the complete working 1.x project.
2. Build the 1.x PDF once and keep it as a visual/text reference.
3. Record the XeLaTeX version, page count, paper size, cover/oral dates, and any deliberately enabled Draft/watermark options.
4. Separate user-owned files from template implementation:

   ```text
   User-owned:        conf/conf.tex, context/, figures/, bibliography data
   Template-owned:    template/, fonts/, build configuration, packaged examples
   Entry point:       thesis.tex (merge local edits deliberately)
   ```

Do not migrate by overwriting an uncommitted thesis directory and hoping Git can reconstruct metadata later.

## Path A: Existing NCKU Project, Compatibility First

Use this path for a thesis already in progress.

1. Keep `conf/conf.tex`, thesis content, figures, bibliography entries, and any local certificate PDF.
2. Replace template-owned implementation files with the v2 package.
3. Merge any local changes to `thesis.tex` instead of replacing them blindly.
4. Keep existing helper calls; the v1 adapter loads automatically.
5. From the project directory that contains `thesis.tex`, build directly with XeLaTeX/latexmk:

   ```bash
   latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
   ```

6. Resolve only the documented correctness changes below.
7. Compare the new PDF with the saved 1.x reference: cover, front matter, dates, contents, references, bibliography, representative body pages, and final pages.
8. Confirm no unexpected `(Draft)`／`(初稿)` text or institutional watermark was enabled.

No helper rename is required for this path.

## Path B: Native V2 Project

Use this path for a new thesis or a maintained institutional fork.

1. Start from the packaged v2 student project.
2. Copy thesis content, figures, bibliography entries, and certificate files.
3. Re-enter or merge thesis metadata in `conf/conf.tex`.
4. Keep the repository default `ncku` profile for NCKU work.
5. For another institution, create/select one profile under `template/style/` by following [`template/style/Customization.md`](template/style/Customization.md).
6. Keep compatibility calls if they remain useful; replacing them is optional during 2.x.
7. Build after every migration step.

## Stable Project Boundaries

These student-facing paths remain stable in 2.x:

```text
thesis.tex
conf/conf.tex
context/
example/
template/
```

`conf/` remains student thesis data. Institution geometry, wording, catalogues, date rules, and assets remain under `template/style/`; v2 does **not** introduce `conf/style.tex`.

## Public Helper Compatibility

The full Git repository's `tests/v1-public-api.json` records 597 runtime-visible
1.x LaTeX/xparse commands/environments plus 65 literal `\def`-style
declarations. Their names and complete audited argument shapes remain available
throughout 2.x. A separate `tests/v1-comment-environment-artifacts.json` audit
records 22 declarations found inside runtime-dead LaTeX `comment` environments;
these are not removed public APIs.

These test manifests and the checker are maintainer tooling in the full Git
checkout; they are intentionally absent from the student ZIP. Maintainers run,
from the repository root:

```bash
python3 scripts/test/check-v1-api.py
```

Native v2 internals may delegate old helpers to profile hooks. Compatibility preserves the API, not a verified defect.

### Unchanged V1.8.2 Project Gate

In the full Git repository, the declaration baseline above is paired with a
runtime migration contract:

```text
tests/v1-project-migration.json
scripts/test/check-v1-project-migration.py
```

The manifest pins 18 student-owned files (296,726 bytes) to release
`v1.8.2.260715154703`. It covers the root `thesis.tex`, `conf/conf.tex`, student
content, bibliography data, and oral-certificate assets as a byte-for-byte
source-integrity contract.

Runtime evidence is deliberately split:

- the unchanged v1 entry point and configuration build through the v2 adapter,
  base contract, and NCKU profile, producing the 271-page A4 canonical result;
- the StudentMode fixture disables teaching examples and asserts the active
  student content files through the XeLaTeX `.fls` recorder plus all three
  bibliography databases through the BibTeX `.blg` record.

Files disabled by the v1 configuration (for example alternate abstracts and
external oral-certificate PDFs) remain source-pinned but are not falsely
claimed as runtime-loaded. Together these gates prove a representative v1
project and its active student-content path run on v2. They complement, but do
not replace, focused semantic tests for corrected helpers.

### V1 Adapter Layout

```text
template/compat/v1.tex
  template/command/cmd-college.tex      compatibility wrapper
  template/command/cmd-department.tex   compatibility wrapper
  template/compat/deprecated.tex        23 deprecated command tombstones
  template/style/ncku/college.tex       NCKU-owned data
  template/style/ncku/department.tex    NCKU-owned data
```

The adapter is loaded even for a custom profile so old NCKU preset commands remain defined. It also owns 23 public commands that had already become unsupported during 1.x: their names remain defined and still emit the same migration diagnostic followed by `\stop`, rather than degrading to an undefined-control-sequence error. The active one-argument `\RefTo{label}` helper remains available; only its historical commented-out zero-argument tombstone stays excluded. A custom profile does **not** load NCKU geometry, date policy, or watermark asset. This source-level compatibility cost is intentional for 2.x.

## Corrected Behaviors

This table is normative and must be updated for every observable helper correction.

| 1.x behavior | 2.x behavior | Required user action |
| --- | --- | --- |
| `\StartSubSubSection{title}{label}` wrote an empty reference when the default heading intentionally hid its number. | The heading remains visually unnumbered, while the label records a stable hierarchical value such as `1.1.1.1`; empty-link warnings are rejected. | None; existing references become usable. |
| `\GetOralYearInTaiwanYear` recalculated through thesis state and could change `\GetThesisYearInTaiwanYear`. | The getter reads oral-year state without modifying thesis-year state; `\SetOralEngDate` keeps oral Taiwan-year state synchronized. | None. |
| The second argument of `\SetDeptName{chi}{short}{full}` was discarded. | The short name is stored and available through `\GetDeptEngShortName`; `\GetDeptEngName` still returns the full name. | None; code may optionally use the new getter. |
| `\SetDeptDPS` produced `Departmment of Photonics`. | The catalogue value is corrected to `Department of Photonics`. | Rebuild to receive the corrected text. |
| The English oral certificate combined oral day with cover month/year. This was hidden by NCKU's rule because both dates normally matched. | English oral output uses oral day, oral month, and oral year consistently. | Non-NCKU projects with distinct dates receive the correct oral date automatically. |
| The Doctoral English cover borrowed its day from oral metadata even though `\SetCoverDate` owns only cover year/month. | Master/Doctoral English cover date tokens are profile-owned. Generic/custom profiles render only cover-owned month/year; NCKU explicitly retains its established oral-day policy. | None for NCKU; non-NCKU profiles may customize the two date tokens if their rules require another format. |
| `\SetCommitteeSize` accepted the renderer's full 2--9 capacity for every degree even though the NCKU teaching text stated Master 3--5 and Doctoral 5--9, and another teaching line incorrectly said 4--9. | Committee-size validation is profile-owned. The NCKU profile clamps Master requests to 3--5 and Doctoral requests to 5--9; the neutral/custom policy retains the generic 2--9 renderer capacity. | Select `\MasterDegree` or `\PhdDegree` before calling `\SetCommitteeSize`, then rebuild. |
| The theorem `label={...}` option was passed to an optional helper with mandatory braces, so the label key appeared in visible text and no label was written. A titled theorem also wrote the mutable `\TmpValueTitle` token to nameref metadata, which became blank after later insertions. | The option is passed through the existing optional signature, label keys stay out of visible output, `\ref` resolves the theorem number, and the title is frozen before `\label` so `\nameref` resolves correctly. | None; rebuild to receive working theorem references. |
| Figure, subfigure, and table captions could write mutable pgf temporary tokens to nameref metadata. A later parse changed the title, while leaving a subfigure scope made `\TmpMISubValueCaption` undefined on the next LaTeX pass. | Numbered, starred, combined, and separate caption wrappers freeze the rendered caption into `\@currentlabelname` before writing labels. Existing `\ref` numbers are unchanged and `\nameref` now returns the literal caption text. | No source migration; rebuild enough times for the auxiliary file to refresh. |
| Numbering getters retained reusable pgf prefix, separator, and counter-name aliases, so a later general/appendix setup could rewrite earlier getters. Repeating appendix equation setup appended again, changing `2.8` to `2.82.8`. | Parsed configuration and counter names are frozen into each format string while counter values remain dynamic. Repeated setup is idempotent across general/appendix title and figure/table/equation paths. | No source migration; custom numbering users should rebuild to refresh generated labels and lists. |
| A theorem configured through a forward or multi-hop `FollowCounter` chain depended on initializer order, could retain mutable getter aliases, or fail with `No counter '...' defined`; optional/starred types could not reliably become numbered, and cycles overflowed recursively. The `Theorem` initializer also hard-coded `section`. | Registered chains resolve recursively to a frozen `section`/empty terminal before environment creation. Numbered and optional types consistently select global/scoped/starred syntax; self-lookups do not create aliases, and cycles stop with a deterministic package error. | None; custom theorem-format users should rebuild. |

## Date Migration

Public setters are unchanged:

```tex
\SetOralDate{2023}{12}{31}
\SetCoverDate{2024}{7}
```

V2 separates raw input from profile-resolved display policy:

- `\GetRequestedCoverYear`／`\GetRequestedCoverMonth`: raw `\SetCoverDate` values;
- `\GetThesisYear`／`\GetThesisMonth`: resolved cover display values;
- oral getters: independent oral metadata.

The NCKU profile still makes oral date authoritative for the cover, so existing NCKU output remains unchanged. A non-NCKU profile uses explicit cover date by default and does not borrow an oral day for its Doctoral English cover. Institutional forks should override `\ApplyOralDatePolicy`／`\ApplyCoverDatePolicy` and the profile-owned Master/Doctoral English cover-date tokens, not the public setters.

## Migrating a 1.x Non-NCKU Style Port

The v1.5.0 placement intent remains: institutional ports belong under `template/style/`. V2 changes how they are activated.

1. Copy `template/style/custom/` as the new profile base; do not copy/load NCKU first merely to undo it later.
2. Move institution geometry,校名、watermark and date behavior from the old custom file into `<profile>/<profile>.tex`.
3. Call exactly one `\RegisterTemplateStyle{<profile>}`.
4. Select the profile through `\TemplateStyleName` in `template/style/style.tex`.
5. Replace old overrides of `\SetOralDate`／`\SetCoverDate` with policy-hook overrides.
6. Override `\ApplyCommitteeSizePolicy` only when the institution has degree-specific committee ranges; keep `\SetCommitteeSize` unchanged.
7. Move institution-specific cover/oral wording and English cover-date formats to the provided profile-token setters.
8. Use `\SetCollName`／`\SetDeptName` for project metadata or maintain an institution-owned catalogue inside the new profile.
9. Build the custom cover and oral certificate with different oral/cover dates to prove policy separation.
10. Confirm the `.fls` recorder output does not load an unintended institutional asset.

The executable example is `tests/custom-style.tex` in the full Git repository;
it is test tooling and is intentionally absent from the student ZIP.

## Verification Checklist

### Portable checks

Run these commands from an extracted student ZIP or any migrated project
directory that contains `thesis.tex`:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex
pdfinfo thesis.pdf
pdftotext thesis.pdf thesis.txt
```

Verify:

- A4 page dimensions and expected page count;
- university/college/department/title/author/advisor text;
- cover and oral dates;
- table of contents and all references;
- bibliography convergence;
- no unexpected Draft text or institutional watermark;
- representative cover, front-matter, body, and final rendered pages.

### Repository-maintainer checks

The following commands require a complete Git checkout and run from the
repository root. They are not available in the student ZIP:

```bash
just _test-custom-style
python3 scripts/test/check-v1-api.py
python3 scripts/test/check-v1-project-migration.py
just test
just ci
git diff --check
```

The v2 architecture acceptance evidence includes:

- 597/597 runtime-visible v1 LaTeX/xparse commands/environments and 65/65
  literal `\def`-style declarations preserved, with 22 runtime-dead
  comment-environment declarations retained in a separate audit;
- 18 student-owned files match v1.8.2 byte-for-byte; the unchanged entry/config
  and active StudentMode content/bibliography paths pass separate v2 runtime
  gates;
- the student ZIP matches the complete tracked `thesis/` tree exactly, retains
  the migration guide/adapter/profile files, and its direct `latexmk -xelatex
  thesis.tex` path produces the canonical 271-page A4 PDF;
- neutral custom profile builds six A4 pages covering Chinese/English Master
  cover, Chinese oral, both Master/Doctoral English oral branches, and the
  Doctoral English cover without NCKU visible policy or watermark asset;
- custom Chinese dates remain Gregorian, explicit cover and oral dates stay
  distinct, the Doctoral English cover does not borrow the oral day, and custom
  degree display names do not change the numeric branch;
- canonical NCKU output remains 271 A4 pages;
- canonical extracted text and cover word bounding boxes/raster remain identical across the profile extraction.
