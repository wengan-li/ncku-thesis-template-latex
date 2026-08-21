<!-- language: en; summary: v2-modernization.md -->

[繁體中文摘要](v2-modernization.md) | [English technical record](v2-modernization.en.md)

# V2 modernization

Status: production

- Base architecture release:
  [`v2.0.0.260717130231`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.0.260717130231)

V2 reorganized the template's internals without changing what students see:
the same NCKU thesis layout, the same project folders, the same XeLaTeX plus
`latexmk` build, and every 1.x command still working. The point of the
reorganization is a clean separation between generic thesis machinery and
NCKU-specific policy. That separation is what lets students from other
institutions build their own profile, and what lets proven bugs get fixed
without breaking existing projects.

## What V2 keeps stable

- `thesis.tex`, `conf/conf.tex`, `context/`, `example/`, and `template/` stay
  where students expect them.
- XeLaTeX remains the production engine. A thesis builds directly with
  `latexmk`; the repository's `just` commands are project tooling, never a
  student requirement.
- Every declared 1.x command and environment keeps its name and argument shape
  throughout the 2.x line. Existing projects load `template/compat/v1.tex`
  automatically and need no helper renaming.

## How the template is organized

`template/configure.tex` loads the pieces in a fixed order, and that order is
a behavior contract, not a filing preference:

```text
1. template/command/     generic helpers, state, renderers (+ v1 adapter)
2. template/style/       base contract plus exactly one institution profile
3. conf/conf.tex         student data selects profile-owned catalogue entries
4. \FillInPDFData        PDF metadata and remaining initialization
```

Generic commands load first so profiles can call them. The selected profile
loads before student configuration so `conf/conf.tex` can use profile-owned
commands such as `\SetDeptCSIE`. Student data resolves before PDF metadata is
written.

`template/style/style.tex` selects exactly one registered profile:

- `base/` holds the profile contract and rendering hooks each profile fills in.
- `ncku/` owns NCKU geometry, wording, date policy, the watermark asset, and
  the preset catalogue: 9 colleges and 110 department slots covering
  departments, graduate institutes, degree programs, and centers, where each
  department preset also selects its college. The full source-checked
  catalogue is
  [`thesis/template/style/ncku/README.en.md`](../../thesis/template/style/ncku/README.en.md).
- `custom/` is a neutral, buildable skeleton for another institution. It loads
  the generic institution API — `\SetUniversityName{chi}{eng}`,
  `\SetCollName{chi}{eng}`,
  `\SetDeptName{chi}{English abbreviation}{English full name}` and their
  getters — and none of the NCKU catalogue, visible policy, dates, or assets.

Only the selected profile's data enters a build. An unchanged 1.x NCKU project
keeps its preset commands because `ncku` is still the default profile; a new
institution starts from `custom` and gives its own catalogue its own command
prefix instead of reusing NCKU `\SetDept...` names. The repository ships no
NTU profile; the named NTU walkthrough in
[`Customization.en.md`](../../thesis/template/style/Customization.en.md) is
API wiring, not a compliance implementation. Institution ports live under
`template/style/`; the template does not introduce `conf/style.tex`.

Public setters keep their signatures. Profiles change behavior through policy
hooks rather than by replacing raw metadata storage:

```text
SetOralDate       -> ApplyOralDatePolicy
SetCoverDate      -> ApplyCoverDatePolicy
SetOralChiDate    -> ApplyOralChiYearPolicy
SetCommitteeSize  -> ApplyCommitteeSizePolicy
```

This is how NCKU keeps its Taiwan-year cover dates and degree-specific
committee ranges (Master 3–5, Doctoral 5–9 from numeric degree state) while
generic and custom profiles stay Gregorian with the generic 2–9 committee
capacity.

## The compatibility contract

1.x never marked a reliable private API, so the baseline is deliberately
conservative: everything that was runtime-visible is protected, and removing
or changing any protected declaration is a later major-version decision with
its own migration contract.

- [`tests/100-v1-public-api.json`](../../tests/100-v1-public-api.json) pins
  597 runtime-visible LaTeX/xparse commands and environments plus 65 literal
  `\def`-style declarations, with complete audited argument shapes. It is
  generated only from the immutable pre-V2 commit
  `f80a2649232dd25761276ccf7043cf3f3a79e031`.
