---
domain: azure-terraform
topic: auth-modes
---

# Modos de autenticação do Terraform no Azure

O provider tenta, nesta ordem prática, o que estiver configurado: client certificate,
client secret, OIDC, Managed Identity, Azure CLI. Configure **um** por contexto.

| Contexto | Modo | Config | Segredo armazenado? |
|---|---|---|---|
| Laptop do dev | Azure CLI | `az login` + `ARM_SUBSCRIPTION_ID` | não (token da CLI) |
| GitHub Actions / Azure DevOps | **SP + OIDC** (workload identity federation) | `ARM_USE_OIDC=true`, `ARM_CLIENT_ID`, `ARM_TENANT_ID`, `ARM_SUBSCRIPTION_ID` | **não** |
| Runner self-hosted em VM Azure | Managed Identity | `ARM_USE_MSI=true` (+ `ARM_CLIENT_ID` se user-assigned) | não |
| CI sem suporte a OIDC | SP + client secret | `ARM_CLIENT_SECRET` como secret do CI | sim — rotacionar |

## Por que OIDC no CI

- Sem secret de longa duração: o CI troca o ID token do próprio runner por um token do
  Entra ID via **federated credential** na App Registration.
- A federated credential amarra **issuer + subject** (ex.: repo + branch/environment) —
  outro repo não consegue usar a identidade.
- GitHub Actions exige `permissions: id-token: write` no job.

## Service Principal: permissões mínimas

| Escopo | Role | Para quê |
|---|---|---|
| RG do projeto | `Contributor` | criar/destruir recursos |
| Container `tfstate` | `Storage Blob Data Contributor` | ler/gravar/travar state |
| RG do projeto (opcional) | `Role Based Access Control Administrator` (condicionado) | se o apply cria role assignments (ex.: SP do Spark no ADLS) |

Evite `Owner` na assinatura. Se precisar criar RG pelo Terraform, `Contributor` na
assinatura é o mínimo — prefira criar o RG no bootstrap.

## Dev local: armadilhas

- `az login` com várias assinaturas → sempre `az account set` + `ARM_SUBSCRIPTION_ID`.
- Tenant com MFA/conditional access: `az login --tenant <TENANT_ID>`.
- Não exporte `ARM_CLIENT_SECRET` no shell do dev "para testar" — usa o SP de CI fora
  do CI e quebra a trilha de auditoria.

## Onde ficam os valores

| Valor | É segredo? | Onde |
|---|---|---|
| `<SUBSCRIPTION_ID>`, `<TENANT_ID>`, `<CLIENT_ID>` | não, mas não versionar real | variáveis do CI / `.env` local ignorado |
| client secret | **sim** | secret do CI ou Key Vault (KB `azure-keyvault`) |
| `*.tfvars` com valores reais | pode conter | gitignored; versionar só `*.tfvars.example` |
