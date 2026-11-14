<!-- doc-pair: student-writing; lang: en; topics: task-routes,agents-and-copy -->

[繁體中文](README.md) | [English](README.en.md)

# Write thesis content

## Choose a task

First comment out `\ExampleMode` in `conf/conf.tex` in the complete student project. `context/context.tex` selects the files to include. Leaving ExampleMode active builds the teaching document. Paths in the references are relative to the student project root.

| Task | Read |
| --- | --- |
| Add chapters, text, front matter or appendices | [Project and chapters](usage/project-and-chapters.en.md) |
| Add supplied images or tables | [Figures and tables](usage/figures-and-tables.en.md) |
| Write equations, theorems or proofs | [Equations and theorems](usage/equations-and-theorems.en.md) |
| Add real sources and citations | [References and bibliography](usage/references-and-bibliography.en.md) |
| Build or diagnose an error | [Build and diagnostics](usage/build-and-diagnostics.en.md) |

## Use an agent or copy content

Ask the agent to explicitly read [SKILL.md](.agents/skills/ncku-thesis-writing/SKILL.md), then the needed topic page. Nested skills are not automatically registered by every client. Supply research material, images and source metadata; missing inputs must not be invented. Human-only builds do not load agent instructions.

Copy the entire `context/` directory with a directory-copy tool that preserves hidden files and relative symlinks, including `.agents/`, `AGENTS.md` and `CLAUDE.md -> AGENTS.md`. Copying only visible files or *.tex loses the knowledge. Replace the destination content directory only after preserving its existing work. The destination still needs a matching complete template with `thesis.tex`, `conf/` and `template/configure.tex`; content alone cannot compile. If those are missing, obtain the matching complete student project first. Update its content assembly and configuration deliberately. No teaching examples or network are needed to read these references.

An agent locates the project through the requested content file/directory and its ancestors, or through cwd and its ancestors when no target was supplied. At a verified repository root, it also checks only the thesis/ child for all three runtime markers. It does not recursively search other directories or attach orphan content to an unrelated template.
