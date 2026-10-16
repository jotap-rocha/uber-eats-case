# Bucket S3 (Bronze) — item 6 do manifesto. Landing único compartilhado por
# Warehouse (Redshift COPY/MERGE), Lakehouse (Glue+Iceberg+Athena) e pelo lookup
# do consumidor do Kappa contra o MongoDB (Decisão 2 e Decisão 4 do DESIGN).

resource "aws_s3_bucket" "bronze" {
  bucket = var.bronze_bucket_name

  tags = {
    Name = "${var.project_prefix}-bronze"
  }
}

resource "aws_s3_bucket_versioning" "bronze" {
  bucket = aws_s3_bucket.bronze.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_public_access_block" "bronze" {
  bucket = aws_s3_bucket.bronze.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "bronze" {
  bucket = aws_s3_bucket.bronze.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Prefixos por fonte, espelhando as pastas usadas nos DMS/DataSync targets
# (postgres/, oracle/, mongodb/, minio/) — documentado em
# docs/data-contract-cdc-aws-dms.md.
