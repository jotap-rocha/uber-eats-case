variable "gcp_project_id" {
  description = "Projeto GCP onde toda a infraestrutura da Fase 3 é provisionada"
  type        = string
}

variable "gcp_region" {
  description = "Região GCP da Fase 3"
  type        = string
  default     = "us-central1"
}

variable "gcp_zone" {
  description = "Zona GCP do bastion"
  type        = string
  default     = "us-central1-a"
}

variable "project_prefix" {
  description = "Prefixo usado em todos os nomes de recurso desta feature"
  type        = string
  default     = "ubereats-fase3"
}

# ---------------------------------------------------------------------------
# Rede (Decisão 1 do DESIGN — bastion mínimo, sem migrar a Fase 0 para a GCP)
# ---------------------------------------------------------------------------

variable "vpc_cidr" {
  description = "CIDR da subnet única da Fase 3 (só hospeda o bastion — a Fase 0 continua local)"
  type        = string
  default     = "10.43.1.0/24"
}

variable "admin_access_cidr" {
  description = "CIDR autorizado a acessar o bastion via SSH para operação manual (nunca 0.0.0.0/0)"
  type        = string
}

variable "datastream_source_ranges" {
  description = <<-EOT
    CIDRs de origem do Datastream permitidos a alcançar o bastion na porta 22.
    O Datastream não publica um bloco fixo e documentado por região no momento
    deste Design — preencher com o(s) range(s) confirmados na documentação do
    Google Cloud para a região escolhida antes do `apply` real (ver Open
    Question equivalente registrada no DEFINE/DESIGN da Fase 2/AWS, agora
    também válida aqui).
  EOT
  type        = list(string)
}

# ---------------------------------------------------------------------------
# Bastion (Decisão 1)
# ---------------------------------------------------------------------------

variable "bastion_machine_type" {
  description = "Tipo de máquina do bastion — só encaminha SSH, não processa dado"
  type        = string
  default     = "e2-micro"
}

variable "bastion_ssh_public_key" {
  description = "Chave pública SSH autorizada no bastion (usuário tunnel-user), injetada via metadata"
  type        = string
}

variable "bastion_ssh_private_key" {
  description = "Chave privada correspondente, usada pelo Datastream na Forward SSH tunnel connectivity profile"
  type        = string
  sensitive   = true
}

# ---------------------------------------------------------------------------
# Credenciais das fontes self-hosted — nunca hardcoded, sempre via variável (GOV-M01)
# ---------------------------------------------------------------------------

variable "postgres_password" {
  description = "Senha do usuário de replicação do Postgres (Fase 0), usada pelo Datastream"
  type        = string
  sensitive   = true
}

variable "oracle_dbz_password" {
  description = "Senha do usuário de CDC do Oracle (Fase 0), usada pelo Datastream"
  type        = string
  sensitive   = true
}

variable "mongo_password" {
  description = "Senha do usuário de leitura do MongoDB (Fase 0), usada pelo Datastream"
  type        = string
  sensitive   = true
}

variable "minio_access_key" {
  description = "Access key do MinIO (Fase 0), usada pelo Storage Transfer Service"
  type        = string
  sensitive   = true
}

variable "minio_secret_key" {
  description = "Secret key do MinIO (Fase 0), usada pelo Storage Transfer Service"
  type        = string
  sensitive   = true
}

# ---------------------------------------------------------------------------
# GCS / BigQuery / Dataplex / Dataproc (Etapas 1 e 2)
# ---------------------------------------------------------------------------

variable "bronze_bucket_name" {
  description = "Nome do bucket GCS usado como Bronze única para Warehouse, Lakehouse e lookup do Kappa"
  type        = string
}

variable "sts_schedule_start_time" {
  description = "Horário de início do job agendado do Storage Transfer Service (MinIO -> GCS)"
  type        = string
  default     = "00:00"
}

variable "bigquery_merge_schedule" {
  description = "Expressão cron da scheduled query LOAD/MERGE do BigQuery (Decisão 4)"
  type        = string
  default     = "every 1 hours"
}

# ---------------------------------------------------------------------------
# Kappa (Etapa 3)
# ---------------------------------------------------------------------------

variable "pubsub_topic_kappa" {
  description = "Tópico Pub/Sub único do trilho real-time (Postgres + Oracle via Debezium Server)"
  type        = string
  default     = "ubereats-kappa-fase3"
}

variable "pubsub_topic_minio_bridge" {
  description = "Tópico Pub/Sub alimentado pela Cloud Function ponte (MinIO)"
  type        = string
  default     = "ubereats-kappa-minio-fase3"
}

variable "minio_webhook_auth_token" {
  description = "Token compartilhado validado pela Cloud Function ponte contra o header Authorization enviado pelo destino webhook do MinIO — mesma limitação já documentada na Fase 2/AWS (MinIO não assina requisições)"
  type        = string
  sensitive   = true
}

variable "teams_webhook_url" {
  description = "Webhook do Microsoft Teams para alertar falhas da Cloud Function ponte MinIO->Pub/Sub (mandato SHOULD, TM-M01)"
  type        = string
  sensitive   = true
  default     = ""
}
