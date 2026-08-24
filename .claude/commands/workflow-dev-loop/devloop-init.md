---
name: devloop-init
description: |
  Inicia execução Dev Loop (L2): cria RUN em .claude/sdd/dev-loop-runs/{RUN_ID}/ com manifest,
  stubs de fases e pasta artifacts/. Não implementa código — use /devloop-phase por fase.
---

# `/devloop-init` — Dev Loop (passo 0)

**Canônico:** `.claude/commands/workflow-dev-loop/devloop-init.md`  
Entrada: [`workflow-dev-loop.md`](workflow-dev-loop.md) → `/workflow-dev-loop`

## Usage

```bash
/devloop-init <RUN_ID>
/devloop-init feat-auth-login
```

Se omitir o ID, o agente pode sugerir `dl-YYYY-MM-DD-<sufixo>`.

## O que faz

1. Cria `.claude/sdd/dev-loop-runs/{RUN_ID}/`
2. Escreve `DEVLOOP_MANIFEST.yaml` (template em `_template/`)
3. Cria `artifacts/` e sete stubs em `phases/` (gate … reflect)
4. Cria `DEVLOOP_LOG.md` com linha inicial
5. Resposta curta + ordem de fases + **`Próximo comando:`** `` `/devloop-phase <RUN_ID> gate` ``

## Agente

**`devloop-init`** — `.claude/agents/workflow-dev-loop/devloop-init.md`

## Próximo passo

```bash
/devloop-phase <RUN_ID> gate
```

Contrato: `.claude/sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml`  
Documentação: `.claude/sdd/dev-loop-runs/README.md`
