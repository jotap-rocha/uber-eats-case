# IAM — item 3 do manifesto. Least privilege por componente: DMS (S3 target),
# DataSync (S3 destino), Lambdas (Kinesis PutRecord / leitura S3 e Kinesis event source).

data "aws_caller_identity" "current" {}

# ---------------------------------------------------------------------------
# DMS -> S3 (Etapas 1 e 3 — mesma role serve os dois targets S3/Kinesis batch e
# real-time, já que ambos escrevem no mesmo bucket Bronze ou no mesmo stream)
# ---------------------------------------------------------------------------

resource "aws_iam_role" "dms_s3_target" {
  name = "${var.project_prefix}-dms-s3-target-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "dms.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "dms_s3_target" {
  name = "${var.project_prefix}-dms-s3-target-policy"
  role = aws_iam_role.dms_s3_target.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket",
      ]
      Resource = [
        aws_s3_bucket.bronze.arn,
        "${aws_s3_bucket.bronze.arn}/*",
      ]
    }]
  })
}

resource "aws_iam_role" "dms_kinesis_target" {
  name = "${var.project_prefix}-dms-kinesis-target-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "dms.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "dms_kinesis_target" {
  name = "${var.project_prefix}-dms-kinesis-target-policy"
  role = aws_iam_role.dms_kinesis_target.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "kinesis:PutRecord",
        "kinesis:PutRecords",
        "kinesis:DescribeStream",
      ]
      Resource = aws_kinesis_stream.kappa.arn
    }]
  })
}

# ---------------------------------------------------------------------------
# DataSync -> S3
# ---------------------------------------------------------------------------

resource "aws_iam_role" "datasync_s3_role" {
  name = "${var.project_prefix}-datasync-s3-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "datasync.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "datasync_s3_role" {
  name = "${var.project_prefix}-datasync-s3-policy"
  role = aws_iam_role.datasync_s3_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket",
        "s3:GetBucketLocation",
      ]
      Resource = [
        aws_s3_bucket.bronze.arn,
        "${aws_s3_bucket.bronze.arn}/*",
      ]
    }]
  })
}

# ---------------------------------------------------------------------------
# Lambda ponte MinIO -> Kinesis (item 15) — só precisa gravar no stream
# ---------------------------------------------------------------------------

resource "aws_iam_role" "lambda_bridge" {
  name = "${var.project_prefix}-lambda-bridge-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_bridge_basic_logs" {
  role       = aws_iam_role.lambda_bridge.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy" "lambda_bridge_kinesis" {
  name = "${var.project_prefix}-lambda-bridge-kinesis-policy"
  role = aws_iam_role.lambda_bridge.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["kinesis:PutRecord", "kinesis:PutRecords"]
      Resource = aws_kinesis_stream.kappa.arn
    }]
  })
}

# ---------------------------------------------------------------------------
# Lambda consumidor do Kappa (item 19) — lê do Kinesis (event source mapping,
# permissões concedidas via policy attachment gerenciada) e do S3 (lookup MongoDB)
# ---------------------------------------------------------------------------

resource "aws_iam_role" "lambda_consumer" {
  name = "${var.project_prefix}-lambda-consumer-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_consumer_basic_logs" {
  role       = aws_iam_role.lambda_consumer.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy" "lambda_consumer_kinesis_read" {
  name = "${var.project_prefix}-lambda-consumer-kinesis-policy"
  role = aws_iam_role.lambda_consumer.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "kinesis:GetRecords",
        "kinesis:GetShardIterator",
        "kinesis:DescribeStream",
        "kinesis:ListShards",
      ]
      Resource = aws_kinesis_stream.kappa.arn
    }]
  })
}

resource "aws_iam_role_policy" "lambda_consumer_s3_read" {
  name = "${var.project_prefix}-lambda-consumer-s3-policy"
  role = aws_iam_role.lambda_consumer.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "s3:GetObject",
        "s3:ListBucket",
      ]
      Resource = [
        aws_s3_bucket.bronze.arn,
        "${aws_s3_bucket.bronze.arn}/*",
      ]
    }]
  })
}

# ---------------------------------------------------------------------------
# Redshift Serverless -> S3 (COPY/MERGE)
# ---------------------------------------------------------------------------

resource "aws_iam_role" "redshift_s3_read" {
  name = "${var.project_prefix}-redshift-s3-read-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "redshift.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "redshift_s3_read" {
  name = "${var.project_prefix}-redshift-s3-read-policy"
  role = aws_iam_role.redshift_s3_read.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "s3:GetObject",
        "s3:ListBucket",
      ]
      Resource = [
        aws_s3_bucket.bronze.arn,
        "${aws_s3_bucket.bronze.arn}/*",
      ]
    }]
  })
}

# ---------------------------------------------------------------------------
# Glue Catalog / crawler -> S3
# ---------------------------------------------------------------------------

resource "aws_iam_role" "glue_crawler" {
  name = "${var.project_prefix}-glue-crawler-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "glue.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "glue_crawler_service" {
  role       = aws_iam_role.glue_crawler.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}

resource "aws_iam_role_policy" "glue_crawler_s3_read" {
  name = "${var.project_prefix}-glue-crawler-s3-policy"
  role = aws_iam_role.glue_crawler.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "s3:GetObject",
        "s3:ListBucket",
      ]
      Resource = [
        aws_s3_bucket.bronze.arn,
        "${aws_s3_bucket.bronze.arn}/*",
      ]
    }]
  })
}
