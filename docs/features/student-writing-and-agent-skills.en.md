<!-- language: en; summary: student-writing-and-agent-skills.md -->

[繁體中文摘要](student-writing-and-agent-skills.md) | [English technical record](student-writing-and-agent-skills.en.md)

# Student writing and portable agent skills

Status: local implementation and acceptance complete, unpublished. No release or hosted agent execution is claimed.

## Intent

Students receive task-oriented writing knowledge with their thesis content. One skill at `thesis/context/.agents/skills/ncku-thesis-writing/SKILL.md` routes to English human usage guides under `thesis/context/usage/`. Those guides have Traditional-Chinese companions outside `.agents/`. The agent tree and both new student AGENTS routers are English only, with no language switchers. Copying the entire `context/` directory preserves this knowledge offline. It does not supply the template runtime.

Preserve XeLaTeX, BibTeX, existing entry/configuration bytes, public commands, normal defaults and visible layout. Student agents edit requested thesis content, preserve scientific claims and cite only supplied sources. No hooks, installation, client settings, network service or CodeGraph dependency enters the student package.

Failure includes incorrect command syntax, a broken local reference, missing hidden payload, escaping aliases, invented citations, an unconverged pilot or a package claim based only on uncommitted source.

## Expectations

The acceptance boundary includes a real own-thesis chapter/section, supplied image/caption/label, cross-reference and existing real BibTeX entry. Compile the published snippets themselves, from an extracted student package without `example/`. Rehearse a full `context/` copy into another matching template. Check missing payload, sidecar, unsafe links, wrong aliases, omitted hidden files and corrupted references. Run the bilingual, API, flat-layout and complete repository gates on an exact committed scratch candidate.

The two student routers are exactly `thesis/AGENTS.md` and `thesis/context/AGENTS.md`. Each adjacent `CLAUDE.md` is a relative symlink to `AGENTS.md`. They carry no repository authority. ZIP validation checks Unix mode, link payload, extraction target and content independently. The root repository alias remains unchanged.

Recovery removes the new documentation/tooling slice; existing thesis sources remain usable. Publication, real-index staging, branches, worktrees, commits in this checkout, uploads and hosted agent evaluation are outside authorization. Scratch fixture Git is explicitly permitted for package proof.

## Context and ownership

The source baseline is `7a42edb9ff69317af08f610eb15029ec22d7521e`. The approved external handoff supersedes the original plan's proposed status. Completed requirement/todo 03 have been retired after local acceptance. This record owns design and durable evidence.

`context/README*` is a task router. Paired `context/usage/` guides own usage knowledge and executable snippets. Agent references are unnecessary: the English-only skill links directly to English human guides. `SKILL.md` owns agent workflow and safeguards. Existing first-run/configuration guides remain authoritative for student data. Nested skill discovery varies by client; routers prescribe an explicit read fallback. No universal agent behavior claim follows from deterministic checks.

Project discovery starts from the requested content file/directory and its ancestors, resolving relative targets from cwd. Without a target, inspect cwd and its ancestors. At a verified repository root, consider only its thesis/ child and require thesis.tex, conf/ and template/configure.tex together. Do not recursively search unrelated children or attach explicit orphan content to the runtime near cwd. Contract cases cover repository-root entry, relative target files/directories, nested cwd, orphan content and an unverified directory containing a runtime child.

## Source-to-guide coverage

The published snippets and existing family fixtures listed below passed local acceptance. The matrix is bounded usage coverage, not a claim that every v1 API is recommended or individually documented.

| Family | Definition under thesis/template/command/ | Human guide under thesis/context/usage/ | Verification |
| --- | --- | --- | --- |
| Own content, chapters, sections, text/lists | cmd-thesis.tex, cmd-chapter.tex, cmd-list.tex | project-and-chapters | Published pilot, 121 sectioning, 800 StudentMode |
| Single/multiple figures, captions, labels | cmd-figure.tex, cmd-figures.tex | figures-and-tables | Published snippets, 400 floats, 402 unknown keys |
| Tables and caption position | cmd-table.tex | figures-and-tables | Published snippet, 400 floats, 403 unknown keys |
| Equations and reference wrappers | cmd-equation.tex, cmd-ref.tex | equations-and-theorems | Published snippet, 300 references |
| Theorems/proofs | cmd-theorem.tex | equations-and-theorems | Published snippet, 500/503 theorem routes |
| BibTeX and convergence | cmd-bibliography.tex, cmd-ref.tex | references-and-bibliography | Published entry/citation, 300/301 references |
| Abstracts, acknowledgments, nomenclature, appendices | cmd-abstract.tex, cmd-acknowledgments.tex, cmd-nomenclature.tex, cmd-appendix.tex | project-and-chapters | Source reconciliation; pilot front matter and appendix |
| Build and diagnostics | template/configure.tex, package README | build-and-diagnostics | Extracted/copy/Overleaf cold builds |

