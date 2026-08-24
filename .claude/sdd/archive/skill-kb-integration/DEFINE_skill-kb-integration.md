# DEFINE: Integração Skill ↔ KB (SDD, Dev Loop, vibecoding)

**Input:** `.claude/sdd/features/BRAINSTORM_skill-kb-integration.md` (pré-validado — 4 perguntas, 2 validações, 3 abordagens comparadas)

## Problem Statement

O projeto não tem uma convenção explícita para decidir quando um novo conteúdo deve virar Skill
nativa do Claude Code (`.claude/skills/`) ou permanecer como KB de referência (`.claude/kb/`), e o
fluxo SDD (`brainstorm-agent.md`, `design-agent.md`) e o roteador (`AGENT_ROUTER.yaml`) não sabem
que Skills existem — só enxergam `kb_reference`/`context_paths`. Sem essa convenção, o risco é
colisão de nome com o bundle vendor já instalado (~37 Skills Databricks/MLflow em `.claude/skills/`)
e inconsistência entre sessões (SDD vs Dev Loop vs vibecoding) sobre qual mecanismo usar.

## Target Users

| User | Papel | Pain Point |
|------|-------|------------|
| Agentes SDD (`brainstorm-agent`, `design-agent`) | Decidem contexto/sub-agentes nas fases 0 e 2 | Hoje só "enxergam" KB; podem reinventar como Skill em vez de reusar |
| Mantenedor do repositório (usuário) | Cria/organiza conteúdo agentic | Sem regra escrita, decisão de Skill-vs-KB fica ad-hoc, risco de colidir nome com bundle vendor |
| Sessões futuras (SDD, Dev Loop, vibecoding) | Consultam `.claude/rules/` automaticamente | Sem uma rule "skill-first", não há nudge consistente entre os três modos de uso |

## Goals

| Priority | Goal |
|----------|------|
| **MUST** | Criar `.claude/rules/skill-first.md` (+ mirrors `.cursor/`, `.github/`) com o critério de decisão Skill-vs-KB e convenção de prefixo de nome |
| **MUST** | Adicionar seção `skill_reference: []` (vazia, comentada) ao `AGENT_ROUTER.yaml` canônico (`.cursor/`) + mirrors `.claude/`, `.github/` |
| **MUST** | Estender `brainstorm-agent.md` (Gather Context) para checar `.claude/skills/` antes de assumir conteúdo de KB — 3 mirrors |
| **MUST** | Estender `design-agent.md` (seleção de sub-agentes) para considerar Skills como sinal de peso — 3 mirrors |
| **SHOULD** | Validar com `python3 scripts/validate-agent-router.py` ao final, garantindo que o schema novo não quebra o validador |
| **COULD** | Nenhum item COULD nesta rodada — escopo já foi cortado por YAGNI no brainstorm |

## Success Criteria

- [ ] `skill-first.md` existe e é idêntico (ou equivalente por path) nos 3 mirrors
- [ ] `AGENT_ROUTER.yaml` (fonte única `.cursor/`) tem `skill_reference: []` documentado, replicado nos mirrors
- [ ] `brainstorm-agent.md` e `design-agent.md` citam explicitamente `.claude/skills/` como fonte de contexto, nos 3 mirrors cada
- [ ] `python3 scripts/validate-agent-router.py` retorna OK após a mudança
- [ ] Nenhum arquivo de `.claude/kb/`, `.cursor/kb/`, `.github/kb/` foi movido, renomeado ou deletado

## Acceptance Tests

| ID | Cenário | Given | When | Then |
|----|---------|-------|------|------|
| AT-001 | Regra universal criada | Repositório sem `.claude/rules/skill-first.md` | `skill-first.md` é criado nos 3 mirrors | Arquivo existe em `.cursor/rules/`, `.claude/rules/`, `.github/rules/` com o mesmo critério de decisão |
| AT-002 | Schema do router preparado | `AGENT_ROUTER.yaml` sem `skill_reference` | Seção `skill_reference: []` é adicionada | `validate-agent-router.py` continua retornando `OK` sem erro |
| AT-003 | SDD fase 0 estendida | `brainstorm-agent.md` sem menção a Skills | Passo "Gather Context" é editado | Arquivo passa a instruir checar `.claude/skills/` antes de assumir KB, nos 3 mirrors |
| AT-004 | SDD fase 2 estendida | `design-agent.md` sem menção a Skills | Seleção de sub-agentes é editada | Arquivo passa a considerar Skills como sinal de peso, nos 3 mirrors |
| AT-005 | Nenhuma migração de conteúdo | `.claude/kb/` com 14 domínios | Feature é concluída | `git status` não mostra nenhum arquivo de `kb/` movido/deletado — só arquivos novos/editados listados acima |

