# Adaptive Explanation

> **Purpose**: Dynamically adjust explanation depth, vocabulary, and structure to match audience expertise
> **MCP Validated**: 2026-02-17

## When to Use

- Explaining a technical concept to an audience whose expertise level varies or is unknown
- Responding to follow-up questions that signal the current explanation is too simple or too complex
- Writing documentation that serves multiple audience levels in a single artifact
- Building AI agents that must tailor responses to detected user proficiency

## Implementation

```markdown
## Adaptive Explanation Framework

### Phase 1: Detect Audience Level

Scan for signals before or during communication:

| Signal Type       | Indicator                          | Detected Level   |
|-------------------|------------------------------------|------------------|
| Vocabulary used   | "throughput", "p99", "sharding"    | Technical        |
| Vocabulary used   | "how does it work?"                | Intermediate     |
| Vocabulary used   | "what is this?"                    | Novice           |
| Questions asked   | "what are the trade-offs?"         | Technical        |
| Questions asked   | "what should I do?"                | Manager          |
| Questions asked   | "what's the bottom line?"          | Executive        |
| Role stated       | "I'm the CTO" / "I'm new here"    | Use role mapping  |
| Context clues     | Slack channel (#engineering)       | Technical        |
| Context clues     | Email to leadership@               | Executive        |

### Phase 2: Select Explanation Strategy

| Audience Level | Strategy               | Structure                          |
|----------------|------------------------|------------------------------------|
| Executive      | Outcome-first          | Result --> impact --> recommendation |
| Manager        | Process-oriented       | Status --> blockers --> actions      |
| Technical      | Mechanism-first        | How --> why --> trade-offs --> code  |
| Novice         | Analogy-first          | Analogy --> concept --> example      |

### Phase 3: Deliver with Feedback Loop

1. Start at the detected level
2. Watch for signals of confusion or boredom
3. Adjust up (more detail) or down (simplify) in real-time
4. Confirm understanding: "Does that make sense?" / "Want more detail?"
```

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `initial_level` | `auto-detect` | Starting audience level if no signals available |
| `escalation_trigger` | `"tell me more"` | Signal to increase detail depth |
| `simplification_trigger` | `"I don't understand"` | Signal to decrease complexity |
| `max_layers` | `4` | Maximum progressive disclosure depth |

## Example Usage

### Same Concept, Four Audiences

**Concept: Database Connection Pooling**

```markdown
## Executive Version
Database changes reduced response times by 40%, improving customer experience
during peak hours. No additional infrastructure cost.

## Manager Version
We implemented connection pooling for the main database. Instead of creating
a new database connection for every request (expensive), the application
reuses a pool of pre-established connections. Result: 40% faster responses
during peak load. The team completed this in one sprint with no downtime.

## Technical Version
We replaced per-request `psycopg2.connect()` calls with `psycopg2.pool.ThreadedConnectionPool`
(min=5, max=20). Connections are acquired from the pool, used, and returned. This
eliminates the TCP handshake + TLS negotiation + authentication overhead per query.
Under load testing (500 concurrent users), p95 latency dropped from 340ms to 195ms.
Pool exhaustion is handled with a 5s timeout and exponential backoff retry.

## Novice Version
Think of a database connection like a phone call. Before, every question required
dialing a new number, waiting for someone to pick up, asking your question, and
hanging up. With connection pooling, we keep several phone lines open all the time.
When someone has a question, they just pick up an already-connected line. This is
much faster because there's no dialing and waiting.
```

### Adapting Mid-Conversation

```markdown
## Initial (Technical) Response
"The service uses gRPC with Protocol Buffers for inter-service communication,
which gives us strongly-typed contracts and efficient binary serialization."

## After Signal: "I'm not sure what that means"
## Adapted (Simplified) Response
"Our services talk to each other using a fast, reliable messaging format.
Think of it like sending a precisely formatted form instead of a free-text
email -- the receiver always knows exactly what each field means, and the
message is smaller so it travels faster."

## After Signal: "Can you show me the code?"
## Adapted (Deeper) Response
"Here's the .proto definition and the Python client code..."
```

## Adaptation Rules

| Current Level | Signal Received | Action |
|--------------|----------------|--------|
| Technical | "What does X mean?" | Drop to Manager/Novice, define X |
| Technical | "Show me the code" | Stay Technical, add code examples |
| Manager | "What are the trade-offs?" | Escalate to Technical |
| Manager | "Just tell me what to do" | Stay Manager, lead with actions |
| Novice | "I get it, go deeper" | Escalate to Manager or Technical |
| Executive | "How does this work?" | Escalate to Manager level |
| Any | Silence / disengagement | Simplify and ask a question |

## Template: Adaptive Response Structure

```markdown
## [Topic Name]

**One-liner:** [Headline for everyone]

**For decision-makers:** [2-3 sentences: impact, cost, recommendation]

**For implementers:** [1-2 paragraphs: architecture, approach, trade-offs]

**Deep-dive:** [Code, config, specs -- link or expandable section]
```

## See Also

- [Audience Analysis](../concepts/audience-analysis.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [Analogies](../concepts/analogies.md)
- [Stakeholder Report](../patterns/stakeholder-report.md)
