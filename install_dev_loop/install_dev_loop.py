#!/usr/bin/env python3
"""
Dev Loop Installer v1.3
=======================
Installs the Agentic Development (Level 2) framework into any project.

Usage:
    python install_dev_loop.py                      # Install in current dir
    python install_dev_loop.py --target /path/to/project
    python install_dev_loop.py --ecosystem all      # Install .claude, .cursor and .github
    python install_dev_loop.py --force              # Overwrite existing files
    python install_dev_loop.py --dry-run            # Preview without writing
"""

import argparse
import shutil
import sys
from pathlib import Path
from typing import Optional

SUPPORTED_ECOSYSTEMS = ("claude", "cursor", "github")

# Workflow Dev Loop — paths relative to .cursor/ (copied to each ecosystem on install)
WORKFLOW_RELATIVE_PATHS = (
    "commands/workflow-dev-loop",
    "agents/workflow-dev-loop",
    "sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml",
    "sdd/architecture/AGENT_ROUTER_DEVLOOP_FRAGMENT.yaml",
    "sdd/architecture/AGENT_ROUTER_DEVLOOP_MERGE.md",
    "sdd/dev-loop-runs",
    "rules/workflow-dev-loop-handoff.mdc",
)

GUIDE_FILENAME = "DEV_LOOP_Guia_Comandos.md"

# ─────────────────────────────────────────────────────────────────────────────
# FILE PAYLOAD
# All Dev Loop files embedded here. Edit these to evolve the framework.
# ─────────────────────────────────────────────────────────────────────────────

