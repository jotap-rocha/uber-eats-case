# Sincronização desta KB

**Origem canónica (editar aqui):**

`/DATALAKE/workspace/prd/data-agentic-ai-for-pipelines/.github/kb/migration-hub/`

**Réplica partilhada (Cursor / agentes no volume):**

`/DATALAKE/.github/kb/migration-hub/`

```bash
CANON="/DATALAKE/workspace/prd/data-agentic-ai-for-pipelines/.github/kb/migration-hub"
rsync -av --delete "${CANON}/" /DATALAKE/.github/kb/migration-hub/
find /DATALAKE -type d -path '*/kb/migration-hub' ! -path "${CANON}" -print0 | \
  xargs -0 -I{} rsync -av --delete "${CANON}/" "{}/"
```
