---
domain: aws-redshift
topic: bulk-load
---

# Pattern: carga em massa S3 → Redshift (`COPY` + IAM role)

## Problema

Carregar a zona `curated/` do S3 no Redshift Serverless em paralelo, sem credencial no
SQL e com erro rastreável. Equivalente ao `COPY INTO` do Synapse.

## 1. Role que o Redshift assume

```hcl
data "aws_iam_policy_document" "redshift_trust" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["redshift.amazonaws.com", "redshift-serverless.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "copy" {
  name               = "<PROJETO>-redshift-copy"
  assume_role_policy = data.aws_iam_policy_document.redshift_trust.json
}

data "aws_iam_policy_document" "copy_s3" {
  statement {
    actions   = ["s3:ListBucket"]
    resources = ["arn:aws:s3:::<BUCKET>"]
    condition {
      test     = "StringLike"
      variable = "s3:prefix"
      values   = ["curated/*"]
    }
  }
  statement {
    actions   = ["s3:GetObject"]
    resources = ["arn:aws:s3:::<BUCKET>/curated/*"]
  }
}

resource "aws_iam_role_policy" "copy_s3" {
  role   = aws_iam_role.copy.id
  policy = data.aws_iam_policy_document.copy_s3.json
}
```

Associe no namespace: `iam_roles = [aws_iam_role.copy.arn]` e
`default_iam_role_arn = aws_iam_role.copy.arn` (ver `quick-reference.md`).
Bucket com SSE-KMS → adicionar `kms:Decrypt` na chave.

## 2. Staging + COPY

```sql
CREATE SCHEMA IF NOT EXISTS staging;

CREATE TABLE IF NOT EXISTS staging.clientes (
  cliente_id   BIGINT,
  nome         VARCHAR(200),
  email_hash   VARCHAR(64),     -- PII já pseudonimizada na zona curated
  cidade       VARCHAR(100),
  atualizado_em TIMESTAMP
);

TRUNCATE staging.clientes;    -- staging é efêmera (não é produção)

COPY staging.clientes
FROM 's3://<BUCKET>/curated/clientes/dt=2026-10-16/'
IAM_ROLE default                      -- ou 'arn:aws:iam::<AWS_ACCOUNT_ID>:role/<PROJETO>-redshift-copy'
FORMAT AS PARQUET;
```

### Formatos

| Formato | Cláusula | Observação |
|---|---|---|
| Parquet / ORC | `FORMAT AS PARQUET` | colunas casam por **posição**/ordem; recomendado |
| CSV | `FORMAT AS CSV IGNOREHEADER 1 DELIMITER ','` | `DATEFORMAT 'auto'`, `TIMEFORMAT 'auto'` |
| JSON | `FORMAT AS JSON 'auto'` | casa por nome de chave; `'auto ignorecase'` |

### Boas práticas

- Aponte para um **prefixo** (ou `MANIFEST`), não arquivo único — o COPY paraleliza por
  arquivo. Arquivos de 100 MB–1 GB comprimidos, quantidade múltipla de slices.
- Use `MANIFEST` quando precisar de lista exata (evita pegar arquivo parcial):

```sql
COPY staging.clientes
FROM 's3://<BUCKET>/manifests/clientes-2026-10-16.manifest'
IAM_ROLE default FORMAT AS PARQUET MANIFEST;
```

- CSV/JSON: `MAXERROR 0` (default) em produção; em exploração, `MAXERROR 10` + inspeção.
- `COMPUPDATE OFF STATUPDATE OFF` em staging truncada a cada carga (acelera);
  rode `ANALYZE` na tabela final depois do MERGE.

## 3. Diagnóstico

```sql
SELECT query_id, file_name, line_number, column_name, error_message
FROM sys_load_error_detail
ORDER BY start_time DESC LIMIT 20;

SELECT query_id, table_name, loaded_rows, status, duration
FROM sys_load_history ORDER BY start_time DESC LIMIT 10;
```

`sys_load_error_detail` pode mostrar trechos da linha rejeitada — **não** cole em issue
se a tabela tem PII.

## 4. Orquestração

- Data API (sem driver), bom para Airflow/Step Functions:

```bash
aws redshift-data execute-statement --workgroup-name <PROJETO>-wg --database analytics \
  --sql "COPY staging.clientes FROM 's3://<BUCKET>/curated/clientes/dt=2026-10-16/' IAM_ROLE default FORMAT AS PARQUET"
```

- Auto-copy (`COPY ... JOB CREATE`) carrega novos arquivos do prefixo automaticamente;
  exige IAM role (não `SESSION`). **A validar** custo de RPU contínuo antes de usar em lab.

## Anti-padrões

| Errado | Certo |
|---|---|
| `CREDENTIALS 'aws_access_key_id=...'` | `IAM_ROLE default` |
| `INSERT` linha a linha via driver | `COPY` de arquivos no S3 |
| COPY direto na dimensão final | staging → `MERGE` (ver `merge-scd2.md`) |
| Role com `s3:*` em `*` | `GetObject` só em `curated/*` |
