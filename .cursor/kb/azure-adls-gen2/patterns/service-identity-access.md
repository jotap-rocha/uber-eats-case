---
domain: azure-adls-gen2
topic: service-identity-access
---

# Pattern — service-identity-access (SP / MI com permissão mínima)

Objetivo: cada processo acessa o lake com **sua** identidade, no **menor escopo**
(container ou diretório), sem account key nem SAS.

## 1. Escolher a identidade

| Runtime | Identidade | Segredo? |
|---|---|---|
| Recurso Azure (Synapse, Stream Analytics, Function, VM, AKS) | **Managed Identity** | não |
| GitHub Actions / ADO | SP com **federated credential** (OIDC) | não |
| Spark fora do Azure, Databricks Free Edition, Kafka Connect em VM externa | **Service Principal** com client secret ou certificado | sim → Key Vault/secret store, rotacionar |

## 2. Criar o SP (quando não há MI)

```bash
APP_ID=$(az ad app create --display-name "sp-<projeto>-spark" --query appId -o tsv)
az ad sp create --id "$APP_ID"
# Secret com validade curta; valor vai direto para o cofre, nunca para o terminal/log
az ad app credential reset --id "$APP_ID" --years 1 --query password -o tsv \
  | az keyvault secret set --vault-name <VAULT> -n sp-spark-secret --file /dev/stdin >/dev/null
```

(Pipe para `--file /dev/stdin`: **a validar** no seu shell; alternativa é script que
lê da variável e não ecoa.)

## 3. RBAC no escopo do container (Terraform)

```hcl
locals {
  acessos = {
    spark_bronze = { container = "bronze", role = "Storage Blob Data Reader",      principal = var.sp_spark_object_id }
    spark_silver = { container = "silver", role = "Storage Blob Data Contributor", principal = var.sp_spark_object_id }
    synapse_gold = { container = "gold",   role = "Storage Blob Data Reader",      principal = azurerm_synapse_workspace.ws.identity[0].principal_id }
  }
}

resource "azurerm_role_assignment" "lake" {
  for_each             = local.acessos
  scope                = "${azurerm_storage_account.lake.id}/blobServices/default/containers/${each.value.container}"
  role_definition_name = each.value.role
  principal_id         = each.value.principal
}
```

- `principal_id` é o **object ID** do SP (não o client/app ID).
- Criar role assignment exige que a identidade do Terraform tenha
  `Role Based Access Control Administrator` / `User Access Administrator` no escopo.
- Propagação: alguns minutos; o primeiro acesso logo após o apply pode dar 403.

## 4. ACL para granularidade abaixo do container (opcional)

Só funciona se o RBAC **não** já conceder a operação (RBAC é avaliado primeiro).
Ex.: SP do Kafka Connect escreve só em `bronze/vendas/`, sem role no container:

```bash
OID=<OBJECT_ID_DO_SP>
# Execute (travessia) na raiz do container
az storage fs access update-recursive --acl "user:$OID:--x" -p / -f bronze \
  --account-name <STORAGE_ACCOUNT> --auth-mode login
# rwx + default (herança) no diretório alvo
az storage fs access update-recursive --acl "user:$OID:rwx,default:user:$OID:rwx" \
  -p vendas -f bronze --account-name <STORAGE_ACCOUNT> --auth-mode login
```

`update-recursive` na raiz propaga para todos os filhos — em container grande, prefira
`az storage fs access set` só no diretório raiz (não recursivo) para o `--x`.

## 5. Spark com Service Principal

```python
import os
acct = os.environ["LAKE_ACCOUNT"]           # <STORAGE_ACCOUNT>
host = f"{acct}.dfs.core.windows.net"
conf = {
    f"fs.azure.account.auth.type.{host}": "OAuth",
    f"fs.azure.account.oauth.provider.type.{host}":
        "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    f"fs.azure.account.oauth2.client.id.{host}": os.environ["LAKE_SP_CLIENT_ID"],
    f"fs.azure.account.oauth2.client.secret.{host}": os.environ["LAKE_SP_SECRET"],  # nunca logar
    f"fs.azure.account.oauth2.client.endpoint.{host}":
        f"https://login.microsoftonline.com/{os.environ['AZURE_TENANT_ID']}/oauth2/token",
}
for k, v in conf.items():
    spark.conf.set(k, v)

df = spark.read.parquet(f"abfss://silver@{host}/vendas/pedidos/")
```

- Requer `hadoop-azure` (ABFS) no classpath — Hadoop **3.x**. Clusters Hadoop 2.x
  podem não ter ABFS (ver risco R1 na KB `azure-event-hubs`).
- Databricks: preferir **storage credential / external location** do Unity Catalog com
  o SP, em vez de `spark.conf` por notebook (extensão prevista na skill
  `databricks-unity-catalog`); secret via Databricks secret scope.

## 6. Managed Identity (recursos Azure)

```hcl
resource "azurerm_stream_analytics_job" "job" {
  # ...
  identity { type = "SystemAssigned" }
}
resource "azurerm_role_assignment" "asa_ref" {
  scope                = "${azurerm_storage_account.lake.id}/blobServices/default/containers/reference"
  role_definition_name = "Storage Blob Data Reader"
  principal_id         = azurerm_stream_analytics_job.job.identity[0].principal_id
}
```

## 7. Verificação

```bash
# Como o SP (em sessão isolada, não no shell do dev)
# flag do secret: --client-secret (az recente) ou --password (antigo) — a validar na sua versão
az login --service-principal -u <CLIENT_ID> --tenant <TENANT_ID> --client-secret "$LAKE_SP_SECRET"
az storage fs file list -f silver --account-name <STORAGE_ACCOUNT> --auth-mode login -o table   # deve listar
az storage fs file list -f gold   --account-name <STORAGE_ACCOUNT> --auth-mode login -o table   # deve dar 403
```

O 403 no container não autorizado é parte do teste (prova o mínimo privilégio).

## Checklist

- [ ] Nenhuma account key/SAS em código, notebook ou config versionada
- [ ] Role de **dados** no escopo **container** (nunca conta/assinatura para apps)
- [ ] Uma identidade por processo; secret de SP no cofre com validade curta
- [ ] `shared_access_key_enabled = false` na conta
- [ ] Teste negativo (403) documentado
