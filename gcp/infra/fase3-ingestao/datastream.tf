# Datastream — trilho batch (Etapa 1). 3 streams (Postgres CDC, Oracle CDC via
# LogMiner, MongoDB full load), todos via "Forward SSH tunnel connectivity
# profile" apontando para o bastion (Decisão 1). Destino Cloud Storage clássico
# (arquivos JSON por evento) — não o destino nativo BigLake Iceberg tables,
# para preservar a separação de consumo da Decisão 4 (BigQuery lê o GCS bruto,
# Dataproc materializa o Iceberg separadamente, Etapa 2).

resource "google_datastream_connection_profile" "gcs_bronze" {
  connection_profile_id = "${var.project_prefix}-gcs-bronze"
  location               = var.gcp_region
  display_name           = "GCS Bronze (destino comum aos 3 streams)"

  gcs_profile {
    bucket    = google_storage_bucket.bronze.name
    root_path = "/"
  }
}

resource "google_datastream_connection_profile" "postgres_source" {
  connection_profile_id = "${var.project_prefix}-postgres-source"
  location               = var.gcp_region
  display_name           = "Postgres Fase 0 (via túnel SSH reverso)"

  postgresql_profile {
    hostname = "127.0.0.1" # relativo ao bastion — porta mapeada pelo autossh
    port     = 15432
    username = "replication_user"
    password = var.postgres_password
    database = "ubereats"
  }

  private_connectivity {
    forward_ssh_connectivity {
      hostname    = google_compute_instance.bastion.network_interface[0].access_config[0].nat_ip
      port        = 22
      username    = "tunnel-user"
      private_key = var.bastion_ssh_private_key
    }
  }
}

resource "google_datastream_connection_profile" "oracle_source" {
  connection_profile_id = "${var.project_prefix}-oracle-source"
  location               = var.gcp_region
  display_name           = "Oracle Fase 0 (via túnel SSH reverso, LogMiner)"

  oracle_profile {
    hostname        = "127.0.0.1"
    port            = 11521
    username        = "c##dbzuser"
    password        = var.oracle_dbz_password
    database_service = "FREE"
  }

  private_connectivity {
    forward_ssh_connectivity {
      hostname    = google_compute_instance.bastion.network_interface[0].access_config[0].nat_ip
      port        = 22
      username    = "tunnel-user"
      private_key = var.bastion_ssh_private_key
    }
  }
}

resource "google_datastream_connection_profile" "mongo_source" {
  connection_profile_id = "${var.project_prefix}-mongo-source"
  location               = var.gcp_region
  display_name           = "MongoDB Fase 0 (via túnel SSH reverso, full load)"

  mongodb_profile {
    hostname_addresses {
      hostname = "127.0.0.1"
      port     = 27017
    }
    username = "readonly_user"
    password = var.mongo_password
  }

  private_connectivity {
    forward_ssh_connectivity {
      hostname    = google_compute_instance.bastion.network_interface[0].access_config[0].nat_ip
      port        = 22
      username    = "tunnel-user"
      private_key = var.bastion_ssh_private_key
    }
  }
}

resource "google_datastream_stream" "postgres_batch" {
  stream_id    = "${var.project_prefix}-postgres-batch"
  location     = var.gcp_region
  display_name = "Postgres -> GCS Bronze (CDC)"

  source_config {
    source_connection_profile = google_datastream_connection_profile.postgres_source.id
    postgresql_source_config {
      publication       = "ubereats_datastream_pub"
      replication_slot  = "ubereats_datastream_slot" # slot dedicado, distinto do Airbyte (Onda 3)
    }
  }

  destination_config {
    destination_connection_profile = google_datastream_connection_profile.gcs_bronze.id
    gcs_destination_config {
      path             = "/postgres"
      file_rotation_mb = 100
      json_file_format {
        schema_file_format = "NO_SCHEMA_FILE"
      }
    }
  }

  backfill_all {}
}

resource "google_datastream_stream" "oracle_batch" {
  stream_id    = "${var.project_prefix}-oracle-batch"
  location     = var.gcp_region
  display_name = "Oracle -> GCS Bronze (CDC via LogMiner)"

  source_config {
    source_connection_profile = google_datastream_connection_profile.oracle_source.id
    oracle_source_config {}
  }

  destination_config {
    destination_connection_profile = google_datastream_connection_profile.gcs_bronze.id
    gcs_destination_config {
      path             = "/oracle"
      file_rotation_mb = 100
      json_file_format {
        schema_file_format = "NO_SCHEMA_FILE"
      }
    }
  }

  backfill_all {}
}

resource "google_datastream_stream" "mongo_batch" {
  stream_id    = "${var.project_prefix}-mongo-batch"
  location     = var.gcp_region
  display_name = "MongoDB -> GCS Bronze (full load/snapshot, sem CDC)"

  source_config {
    source_connection_profile = google_datastream_connection_profile.mongo_source.id
    mongodb_source_config {}
  }

  destination_config {
    destination_connection_profile = google_datastream_connection_profile.gcs_bronze.id
    gcs_destination_config {
      path             = "/mongodb"
      file_rotation_mb = 100
      json_file_format {
        schema_file_format = "NO_SCHEMA_FILE"
      }
    }
  }

  backfill_all {}
}
