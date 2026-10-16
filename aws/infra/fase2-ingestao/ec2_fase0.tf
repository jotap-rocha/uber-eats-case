# EC2 rodando os sistemas self-hosted da Fase 0 — item 2 do manifesto.
# Decisão 1 (DESIGN_INGESTAO_AWS_FASE2.md): mesmo docker-compose.yml da Fase 0,
# só muda o local de execução. Sem IP público — acesso só de dentro da VPC (DMS,
# DataSync) e via SSH restrito a admin_access_cidr para operação manual.

resource "aws_instance" "fase0" {
  ami                    = var.fase0_ec2_ami_id
  instance_type          = var.fase0_ec2_instance_type
  key_name               = var.fase0_ec2_key_name
  subnet_id              = aws_subnet.private.id
  vpc_security_group_ids = [aws_security_group.fase0_ec2.id]

  root_block_device {
    volume_size = 60 # Oracle (~2.25GB de imagem) + Postgres + MongoDB + MinIO + volumes de dados
    volume_type = "gp3"
  }

  # Clona o repositório e sobe o docker-compose.yml já existente da Fase 0 — nenhuma
  # mudança de configuração dos geradores, só o host onde os containers rodam.
  user_data = <<-EOF
    #!/bin/bash
    set -euo pipefail
    dnf install -y docker git
    systemctl enable --now docker
    curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
      -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    echo "Clonar o repositório do projeto e rodar 'docker-compose up -d' manualmente" \
      "ou via pipeline de deploy — ver docs/minio/webhook-notification-config.md" \
      > /home/ec2-user/README_FASE0.txt
  EOF

  tags = {
    Name = "${var.project_prefix}-fase0-sistemas-selfhosted"
  }
}
