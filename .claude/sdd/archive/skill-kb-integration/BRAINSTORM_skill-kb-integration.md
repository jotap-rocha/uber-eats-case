# BRAINSTORM: Integração Skill ↔ KB (SDD, Dev Loop, vibecoding)

## Initial Idea

O projeto usa `.claude/kb/` (KB de referência textual, lida deliberadamente por agentes/SDD) e
descobriu que `.claude/skills/` já existe, populado com ~37 Skills vendor (Databricks/MLflow),
mecanismo nativo do Claude Code (`SKILL.md` com frontmatter, auto-descoberto pela ferramenta
`Skill`). Em vez de renomear KB→Skills (colidiria com o bundle vendor), decidiu-se por um modelo
híbrido: **Skill = como fazer** (procedural, repetível), **KB = contexto/conceito** (o que é
verdade sobre X, contratos, convenções). Este brainstorm define como formalizar essa convenção e
"linkar" o uso de Skills ao SDD, ao Dev Loop e a sessões não-estruturadas ("vibecoding").

## Discovery Questions & Answers

| # | Pergunta | Resposta | Impacto |
|---|----------|----------|---------|
| 1 | Escopo do MVP: só regra + wiring, ou já migrar 1 Skill piloto? | Só regra + wiring no router/SDD | Nenhum conteúdo de KB migra nesta rodada — YAGNI aplicado |
| 2 | Como evitar colisão de nome com o bundle vendor (~37 Skills) quando o projeto criar Skills próprias? | Prefixo no nome (ex.: `sql-capacity-criar-pipeline/SKILL.md`) | Sem reestruturação de pastas; convenção de nomenclatura documentada na rule |
| 3 | Como representar Skills no `AGENT_ROUTER.yaml`, já que não existe nenhuma Skill própria ainda? | Preparar schema vazio (`skill_reference: []`) | Estrutura pronta, sem quebrar `validate-agent-router.py`, sem dado fictício |
| 4 | O nudge "verifique Skill antes de reinventar" deve tocar Dev Loop fase a fase? | Não — regra universal em `.claude/rules/`, cobre SDD + Dev Loop + vibecoding sem editar cada fase do Dev Loop | Evita tocar `devloop-*` individualmente; `.claude/rules/` já é lido em qualquer sessão |

## Approaches Explored

### Approach A: Documentação + convenção (schema vazio) ⭐ Recommended

**O que faz:** Cria `.claude/rules/skill-first.md` (regra universal, padrão `app-security-kb.md`),
adiciona seção `skill_reference: []` vazia e documentada no `AGENT_ROUTER.yaml`, e estende
`brainstorm-agent.md` + `design-agent.md` (fase 0 e 2 do SDD) para considerar Skills disponíveis
antes de assumir que algo é conteúdo de KB.

**Pros:**
- Nenhum código ou validação nova — risco mínimo, reversível
- `.claude/rules/` já é carregado em qualquer sessão (SDD, Dev Loop, vibecoding) — "linka" os três
  sem editar cada workflow individualmente
- Alinhado ao gate `use_sdd_when: multi_component_features, full_audit_trail_required` do próprio
  projeto (mexe em convenção cross-cutting usada por ~200+ arquivos)

**Cons:**
- Não valida automaticamente se `skill_reference` está correto (mas hoje `kb_reference` também não
  é validado — não é regressão)
- Só funciona se agentes de fato lerem a rule; não há enforcement de código

**Por que recomendo:** É o menor passo que resolve o problema real (falta de convenção explícita),
sem inventar infraestrutura para Skills que ainda não existem.

### Approach B: Validação forçada (estender `validate-agent-router.py`)

**O que faz:** Além de A, adiciona checagem no validador para `skill_reference` (existência de
`SKILL.md`, formato de nome com prefixo).

**Por que não recomendo agora:** O validador atual nem checa `kb_reference`/`context_paths`
existentes — adicionar rigor só para uma seção vazia, sem nenhuma Skill real, é validação sem
sujeito. Fica marcado como melhoria futura, quando `skill_reference` tiver entradas de verdade.

### Approach C: Skill como entidade roteável de primeira classe no `/intake`

**O que faz:** Estende `intake_contract`/`select_agents` para permitir `@Skill:<nome>` como
resultado de roteamento, não só `@agent-id`.

**Por que não recomendo agora:** Não há nenhuma Skill própria para rotear ainda — seria estrutura
de roteamento sem uso real. Reavaliar quando `skill_reference` tiver as primeiras entradas.

## Features Removed (YAGNI)

| Feature | Razão | Depois? |
|---------|-------|---------|
| Migração de conteúdo KB→Skill (qualquer domínio) | Fora do escopo deste MVP (Q1) | Sim — pilotar 1 domínio numa próxima feature |
| Validação automática de `skill_reference` (Approach B) | Nada para validar ainda; validador atual não valida `kb_reference` também | Sim — quando houver Skills reais |
| Edição fase a fase do Dev Loop (`devloop-*.md`) | Coberta pela rule universal em `.claude/rules/` (Q4) | Reavaliar se a rule universal não for suficiente na prática |
| Subpasta dedicada para Skills do projeto (`.claude/skills/project/`) | Prefixo de nome escolhido em vez disso (Q2) | Não planejado |
| Skill como entidade roteável no `/intake` (Approach C) | Sem Skills reais para rotear | Sim — quando `skill_reference` tiver entradas |

## Validações Incrementais

1. **Abordagem (só documentação + schema vazio, sem validador, sem tocar Dev Loop fase a fase):**
   confirmado pelo usuário — "Sim, faz sentido".
2. **Artefatos concretos (rule nova, seção no router, brainstorm-agent.md):** usuário pediu para
   estender também `design-agent.md` na mesma rodada, além de `brainstorm-agent.md` — incorporado.

## Draft Requirements (para /define)

1. Criar `.claude/rules/skill-first.md` — regra universal com critério de decisão Skill-vs-KB,
   convenção de prefixo de nome para Skills próprias, nota sobre auto-descoberta de Skill vs
   leitura deliberada de KB. Replicar em `.cursor/rules/` (canônico) e `.github/rules/` (mirror).
2. Adicionar seção `skill_reference: []` (vazia, comentada) ao `AGENT_ROUTER.yaml` — fonte única
   `.cursor/sdd/architecture/AGENT_ROUTER.yaml`, replicar em `.claude/` e `.github/`.
3. Estender `brainstorm-agent.md` (Gather Context, fase 0) e `design-agent.md` (fase 2, sinal de
   peso na seleção de sub-agentes) para considerar Skills disponíveis em `.claude/skills/` — 3
   mirrors cada.
4. Validar com `python3 scripts/validate-agent-router.py` ao final (garantir que a seção nova não
   quebra o schema esperado pelo validador).
5. Fora de escopo (ver Features Removed): nenhuma migração de conteúdo KB→Skill, nenhuma mudança
   em `validate-agent-router.py`, nenhuma mudança nas fases do Dev Loop, nenhum campo de roteamento
   novo no `/intake`.

## Status: ✅ Shipped

_Shipped e arquivado em 2026-08-17. Ver `SHIPPED_2026-08-17.md` nesta mesma pasta._
