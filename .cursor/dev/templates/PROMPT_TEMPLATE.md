# PROMPT: [NAME]

> Replace [NAME] with your task identifier (e.g., SPARK_KB, DATE_PARSER, CACHE_FEATURE)

---

## Goal

[One sentence describing what "done" looks like — be specific and verifiable]

---

## Quality Tier

<!-- Choose ONE tier that sets expectations for this task -->

**Tier:** production

| Tier | Expectations |
|------|--------------|
| `prototype` | Speed over perfection. Skip edge cases. Minimal tests. |
| `production` | Tests required. Best practices. Full verification. |
| `library` | Backward compatibility. Full documentation. API stability. |

---

## Context

[Optional: Background info, constraints, file references, or links to existing code/docs]

---

## Agentes (Dev Loop Executor)

<!--
OBRIGATÓRIO (prompt-crafter + dev-loop-executor): mapa visível de quem invocar com @ no Cursor.
Use caminhos completos: @.cursor/agents/<domínio>/<agente>.md — ver HOW_TO_USE_AGENTS.md.
Cada tarefa abaixo que precise de especialista deve começar pelo mesmo @ na linha da checkbox.
-->

| Etapa / necessidade | Agente (papel) | Caminho |
|---------------------|----------------|---------|
| [ex.: planejamento / ADR] | the-planner | `@.cursor/agents/communication/the-planner.md` |
| [ex.: implementação domínio] | (preencher) | `@.cursor/agents/...` |

---

## Tasks (Prioritized)

<!--
Priority Order: Execute RISKY first, then CORE, then POLISH
Mark tasks with: - [ ] (pending) or - [x] (done)
Prefix with @.cursor/agents/.../file.md quando for delegação explícita ao executor
Add verification with: Verify: `command`
-->

### 🔴 RISKY (Do First)
<!-- Architectural decisions, unknown unknowns, integration points -->

- [ ] `@.cursor/agents/...` — [Architectural or integration task]

### 🟡 CORE
<!-- Main feature implementation -->

- [ ] `@.cursor/agents/...` — [Main feature task]
- [ ] [Task with verification]: Verify: `python3 scripts/validate-agent-router.py`

### 🟢 POLISH (Do Last)
<!-- Cleanup, optimization, nice-to-haves -->

- [ ] `@.cursor/agents/code-quality/code-reviewer.md` — [Revisão final, se aplicável]

---

## Exit Criteria

<!--
List OBJECTIVE, VERIFIABLE conditions that indicate completion.
Each criterion should be checkable with a command.
-->

- [ ] Agent router validates: `python3 scripts/validate-agent-router.py`
- [ ] Dev Loop installer dry-run succeeds: `python3 install_dev_loop/install_dev_loop.py --dry-run --target .`
- [ ] File exists: `test -f path/to/expected/file`
- [ ] [Custom criterion]: `[verification command]`

---

## Progress

<!--
AUTO-UPDATED by the executor after each iteration.
This is the "memory bridge" that prevents token burn from re-exploration.
-->

**Status:** NOT_STARTED

| Iteration | Timestamp | Task Completed | Key Decision | Files Changed |
|-----------|-----------|----------------|--------------|---------------|
| - | - | - | - | - |

---

## Config

```yaml
mode: hitl                # hitl (human-in-loop) | afk (autonomous)
quality_tier: production  # prototype | production | library
max_iterations: 30        # Stop after N loops
max_retries: 3            # Retry failed tasks N times
circuit_breaker: 3        # Stop if no progress for N loops
small_steps: true         # One logical change per task
feedback_loops:           # Commands to run between tasks
  - python3 scripts/validate-agent-router.py
  - python3 install_dev_loop/install_dev_loop.py --dry-run --target .
```

---

## Notes

[Optional: Any additional notes, reminders, architectural decisions, or TODOs]

---

## References

<!-- Links to relevant documentation, PRDs, or external resources -->

- [Related PRD or Spec](.cursor/sdd/features/PRD_*.md)
- [External documentation](https://...)