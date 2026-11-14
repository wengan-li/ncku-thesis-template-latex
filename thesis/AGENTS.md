# Student thesis project

These instructions apply to student writing in this project. Read [the writing skill](.agents/skills/ncku-thesis-writing/SKILL.md) before editing thesis content, then load only the relevant section of its generated English reference. The relative directory alias .claude/skills -> ../.agents/skills exposes the same canonical skill. Explicitly open SKILL.md if the client does not discover it; alias resolution does not prove automatic invocation.

Copy the complete buildable project, including hidden .agents/, .claude/ and relative links. Build from the directory containing thesis.tex. The context/ directory holds student content and is not an independently bundled agent project.

Find the project from the requested content file/directory and its ancestors, or from cwd and its ancestors when no target was supplied. At a verified repository root, also consider only its thesis/ child if thesis.tex, conf/ and template/configure.tex all exist there. Reject an orphan target instead of attaching it to an unrelated runtime. Read [the student guide](README.en.md) for first use. Preserve research claims and existing content; never invent citations, data or successful builds. This router grants no installation, publication, upload or account authority.
