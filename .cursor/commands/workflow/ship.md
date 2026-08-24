# Ship Command

> Archive completed feature with lessons learned (Phase 4)

## Usage

```bash
/ship <define-file>
```

## Examples

```bash
/ship .cursor/sdd/features/DEFINE_CLOUD_RUN_FUNCTIONS.md
/ship DEFINE_USER_AUTH.md
```

---

## Overview

This is **Phase 4** of the 5-phase AgentSpec workflow:

```text
Phase 0: /brainstorm → .cursor/sdd/features/BRAINSTORM_{FEATURE}.md (optional)
Phase 1: /define     → .cursor/sdd/features/DEFINE_{FEATURE}.md
Phase 2: /design     → .cursor/sdd/features/DESIGN_{FEATURE}.md
Phase 3: /build      → Code + .cursor/sdd/reports/BUILD_REPORT_{FEATURE}.md
Phase 4: /ship       → .cursor/sdd/archive/{FEATURE}/SHIPPED_{DATE}.md (THIS COMMAND)
```

The `/ship` command archives all feature artifacts and captures lessons learned.

---

## What This Command Does

1. **Verify** - Confirm all artifacts exist and build passed
2. **Archive** - Move feature documents to archive folder
3. **Document** - Create SHIPPED summary with lessons learned
4. **Clean** - Remove working files from features folder

---

## Process

### Step 1: Verify Completion

```markdown
Read(.cursor/sdd/features/DEFINE_{FEATURE}.md)
Read(.cursor/sdd/features/DESIGN_{FEATURE}.md)
Read(.cursor/sdd/reports/BUILD_REPORT_{FEATURE}.md)

# Verify build report shows success
```

### Step 2: Create Archive Folder

```bash
mkdir -p .cursor/sdd/archive/{FEATURE_NAME}/
```

### Step 3: Copy Artifacts to Archive

```bash
cp .cursor/sdd/features/DEFINE_{FEATURE}.md .cursor/sdd/archive/{FEATURE}/
cp .cursor/sdd/features/DESIGN_{FEATURE}.md .cursor/sdd/archive/{FEATURE}/
cp .cursor/sdd/reports/BUILD_REPORT_{FEATURE}.md .cursor/sdd/archive/{FEATURE}/
```

### Step 4: Generate SHIPPED Document

Create summary with:

| Section | Content |
|---------|---------|
| **Summary** | What was built |
| **Timeline** | Start → Ship dates |
| **Metrics** | Lines of code, files created |
| **Lessons Learned** | What went well, what to improve |
| **Artifacts** | List of all archived documents |

### Step 5: Update Document Statuses

Update archived documents to "Shipped" status:

```markdown
Edit: archive/{FEATURE}/DEFINE_{FEATURE}.md
  - Status: → "✅ Shipped"
  - Add revision: "Shipped and archived"

Edit: archive/{FEATURE}/DESIGN_{FEATURE}.md
  - Status: → "✅ Shipped"
  - Add revision: "Shipped and archived"
```

### Step 6: Clean Up Working Files

```bash
rm .cursor/sdd/features/DEFINE_{FEATURE}.md
rm .cursor/sdd/features/DESIGN_{FEATURE}.md
rm .cursor/sdd/reports/BUILD_REPORT_{FEATURE}.md
```

### Step 7: Save SHIPPED Document

```markdown
Write(.cursor/sdd/archive/{FEATURE}/SHIPPED_{DATE}.md)
```

---

## Output

| Artifact | Location |
|----------|----------|
| **SHIPPED** | `.cursor/sdd/archive/{FEATURE}/SHIPPED_{DATE}.md` |
| **DEFINE** | `.cursor/sdd/archive/{FEATURE}/DEFINE_{FEATURE}.md` |
| **DESIGN** | `.cursor/sdd/archive/{FEATURE}/DESIGN_{FEATURE}.md` |
| **BUILD_REPORT** | `.cursor/sdd/archive/{FEATURE}/BUILD_REPORT_{FEATURE}.md` |

**Next Step:** Start new feature with `/define`

---

## Quality Gate

Before shipping, verify:

```text
[ ] BUILD_REPORT shows all tasks completed
[ ] No critical issues in build report
[ ] All tests passing
[ ] Code deployed (if applicable)
```

---

## When to Ship

Ship when:
- All acceptance tests from DEFINE pass
- Build report shows 100% completion
- No blocking issues remain

---

## Lessons Learned Categories

Document lessons in these areas:

| Category | Example |
|----------|---------|
| **Process** | "Breaking tasks into smaller chunks helped" |
| **Technical** | "Config files work better than env vars" |
| **Communication** | "Early clarification saved rework" |
| **Tools** | "Using X library simplified Y" |

---

## Tips

1. **Don't Skip This** - Lessons learned prevent future mistakes
2. **Be Honest** - Document what didn't work too
3. **Be Specific** - "Better planning" → "Create architecture diagram before coding"
4. **Archive Everything** - Future you will thank present you

---

## References

- Agent: `.cursor/agents/workflow/ship-agent.md`
- Template: `.cursor/sdd/templates/SHIPPED_TEMPLATE.md`
- Contracts: `.cursor/sdd/architecture/WORKFLOW_CONTRACTS.yaml`
- Previous Phase: `.cursor/commands/workflow/build.md`