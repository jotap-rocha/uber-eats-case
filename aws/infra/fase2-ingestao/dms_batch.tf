# AWS DMS — trilho batch (Etapa 1). 1 task por fonte relacional/documental, todas
# com target S3 (Bronze). Postgres e Oracle em ongoing replication (full-load-and-cdc);
# MongoDB em full load/snapshot, sem CDC (fonte estática, decisão da Onda 3).

resource "aws_dms_replication_subnet_group" "fase2" {
  replication_subnet_group_id          = "${var.project_prefix}-dms-subnet-group"
  replication_subnet_group_description = "Subnet privada onde a replication instance acessa os sistemas da Fase 0"
  subnet_ids                           = [aws_subnet.private.id]
}

resource "aws_dms_replication_instance" "fase2" {
  replication_instance_id    = "${var.project_prefix}-dms-instance"
  replication_instance_class = "dms.t3.medium"
  allocated_storage          = 50
  vpc_security_group_ids     = [aws_security_group.fase0_ec2.id]
  replication_subnet_group_id = aws_dms_replication_subnet_group.fase2.id
  publicly_accessible        = false
}

# ---------------------------------------------------------------------------
# Endpoints de origem — todos apontam para a EC2 da Fase 0 (Decisão 1)
# ---------------------------------------------------------------------------

resource "aws_dms_endpoint" "postgres_source" {
  endpoint_id   = "${var.project_prefix}-postgres-source"
  endpoint_type = "source"
  engine_name   = "postgres"

  server_name   = aws_instance.fase0.private_ip
  port          = 5432
  database_name = "ubereats"
  username      = "replication_user"
  password      = var.postgres_password

  # Requer wal_level=logical já configurado no Postgres da Fase 0 (mesma exigência
  # já satisfeita pelo Airbyte na Onda 3 — nenhuma mudança no lado da fonte).
}

resource "aws_dms_endpoint" "oracle_source" {
  endpoint_id   = "${var.project_prefix}-oracle-source"
  endpoint_type = "source"
  engine_name   = "oracle"

  server_name   = aws_instance.fase0.private_ip
  port          = 1521
  database_name = "FREE"
  username      = "c##dbzuser"
  password      = var.oracle_dbz_password

  # Requer ARCHIVELOG + supplemental logging já habilitados (mesmo script da Onda 3,
  # DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md, Decisão 6) — DMS usa LogMiner, igual ao Debezium.
}

resource "aws_dms_endpoint" "mongo_source" {
  endpoint_id   = "${var.project_prefix}-mongo-source"
  endpoint_type = "source"
  engine_name   = "mongodb"

  server_name   = aws_instance.fase0.private_ip
  port          = 27017
  database_name = "ubereats"
  username      = "readonly_user"
  password      = var.mongo_password

  mongo_db_settings {
    auth_type   = "PASSWORD"
    auth_source = "admin"
    nesting_level = "NONE" # modo "table", não "document" — decisão já registrada no roadmap v1.5
  }
}

# ---------------------------------------------------------------------------
# Target S3 comum às 3 tasks batch
# ---------------------------------------------------------------------------

resource "aws_dms_s3_endpoint" "bronze_target" {
  endpoint_id     = "${var.project_prefix}-s3-bronze-target"
  endpoint_type   = "target"
  bucket_name     = aws_s3_bucket.bronze.bucket
  service_access_role_arn = aws_iam_role.dms_s3_target.arn

  # Contrato canônico de CDC (docs/data-contract-cdc-aws-dms.md):
  include_op_for_full_load    = true
  timestamp_column_name       = "cdc_commit_ts"
  add_column_name             = true
  include_transaction_details = true
  cdc_path                    = "cdc"
}

# ---------------------------------------------------------------------------
# Tasks — 1 por fonte, prefixo de bucket dedicado
# ---------------------------------------------------------------------------

resource "aws_dms_replication_task" "postgres_batch" {
  replication_task_id      = "${var.project_prefix}-postgres-batch"
  migration_type           = "full-load-and-cdc"
  replication_instance_arn = aws_dms_replication_instance.fase2.replication_instance_arn
  source_endpoint_arn      = aws_dms_endpoint.postgres_source.endpoint_arn
  target_endpoint_arn      = aws_dms_s3_endpoint.bronze_target.endpoint_arn

  table_mappings = jsonencode({
    rules = [{
      rule-type      = "selection"
      rule-id        = "1"
      rule-name      = "all-tables"
      object-locator = { schema-name = "public", table-name = "%" }
      rule-action    = "include"
    }]
  })
}

resource "aws_dms_replication_task" "oracle_batch" {
  replication_task_id      = "${var.project_prefix}-oracle-batch"
  migration_type           = "full-load-and-cdc"
  replication_instance_arn = aws_dms_replication_instance.fase2.replication_instance_arn
  source_endpoint_arn      = aws_dms_endpoint.oracle_source.endpoint_arn
  target_endpoint_arn      = aws_dms_s3_endpoint.bronze_target.endpoint_arn

  table_mappings = jsonencode({
    rules = [{
      rule-type      = "selection"
      rule-id        = "1"
      rule-name      = "all-tables"
      object-locator = { schema-name = "UBEREATS", table-name = "%" }
      rule-action    = "include"
    }]
  })
}

resource "aws_dms_replication_task" "mongo_batch" {
  replication_task_id      = "${var.project_prefix}-mongo-batch"
  migration_type           = "full-load" # sem CDC — fonte estática (Onda 3)
  replication_instance_arn = aws_dms_replication_instance.fase2.replication_instance_arn
  source_endpoint_arn      = aws_dms_endpoint.mongo_source.endpoint_arn
  target_endpoint_arn      = aws_dms_s3_endpoint.bronze_target.endpoint_arn

  table_mappings = jsonencode({
    rules = [{
      rule-type      = "selection"
      rule-id        = "1"
      rule-name      = "perfil-restaurante"
      object-locator = { schema-name = "ubereats", table-name = "perfil_restaurante" }
      rule-action    = "include"
    }]
  })
}
