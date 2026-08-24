---
name: reviewer-init
description: |
  Inicia execução MakeApp Review: cria RUN em .claude/sdd/reviews/{RUN_ID}/ com manifest
  e stubs de lanes. Não analisa código — use /reviewer-lane por dimensão para poupar contexto.
---

# `/reviewer-init` — Workflow MakeApp Review (passo 0)

**Canónico:** `.claude/commands/workflow-makeapp-review/reviewer-init.md`. Atalho: [`../review/reviewer-init.md`](../review/reviewer-init.md) (mesmo `name` no frontmatter).

Entrada do fluxo (visão geral): [`workflow-makeapp-review.md`](workflow-makeapp-review.md) → `/workflow-makeapp-review`.

## Usage

```bash
/reviewer-init <RUN_ID>
/reviewer-init pr-1842
/reviewer-init feat-databricks-lab
```

Se omitires o ID, o agente pode sugerir `rev-YYYY-MM-DD-<sufixo>`.

---

## O que faz

1. Cria `.claude/sdd/reviews/{RUN_ID}/`
2. Escreve `REVIEW_MANIFEST.yaml` (estado enxuto — ver template em `_template/`)
3. Cria `lanes/backend.md` … `lanes/ui_ux.md` (stubs)
4. Cria `REVIEW_LOG.md` com linha inicial
5. **Resposta curta** com a **ordem recomendada** de `/reviewer-lane` (ver `WORKFLOW_MAKEAPP_REVIEW_CONTRACTS.yaml`) e linha explícita **`Próximo comando:`** `` `/reviewer-lane <RUN_ID> security` ``.

---

## Agente

Invocar **`makeapp-review-init`** (`.claude/agents/workflow-makeapp-review/makeapp-review-init.md`).

---

## Próximo passo (obrigatório para revisar)

**Uma lane por comando** — cada `/reviewer-lane` concluído deve indicar o **próximo** slash; após **`ui_ux`**, ver `REVIEW_SUMMARY.md`, `/reviewer-round` e `/reviewer-fixer`.

```bash
/reviewer-init pr-1842
/reviewer-lane pr-1842 security
/reviewer-lane pr-1842 backend
# … etc.
```

Contrato de lanes: `.claude/sdd/architecture/WORKFLOW_MAKEAPP_REVIEW_CONTRACTS.yaml`  
Documentação: `.claude/sdd/reviews/README.md`
