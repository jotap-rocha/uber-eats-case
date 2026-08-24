# Communication Quick Reference

> Fast lookup tables. For detailed examples, see linked files.
> **MCP Validated:** 2026-02-17

## Audience Levels

| Level | Vocabulary | Detail | Example Opener |
|-------|-----------|--------|----------------|
| Executive | Business outcomes | Impact only | "This reduces cost by 30%..." |
| Manager | Process + metrics | How it works | "The pipeline processes 10K records/hour..." |
| Technical | Implementation | Full depth | "The Cloud Run service uses a PubSub push..." |
| Non-technical | Everyday language | Analogy-first | "Think of it like a postal sorting office..." |

## Progressive Disclosure Layers

| Layer | Length | Contains | Audience |
|-------|--------|----------|----------|
| Headline | 1 sentence | Core outcome | Everyone |
| Summary | 2-3 sentences | What + why + impact | Executives, managers |
| Detail | 1-2 paragraphs | How it works, trade-offs | Managers, senior technical |
| Deep-dive | Full section | Code, specs, edge cases | Technical implementers |

## Analogy Selection

| Technical Concept | Analogy Domain | Example Mapping |
|-------------------|---------------|-----------------|
| Message queue | Postal system | PubSub = post office sorting |
| Load balancing | Restaurant host | Distributes diners to tables |
| Caching | Notebook summary | Quick notes vs. re-reading book |
| CI/CD pipeline | Assembly line | Each station checks one thing |
| Database index | Book index | Jump to page vs. read everything |

## Meeting Extraction Fields

| Field | Required | Format | Example |
|-------|----------|--------|---------|
| Decision | Yes | `[D-001] Statement` | `[D-001] Migrate to Cloud Run by Q2` |
| Action Item | Yes | `[A-001] Task @owner due:DATE` | `[A-001] Draft RFC @alice due:2026-03-01` |
| Risk | If present | `[R-001] Risk (likelihood/impact)` | `[R-001] Vendor lock-in (medium/high)` |
| Blocker | If present | `[B-001] Blocking issue` | `[B-001] API key not provisioned` |

## Decision Matrix

| Use Case | Choose |
|----------|--------|
| Explaining to executives | Headline + Summary layers only |
| Writing technical docs | All four disclosure layers |
| Meeting notes for team | Decisions + Action Items |
| Stakeholder update email | Stakeholder report pattern |
| Teaching a concept | Analogy-first, then progressive disclosure |
| Status report | Meeting extraction + stakeholder report |

## Common Pitfalls

| Don't | Do |
|-------|-----|
| Use jargon with non-technical audience | Lead with analogy, define terms |
| Dump all details at once | Use progressive disclosure layers |
| Skip audience analysis | Always classify before explaining |
| Write action items without owners | Every action needs `@owner` + `due:DATE` |
| Mix decisions and discussion | Separate `[D-xxx]` from conversation notes |

## Related Documentation

| Topic | Path |
|-------|------|
| Audience Analysis | `concepts/audience-analysis.md` |
| Progressive Disclosure | `concepts/progressive-disclosure.md` |
| Adaptive Explanation | `patterns/adaptive-explanation.md` |
| Full Index | `index.md` |
