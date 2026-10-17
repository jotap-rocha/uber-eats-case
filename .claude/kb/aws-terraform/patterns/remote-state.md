---
domain: aws-terraform
topic: remote-state
---

# Pattern: state remoto em S3 com lock nativo

## Problema

State local se perde e não tem lock. Precisamos de state compartilhado, criptografado,
versionado e com lock — sem pagar/gerenciar tabela DynamoDB.

## Decisão

| Opção | Status | Usar? |
|---|---|---|
| `use_lockfile = true` (lock por objeto `.tflock` no próprio S3) | Atual (Terraform ≥ 1.10) | **Sim** |
| `dynamodb_table = "..."` | **Deprecated** — "will be removed in a future minor version" | Não em projeto novo |
| Ambos ao mesmo tempo | Suportado para migração | Só durante a transição |

## 1. Bootstrap do bucket de state (stack separada, state local, aplicada 1×)

```hcl
resource "aws_s3_bucket" "tfstate" {
  bucket = "<STATE_BUCKET>"          # nome globalmente único
}

resource "aws_s3_bucket_versioning" "tfstate" {
  bucket = aws_s3_bucket.tfstate.id
  versioning_configuration { status = "Enabled" }
}

resource "aws_s3_bucket_public_access_block" "tfstate" {
  bucket                  = aws_s3_bucket.tfstate.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "tfstate" {
  bucket = aws_s3_bucket.tfstate.id
  rule {
    apply_server_side_encryption_by_default { sse_algorithm = "AES256" }  # ou aws:kms
  }
}
```

O bucket de state **não** entra no `terraform destroy` diário — é infraestrutura de
base (custo: centavos). Proteja com `lifecycle { prevent_destroy = true }`.

## 2. Backend nas stacks de trabalho

```hcl
terraform {
  backend "s3" {}       # parcial: valores vêm do arquivo abaixo
}
```

`backend.hcl` (pode ser versionado se só tiver placeholders resolvidos por ambiente):

```hcl
bucket       = "<STATE_BUCKET>"
key          = "<PROJETO>/<AMBIENTE>/terraform.tfstate"
region       = "<REGION>"
encrypt      = true
use_lockfile = true
```

```bash
terraform init -backend-config=backend.hcl
```

## 3. Permissões mínimas da identidade que roda o Terraform

```json
{
  "Version": "2012-10-17",
  "Statement": [
    { "Effect": "Allow", "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::<STATE_BUCKET>" },
    { "Effect": "Allow", "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::<STATE_BUCKET>/<PROJETO>/*" },
    { "Effect": "Allow", "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
      "Resource": "arn:aws:s3:::<STATE_BUCKET>/<PROJETO>/*.tflock" }
  ]
}
```

Com SSE-KMS: adicionar `kms:Encrypt`, `kms:Decrypt`, `kms:GenerateDataKey` na chave.

## Migração de DynamoDB → lockfile

1. Adicione `use_lockfile = true` mantendo `dynamodb_table` (os dois locks coexistem).
2. `terraform init -reconfigure` em todos os ambientes/CI.
3. Remova `dynamodb_table`, `init -reconfigure` de novo, depois destrua a tabela.

## Operação

| Situação | Ação |
|---|---|
| Lock preso (processo morto) | confirmar que ninguém roda → `terraform force-unlock <LOCK_ID>` |
| State corrompido | restaurar versão anterior do objeto (versionamento do bucket) |
| Separar ambientes | `key` diferente por ambiente (preferível a workspaces para stacks pequenas) |

## SI

- State tem segredos em claro (ex.: senha gerada). Bucket privado + SSE + versionamento.
- Nada de `terraform state pull` colado em issue/chat.
- `<STATE_BUCKET>` e `key` reais ficam fora de docs públicas.
