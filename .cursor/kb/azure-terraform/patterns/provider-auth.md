---
domain: azure-terraform
topic: provider-auth
---

# Pattern — provider-auth (azurerm + OIDC no CI)

Objetivo: o mesmo código `.tf` roda no laptop (az login) e no CI (OIDC), sem nenhum ID
ou segredo no repositório.

## 1. `providers.tf` (versionado)

```hcl
terraform {
  required_version = ">= 1.9"
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = "~> 5.10" }
    # azuread = { source = "hashicorp/azuread", version = "~> 3.0" }  # só se criar SP/App (versão a validar)
  }
}

provider "azurerm" {
  features {}
  storage_use_azuread = true   # containers/filesystems via Entra ID, não Shared Key
  # Nada de subscription_id/tenant_id/client_id aqui: vêm de ARM_* no ambiente.
}
```

O provider lê `ARM_SUBSCRIPTION_ID`, `ARM_TENANT_ID`, `ARM_CLIENT_ID`, `ARM_USE_OIDC`
automaticamente.

## 2. Dev local

```bash
az login --tenant <TENANT_ID>
az account set --subscription <SUBSCRIPTION_ID>
export ARM_SUBSCRIPTION_ID=<SUBSCRIPTION_ID>
terraform init -backend-config=backend.dev.hcl   # ver remote-state.md
terraform plan -out tf.plan
```

## 3. Bootstrap da identidade do CI (uma vez, via az)

```bash
# App Registration + Service Principal
APP_ID=$(az ad app create --display-name "sp-<projeto>-ci" --query appId -o tsv)
az ad sp create --id "$APP_ID"

# Federated credential: só a branch main deste repo pode usar a identidade
az ad app federated-credential create --id "$APP_ID" --parameters '{
  "name": "gh-main",
  "issuer": "https://token.actions.githubusercontent.com",
  "subject": "repo:<ORG>/<REPO>:ref:refs/heads/main",
  "audiences": ["api://AzureADTokenExchange"]
}'

# Permissão mínima: Contributor no RG do projeto
az role assignment create --assignee "$APP_ID" --role Contributor \
  --scope "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/rg-<projeto>-dev"
```

Para PR (plan sem apply) crie outra federated credential com
`"subject": "repo:<ORG>/<REPO>:pull_request"` e, idealmente, outro SP só com `Reader`.
Para GitHub Environments: `repo:<ORG>/<REPO>:environment:<ENV>`.

`$APP_ID` = `<CLIENT_ID>`. Guardar como **variável** do CI (não é segredo, mas não
versionar).

## 4. GitHub Actions

```yaml
permissions:
  id-token: write      # obrigatório para OIDC
  contents: read

jobs:
  terraform:
    runs-on: ubuntu-latest
    env:
      ARM_USE_OIDC: "true"
      ARM_USE_AZUREAD: "true"            # backend autentica no blob via Entra ID
      ARM_CLIENT_ID: ${{ vars.AZURE_CLIENT_ID }}
      ARM_TENANT_ID: ${{ vars.AZURE_TENANT_ID }}
      ARM_SUBSCRIPTION_ID: ${{ vars.AZURE_SUBSCRIPTION_ID }}
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
      - run: terraform init -backend-config=backend.ci.hcl
      - run: terraform plan -out tf.plan
```

Azure DevOps: use service connection do tipo *Workload identity federation* e
`ARM_ADO_PIPELINE_SERVICE_CONNECTION_ID` (o provider também lê `SYSTEM_ACCESSTOKEN`).

## 5. Fallback: client secret (só sem OIDC)

```bash
export ARM_CLIENT_ID=<CLIENT_ID>
export ARM_TENANT_ID=<TENANT_ID>
export ARM_SUBSCRIPTION_ID=<SUBSCRIPTION_ID>
export ARM_CLIENT_SECRET="$(az keyvault secret show --vault-name <VAULT> -n tf-sp-secret --query value -o tsv)"
```

Nunca `client_secret = "..."` no `.tf`; nunca ecoar a variável em log.

## Checklist

- [ ] `providers.tf` sem nenhum ID/segredo
- [ ] `.terraform.lock.hcl` commitado
- [ ] Federated credential com subject restrito (repo + branch/environment)
- [ ] SP com `Contributor` só no RG + `Storage Blob Data Contributor` no container de state
- [ ] RPs registrados na assinatura (v5 não registra)
