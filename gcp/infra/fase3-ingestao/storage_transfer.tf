# Storage Transfer Service — MinIO -> GCS (Etapa 1, Decisão 3). O agente roda
# containerizado no docker-compose.yml LOCAL (item 9 do manifesto), não numa VM
# GCP dedicada como a AMI da AWS DataSync — é push-based (outbound), sem
# precisar do túnel SSH.

resource "google_storage_transfer_agent_pool" "fase3" {
  agent_pool_id = "${var.project_prefix}-agent-pool"
  display_name  = "Agent pool — agente containerizado local (MinIO)"
}

resource "google_storage_transfer_job" "minio_to_gcs" {
  description = "MinIO (self-hosted, S3-compatible) -> GCS/Bronze"

  transfer_spec {
    aws_s3_data_source {
      bucket_name = "ubereats-minio-bucket"
      aws_access_key {
        access_key_id     = var.minio_access_key
        secret_access_key = var.minio_secret_key
      }
      # Endpoint customizado (S3-compatible) apontando para o MinIO local —
      # exige provider google >= 6.x com suporte a endpoint customizado no
      # data source S3-compatible; confirmar no /build antes do apply real.
      endpoint = "http://minio-ubereats:9000"
    }

    gcs_data_sink {
      bucket_name = google_storage_bucket.bronze.name
      path        = "minio/"
    }

    transfer_options {
      overwrite_objects_already_existing_in_sink = false
    }
  }

  schedule {
    schedule_start_date {
      year  = 2026
      month = 1
      day   = 1
    }
    start_time_of_day {
      hours   = tonumber(split(":", var.sts_schedule_start_time)[0])
      minutes = tonumber(split(":", var.sts_schedule_start_time)[1])
      seconds = 0
      nanos   = 0
    }
  }
}
