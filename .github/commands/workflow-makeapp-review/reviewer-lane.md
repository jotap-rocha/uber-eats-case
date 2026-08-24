---
name: reviewer-lane
description: |
  Revisa uma única lane (backend, frontend, security, databricks, performance, ui_ux).
  Contexto mínimo: só globs e KB dessa lane. Atualiza lanes/<lane>.md e o manifest.
---

# `/reviewer-lane` — Uma dimensão por conversa

**Canónico:** `.github/commands/workflow-makeapp-review/reviewer-lane.md`. Atalho: [`../review/reviewer-lane.md`](../review/reviewer-lane.md).

Entrada do fluxo: [`workflow-makeapp-review.md`](workflow-makeapp-review.md) → `/workflow-makeapp-review`.

## Usage

```bash
/reviewer-lane <RUN_ID> <lane_id>

/reviewer-lane pr-1842 security
/reviewer-lane pr-1842 backend
/reviewer-lane pr-1842 frontend
/reviewer-lane pr-1842 databricks
/reviewer-lane pr-1842 performance
/reviewer-lane pr-1842 ui_ux
```

**lane_id** canônico: `backend` | `frontend` | `security` | `databricks` | `performance` | `ui_ux`

---

## Regra de contexto

- **Não** pedir ao modelo para rever todas as lanes neste comando.
- Relatório **completo** em `.github/sdd/reviews/{RUN_ID}/lanes/{lane_id}.md`
- No chat: **resumo curto** + pointer ao arquivo + **sempre** o bloco **Próximo comando** (ver abaixo).

---

## Resposta do agente (obrigatório)

Ordem das lanes: `security` → `backend` → `frontend` → `databricks` → `performance` → `ui_ux`.

1. **Após cada lane exceto `ui_ux`:** o agente deve terminar com **`Próximo comando:`** `` `/reviewer-lane <RUN_ID> <próxima_lane>` ``.
2. **Após `ui_ux`:**  
   - Gerar/atualizar **`REVIEW_SUMMARY.md`** na raiz do RUN (consolidado de todas as lanes + estado do manifest).  
   - Terminar com **`Próximos comandos (pós-lanes):`**  
     - `` `/reviewer-round <RUN_ID>` ``  
     - `` `/reviewer-fixer <RUN_ID> <lane> — <instrução>` ``  
     - Opcional: novo ciclo `` `/reviewer-init <novo_RUN_ID>` `` e repetir as lanes na mesma ordem  
   - Indicar o path a `REVIEW_SUMMARY.md`.

Detalhe do processo: `.github/agents/workflow-makeapp-review/makeapp-review-lane.md`.

---

## Agente

**`makeapp-review-lane`** — `.github/agents/workflow-makeapp-review/makeapp-review-lane.md`

---

## Referências

- Lanes, globs, KB: `.github/sdd/architecture/WORKFLOW_MAKEAPP_REVIEW_CONTRACTS.yaml`
- Estado: `.github/sdd/reviews/{RUN_ID}/REVIEW_MANIFEST.yaml`
- Sumário consolidado (após `ui_ux`): `.github/sdd/reviews/{RUN_ID}/REVIEW_SUMMARY.md`
