# MinIO — notificação de bucket (Webhook) para a ponte Kinesis (Fase 2/AWS)

> Configuração da notificação de bucket nativa do MinIO usada no trilho real-time
> da Fase 2 (Etapa 3/Kappa) — ver Decisão 5 de `DESIGN_INGESTAO_AWS_FASE2.md`.
> Kinesis não fala protocolo Kafka, e o MinIO só publica em Kafka/AMQP/NATS/Webhook
> — por isso o mecanismo é Webhook + Lambda ponte, não integração direta.

## 1. Por que Webhook, não Kafka/AMQP/NATS

O Kinesis Data Streams usa API proprietária (`PutRecord`/KCL), incompatível com os
destinos nativos que o MinIO suporta para notificação de bucket. O destino
**Webhook** é o único que permite plugar uma Lambda (via Function URL) sem subir
um broker Kafka-compatível (MSK, descartado por não ser serverless — ver
`BRAINSTORM_INGESTAO_AWS_FASE2.md`).

## 2. Configuração do lado do MinIO

```bash
mc admin config set myminio notify_webhook:kinesis_bridge \
  endpoint="${LAMBDA_BRIDGE_FUNCTION_URL}" \
  auth_token="${MINIO_WEBHOOK_AUTH_TOKEN}"

mc admin service restart myminio

mc event add myminio/ubereats-minio-bucket arn:minio:sqs::kinesis_bridge:webhook \
  --event put
```

- `LAMBDA_BRIDGE_FUNCTION_URL` — saída `lambda_bridge_function_url` do Terraform
  (`infra/aws/fase2-ingestao/outputs.tf`).
- `MINIO_WEBHOOK_AUTH_TOKEN` — mesmo valor da variável Terraform
  `minio_webhook_auth_token`; o MinIO envia esse valor no header `Authorization`
  de toda chamada webhook, e a Lambda ponte valida esse header antes de processar
  qualquer evento (`src/aws/lambda_minio_kinesis_bridge/handler.py`).

## 3. Formato do payload recebido pela Lambda

O MinIO envia um payload compatível com o formato de S3 Event Notification
(`Records[].s3.bucket.name`, `Records[].s3.object.key`, `Records[].eventName`).
A Lambda ponte (`handler.py`) espera exatamente esse formato — se uma versão
futura do MinIO mudar o payload, ajustar `_build_payload()` no mesmo arquivo.

🔶 **Não confirmado com teste real** — o formato exato do payload deve ser validado
contra uma instância MinIO real no início do `/build` real desta feature (mesmo
tipo de spike técnico já feito para o Oracle/LogMiner na Onda 3).

## 4. Function URL pública, autenticação na aplicação

A Function URL da Lambda ponte é pública (`authorization_type = "NONE"`) porque o
MinIO não assina requisições com SigV4 (não há suporte nativo a IAM auth no
destino webhook). A segurança fica na validação do `Authorization` header dentro
do handler — nunca aceitar um payload sem esse header correspondendo ao token
configurado.

## 5. Agente DataSync (trilho batch, Etapa 1) — ativação manual

O DataSync exige um agente rodando na rede que enxerga o MinIO (location type
"Self-managed object storage"). Depois que a EC2 do agente (`aws_instance.datasync_agent`)
subir:

1. Acessar `https://<IP privado do agente>` de dentro da VPC (ex. via bastion/SSM).
2. Copiar a chave de ativação exibida no console local do agente.
3. Preencher `datasync_agent_activation_key` no `.tfvars` e rodar `terraform apply` novamente.

Esse passo não pode ser automatizado só com Terraform — é uma limitação conhecida
do DataSync, não um gap deste design.
