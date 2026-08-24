# PROMPT: EXAMPLE_KB

> Example PROMPT for AgentLoop — Building a Knowledge Base

---

## Goal

Create a complete Redis KB domain with quick-reference, concepts, and patterns following the KB architecture standards.

---

## Quality Tier

**Tier:** production

---

## Context

- KB domains live in `.github/kb/{domain}/`
- Must follow structure: quick-reference.md, concepts/, patterns/
- Registry is at `.github/kb/_index.yaml`
- See existing KB: `.github/kb/pydantic/` for reference

---

## Tasks (Prioritized)

### 🔴 RISKY (Do First)

- [ ] Validate KB structure requirements by reading `.github/kb/_index.yaml`
- [ ] Check if Redis domain already exists: Verify: `ls .github/kb/redis/ 2>/dev/null || echo "Domain not found"`

### 🟡 CORE

- [ ] @kb-architect: Create Redis KB domain structure
- [ ] Create quick-reference.md (max 100 lines): Verify: `wc -l .github/kb/redis/quick-reference.md | awk '{print ($1 <= 100) ? "OK" : "TOO_LONG"}'`
- [ ] Create concepts/data-structures.md: Verify: `ls .github/kb/redis/concepts/data-structures.md`
- [ ] Create concepts/persistence.md: Verify: `ls .github/kb/redis/concepts/persistence.md`
- [ ] Create patterns/caching.md: Verify: `ls .github/kb/redis/patterns/caching.md`

### 🟢 POLISH (Do Last)

- [ ] Update `.github/kb/_index.yaml` with Redis domain
- [ ] @code-reviewer: Review KB structure for completeness

---

## Exit Criteria

- [ ] Domain folder exists: `ls -la .github/kb/redis/`
- [ ] Quick reference exists: `ls .github/kb/redis/quick-reference.md`
- [ ] At least 2 concepts: `ls .github/kb/redis/concepts/ | wc -l | awk '{print ($1 >= 2) ? "OK" : "NEED_MORE"}'`
- [ ] At least 1 pattern: `ls .github/kb/redis/patterns/ | wc -l | awk '{print ($1 >= 1) ? "OK" : "NEED_MORE"}'`
- [ ] Registered in index: `grep -q "redis" .github/kb/_index.yaml && echo "OK" || echo "NOT_REGISTERED"`

---

## Progress

**Status:** NOT_STARTED

| Iteration | Timestamp | Task Completed | Key Decision | Files Changed |
|-----------|-----------|----------------|--------------|---------------|
| - | - | - | - | - |

---

## Config

```yaml
mode: hitl
quality_tier: production
max_iterations: 15
max_retries: 3
circuit_breaker: 3
small_steps: true
feedback_loops:
  - ls .github/kb/redis/
```

---

## Notes

This is an example PROMPT file demonstrating how to build a KB domain using AgentLoop.
Copy this file to `.github/dev/tasks/` and customize it for your use case.

---

## References

- [KB Architecture](.github/kb/_index.yaml)
- [Example KB: LLMOps](.github/kb/pydantic/)