output "bronze_bucket_name" {
  description = "Bucket S3 usado como Bronze única (Warehouse + Lakehouse + lookup do Kappa)"
  value       = aws_s3_bucket.bronze.bucket
}

output "fase0_ec2_private_ip" {
  description = "IP privado da EC2 rodando os sistemas self-hosted da Fase 0"
  value       = aws_instance.fase0.private_ip
}

output "kinesis_stream_arn" {
  description = "ARN do Kinesis Data Stream do trilho real-time (Kappa)"
  value       = aws_kinesis_stream.kappa.arn
}

output "redshift_workgroup_endpoint" {
  description = "Endpoint do Redshift Serverless workgroup"
  value       = aws_redshiftserverless_workgroup.fase2.endpoint
}

output "lambda_bridge_function_url" {
  description = "URL pública da Lambda ponte — configurar como destino Webhook na notificação de bucket do MinIO"
  value       = aws_lambda_function_url.bridge.function_url
}

output "datasync_agent_activation_console" {
  description = "IP do agente DataSync — acessar via HTTPS na porta 443 para obter a activation_key (passo manual)"
  value       = "https://${aws_instance.datasync_agent.private_ip}"
}
