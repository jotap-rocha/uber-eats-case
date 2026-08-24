# Meeting Extraction

> **Purpose**: Extract structured decisions, action items, risks, and key topics from meeting transcripts
> **MCP Validated**: 2026-02-17

## When to Use

- Processing raw meeting transcripts or notes into structured outputs
- Generating post-meeting summaries for stakeholders who did not attend
- Building automated meeting analysis pipelines with LLMs
- Tracking decisions and action items across multiple meetings

## Implementation

```markdown
## IDA Framework (Information-Decision-Action)

Every meeting produces three categories of output:

### 1. Information (I) -- What was shared
Key facts, data points, status updates, and context that was communicated.
Tag as: `[I-001]`, `[I-002]`, etc.

### 2. Decisions (D) -- What was decided
Explicit agreements or choices made by the group. Must have:
- A clear statement of what was decided
- Who made or approved the decision
- Rationale (why this option was chosen)
Tag as: `[D-001]`, `[D-002]`, etc.

### 3. Actions (A) -- What will be done
Concrete tasks assigned to specific people with deadlines. Must have:
- Task description (verb + object)
- Owner (@person)
- Due date (due:YYYY-MM-DD)
- Priority (P1/P2/P3)
Tag as: `[A-001]`, `[A-002]`, etc.
```

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `extract_decisions` | `true` | Extract `[D-xxx]` tagged decisions |
| `extract_actions` | `true` | Extract `[A-xxx]` tagged action items |
| `extract_risks` | `true` | Extract `[R-xxx]` tagged risks |
| `extract_blockers` | `true` | Extract `[B-xxx]` tagged blockers |
| `extract_topics` | `true` | Extract discussed topic summaries |
| `sentiment_analysis` | `false` | Detect emotional tone per topic |

## Example Usage

### Input: Raw Meeting Transcript

```text
Meeting: Data Pipeline Review
Date: 2026-02-15
Attendees: Alice (Tech Lead), Bob (PM), Carol (Data Eng), Dave (VP Eng)

Alice: The invoice pipeline is processing about 10K documents per day now.
We're hitting some timeouts on large PDFs over 50 pages.

Bob: How many documents are affected?

Alice: About 3% of total volume. We could increase the timeout from 30s to
60s, or split large PDFs into chunks before processing.

Dave: Let's go with chunking. I don't want to just mask the problem with
longer timeouts. Carol, can you handle that?

Carol: Sure. I'll need about a week. I'll also need the PDF splitting
library approved by security.

Bob: I'll follow up with security on the library approval. Let's aim to
have this done before the Q1 review on March 5th.

Alice: One risk -- if we chunk PDFs, we need to handle cross-page tables.
That's a harder problem.

Dave: Flag it but don't let it block the main fix. We can handle edge
cases in a follow-up sprint.
```

### Output: Structured Extraction

```markdown
# Meeting Summary: Data Pipeline Review
**Date:** 2026-02-15
**Attendees:** Alice (Tech Lead), Bob (PM), Carol (Data Eng), Dave (VP Eng)

## Key Information
- [I-001] Invoice pipeline processes ~10K documents/day
- [I-002] ~3% of documents (large PDFs >50 pages) cause timeouts
- [I-003] Two options discussed: increase timeout vs. chunk PDFs

## Decisions
- [D-001] Use PDF chunking approach instead of increasing timeouts
  - **Decided by:** Dave (VP Eng)
  - **Rationale:** Address root cause rather than masking with longer timeouts
- [D-002] Cross-page table handling deferred to follow-up sprint
  - **Decided by:** Dave (VP Eng)
  - **Rationale:** Do not block the main fix with edge cases

## Action Items
- [A-001] Implement PDF chunking for large documents
  - **Owner:** @carol | **Due:** 2026-02-22 | **Priority:** P1
- [A-002] Get PDF splitting library approved by security
  - **Owner:** @bob | **Due:** 2026-02-20 | **Priority:** P1
- [A-003] Document cross-page table edge cases for follow-up sprint
  - **Owner:** @alice | **Due:** 2026-03-01 | **Priority:** P2

## Risks
- [R-001] Cross-page tables may not render correctly after chunking
  - **Likelihood:** Medium | **Impact:** Medium
  - **Mitigation:** Deferred to follow-up sprint (see [D-002])

## Blockers
- [B-001] PDF splitting library requires security approval before work begins
  - **Blocked:** [A-001] | **Unblocked by:** [A-002]

## Next Steps
- Security review for PDF library ([A-002]) is the critical path
- Q1 review deadline: 2026-03-05
```

## Extraction Prompt Template

```markdown
You are a meeting analyst. Extract structured information from the
following meeting transcript.

For each item, use these tags:
- [I-xxx] Information: key facts shared
- [D-xxx] Decisions: choices made (include who decided and why)
- [A-xxx] Actions: tasks assigned (include @owner, due:DATE, priority)
- [R-xxx] Risks: potential problems (include likelihood and impact)
- [B-xxx] Blockers: issues preventing progress

Output format: Use the structured markdown template provided.

TRANSCRIPT:
{transcript}
```

## See Also

- [Stakeholder Report](../patterns/stakeholder-report.md)
- [Audience Analysis](../concepts/audience-analysis.md)
- [Adaptive Explanation](../patterns/adaptive-explanation.md)
