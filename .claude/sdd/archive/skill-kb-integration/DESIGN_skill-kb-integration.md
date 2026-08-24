# DESIGN: Integração Skill ↔ KB (SDD, Dev Loop, vibecoding)

**Input:** `.claude/sdd/features/DEFINE_skill-kb-integration.md` (Clarity Score 15/15)

## Architecture Overview

```text
┌──────────────────────────────────────────────────────────────────────┐
│                    CONVENÇÃO SKILL ↔ KB (meta-sistema)                │
├──────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  .claude/rules/skill-first.md(+.mdc)  ──┐   regra universal          │
│  .cursor/rules/skill-first.mdc          │   (lida em qualquer         │
│  .github/rules/skill-first.md(+.mdc)  ──┘    sessão: SDD/DevLoop/     │
│                    │                          vibecoding)             │
│                    │ referenciada por                                 │
│                    ▼                                                  │
│  AGENT_ROUTER.yaml (fonte .cursor/, mirrors .claude/, .github/)       │
│    kb_reference: [...]        (existente, inalterado)                 │
│    skill_reference: []        (novo, vazio, documentado)              │
│                    │                                                  │
│                    │ consumida por                                    │
│                    ▼                                                  │
│  SDD Fase 0                    SDD Fase 2                             │
│  brainstorm-agent.md            design-agent.md                       │
│  Gather Context ganha:          Match Criteria ganha linha:           │
│  Glob(.claude/skills/*/         "Skills disponíveis → sinal de        │
│    SKILL.md)                     peso Medium"                         │
│                                                                        │
└──────────────────────────────────────────────────────────────────────┘

Fora do diagrama (não tocado): .claude/kb/**, .claude/skills/** (bundle vendor),
Dev Loop (devloop-*.md), scripts/validate-agent-router.py
```

## Decision: Regra universal em `.claude/rules/` em vez de editar cada fase do Dev Loop

| Attribute | Value |
|-----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-17 |

**Context:** O pedido original incluía "linkar" Skills ao SDD, Dev Loop e vibecoding. Editar cada
fase do Dev Loop (`gate`, `requirements`, `design`, `craft`, `prompt_review`, `execute`, `reflect`)
individualmente tocaria 7+ arquivos sem necessidade, já que nenhuma delas tem hoje dependência de
KB (confirmado em investigação anterior nesta mesma sessão).

**Choice:** Uma única regra em `.claude/rules/` (+ mirrors), que o projeto já carrega
automaticamente em qualquer sessão via o mecanismo existente (mesmo padrão de `app-security-kb`).

**Rationale:** `.claude/rules/*.md`/`.mdc` já é o mecanismo deste repositório para nudges
universais — não precisa ser "religado" por workflow, já vale para SDD, Dev Loop e vibecoding
igualmente, sem trabalho extra.

**Alternatives Rejected:**
1. Editar cada fase do Dev Loop — rejeitado: redundante, sem ganho sobre a regra universal.
2. Não ter regra nenhuma, só confiar na extensão do `brainstorm-agent.md`/`design-agent.md` —
   rejeitado: não cobriria vibecoding (sessões fora do SDD nunca leriam esses agentes).

**Consequences:** A regra precisa ser escrita de forma genérica o bastante para fazer sentido fora
do contexto SDD também (não pode assumir que está numa fase de brainstorm).

## Decision: Replicar rule em formato duplo `.md` + `.mdc` nos mirrors, não só `.md`

| Attribute | Value |
|-----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-17 |

**Context:** O DEFINE assumia "3 mirrors" (`.md` em cada um de `.cursor`/`.claude`/`.github`).
Explorando o padrão existente (`app-security-kb`) durante o design, descobri que `.claude/rules/`
e `.github/rules/` já mantêm **duas versões** de cada rule: `<nome>.md` (markdown puro, sem
frontmatter) e `<nome>.mdc` (formato nativo Cursor, com frontmatter `description`/`globs`/
`alwaysApply`) — enquanto `.cursor/rules/` só tem `.mdc`. Esse é o padrão real e consistente nas
3 rules existentes (`app-security-kb`, `workflow-data-pipeline-review-handoff`,
`workflow-makeapp-review-handoff`), não uma anomalia isolada.

**Choice:** Seguir o padrão real: `.cursor/rules/skill-first.mdc` (1 arquivo), `.claude/rules/`
e `.github/rules/` com `skill-first.md` **e** `skill-first.mdc` (2 arquivos cada) — total 5
arquivos de rule, não 3.

**Rationale:** Consistência com o que já existe > o que o DEFINE assumiu antes de explorar o
código. Divergir criaria uma rule "diferente" das outras três sem motivo.

**Alternatives Rejected:**
1. Manter só `.md` nos 3 mirrors (como o DEFINE assumia) — rejeitado: quebraria o padrão
   estabelecido, a rule ficaria inconsistente com as outras 3 já existentes.
