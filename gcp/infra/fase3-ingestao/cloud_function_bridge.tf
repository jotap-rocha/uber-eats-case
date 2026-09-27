# Cloud Function ponte MinIO -> Pub/Sub (Decisão 7, item 24 do manifesto).
# HTTP trigger via URL pública — MinIO não assina requisições com SigV4, então
# a autenticação é um token estático validado no handler (mesma limitação já
# documentada na Fase 2/AWS).

data "archive_file" "cloud_function_bridge" {
  type        = "zip"
  source_dir  = "${path.module}/../../../src/gcp/cloud_function_minio_pubsub_bridge"
  output_path = "${path.module}/.build/cloud_function_minio_pubsub_bridge.zip"
}

resource "google_storage_bucket_object" "cloud_function_bridge_source" {
  name   = "cloud-functions/minio_pubsub_bridge-${data.archive_file.cloud_function_bridge.output_base64sha256}.zip"
  bucket = google_storage_bucket.bronze.name
  source = data.archive_file.cloud_function_bridge.output_path
}

resource "google_cloudfunctions2_function" "minio_pubsub_bridge" {
  name     = "${var.project_prefix}-minio-pubsub-bridge"
  location = var.gcp_region

  build_config {
    runtime     = "python312"
    entry_point = "handler"
    source {
      storage_source {
        bucket = google_storage_bucket.bronze.name
        object = google_storage_bucket_object.cloud_function_bridge_source.name
      }
    }
  }

  service_config {
    available_memory      = "256M"
    timeout_seconds        = 30
    service_account_email = google_service_account.cloud_function_bridge.email

    environment_variables = {
      GCP_PROJECT_ID           = var.gcp_project_id
      PUBSUB_TOPIC_MINIO       = google_pubsub_topic.minio_bridge.name
      MINIO_WEBHOOK_AUTH_TOKEN = var.minio_webhook_auth_token
      TEAMS_WEBHOOK_URL        = var.teams_webhook_url
    }
  }
}

# Function URL pública (NONE) — mesma decisão já tomada na Fase 2/AWS (Lambda
# Function URL), pelo mesmo motivo: MinIO não suporta autenticação assinada.
resource "google_cloud_run_service_iam_member" "bridge_public_invoker" {
  location = google_cloudfunctions2_function.minio_pubsub_bridge.location
  service  = google_cloudfunctions2_function.minio_pubsub_bridge.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
