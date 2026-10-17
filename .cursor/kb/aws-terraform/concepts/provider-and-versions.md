---
domain: aws-terraform
topic: provider-and-versions
---

# Provider `aws` e versões

## Pinagem

```hcl
terraform {
  required_version = ">= 1.10"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 6.0" }
  }
}
```

- `~> 6.0` aceita 6.x, bloqueia 7.0 (major com breaking changes).
- Commitar `.terraform.lock.hcl` — fixa o hash do provider entre máquinas e CI.
- Terraform ≥ 1.10 é o piso para o lock nativo do backend S3 (`use_lockfile`).
  **A validar:** a versão exata em que o DynamoDB foi marcado deprecated (a doc atual
  só diz "deprecated and will be removed in a future minor version").

## Bloco `provider`

| Argumento | Uso no harness |
|---|---|
| `region` | sempre explícito (via variável); nada de depender do default da máquina |
| `profile` | só no dev local; no CI omitir (credenciais vêm de OIDC/env) |
| `assume_role { role_arn }` | assumir role de deploy a partir de uma identidade base |
| `assume_role_with_web_identity` | CI com token OIDC em arquivo |
| `default_tags { tags = {...} }` | tags herdadas por todo recurso que suporta tags |
| `allowed_account_ids` | trava contra apply na conta errada |

```hcl
provider "aws" {
  region              = var.region
  allowed_account_ids = [var.aws_account_id]   # "<AWS_ACCOUNT_ID>" via tfvars não versionado
  default_tags {
    tags = {
      Projeto  = var.projeto
      Ambiente = var.ambiente
      Dono     = var.dono
      TTL      = "1d"      # sinaliza recurso efêmero (teardown no mesmo dia)
    }
  }
}
```

## Aliases (multi-região)

```hcl
provider "aws" {
  alias  = "us_east_1"
  region = "us-east-1"
}
# resource "aws_budgets_budget" ... { provider = aws.us_east_1 }  # se precisar fixar região
```

## `default_tags` — regras

- Tags do recurso **sobrescrevem** a mesma chave das `default_tags`.
- Alguns recursos não suportam tags (ex.: `aws_s3_bucket_policy`) — ok, são ignorados.
- Use `TTL`/`Ambiente` para achar órfãos: `aws resourcegroupstaggingapi get-resources
  --tag-filters Key=Projeto,Values=<PROJETO>`.

## Recursos que este harness costuma criar

| Papel | Recursos principais |
|---|---|
| object-storage | `aws_s3_bucket`, `aws_s3_bucket_public_access_block`, `aws_s3_bucket_policy` |
| warehouse | `aws_redshiftserverless_namespace`, `_workgroup`, `_usage_limit` |
| streaming | `aws_msk_serverless_cluster`, `aws_mskconnect_connector`, `_custom_plugin` |
| stream-processing | `aws_kinesisanalyticsv2_application` |
| custo | `aws_budgets_budget` |

Cada um tem sua KB (`aws-s3`, `aws-redshift`, `aws-msk`, `aws-managed-flink`).