2. Consolidar tudo em só `.mdc` e eliminar a duplicação `.md`/`.mdc` existente — rejeitado:
   fora de escopo (seria refatorar as rules existentes, não esta feature).

**Consequences:** 2 arquivos a mais do que o DEFINE previu (14 no total, não 12) — atualiza a
Success Criteria implicitamente, mas os Acceptance Tests do DEFINE continuam válidos (AT-001 diz
"nos 3 mirrors", não "3 arquivos").

## File Manifest

| # | File | Action | Purpose | Agent | Rationale |
|---|------|--------|---------|-------|-----------|
| 1 | `.cursor/rules/skill-first.mdc` | Create | Regra canônica (formato Cursor) | @kb-architect | Dono da convenção de organização de conhecimento |
| 2 | `.claude/rules/skill-first.md` | Create | Mirror plano | @kb-architect | idem |
| 3 | `.claude/rules/skill-first.mdc` | Create | Mirror formato Cursor | @kb-architect | idem |
| 4 | `.github/rules/skill-first.md` | Create | Mirror plano | @kb-architect | idem |
| 5 | `.github/rules/skill-first.mdc` | Create | Mirror formato Cursor | @kb-architect | idem |
| 6 | `.cursor/sdd/architecture/AGENT_ROUTER.yaml` | Edit | Seção `skill_reference: []` | @agent-architect | Dono do schema do router |
| 7 | `.claude/sdd/architecture/AGENT_ROUTER.yaml` | Edit | idem (mirror) | @agent-architect | idem |
| 8 | `.github/sdd/architecture/AGENT_ROUTER.yaml` | Edit | idem (mirror) | @agent-architect | idem |
| 9 | `.cursor/agents/workflow/brainstorm-agent.md` | Edit | Gather Context considera Skills | @agent-architect | Dono de edição de arquivos de agente |
| 10 | `.claude/agents/workflow/brainstorm-agent.md` | Edit | idem (mirror) | @agent-architect | idem |
| 11 | `.github/agents/workflow/brainstorm-agent.md` | Edit | idem (mirror) | @agent-architect | idem |
| 12 | `.cursor/agents/workflow/design-agent.md` | Edit | Match Criteria considera Skills | @agent-architect | idem |
| 13 | `.claude/agents/workflow/design-agent.md` | Edit | idem (mirror) | @agent-architect | idem |
| 14 | `.github/agents/workflow/design-agent.md` | Edit | idem (mirror) | @agent-architect | idem |

Dependências: 1-5 são independentes entre si; 6-8 dependem conceitualmente de 1-5 (referenciam a
rule) mas não tecnicamente (podem ser criados em qualquer ordem); 9-14 idem.

## Code Pattern: conteúdo da rule `skill-first` (corpo comum, `{KB_PREFIX}` = `.cursor`/`.claude`/`.github`)

```markdown
# Convenção — Skill vs KB

Antes de criar conteúdo novo de referência ou procedimento reutilizável, decida onde ele pertence
— não crie um novo padrão de KB se já existir (ou fizer mais sentido como) uma Skill, e vice-versa.

## Critério de decisão

| Pergunta | Se SIM → | Local |
|----------|----------|-------|
| É um procedimento repetível, "como fazer X" (passo a passo acionável)? | **Skill** | `{KB_PREFIX}/skills/<nome>/SKILL.md` |
| É contexto, conceito, contrato ou "o que é verdade sobre X"? | **KB** | `{KB_PREFIX}/kb/<dominio>/...` |

## Descoberta — mecanismos diferentes

- **Skill**: auto-descoberta nativa pelo Claude Code via `SKILL.md` (frontmatter `name`/
  `description`/`compatibility`) — aparece automaticamente na listagem de skills disponíveis, sem
  precisar de índice manual.
- **KB**: leitura deliberada — um agente ou regra faz `Read()` explícito de um caminho específico
  (ex.: `{KB_PREFIX}/kb/_index.yaml`, `{KB_PREFIX}/kb/<dominio>/index.md`).

## Convenção de nome (evitar colisão com o bundle vendor)

`.claude/skills/` já contém Skills vendor (Databricks/MLflow — ex.: `databricks-core`,
`mlflow-onboarding`). Skills autoradas por este projeto usam **prefixo de domínio** no nome para
nunca colidir com atualizações futuras do bundle, ex.: `sql-capacity-criar-pipeline/SKILL.md`,
`teams-notificar-falha/SKILL.md`. Nunca usar nomes genéricos.

## Registro

`AGENT_ROUTER.yaml` tem a seção `skill_reference` (paralela a `kb_reference`) para registrar
Skills próprias do projeto quando existirem. Enquanto não houver nenhuma, a seção fica vazia
(`skill_reference: []`).

## Não migrar KB existente

Esta regra não implica migrar conteúdo já existente em `{KB_PREFIX}/kb/` para Skill — isso é
decisão caso a caso, feita deliberadamente (ver
`.claude/sdd/features/DESIGN_skill-kb-integration.md` para o histórico desta decisão).
```