Chapter/section labels are optional braced arguments. Equation labels use `G{\empty}`, not square brackets. Figure `pos` and `align`, multiple-figure `align` and subfigure `align` are accepted compatibility keys without placement/alignment effects. Tables use `pos=top` for an above-table caption and another value for below; their float remains `[H]`. Do not advertise inactive controls or republish the full v1 manifest as recommended usage.

## Accepted language decision

The owner correction supersedes the original bilingual-agent-reference layout. All new SKILL.md, agent sidecars and student AGENTS.md prose is English only. Human usage documentation remains bilingual under `context/usage/`, outside `.agents/`. Preserve `CLAUDE.md -> AGENTS.md` symlinks. The earlier bilingual-agent scratch candidate is historical validation only and cannot establish corrected acceptance. Explicit language mutations cover the skill, a sidecar and both student routers; a positive case preserves Chinese human guidance.

## Independent CodeGraph pilot

CodeGraph remains optional and local to repository tooling. Installed CLI 1.6.1 supports Python symbols and YAML file nodes; it has no extension mapping for TeX, BibTeX, shell or Markdown. Native LaTeX semantic coverage and custom parsers are outside this scope. Before init, inspect watcher fallback because `--yes` may install Git hooks. No hook, client/global configuration or daemon mutation is authorized. Record any blocker independently of the student feature.

## Executed local evidence

The corrected implementation, including the acceptance review's runtime-discovery fix, was snapshotted from the existing checkout without changing its index or refs. The exact tested scratch source is commit `6389fa14ca515a9296eb6a3ef75538c9ca91601c`, tree `57bd92a9aae68e3096fceac86b97ffd136522580`, based on `7a42edb9ff69317af08f610eb15029ec22d7521e`. A retained path/mode/SHA-256 manifest authenticates every tracked candidate file and intended new file, including parent-owned maintenance-skill updates. Build output, local graph state and unrelated files were excluded. The historical migration tag was imported read-only into the isolated scratch Git fixture. No real repository staging, commit, branch, worktree or publication occurred.

| Check | Executed result |
| --- | --- |
| `python3 scripts/test/check-student-agent-skills.py --build` | PASS, exact human-guide snippets, supplied image and source-pinned real MapReduce entry |
| English-only and portable-payload contracts | PASS, skill and both routers English only, all human guide links bounded inside copied context |
| Repository/target discovery | PASS from verified repository root, requested content file/directory and nested cwd; orphan targets and unverified child runtimes rejected |
| Negative cases | PASS, 19 payload/language/alias/runtime/reference/citation mutations, plus seven required-member deletions in the archive gate |
| `python3 scripts/test/check-bilingual-docs.py` | PASS, 14 complete human-guide pairs and 4 summary pairs; action/default/exception parity reviewed |
| `python3 scripts/test/check-test-layout.py` | PASS, 46 tracked flat numbered artifacts in the committed candidate, including 802 |
| `python3 scripts/test/check-v1-api.py` | PASS, 597 LaTeX/xparse and 65 literal def declarations retained |
| `just test` / `just ci` | Both PASS on the corrected candidate, 92.37 / 80.13 seconds |
| Direct extracted default build | PASS using `latexmk -xelatex -synctex=1 -interaction=nonstopmode thesis.tex`, 261 A4 pages plus SyncTeX, final references/citations converged |
| Extracted own-thesis pilot and whole-context copy | PASS without example/ or repository maintenance files; expected PDF text, caption, labels and real citation; corrupted reference and citation reject, restored content passes |
| Visual inspection | Pilot pages 6/7 inspected for image/subimages, table, equation, theorem/proof and references; no clipping observed |
| Runtime isolation | Nonempty recorder files confirm neither agent instructions nor human usage guides are TeX inputs |
| `git diff --check` and immutable student inputs | PASS; thesis.tex/conf/conf.tex unchanged, real index digest preserved |

