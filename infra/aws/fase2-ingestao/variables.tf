variable "aws_region" {
  description = "Região AWS onde toda a infraestrutura da Fase 2 é provisionada"
  type        = string
  default     = "us-east-1"
}

variable "project_prefix" {
  description = "Prefixo usado em todos os nomes de recurso desta feature"
  type        = string
  default     = "ubereats-fase2"
}

# ---------------------------------------------------------------------------
# Rede (Decisão 1 do DESIGN — EC2 com a Fase 0 dentro da VPC, sem exposição pública)
# ---------------------------------------------------------------------------

variable "vpc_cidr" {
  description = "CIDR da VPC da Fase 2"
  type        = string
  default     = "10.42.0.0/16"
}

variable "private_subnet_cidr" {
  description = "CIDR da subnet privada onde a EC2 da Fase 0 e o agente DataSync rodam"
  type        = string
  default     = "10.42.1.0/24"
}

variable "admin_access_cidr" {
  description = "CIDR autorizado a acessar a EC2 da Fase 0 via SSH/bastion para operação manual (nunca 0.0.0.0/0)"
  type        = string
}

# ---------------------------------------------------------------------------
# EC2 — sistemas self-hosted da Fase 0 (Decisão 1)
# ---------------------------------------------------------------------------

variable "fase0_ec2_instance_type" {
  description = "Tipo de instância para rodar Postgres+Oracle+MongoDB+MinIO+ShadowTraffic simultaneamente"
  type        = string
  default     = "t3.xlarge"
}

variable "fase0_ec2_key_name" {
  description = "Nome do EC2 Key Pair já existente na conta, usado para acesso SSH administrativo"
  type        = string
}

variable "fase0_ec2_ami_id" {
  description = "AMI base (Amazon Linux 2023 ou Ubuntu 22.04 com Docker) para a instância da Fase 0"
  type        = string
}

# ---------------------------------------------------------------------------
# Credenciais das fontes self-hosted — nunca hardcoded, sempre via variável (GOV-M01)
# ---------------------------------------------------------------------------

variable "postgres_password" {
  description = "Senha do usuário de replicação do Postgres (Fase 0)"
  type        = string
  sensitive   = true
}

variable "oracle_dbz_password" {
  description = "Senha do usuário de CDC do Oracle (Fase 0)"
  type        = string
  sensitive   = true
}

variable "mongo_password" {
  description = "Senha do usuário de leitura do MongoDB (Fase 0)"
  type        = string
  sensitive   = true
}

variable "minio_access_key" {
  description = "Access key do MinIO (Fase 0), usada pelo DataSync"
  type        = string
  sensitive   = true
}

variable "minio_secret_key" {
  description = "Secret key do MinIO (Fase 0), usada pelo DataSync"
  type        = string
  sensitive   = true
}

# ---------------------------------------------------------------------------
# DataSync — ativação do agente é manual (ver docs/minio/webhook-notification-config.md
# e o comentário em datasync.tf); a chave só existe depois do agente já estar rodando
# ---------------------------------------------------------------------------

variable "datasync_agent_activation_key" {
  description = "Chave de ativação do agente DataSync, obtida manualmente após o boot do agente (ver README da Etapa 1 no build report)"
  type        = string
  default     = ""
}

variable "datasync_schedule_expression" {
  description = "Expressão de agendamento do sync MinIO -> S3 (formato rate()/cron() do EventBridge)"
  type        = string
  default     = "rate(1 hour)"
}

# ---------------------------------------------------------------------------
# S3 / Redshift / Glue (Etapas 1 e 2)
# ---------------------------------------------------------------------------

variable "bronze_bucket_name" {
  description = "Nome do bucket S3 usado como Bronze única para Warehouse, Lakehouse e lookup do Kappa"
  type        = string
}

variable "redshift_admin_username" {
  description = "Usuário admin do Redshift Serverless"
  type        = string
  default     = "ubereats_admin"
}

variable "redshift_admin_password" {
  description = "Senha do admin do Redshift Serverless"
  type        = string
  sensitive   = true
}

# ---------------------------------------------------------------------------
# Kappa (Etapa 3)
# ---------------------------------------------------------------------------

variable "kinesis_stream_name" {
  description = "Nome do Kinesis Data Stream único do trilho real-time"
  type        = string
  default     = "ubereats-kappa-fase2"
}

variable "minio_webhook_auth_token" {
  description = "Token compartilhado validado pela Lambda ponte contra o header Authorization enviado pelo destino webhook do MinIO (MINIO_NOTIFY_WEBHOOK_AUTH_TOKEN no lado do MinIO) — a Function URL é pública (NONE) porque o MinIO não assina requisições com SigV4"
  type        = string
  sensitive   = true
}

variable "teams_webhook_url" {
  description = "Webhook do Microsoft Teams para alertar falhas da Lambda ponte MinIO->Kinesis (mandato SHOULD, TM-M01)"
  type        = string
  sensitive   = true
  default     = ""
}
