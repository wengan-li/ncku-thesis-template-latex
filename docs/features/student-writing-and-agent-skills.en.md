<!-- language: en; summary: student-writing-and-agent-skills.md -->

[繁體中文摘要](student-writing-and-agent-skills.md) | [English technical record](student-writing-and-agent-skills.en.md)

# Student writing and portable agent skills

Students and agents use one set of writing knowledge under `thesis/context/`. The [human writing entry](../../thesis/context/README.en.md) routes to task guides; the single [agent skill](../../thesis/context/.agents/skills/ncku-thesis-writing/SKILL.md) loads only the relevant English guide. These descriptions apply to current source. Published package availability is determined by [GitHub Releases](https://github.com/wengan-li/ncku-thesis-template-latex/releases).

## Knowledge and language ownership

`thesis/context/usage/` owns paired Traditional-Chinese and English guides, including executable examples. Agent-facing AGENTS.md, SKILL.md and any skill sidecars use English only, without language switchers. The skill does not duplicate an English handbook inside `.agents/`.

| Task | Human English guide under context/usage/ | Runtime owner under template/command/ |
| --- | --- | --- |
| Own thesis, chapters, text, front matter, appendices | project-and-chapters.en.md | cmd-thesis, cmd-chapter, cmd-abstract, cmd-acknowledgments, cmd-nomenclature, cmd-appendix |
| Images, captions and tables | figures-and-tables.en.md | cmd-figure, cmd-figures, cmd-table |
| Equations, theorems and proofs | equations-and-theorems.en.md | cmd-equation, cmd-theorem |
| Citation keys and BibTeX databases | references-and-bibliography.en.md | cmd-ref, cmd-bibliography |
| Builds and diagnostics | build-and-diagnostics.en.md | template/configure.tex and the student build path |

Chapter/section labels and equation labels use optional braced arguments. Figure pos/align and multi/subfigure align are accepted compatibility keys without placement/alignment effects. Table pos controls caption order; the float remains `[H]`. The guides distinguish actual behavior from accepted syntax.

## Discovery and copy contract

`thesis/AGENTS.md` and `thesis/context/AGENTS.md` are thin student routers. Each adjacent alias is exactly `CLAUDE.md -> AGENTS.md`. Nested skills are not automatically registered by every client; explicitly read the named SKILL.md when discovery does not occur.

Start from the requested content file/directory and inspect its ancestors, resolving relative targets from cwd. Without a target, inspect cwd and its ancestors. At a verified repository root, consider only its `thesis/` child. A matching runtime requires `thesis.tex`, `conf/` and `template/configure.tex` together. An explicit orphan target cannot borrow a runtime merely because cwd has another project.

Copy the entire `context/` with a tool preserving hidden `.agents/` and relative symlinks. Content carries knowledge and student material, not the template/compiler runtime. Preserve existing destination work before replacement, and use a matching complete template. The guides remain readable without example/, repository maintenance skills, CodeGraph or a network. Ordinary TeX builds do not load agent instructions or Markdown guides.

## Writing and authority boundaries

Agents edit requested student files and preserve research claims, labels, bibliography and unrelated work. Supply images and verified citation metadata; missing input must be reported rather than invented. Keep XeLaTeX/BibTeX and the existing layout/configuration boundary. A writing request does not authorize template optimization, installation, global/client configuration, Git publication, upload or account access.

Use official school-system certificate files. The community template does not imply institutional endorsement. Report actual build commands/results or missing tools; editing a file is not successful compilation, and deterministic payload checks do not prove every agent's behavior.

## Validation and recovery

From the repository root:

```bash
python3 scripts/test/check-student-agent-skills.py
just test
just ci
```

The required gate compiles the published human-guide snippets with a supplied image and existing real BibTeX entry. It checks chapter/section/figure labels, captions, references, bibliography convergence, PDF text, copied-context builds and runtime isolation. Student builds remain direct `latexmk` builds; Overleaf and editors use XeLaTeX with `thesis.tex`, as described in the [build guide](../../thesis/context/usage/build-and-diagnostics.en.md).

Negative contracts cover missing entrypoints/guides, malformed metadata, unsafe links, omitted hidden files, extra maintenance instructions, Chinese agent prose, wrong alias type/target, missing runtime, unverified child discovery, and broken labels/citation keys. Chinese human guides are a positive case. Archive checks inspect ZIP symlink mode, literal target payload and actual extraction separately from resolved AGENTS content.

If discovery fails, explicitly read the skill and check the requested content path. If the runtime is absent, obtain the matching complete template. If copying broke links, restore the whole content directory with hidden files and relative aliases. For build errors, follow the human diagnostic guide before changing template internals.

## CodeGraph for repository tooling

CodeGraph is optional assistance for maintained Python symbols and YAML file nodes. Configuration excludes student content, TeX templates, fixtures, documentation, instructions and generated output. It supplies no native LaTeX macro/include graph. Use direct TeX source, public API manifests, focused fixtures and nonempty `.fls` records for that work.

Synchronize before queries and compare results with current source. Lexical matching may return shared-word symbols; fuzzy results are not semantic absence tests. A missing or busy index does not authorize initialization, installs, hook changes, client/MCP setup, daemon stops or unlocking. Generated `.codegraph/` state stays ignored and outside every package. See the [CodeGraph skill](../../.agents/skills/codegraph/SKILL.md) for the scoped procedure. CLI readiness and client integration are separate.