FILES = {

# ── DOCUMENTATION ─────────────────────────────────────────────────────────────

".claude/dev/readme.md": """\
# Dev Loop

> **Agentic Development (Level 2)** — Ask first, execute perfectly, recover gracefully.

Dev Loop is a structured iteration system that sits between "vibe coding" and full
Spec-Driven Development (SDD). It provides PROMPT-driven task execution with
verification loops, session recovery, and intelligent agent orchestration.

---

## Quick Start

```bash
# Guided PROMPT creation (recommended)
/dev "I want to build a date parser utility"

# Execute an existing PROMPT
/dev tasks/PROMPT_DATE_PARSER.md

# Resume an interrupted session
/dev tasks/PROMPT_DATE_PARSER.md --resume

# Validate without executing
/dev tasks/PROMPT_DATE_PARSER.md --dry-run
```

---

## Folder Structure

```text
.claude/dev/
├── readme.md                        # This file
├── _index.md                        # Full documentation
├── tasks/                           # Your PROMPT files (active work)
│   └── PROMPT_*.md
├── progress/                        # Memory bridge (auto-managed)
│   └── PROGRESS_*.md
├── logs/                            # Execution logs (auto-generated)
│   └── LOG_*.md
└── templates/                       # Templates and examples
    ├── PROMPT_TEMPLATE.md
    ├── PROGRESS_TEMPLATE.md
    ├── PROMPT_EXAMPLE_FEATURE.md
    └── PROMPT_EXAMPLE_KB.md
```

---

## The 3-Level Development Spectrum

```text
LEVEL 1             LEVEL 2              LEVEL 3
Vibe Coding         Dev Loop             Spec-Driven Dev
───────────         ────────             ───────────────
• Just prompts      • PROMPT.md driven   • 8-phase pipeline
• No structure      • Verification loops • Full traceability
• Hope it works     • Agent leverage     • Quality gates
Time: < 30 min      Time: 1-4 hours      Time: Multi-day
Command: (none)     Command: /dev        Command: /build-feature
```

---

## Task Priority System

| Priority | Symbol | Execute Order | Use For |
|----------|--------|---------------|---------|
| RISKY | 🔴 | First | Fail fast on hard problems |
| CORE | 🟡 | Second | Main implementation |
| POLISH | 🟢 | Last | Cleanup and optimization |

---

## Quality Tiers

| Tier | Expectations |
|------|--------------|
| `prototype` | Speed over perfection. Minimal verification. |
| `production` | Tests required. Best practices. Full verification. |
| `library` | Backward compatibility. Full documentation. |

---

*Dev Loop v1.1 — Ask first, execute perfectly, recover gracefully*
""",

# ── TEMPLATES ─────────────────────────────────────────────────────────────────

".claude/dev/templates/PROMPT_TEMPLATE.md": """\
# PROMPT: [NAME]

> Replace [NAME] with your task identifier (e.g., SPARK_KB, DATE_PARSER, CACHE_FEATURE)

---

## Goal

[One sentence describing what "done" looks like — be specific and verifiable]

---

## Quality Tier

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

## Tasks (Prioritized)

<!--
Priority Order: Execute RISKY first, then CORE, then POLISH
Mark tasks with: - [ ] (pending) or - [x] (done)
Use @agent-name to invoke specific agents
Add verification with: Verify: `command`
-->

### 🔴 RISKY (Do First)
<!-- Architectural decisions, unknown unknowns, integration points -->

- [ ] [Architectural or integration task]

### 🟡 CORE
<!-- Main feature implementation -->

- [ ] [Main feature task]
- [ ] @agent-name: [Task that needs a specific agent]
- [ ] [Task with verification]: Verify: `pytest tests/test_foo.py`

### 🟢 POLISH (Do Last)
<!-- Cleanup, optimization, nice-to-haves -->

- [ ] [Cleanup or optimization task]

---

## Exit Criteria

<!--
List OBJECTIVE, VERIFIABLE conditions that indicate completion.
Each criterion should be checkable with a command.
-->

- [ ] All tests pass: `pytest --tb=short`
- [ ] Lint passes: `ruff check src/`
- [ ] File exists: `ls path/to/expected/file`
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
  - pytest
  - ruff check
```

---

## Notes

[Optional: Any additional notes, reminders, architectural decisions, or TODOs]
""",

".claude/dev/templates/PROGRESS_TEMPLATE.md": """\
# PROGRESS: [NAME]

> Memory bridge for Dev Loop iterations. Updated after each task completion.

---

## Summary

| Metric | Value |
|--------|-------|
| **PROMPT File** | `.claude/dev/tasks/PROMPT_[NAME].md` |
| **Started** | [timestamp] |
| **Last Updated** | [timestamp] |
| **Status** | IN_PROGRESS / COMPLETE / BLOCKED |
| **Tasks Completed** | 0 / N |
| **Current Iteration** | 1 |

---

## Iteration Log

### Iteration 1 — [timestamp]

**Task:** [Task description]
**Status:** PASS / FAIL / SKIPPED
**Agent:** [If @agent was used]
**Verification:** `[command]` → exit [code]

**Key Decisions:**
- [Decision made and reasoning]

**Files Changed:**
- `path/to/file.py` — [what changed]

**Notes for Next Iteration:**
- [Context that helps the next iteration]

---

## Blockers

| Blocker | Iteration | Resolution |
|---------|-----------|------------|
| - | - | - |

---

## Architecture Decisions

1. **[Decision]**: [Reasoning]

---

## Exit Criteria Status

| Criterion | Status | Last Checked |
|-----------|--------|--------------|
| All tests pass | ❌ | - |
| Lint passes | ❌ | - |
| [Custom] | ❌ | - |

---

*Dev Loop v1.1 — Memory bridge for session recovery*
""",

".claude/dev/templates/PROMPT_EXAMPLE_FEATURE.md": """\
# PROMPT: EXAMPLE_FEATURE

> Example PROMPT for Dev Loop — Building a Python utility

---

## Goal

Create a date parsing utility that handles multiple date formats and outputs ISO 8601.

---

## Quality Tier

**Tier:** production

---

## Context

- Target location: `src/utils/date_parser.py`
- Test location: `tests/test_date_parser.py`
- Must handle: ISO, US format (MM/DD/YYYY), EU format (DD/MM/YYYY)
- Use Python 3.10+ with type hints

---

## Tasks (Prioritized)

### 🔴 RISKY (Do First)

- [ ] Decide on date parsing library (dateutil vs manual): Document decision in Notes
- [ ] Create directory structure if needed: Verify: `mkdir -p src/utils tests`

### 🟡 CORE

- [ ] Create `src/utils/__init__.py`: Verify: `ls src/utils/__init__.py`
- [ ] @python-developer: Implement date_parser.py with parse_date() function
- [ ] Implement format detection logic: Verify: `python -c "from src.utils.date_parser import parse_date; print('Import OK')"`
- [ ] @test-generator: Create comprehensive tests for date_parser
- [ ] Run tests: Verify: `pytest tests/test_date_parser.py -v`

### 🟢 POLISH (Do Last)

- [ ] Add docstrings and type hints
- [ ] @code-reviewer: Review implementation for edge cases

---

## Exit Criteria

- [ ] Module imports: `python -c "from src.utils.date_parser import parse_date; print('OK')"`
- [ ] All tests pass: `pytest tests/test_date_parser.py --tb=short`

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
max_retries: 3
circuit_breaker: 3
small_steps: true
feedback_loops:
  - pytest tests/test_date_parser.py --tb=short
```
""",

".claude/dev/templates/PROMPT_EXAMPLE_KB.md": """\
# PROMPT: EXAMPLE_KB

> Example PROMPT for Dev Loop — Building a Knowledge Base domain

---

## Goal

Create a complete Redis KB domain with quick-reference, concepts, and patterns.

---

## Quality Tier

**Tier:** production

---

## Context

- KB domains live in `.claude/kb/{domain}/`
- Must follow structure: index.md, quick-reference.md, concepts/, patterns/
- Registry is at `.claude/kb/_index.yaml`

---

## Tasks (Prioritized)

### 🔴 RISKY (Do First)

- [ ] Check if domain already exists: Verify: `ls .claude/kb/redis/ 2>/dev/null || echo "Not found - OK to create"`
- [ ] Validate KB registry exists: Verify: `ls .claude/kb/_index.yaml`

### 🟡 CORE

- [ ] @kb-architect: Create Redis KB domain structure
- [ ] Create quick-reference.md (max 100 lines): Verify: `ls .claude/kb/redis/quick-reference.md`
- [ ] Create concepts/data-structures.md: Verify: `ls .claude/kb/redis/concepts/data-structures.md`
- [ ] Create patterns/caching.md: Verify: `ls .claude/kb/redis/patterns/caching.md`

### 🟢 POLISH (Do Last)

- [ ] Update `.claude/kb/_index.yaml` with new domain entry
- [ ] @code-reviewer: Review KB completeness

---

## Exit Criteria

- [ ] Domain folder exists: `ls -la .claude/kb/redis/`
- [ ] Quick reference exists: `ls .claude/kb/redis/quick-reference.md`
- [ ] Registered in index: `grep -q "redis" .claude/kb/_index.yaml && echo "OK"`

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
  - ls .claude/kb/redis/
```
""",

# ── AGENTS ────────────────────────────────────────────────────────────────────

".claude/agents/dev/prompt-crafter.md": """\
---
name: prompt-crafter
description: |
  Interactive PROMPT.md builder for Dev Loop (Agentic Development Level 2). Guides users through
  requirements gathering with targeted questions, then generates a ready-to-execute PROMPT file.
  The "PRD-crafter" for Dev Loop — ensures tasks are well-defined before execution.

  <example>
  Context: User wants to build something with Level 2
  user: "/dev I want to create a date parser utility"
  assistant: "I'll help you craft a PROMPT for your date parser. Let me ask a few questions..."
  </example>

  <example>
  Context: User has a vague idea
  user: "/dev add caching to the API"
  assistant: "Let me understand your caching requirements better..."
  </example>

tools: [Read, Write, Edit, Glob, Grep, AskUserQuestion, TodoWrite, Task]
model: sonnet
---

# Prompt Crafter

> **Identity:** Interactive PROMPT.md builder for Dev Loop
> **Domain:** Requirements gathering, task definition, exit criteria design
> **Philosophy:** Ask first, execute perfectly

---

## Core Workflow

```text
1. UNDERSTAND  → Parse user's initial request
2. EXPLORE     → Check codebase context (existing code, patterns)
3. ASK         → Targeted questions to clarify requirements
4. DESIGN      → Identify tasks, priorities, verifications
5. GENERATE    → Create complete PROMPT.md file
6. CONFIRM     → Present for user approval
7. HANDOFF     → Ready for /dev execution
```

---

## Phase 2: Explore

Before asking questions, gather context:

```text
1. Search for related code:    Grep for similar functionality
2. Check existing patterns:    Glob for similar file structures
3. Read relevant files:        Understand current architecture
4. Identify dependencies:      What this integrates with
```

---

## Phase 3: Ask (The Key Phase)

Use AskUserQuestion to clarify:

| Category | Questions to Ask |
|----------|------------------|
| **Scope** | What's the minimum viable version? Any features out of scope? |
| **Quality** | Prototype, production, or library? |
| **Integration** | What existing code does this interact with? |
| **Verification** | How will we know it works? What tests are needed? |
| **Risks** | What's the hardest part? Any unknowns? |

---

## Phase 4: Design

Based on answers, design:

1. **Goal Statement**: Single sentence, verifiable
2. **Quality Tier**: prototype | production | library
3. **Task Breakdown**:
   - 🔴 RISKY: Architectural decisions, unknowns
   - 🟡 CORE: Main implementation
   - 🟢 POLISH: Cleanup, optimization
4. **Verification Commands**: Objective, exit-code based
5. **Exit Criteria**: What defines "done"

---

## Phase 5: Generate

Create the PROMPT.md file at:
```
.claude/dev/tasks/PROMPT_{FEATURE_NAME}.md
```

---

## Phase 7: Handoff

Once approved:
```text
PROMPT READY
============
File: .claude/dev/tasks/PROMPT_{NAME}.md
Tasks: {count} (🔴{risky} 🟡{core} 🟢{polish})

To execute:
  /dev tasks/PROMPT_{NAME}.md
```

---

## Anti-Patterns

| Don't | Do Instead |
|-------|------------|
| Assume requirements | Ask clarifying questions |
| Skip codebase exploration | Check existing patterns first |
| Create vague tasks | Make tasks specific and atomic |
| Use subjective verifications | Use exit-code based checks |
| Generate without confirmation | Always confirm before handoff |

---

*Prompt Crafter v1.1 — Dev Loop's question-first PROMPT builder*
""",

".claude/agents/dev/dev-loop-executor.md": """\
---
name: dev-loop-executor
description: |
  Dev Loop executor for Agentic Development (Level 2). Processes PROMPT_*.md files with verification loops,
  circuit breakers, priority-based execution, and on-demand agent invocation.
  Supports session recovery via PROGRESS files and full audit trail via LOG files.

  <example>
  Context: User wants to execute a crafted PROMPT
  user: "/dev tasks/PROMPT_SPARK_KB.md"
  assistant: "I'll execute the Dev Loop for building the Spark KB."
  </example>

  <example>
  Context: User wants to resume an interrupted session
  user: "/dev tasks/PROMPT_CACHE.md --resume"
  assistant: "I'll resume the Dev Loop from where it left off."
  </example>

  <example>
  Context: User wants to validate without executing
  user: "/dev tasks/PROMPT_AUTH.md --dry-run"
  assistant: "I'll validate the PROMPT structure and show the execution plan."
  </example>

tools: [Read, Write, Edit, Bash, Grep, Glob, TodoWrite, Task]
model: sonnet
---

# Dev Loop Executor

> **Identity:** Dev Loop executor for Agentic Development (Level 2)
> **Domain:** Structured iteration, verification loops, session recovery
> **Philosophy:** Structure without ceremony, recovery without loss

---

## Execution Flow

```text
1. LOAD      → Read PROMPT.md + PROGRESS.md (memory bridge)
2. VALIDATE  → Check syntax, identify @agent references, parse config
3. INIT      → Create/update PROGRESS file if not exists
4. PICK      → Select next task by priority (RISKY → CORE → POLISH)
5. EXECUTE   → Run task (invoke @agent if specified)
6. VERIFY    → Run verification command (exit code check)
7. UPDATE    → Mark complete, update PROGRESS.md + PROMPT.md
8. CHECK     → Exit criteria met? Circuit breaker?
9. LOOP      → Continue until done or safeguard triggers
10. LOG      → Write execution log on completion
```

---

## Command Options

| Option | Description |
|--------|-------------|
| `--mode hitl` | Human-in-the-loop (default) — pause for review |
| `--mode afk` | Autonomous — run without pauses |
| `--resume` | Resume from existing PROGRESS file |
| `--dry-run` | Validate and show plan without executing |
| `--max N` | Override max iterations |

---

## Session Recovery (--resume)

```text
1. Read .claude/dev/progress/PROGRESS_{NAME}.md
2. Parse completed iterations and task status
3. Skip already-completed tasks (marked [x] in PROMPT)
4. Continue from last incomplete task
5. Preserve all previous key decisions and context
```

---

## Task Priority

| Section | Priority | Order |
|---------|----------|-------|
| `### 🔴 RISKY` | 1 (Highest) | Execute first |
| `### 🟡 CORE` | 2 | Execute second |
| `### 🟢 POLISH` | 3 (Lowest) | Execute last |

---

## Task Patterns

| Pattern | Meaning |
|---------|---------|
| `- [ ] Do X` | Plain task, execute directly |
| `- [ ] @agent: Do X` | Invoke agent via Task tool |
| `- [ ] Do X: Verify: 'cmd'` | Execute then verify |
| `- [x] Done` | Skip (already complete) |

---

## Safeguards

| Safeguard | Default | Purpose |
|-----------|---------|---------|
| `max_iterations` | 30 | Prevent infinite loops |
| `max_retries` | 3 | Retry failed tasks |
| `circuit_breaker` | 3 | Stop if no progress |
| `small_steps` | true | One logical change per task |

---

## Exit Conditions

| Exit | Description |
|------|-------------|
| EXIT_COMPLETE | All tasks done, criteria met |
| MAX_ITERATIONS | Reached iteration limit |
| CIRCUIT_BREAKER | No progress detected |
| USER_INTERRUPT | User stopped execution |
| VALIDATION_ERROR | PROMPT file invalid |

---

## Response on Start

```text
DEV LOOP STARTED
================
PROMPT: {path}
Goal: {goal}
Tasks: {count} (🔴{risky} 🟡{core} 🟢{polish})
Mode: {hitl/afk}

Progress: .claude/dev/progress/PROGRESS_{name}.md
Executing...
```

---

## Response on Complete

```text
EXIT_COMPLETE
=============
Tasks: {passed}/{total} passed
Duration: {HH:MM:SS}

Artifacts:
  Progress: .claude/dev/progress/PROGRESS_{name}.md
  Log: .claude/dev/logs/LOG_{name}_{ts}.md

All exit criteria met!
```

---

*Dev Loop Executor v1.1 — Agentic Development with Recovery*
""",

# ── COMMAND ───────────────────────────────────────────────────────────────────

".claude/commands/dev/dev.md": """\
# /dev Command

> **Dev Loop** — Agentic Development (Level 2) with structured iteration and intelligent routing.

## Usage

```bash
# Craft a new PROMPT (prompt-crafter guides you)
/dev "I want to build a date parser"

# Execute an existing PROMPT
/dev tasks/PROMPT_DATE_PARSER.md
/dev tasks/PROMPT_CACHE.md --mode afk

# Resume an interrupted session
/dev tasks/PROMPT_CACHE.md --resume

# Validate without executing
/dev tasks/PROMPT_AUTH.md --dry-run
```

## How It Works

The `/dev` command intelligently routes between two modes:

```text
User Input                              Action
──────────                              ──────

/dev "description"         →  prompt-crafter (ask questions, build PROMPT)
/dev tasks/PROMPT_*.md     →  dev-loop-executor (execute the PROMPT)
```

---

## Mode 1: Craft (New Request)

When you provide a description (not a file path), the **prompt-crafter** agent:

1. **Explores** the codebase for context
2. **Asks** targeted questions to clarify requirements
3. **Generates** a complete PROMPT.md file
4. **Confirms** with you before handoff

---

## Mode 2: Execute (Existing PROMPT)

When you provide a PROMPT file path, the **dev-loop-executor** agent:

1. **Loads** PROMPT.md + existing PROGRESS.md
2. **Picks** next task by priority (🔴→🟡→🟢)
3. **Executes** task (invokes @agent if specified)
4. **Verifies** with objective commands
5. **Updates** progress (memory bridge)
6. **Loops** until done or safeguard triggers

---

## Arguments

| Argument | Description |
|----------|-------------|
| `"description"` | Natural language request → triggers prompt-crafter |
| `tasks/PROMPT_*.md` | Path to PROMPT file → triggers executor |
| `--mode` | Execution mode: `hitl` (default) or `afk` |
| `--resume` | Resume from existing PROGRESS file |
| `--dry-run` | Validate and show plan without executing |
| `--max N` | Override max iterations (default: 30) |

---

## Complete Workflow

```text
1. /dev "I want to build X"        # Craft phase
   ↓
2. [Questions and clarifications]   # Interactive
   ↓
3. PROMPT.md generated              # Ready to execute
   ↓
4. /dev tasks/PROMPT_X.md           # Execute phase
   ↓
5. [Loop with verification]         # Automated
   ↓
6. EXIT_COMPLETE                    # Done
```

---

## Folder Structure

```text
.claude/dev/
├── tasks/        # Your PROMPT files (active work)
├── progress/     # Memory bridge (auto-managed)
├── logs/         # Execution logs
└── templates/    # Blank template + examples
```

---

*Dev Loop v1.1 — Ask first, execute perfectly, recover gracefully*
""",

# ── GITKEEP (empty directory placeholders) ────────────────────────────────────

".claude/dev/tasks/.gitkeep": "",
".claude/dev/progress/.gitkeep": "",
".claude/dev/logs/.gitkeep": "",
".claude/dev/examples/.gitkeep": "",

}

