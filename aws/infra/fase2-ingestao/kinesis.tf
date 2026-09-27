# Kinesis Data Stream — Etapa 3 (Kappa), item 12 do manifesto. Modo on-demand
# (serverless) — único target do trilho real-time (Decisão do brainstorm: MSK
# descartado por não ser serverless).

resource "aws_kinesis_stream" "kappa" {
  name = var.kinesis_stream_name

  stream_mode_details {
    stream_mode = "ON_DEMAND"
  }
}
