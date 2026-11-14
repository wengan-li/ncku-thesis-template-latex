---
name: ncku-thesis-writing
description: Write or revise student thesis content using the NCKU template helpers, with source-backed chapter, float, equation and BibTeX guidance.
---

# NCKU thesis writing

Use for student writing tasks in a matching XeLaTeX thesis project. Start from the requested change and supplied research material. Preserve existing claims, labels, bibliography and unrelated content. Missing data, images or citation metadata must be reported, never invented.

## Find the project

Start from the requested content file or directory and inspect that path and its ancestors for `thesis.tex`, `conf/` and `template/configure.tex` together. For a relative target, resolve it from the working directory. If no target was supplied, inspect the working directory and its ancestors. That directory is the student project root. When starting at a verified repository root, also consider only its `thesis/` child, and accept it only when all three runtime markers exist. Verify a repository root with `git rev-parse --show-toplevel` when Git is available; do not recursively search unrelated children. An explicit orphan target must not attach to an unrelated runtime just because the working directory is a repository. A copied `context/` contains student content only; it carries neither this project-root skill nor the template runtime. If no matching runtime exists, report: "A matching complete thesis template containing thesis.tex, conf/ and template/configure.tex is required." Do not fabricate the runtime.

Copy the entire buildable project, including hidden `.agents/`, `.claude/` and relative aliases. The Claude skill alias `.claude/skills -> ../.agents/skills` exposes the same canonical skill. Explicitly read SKILL.md when the client does not discover it; alias resolution does not prove automatic invocation. Build from the directory containing thesis.tex.

Check the existing configuration and content assembly before editing. The default enables `\ExampleMode`; own-thesis mode uses the student's `context/context.tex`. Do not change `thesis.tex`, template internals, engine, bibliography system or institutional style during ordinary writing. Change student configuration only when the requested task needs it.

## Use the shared teaching reference

Read only the relevant section of [template-usage.md](references/template-usage.md). It is generated from the same code blocks used by the teaching document. Do not maintain a second handbook or edit the generated file. The full human tutorial remains in the teaching sources/PDF; the portable reference remains usable when that corpus is absent.

The reference covers chapter/section shapes, front matter, appendices, lists, single/multiple figures, tables, equations, theorem/proof wrappers, references, a real BibTeX entry, database registration and the direct build command. Its titles/labels are illustrative. Preserve existing user labels or choose unique ones, then update every matching reference. Demo entries belong in a thesis only when its research actually cites them.

## Apply the requested change

- For own-thesis writing, comment out the active \ExampleMode in conf/conf.tex when the task calls for switching modes. Otherwise it compiles the teaching document. Keep the student's data and remaining settings.
- Write a new chapter under context/, pair the chapter opening/closing commands, and add its input in context/context.tex before the bibliography. Order input lines to order chapters. Preserve enabled abstract/acknowledgment/nomenclature wrappers and choose their existing language files. Appendices follow the bibliography; ending an appendix does not restore ordinary chapter mode.
- Supply image files first. Paths are relative to the project root, even when authoring a nested chapter. Replace the reference's figure.png with the actual supplied asset path. Put captions with commas in braces, pair labels with numbered captions, and check that figures fit.
- Keep optional/braced syntax exactly as shown. Chapter/section and equation labels use optional braced arguments. Figure pos/align and multi/subfigure align are accepted compatibility keys without placement/alignment effects. Table pos changes caption order, while these floats retain forced [H] placement.
- Put supplied, verified BibTeX metadata in an already registered database under context/references/. Preserve citation keys, reject duplicates and check registration before adding another database. Keep the existing BibTeX style/system. Do not invent authors, dates, DOIs, data or experimental results.

## Validate and recover

Run the reference's direct latexmk command from the matching project root when tools are available. Overleaf uses XeLaTeX with thesis.tex as the main document; editors use the same root and a XeLaTeX/BibTeX latexmk chain. Do not install missing tools or change global settings as part of writing.

Start with the first actual error in the log:

| Error or symptom | Check and recovery |
| --- | --- |
| File ... not found | Root directory, relative path, letter case and extension; request a missing asset |
| Undefined control sequence | Spelling, supported XeLaTeX engine and matching template runtime |
| Missing $ inserted | Unescaped text underscores or an incorrect math boundary |
| Citation ... undefined | Exact key, registered database and BibTeX convergence |
| I couldn't open database file | Registered database path, without guessing another source |
| Unknown option/key | Supported helper options and spelling; do not patch template internals |
| Teaching output instead of own content | Active ExampleMode and context assembly |
| Broken copied instructions | Restore the complete hidden payload and relative aliases |

A PDF alone is insufficient. Require PDF and SyncTeX, no undefined citations/references or rerun requests in the final log, and expected text/captions/references/bibliography in the PDF. Inspect affected pages for clipping and pagination. For stale auxiliary state or a requested bibliography-style change, clean generated intermediates with latexmk and rebuild; do not delete student input. Preserve the last buildable thesis and reapply a failed edit in small steps.

Report actual changed files, command and result, or the exact unavailable tool/runtime. File editing alone is not build success. Current university/department rules override the community template. Use university-system certificate files; never create an official certificate or imply endorsement. Writing does not authorize installations, permissions, hooks, client/MCP settings, Git publication, uploads or account access.