_SCRIPT_DIR = Path(__file__).resolve().parent
_ASSETS_DIR = _SCRIPT_DIR / "assets"

# ─────────────────────────────────────────────────────────────────────────────
# INSTALLER LOGIC
# ─────────────────────────────────────────────────────────────────────────────

GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BLUE   = "\033[94m"
RESET  = "\033[0m"
BOLD   = "\033[1m"


def print_banner():
    print(f"""
{BOLD}{BLUE}╔══════════════════════════════════════════════════╗
║        Dev Loop Installer v1.3                   ║
║  Agentic Development (Level 2) for any project   ║
╚══════════════════════════════════════════════════╝{RESET}
""")


def _load_asset(rel: str) -> Optional[str]:
    path = _ASSETS_DIR / rel
    if path.is_file():
        return path.read_text(encoding="utf-8")
    return None


def _load_prompt_init() -> Optional[str]:
    path = _SCRIPT_DIR / "PROMPT_INIT_DEV_LOOP.md"
    if path.is_file():
        return path.read_text(encoding="utf-8")
    return None


def _resolve_file_content(relative_path: str, default: str) -> str:
    if relative_path == ".claude/dev/_index.md":
        content = _load_asset("dev/_index.md")
        if content is None:
            raise FileNotFoundError(
                f"missing asset: {_ASSETS_DIR / 'dev/_index.md'} "
                "(sync from .cursor/dev/_index.md with __TREE__ paths)"
            )
        return content
    if relative_path == ".claude/dev/tasks/PROMPT_INIT_DEV_LOOP.md":
        content = _load_prompt_init()
        if content is None:
            raise FileNotFoundError(
                f"missing PROMPT_INIT: {_SCRIPT_DIR / 'PROMPT_INIT_DEV_LOOP.md'}"
            )
        return content
    return default


