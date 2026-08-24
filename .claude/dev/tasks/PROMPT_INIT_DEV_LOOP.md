# PROMPT: INIT_DEV_LOOP

> Auto-bootstrapping PROMPT — adapts the Dev Loop framework to this specific project.
> Run this ONCE after `python install_dev_loop.py` to customize everything.

---

## Goal

Adapt the installed Dev Loop framework to this project's context: update documentation,
create a project-specific first PROMPT example, and ensure the .claude/dev/ structure
is ready for day-to-day use by a developer unfamiliar with the project.

---

## Quality Tier

**Tier:** production

---

## Context

- Dev Loop was just installed via `install_dev_loop.py`
- Installed files are in `.claude/dev/`, `.claude/agents/dev/`, `.claude/commands/dev/`
- Padronização multi-árvore também cobre `.cursor/` e `.github/` quando existirem no repositório
- This PROMPT should be idempotent — safe to run multiple times
- Goal: make Dev Loop feel native to THIS project, not generic

---

## Tasks (Prioritized)

### 🔴 RISKY (Do First)

- [x] Explore project structure to understand its tech stack, language, test framework, and linting tools: Verify: `ls -la`
- [x] Read existing CLAUDE.md (if present) to understand project conventions: Verify: `ls CLAUDE.md 2>/dev/null && echo "Found" || echo "Not found — will create section"`

### 🟡 CORE

- [x] Update `.claude/dev/templates/PROMPT_TEMPLATE.md` — replace generic `pytest`/`ruff` verification commands with the actual commands used in this project (e.g., `npm test`, `cargo test`, `go test ./...`, `mvn test`)
- [x] Create `.claude/dev/tasks/PROMPT_HELLO_WORLD.md` — a simple, project-specific first PROMPT that a developer can immediately execute to validate the Dev Loop setup (e.g., "add a utility function", "create a hello world module", "write a simple test")
- [x] Add a Dev Loop section to CLAUDE.md (create the file if it doesn't exist) with: quick-start commands, folder structure overview, and link to `.claude/dev/_index.md`
- [x] Update `.claude/agents/dev/dev-loop-executor.md` — add the project's main verification commands to the "feedback_loops" defaults section

### 🟢 POLISH (Do Last)

- [x] Verify all installed agent files have correct frontmatter (name, description, tools, model): Verify: `grep -l "^---" .claude/agents/dev/*.md | wc -l`
- [x] Create `.claude/dev/examples/readme.md` with a note about this project's first successful Dev Loop run (leave a placeholder if not yet run)

---

## Exit Criteria

- [x] PROMPT_TEMPLATE.md uses this project's actual test command: `rg "python3 scripts/validate-agent-router.py" .claude/dev/templates/PROMPT_TEMPLATE.md`
- [x] A project-specific PROMPT exists in tasks/: `test -f .claude/dev/tasks/PROMPT_HELLO_WORLD.md`
- [x] CLAUDE.md references Dev Loop: `rg "Dev Loop|/dev" CLAUDE.md`
- [x] Both agent files present: `test -f .claude/agents/dev/prompt-crafter.md && test -f .claude/agents/dev/dev-loop-executor.md`
- [x] Dev command present: `test -f .claude/commands/dev/dev.md`

---

## Progress

**Status:** COMPLETE

| Iteration | Timestamp | Task Completed | Key Decision | Files Changed |
|-----------|-----------|----------------|--------------|---------------|
| 1 | 2026-05-14 10:09 UTC-3 | Bootstrap Dev Loop customizado para o repo | Repo usa verificações nativas (`validate-agent-router` e dry-run do instalador), sem suite de app na raiz | `.claude/dev/templates/PROMPT_TEMPLATE.md`, `.claude/dev/tasks/PROMPT_HELLO_WORLD.md`, `CLAUDE.md`, `.claude/agents/dev/dev-loop-executor.md`, `.claude/dev/examples/readme.md` |
| 2 | 2026-05-14 10:16 UTC-3 | Bootstrap padronizado em `.cursor/` e `.github/` | O instalador passa a prever `--ecosystem all` para manter as árvores alinhadas quando o time usar mais de uma ferramenta | `.cursor/dev/**`, `.github/dev/**`, `.cursor/CURSOR.md`, `.github/CURSOR.md`, `.claude/CURSOR.md`, `install_dev_loop/install_dev_loop.py`, `install_dev_loop/INSTALL_DEV_LOOP.md`, `install_dev_loop/PROMPT_INIT_DEV_LOOP.md` |

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
  - ls .claude/dev/tasks/
  - ls .claude/agents/dev/
```

---

## Notes

**What this PROMPT does:**
1. Reads the project to understand its tech stack
2. Customizes the PROMPT_TEMPLATE with project-specific commands
3. Creates a first executable PROMPT tailored to the project
4. Documents Dev Loop in the project's CLAUDE.md

**After this PROMPT completes:**
```bash
# You're ready to use Dev Loop natively:
/dev "describe something you want to build in this project"

# Or execute the generated first PROMPT:
/dev tasks/PROMPT_HELLO_WORLD.md
```

---

## References

- [Dev Loop Documentation](.claude/dev/_index.md)
- [PROMPT Template](.claude/dev/templates/PROMPT_TEMPLATE.md)
- [Prompt Crafter Agent](.claude/agents/dev/prompt-crafter.md)
