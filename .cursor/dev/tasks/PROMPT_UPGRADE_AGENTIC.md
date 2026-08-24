# PROMPT: UPGRADE_AGENTIC — merge pós `upgrade_agentic.py`

> Execute após `python3 agentspec/upgrade_agentic.py --target <projeto> --apply`.
> Objetivo: resolver conflitos listados em `.agentic-upgrade/UPGRADE_REPORT.md` sem perder customizações do projeto.

---

## Goal

Fundir, arquivo a arquivo, o que o instalador deixou em conflito: manter regras de negócio e paths locais; incorporar comandos, workflows, KB e contratos SDD novos do template.

---

## Quality Tier

**Tier:** production

---

## Context

- Relatório: `.agentic-upgrade/UPGRADE_REPORT.md`
- Template (incoming): `.agentic-upgrade/incoming/<rel-path>`
- Destino preservado: `.agentic-upgrade/preserved/<rel-path>` ou o arquivo vivo no repo
- **Não alterar:** `agents/domain/*-expert.md`, `CONTEXT.md`, `README.md`, `.cursorrules`, `dev/tasks/PROMPT_*.md` locais (exceto bootstrap `PROMPT_INIT_*`, `PROMPT_HELLO_WORLD`)

---

## Tasks

### 🔴 RISKY (Do First)

- [ ] Ler `UPGRADE_REPORT.md` e listar conflitos por categoria: `commands/`, `agents/`, `kb/`, `sdd/`, `rules/`
- [ ] Para cada `AGENT_ROUTER.yaml` / fragmentos YAML: confirmar que `upgrade_agentic.py` já mergeou; só ajustar entradas manuais se o relatório indicar

### 🟡 CORE

- [ ] **Comandos** (`.cursor/commands/`): para cada conflito, unir instruções novas do template sem remover handoffs ou RUN_ID específicos do projeto
- [ ] **Agentes** (`.cursor/agents/`): acrescentar seções/KB links do template; preservar exemplos e escopo local no corpo do agente destino
- [ ] **KB** (`.cursor/kb/`): copiar domínios/arquivos novos; em `index.md` conflitantes, mesclar tabelas de entrada (não duplicar linhas)
- [ ] **Regras** (`.cursor/rules/`): acrescentar regras `.mdc` novas; em conflito, concatenar blocos distintos ou escolher o mais restritivo para segurança

### 🟢 POLISH

- [ ] Rodar `python3 scripts/validate-agent-router.py`
- [ ] Atualizar `docs/00-INDEX.md` só se novos guias/workflows foram incorporados
- [ ] Remover `.agentic-upgrade/incoming/` após merge aceito (manter `UPGRADE_REPORT.md` até commit)

---

## Exit Criteria

- [ ] Nenhum conflito crítico em `commands/workflow-*`, `intake.md` ou `AGENT_ROUTER.yaml` sem decisão documentada
- [ ] `python3 scripts/validate-agent-router.py` → exit 0
- [ ] Expert de domínio e PROMPTs locais intactos

---

## Notas

- Preferir **merge por seção** (Markdown `##`) em vez de substituir arquivo inteiro.
- Em dúvida entre template e destino para **segurança/governança**, preferir o texto mais restritivo; para **nomes/paths do projeto**, preferir o destino.
