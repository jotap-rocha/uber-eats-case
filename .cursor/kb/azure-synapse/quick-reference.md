---
domain: azure-synapse
topic: quick-reference
---

# Azure Synapse Dedicated SQL Pool — Quick Reference

### Ciclo de vida do pool (az CLI)

```bash
RG=rg-<projeto>-dev; WS=<WORKSPACE>; POOL=dwlab
az synapse sql pool create  -n $POOL --performance-level DW100c --workspace-name $WS -g $RG
az synapse sql pool show    -n $POOL --workspace-name $WS -g $RG --query status -o tsv  # Online|Paused
az synapse sql pool pause   -n $POOL --workspace-name $WS -g $RG
az synapse sql pool resume  -n $POOL --workspace-name $WS -g $RG
az synapse sql pool update  -n $POOL --workspace-name $WS -g $RG --performance-level DW200c
az synapse sql pool delete  -n $POOL --workspace-name $WS -g $RG --yes   # para de pagar storage
```

PowerShell: `Suspend-AzSynapseSqlPool` / `Resume-AzSynapseSqlPool` (workspace).
"Formerly SQL DW" usa outros cmdlets (`Suspend-AzSqlDatabase`).

### Terraform

```hcl
resource "azurerm_synapse_sql_pool" "dw" {
  name                 = "dwlab"
  synapse_workspace_id = azurerm_synapse_workspace.ws.id
  sku_name             = "DW100c"
  storage_account_type = "LRS"      # backups; LRS barateia lab
  create_mode          = "Default"
  geo_backup_policy_enabled = false # lab; manter true em produção
}
```

Sem atributo de pausa → pausar com `az` após o apply.

### COPY INTO (Parquet, ADLS, Managed Identity)

```sql
COPY INTO stg.produto
FROM 'https://<STORAGE_ACCOUNT>.dfs.core.windows.net/silver/produto/*.parquet'
WITH (FILE_TYPE = 'PARQUET', CREDENTIAL = (IDENTITY = 'Managed Identity'));
```

MSI + Parquet exige endpoint **`dfs`**; SAS + Parquet exige **`blob`**.

### Credenciais aceitas no COPY

| IDENTITY | SECRET |
|---|---|
| `'Managed Identity'` | — |
| `'<CLIENT_ID>@<OAuth_2.0_Token_EndPoint>'` (SP) | client secret (evitar) |
| `'Shared Access Signature'` | token SAS (evitar) |
| sem `CREDENTIAL` | usuário Entra ID executando |

### Permissões de carga

```sql
GRANT ADMINISTER DATABASE BULK OPERATIONS TO [loader];
GRANT INSERT ON SCHEMA::stg TO [loader];
```

### Distribuição — regra de bolso

| Tabela | Distribuição | Índice |
|---|---|---|
| Staging | `ROUND_ROBIN` | `HEAP` |
| Dimensão pequena (< ~2 GB) | `REPLICATE` ou `HASH(bk)` | CCI |
| Dimensão alvo de MERGE com INSERT | **`HASH(bk)`** (obrigatório) | CCI |
| Fato | `HASH(chave de join mais usada)` | CCI |

### MERGE no Synapse — limites

- `;` final **obrigatório**.
- `WHEN NOT MATCHED [BY TARGET]` só com alvo **HASH**.
- `WHEN NOT MATCHED ... INSERT` **não** suportado em tabela com `IDENTITY`.
- Sem `OUTPUT`/composable DML no MERGE do dedicated pool → SCD2 em 2 passos.
- Update via MERGE = delete + insert (row count dobra).
- `SELECT @@VERSION` ≥ 10.0.17829.0 para MERGE seguro em HASH (senão pause/resume).

### Diagnóstico rápido

```sql
SELECT @@VERSION;
SELECT * FROM sys.dm_pdw_exec_requests WHERE status = 'Running';
DBCC PDW_SHOWSPACEUSED('dbo.dim_produto');   -- skew por distribuição
```
