# Lambda consumidora do Kappa — item 19 do manifesto. Event source mapping com o
# Kinesis (invocação automática por lote), sem Function URL nem trigger HTTP.

data "archive_file" "lambda_consumer" {
  type        = "zip"
  source_dir  = "${path.module}/../../../src/aws/lambda_kappa_consumer"
  output_path = "${path.module}/.build/lambda_kappa_consumer.zip"
}

resource "aws_lambda_function" "consumer" {
  function_name    = "${var.project_prefix}-kappa-consumer"
  role             = aws_iam_role.lambda_consumer.arn
  handler          = "handler.handler"
  runtime          = "python3.12"
  filename         = data.archive_file.lambda_consumer.output_path
  source_code_hash = data.archive_file.lambda_consumer.output_base64sha256
  timeout          = 60
  memory_size      = 256 # cache do MongoDB em memória (Decisão 4) — folga acima do mínimo

  environment {
    variables = {
      BRONZE_BUCKET = aws_s3_bucket.bronze.bucket
    }
  }
}

resource "aws_lambda_event_source_mapping" "consumer_kinesis" {
  event_source_arn  = aws_kinesis_stream.kappa.arn
  function_name     = aws_lambda_function.consumer.arn
  starting_position = "LATEST"
  batch_size        = 100
}