def _parse_ecosystems(ecosystem: str) -> tuple[str, ...]:
    if ecosystem == "all":
        return SUPPORTED_ECOSYSTEMS
    return (ecosystem,)


def _adapt_path(relative_path: str, ecosystem: str) -> str:
    return relative_path.replace(".claude/", f".{ecosystem}/", 1)


def _adapt_content(content: str, ecosystem: str) -> str:
    if "__TREE__" in content:
        content = content.replace("__TREE__", f".{ecosystem}")
    if ecosystem != "claude":
        content = content.replace(".claude", f".{ecosystem}")
    if ecosystem != "cursor":
        content = content.replace(".cursor", f".{ecosystem}")
    return content


def _adapt_workflow_content(content: str, ecosystem: str) -> str:
    content = content.replace(".cursor/", f".{ecosystem}/")
    if ecosystem != "claude":
        content = content.replace(".claude/", f".{ecosystem}/")
    return content


def _build_files(ecosystems: tuple[str, ...]) -> dict[str, str]:
    rendered_files: dict[str, str] = {}
    for ecosystem in ecosystems:
        for relative_path, content in FILES.items():
            content = _resolve_file_content(relative_path, content)
            rendered_files[_adapt_path(relative_path, ecosystem)] = _adapt_content(
                content, ecosystem
            )
        index_path = _adapt_path(".claude/dev/_index.md", ecosystem)
        prompt_init_path = _adapt_path(
            ".claude/dev/tasks/PROMPT_INIT_DEV_LOOP.md", ecosystem
        )
        rendered_files[index_path] = _adapt_content(
            _resolve_file_content(".claude/dev/_index.md", ""), ecosystem
        )
        rendered_files[prompt_init_path] = _adapt_content(
            _resolve_file_content(".claude/dev/tasks/PROMPT_INIT_DEV_LOOP.md", ""),
            ecosystem,
        )
    return rendered_files


