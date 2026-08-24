# Audience Analysis

> **Purpose**: Identify audience expertise level, role, goals, and information needs before communicating
> **Confidence**: 0.95
> **MCP Validated**: 2026-02-17

## Overview

Audience analysis is the practice of classifying your listeners or readers by their technical
expertise, organizational role, and immediate goals before crafting a message. Effective
communication starts with understanding who you are talking to, not what you want to say.
This concept drives every other communication pattern in this knowledge base.

## The Pattern

```markdown
## Audience Classification Template

### Step 1: Identify the Audience Profile

| Dimension       | Question to Ask                        | Options                              |
|-----------------|----------------------------------------|--------------------------------------|
| Expertise       | How deep is their technical knowledge? | Executive / Manager / Technical / Novice |
| Role            | What decisions do they make?           | Sponsor / Implementer / Reviewer / Consumer |
| Goal            | What do they need from this message?   | Decide / Act / Learn / Monitor       |
| Time Budget     | How much time will they invest?        | < 30s / 1-3 min / 5-10 min / Unlimited |
| Prior Context   | What do they already know?             | None / High-level / Partial / Full   |

### Step 2: Select Communication Strategy

- **Executive + Decide + < 30s** --> Headline only, with recommendation
- **Manager + Act + 1-3 min** --> Summary with action items
- **Technical + Learn + 5-10 min** --> Progressive disclosure, full depth
- **Novice + Learn + Unlimited** --> Analogy-first, step-by-step
```

## Quick Reference

| Audience Level | Vocabulary | Max Jargon | Lead With |
|---------------|-----------|------------|-----------|
| Executive | Business outcomes | Zero | Impact + recommendation |
| Manager | Process terms | Minimal | Status + blockers + actions |
| Technical | Domain-specific | Full | Architecture + trade-offs |
| Novice | Everyday language | Zero | Analogy + "why it matters" |

## Common Mistakes

### Wrong

```markdown
To: CEO, CTO, Junior Developer, Product Manager

Subject: System Update

We've implemented a Kubernetes-based microservices architecture with
gRPC inter-service communication, Istio service mesh for mTLS, and
Prometheus/Grafana for observability. The p99 latency improved from
450ms to 120ms after we optimized the connection pooling in our
PostgreSQL read replicas.
```

### Correct

```markdown
To: CEO
Subject: Platform Upgrade Complete -- 3x Faster, 20% Lower Cost

To: CTO
Subject: Microservices Migration Results -- Architecture Decisions & Metrics

To: Junior Developer
Subject: How Our New Platform Works (Step-by-Step Guide)

To: Product Manager
Subject: Platform Upgrade -- What Changed for Your Features
```

## Audience Signals to Detect

| Signal | Indicates | Adapt By |
|--------|-----------|----------|
| "Can you give me the bottom line?" | Executive, time-pressed | Jump to conclusion first |
| "How does this work?" | Curious learner | Use progressive disclosure |
| "What should I do?" | Action-oriented | Lead with action items |
| "What are the trade-offs?" | Technical evaluator | Compare options with data |
| "I don't understand X" | Knowledge gap | Insert analogy or definition |
| Silence / no questions | Disengaged or overwhelmed | Simplify, check understanding |

## Multi-Audience Communication

When addressing mixed audiences simultaneously:

1. **Layer the message** -- headline for everyone, details for those who need them
2. **Use expandable sections** -- summaries that link to deep-dives
3. **Label sections by audience** -- "For Technical Teams:", "For Stakeholders:"
4. **Provide multiple artifacts** -- one-page summary + detailed appendix

## Related

- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [Adaptive Explanation](../patterns/adaptive-explanation.md)
- [Stakeholder Report](../patterns/stakeholder-report.md)
