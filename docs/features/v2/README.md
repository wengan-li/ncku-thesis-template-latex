# V2 Template Modernization

Status: shipped as [`v2.0.0.260717130231`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.0.260717130231) on 2026-07-17

V2 modernizes the XeLaTeX template while preserving the established NCKU output,
student project shape, and complete audited 1.x public API through the 2.x line.

## Product and compatibility records

- [`requirement.md`](requirement.md) — completed product requirement.
- [`modernization.md`](modernization.md) — IDSD intent, expectations, context, and
  final evidence.
- [`public-api-compatibility.md`](public-api-compatibility.md) — declaration,
  adapter, and unchanged-project contracts.
- [`../../MIGRATION-1.x-TO-2.x.md`](../../MIGRATION-1.x-TO-2.x.md) — user and
  maintainer migration guide.

## Completed implementation records

- [`deprecated-command-compatibility.md`](deprecated-command-compatibility.md)
- [`api-manifest-hardening.md`](api-manifest-hardening.md)
- [`theorem-hardening.md`](theorem-hardening.md)
- [`float-hardening.md`](float-hardening.md)
- [`numbering-hardening.md`](numbering-hardening.md)
- [`full-review-repairs.md`](full-review-repairs.md)
- [`super-optimization.md`](super-optimization.md)
- [`expl3-internals.md`](expl3-internals.md) — bounded post-release internal
  modernization with ten output-neutral implementation slices.
- [`pgfkeys-replacement-landscape-2026-07.md`](pgfkeys-replacement-landscape-2026-07.md)
  — dated official-source comparison of `l3keys`, kernel key options,
  `expkv-bundle`, retained PGF/TikZ `pgfkeys`, and deprecated `l3keys2e`.

## Current machine-checked contracts

The durable behavior remains enforced by the repository source and tests,
including `tests/v1-public-api.json`, `tests/v1-project-migration.json`, focused
TeX fixtures, the exact-tree student archive gate, and `just ci`.
