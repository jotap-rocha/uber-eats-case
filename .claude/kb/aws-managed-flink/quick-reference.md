---
domain: aws-managed-flink
topic: quick-reference
---

# Managed Flink — Quick Reference

### Números

| Item | Valor |
|---|---|
| Runtime recomendado | `FLINK-1_20` (Apache Flink 1.20.5, LTS da linha 1.x) |
| Studio (Zeppelin) | só runtime Flink **1.15** |
| KPU | 1 vCPU + 4 GB · US$ 0,11/h · +1 KPU orquestração por app |
| Lab mínimo | parallelism 1 → 2 KPU ≈ US$ 0,22/h |

### Terraform mínimo

```hcl
resource "aws_kinesisanalyticsv2_application" "app" {
  name                   = "<PROJETO>-flink"
  runtime_environment    = "FLINK-1_20"
  service_execution_role = aws_iam_role.flink.arn
  start_application      = false                  # liga só quando for testar

  application_configuration {
    application_code_configuration {
      code_content_type = "ZIPFILE"
      code_content {
        s3_content_location {
          bucket_arn = "arn:aws:s3:::<ARTIFACTS_BUCKET>"
          file_key   = "flink/app.zip"
        }
      }
    }
    flink_application_configuration {
      parallelism_configuration {
        configuration_type   = "CUSTOM"
        parallelism          = 1
        parallelism_per_kpu  = 1
        auto_scaling_enabled = false
      }
      checkpoint_configuration { configuration_type = "DEFAULT" }
    }
    environment_properties {
      property_group {
        property_group_id = "app"
        property_map = {
          "msk.bootstrap"  = aws_msk_serverless_cluster.this.bootstrap_brokers_sasl_iam
          "reference.path" = "s3://<BUCKET>/reference/lojas/"
        }
      }
    }
    vpc_configuration {
      subnet_ids         = var.private_subnet_ids
      security_group_ids = [aws_security_group.flink.id]
    }
  }
}
```

### Ciclo de vida (CLI)

```bash
aws kinesisanalyticsv2 start-application --application-name <PROJETO>-flink \
  --run-configuration '{"FlinkRunConfiguration":{"AllowNonRestoredState":false}}'
aws kinesisanalyticsv2 describe-application --application-name <PROJETO>-flink \
  --query 'ApplicationDetail.ApplicationStatus'        # STARTING | RUNNING | READY ...
aws kinesisanalyticsv2 stop-application --application-name <PROJETO>-flink   # para de cobrar KPU
```

### Reference data — escolha rápida

| Reference data | Técnica |
|---|---|
| Arquivo pequeno no S3, muda raramente | regular join com tabela `filesystem` bounded (restart para recarregar) |
| Tabela em banco (RDS/Aurora) | **lookup join** JDBC com cache |
| Muda com frequência, quer versão no tempo do evento | tópico **compactado** no MSK + `upsert-kafka` + **temporal join** |
| Lógica custom / reload periódico do S3 | DataStream **broadcast state** |

Detalhes: `patterns/reference-data.md`.

### Janela (Flink SQL)

```sql
SELECT window_start, window_end, loja_id, COUNT(*) AS pedidos
FROM TABLE(TUMBLE(TABLE pedidos, DESCRIPTOR(ts_evento), INTERVAL '5' MINUTES))
GROUP BY window_start, window_end, loja_id;
```

### Armadilhas

| Sintoma | Causa |
|---|---|
| Conta alta sem tráfego | app em `RUNNING`; dê `stop-application` |
| Timeout no MSK | app sem `vpc_configuration` / SG sem saída 9098 |
| `ClassNotFound` connector | jar do connector não empacotado no zip (uber-jar) |
| Studio não acha recurso de 1.20 | Studio está em Flink 1.15 |
