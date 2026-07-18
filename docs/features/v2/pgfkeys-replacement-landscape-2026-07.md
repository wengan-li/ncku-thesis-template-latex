# `pgfkeys` Replacement Landscape — 2026-07-18

## Question

What should replace `pgfkeys` in a modern LaTeX template, and when should it
remain?

There is no single drop-in winner for every use. Select by interface role:
ordinary LaTeX command/configuration keys, package/class options, fully
expandable or cross-format parsing, or PGF/TikZ-native style trees.

## Current primary-source snapshot

- [`l3kernel`](https://ctan.org/pkg/l3kernel) is the LaTeX Project's supported
  programming layer. CTAN reports version/release `2026-06-18`; the matching
  [`interface3`](https://mirrors.ctan.org/macros/latex/required/l3kernel/interface3.pdf)
  documents `l3keys`, including key definition/setting, value expansion,
  unknown-key handling, selective setting, and precompilation.
- The LaTeX Project's
  [`clsguide`](https://mirrors.ctan.org/macros/latex/base/clsguide.pdf), dated
  `2025-12-06`, recommends the key-value option system for new classes and
  packages. Kernel key/value option handling requires LaTeX `2022-06-01` or
  newer.
- [`l3keys2e`](https://ctan.org/pkg/l3keys2e) explicitly says it is deprecated
  in favor of methods integrated into the LaTeX kernel from `2022-06-01`.
- [`expkv-bundle`](https://ctan.org/pkg/expkv-bundle) is version `2024-12-26`.
  Its official documentation describes a fully expandable parser, robustness
  for active commas/equals signs and brace preservation, `expkv-def` for rich
  key definitions, `expkv-cs` for expandable key-value macros, and `expkv-opt`
  for class/package options.
- [`pgf`](https://ctan.org/pkg/pgf) is still maintained, at version `3.1.11a`
  dated `2025-08-29`. `pgfkeys` remains PGF's tree-oriented key management
  system and is not abandoned merely because its standalone CTAN record shows
  an old component date.
- [`keyval`](https://ctan.org/pkg/keyval) remains current as required LaTeX
  infrastructure (`1.15`, `2026-05-17`) but is the original minimal decoder,
  not the preferred architecture for a new rich configuration layer.
- [`kvoptions`](https://ctan.org/pkg/kvoptions) is `3.15` (`2022-06-15`), while
  [`xkeyval`](https://ctan.org/pkg/xkeyval) remains maintained as an extension
  of `keyval`. Both are compatibility/ecosystem tools rather than the default
  modernization target when current kernel `l3keys` is already available.
- [`ltxkeys`](https://ctan.org/pkg/ltxkeys) last shows version `0.0.3c` and a
  2012 update. It should not be selected as the modern replacement here.

## Decision matrix

### 1. Ordinary LaTeX command and internal configuration keys

**Default recommendation: `l3keys`.**

Why:

- maintained by the LaTeX Project and shipped in the current programming layer;
- no extra parser dependency for a modern LaTeX template already using `expl3`;
- typed properties, namespaced modules, choices, unknown-key handling, usage
  scopes, and explicit expansion/storage controls;
- fits the NCKU migration's proven `.estore in` to `.tl_set_e:N` mapping.

This is the correct target for isolated NCKU command parsers whose complete
semantics can first be frozen under the legacy implementation.

### 2. New class or package options

**Use the kernel `\DeclareKeys`, `\ProcessKeyOptions`, and `\SetKeys` surface,
backed by `l3keys`.**

The current `clsguide` says `\DeclareKeys` creates namespaced key options and
can use the full range of `l3keys` properties; `\ProcessKeyOptions` processes the
current class/package option list and should appear only once; `\SetKeys` applies
explicit settings before or after option processing.

Do not add `l3keys2e` for a template whose supported LaTeX baseline is
`2022-06-01` or newer: the package is deprecated because this integration is in
the kernel. Pin the required LaTeX date when publishing a class/package that
relies on it.

### 3. Fully expandable, cross-format, or parser-performance-sensitive code

**Evaluate `expkv-bundle`; do not adopt it by fashion.**

It is the strongest current specialist alternative when the requirement is a
fully expandable parser, plain TeX/LaTeX/ConTeXt portability, active comma/equal
robustness, or measured parser cost. Its subpackages cover rich definitions,
expandable macros, and package options.

For NCKU today, it would add a second modern key system without a demonstrated
need. Benchmark and build a semantic fixture before considering it; speed or
expandability claims alone do not justify replacing already-working `l3keys`.

### 4. PGF/TikZ-native style trees and handlers

**Keep `pgfkeys` when the interface is genuinely PGF/TikZ-native.**

`pgfkeys` provides tree-like paths and PGF handler conventions. `l3keys` is a
modern LaTeX configuration interface, not a mechanical drop-in for every PGF
style tree. If TikZ/PGF remains active, removing direct template use may still
not remove `pgfkeys` from the runtime `.fls` graph.

### 5. Legacy compatibility

Keep `keyval`, `xkeyval`, or `kvoptions` only where a public API, upstream
package, or old format baseline requires them. Replacing `pgfkeys` with another
legacy key package is churn, not modernization.

## NCKU-specific evidence and judgement

1. Four isolated command families now use `l3keys`: single figure, single table,
   theorem content, and reference setup. Each migration first froze the legacy
   parser contract and then proved canonical output identity.
2. `SetupReference` preserves its default/custom/repeated setup, rendered BibTeX
   output, unknown-key failure, and `apacite[notocbib]` preamble side effect.
3. Active student source contains zero `l3keys2e` references, and generated
   runtime `.fls` files contain zero `l3keys2e` loads. The command-level parsers
   use `l3keys` directly and do not need the deprecated option bridge.
4. Keep the top-level/nested multi-figure parser deferred until both shared
   scratch state and all row-dispatch routes are covered.
5. Keep dynamic theorem-format/counter families deferred; they are not the same
   state machine as theorem-content `title`/`label` parsing.
6. Do not claim package removal while 46 direct `pgfkeys`/`pgfkeysvalueof`
   references remain across four files or while PGF/TikZ keeps `pgfkeys` active
   transitively.
7. Continue requiring focused semantic checks, full text/normalized bbox/fonts,
   all-page fixed-DPI raster identity, exact-HEAD archive verification, extracted
   student ZIP direct build, and exact-SHA hosted checks.

For this repository, `l3keys` is the best-fit default because it is official,
current, already loaded, and has passed four independently reversible,
output-neutral family migrations. `expkv-bundle` is a credible modern
alternative, but it solves a more specialized expandability and cross-format
problem that NCKU has not demonstrated. `pgfkeys` should be reduced where it is
only acting as a generic command parser, not purged where PGF/TikZ semantics or
transitive dependencies make it the natural implementation.

The modernization goal is therefore **interface consolidation and frozen
semantics**, not maximizing the number of removed library names.
