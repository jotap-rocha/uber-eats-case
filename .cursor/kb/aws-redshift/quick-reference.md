---
domain: aws-redshift
topic: quick-reference
---

# Redshift Serverless — Quick Reference

### Números que importam

| Item | Valor |
|---|---|
| Base RPU | mín **4**, depois múltiplos de 8 (8, 16, 24 … 512); default **128** (caro!) |
| 4 RPU | até 32 TB, recomendado ≤ 100 colunas/tabela, 64 GB RAM; regiões limitadas |
| 1 RPU | 16 GB de memória |
| Preço | US$ 0,375/RPU-h (us-east-1), por segundo, mínimo 60 s |
| Trial | US$ 300 / 90 dias (primeira vez) |
| Usage limits | até 4 por workgroup; período daily/weekly/monthly |

### Terraform mínimo

```hcl
resource "aws_redshiftserverless_namespace" "dw" {
  namespace_name        = "<PROJETO>-dw"
  db_name               = "analytics"
  admin_username        = "dwadmin"
  manage_admin_password = true                          # senha no Secrets Manager
  iam_roles             = [aws_iam_role.copy.arn]
  default_iam_role_arn  = aws_iam_role.copy.arn
}

resource "aws_redshiftserverless_workgroup" "dw" {
  namespace_name      = aws_redshiftserverless_namespace.dw.namespace_name
  workgroup_name      = "<PROJETO>-wg"
  base_capacity       = 8
  max_capacity        = 16                              # teto de RPU
  publicly_accessible = false
  subnet_ids          = var.private_subnet_ids
  security_group_ids  = [aws_security_group.dw.id]
}

resource "aws_redshiftserverless_usage_limit" "daily" {
  resource_arn  = aws_redshiftserverless_workgroup.dw.arn
  usage_type    = "serverless-compute"
  amount        = 8              # RPU-horas por dia
  period        = "daily"
  breach_action = "deactivate"   # log | emit-metric | deactivate
}
```

### SQL essencial

```sql
COPY staging.clientes
FROM 's3://<BUCKET>/curated/clientes/dt=2026-10-16/'
IAM_ROLE default
FORMAT AS PARQUET;

MERGE INTO dw.dim_cliente USING staging.src s ON dw.dim_cliente.cliente_id = s.cliente_id
WHEN MATCHED THEN UPDATE SET nome = s.nome
WHEN NOT MATCHED THEN INSERT VALUES (s.cliente_id, s.nome);
```

### Diagnóstico

```sql
SELECT * FROM sys_load_error_detail ORDER BY start_time DESC LIMIT 20;   -- erros de COPY
SELECT * FROM sys_serverless_usage ORDER BY end_time DESC LIMIT 50;      -- RPU consumidos
```

### Armadilhas

| Sintoma | Causa |
|---|---|
| Conta alta sem queries "suas" | BI/agendador mantendo compute acordado |
| `Found multiple matches to update the same tuple` | fonte do MERGE com chave duplicada |
| COPY `Access denied` | role não associada ao namespace ou sem `s3:ListBucket` |
| Não volta para 4 RPU | após escalar acima de 4, não desce sozinho — ajuste manual |