- [`tests/101-v1-comment-environment-artifacts.json`](../../tests/101-v1-comment-environment-artifacts.json)
  separately records 22 declarations that existed only inside runtime-dead
  LaTeX `comment` environments. They are scanner artifacts, not public APIs,
  and the checker refuses to regenerate the baseline from current V2 just to
  make a deletion pass.
- [`tests/102-v1-project-migration.json`](../../tests/102-v1-project-migration.json)
  pins 18 student-owned files (296,726 bytes) to immutable release
  `v1.8.2.260715154703`. The gate builds that unchanged entry point and
  configuration through the V2 adapter, base layer, and NCKU profile into the
  canonical 271-page A4 thesis, and a separate StudentMode run proves the
  active content and all three bibliography databases through exact `.fls`
  and `.blg` records. Files the historical configuration never loaded stay
  source-pinned without being misreported as runtime-loaded.

The pin deliberately sits on the live student files rather than on fixture
copies, so the packaged configuration keeps exactly the wording, defaults,
and comments that 1.x students already know; moving the pin onto test
fixtures to free those files for a rewrite was considered and declined on
2026-08-21.

The v1 adapter also keeps all 23 deprecated-command tombstones as literal
declarations with their exact diagnostics and `\stop` behavior, so a bounded
migration error can never turn into an undefined command. The active
one-argument `\RefTo{label}` remains a live helper; its historical
zero-argument tombstone is not revived.

## Fixed on purpose

Compatibility preserves APIs, not proven defects. Every correction keeps the
public name and argument shape, has a focused fixture, and retains integration
proof for unrelated NCKU output. The normative before/after table with
required user actions is in the
[migration guide](../v1-to-v2-migration.en.md#corrected-behaviors); it covers
stable subsubsection references, oral/Taiwan-year state separation, department
short-name storage and the DPS spelling, cover-date composition, profile-owned
committee ranges, theorem labels and caption `nameref` metadata, repeatable
numbering state, theorem counter-chain resolution with cycle diagnostics, and
custom font-type dispatch.

## Hardened internals

- **Key parsing.** Nineteen repository-owned command parser families moved
  from direct `pgfkeys` use to namespaced `l3keys` families in eleven
  independently validated slices, preserving defaults, expanded storage,
  omission sentinels, unknown-key hard failure, and public signatures. Active
  student source now has zero direct `\pgfkeys`/`\pgfkeysvalueof` parser
  references, zero `l3keys2e` references, and no explicit `pgfkeys` package
  load. PGF/TikZ did not disappear: `mdframed[framemethod=tikz]` still loads
  the visual stack transitively. Explicit `xparse` stays because protected
  public signatures use `G{...}` argument types the kernel interface does not
  provide.
- **Theorems.** One 21-row registry owns theorem order, style and numbering
  policy, defaults, membership, key parsing, and initialization; the literal
  public insertion and initializer wrappers remain compatibility adapters.
  Counter chains resolve forward and multi-hop references to a frozen terminal
  counter, and cyclic configurations fail with a deterministic package error
  instead of a recursion overflow. Title and label metadata are frozen so
  `\ref` and `\nameref` survive later parses.
- **Numbering.** Parsed title prefixes, separators, and counter names freeze
  at setup while counter values stay dynamic; general and appendix setup can
  be repeated idempotently instead of accumulating output.
- **Floats.** Figure, multi-figure, subfigure, and table captions freeze
  literal label text before writing auxiliary data, and one private helper
  owns the shared minipage/frame/opacity wrapper without changing public
  commands, forced `[H]` placement, compatibility no-op keys, or visible
  output.
- **Source scanner.** The API inventory scanner handles balanced TeX groups,
  optional defaults, parity-aware `%` comments, and `comment` environments.
  Only audited runtime-dead blocks were removed, and the separate artifact
  manifest preserves why the old count was wrong.

## Where V2 stops

The V2 modernization and the command-parser migration are complete, and
`docs/requirements/` holds no active promise. The following stay inactive
until a new owner-approved Intent opens them: a formal `nckuthesis.cls` or
broad class/package redesign, repository-wide `ifthen` conversion, broad
unrelated `expl3` rewriting, `l3build` replacing the current gate, engine
migration, and tagged-PDF or PDF/UA claims. Current output is not tagged.
Future work starts from measured need and a bounded compatibility fixture,
not from parser or package reference counts.

## Where the evidence lives

[Validation and performance](validation-and-performance.en.md) documents the
active gates, output-identity proof, and measured decisions;
[release and distribution](release-and-distribution.en.md) documents the
public package contracts.
