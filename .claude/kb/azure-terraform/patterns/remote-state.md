---
domain: azure-terraform
topic: remote-state
---

# Pattern — remote-state (backend azurerm)

State em Blob Storage, autenticado por **Entra ID** (recomendado pela HashiCorp; access
key/SAS "not recommended for new workloads"). Locking e consistência usam capacidades
nativas do Blob Storage — não há tabela de lock separada.

## 1. Bootstrap (uma vez por assinatura, via az)

O storage do state não pode ser criado pela mesma config que o usa (ovo e galinha).
Fica num RG próprio que **nunca** entra no `terraform destroy` do projeto.

```bash
az group create -n rg-tfstate -l <REGION>

az storage account create -n <STORAGE_ACCOUNT> -g rg-tfstate \
  --sku Standard_LRS --kind StorageV2 \
  --min-tls-version TLS1_2 --allow-blob-public-access false \
  --allow-shared-key-access false

# Versionamento de blob = histórico do state para recuperação
az storage account blob-service-properties update \
  --account-name <STORAGE_ACCOUNT> -g rg-tfstate --enable-versioning true

# Via ARM (control plane): não exige role de dados nem shared key
az storage container-rm create -n tfstate \
  --storage-account <STORAGE_ACCOUNT> -g rg-tfstate

SCOPE="/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/rg-tfstate/providers/Microsoft.Storage/storageAccounts/<STORAGE_ACCOUNT>/blobServices/default/containers/tfstate"
# Humano (dev) e SP do CI
az role assignment create --role "Storage Blob Data Contributor" --assignee <SEU_UPN_OU_OBJECT_ID> --scope "$SCOPE"
az role assignment create --role "Storage Blob Data Contributor" --assignee <CLIENT_ID> --scope "$SCOPE"
```

Role assignment pode levar alguns minutos para propagar — 403 logo após criar é normal.

## 2. Backend no código (versionado, sem valores)

```hcl
terraform {
  backend "azurerm" {
    use_azuread_auth = true
    # use_oidc = true  -> ou ARM_USE_OIDC no CI
  }
}
```

## 3. Config parcial por ambiente (`backend.<env>.hcl`, gitignored ou só placeholders)

```hcl
storage_account_name = "<STORAGE_ACCOUNT>"
container_name       = "tfstate"
key                  = "<projeto>/dev.terraform.tfstate"
```

```bash
terraform init -backend-config=backend.dev.hcl
# ou
terraform init \
  -backend-config="storage_account_name=<STORAGE_ACCOUNT>" \
  -backend-config="container_name=tfstate" \
  -backend-config="key=<projeto>/dev.terraform.tfstate"
```

`resource_group_name` só é necessário nos métodos de lookup por access key ou com
`lookup_blob_endpoint = true` — com Entra ID não precisa.

## 4. Uma key por projeto/ambiente

| key | Conteúdo |
|---|---|
| `<projeto>/dev.terraform.tfstate` | RG do projeto + serviços dev |
| `<projeto>/prd.terraform.tfstate` | idem prd (outra assinatura, idealmente) |

Nunca compartilhar a mesma key entre configs diferentes.

## 5. Teardown do dia

```bash
terraform plan -destroy -out destroy.plan
terraform apply destroy.plan          # remove rg-<projeto>-<env>, não o rg-tfstate
```

Lock preso (job morto no meio): `terraform force-unlock <LOCK_ID>` — só depois de
confirmar que nenhum outro apply está rodando.

## SI

- Container privado, sem shared key, sem SAS em pipeline.
- State pode conter atributos sensíveis (connection strings de Event Hubs, senhas de
  admin do Synapse): **nunca** `terraform state pull > arquivo` em pasta versionada;
  marcar outputs com `sensitive = true`.
- `.gitignore`: `*.tfstate`, `*.tfstate.*`, `.terraform/`, `*.tfvars` (exceto `*.example`).
