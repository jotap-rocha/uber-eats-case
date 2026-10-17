---
domain: azure-synapse
topic: bulk-load
---

# Pattern — bulk-load (COPY INTO do ADLS Gen2)

`COPY INTO` é o caminho recomendado de carga no dedicated pool (mais simples que
PolyBase/external tables, sem objetos auxiliares). Fluxo: lake (silver) → **staging**
(HEAP, ROUND_ROBIN) → MERGE/INSERT na tabela final.

## 1. Pré-requisitos de identidade (Terraform)

```hcl
# Workspace com identidade gerenciada (system-assigned)
resource "azurerm_synapse_workspace" "ws" {
  name                                 = "<WORKSPACE>"
  resource_group_name                  = azurerm_resource_group.base.name
  location                             = azurerm_resource_group.base.location
  storage_data_lake_gen2_filesystem_id = azurerm_storage_data_lake_gen2_filesystem.ws.id
  sql_administrator_login              = "sqladminuser"
  sql_administrator_login_password     = var.sql_admin_password   # sensitive, via env/Key Vault
  identity { type = "SystemAssigned" }
}

# MSI do workspace lê o lake de dados
resource "azurerm_role_assignment" "ws_lake" {
  scope                = azurerm_storage_account.lake.id
  role_definition_name = "Storage Blob Data Contributor"   # Reader basta só para leitura (a validar p/ ERRORFILE)
  principal_id         = azurerm_synapse_workspace.ws.identity[0].principal_id
}
```

Propagação de role assignment leva minutos: primeiro COPY logo após o apply pode dar 403.

## 2. Tabela de staging

```sql
CREATE SCHEMA stg;
GO
CREATE TABLE stg.produto
(
    produto_id     INT            NOT NULL,
    nome           NVARCHAR(200)  NULL,
    categoria      NVARCHAR(100)  NULL,
    preco          DECIMAL(18,2)  NULL,
    atualizado_em  DATETIME2      NULL
)
WITH (DISTRIBUTION = ROUND_ROBIN, HEAP);
```

## 3. Carga Parquet (Managed Identity)

```sql
TRUNCATE TABLE stg.produto;   -- staging é descartável: TRUNCATE em stg de dev é ok

COPY INTO stg.produto
    (produto_id, nome, categoria, preco, atualizado_em)
FROM 'https://<STORAGE_ACCOUNT>.dfs.core.windows.net/silver/produto/dt=2026-10-16/*.parquet'
WITH (
    FILE_TYPE  = 'PARQUET',
    CREDENTIAL = (IDENTITY = 'Managed Identity')
);
```

- MSI + Parquet/ORC → URL **`.dfs.core.windows.net`**.
- Nomes de coluna: listar a column list explícita evita depender da ordem do arquivo.
- Parquet/ORC não precisam ser divididos (COPY divide sozinho); arquivos ≥ 256 MB rendem
  melhor. Muitos arquivos minúsculos (saída de streaming) → compactar antes no lake.
- `MAXERRORS` não protege de erro de conversão de tipo em Parquet — o COPY falha.

## 4. Carga CSV com rejeitados

```sql
COPY INTO stg.produto
FROM 'https://<STORAGE_ACCOUNT>.dfs.core.windows.net/bronze/produto/*.csv'
WITH (
    FILE_TYPE       = 'CSV',
    CREDENTIAL      = (IDENTITY = 'Managed Identity'),
    FIELDTERMINATOR = ',',
    FIELDQUOTE      = '"',
    FIRSTROW        = 2,
    ENCODING        = 'UTF8',
    MAXERRORS       = 10,
    ERRORFILE       = '/_rejeitados/produto/'   -- relativo ao container; cria _rejectedrows
);
```

`ERRORFILE` só vale para CSV. Rejeitados podem conter PII → mesma política de acesso
da zona bronze.

## 5. Permissões do usuário de carga

```sql
CREATE USER [loader] FROM EXTERNAL PROVIDER;   -- Entra ID (SP ou grupo)
GRANT ADMINISTER DATABASE BULK OPERATIONS TO [loader];
GRANT INSERT, SELECT ON SCHEMA::stg TO [loader];
```

O COPY roda no contexto do usuário; a MSI do workspace só autoriza a leitura dos
arquivos.

## 6. Pós-carga

```sql
UPDATE STATISTICS stg.produto;
SELECT COUNT(*) FROM stg.produto;          -- conferir contra contagem do lake
```

## Alternativas e quando usar

| Opção | Quando |
|---|---|
| `COPY INTO` | padrão |
| `CTAS` sobre external table | já existe external table/PolyBase legado |
| Pipeline Synapse/ADF Copy activity | orquestração visual; por baixo usa COPY/PolyBase |

## Erros comuns

| Erro | Causa provável |
|---|---|
| 403 / "not authorized" | role da MSI ausente ou não propagada; endpoint blob vs dfs errado |
| "Managed Service Identity isn't enabled" | workspace antigo (pré-dez/2020) — ver doc oficial |
| Linhas truncadas/NULL | ordem de colunas sem column list; tipo incompatível |
