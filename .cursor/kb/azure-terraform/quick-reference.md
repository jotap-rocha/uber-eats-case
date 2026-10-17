---
domain: azure-terraform
topic: quick-reference
---

# Azure Terraform — Quick Reference

### Versões (validado 2026-10-16)

| Peça | Valor |
|---|---|
| `hashicorp/azurerm` | 5.x (última: 5.10.0) → `version = "~> 5.10"` |
| `subscription_id` | **obrigatório** desde v4 (bloco ou `ARM_SUBSCRIPTION_ID`) |
| `resource_provider_registrations` | default **`none`** na v5 (antes `legacy`) |
| `skip_provider_registration` | **removido** na v5 |

### Provider mínimo

```hcl
terraform {
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = "~> 5.10" }
  }
}
provider "azurerm" {
  features {}                       # bloco obrigatório, mesmo vazio
  # subscription_id via ARM_SUBSCRIPTION_ID
}
```

### Env vars de auth (`ARM_*`)

| Var | Uso |
|---|---|
| `ARM_SUBSCRIPTION_ID` | sempre |
| `ARM_TENANT_ID` / `ARM_CLIENT_ID` | SP / OIDC |
| `ARM_USE_OIDC=true` | CI com federated credential |
| `ARM_CLIENT_SECRET` | SP com secret (evitar; só via secret do CI) |
| `ARM_USE_AZUREAD=true` | backend: auth no blob por Entra ID |
| `ARM_STORAGE_USE_AZUREAD=true` | provider: data plane de storage via Entra ID |

### Dev local

```bash
az login
az account set --subscription <SUBSCRIPTION_ID>
export ARM_SUBSCRIPTION_ID=<SUBSCRIPTION_ID>
terraform init && terraform plan -out tf.plan && terraform apply tf.plan
```

### Registrar resource providers (assinatura nova + azurerm v5)

```bash
for p in Microsoft.Storage Microsoft.EventHub Microsoft.Synapse \
         Microsoft.StreamAnalytics Microsoft.Sql; do
  az provider register --namespace "$p"
done
```

### Backend

```hcl
terraform {
  backend "azurerm" {
    use_azuread_auth = true
    # storage_account_name / container_name / key via -backend-config
  }
}
```

```bash
terraform init \
  -backend-config="storage_account_name=<STORAGE_ACCOUNT>" \
  -backend-config="container_name=tfstate" \
  -backend-config="key=dev.terraform.tfstate"
```

### Teardown

```bash
terraform plan -destroy -out destroy.plan && terraform apply destroy.plan
```

State RG (`rg-tfstate`) **não** entra no destroy.

### Armadilhas

| Sintoma | Causa |
|---|---|
| `subscription_id is a required provider property` | faltou `ARM_SUBSCRIPTION_ID` |
| `MissingSubscriptionRegistration` | v5 não registra RP — rodar `az provider register` |
| 403 no `init` (backend) | falta `Storage Blob Data Contributor` no container |
| 403 criando filesystem/container | `storage_use_azuread` sem role de dados Storage |
