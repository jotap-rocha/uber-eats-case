output "bronze_bucket_name" {
  description = "Bucket GCS Bronze — landing único do trilho batch"
  value       = google_storage_bucket.bronze.name
}

output "pubsub_topic_kappa" {
  description = "Tópico Pub/Sub do trilho real-time (Postgres/Oracle via Debezium Server)"
  value       = google_pubsub_topic.kappa.name
}

output "pubsub_topic_minio_bridge" {
  description = "Tópico Pub/Sub alimentado pela Cloud Function ponte (MinIO)"
  value       = google_pubsub_topic.minio_bridge.name
}

output "cloud_function_bridge_url" {
  description = "URL pública da Cloud Function ponte MinIO -> Pub/Sub, para configurar o destino webhook do MinIO"
  value       = google_cloudfunctions2_function.minio_pubsub_bridge.url
}

output "dataplex_lake_name" {
  description = "Nome do Dataplex Universal Catalog lake"
  value       = google_dataplex_lake.fase3.name
}