## Out of Scope

- Migração de qualquer conteúdo real de `.claude/kb/` para `.claude/skills/` (nenhum domínio vira Skill nesta rodada)
- Validação automática de `skill_reference` em `scripts/validate-agent-router.py` (nada para validar ainda — seção fica vazia)
- Edição das fases do Dev Loop (`devloop-*.md`) — coberto pela rule universal em `.claude/rules/`, que já se aplica a qualquer sessão
- Estrutura de subpasta dedicada para Skills do projeto (`.claude/skills/project/`) — convenção escolhida foi prefixo de nome
- Skill como entidade roteável de primeira classe no `/intake` (`@Skill:<nome>`) — sem Skills próprias reais para rotear ainda

## Assumptions

| ID | Assumption | If Wrong, Impact | Validated? |
|----|------------|-------------------|------------|
| A-001 | O harness do Claude Code descobre `SKILL.md` em `.claude/skills/<nome>/` automaticamente, sem precisar de índice central | Baixo — esta feature é só documentação/schema, não depende de mudar a mecânica de descoberta | [x] — confirmado por observação: as ~37 Skills vendor já aparecem listadas automaticamente nas sessões deste repositório |
| A-002 | `scripts/validate-agent-router.py` não quebra ao encontrar um campo top-level novo (`skill_reference`) no YAML | Médio — precisaria ajustar o parser do validador se ele usar schema estrito | [ ] — validar rodando o script durante `/build` |
| A-003 | Convenção de prefixo de nome (sem subpasta) é suficiente para evitar colisão com o bundle vendor no médio prazo | Baixo-Médio — se o número de Skills próprias crescer muito, pode exigir reestruturação futura | [ ] — decisão de convenção do usuário, não testável agora |

## Contexto técnico (adaptado — sem infraestrutura GCP aplicável)

- **Localização:** feature toca só arquivos meta do próprio sistema agentic — `.claude/rules/`, `.claude/sdd/architecture/AGENT_ROUTER.yaml`, `.claude/agents/workflow/{brainstorm-agent,design-agent}.md` — e seus mirrors `.cursor/`, `.github/`. Não há `src/`, `functions/`, `gen/` ou `deploy/` envolvidos.
- **Domínio de KB relevante:** nenhum domínio de negócio (não é Spark/Databricks/SQL Capacity) — o "domínio" aqui é o próprio meta-sistema de roteamento e workflow (`AGENT_ROUTER.yaml`, SDD).
- **Impacto de infraestrutura:** nenhum — não há GCP, Terraform/Terragrunt ou recursos de nuvem envolvidos.

## Clarity Score: 15/15

| Elemento | Score | Justificativa |
|----------|-------|----------------|
| Problem | 3 | Claro, específico, acionável — já validado no brainstorm |
| Users | 3 | Identificados (agentes SDD, mantenedor, sessões futuras) com pain point claro |
| Goals | 3 | 4 MUST + 1 SHOULD, priorizados, sem ambiguidade |
| Success | 3 | Critérios testáveis (existência de arquivo, exit code do validador, git status) |
| Scope | 3 | Out of Scope explícito com 5 itens, herdado diretamente do YAGNI do brainstorm |

**Score ≥ 12/15 — segue para `/design` sem necessidade de perguntas adicionais.**

## Revisão do BRAINSTORM

Status atualizado em `BRAINSTORM_skill-kb-integration.md`: `Ready for Define` → `✅ Complete (Defined)`.

## Status: ✅ Shipped

_Shipped e arquivado em 2026-08-17. Ver `SHIPPED_2026-08-17.md` nesta mesma pasta._