def install_dev_loop_guide(
    target: Path,
    force: bool = False,
    dry_run: bool = False,
) -> tuple[list[str], list[str], list[tuple[str, str]]]:
    """Copy DEV_LOOP_Guia_Comandos.md to the target project root."""
    created: list[str] = []
    skipped: list[str] = []
    errors: list[tuple[str, str]] = []
    src = _ASSETS_DIR / GUIDE_FILENAME
    if not src.is_file():
        errors.append((GUIDE_FILENAME, f"missing in {_ASSETS_DIR}"))
        return created, skipped, errors

    dest = target / GUIDE_FILENAME
    if dest.exists() and not force:
        skipped.append(GUIDE_FILENAME)
        return created, skipped, errors

    if dry_run:
        created.append(GUIDE_FILENAME)
        return created, skipped, errors

    try:
        dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        created.append(GUIDE_FILENAME)
    except Exception as exc:
        errors.append((GUIDE_FILENAME, str(exc)))

    return created, skipped, errors


def _workflow_bundle_root() -> Path:
    """Portable bundle next to this script; fallback to repo .cursor when developing."""
    bundle = Path(__file__).resolve().parent / "workflow_bundle" / "cursor"
    if bundle.exists():
        return bundle
    repo_cursor = Path(__file__).resolve().parent.parent / ".cursor"
    if repo_cursor.exists():
        return repo_cursor
    return bundle


