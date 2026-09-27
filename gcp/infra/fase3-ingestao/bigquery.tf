# BigQuery — carga física a partir do GCS/Bronze (Etapa 1, Decisão 4). Sem
# query-in-place: o job LOAD/MERGE materializa o dado no storage nativo do
# BigQuery, mesmo padrão de Redshift (AWS) e Synapse (Azure).

resource "google_bigquery_dataset" "bronze" {
  dataset_id = "ubereats_bronze"
  location   = var.gcp_region
}

resource "google_bigquery_dataset" "warehouse" {
  dataset_id = "ubereats_warehouse"
  location   = var.gcp_region
}

# Scheduled query — dispara o LOAD/MERGE (sql/gcp/bigquery_load_merge.sql)
# periodicamente. Nota: LOAD DATA + MERGE como 2 statements num script só é
# suportado pela Data Transfer Service a partir de multi-statement scripts;
# confirmar no /build se o job precisa ser dividido em duas scheduled queries
# ou orquestrado via Cloud Composer/Cloud Scheduler + Cloud Function.
resource "google_bigquery_data_transfer_config" "load_merge_restaurants" {
  display_name           = "${var.project_prefix}-load-merge-restaurants"
  location               = var.gcp_region
  data_source_id         = "scheduled_query"
  schedule                = var.bigquery_merge_schedule
  destination_dataset_id = google_bigquery_dataset.warehouse.dataset_id

  params = {
    query = file("${path.module}/../../../sql/gcp/bigquery_load_merge.sql")
  }
}
