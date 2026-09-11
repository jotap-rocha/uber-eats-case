# AWS DataSync — MinIO -> S3 (Etapa 1). Item 5 do manifesto.
#
# Nota operacional: o location type "Self-managed object storage" exige um AGENTE
# DataSync rodando dentro da rede que enxerga o MinIO (AWS não acessa storage
# self-hosted diretamente). O agente é uma AMI publicada pela AWS; depois de subir,
# ele expõe um console local (porta 443) onde se obtém a activation_key — passo
# manual, documentado em docs/minio/webhook-notification-config.md. Terraform não
# consegue automatizar essa ativação sem um passo local-exec contra o IP do agente.

resource "aws_instance" "datasync_agent" {
  ami                    = var.fase0_ec2_ami_id # substituir pela AMI oficial do agente DataSync na região no /build
  instance_type          = "m5.2xlarge"         # tamanho mínimo recomendado pela AWS para o agente
  subnet_id              = aws_subnet.private.id
  vpc_security_group_ids = [aws_security_group.datasync_agent.id]

  tags = {
    Name = "${var.project_prefix}-datasync-agent"
  }
}

resource "aws_datasync_agent" "fase2" {
  ip_address = aws_instance.datasync_agent.private_ip
  name       = "${var.project_prefix}-datasync-agent"

  # activation_key vem do console local do agente (ver nota acima) — enquanto vazio,
  # este recurso não pode ser aplicado; preencher via -var ou .tfvars após o passo manual.
  activation_key = var.datasync_agent_activation_key
}

resource "aws_datasync_location_object_storage" "minio_source" {
  agent_arns      = [aws_datasync_agent.fase2.arn]
  server_hostname = aws_instance.fase0.private_ip
  server_port     = 9000
  bucket_name     = "ubereats-minio-bucket"
  access_key      = var.minio_access_key
  secret_key      = var.minio_secret_key
}

resource "aws_datasync_location_s3" "bronze_target" {
  s3_bucket_arn = aws_s3_bucket.bronze.arn
  subdirectory  = "/minio"

  s3_config {
    bucket_access_role_arn = aws_iam_role.datasync_s3_role.arn
  }
}

resource "aws_datasync_task" "minio_to_s3" {
  name                     = "${var.project_prefix}-minio-to-s3"
  source_location_arn      = aws_datasync_location_object_storage.minio_source.arn
  destination_location_arn = aws_datasync_location_s3.bronze_target.arn

  schedule {
    schedule_expression = var.datasync_schedule_expression
  }

  options {
    verify_mode = "ONLY_FILES_TRANSFERRED"
  }
}
