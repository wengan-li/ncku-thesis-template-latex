<!-- doc-pair: maintainer-index; lang: en; topics: start-here,directory-model,bilingual-policy,documentation-lifecycle,source-of-truth-order,current-state -->

[繁體中文](README.md) | [English](README.en.md)

# Maintainer documentation

Current production release: [`v2.0.1.260719010734`](https://github.com/wengan-li/ncku-thesis-template-latex/releases/tag/v2.0.1.260719010734)

## Start here

This directory contains maintainer documentation for the released NCKU thesis template. Students start from the packaged `thesis/README.en.md` and `thesis/conf/README.en.md`; this directory owns migration, architecture, validation, release, and Overleaf records. Root `README.en.md` is the English public router, not the maintainer runbook.

| Audience or task | Canonical document |
| --- | --- |
| Student build/edit | [`thesis/README.en.md`](../thesis/README.en.md) |
| Student configuration | [`thesis/conf/README.en.md`](../thesis/conf/README.en.md) |
| 1.x to 2.x migration | [`v1-to-v2-migration.en.md`](v1-to-v2-migration.en.md) |
| V2 architecture | [`features/v2-modernization.md`](features/v2-modernization.md) |
| Tests/output/performance | [`features/validation-and-performance.md`](features/validation-and-performance.md) |
| Release/Overleaf | [`features/release-and-distribution.md`](features/release-and-distribution.md) |
| Version history | [`CHANGELOG.md`](../CHANGELOG.md) |

## Directory model

User journeys use one file per language with a text language switcher to the equivalent page. Each maintainer feature has a canonical English technical record and a separate Traditional-Chinese executive-summary companion, so hashes, run IDs, and benchmarks are not duplicated. Active requirements store only owner-approved what/why promises and active todos store implementation progress; both are removed after durable knowledge is consolidated.

```text
docs/
  README.md
  README.en.md
  v1-to-v2-migration.md
  v1-to-v2-migration.en.md
  features/
    README.md
    README.en.md
    v2-modernization.md
    v2-modernization.zh-TW.md
    validation-and-performance.md
    validation-and-performance.zh-TW.md
    release-and-distribution.md
    release-and-distribution.zh-TW.md
  requirements/
    .gitkeep
```

Git history keeps per-branch checklists, superseded plans, and detailed chronology.

## Bilingual policy

Public and student-facing content uses formal Taiwan Traditional Chinese (`zh-Hant-TW`) and natural technical English. Each document has one predominant language and a top-of-page `繁體中文 | English` text switcher to an equivalent page with the same stable topic IDs; flags are not used. Pair metadata is hidden when rendered, and the checker requires shared code blocks to stay identical. Documentation language, institution profile, cover language, degree, and content mode remain independent. New Chinese prose uses `論文範本`; product names retain exact `LaTeX`, `XeLaTeX`, `BibTeX`, `latexmk`, and `SyncTeX` casing.

This follows W3C localized-page linking, the USWDS top language-selector pattern, GitHub's locale-specific documentation model, and WCAG's predominant-page-language principle. The mechanical checker proves only pair topics, switchers, links, shared code, casing, and selected terminology. Semantic translation parity remains a manual review gate.

Run:

```bash
python3 scripts/test/check-bilingual-docs.py
```

## Documentation lifecycle

1. Start from an owner-approved Intent.
2. Create `docs/requirements/<NN>-<slug>.md` only while a real promise is active.
3. Track implementation in `todos/<NN>-<slug>.md` and keep backlinks synchronized.
4. When work ships, update every user surface and the owning topical feature record.
5. Remove the completed requirement and todo; do not keep an active document per branch, commit, parser, or bugfix.
6. When no requirement is active, retain only `.gitkeep` under `docs/requirements/`.

No requirement is currently active; `docs/requirements/` contains only `.gitkeep`.

## Source-of-truth order

On drift, resolve facts in this order: current tracked source/tests/scripts/`justfile`; immutable release tag and publicly re-downloaded assets; current documentation; historical Git evidence. History explains decisions but does not override current tested behavior or automatically reopen deferred work.

```text
source and deterministic tests
-> immutable public release evidence
-> current user/maintainer documentation
-> historical commits, PRs, and removed notes
```

## Current state

The production source line is V2 with XeLaTeX and a direct `latexmk` student build. The latest immutable release is `v2.0.1.260719010734`. `main` is the only persistent development branch and work uses short-lived `feat/<short-name>` branches. GitHub Releases remains canonical for the latest package until the Overleaf update is approved and publicly read back.

No requirement is currently active. Completed implementation chronology remains in Git history.
