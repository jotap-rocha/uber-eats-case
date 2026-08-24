# Progressive Disclosure

> **Purpose**: Layer complexity gradually from simple headline to full technical depth
> **Confidence**: 0.95
> **MCP Validated**: 2026-02-17

## Overview

Progressive disclosure is a communication technique that presents information in layers of
increasing complexity. Initially, show only the most important outcome. Then reveal supporting
detail, technical context, and deep-dive content only as the audience requests or needs it.
This reduces cognitive load and ensures every audience level gets value from the first layer
they read.

## The Pattern

```markdown
## Four-Layer Disclosure Model

### Layer 1: Headline (1 sentence)
The pipeline now processes invoices 3x faster at 20% lower cost.

### Layer 2: Summary (2-3 sentences)
We migrated the invoice processing pipeline from batch Cloud Functions to
event-driven Cloud Run services. Processing time dropped from 45 minutes to
15 minutes per batch. Infrastructure cost decreased from $2,400/month to
$1,920/month due to scale-to-zero behavior.

### Layer 3: Detail (1-2 paragraphs)
The new architecture uses Pub/Sub to fan out individual invoice documents to
Cloud Run containers that scale horizontally. Each container processes one
invoice in isolation, enabling parallel execution. We replaced the monolithic
Cloud Function with three focused microservices: intake, extraction, and
validation. Error handling improved because failures are isolated to
individual documents rather than failing the entire batch.

### Layer 4: Deep-Dive (full technical section)
[Architecture diagram, code snippets, configuration details,
 performance benchmarks, edge cases, failure modes]
```

## Quick Reference

| Layer | Target | Length | Contains | Stops Here If |
|-------|--------|--------|----------|--------------|
| Headline | Everyone | 1 sentence | Core outcome | Reader only needs the result |
| Summary | Decision-makers | 2-3 sentences | What + why + impact | Reader can decide/act |
| Detail | Managers, leads | 1-2 paragraphs | How, trade-offs, risks | Reader understands approach |
| Deep-dive | Implementers | Unlimited | Code, specs, edge cases | Reader needs to build it |

## Common Mistakes

### Wrong (Information Dump)

```markdown
## Invoice Pipeline Update

We implemented a Kubernetes-based microservices architecture using Cloud Run
with Pub/Sub triggers. The Dockerfile uses a multi-stage build with Python
3.11 slim base image. We configured concurrency to 80 with a max-instances
of 10. The Pub/Sub subscription uses exactly-once delivery with a 600s
ack deadline. We added dead-letter topics for failed messages with a
max-delivery-attempts of 5. The extraction service uses Gemini 1.5 Flash
with temperature 0.0 and structured output mode...
```

### Correct (Layered)

```markdown
## Invoice Pipeline Update

**Result:** 3x faster processing, 20% cost reduction.

**How:** Migrated from batch Cloud Functions to event-driven Cloud Run with
Pub/Sub. Each invoice processes independently, enabling parallelism.

**Details:** [link to architecture doc]
**Code:** [link to implementation PR]
```

## Applying Progressive Disclosure

### In Documentation

```markdown
# Feature: Auto-Scaling Pipeline

> **TL;DR**: Pipeline now handles 10x traffic spikes without manual intervention.

## Overview
The auto-scaling pipeline uses Cloud Run's built-in horizontal scaling
combined with Pub/Sub backpressure to handle variable workloads.

## How It Works
[Detailed explanation with diagrams]

## Configuration Reference
[Full parameter tables and YAML examples]

## Troubleshooting
[Edge cases, failure modes, debugging steps]
```

### In Verbal Communication

| Step | Say | Duration |
|------|-----|----------|
| 1 | "The short version is..." | 10 seconds |
| 2 | "Here's why that matters..." | 30 seconds |
| 3 | "The way we did it was..." | 1-2 minutes |
| 4 | "Let me walk you through the details..." | As needed |

### In Slack/Email

```markdown
**Subject line** = Layer 1 (headline)
**First paragraph** = Layer 2 (summary)
**Below the fold** = Layer 3 (detail)
**Attached doc/link** = Layer 4 (deep-dive)
```

## When NOT to Use Progressive Disclosure

| Situation | Why | Instead |
|-----------|-----|---------|
| Emergency/incident | Need all info immediately | Lead with severity + impact + action |
| Compliance/legal | Must disclose everything | Structured checklist, nothing hidden |
| Peer code review | Reviewer needs full context | Provide complete diff with annotations |

## Related

- [Audience Analysis](../concepts/audience-analysis.md)
- [Analogies](../concepts/analogies.md)
- [Adaptive Explanation](../patterns/adaptive-explanation.md)
