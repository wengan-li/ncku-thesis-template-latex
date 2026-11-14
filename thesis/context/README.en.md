<!-- doc-pair: student-writing; lang: en; topics: task-routes,agents-and-copy -->

[繁體中文](README.md) | [English](README.en.md)

# Thesis content and writing entry

## Learn to write

The existing example/how-to sources and generated teaching PDF own the full tutorial for chapters, figures, tables, equations, theorems, bibliography and front matter. This page provides routes rather than another syntax handbook. ExampleMode builds the teaching document in a complete project; for an own thesis, turn that mode off following the student project README and select content in context/context.tex. Packages without teaching source can use the full teaching PDF from the release packages.

## Use an agent or copy the project

Ask the agent to explicitly read [SKILL.md](../.agents/skills/ncku-thesis-writing/SKILL.md), then the relevant section of its [generated English reference](../.agents/skills/ncku-thesis-writing/references/template-usage.md). This small reference comes from code actually consumed by the teaching document, rather than another human handbook. It is readable without the teaching directory or a network. Explicitly read the skill if the client does not discover it; alias resolution does not prove automatic invocation.

Copy the entire buildable student project, including hidden .agents/, .claude/ and relative links. The project-root .claude/skills -> ../.agents/skills alias exposes the canonical writing skill. Preserve existing destination work first and build from the directory containing thesis.tex. Context holds student content; it is not an independently bundled agent project and includes neither the skill nor template runtime.

The agent inspects the requested content path's ancestors, or cwd when no target is supplied, and only the thesis/ child at a verified repository root. A matching complete project must contain thesis.tex, conf/ and template/configure.tex together. Orphan content must not borrow an unrelated runtime. Ordinary builds read no agent instructions and require no generator.
