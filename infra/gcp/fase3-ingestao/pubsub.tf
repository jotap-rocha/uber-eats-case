# Pub/Sub — trilho real-time (Etapa 3). Tópico único do Kappa, alimentado pelo
# Debezium Server (Postgres/Oracle, containers locais) e pela Cloud Function
# ponte (MinIO).

resource "google_pubsub_topic" "kappa" {
  name = var.pubsub_topic_kappa
}

resource "google_pubsub_topic" "minio_bridge" {
  name = var.pubsub_topic_minio_bridge
}

resource "google_pubsub_subscription" "kappa_dataflow" {
  name  = "${var.project_prefix}-kappa-dataflow-sub"
  topic = google_pubsub_topic.kappa.name

  ack_deadline_seconds = 60
}

resource "google_pubsub_subscription" "minio_bridge_dataflow" {
  name  = "${var.project_prefix}-minio-bridge-dataflow-sub"
  topic = google_pubsub_topic.minio_bridge.name

  ack_deadline_seconds = 60
}
