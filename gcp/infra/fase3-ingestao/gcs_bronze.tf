# Bucket GCS (Bronze) — landing único, consumido por dois caminhos independentes:
# BigQuery (LOAD/MERGE, Decisão 4) e Dataproc (MERGE Iceberg, Decisão 5). Mesmo
# princípio de landing compartilhado já usado na AWS (S3) e na Azure (ADLS Gen2).

resource "google_storage_bucket" "bronze" {
  name                        = var.bronze_bucket_name
  location                    = var.gcp_region
  uniform_bucket_level_access = true
  force_destroy               = false

  versioning {
    enabled = true
  }

  lifecycle_rule {
    condition {
      age = 90
    }
    action {
      type = "Delete"
    }
  }
}
