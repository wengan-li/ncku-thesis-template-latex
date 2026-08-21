# 01 — Human-first documentation and maintenance sweep

Owner-approved goal (2026-08-21): make the whole project read as written for
humans first while staying machine-verifiable; fix drifted teaching content and
small tooling gaps found in the full-repository review.

Intent boundaries:

- Every fact, contract, and gate survives; prose gets reorganized for a human
  reader, evidence moves behind the explanation instead of in front of it.
- Mixed English inside Chinese prose is acceptable in small amounts; fix only
  where switching harms readability. The historical bilingual root title and the
  gate-protected root README headings stay unchanged.
- Byte-pinned v1.8.2 student files (`thesis.tex`, `conf/conf.tex`, `context/`)
  stay byte-identical; no unpin in this todo.
- Validate each phase with the repository gates before moving on; visible-output
  changes additionally require a canonical rebuild and updated expectations.

## Phase 1 — Skill and agent-setup hygiene — DONE

- [x] List `unslop` in `.agents/skills/README.md` with a scope note: applies to
      conversational and commit prose; gate-checked public documentation keeps
      the repository third-person voice rules.
- [x] Add `unslop` to the repo-local skills list in `AGENTS.md`.
- Validation: `python3 scripts/test/check-bilingual-docs.py` PASS.

## Phase 2 — Template comment English sweep (output-neutral) — DONE

- [x] Fix the shared boilerplate header in 39 `thesis/template/**` files:
      "is hold at" → "is hosted at"; "in the hope of usefuling to someone" →
      "in the hope that it will be useful to someone".
- [x] Fix `thesis/template/configure.tex` comments: "Initinal all theorem
      formats" → "Initialize all theorem formats"; stray comment casing.
- [x] Keep the historical project title string (including its `LaTex` form)
      unchanged wherever it appears.
- [x] Do not touch byte-pinned files. (`\Initinal...` command name kept:
      renaming a declared helper is an API change, out of scope.)
- Validation: comment-only diff confirmed; migration manifest PASS; rebuild
  stays 271 A4 pages with identical diagnostics budget.

## Phase 3 — Gate and tooling gap fixes — DONE

- [x] `scripts/test/check-bilingual-docs.py`: accept `NN-slug.md` requirement
      files; the no-requirement state still demands exactly `.gitkeep`.
      Probed both directions (NN-slug accepted, stray rejected).
- [x] `scripts/overleaf/package-and-verify.sh`: enforce the documented 2 MB
      per-editable-text-file Overleaf limit.
- [x] `.github/workflows/test.yml`: upload `build/tests` fixture logs on
      failure.
- Validation: docs gate PASS; gallery package build + limits PASS
  (cold XeLaTeX 3.24 s); workflow YAML parses.

## Phase 4 — Feature records rewritten for humans

- [x] `docs/features/v2-modernization.en.md`: restructured as what → how it is
      organized → compatibility contract → fixed on purpose → hardened
      internals → boundary → evidence pointers. All facts and links kept.
- [x] `docs/features/validation-and-performance.en.md`: reframed with
      explanatory intros; `v2.0.2 production release read-back` anchor kept.
- [x] `docs/features/release-and-distribution.en.md`: reframed;
      `Draft and watermark policy` anchor kept.
- [x] The three Traditional-Chinese summaries rewritten as natural Chinese
      prose with 6–7 summary bullets each.
- [x] No checker relaxation was needed; the structural gate passed unchanged.
- Validation: docs gate PASS (8 guide pairs, 3 summary pairs, 479 links).

## Phase 5 — Migration guide refocused on students — DONE

- [x] Both guides restructured: student steps and the corrected-behavior table
      stay up front; the four evidence-heavy sections merged into one short
      "Compatibility evidence" section that points at the validation record
      (bbox/raster dumps removed from the student path).
- [x] `corrected-behaviors` anchor kept; topics metadata now 10 stable IDs in
      both files; fenced blocks identical across the pair.
- Validation: docs gate PASS (484 links).

## Phase 6 — AGENTS.md stale-content trim — DONE

- [x] Replaced the completed "Sample repository migration" checklist with a
      short outcome note pointing at the release-and-distribution record.
- Validation: docs gate PASS.

## Phase 7 — README parity nits — DONE

- [x] Root `README.md` now carries the official-guidance "last checked" date
      line that `README.en.md` already had.
- [x] `CONTRIBUTE` linked from both root READMEs.
- [x] Root README headings unchanged (owner decision).
- Validation: docs gate PASS.

## Phase 8 — Licence file in shipped packages

- [x] `thesis/LICENSE` added so the student ZIP carries licence text;
      student-archive required entries extended.
- [x] Examples ZIP packages `LICENSE`; allowlist verification and every
      documented contents listing (root READMEs, release record, AGENTS.md,
      repo-maintenance skill) updated together.
- [x] Student README (both languages) links its packaged `LICENSE`.
- [x] Validation: local clean-tree `just release dev` passed end-to-end
      (full gate, six PDFs, both ZIPs verified; LICENSE present in both).
      Phase marked DONE.

## Phase 9 — Teaching-example content refresh (visible output) — DONE

- [x] intro: Releases-first download guidance; "Mircosoft" fixed everywhere
      (nine occurrences across the example corpus).
- [x] source tree rewritten to the extracted student-package layout (with
      LICENSE) and the correct `CHANGELOG.md` name.
- [x] "Departmment of Photonics" teaching-table row fixed.
- [x] `LaTex`/`Latex`/`XeLatex`/`BibTex` swept to exact casing in example
      prose; historical project title untouched.
- [x] Rebuild stayed 271 A4 pages with an identical diagnostics budget, so no
      expectation updates were needed; pages 21, 23, and 55 rendered and
      inspected.
- Validation: final `just ci` run recorded in the status log.

## Phase 10 — Tooling and speed follow-ups

- [x] `justfile`: fixture-build mechanics shared through four private
      builder recipes (152 lines became 55); full gate green with every
      fixture rebuilt deterministically.
- [x] Release example PDFs build concurrently: cold segment 24.7 s -> 15.1 s
      on the reference host; `JUST_JOBS=1` restores serial execution.
- [x] CI TeX-container caching: measured and rejected. The image pull is
      about 79 s of a 3 m 51 s hosted Test job (run 32492812318), so a cache
      round trip for the multi-GB image saves nothing dependable; decision
      recorded in the validation record. A repository-owned slim pinned image
      would be a separate Intent.
- [ ] Owner decision pending: move the v1.8.2 byte-pin from the live student
      files to test fixtures so `conf/conf.tex` and starter content can be
      rewritten cleanly; flips `\ExampleMode` default. Large slice; separate
      Intent required.

## Status log

- 2026-08-21: todo created from full-repository review; baseline gate run
  started before any edit.
- 2026-08-21: baseline `just test` passed (129 PASS lines). Phases 1–9
  implemented and committed as nine slices on `feat/install-unslop-skill`;
  every slice validated (docs gate, migration manifest, gallery packaging,
  clean-tree `just release dev` end-to-end, canonical rebuild with rendered
  page inspection). Phase 10 items remain deferred pending separate
  validation or owner Intent.
- 2026-08-21: Phase 10 tooling items executed. Fixture-build dedupe validated
  by a full gate run; parallel release-PDF builds measured 24.7 s -> 15.1 s
  cold; TeX-container caching measured on hosted run 32492812318 and rejected
  (pull is about 79 s of a 3 m 51 s job). The byte-pin move stays the one
  open owner decision.
