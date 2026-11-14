---
name: ncku-thesis-writing
description: Write or revise student thesis content using the NCKU template helpers, with source-backed chapter, float, equation and BibTeX guidance.
---

# NCKU thesis writing

Use for student writing tasks in a matching XeLaTeX thesis project. Start from the requested change and supplied research material. Preserve existing claims, labels, bibliography and unrelated content. Missing data, images or citation metadata must be reported, never invented.

## Find the project

Start from the requested content file or directory and inspect that path and its ancestors for `thesis.tex`, `conf/` and `template/configure.tex` together. For a relative target, resolve it from the working directory. If no target was supplied, inspect the working directory and its ancestors. That directory is the student project root. When starting at a verified repository root, also consider only its `thesis/` child, and accept it only when all three runtime markers exist. Verify a repository root with `git rev-parse --show-toplevel` when Git is available; do not recursively search unrelated children. An explicit orphan target must not attach to an unrelated runtime just because the working directory is a repository. A copied `context/` is content and instructions only. If no matching runtime exists, report: "A matching complete thesis template containing thesis.tex, conf/ and template/configure.tex is required." Do not fabricate the runtime.

Check the existing configuration and content assembly before editing. The default enables `\ExampleMode`; own-thesis mode uses the student's `context/context.tex`. Do not change `thesis.tex`, template internals, engine, bibliography system or institutional style during ordinary writing. Change student configuration only when the requested task needs it.

## Load only the needed reference

The English human usage guides own the exact examples. Load only the relevant page; do not duplicate the handbook here.

| Task | English usage guide |
| --- | --- |
| Own thesis, chapters, text, front matter and appendices | [Project and chapters](../../../usage/project-and-chapters.en.md) |
| Supplied images, captions, tables and labels | [Figures and tables](../../../usage/figures-and-tables.en.md) |
| Equations, theorem statements and proofs | [Equations and theorems](../../../usage/equations-and-theorems.en.md) |
| Citation keys and BibTeX files | [References and bibliography](../../../usage/references-and-bibliography.en.md) |
| Compilation and error recovery | [Build and diagnostics](../../../usage/build-and-diagnostics.en.md) |

## Complete the requested edit

Use the exact optional/braced syntax in the relevant reference. Paths are relative to the student project root. Reuse supplied labels and citation keys; detect collisions before adding new ones. Edit requested student content only. Do not invent experimental results, sources or successful compilation.

Build when tools are available, inspect the final log for unresolved citations/references and rerun requests, and report the actual command, result and changed files. If compilation cannot run, state the missing tool or runtime. File editing alone is not build success.

Current university and department rules override this community template. Use university-system certificate files; do not create an official certificate or imply institutional endorsement. Writing tasks do not authorize installation, permission changes, hooks, client settings, Git publication, network upload or account access.
