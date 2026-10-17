---
domain: aws-s3
topic: service-identity-access
---

# Pattern: acesso ao S3 por identidade de serviço (IAM role)

## Problema

Jobs e serviços precisam ler/gravar em zonas do lake sem credencial estática.
Equivalente ao "Service Principal + Storage Blob Data Contributor" do ADLS Gen2 — na AWS
a identidade é uma **IAM role** com credenciais temporárias, e a "role de dados" é uma
**IAM policy por prefixo**.

## Mapeamento Azure → AWS

| ADLS Gen2 | S3 |
|---|---|
| Service Principal (client id + secret/cert) | IAM role (sem secret; STS temporário) |
| Managed Identity | instance profile / task role / service role |
| RBAC "Storage Blob Data Contributor" no container | IAM policy `Get/Put/Delete` em `bucket/prefixo/*` |
| ACL POSIX por diretório | condição `s3:prefix` / ARN por prefixo |

## 1. Policy de dados por papel (reutilizável)

```hcl
locals {
  bucket_arn = "arn:aws:s3:::<BUCKET>"
}

data "aws_iam_policy_document" "lake_rw" {
  statement {
    sid       = "ListPrefixos"
    actions   = ["s3:ListBucket"]
    resources = [local.bucket_arn]
    condition {
      test     = "StringLike"
      variable = "s3:prefix"
      values   = ["raw/*", "curated/*"]
    }
  }
  statement {
    sid       = "RWPrefixos"
    actions   = ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"]
    resources = ["${local.bucket_arn}/raw/*", "${local.bucket_arn}/curated/*"]
  }
}

resource "aws_iam_policy" "lake_rw" {
  name   = "<PROJETO>-lake-rw"
  policy = data.aws_iam_policy_document.lake_rw.json
}
```

Crie variações `lake_ro` (só Get/List em `curated/*`) e `lake_raw_writer` (só Put em
`raw/kafka/*`). Bucket com SSE-KMS (CMK) → acrescente `kms:Decrypt`, `kms:GenerateDataKey`
na key.

## 2a. Workload em EC2/EMR — instance profile

```hcl
data "aws_iam_policy_document" "ec2_trust" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "etl" {
  name               = "<PROJETO>-etl"
  assume_role_policy = data.aws_iam_policy_document.ec2_trust.json
}

resource "aws_iam_role_policy_attachment" "etl_lake" {
  role       = aws_iam_role.etl.name
  policy_arn = aws_iam_policy.lake_rw.arn
}

resource "aws_iam_instance_profile" "etl" {
  name = "<PROJETO>-etl"
  role = aws_iam_role.etl.name
}
```

O SDK/CLI na instância pega credenciais do IMDS automaticamente — código **sem** chave:

```python
import boto3
s3 = boto3.client("s3")   # cadeia padrão → instance profile
s3.download_file("<BUCKET>", "curated/vendas/x.parquet", "/tmp/x.parquet")
```

Exija IMDSv2 nas instâncias (`metadata_options { http_tokens = "required" }`).

## 2b. Serviço gerenciado — service role

| Serviço | `principals.identifiers` no trust |
|---|---|
| ECS task | `ecs-tasks.amazonaws.com` |
| Glue job | `glue.amazonaws.com` |
| MSK Connect | `kafkaconnect.amazonaws.com` |
| Managed Flink | `kinesisanalytics.amazonaws.com` |
| Redshift (COPY) | `redshift.amazonaws.com` (+ `redshift-serverless.amazonaws.com`) |

Anexe a mesma policy de dados (ou a variação mínima) à role do serviço.

## 2c. Role assumida (cross-account ou elevação pontual)

```hcl
data "aws_iam_policy_document" "assume_from_ci" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::<AWS_ACCOUNT_ID>:role/<CALLER_ROLE>"]
    }
  }
}
```

```bash
aws sts assume-role --role-arn arn:aws:iam::<AWS_ACCOUNT_ID>:role/<PROJETO>-etl \
  --role-session-name teste-lake --query 'Credentials.Expiration'
# nunca imprima AccessKeyId/SecretAccessKey/SessionToken em log
```

Cross-account: além do trust, a **bucket policy** do bucket alvo precisa dar Allow ao
ARN da role (ver `concepts/access-model-and-defaults.md`).

## 3. Rede (VPC → S3 sem NAT)

```hcl
resource "aws_vpc_endpoint" "s3" {
  vpc_id            = var.vpc_id
  service_name      = "com.amazonaws.<REGION>.s3"
  vpc_endpoint_type = "Gateway"
  route_table_ids   = var.private_route_table_ids
}
```

Gateway endpoint S3 é gratuito e evita custo de NAT para Connect/Flink/Redshift.

## 4. Verificação (critérios de aceite)

```bash
# como a role do serviço (via sessão assumida ou na própria instância):
aws s3 ls s3://<BUCKET>/curated/                       # OK
aws s3 cp teste.txt s3://<BUCKET>/curated/_probe.txt   # OK (rw) / AccessDenied (ro)
aws s3 ls s3://<BUCKET>/landing/                       # AccessDenied (fora do escopo)
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::<AWS_ACCOUNT_ID>:role/<PROJETO>-etl \
  --action-names s3:PutObject --resource-arns arn:aws:s3:::<BUCKET>/landing/x
```

## Anti-padrões

| Errado | Certo |
|---|---|
| IAM user com access key no `.env` do job | role do runtime |
| `s3:*` em `*` | ações por papel, ARN por prefixo |
| `s3:ListBucket` em `bucket/*` | `ListBucket` no ARN do bucket + `s3:prefix` |
| URL pré-assinada de 7 dias em config | role; presigned só para troca pontual com humano |
| Bucket policy com `Principal: "*"` + Allow | Allow via IAM; bucket policy para Deny |
