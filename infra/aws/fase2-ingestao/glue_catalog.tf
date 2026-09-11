# Glue Catalog + Iceberg + Athena — Etapa 2 (Lakehouse), item 10 do manifesto.
# Zero ingestão nova: lê o mesmo S3/Bronze já populado na Etapa 1 (Decisão 2 do DESIGN).

resource "aws_glue_catalog_database" "bronze" {
  name = "${replace(var.project_prefix, "-", "_")}_bronze"
}

resource "aws_glue_crawler" "bronze" {
  name          = "${var.project_prefix}-bronze-crawler"
  role          = aws_iam_role.glue_crawler.arn
  database_name = aws_glue_catalog_database.bronze.name

  s3_target {
    path = "s3://${aws_s3_bucket.bronze.bucket}/"
  }

  # Tabela Iceberg: criada explicitamente por fonte no /build (não pelo crawler,
  # que gera schema Hive por padrão) — ver sql/aws/athena_queries.sql para o DDL
  # `CREATE TABLE ... TBLPROPERTIES ('table_type'='ICEBERG')` de cada entidade.
  schedule = "cron(0 * * * ? *)" # a cada hora, alinhado ao datasync_schedule_expression padrão
}

resource "aws_athena_workgroup" "fase2" {
  name = "${var.project_prefix}-athena-wg"

  configuration {
    result_configuration {
      output_location = "s3://${aws_s3_bucket.bronze.bucket}/_athena_results/"
    }
  }
}
