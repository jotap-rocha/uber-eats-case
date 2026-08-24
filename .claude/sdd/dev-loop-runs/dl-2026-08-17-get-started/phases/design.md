# Phase: **design** — **Design e plano**

**Run:** `dl-2026-08-17-get-started`
**Manifest:** estado canônico em `../DEVLOOP_MANIFEST.yaml` (`phases.design.status`).

## Sumário (enxuto)

- Status: `pass`
- Artefato principal: [`../artifacts/dl-2026-08-17-get-started_design.md`](../artifacts/dl-2026-08-17-get-started_design.md)
- Última atualização: 2026-08-17T00:00:00Z (registrado nesta fase)

## Notas da fase

Plano com 19 tarefas (T1-T19) mapeadas 1:1 para os FR-001..FR-008 do requirements. T1 (mover os
10 arquivos com `git mv`) é bloqueante para todas as demais. T14/T15 (corrigir paths hardcoded em
`scripts/sync-workflow-bundle.sh` e `scripts/validate-workflow-bundle.py`) bloqueiam T17
(ressincronizar bundle do instalador). T19 é uma verificação final ampla por grep, cobrindo toda a
árvore fora dos diretórios de exclusão, para reduzir o risco de link esquecido.

Nenhum agente de domínio (`@`) necessário — tarefa 100% mecânica de mover arquivos e editar
referências/paths; `dev-loop-executor` executa diretamente com `Read`/`Edit`/`Bash`.

## Bloqueios / pendências

| Item | Severidade | Resumo |
|------|------------|--------|
| — | — | Nenhum bloqueio para prosseguir à fase `craft` |
