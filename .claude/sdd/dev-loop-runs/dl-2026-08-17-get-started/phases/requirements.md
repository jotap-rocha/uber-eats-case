# Phase: **requirements** — **Requisitos**

**Run:** `dl-2026-08-17-get-started`
**Manifest:** estado canônico em `../DEVLOOP_MANIFEST.yaml` (`phases.requirements.status`).

## Sumário (enxuto)

- Status: `pass`
- Artefato principal: [`../artifacts/dl-2026-08-17-get-started_requirements.md`](../artifacts/dl-2026-08-17-get-started_requirements.md)
- Última atualização: 2026-08-17T00:00:00Z (registrado nesta fase)

## Notas da fase

Escopo confirmado via grep exaustivo: **10 arquivos movem** para `get_started/`
(`START_HERE.md`, `DEV_LOOP_Guia_Comandos.md`, `SDD_Guia_Comandos.md`, `HOW_TO_USE_AGENTS.md`,
`HOW_TO_MAKE_NEW_AGENT.md`, `MANUAL_AGENTES.md`, `AGENTIC_UPGRADE_Guia.md`,
`COMO_TORNAR_PROJETO_AGENTIC.md`, `CRIAR_AMBIENTE_VIRTUAL.md`, `copilot-instructions.md` da raiz);
**3 ficam na raiz** (`README.md`, `CLAUDE.md`, `CONTEXT.md` — correção em relação ao briefing
inicial, que sugeria mover `CONTEXT.md`).

Achado crítico: 3 scripts de tooling têm paths hardcoded para os docs que vão mover
(`scripts/sync-workflow-bundle.sh`, `scripts/validate-workflow-bundle.py`,
`scripts/validate-agentic-template.py`) — sem corrigi-los a reorganização quebra validação
silenciosamente. Tratado como FR-007/FR-008 (críticos) no artefato.

Mapeamento completo de links a corrigir (raiz, `docs/00-INDEX.md`, os próprios arquivos movidos,
e mirrors `.cursor/`/`.claude/`/`.github/`) está detalhado no artefato principal (seções FR-003 a
FR-006). Fora de escopo: `.claude/worktrees/**` (worktree separado), `install_dev_loop/**`,
`agentspec/**`, `templates/*-generico.md` (conteúdo genérico para outros projetos).

## Bloqueios / pendências

| Item | Severidade | Resumo |
|------|------------|--------|
| — | — | Nenhum bloqueio para prosseguir à fase `design` |
