---
name: pipeline-review-init
description: |
  Inicia execução Data Pipeline Review: cria RUN em .github/sdd/data-pipeline-reviews/{RUN_ID}/
  com manifest e stubs de lanes. Não analisa código — use /pipeline-review-lane por dimensão.
---

# `/pipeline-review-init` — Data Pipeline Review (passo 0)

**Canônico:** `.github/commands/workflow-data-pipeline-review/pipeline-review-init.md`.

Entrada do fluxo: [`workflow-data-pipeline-review.md`](workflow-data-pipeline-review.md) → `/workflow-data-pipeline-review`.

## Usage

```bash
/pipeline-review-init <RUN_ID>
/pipeline-review-init pr-1842-pipeline-dim-cliente
```

Se o ID for omitido, o agente pode sugerir `dpr-YYYY-MM-DD-<sufixo>`.

## O que faz

1. Cria `.github/sdd/data-pipeline-reviews/{RUN_ID}/`.
2. Escreve `REVIEW_MANIFEST.yaml` usando o template em `_template/`.
3. Cria 11 arquivos em `lanes/`, um por lane do contrato.
4. Cria `REVIEW_LOG.md` com linha inicial.
5. Responde com a ordem recomendada de `/pipeline-review-lane` e linha explícita **`Próximo comando:`** `` `/pipeline-review-lane <RUN_ID> data_contracts` ``.

## Agente

Invocar **`data-pipeline-review-init`** (`.github/agents/workflow-data-pipeline-review/data-pipeline-review-init.md`).

## Próximo passo obrigatório

```bash
/pipeline-review-lane <RUN_ID> data_contracts
```

Contrato de lanes: `.github/sdd/architecture/WORKFLOW_DATA_PIPELINE_REVIEW_CONTRACTS.yaml`  
Documentação: `.github/sdd/data-pipeline-reviews/README.md`
