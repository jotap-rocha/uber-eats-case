---
domain: aws-s3
topic: quick-reference
---

# Amazon S3 — Quick Reference

### Layout padrão

```
s3://<BUCKET>/
├── landing/   # arquivos como chegam (expira em 7–30 dias)
├── raw/       # imutável, particionado por data de ingestão (ex.: raw/kafka/<topico>/dt=…)
├── curated/   # limpo, tipado, Parquet; origem do COPY no Redshift
├── reference/ # tabelas de referência (Flink lookup/broadcast)
└── tmp/       # scratch (expira em 1 dia)
```

### Terraform mínimo de bucket seguro

```hcl
resource "aws_s3_bucket" "lake" {
  bucket        = "<BUCKET>"
  force_destroy = var.ambiente == "lab"     # nunca true em produção
}

resource "aws_s3_bucket_public_access_block" "lake" {
  bucket                  = aws_s3_bucket.lake.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_ownership_controls" "lake" {
  bucket = aws_s3_bucket.lake.id
  rule { object_ownership = "BucketOwnerEnforced" }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "lake" {
  bucket = aws_s3_bucket.lake.id
  rule {
    apply_server_side_encryption_by_default { sse_algorithm = "AES256" }   # ou "aws:kms"
  }
}
```

### Quem decide o acesso

| Mecanismo | Anexado a | Use para |
|---|---|---|
| IAM policy | role/usuário | "o que esta identidade pode fazer" (padrão) |
| Bucket policy | bucket | negar sem TLS, cross-account, restringir a VPC endpoint |
| ACL | objeto/bucket | **desabilitado** (BucketOwnerEnforced) |
| Access Point | bucket | muitos consumidores com policies separadas (opcional) |

Mesma conta: **Allow em IAM policy OU bucket policy** basta (e nenhum Deny explícito).
Cross-account: precisa de Allow **nos dois** lados.

### Ações por papel

| Papel | Ações | Recurso |
|---|---|---|
| Leitor (Redshift COPY) | `s3:GetObject` · `s3:ListBucket` (cond. `s3:prefix`) | `curated/*` |
| Escritor (Connect sink) | `s3:PutObject`, `AbortMultipartUpload`, `ListMultipartUploadParts` · `ListBucket`, `GetBucketLocation` | `raw/kafka/*` |
| Pipeline ETL | Get/Put/Delete em `raw/*`, `curated/*` | prefixos do pipeline |

### CLI

```bash
aws s3 ls s3://<BUCKET>/curated/ --profile <PROFILE>
aws s3api get-bucket-encryption --bucket <BUCKET>
aws s3api get-public-access-block --bucket <BUCKET>
aws s3 rm s3://<BUCKET> --recursive    # esvaziar antes do destroy (confirmar com o usuário!)
```

### Armadilhas

| Sintoma | Causa |
|---|---|
| `AccessDenied` no List | `s3:ListBucket` vai no ARN do **bucket**, não em `bucket/*` |
| `AccessDenied` com KMS | falta `kms:Decrypt`/`GenerateDataKey` na key policy/IAM |
| Custo de NAT alto | falta gateway endpoint S3 na VPC |
| `BucketNotEmpty` no destroy | versões antigas; esvaziar versões ou `force_destroy` (lab) |