Frontmatter a acrescentar nos arquivos `.mdc` (não nos `.md` planos, seguindo o padrão de
`app-security-kb`):

```yaml
---
description: Skill vs KB — decidir se conteúdo novo vira Skill nativa (.claude/skills/) ou KB de referência (.claude/kb/) antes de criar padrões novos
globs:
  - ".claude/**"
  - ".cursor/**"
  - ".github/**"
alwaysApply: false
---
```

## Code Pattern: append em `AGENT_ROUTER.yaml` (após `kb_reference`, mesma indentação)

```yaml
skill_reference: []
# Skills próprias do projeto (não o bundle vendor em .claude/skills/). Vazio até a primeira
# Skill autorada pelo projeto existir. Ver {KB_PREFIX}/rules/skill-first.md para o critério de
# decisão e a convenção de nome (prefixo de domínio, para não colidir com o bundle vendor).
# Formato de cada entrada, quando populado:
#   - skill_name: <nome>
#     path: {KB_PREFIX}/skills/<nome>/SKILL.md
#     used_by_roster_groups: [...]   # ou used_by_agent_ids: [...]
```

## Code Pattern: edição em `brainstorm-agent.md` (Step "1. Gather Context")

Antes:
```markdown
Read(.claude/CURSOR.MD)
Read(.claude/sdd/templates/BRAINSTORM_TEMPLATE.md)
Read(.claude/kb/_index.yaml)  # Available KB domains
Explore recent commits, existing code patterns, project structure
```

Depois:
```markdown
Read(.claude/CURSOR.MD)
Read(.claude/sdd/templates/BRAINSTORM_TEMPLATE.md)
Read(.claude/kb/_index.yaml)  # Available KB domains
Glob(.claude/skills/*/SKILL.md)  # Available Skills — ver .claude/rules/skill-first.md
Explore recent commits, existing code patterns, project structure
```

E adicionar item em "Observe for Define Phase":
```markdown
- Skills disponíveis → Se já existe uma Skill cobrindo "como fazer X", preferir referenciá-la em
  vez de desenhar um novo padrão de KB do zero (ver `.claude/rules/skill-first.md`)
```

## Code Pattern: edição em `design-agent.md` (tabela "Match Criteria", Step 5.1)

Antes:
```markdown
| Match Criteria | Weight | Example |
|----------------|--------|---------|
| File type (.py, .yaml, .tf) | High | `.tf` → ci-cd-specialist |
| Purpose keywords | High | "extraction" → extraction-specialist |
| Path patterns | Medium | `functions/` → function-developer |
| KB domains from DEFINE | Medium | gemini KB → extraction-specialist |
| Fallback | Low | Any .py → python-developer |
```

Depois (nova linha antes de Fallback):
```markdown
| Match Criteria | Weight | Example |
|----------------|--------|---------|
| File type (.py, .yaml, .tf) | High | `.tf` → ci-cd-specialist |
| Purpose keywords | High | "extraction" → extraction-specialist |
| Path patterns | Medium | `functions/` → function-developer |
| KB domains from DEFINE | Medium | gemini KB → extraction-specialist |
| Skills disponíveis (`.claude/skills/`) | Medium | Skill já cobre "como fazer X" → referenciar em vez de desenhar do zero (ver `.claude/rules/skill-first.md`) |
| Fallback | Low | Any .py → python-developer |
```

## Testing Strategy

| Test Type | Escopo | Comando de verificação | Mapeia p/ |
|-----------|--------|-------------------------|-----------|
| Existência de arquivo | 5 arquivos de rule | `ls .cursor/rules/skill-first.mdc .claude/rules/skill-first.{md,mdc} .github/rules/skill-first.{md,mdc}` | AT-001 |
| Schema do router | 3 `AGENT_ROUTER.yaml` | `python3 scripts/validate-agent-router.py` (deve retornar OK) + `grep -c "^skill_reference:" .cursor/.claude/.github .../AGENT_ROUTER.yaml` (1 cada) | AT-002 |
| Conteúdo brainstorm-agent | 3 mirrors | `grep -l "SKILL.md" .cursor/.claude/.github .../brainstorm-agent.md` (3 resultados) | AT-003 |
| Conteúdo design-agent | 3 mirrors | `grep -l "Skills disponíveis" .cursor/.claude/.github .../design-agent.md` (3 resultados) | AT-004 |
| Nenhuma migração de KB | Repositório inteiro | `git status --short -- '*/kb/*'` deve retornar vazio (nenhum arquivo de kb tocado) | AT-005 |

## Update DEFINE Status

`.claude/sdd/features/DEFINE_skill-kb-integration.md`: `Ready for Design` → `✅ Complete (Designed)`.

## Status: ✅ Shipped

_Shipped e arquivado em 2026-08-17. Ver `SHIPPED_2026-08-17.md` nesta mesma pasta._
