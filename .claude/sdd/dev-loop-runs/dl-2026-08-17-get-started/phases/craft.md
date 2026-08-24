# Phase: **craft** — **Craft do PROMPT**

**Run:** `dl-2026-08-17-get-started`
**Manifest:** estado canônico em `../DEVLOOP_MANIFEST.yaml` (`phases.craft.status`).

## Sumário (enxuto)

- Status: `pass`
- Artefato principal: [`.claude/dev/tasks/PROMPT_dl-2026-08-17-get-started.md`](../../../dev/tasks/PROMPT_dl-2026-08-17-get-started.md)
- Última atualização: 2026-08-17T00:00:00Z (registrado nesta fase)

## Notas da fase

PROMPT gerado com 19 tarefas (T1-T19), tradução 1:1 do design: 🔴 RISKY = T1 (mover os 10
arquivos, fundamento de tudo); 🟡 CORE = T2-T16 (correções de link em raiz, `docs/00-INDEX.md`,
arquivos movidos, mirrors `.cursor/`/`.claude/`/`.github/` e os 3 scripts de tooling); 🟢 POLISH =
T17-T19 (ressincronizar bundle do instalador, validar isoladamente, verificação final ampla por
grep). Cada tarefa tem verificação objetiva via `grep`/comandos de exit code. Nenhum agente `@` de
domínio necessário — seção "Agentes (Dev Loop Executor)" registra isso explicitamente, conforme
decidido no design. `Exit Criteria` inclui os 2 comandos de verificação padrão do projeto
(`validate-agent-router.py`, `install_dev_loop --dry-run`) mais `validate-workflow-bundle.py`.

## Bloqueios / pendências

| Item | Severidade | Resumo |
|------|------------|--------|
| — | — | Nenhum bloqueio — aguardando gate humano em `prompt_review` |
