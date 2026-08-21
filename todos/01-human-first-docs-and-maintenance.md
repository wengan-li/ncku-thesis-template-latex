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

## Phase 5 — Migration guide refocused on students

- [ ] `docs/v1-to-v2-migration.md` + `.en.md`: keep student steps (backup,
      replace, build, compare) and the corrected-behavior table; compress
      maintainer evidence (declaration counts, bbox words, raster identity)
      into a short pointer to the validation record.
- [ ] Keep the `corrected-behaviors` anchor used by the V2 feature record; keep
      paired topics metadata, H2 counts, and identical fenced blocks.
- Validation: `python3 scripts/test/check-bilingual-docs.py`.

## Phase 6 — AGENTS.md stale-content trim

- [ ] Replace the completed "Sample repository migration" checklist with a
      two-line completion note pointing at the release-and-distribution record
      (the sample repository was deleted 2026-07-12).
- Validation: `python3 scripts/test/check-bilingual-docs.py`.

## Phase 7 — README parity nits

- [ ] Root `README.md`: add the official-guidance "last checked" date line that
      `README.en.md` already carries.
- [ ] Link `CONTRIBUTE` from both root READMEs so the contributor list is
      reachable.
- [ ] Root README headings stay as-is (owner decision).
- Validation: `python3 scripts/test/check-bilingual-docs.py`.

## Phase 8 — Licence file in shipped packages

- [ ] Add a `LICENSE` copy under `thesis/` so the student ZIP carries licence
      text (CC BY-NC-SA redistribution); extend the student-archive required
      entries.
- [ ] Include `LICENSE` in the examples ZIP and extend the examples allowlist
      verification.
- Validation: `just test` (student-archive and release-verifier fixtures),
  plus a local `just release dev-check` if needed.

## Phase 9 — Teaching-example content refresh (visible output)

- [ ] `thesis/example/how-to/use/intro/intro.tex`: fix "Mircosoft"; describe
      the current GitHub Releases download path instead of the front-page
      Download ZIP flow.
- [ ] `thesis/example/how-to/use/source-tree.tex`: correct `ChangeLog.md` →
      `CHANGELOG.md`; describe the extracted student-package layout instead of
      a repository tree with files the package does not contain.
- [ ] `thesis/example/how-to/use/conf.tex`: fix the stale
      "Departmment of Photonics" teaching-table row.
- [ ] Sweep `LaTex` → `LaTeX` in example prose except the historical project
      title.
- [ ] Rebuild the canonical document; if the page count moves from 271, update
      the `justfile` expectations and every documentation reference in the same
      change.
- Validation: `just test`, `just ci`, `pdfinfo build/thesis.pdf`, rendered
  inspection of changed teaching pages.

## Phase 10 — Deferred candidates (need separate validation)

- [ ] `justfile`: generalize repetitive fixture recipes (pure tooling).
- [ ] Parallelize the five sequential release example-PDF builds.
- [ ] CI TeX container caching or a smaller pinned scheme (needs hosted-run
      experiments; the container pull dominates hosted time).
- [ ] Owner decision pending: move the v1.8.2 byte-pin from the live student
      files to test fixtures so `conf/conf.tex` and starter content can be
      rewritten cleanly; flips `\ExampleMode` default. Large slice; separate
      Intent required.

## Status log

- 2026-08-21: todo created from full-repository review; baseline gate run
  started before any edit.
