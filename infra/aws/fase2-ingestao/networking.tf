# Rede da Fase 2 — item 1 do manifesto (DESIGN_INGESTAO_AWS_FASE2.md, Decisão 1).
# A EC2 da Fase 0, a replication instance do DMS e o agente do DataSync vivem todos
# na mesma subnet privada: nenhum sistema self-hosted é exposto à internet pública.

resource "aws_vpc" "fase2" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "${var.project_prefix}-vpc"
  }
}

resource "aws_internet_gateway" "fase2" {
  vpc_id = aws_vpc.fase2.id

  tags = {
    Name = "${var.project_prefix}-igw"
  }
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.fase2.id
  cidr_block        = var.private_subnet_cidr
  availability_zone = data.aws_availability_zones.available.names[0]

  tags = {
    Name = "${var.project_prefix}-private-subnet"
  }
}

# Subnet pública só para o NAT Gateway — a EC2 da Fase 0 e o agente DataSync ficam
# sempre na subnet privada, nunca recebem IP público.
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.fase2.id
  cidr_block              = cidrsubnet(var.vpc_cidr, 8, 255)
  availability_zone       = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = false

  tags = {
    Name = "${var.project_prefix}-public-subnet"
  }
}

data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_eip" "nat" {
  domain = "vpc"

  tags = {
    Name = "${var.project_prefix}-nat-eip"
  }
}

# NAT Gateway: única via de saída da subnet privada para a internet — necessária para
# a EC2 da Fase 0 baixar imagens Docker e para o agente DataSync se registrar no
# endpoint público do DataSync. Custo por hora (Constraint: revisar troca por VPC
# Interface Endpoints no /build se o custo pesar mais que o de uma NAT).
resource "aws_nat_gateway" "fase2" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.public.id

  tags = {
    Name = "${var.project_prefix}-nat"
  }

  depends_on = [aws_internet_gateway.fase2]
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.fase2.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.fase2.id
  }

  tags = {
    Name = "${var.project_prefix}-public-rt"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.fase2.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.fase2.id
  }

  tags = {
    Name = "${var.project_prefix}-private-rt"
  }
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

# Security group único para todos os sistemas self-hosted da Fase 0 (EC2) e para o
# agente do DataSync — regras de entrada restritas às portas dos serviços consumidos
# pelo DMS/DataSync, nunca 0.0.0.0/0.
resource "aws_security_group" "fase0_ec2" {
  name        = "${var.project_prefix}-fase0-ec2-sg"
  description = "Acesso aos sistemas self-hosted da Fase 0 (Postgres/Oracle/MongoDB/MinIO) somente de dentro da VPC"
  vpc_id      = aws_vpc.fase2.id

  ingress {
    description = "Postgres — replicação lógica (DMS)"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  ingress {
    description = "Oracle — LogMiner/listener (DMS)"
    from_port   = 1521
    to_port     = 1521
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  ingress {
    description = "MongoDB (DMS)"
    from_port   = 27017
    to_port     = 27017
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  ingress {
    description = "MinIO — API S3-compatível (agente DataSync)"
    from_port   = 9000
    to_port     = 9000
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  ingress {
    description = "SSH administrativo"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.admin_access_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_prefix}-fase0-ec2-sg"
  }
}

resource "aws_security_group" "datasync_agent" {
  name        = "${var.project_prefix}-datasync-agent-sg"
  description = "Agente DataSync — acesso de saída ao MinIO e ao endpoint do DataSync na AWS"
  vpc_id      = aws_vpc.fase2.id

  ingress {
    description = "Console local de ativação do agente (só na VPC)"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_prefix}-datasync-agent-sg"
  }
}
