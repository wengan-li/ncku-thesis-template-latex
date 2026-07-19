---
id: "02"
title: Bilingual documentation for Traditional Chinese and English readers
status: active
owner: Leon Li
created: 2026-07-19
implementation_plan: ../../todos/01-bilingual-documentation.md
---

# Bilingual documentation for Traditional Chinese and English readers

## Intent

Make the NCKU Thesis Template independently usable by Traditional-Chinese and
English readers without conflating document language, institution profile,
degree type, or example/content mode.

A student must be able to discover, configure, build, migrate, and prepare a
submission from the documentation in either supported language. A maintainer
must be able to understand the shipped architecture and evidence without
maintaining two drifting copies of every technical record.

## Confirmed documentation model

Use a hybrid bilingual model:

1. Public and student-facing instructions are complete in formal Taiwan
   Traditional Chinese (`zh-Hant-TW`) and natural technical English.
2. User-facing sections place the two language blocks together and share paths,
   commands, code blocks, and links.
3. Maintainer feature records provide a Traditional-Chinese executive summary
   followed by the complete English technical body.
4. Internal identifiers, LaTeX macros, paths, logs, API names, and commands are
   never translated.
5. Neither prose language overrides source. Current source, tests, scripts, and
   immutable release evidence remain authoritative on drift.

## Independent configuration axes

Documentation must never imply that Taiwanese users select one profile and
international users select another. It must teach these independent axes:

| Axis | Supported choices |
| --- | --- |
| Documentation language | Traditional Chinese, English |
| Institution profile | `ncku`, another maintained profile such as `custom` |
| Cover language | `\DisplayCoverInChi`, `\DisplayCoverInEng` |
| Degree | `\MasterDegree`, `\PhdDegree` |
| Content mode | own thesis content, `\ExampleMode` teaching example |

Examples must include an English-reading NCKU student and a Chinese-reading
non-NCKU maintainer so that language and institution cannot be mistaken for the
same decision.

## In scope

- establish the language, terminology, formatting, and parity policy;
- rewrite the root `README.md` as a concise bilingual public landing page;
- make `thesis/README.md` a complete bilingual offline student guide;
- add a complete bilingual companion guide under `thesis/conf/` while preserving
  the byte-pinned `thesis/conf/conf.tex`;
- make `docs/v1-to-v2-migration.md` fully usable in either language;
- make `thesis/template/style/Customization.md` fully usable in either language;
- make `docs/README.md` a bilingual audience and task router;
- add Traditional-Chinese executive summaries to the three current maintainer
  feature records;
- define a bilingual format for current/future changelog entries without
  retro-translating every historical 1.x entry;
- update first-party links, package verification, and documentation policy;
- add deterministic structural checks that detect missing language sections,
  incorrect product casing, selected Cantonese-only wording, and stale links;
- verify the exact staged tree, release packages, direct student build, and
  unchanged canonical PDF output.

## Explicitly out of scope

- changing LaTeX macro behavior, defaults, argument signatures, or profile
  selection;
- modifying any of the 18 byte-pinned v1.8.2 student inputs;
- translating runtime `\errmessage` diagnostics in this documentation slice;
- translating all 271 pages of the teaching corpus;
- translating internal source comments that are not part of a student workflow;
- changing release version, tag, GitHub Release, or Overleaf Gallery state;
- publishing, pushing, opening a PR, merging, or releasing without a separate
  owner instruction.

## Compatibility boundary

`thesis/conf/conf.tex` is pinned by `tests/v1-project-migration.json` to the
immutable v1.8.2 release:

```text
path:   thesis/conf/conf.tex
size:   24780 bytes
sha256: ca7232190705e4dbc6ff1f6fe2613c0ce1cfdb6dcd6486ee15df6a07b195b4e0
source: v1.8.2.260715154703
commit: 2c9557a74983023bba7a8f0cf233e1eb812edec7
```

The bilingual solution must therefore add a packaged companion guide and link
to it; it must not rewrite comments in `conf.tex` during 2.x.

## Acceptance scenarios

1. A Traditional-Chinese NCKU student can download the student ZIP, disable
   `\ExampleMode`, select the cover language and degree, enter metadata, build,
   and follow final-submission warnings without requiring English prose.
2. An English-reading NCKU student can complete the same journey without
   requiring Chinese prose.
3. A Traditional-Chinese non-NCKU maintainer can understand that institution
   profile selection is independent of language and can start from `custom`.
4. An English-reading non-NCKU maintainer can complete the same profile journey.
5. A 1.x user can follow compatibility-first and native-v2 migration paths in
   either language with identical commands and safety warnings.
6. A maintainer can locate architecture, validation, release, and Overleaf
   evidence through a bilingual index and Chinese summaries without duplicating
   the technical evidence body.
7. The versioned student ZIP contains all bilingual student instructions and
   builds directly with the documented XeLaTeX/latexmk command.

## Failure conditions

The requirement is not complete if any of the following is true:

- either language cannot complete a student quick-start or migration journey;
- documentation equates English with non-NCKU or Chinese with NCKU;
- paired language blocks contain different commands, paths, defaults, warnings,
  release facts, or acceptance claims;
- a targeted public/student surface retains unexplained Cantonese-only prose or
  inconsistent `LaTex`/`XeLatex` casing;
- `thesis/conf/conf.tex` changes or its pinned hash changes;
- bilingual work changes the canonical PDF, page count, paper size, text,
  bounding boxes, fonts, or raster output;
- a student package omits the bilingual configuration guide;
- links or package verifiers still expect removed/old paths;
- a requirement is marked complete before exact staged-tree validation passes.

## Recovery

Changes must be grouped into reviewable local commits. If a slice fails semantic
review or build validation, revert only that slice, keep this requirement and its
todo active, and restore the last verified documentation state. Do not weaken
compatibility manifests, package checks, or output gates to make translation work
pass.

## Linked plan

Detailed sequence, file matrix, terminology, review checkpoints, test commands,
and completion evidence are maintained in
[`todos/01-bilingual-documentation.md`](../../todos/01-bilingual-documentation.md).
