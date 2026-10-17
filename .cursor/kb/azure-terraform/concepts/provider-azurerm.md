---
domain: azure-terraform
topic: provider-azurerm
---

# Provider azurerm — o que importa no Azure

## Dois providers, dois planos

| Provider | Gerencia | Quando precisa |
|---|---|---|
| `hashicorp/azurerm` | Recursos ARM: RG, Storage, Event Hubs, Synapse, ASA, role assignments | sempre |
| `hashicorp/azuread` | Objetos Entra ID: App Registration, Service Principal, grupos, federated credentials | só se o Terraform **cria** a identidade do pipeline/app |

Recomendação para projeto pequeno: criar o SP do CI **uma vez via `az`** (bootstrap) e
deixar o Terraform só com `azurerm`. Adicione `azuread` quando a identidade fizer parte
do ciclo de vida da infra (ex.: SP por ambiente).

## Bloco `features {}`

Obrigatório no `provider "azurerm"`, mesmo vazio. Controla comportamentos de
create/destroy por serviço. Úteis em lab:

```hcl
provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = true   # destroy falha se sobrou recurso fora do state
    }
  }
}
```

Mantenha o default `true` acima: evita apagar RG com recurso criado à mão.

## Mudanças de versão que quebram config antiga

| Versão | Mudança | Ação |
|---|---|---|
| 4.0 | `subscription_id` obrigatório | `ARM_SUBSCRIPTION_ID` em dev e CI |
| 5.0 | `resource_provider_registrations` default `none` | registrar RPs com `az provider register` (ou setar o atributo) |
| 5.0 | `skip_provider_registration` removido | apagar o argumento da config |

Pin: `version = "~> 5.10"` e commitar `.terraform.lock.hcl`.

## Resource providers (RP)

Assinatura nova só tem RPs básicos registrados. Com v5 o provider **não** registra nada
sozinho → o primeiro `apply` de Synapse/Event Hubs/ASA falha com
`MissingSubscriptionRegistration`. Registre uma vez por assinatura (ver
quick-reference) e confira com `az provider show -n Microsoft.Synapse --query registrationState`.

## Storage data plane

Por padrão o provider usa **Shared Key** para criar containers/filesystems. Se a conta
tiver `shared_access_key_enabled = false` (recomendado), ligue no provider:

```hcl
provider "azurerm" {
  features {}
  storage_use_azuread = true
}
```

e dê à identidade do Terraform `Storage Blob Data Contributor` (ou Owner, se precisar
setar ACL) na conta.

## Resource group base

Um RG por ambiente/projeto (`rg-<projeto>-<env>`), tags obrigatórias para custo:

```hcl
resource "azurerm_resource_group" "base" {
  name     = "rg-${var.projeto}-${var.env}"
  location = var.location            # ex.: "brazilsouth" ou "eastus"
  tags     = { projeto = var.projeto, env = var.env, ttl = "same-day" }
}
```

Tag `ttl` ajuda a skill de custo a achar o que deve morrer hoje.
