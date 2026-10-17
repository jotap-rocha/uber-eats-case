---
domain: terraform
topic: variables-and-secrets
---

# Variáveis e secrets

## Fontes de valor (precedência crescente)

1. `default` na declaração da variável
2. `terraform.tfvars` / `*.auto.tfvars`
3. `-var-file=...`
4. `-var name=value`
5. Variável de ambiente `TF_VAR_<nome>` — **canal preferido para segredo**

## O que versionar

| Arquivo | Versionar? |
|---|---|
| `variables.tf` | Sim |
| `terraform.tfvars.example` (placeholders) | Sim |
| `terraform.tfvars` com valores reais | **Não** (`.gitignore`) |
| `*.tfstate`, `*.tfstate.backup`, `.terraform/` | **Não** |
| `.terraform.lock.hcl` | Sim |

`.gitignore` mínimo:

```gitignore
.terraform/
*.tfstate
*.tfstate.*
*.tfvars
!*.tfvars.example
crash.log
```

## Segredos

- Declare `sensitive = true` em variável e output que carreguem segredo — esconde do
  `plan`/log, **mas o valor continua no state**. Por isso o backend precisa de acesso restrito.
- Prefira não passar segredo pelo Terraform: crie o recurso de cofre e deixe a aplicação ler
  em runtime pela identidade de serviço (ver skill `cloud-secrets` e KBs de cofre).
- Credencial da própria nuvem para o Terraform: login da CLI (dev) ou federação OIDC (CI).
  Nunca chave estática em arquivo. Detalhe por provider → `patterns/provider-auth.md` da
  KB `role: iac-provider`.

## Placeholders (SI do harness)

Exemplos e `*.example` usam só placeholders: `<SUBSCRIPTION_ID>`, `<AWS_ACCOUNT_ID>`,
`<GCP_PROJECT_ID>`, `<REGION>`. Nunca ID real de conta em arquivo versionado.
