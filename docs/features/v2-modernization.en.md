<!-- language: en; summary: v2-modernization.md -->

[繁體中文摘要](v2-modernization.md) | [English technical record](v2-modernization.en.md)

# Template architecture and 2.x compatibility

The template provides a community-maintained NCKU thesis layout with XeLaTeX, BibTeX and `latexmk`. Student data, reusable mechanisms and institution policy have separate owners. Current university and department rules override template guidance.

## Project and load order

Student projects keep `thesis.tex`, `conf/conf.tex`, `context/`, `example/` and `template/`. Students write under `context/` and select content in `context/context.tex`; `conf/` contains thesis data. Institution ports belong under `template/style/`, never `conf/style.tex`.

`template/configure.tex` loads the runtime in this order:

```text
1. template/command/ and template/compat/v1.tex
2. template/style/base/ plus exactly one selected institution profile
3. \TemplateConfigurationFile (default: ./conf/conf)
4. \FillInPDFData and remaining initialization
```

Generic commands are available to profiles. A selected profile defines reusable catalogue entries before student configuration selects an entry. PDF metadata uses the resulting student values.

## Institution profiles and resolved policy

`template/style/style.tex` selects one registered profile. The base layer supplies generic metadata and rendering hooks. The default `ncku` profile owns NCKU geometry, wording, date policy, assets and the [college/department catalogue](../../thesis/template/style/ncku/README.en.md). The `custom` profile is a neutral buildable skeleton with no NCKU catalogue or assets. It is not a ready-to-submit profile for another university.

The generic metadata contract includes `\SetUniversityName{chi}{eng}`, `\SetCollName{chi}{eng}` and `\SetDeptName{chi}{short}{full}`. NCKU presets are available only when the NCKU profile is selected. Other catalogues use institution-prefixed command names. See [institution customization](../../thesis/template/style/Customization.en.md) for the complete porting procedure; the NTU example demonstrates API wiring, not institutional compliance.

Public setters store input and delegate policy to `\ApplyOralDatePolicy`, `\ApplyCoverDatePolicy`, `\ApplyOralChiYearPolicy` and `\ApplyCommitteeSizePolicy`. Degree branching uses numeric Master/Doctoral state, independent of display language.

- `\GetRequestedCoverYear` and `\GetRequestedCoverMonth` expose raw cover input; `\GetThesisYear` and `\GetThesisMonth` expose profile-resolved values. Oral getters remain independent.
- NCKU derives the cover date from oral metadata. Generic/custom profiles use cover-owned month/year without borrowing an oral day. Cover-date tokens belong to the profile.
- NCKU committee policy clamps Master to 3–5 and Doctoral to 5–9. Generic/custom capacity is 2–9. Select degree before setting committee size.

## Public compatibility

Every declared 1.x public command and environment keeps its name and argument shape throughout 2.x. `template/compat/v1.tex` loads automatically; unchanged NCKU projects retain their presets through the default profile. Deprecated commands retain explicit migration diagnostics rather than becoming undefined commands. The one-argument `\RefTo{label}` remains active.

The [public API manifest](../../tests/100-v1-public-api.json) and [project migration contract](../../tests/102-v1-project-migration.json) protect the support boundary. An immutable v1.8.2 fixture builds through the current runtime in example and StudentMode paths; live student placeholders need not be byte-identical to that fixture. Student-guide configuration line references are checked separately.

The [migration guide](../v1-to-v2-migration.en.md) explains current helper behavior, dates, fonts and recovery. Compatibility preserves public interfaces while allowing verified behavior corrections.

## Helper responsibilities

- Namespaced `l3keys` parsers reset defaults on every call, preserve expanded values and reject unknown keys. Explicit `xparse` supports protected `G{...}` signatures; the visual framing stack still uses PGF/TikZ.
- The theorem registry owns type order, style, defaults and counter policy. Public wrappers remain available. Counter chains resolve forward and through multiple hops; cycles produce a deterministic error. Titles and labels retain stable reference metadata.
- Numbering setup freezes prefixes, separators and counter names while counter values remain dynamic. Repeated general/appendix setup is idempotent.
- Figure, subfigure and table captions freeze label metadata. Floats retain `[H]`; accepted compatibility options are described according to their actual effects in the [writing guides](../../thesis/context/README.en.md).

## Supported boundaries

XeLaTeX is the supported 2.x engine; BibTeX remains the bibliography system. Direct student and Overleaf builds do not require repository tooling. Output is untagged, with no PDF/UA claim. The template is not officially endorsed by NCKU and cannot certify another institution's compliance.

[Validation](validation-and-performance.en.md) describes the live checks. [Distribution](release-and-distribution.en.md) defines package and publication contracts.
