<!-- doc-pair: student-writing; lang: en; topics: task-routes,agents-and-copy -->

[繁體中文](README.md) | [English](README.en.md)

# Thesis content and writing entry

## Learn to write

The existing example/how-to sources and generated teaching PDF own the full tutorial for chapters, figures, tables, equations, theorems, bibliography and front matter. This page provides routes rather than another syntax handbook. ExampleMode builds the teaching document in a complete project; for an own thesis, turn that mode off following the student project README and select content in context/context.tex. Packages without teaching source can use the full teaching PDF from the release packages.

## Use an agent or copy content

Ask the agent to explicitly read [SKILL.md](.agents/skills/ncku-thesis-writing/SKILL.md), then the relevant section of its [generated English reference](.agents/skills/ncku-thesis-writing/references/template-usage.md). This small reference comes from code actually consumed by the teaching document, rather than another human handbook. It is readable without the teaching directory or a network. Nested skills are not automatically registered in every client.

Copy the entire context/, including hidden .agents/, the generated reference and the relative CLAUDE.md -> AGENTS.md aliases. Preserve existing destination work first. Content alone includes neither the template nor compiler; a matching complete project must contain thesis.tex, conf/ and template/configure.tex together. The agent inspects the requested content path's ancestors, or cwd when no target is supplied, and only the thesis/ child at a verified repository root. Orphan content must not borrow an unrelated runtime. Ordinary builds read no agent instructions and require no generator.
