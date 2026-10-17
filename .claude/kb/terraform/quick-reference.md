---
domain: terraform
topic: quick-reference
---

# Terraform — Quick Reference

## Ciclo

```bash
terraform fmt -recursive -check
terraform init
terraform validate
terraform plan -out=tfplan
terraform show -no-color tfplan      # mostrar → acordo explícito
terraform apply tfplan
```

## Teardown

```bash
terraform plan -destroy -out=destroy.tfplan
terraform show -no-color destroy.tfplan   # acordo explícito
terraform apply destroy.tfplan
```

## Inspeção

| Comando | Para quê |
|---|---|
| `terraform state list` | O que existe no state |
| `terraform state show <addr>` | Atributos de um recurso |
| `terraform output` | Saídas (segredos ficam `sensitive`) |
| `terraform plan -refresh-only` | Detectar drift |
| `terraform providers` | Providers em uso |

## Nunca sem acordo

`apply`, `destroy`, `apply -auto-approve`, `force-unlock`, `state rm`, `import` em produção.

## Arquivos

| Versiona | Não versiona |
|---|---|
| `*.tf`, `.terraform.lock.hcl`, `*.tfvars.example` | `.terraform/`, `*.tfstate*`, `*.tfvars` |

## Específico da nuvem

Autenticação, backend de state e budget → KB `role: iac-provider` do provider (Passo 0 na KB
`cloud-resolution`).
