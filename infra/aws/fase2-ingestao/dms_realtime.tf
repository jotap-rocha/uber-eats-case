# 2ª task DMS por fonte relacional — Etapa 3 (Kappa), item 13 do manifesto.
# Só Postgres e Oracle (MongoDB nunca entra no Kinesis — Decisão do DEFINE/brainstorm,
# consumido por lookup no S3 pelo consumidor do Kappa, não por ingestão própria).
#
# migration_type = "cdc" (não "full-load-and-cdc"): o full load já foi feito pela
# task batch da Etapa 1 — esta 2ª task só replica mudanças a partir de agora.
#
# Risco carregado do DEFINE (A-003): esta task só é criada na Etapa 3, a última do
# roadmap desta fase — a janela de concorrência com a task batch (mesmo replication
# slot/LogMiner) é curta e conhecida, não um regime permanente.

resource "aws_dms_kinesis_endpoint" "kappa_target" {
  endpoint_id      = "${var.project_prefix}-kinesis-realtime-target"
  endpoint_type    = "target"
  stream_arn       = aws_kinesis_stream.kappa.arn
  message_format   = "json"
  service_access_role_arn = aws_iam_role.dms_kinesis_target.arn

  include_transaction_details    = true # transaction_id/transaction_record_id -> cdc_sequence
  include_partition_value        = true
  partition_include_schema_table = true
}

resource "aws_dms_replication_task" "postgres_realtime" {
  replication_task_id      = "${var.project_prefix}-postgres-realtime"
  migration_type           = "cdc"
  replication_instance_arn = aws_dms_replication_instance.fase2.replication_instance_arn
  source_endpoint_arn      = aws_dms_endpoint.postgres_source.endpoint_arn
  target_endpoint_arn      = aws_dms_kinesis_endpoint.kappa_target.endpoint_arn
  table_mappings           = aws_dms_replication_task.postgres_batch.table_mappings
}

resource "aws_dms_replication_task" "oracle_realtime" {
  replication_task_id      = "${var.project_prefix}-oracle-realtime"
  migration_type           = "cdc"
  replication_instance_arn = aws_dms_replication_instance.fase2.replication_instance_arn
  source_endpoint_arn      = aws_dms_endpoint.oracle_source.endpoint_arn
  target_endpoint_arn      = aws_dms_kinesis_endpoint.kappa_target.endpoint_arn
  table_mappings           = aws_dms_replication_task.oracle_batch.table_mappings
}
