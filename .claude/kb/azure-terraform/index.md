---
domain: azure-terraform
description: Terraform no Azure — provider azurerm (v5) + azuread opcional, auth az login (dev) / Service Principal OIDC (CI), state remoto em Storage Account com Entra ID, resource group base e features {}
mcp_validated: "2026-10-16"
confidence: 0.85
---

# KB: Azure Terraform (provider azurerm)

Só o **específico do Azure** no Terraform: provider, autenticação, backend de state e
recursos base. Terraform genérico (módulos, workspaces, `for_each`) não mora aqui.

## Papel

`role: iac-provider` — dá ao `iac-engineer` / `cloud-data-engineer` o que precisa para
`terraform init/plan/apply` contra uma assinatura Azure: provider `azurerm` configurado,
identidade da ferramenta (humano ou CI), state remoto travado e o resource group onde os
serviços dos outros papéis (`warehouse`, `streaming`, `object-storage`,
`stream-processing`) são criados.

## Capability map

| Pergunta | Onde achar |
|---|---|
| O que muda no provider azurerm v5? `features {}`? | [concepts/provider-azurerm.md](concepts/provider-azurerm.md) |
| Quais modos de auth existem e qual usar onde? | [concepts/auth-modes.md](concepts/auth-modes.md) |
| Bloco `provider` + OIDC no GitHub Actions | [patterns/provider-auth.md](patterns/provider-auth.md) |
| Backend `azurerm` + bootstrap do storage de state | [patterns/remote-state.md](patterns/remote-state.md) |
| Cheatsheet | [quick-reference.md](quick-reference.md) |

## Custo e free tier

| Item | Custo |
|---|---|
| Terraform CLI, provider azurerm/azuread | grátis (open source) |
| Storage Account do state (LRS, KB de dados) | centavos/mês — pode ficar ligado |
| Resource group | grátis (custo é dos recursos dentro dele) |
| Recursos criados pelo `apply` | ver `## Custo e free tier` da KB de cada papel |

- Conta nova: **US$ 200 de crédito por 30 dias** + cota de serviços grátis por 12 meses
  (ver learn.microsoft.com "Avoid charges with your Azure free account"). Esgotou ou
  venceu o crédito → assinatura e serviços **desabilitados** até upgrade.
- Quem queima crédito não é o Terraform, é o que ele cria (DW100c ligado, TUs, SUs).
- Regra: **criar → testar → `terraform destroy` (ou pausar) no mesmo dia.** O state RG
  (`rg-tfstate`) fica **fora** da config destruída — ver `patterns/remote-state.md`.
- Antes do apply: `terraform plan` e conferir o que é cobrado por hora.

## SI

- Identidade de CI: Service Principal / App Registration com **OIDC (federated
  credential)** — sem client secret armazenado. Secret só se OIDC impossível, e então
  via secret do CI/Key Vault, nunca em `.tf`/`.tfvars` versionado.
- Permissão mínima: `Contributor` no **resource group** (não na assinatura) +
  `Storage Blob Data Contributor` no container do state. `User Access Administrator` /
  `Role Based Access Control Administrator` só se o apply cria role assignments.
- Placeholders only: `<SUBSCRIPTION_ID>`, `<TENANT_ID>`, `<CLIENT_ID>`, `<STORAGE_ACCOUNT>`.
- State contém outputs/atributos sensíveis → container privado, acesso por Entra ID,
  nunca commitar `*.tfstate`.

## Por que este serviço

| Alternativa | Por que não (aqui) |
|---|---|
| Bicep / ARM | Só Azure; o harness é multi-cloud e o state/plan do Terraform é o padrão comum |
| Provider `azapi` | Útil para recurso em preview; usar pontualmente **ao lado** do azurerm, não no lugar |
| Pulumi | Outra linguagem/runtime e state service; sem ganho para o escopo |
| Portal / `az` imperativo | Sem plano, sem drift detection, sem teardown reprodutível |

## Learning path

1. `concepts/provider-azurerm.md` — versão, `features {}`, registro de resource providers
2. `concepts/auth-modes.md` — az login vs SP vs OIDC
3. `patterns/remote-state.md` — bootstrap do state (uma vez por assinatura)
4. `patterns/provider-auth.md` — provider + pipeline de CI

## Quick Reference

Ver [quick-reference.md](quick-reference.md).

## A validar

- Versão exata do provider `azuread` compatível (usar a última `~>` publicada no registry).
