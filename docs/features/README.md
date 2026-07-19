<!-- bilingual:complete -->

# 已發行功能記錄 / Shipped feature records

## V2正式記錄 / V2 production records

**繁體中文**

本目錄保存production behavior、durable architecture decisions及machine-checked evidence。Feature records不是implementation queue；branch names、temporary boundaries、checkbox progress及重複command transcripts留在Git history。每個record提供繁中executive summary及完整英文technical body。

**English**

This directory preserves production behavior, durable architecture decisions, and machine-checked evidence. Feature records are not an implementation queue; branch names, temporary boundaries, checkbox progress, and duplicate command transcripts remain in Git history. Each record provides a Traditional-Chinese executive summary followed by the complete English technical body.

- [`v2-modernization.md`](v2-modernization.md) — product intent, compatibility, architecture, hardened subsystems, completion boundary / 產品目標、相容性、架構及完成邊界。
- [`validation-and-performance.md`](validation-and-performance.md) — tests, artifact proof, benchmarks, accepted/rejected/deferred decisions / 測試、artifact proof、benchmark及工程決定。
- [`release-and-distribution.md`](release-and-distribution.md) — versioning, package, GitHub Release, Overleaf, retired sample repository, Draft/watermark policy / 版本、套件、發行、Overleaf及提交政策。

User migration / 使用者升級：[`../v1-to-v2-migration.md`](../v1-to-v2-migration.md)<br>
Student instructions / 學生指引：[`thesis/README.md`](../../thesis/README.md)

## 記錄政策與進行中工作 / Record policy and active work

**繁體中文**

Durable compatibility numbers、architecture decisions、measured rejected experiments及publication boundaries會保留，因為它們限制未來維護。雙語文件工作已完成；stable language policy保留在現行文件、AGENTS、repo-local skill及deterministic checker，implementation chronology則留在Git history。目前沒有active requirement。

**English**

Durable compatibility numbers, architecture decisions, measured rejected experiments, and publication boundaries remain because they constrain future maintenance. Bilingual-documentation work is complete: stable language policy remains in current documentation, AGENTS, the repo-local skill, and the deterministic checker, while implementation chronology remains in Git history. No requirement is currently active.
