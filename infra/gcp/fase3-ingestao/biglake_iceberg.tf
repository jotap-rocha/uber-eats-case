# BigLake — conexão para as tabelas Iceberg materializadas pelo job Dataproc
# (Decisão 5). A criação da tabela Iceberg em si (CREATE TABLE ... WITH
# CONNECTION ... OPTIONS(table_format='ICEBERG', ...)) é DDL executada pelo
# job (src/gcp/dataproc_iceberg_merge/merge_job.py), não um resource Terraform
# — o provider google não expõe todas as opções específicas de tabela Iceberg
# no resource google_bigquery_table na versão fixada (ver Open Question no
# BUILD_REPORT).

resource "google_bigquery_connection" "biglake" {
  connection_id = "${var.project_prefix}-biglake-connection"
  location      = var.gcp_region

  cloud_resource {}
}

resource "google_project_iam_member" "biglake_connection_storage_reader" {
  project = var.gcp_project_id
  role    = "roles/storage.objectViewer"
  member  = "serviceAccount:${google_bigquery_connection.biglake.cloud_resource[0].service_account_id}"
}

resource "google_bigquery_dataset" "biglake_iceberg" {
  dataset_id = "biglake_iceberg"
  location   = var.gcp_region
}
