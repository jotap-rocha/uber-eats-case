# Lambda ponte MinIO -> Kinesis — item 15 do manifesto. Trigger via Function URL
# (sem API Gateway — mais simples e mais barato para um único endpoint de webhook).

data "archive_file" "lambda_bridge" {
  type        = "zip"
  source_dir  = "${path.module}/../../../src/aws/lambda_minio_kinesis_bridge"
  output_path = "${path.module}/.build/lambda_minio_kinesis_bridge.zip"
}

resource "aws_lambda_function" "bridge" {
  function_name    = "${var.project_prefix}-minio-kinesis-bridge"
  role             = aws_iam_role.lambda_bridge.arn
  handler          = "handler.handler"
  runtime          = "python3.12"
  filename         = data.archive_file.lambda_bridge.output_path
  source_code_hash = data.archive_file.lambda_bridge.output_base64sha256
  timeout          = 30

  environment {
    variables = {
      KINESIS_STREAM_NAME      = aws_kinesis_stream.kappa.name
      TEAMS_WEBHOOK_URL        = var.teams_webhook_url
      MINIO_WEBHOOK_AUTH_TOKEN = var.minio_webhook_auth_token
    }
  }
}

# MinIO não assina requisições com SigV4 — o destino "webhook" nativo dele só
# suporta um header Authorization estático (MINIO_NOTIFY_WEBHOOK_AUTH_TOKEN no
# lado do MinIO). Por isso a Function URL fica pública (NONE) e a validação do
# token acontece dentro do handler (ver src/aws/lambda_minio_kinesis_bridge/handler.py).
resource "aws_lambda_function_url" "bridge" {
  function_name      = aws_lambda_function.bridge.function_name
  authorization_type = "NONE"
}
