# Dataflow — consumidor do Kappa (Decisão 6, item 28 do manifesto). Flex
# Template: a construção da imagem (`gcloud dataflow flex-template build`) é
# um passo de CI/build separado, não coberto pelo Terraform — este resource
# assume que o template já foi publicado no GCS antes do apply.

variable "dataflow_flex_template_gcs_path" {
  description = "Caminho GCS do Flex Template já construído (gcloud dataflow flex-template build) para o pipeline em src/gcp/dataflow_kappa_consumer/pipeline.py"
  type        = string
  default     = ""
}

resource "google_dataflow_flex_template_job" "kappa_consumer" {
  count = var.dataflow_flex_template_gcs_path != "" ? 1 : 0

  provider                = google
  name                    = "${var.project_prefix}-kappa-consumer"
  container_spec_gcs_path = var.dataflow_flex_template_gcs_path
  region                  = var.gcp_region

  parameters = {
    inputSubscription = google_pubsub_subscription.kappa_dataflow.id
    biglakeDataset    = google_bigquery_dataset.biglake_iceberg.dataset_id
  }

  service_account_email = google_service_account.dataflow_consumer.email

  on_delete = "cancel"
}