def install_workflow_dev_loop(
    target: Path,
    ecosystems: tuple[str, ...],
    force: bool = False,
    dry_run: bool = False,
) -> tuple[list[str], list[str], list[tuple[str, str]]]:
    """Install workflow-dev-loop commands, agents, SDD contracts and templates."""
    created: list[str] = []
    skipped: list[str] = []
    errors: list[tuple[str, str]] = []
    bundle_root = _workflow_bundle_root()

    if not bundle_root.exists():
        errors.append(
            (
                "workflow-dev-loop",
                f"workflow bundle not found at {bundle_root}",
            )
        )
        return created, skipped, errors

    for ecosystem in ecosystems:
        for rel in WORKFLOW_RELATIVE_PATHS:
            src = bundle_root / rel
            if not src.exists():
                errors.append((f".{ecosystem}/{rel}", "missing in workflow bundle"))
                continue

            dest_base = target / f".{ecosystem}" / rel
            if src.is_file():
                dest = dest_base
                rel_dest = f".{ecosystem}/{rel}"
                if dest.exists() and not force:
                    skipped.append(rel_dest)
                    continue
                if dry_run:
                    created.append(rel_dest)
                    continue
                try:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    text = _adapt_workflow_content(
                        src.read_text(encoding="utf-8"), ecosystem
                    )
                    dest.write_text(text, encoding="utf-8")
                    created.append(rel_dest)
                except Exception as exc:
                    errors.append((rel_dest, str(exc)))
            else:
                for src_file in src.rglob("*"):
                    if src_file.is_dir():
                        continue
                    file_rel = src_file.relative_to(bundle_root)
                    dest_file = target / f".{ecosystem}" / file_rel
                    rel_dest = f".{ecosystem}/{file_rel.as_posix()}"
                    if dest_file.exists() and not force:
                        skipped.append(rel_dest)
                        continue
                    if dry_run:
                        created.append(rel_dest)
                        continue
                    try:
                        dest_file.parent.mkdir(parents=True, exist_ok=True)
                        if src_file.suffix in {".md", ".yaml", ".mdc", ".yml"}:
                            text = _adapt_workflow_content(
                                src_file.read_text(encoding="utf-8"), ecosystem
                            )
                            dest_file.write_text(text, encoding="utf-8")
                        else:
                            shutil.copy2(src_file, dest_file)
                        created.append(rel_dest)
                    except Exception as exc:
                        errors.append((rel_dest, str(exc)))

    return created, skipped, errors


