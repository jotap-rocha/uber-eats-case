---
domain: aws-terraform
topic: quick-reference
---

# AWS Terraform — Quick Reference

### Versões mínimas

| Item | Versão | Por quê |
|---|---|---|
| Terraform | `>= 1.10` | `use_lockfile` (lock nativo S3) — DynamoDB deprecated depois |
| Provider `hashicorp/aws` | `~> 6.0` | docs validadas em v6.x |

### Esqueleto

```hcl
terraform {
  required_version = ">= 1.10"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 6.0" }
  }
  backend "s3" {}               # valores via -backend-config=backend.hcl
}

provider "aws" {
  region = var.region
  default_tags {
    tags = { Projeto = var.projeto, Ambiente = var.ambiente, Dono = var.dono, TTL = "1d" }
  }
}
```

### Auth em uma linha

| Contexto | Como |
|---|---|
| Laptop | `aws configure sso` → `aws sso login --profile <PROFILE>` → `AWS_PROFILE=<PROFILE>` |
| CI (GitHub/Azure DevOps) | OIDC → `assume_role_with_web_identity` (ou action oficial que exporta credenciais temporárias) |
| Proibido | `access_key`/`secret_key` no HCL, tfvars ou secret de pipeline de longa duração |

### Backend (`backend.hcl`, não versionar valores reais se sensíveis)

```hcl
bucket       = "<STATE_BUCKET>"
key          = "<PROJETO>/<AMBIENTE>/terraform.tfstate"
region       = "<REGION>"
use_lockfile = true
encrypt      = true
```

### Ciclo diário

```bash
aws sso login --profile <PROFILE>
terraform init -backend-config=backend.hcl
terraform fmt -check && terraform validate
terraform plan -out tfplan
terraform apply tfplan
# ... testar ...
terraform destroy            # mesmo dia
```

### Permissões do lock

`s3:GetObject`, `s3:PutObject`, `s3:DeleteObject` em `<key>.tflock` + `s3:ListBucket` no bucket.

### Armadilhas

| Sintoma | Causa |
|---|---|
| `ExpiredToken` / `SSO session expired` | rode `aws sso login` de novo |
| Lock preso após Ctrl+C | `terraform force-unlock <LOCK_ID>` (só se ninguém mais roda) |
| `profile` ignora env vars | com `profile` explícito o provider não cai para `AWS_ACCESS_KEY_ID` |
| Drift de tags | use `default_tags`; não duplique a mesma chave em `tags` do recurso |
