# Redshift Serverless — item 7 do manifesto. Lê só do S3/Bronze (COPY/MERGE),
# sem nenhum endpoint DMS apontando diretamente para ele (Decisão 2 do DESIGN).

resource "aws_redshiftserverless_namespace" "fase2" {
  namespace_name      = "${var.project_prefix}-namespace"
  admin_username       = var.redshift_admin_username
  admin_user_password  = var.redshift_admin_password
  db_name              = "ubereats"
  iam_roles            = [aws_iam_role.redshift_s3_read.arn]
}

resource "aws_redshiftserverless_workgroup" "fase2" {
  namespace_name = aws_redshiftserverless_namespace.fase2.namespace_name
  workgroup_name = "${var.project_prefix}-workgroup"

  base_capacity      = 8 # RPUs — menor unidade, escala sob demanda (princípio serverless/on-demand)
  publicly_accessible = false
  subnet_ids          = [aws_subnet.private.id]
  security_group_ids  = [aws_security_group.fase0_ec2.id]
}