def install(
    target: Path,
    force: bool = False,
    dry_run: bool = False,
    ecosystem: str = "claude",
) -> None:
    created = []
    skipped = []
    errors = []
    ecosystems = _parse_ecosystems(ecosystem)
    files = _build_files(ecosystems)

    for relative_path, content in files.items():
        dest = target / relative_path
        dest.parent.mkdir(parents=True, exist_ok=True)

        if dest.exists() and not force:
            skipped.append(relative_path)
            continue

        if dry_run:
            created.append(relative_path)
            continue

        try:
            dest.write_text(content, encoding="utf-8")
            created.append(relative_path)
        except Exception as e:
            errors.append((relative_path, str(e)))

    wf_created, wf_skipped, wf_errors = install_workflow_dev_loop(
        target, ecosystems, force=force, dry_run=dry_run
    )
    created.extend(wf_created)
    skipped.extend(wf_skipped)
    errors.extend(wf_errors)

    guide_created, guide_skipped, guide_errors = install_dev_loop_guide(
        target, force=force, dry_run=dry_run
    )
    created.extend(guide_created)
    skipped.extend(guide_skipped)
    errors.extend(guide_errors)

    _print_report(target, created, skipped, errors, dry_run, ecosystems)


def _print_report(
    target: Path,
    created: list,
    skipped: list,
    errors: list,
    dry_run: bool,
    ecosystems: tuple[str, ...],
) -> None:
    action = "Would create" if dry_run else "Created"
    prefix  = f"{YELLOW}[DRY RUN]{RESET} " if dry_run else ""
    ecosystem_label = ", ".join(f".{name}" for name in ecosystems)

    print(f"{prefix}{BOLD}Target:{RESET} {target}\n")
    print(f"{BOLD}Ecosystems:{RESET} {ecosystem_label}\n")

    if created:
        print(f"{GREEN}{action} ({len(created)} files):{RESET}")
        for path in created:
            print(f"  {GREEN}+{RESET} {path}")

    if skipped:
        print(f"\n{YELLOW}Skipped — already exists ({len(skipped)} files):{RESET}")
        for path in skipped:
            print(f"  {YELLOW}~{RESET} {path}")
        print(f"\n  {YELLOW}Tip:{RESET} use --force to overwrite existing files.")

    if errors:
        print(f"\n{RED}Errors ({len(errors)}):{RESET}")
        for path, err in errors:
            print(f"  {RED}✗{RESET} {path}: {err}")

    if not errors:
        print(f"""
{BOLD}{'[DRY RUN] ' if dry_run else ''}Installation complete!{RESET}

{BOLD}Next steps:{RESET}

  1. {BLUE}Open the project in your AI coding tool{RESET}

  2. {BLUE}Run the PROMPT to customize Dev Loop to your project:{RESET}
     /dev tasks/PROMPT_INIT_DEV_LOOP.md

  3. {BLUE}Start using Dev Loop:{RESET}
     /dev "describe what you want to build"

  4. {BLUE}Or use the structured workflow:{RESET}
     /workflow-dev-loop
     /devloop-init my-feature

{BOLD}Full documentation:{RESET} {', '.join(f'.{name}/dev/_index.md' for name in ecosystems)}
{BOLD}Workflow commands:{RESET} {', '.join(f'.{name}/commands/workflow-dev-loop/' for name in ecosystems)}
{BOLD}Human guide:{RESET} {GUIDE_FILENAME} (project root)
{BOLD}Router merge:{RESET} see AGENT_ROUTER_DEVLOOP_MERGE.md under each installed .claude/.cursor/.github tree
""")
    else:
        print(f"\n{RED}Installation finished with errors. Check the report above.{RESET}")
        sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Install Dev Loop (Agentic Development Level 2) into a project.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python install_dev_loop.py
  python install_dev_loop.py --target /path/to/my-project
  python install_dev_loop.py --ecosystem cursor
  python install_dev_loop.py --ecosystem all
  python install_dev_loop.py --force
  python install_dev_loop.py --dry-run
        """,
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.cwd(),
        help="Target project directory (default: current directory)",
    )
    parser.add_argument(
        "--ecosystem",
        choices=(*SUPPORTED_ECOSYSTEMS, "all"),
        default="claude",
        help="Dev Loop tree to install: claude, cursor, github, or all (default: claude)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be created without writing any files",
    )
    args = parser.parse_args()

    target = args.target.resolve()

    if not target.exists():
        print(f"{RED}Error: target directory does not exist: {target}{RESET}")
        sys.exit(1)

    print_banner()
    install(
        target=target,
        force=args.force,
        dry_run=args.dry_run,
        ecosystem=args.ecosystem,
    )


if __name__ == "__main__":
    main()
