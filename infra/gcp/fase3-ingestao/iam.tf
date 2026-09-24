# Service accounts least-privilege por componente (mandato GOV-M01 do DEFINE).

resource "google_service_account" "storage_transfer" {
  account_id   = "${var.project_prefix}-sts"
  display_name = "Storage Transfer Service — MinIO -> GCS/Bronze"
}

resource "google_storage_bucket_iam_member" "storage_transfer_bronze_writer" {
  bucket = var.bronze_bucket_name
  role   = "roles/storage.objectAdmin"
  member = "serviceAccount:${google_service_account.storage_transfer.email}"
}

resource "google_service_account" "cloud_function_bridge" {
  account_id   = "${var.project_prefix}-fn-bridge"
  display_name = "Cloud Function ponte MinIO -> Pub/Sub"
}

resource "google_pubsub_topic_iam_member" "cloud_function_bridge_publisher" {
  topic  = var.pubsub_topic_minio_bridge
  role   = "roles/pubsub.publisher"
  member = "serviceAccount:${google_service_account.cloud_function_bridge.email}"

  depends_on = [google_pubsub_topic.minio_bridge]
}

resource "google_service_account" "dataflow_consumer" {
  account_id   = "${var.project_prefix}-dataflow"
  display_name = "Dataflow — consumidor do Kappa"
}

resource "google_project_iam_member" "dataflow_worker" {
  project = var.gcp_project_id
  role    = "roles/dataflow.worker"
  member  = "serviceAccount:${google_service_account.dataflow_consumer.email}"
}

resource "google_project_iam_member" "dataflow_bigquery_data_viewer" {
  project = var.gcp_project_id
  role    = "roles/bigquery.dataViewer"
  member  = "serviceAccount:${google_service_account.dataflow_consumer.email}"
}

resource "google_service_account" "dataproc_iceberg_merge" {
  account_id   = "${var.project_prefix}-dataproc"
  display_name = "Dataproc — job de MERGE do Iceberg (BigLake)"
}

resource "google_project_iam_member" "dataproc_worker" {
  project = var.gcp_project_id
  role    = "roles/dataproc.worker"
  member  = "serviceAccount:${google_service_account.dataproc_iceberg_merge.email}"
}

resource "google_storage_bucket_iam_member" "dataproc_bronze_reader" {
  bucket = var.bronze_bucket_name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.dataproc_iceberg_merge.email}"
}
