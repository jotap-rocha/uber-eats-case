# Relatório consolidado — **RUN_ID**

**Gerado em:** REPLACE_ISO8601 (UTC)  
**Manifest:** [`REVIEW_MANIFEST.yaml`](./REVIEW_MANIFEST.yaml)  
**Branch / PR:** _(do manifest, se preenchido)_

## Estado por lane

| Lane | Status (manifest) | Relatório |
|------|-------------------|-----------|
| security | _pending / pass / fail_ | [lanes/security.md](./lanes/security.md) |
| backend | … | [lanes/backend.md](./lanes/backend.md) |
| frontend | … | [lanes/frontend.md](./lanes/frontend.md) |
| databricks | … | [lanes/databricks.md](./lanes/databricks.md) |
| performance | … | [lanes/performance.md](./lanes/performance.md) |
| ui_ux | … | [lanes/ui_ux.md](./lanes/ui_ux.md) |

## Achados consolidados (por lane)

Resumo das linhas da tabela **Findings** de cada `lanes/<lane>.md` (blocker / major em primeiro plano).

### security

- _(copiar ou resumir SEC-xxx …)_

### backend

- _(BE-xxx …)_

### frontend

- _(FE-xxx …)_

### databricks

- _(DBX-xxx …)_

### performance

- _(PERF-xxx …)_

### ui_ux

- _(UX-xxx …)_

## Próximos passos sugeridos

1. `/reviewer-round RUN_ID` — revalidar após correções.
2. `/reviewer-fixer RUN_ID <lane> — <finding>` — corrigir com escopo explícito.
3. Novo ciclo completo: `/reviewer-init <novo_RUN_ID>` e repetir lanes se a branch mudou muito.