The two-image helper retains its existing 8pt overfull hbox diagnostic; representative output was readable. The default teaching build also emits inherited xdvipdfmx duplicate-object console diagnostics. These observations do not authorize a template/layout refactor; the unchanged canonical warning-budget gate passed. No warning-free or cross-platform byte-identical PDF claim is made.

The bundled stock skill validator could not run with the existing Python because PyYAML is absent. Nothing was installed. The repository's new frontmatter/link/language/payload checker uses the standard library and passed the full gate.

## Package provenance

All three packages below came from the exact corrected scratch commit. The student verifier checks the complete HEAD:thesis inventory and every member's bytes, separately checking symlink mode, literal target payload and actual Info-ZIP extraction. Symlink payload is never compared with resolved AGENTS text. The two aliases are exactly `CLAUDE.md -> AGENTS.md` and `context/CLAUDE.md -> AGENTS.md`; unexpected instruction trees and escaping links reject.

| Package | Files | Editable bytes | ZIP bytes | SHA-256 |
| --- | ---: | ---: | ---: | --- |
| Student | 210 | 671764 | 32562640 | a18cfe6f44a98137f8fb890618036ced664f31e25915072dda5a62e0e9ddb423 |
| Overleaf student | 96 | 433832 | 5039619 | b2cb8d51916f534ce97026ccb9aee033007e234427cde7e8aaae9451e10ccd30 |
| Overleaf Gallery | 94 | 434420 | 4755511 | 8947ef5ee746f7ea801469520e8d4f97c108ebfa7f2dd3dbd1c41d0a2a503cac |

Both generated Overleaf profiles passed local cold builds, hidden-skill/alias extraction and file/byte limits. Official [upload limits](https://docs.overleaf.com/managing-projects-and-files/uploading-a-project) and [plan limits](https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits) were rechecked on 2026-11-14. The root README is augmented only in generated Overleaf packages; source defaults remain intact. Local checks establish no hosted Overleaf execution or client-specific symlink/discovery guarantee.

Full logs, manifests, graph inventory, package receipts and rendered pilot pages remain in private scratch. The completed acceptance tracker was consolidated here; subsequent documentation-only closure is structurally rechecked separately. The student subtree and test/tooling bytes are unchanged by that closure.

## CodeGraph result and procedure

The launcher changed externally from 1.6.1 to 1.6.2 during the session; this implementation performed no install or upgrade. Init/watch-policy source was inspected before execution. On this native filesystem the watcher policy returned null, so init did not invoke its hook fallback. Snapshotted instructions, settings and hook bytes were unchanged after initialization. Telemetry/update environment flags were set per command. Generated state remains ignored.

The actual 1.6.2 index contains 24 files: 19 Python validators plus the Python release-notes script, and four YAML workflow/issue-template files. Current inventory and status are retained with the private receipts. The final sync reported 328 nodes, 964 edges, Python/YAML only and zero pending changes. Queries for check_guide_pair and check_active_work_directory matched 153 current on-disk source lines. An isolated fixture proved exact function removal/addition after sync and returned the replacement source.

A query-only deletion assertion initially failed because lexical matching returned a symbol sharing a name segment. Exact database membership proved freshness; an empty/fuzzy response is not a semantic absence test. InsertFigure returned no indexed result, and the actual extension registry has no .tex/.sty/.cls/.bib/.sh/.md mapping. The configured thesis exclusion independently keeps student content outside the graph. Use direct TeX source, API manifests, focused fixtures and nonempty .fls evidence for that work. No custom parser, extension spoofing, MCP registration, hook installation, live-daemon stop or unlock was performed.

The scoped [CodeGraph skill](../../.agents/skills/codegraph/SKILL.md) owns the reusable procedure. It stays outside student archives. CLI readiness is separate from any client integration.

## Remaining authority boundaries

The local implementation scope is complete and unpublished. Hosted agent behavior, authenticated Overleaf execution, release/publication and any future policy/compliance change need their own authorized work. No universal client discovery, institutional endorsement or official certificate generation is claimed.
