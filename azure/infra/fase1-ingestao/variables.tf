variable "azure_location" {
  description = "Regiao Azure para todos os recursos da Fase 1"
  type        = string
  default     = "brazilsouth"
}

variable "azure_tenant_id" {
  description = "Tenant ID do Azure AD (Service Principal do Unity Catalog, Decisao 4 do DESIGN)"
  type        = string
  sensitive   = true
}

variable "databricks_workspace_host" {
  description = "URL do workspace Databricks Free Edition (fora da subscription Azure)"
  type        = string
}

variable "databricks_pat_token" {
  description = "Personal Access Token do Databricks Free Edition, usado para o provider databricks"
  type        = string
  sensitive   = true
}

variable "postgres_replication_password" {
  description = "Senha do usuario de replicacao do Postgres (usado pelo Airbyte, conexao CDC real-time)"
  type        = string
  sensitive   = true
}

variable "eventhub_namespace_connection_string" {
  description = "Connection string do Event Hubs Namespace, usada por Airbyte/MinIO/Kafka Connect (SASL_SSL)"
  type        = string
  sensitive   = true
  default     = ""
}
