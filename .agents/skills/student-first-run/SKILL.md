---
name: student-first-run
description: Design every student-facing change from the viewpoint of a graduate student meeting this repository for the first time. Load before touching READMEs, conf/context skeletons, the teaching example, release notes, or the Overleaf package.
---

# Student First Run

## When to Use

Load this skill before changing anything a student sees before their first
successful build:

- `README.md` / `README.en.md` at the repository root
- `thesis/README.md`, `thesis/conf/README.md`, and their English companions
- `thesis/conf/conf.tex` comments, `thesis/context/**` placeholders (both are
  byte-pinned; see below), and `thesis/template/style/ncku/README.md`
- `thesis/example/how-to/**` and the other teaching chapters
- GitHub Release notes, `CHANGELOG.md`, `CHANGELOG.en.md`
- the Overleaf package and its quick start
- any default value in `thesis/conf/conf.tex` or `thesis/context/context.tex`
  that a new thesis would inherit

Load [`idsd-workflow`](../idsd-workflow/SKILL.md) first as usual, and
[`documentation-management`](../documentation-management/SKILL.md) for pair,
voice, and lifecycle rules. This skill adds the audience lens those two do not
check.

## The Lens

Before writing, walk the path a student actually takes and read what they read,
in order:

1. GitHub repository page (`README.md`, repository description, topics)
2. Releases page (release notes, asset names)
3. Unzipped package (`README.md`, `LICENSE`, the directory tree)
4. `conf/conf.tex` with `conf/README.md` beside it
5. `context/context.tex` and the chapter placeholders
6. First build: Overleaf, a terminal, or Texmaker/TeXstudio
7. First own-thesis build after turning `\ExampleMode` off
8. Submission: certificate page, cover PDF for printing, ETDS upload

At every step ask three questions: What must the student change here? Where
exactly? What happens if they do not? A page that cannot answer those for its
step is not finished.

## Rules

1. **The student path carries no maintainer mechanics.** Byte pins, migration
   hashes, profile architecture, regression evidence, immutable source
   revisions, and gate names belong in `docs/features/`. An NCKU student never
   needs the word "profile"; students from other institutions get one sentence
   and a link to `thesis/template/style/Customization.md`.
2. **Every shipped default that prints wrong data is listed with its line and
   consequence.** `thesis/conf/conf.tex` is byte-pinned to v1.8.2, so its line
   numbers are stable and may be cited. The shipped file enables
   `\ExampleMode`, selects `\PhdDegree`, dates the oral exam 2023-12-31, sets
   three placeholder advisors that the cover prints whenever non-empty, and
   enables `\DisplayOralImage` with the file names commented out. The
   must-change table in `thesis/README.md` owns that list; update it when a
   default or its effect changes.
3. **Fix the experience around pinned files, never inside them.** Typos and
   placeholders in `thesis/conf/conf.tex`, `thesis/thesis.tex`, and
   `thesis/context/**` are recorded, not edited, unless the owner moves the pin
   (`tests/102-v1-project-migration.json`).
4. **Every known failure gets an entry in the common-errors section** of
   `thesis/README.md` with the exact message a student sees, the cause, and the
   fix. When an issue or a session uncovers a new one, add it in the same
   slice.
5. **Wherever a build command appears, all three paths appear**: Overleaf,
   terminal, editor. A command alone assumes a terminal user.
6. **Release notes speak to students.** They say which ZIP to download and what
   changed in plain words, in both languages, generated from the changelog
   entries by `scripts/release/release-notes.py`. A release version without a
   changelog entry must not build.
7. **Consequences before features.** Explain what a student gets and what goes
   wrong before explaining how the mechanism works. Word analogies (`.tex` is to
   LaTeX what `.doc` is to Word) are welcome on the student path.
8. **One predominant language per page, student first.** Keep the pair rules
   from `AGENTS.md`; a new section exists in both languages of a guide pair in
   the same commit, with the topic list updated on both sides.
9. **Official rules win, and the template says so where it matters**: next to
   the certificate, the cover date, the abstracts, and the upload steps, not
   only in a disclaimer at the top.

## Review Checklist

Run through this before opening a pull request that touches the student path:

- Does the first screen of the changed page tell a new student what to do next?
- Could a student with only `thesis/README.md` and `conf/README.md` produce a
  correct cover on the first own build? If a default still leaks through, is it
  in the must-change table?
- Is there any sentence a student would have to skip because it is about how
  the repository is maintained?
- Does every new error path have a common-errors entry?
- Does the change keep the Overleaf, terminal, and editor paths in step?
- Are both languages of every touched pair updated, with identical code blocks?
- For teaching-example text: was the corrected sentence confirmed with
  `pdftotext build/thesis.pdf -`, and does `just release dev` still pass with
  the teaching-document page count pinned in `justfile`?

## Evidence

- Walk-through findings and the P0/P1/P2 backlog: `todos/02-student-first-run.md`
  while active; afterwards the owning feature record under `docs/features/`.
- Shipped-default facts: `thesis/conf/conf.tex`,
  `thesis/template/cover/cover-chi.tex`, `thesis/template/style/ncku/ncku.tex`.
- Gates: `python3 scripts/test/check-bilingual-docs.py`, `just ci`,
  `just release dev`.
