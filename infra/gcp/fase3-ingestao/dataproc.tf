# Dataproc — processamento/consulta das tabelas Iceberg do BigLake (Etapa 2,
# Lakehouse). Job serverless (Batch), agendado via Cloud Scheduler + Workflow
# Templates API (orquestração fina fica para o /build).

resource "google_storage_bucket_object" "merge_job_script" {
  name   = "dataproc/merge_job.py"
  bucket = google_storage_bucket.bronze.name
  source = "${path.module}/../../../src/gcp/dataproc_iceberg_merge/merge_job.py"
}

resource "google_dataproc_batch" "iceberg_merge" {
  batch_id = "${var.project_prefix}-iceberg-merge"
  location = var.gcp_region

  pyspark_batch {
    main_python_file_uri = "gs://${google_storage_bucket.bronze.name}/${google_storage_bucket_object.merge_job_script.name}"
    args = [
      "--bronze-bucket=${google_storage_bucket.bronze.name}",
      "--connection=${google_bigquery_connection.biglake.name}",
      "--dataset=${google_bigquery_dataset.biglake_iceberg.dataset_id}",
    ]
  }

  runtime_config {
    version = "2.2"
  }

  environment_config {
    execution_config {
      service_account = google_service_account.dataproc_iceberg_merge.email
    }
  }
}

resource "google_cloud_scheduler_job" "iceberg_merge_trigger" {
  name      = "${var.project_prefix}-iceberg-merge-trigger"
  region    = var.gcp_region
  schedule  = "0 * * * *" # a cada hora — ajustar no /build conforme frescor desejado

  http_target {
    uri         = "https://dataproc.googleapis.com/v1/projects/${var.gcp_project_id}/locations/${var.gcp_region}/batches"
    http_method = "POST"
    oauth_token {
      service_account_email = google_service_account.dataproc_iceberg_merge.email
    }
  }
}
