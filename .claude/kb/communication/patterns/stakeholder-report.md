# Stakeholder Report

> **Purpose**: Generate executive summaries and stakeholder updates tailored to different audience levels
> **MCP Validated**: 2026-02-17

## When to Use

- Sending project status updates to leadership or cross-functional teams
- Converting detailed technical outcomes into business-level summaries
- Preparing weekly/monthly reports for sponsors and stakeholders
- Summarizing meeting outcomes (pairs with meeting-extraction pattern)

## Implementation

```markdown
## Stakeholder Report Template

### Header Block
- **Project:** [Project Name]
- **Period:** [Date Range]
- **Author:** [Name]
- **Distribution:** [Audience List]
- **Status:** [On Track / At Risk / Blocked / Complete]

### Section 1: Executive Summary (3-5 bullet points)
The most critical information. A busy executive reads ONLY this.
- What happened (outcome, not activity)
- What it means (business impact)
- What needs attention (risks, decisions needed)
- What comes next (key milestones)

### Section 2: Key Metrics
| Metric            | Previous | Current | Target | Trend |
|-------------------|----------|---------|--------|-------|
| [Metric Name]     | [Value]  | [Value] | [Value]| [up/down/flat] |

### Section 3: Decisions Needed
| Decision                  | Options          | Recommendation | Deadline   |
|---------------------------|------------------|----------------|------------|
| [What needs to be decided]| [A, B, or C]     | [Your pick]    | [By when]  |

### Section 4: Risks and Blockers
| ID     | Description    | Likelihood | Impact | Mitigation         | Owner   |
|--------|----------------|------------|--------|--------------------|---------|
| [R-001]| [Risk desc]    | [H/M/L]   | [H/M/L]| [What we're doing] | [@name] |

### Section 5: Detailed Progress (Optional)
For readers who want depth. Use progressive disclosure --
this section is skippable for executives.
```

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `summary_bullets` | `3-5` | Number of executive summary points |
| `include_metrics` | `true` | Show metrics table |
| `include_risks` | `true` | Show risk register |
| `detail_level` | `summary` | Options: `summary`, `detailed`, `full` |
| `audience` | `executive` | Options: `executive`, `manager`, `technical` |

## Example Usage

### Executive Report

```markdown
# Project Status: Invoice Processing Pipeline
**Period:** 2026-02-01 to 2026-02-14 | **Status:** On Track

## Executive Summary
- Pipeline migration to Cloud Run is **85% complete** (target: 100% by Mar 5)
- Processing speed improved **3x** (15 min vs. 45 min per batch)
- Infrastructure cost reduced **20%** ($1,920/mo vs. $2,400/mo)
- One risk: large PDF handling requires security approval for new library
- **Decision needed:** Approve $500/mo budget for enhanced PDF processing

## Key Metrics
| Metric              | Jan      | Feb      | Target   | Trend |
|---------------------|----------|----------|----------|-------|
| Processing time     | 45 min   | 15 min   | < 20 min | Down  |
| Monthly cost        | $2,400   | $1,920   | < $2,000 | Down  |
| Documents/day       | 8,000    | 10,000   | 10,000   | Up    |
| Error rate          | 4.2%     | 2.1%     | < 3%     | Down  |

## Decisions Needed
| Decision                         | Options            | Recommendation | Deadline   |
|----------------------------------|--------------------|----------------|------------|
| PDF processing library budget    | Approve / Defer    | Approve         | 2026-02-20 |

## Risks
| ID    | Description                  | L   | I   | Mitigation              | Owner  |
|-------|------------------------------|-----|-----|-------------------------|--------|
| R-001 | Security approval delay      | Med | High| Escalate if not done by 2/20 | @bob |
| R-002 | Cross-page table edge cases  | Low | Med | Deferred to sprint 3    | @alice |
```

### Manager Report (Same Project, More Detail)

```markdown
# Sprint Report: Invoice Pipeline Migration
**Sprint:** 2026-S04 (Feb 3-14) | **Status:** On Track

## Summary
Completed Cloud Run migration for intake and extraction services.
Validation service PR under review. PDF chunking implementation
starting next sprint pending security approval.

## Completed This Sprint
- [A-001] Cloud Run intake service deployed to staging -- @carol
- [A-002] Extraction service migrated from Cloud Function -- @carol
- [A-003] Load testing completed (500 concurrent users) -- @alice
- [A-004] Monitoring dashboard created in Grafana -- @alice

## In Progress
- [A-005] Validation service migration (PR #247 in review) -- @carol
- [A-006] Security review for PDF splitting library -- @bob

## Blocked
- [B-001] PDF chunking cannot start until security approves library

## Next Sprint Plan
1. Complete validation service deployment
2. Begin PDF chunking implementation (if unblocked)
3. End-to-end integration testing
```

## Report Tone by Audience

| Audience | Tone | Lead With | Avoid |
|----------|------|-----------|-------|
| Board/C-suite | Strategic, confident | Business impact, ROI | Technical jargon, implementation details |
| VP/Director | Analytical, direct | Metrics, risks, decisions | Code-level details |
| Manager | Operational, actionable | Status, blockers, actions | Architecture deep-dives |
| Technical team | Precise, detailed | What changed, how, PRs | Business platitudes |

## See Also

- [Meeting Extraction](../patterns/meeting-extraction.md)
- [Audience Analysis](../concepts/audience-analysis.md)
- [Adaptive Explanation](../patterns/adaptive-explanation.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
