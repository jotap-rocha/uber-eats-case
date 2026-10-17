---
domain: azure-adls-gen2
topic: quick-reference
---

# Azure ADLS Gen2 — Quick Reference

### Endpoints e URIs

| Uso | Formato |
|---|---|
| Spark/Hadoop (ABFS) | `abfss://<container>@<STORAGE_ACCOUNT>.dfs.core.windows.net/<path>` |
| REST DFS / Synapse COPY com MSI | `https://<STORAGE_ACCOUNT>.dfs.core.windows.net/<container>/<path>` |
| REST Blob / SAS | `https://<STORAGE_ACCOUNT>.blob.core.windows.net/<container>/<path>` |

Container (blob) = **filesystem** (DFS) — mesma coisa.

### Terraform mínimo

```hcl
resource "azurerm_storage_account" "lake" {
  name                            = "<STORAGE_ACCOUNT>"   # 3-24, minúsculas+dígitos, único global
  resource_group_name             = azurerm_resource_group.base.name
  location                        = azurerm_resource_group.base.location
  account_kind                    = "StorageV2"
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  is_hns_enabled                  = true      # muda = recria a conta
  shared_access_key_enabled       = false
  allow_nested_items_to_be_public = false
  min_tls_version                 = "TLS1_2"
}
resource "azurerm_storage_data_lake_gen2_filesystem" "zona" {
  for_each           = toset(["bronze", "silver", "gold"])
  name               = each.key
  storage_account_id = azurerm_storage_account.lake.id
}
```

Com `shared_access_key_enabled = false`: provider com `storage_use_azuread = true` e a
identidade do Terraform com role de dados (ver KB `azure-terraform`).

### Roles de dados

| Role | Pode |
|---|---|
| `Storage Blob Data Reader` | ler/listar |
| `Storage Blob Data Contributor` | ler/escrever/apagar |
| `Storage Blob Data Owner` | tudo + **setar ACL/owner** |
| `Contributor` / `Owner` (ARM) | gerenciar a conta — **não** dá acesso a dados via Entra ID |

### az CLI

```bash
az role assignment create --role "Storage Blob Data Contributor" \
  --assignee <CLIENT_ID> \
  --scope "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RG>/providers/Microsoft.Storage/storageAccounts/<STORAGE_ACCOUNT>/blobServices/default/containers/silver"

az storage fs directory create -f silver -n vendas/pedidos \
  --account-name <STORAGE_ACCOUNT> --auth-mode login
az storage fs file list -f silver --path vendas --account-name <STORAGE_ACCOUNT> --auth-mode login -o table
az storage fs access set --acl "user::rwx,group::r-x,other::---" -p vendas \
  -f silver --account-name <STORAGE_ACCOUNT> --auth-mode login
```

### Spark (SP, client credentials)

```properties
fs.azure.account.auth.type.<STORAGE_ACCOUNT>.dfs.core.windows.net=OAuth
fs.azure.account.oauth.provider.type.<STORAGE_ACCOUNT>.dfs.core.windows.net=org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider
fs.azure.account.oauth2.client.id.<STORAGE_ACCOUNT>.dfs.core.windows.net=<CLIENT_ID>
fs.azure.account.oauth2.client.secret.<STORAGE_ACCOUNT>.dfs.core.windows.net=<FROM_SECRET_STORE>
fs.azure.account.oauth2.client.endpoint.<STORAGE_ACCOUNT>.dfs.core.windows.net=https://login.microsoftonline.com/<TENANT_ID>/oauth2/token
```

### Troubleshooting

| Sintoma | Causa |
|---|---|
| 403 `AuthorizationPermissionMismatch` | falta role de **dados** (Contributor ARM não basta) ou propagação (minutos) |
| 403 com role ok | ACL negando no diretório pai (falta `--x` no caminho) |
| `KeyBasedAuthenticationNotPermitted` | cliente usando account key com shared key desligado |
| `abfss` "FileSystem not found" | container não criado ou URI com endpoint `blob` |
