# Dataplex Universal Catalog — governança/catalogação do Lakehouse (papel
# equivalente ao Unity Catalog/Glue). Aponta para o GCS/Bronze e para as
# tabelas Iceberg do BigLake (Etapa 2).

resource "google_dataplex_lake" "fase3" {
  name     = "${var.project_prefix}-lake"
  location = var.gcp_region
}

resource "google_dataplex_zone" "curated" {
  name     = "${var.project_prefix}-curated-zone"
  lake     = google_dataplex_lake.fase3.name
  location = var.gcp_region
  type     = "CURATED"

  discovery_spec {
    enabled = true
  }

  resource_spec {
    location_type = "SINGLE_REGION"
  }
}

resource "google_dataplex_asset" "bronze_bucket" {
  name     = "${var.project_prefix}-bronze-asset"
  lake     = google_dataplex_lake.fase3.name
  zone     = google_dataplex_zone.curated.name
  location = var.gcp_region

  discovery_spec {
    enabled = true
  }

  resource_spec {
    name = "projects/${var.gcp_project_id}/buckets/${google_storage_bucket.bronze.name}"
    type = "STORAGE_BUCKET"
  }
}
