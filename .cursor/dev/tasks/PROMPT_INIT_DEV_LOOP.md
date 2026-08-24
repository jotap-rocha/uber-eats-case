# PROMPT: INIT_DEV_LOOP

> Auto-bootstrapping PROMPT — adapts the Dev Loop framework to this specific project.
> Run this ONCE after `python install_dev_loop.py --ecosystem cursor` or `python install_dev_loop.py --ecosystem all` to customize everything.

---

## Goal

Adapt the installed Dev Loop framework to this project's context: update documentation,
create a project-specific first PROMPT example, and ensure the `.cursor/dev/` structure
is ready for day-to-day use by a developer unfamiliar with the project.

---

## Quality Tier

**Tier:** production

---

## Context

- Dev Loop was just installed via `install_dev_loop.py`
- Installed files are in `.cursor/dev/`, `.cursor/agents/dev/`, `.cursor/commands/dev/`
- This PROMPT should be idempotent — safe to run multiple times
- Goal: make Dev Loop feel native to THIS project, not generic

---

## Tasks (Prioritized)

### 🔴 RISKY (Do First)

- [x] Explore project structure to understand its tech stack, language, test framework, and linting tools: Verify: `ls -la`
- [x] Read existing Cursor context (if present) to understand project conventions: Verify: `test -f .cursor/CURSOR.md && echo "Found" || echo "Not found — will create section"`

### 🟡 CORE

- [x] Update `.cursor/dev/templates/PROMPT_TEMPLATE.md` — replace generic `pytest`/`ruff` verification commands with the actual commands used in this project
- [x] Create `.cursor/dev/tasks/PROMPT_HELLO_WORLD.md` — a simple, project-specific first PROMPT that a developer can immediately execute to validate the Dev Loop setup
- [x] Add a Dev Loop section to `.cursor/CURSOR.md` with quick-start commands, folder structure overview, and link to `.cursor/dev/_index.md`
- [x] Update `.cursor/agents/dev/dev-loop-executor.md` — add the project's main verification commands to the `feedback_loops` defaults section

### 🟢 POLISH (Do Last)

- [x] Verify all installed agent files have correct frontmatter (name, description, tools, model): Verify: `grep -l "^---" .cursor/agents/dev/*.md | wc -l`
- [x] Create `.cursor/dev/examples/readme.md` with a note about this project's first successful Dev Loop run (leave a placeholder if not yet run)

---

## Exit Criteria

- [x] PROMPT_TEMPLATE.md uses this project's actual test command: `rg "python3 scripts/validate-agent-router.py" .cursor/dev/templates/PROMPT_TEMPLATE.md`
- [x] A project-specific PROMPT exists in tasks/: `test -f .cursor/dev/tasks/PROMPT_HELLO_WORLD.md`
- [x] Cursor context references Dev Loop: `rg "Dev Loop|/dev" .cursor/CURSOR.md`
- [x] Both agent files present: `test -f .cursor/agents/dev/prompt-crafter.md && test -f .cursor/agents/dev/dev-loop-executor.md`
- [x] Dev command present: `test -f .cursor/commands/dev/dev.md`

---

## Progress

**Status:** COMPLETE

| Iteration | Timestamp | Task Completed | Key Decision | Files Changed |
|-----------|-----------|----------------|--------------|---------------|
| 1 | 2026-05-14 10:16 UTC-3 | Bootstrap Dev Loop padronizado para `.cursor/` | Repo usa verificações nativas (`validate-agent-router` e dry-run do instalador), sem suite de app na raiz | `.cursor/dev/templates/PROMPT_TEMPLATE.md`, `.cursor/dev/tasks/PROMPT_HELLO_WORLD.md`, `.cursor/CURSOR.md`, `.cursor/agents/dev/dev-loop-executor.md`, `.cursor/dev/examples/readme.md` |

---

## Config

```yaml
mode: hitl
quality_tier: production
max_iterations: 15
max_retries: 2
circuit_breaker: 3
small_steps: true
feedback_loops:
  - python3 scripts/validate-agent-router.py
  - python3 install_dev_loop/install_dev_loop.py --dry-run --target .
```

---

## Notes

**What this PROMPT does:**
1. Reads the project to understand its tech stack
2. Customizes the PROMPT_TEMPLATE with project-specific commands
3. Creates a first executable PROMPT tailored to the project
4. Documents Dev Loop in `.cursor/CURSOR.md`

**After this PROMPT completes:**
```bash
# You're ready to use Dev Loop natively:
/dev "describe something you want to build in this project"

# Or execute the generated first PROMPT:
/dev tasks/PROMPT_HELLO_WORLD.md
```

---

## References

- [Dev Loop Documentation](../_index.md)
- [PROMPT Template](../templates/PROMPT_TEMPLATE.md)
- [Prompt Crafter Agent](../../agents/dev/prompt-crafter.md)
