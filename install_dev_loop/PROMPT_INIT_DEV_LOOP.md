# PROMPT: INIT_DEV_LOOP

> Auto-bootstrapping PROMPT — adapts the Dev Loop framework to this specific project.
> Run this ONCE after `python install_dev_loop.py` to customize everything.

---

## Goal

Adapt the installed Dev Loop framework to this project's context: update documentation,
create a project-specific first PROMPT example, validate the structured workflow
(`workflow-dev-loop`), and ensure the selected Dev Loop structure is ready for day-to-day
use by a developer unfamiliar with the project.

---

## Quality Tier

**Tier:** production

---

## Context

- Dev Loop was just installed via `install_dev_loop.py`
- Default install target is `.claude/`; multi-tree install is available with `--ecosystem all`
- Supported trees are `.claude/`, `.cursor/`, and `.github/`
- The installer also copies `workflow-dev-loop` (commands, agents, CONTRACTS, `dev-loop-runs/`) and `DEV_LOOP_Guia_Comandos.md` at the project root
- This PROMPT should be idempotent — safe to run multiple times
- Goal: make Dev Loop feel native to THIS project, not generic

---

## Tasks (Prioritized)

### 🔴 RISKY (Do First)

- [ ] Explore project structure to understand its tech stack, language, test framework, and linting tools: Verify: `ls -la`
- [ ] Identify installed Dev Loop trees and choose the trees to customize (`.claude`, `.cursor`, `.github`): Verify: `test -d .claude/dev && echo ".claude/dev found" || true; test -d .cursor/dev && echo ".cursor/dev found" || true; test -d .github/dev && echo ".github/dev found" || true`
- [ ] Read existing project context files (`CLAUDE.md`, `.cursor/CURSOR.md`, `.github/CURSOR.md`, if present) to understand conventions: Verify: `test -f CLAUDE.md || test -f .cursor/CURSOR.md || test -f .github/CURSOR.md`
- [ ] Confirm structured workflow is installed in each selected tree: Verify: `for r in .claude .cursor .github; do test -f "$r/commands/workflow-dev-loop/workflow-dev-loop.md" && echo "$r workflow OK" || true; done`
- [ ] Confirm human guide at project root: Verify: `test -f DEV_LOOP_Guia_Comandos.md && head -5 DEV_LOOP_Guia_Comandos.md`

### 🟡 CORE

- [ ] Update each installed `dev/templates/PROMPT_TEMPLATE.md` — replace generic `pytest`/`ruff` verification commands with the actual commands used in this project
- [ ] Create `dev/tasks/PROMPT_HELLO_WORLD.md` in each selected tree — a simple, project-specific first PROMPT that validates the Dev Loop setup
- [ ] Add or update a Dev Loop section in the relevant context docs (`CLAUDE.md`, `.cursor/CURSOR.md`, `.github/CURSOR.md`) with quick-start commands, folder structure overview, links to each `dev/_index.md`, and pointer to `DEV_LOOP_Guia_Comandos.md` + `/workflow-dev-loop`
- [ ] Update each installed `agents/dev/dev-loop-executor.md` — add the project's main verification commands to the `feedback_loops` defaults section
- [ ] If `sdd/architecture/AGENT_ROUTER.yaml` exists, merge Dev Loop entries from `sdd/architecture/AGENT_ROUTER_DEVLOOP_FRAGMENT.yaml` following `AGENT_ROUTER_DEVLOOP_MERGE.md` (or document that merge is N/A): Verify: `test -f .cursor/sdd/architecture/AGENT_ROUTER_DEVLOOP_MERGE.md || test -f .claude/sdd/architecture/AGENT_ROUTER_DEVLOOP_MERGE.md || true`
- [ ] Create an example RUN for workflow smoke test (replace `hello-devloop` with a project-specific RUN_ID): run `/devloop-init hello-devloop` then document in `dev/examples/readme.md` that gate phase is the next step (`/devloop-phase hello-devloop gate`) without executing all phases in this PROMPT unless the user requests it

### 🟢 POLISH (Do Last)

- [ ] Verify installed agent files have correct frontmatter (name, description, tools, model): Verify: `python - <<'PY'\nfrom pathlib import Path\nfor root in ('.claude', '.cursor', '.github'):\n    agents = Path(root, 'agents/dev')\n    if agents.exists():\n        print(root, len(list(agents.glob('*.md'))))\nPY`
- [ ] Create or update each `dev/examples/readme.md` with a note about this project's first successful Dev Loop run (leave a placeholder if not yet run)
- [ ] Add a one-line reference to `/workflow-dev-loop` in each installed `dev/readme.md` if present

---

## Exit Criteria

- [ ] PROMPT_TEMPLATE.md uses this project's actual verification commands in each selected tree
- [ ] A project-specific `PROMPT_HELLO_WORLD.md` exists in each selected tree
- [ ] Relevant context docs reference Dev Loop, `/dev`, and the structured workflow (`/workflow-dev-loop`)
- [ ] `DEV_LOOP_Guia_Comandos.md` exists at project root and is linked from context or `dev/_index.md`
- [ ] `commands/workflow-dev-loop/` exists in each selected ecosystem tree
- [ ] Example RUN folder exists under `sdd/dev-loop-runs/` (e.g. `hello-devloop/`) OR merge doc explains deferring RUN creation
- [ ] Dev Loop agent files are present in each selected tree
- [ ] Dev command is present in each selected tree

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
max_iterations: 20
max_retries: 2
circuit_breaker: 3
small_steps: true
feedback_loops:
  - test -d .claude/dev || test -d .cursor/dev || test -d .github/dev
  - test -f install_dev_loop/install_dev_loop.py || test -f install_dev_loop.py || true
  - test -f DEV_LOOP_Guia_Comandos.md
  - for r in .claude .cursor .github; do test -f "$r/commands/workflow-dev-loop/workflow-dev-loop.md" || true; done
```

---

## Notes

**What this PROMPT does:**
1. Reads the project to understand its tech stack
2. Customizes the PROMPT_TEMPLATE with project-specific commands
3. Creates a first executable PROMPT tailored to the project
4. Documents Dev Loop in the project context files
5. Validates and documents the structured workflow (`workflow-dev-loop`)
6. Keeps `.claude/`, `.cursor/`, and `.github/` aligned when those trees are installed

**After this PROMPT completes:**
```bash
# You're ready to use Dev Loop natively:
/dev "describe something you want to build in this project"

# Or execute the generated first PROMPT:
/dev tasks/PROMPT_HELLO_WORLD.md

# Or use the structured workflow (recommended for features with RUN/manifest):
/workflow-dev-loop
/devloop-init <RUN_ID>
/devloop-phase <RUN_ID> gate
```

See also: `DEV_LOOP_Guia_Comandos.md` at the project root.

---

## References

- [Dev Loop Documentation](../_index.md)
- [PROMPT Template](../templates/PROMPT_TEMPLATE.md)
- [Prompt Crafter Agent](../../agents/dev/prompt-crafter.md)
- [Workflow Dev Loop](../../commands/workflow-dev-loop/workflow-dev-loop.md)
- [DEV_LOOP_Guia_Comandos.md](../../../../DEV_LOOP_Guia_Comandos.md) (project root)
- [AGENT_ROUTER merge](../../sdd/architecture/AGENT_ROUTER_DEVLOOP_MERGE.md) (if present)
