---
domain: aws-msk
description: Amazon MSK como broker Kafka — MSK Serverless (IAM obrigatório, porta 9098, tópicos compactados com cleanup.policy só na criação) vs provisionado, auth SASL/IAM com aws-msk-iam-auth, MSK Connect / Kafka Connect self-managed, S3 Sink e HDFS Sink (risco a validar)
mcp_validated: "2026-10-16"
confidence: 0.8
---

# KB: Amazon MSK (Managed Streaming for Apache Kafka)

Paridade com `azure-event-hubs` (endpoint Kafka, SASL_SSL, tópicos compactados, Kafka
Connect). Aqui o broker **é** Kafka nativo — não um protocolo emulado.

## Papel

`role: streaming` — broker de eventos gerenciado com endpoint Kafka: produtores e
consumidores Kafka, tópicos compactados (estado/CDC) e Kafka Connect para descarregar no
`object-storage` (S3).

## Capability map

| Pergunta | Onde achar |
|---|---|
| Serverless ou provisionado (Standard/Express)? | [concepts/serverless-vs-provisioned.md](concepts/serverless-vs-provisioned.md) |
| Tópicos, configs permitidas, compactação, quotas? | [concepts/topics-and-quotas.md](concepts/topics-and-quotas.md) |
| Auth do cliente (SASL/IAM, 9098, policy)? | [patterns/kafka-client-auth.md](patterns/kafka-client-auth.md) |
| Kafka Connect → S3 (e HDFS)? | [patterns/kafka-connect-sink.md](patterns/kafka-connect-sink.md) |
| Cheatsheet? | [quick-reference.md](quick-reference.md) |

## Custo e free tier

| Item (MSK Serverless, US East, validado 2026-10-16) | Preço |
|---|---|
| **Cluster-hora** | **US$ 0,75** (≈ US$ 18/dia **só por existir**) |
| Partição-hora | US$ 0,0015 (100 partições ≈ US$ 3,60/dia) |
| Dados escritos | US$ 0,10 / GB |
| Dados lidos | US$ 0,05 / GB |
| Storage | US$ 0,10 / GB-mês |
| **MSK Connect** | **US$ 0,11 por MCU-hora** (1 MCU = 1 vCPU + 4 GB), por segundo |

- **Free tier:** MSK não tem uso gratuito; consome os créditos da conta nova (modelo
  2025: US$ 100 + até US$ 100; ver `aws-terraform`). **A validar** se a conta Free plan
  permite MSK sem upgrade para Paid plan.
- **O que queima rápido:** o cluster Serverless cobra cluster-hora **mesmo sem tráfego**
  e não tem pausa. Um cluster esquecido no fim de semana ≈ US$ 50+. Connector MSK Connect
  idem (MCU-hora contínuo).
- **Como limitar:** poucas partições (3 por tópico em lab), retenção curta
  (`retention.ms` 1–24 h), 1 worker / 1 MCU no connector.
- **Destruir:** `terraform destroy` do connector **antes** do cluster; depois o cluster.
- **Regra:** criar → testar → destruir no mesmo dia; **AWS Budgets** ativo antes.

## SI

- **MSK Serverless exige IAM access control** — não há SASL/SCRAM nem ACLs Kafka. Ótimo:
  nenhuma senha de broker para guardar.
- Clientes autenticam com a identidade AWS do runtime (instance profile, ECS task role,
  role do MSK Connect, role do Flink). Nunca access key em `client.properties`.
- Policy mínima por aplicação: `kafka-cluster:Connect` + `WriteData`/`ReadData` só nos
  tópicos/grupos dela (ARNs com `<REGION>`, `<AWS_ACCOUNT_ID>`, `<CLUSTER_NAME>/<CLUSTER_UUID>`).
- Cluster só em subnets privadas; acesso de laptop via bastion/VPN — nunca abrir SG para `0.0.0.0/0`.
- Payload com PII: não logar mensagens no consumer; mascarar antes de publicar se possível.

## Por que este serviço

| Alternativa (AWS) | Por que não aqui |
|---|---|
| MSK **provisionado** (Standard/Express) | Paga broker-hora (mín. 2–3 brokers) + storage; faz sentido com throughput alto e estável, SCRAM/mTLS, ou Data Delivery nativo (só Express). Para lab/baixo volume o Serverless é mais simples |
| **Kinesis Data Streams** | Não é Kafka (API própria); quebra paridade com Event Hubs-Kafka e com Kafka Connect |
| Kafka self-managed em EC2 | Operação de brokers/KRaft/patch por conta do time |
| Amazon Data Firehose | Ótimo sink para S3, mas não é broker Kafka; pode **complementar** como consumidor (a validar) |

## Learning path

1. `concepts/serverless-vs-provisioned.md`
2. `concepts/topics-and-quotas.md`
3. `patterns/kafka-client-auth.md` → `patterns/kafka-connect-sink.md`

## Fontes validadas (2026-10-16)

- docs.aws.amazon.com/msk/latest/developerguide/serverless.html · serverless-config.html · limits.html
- …/configure-clients-for-iam-access-control.html · msk-connect.html · msk-data-delivery.html
- aws.amazon.com/msk/pricing · Context7 `/hashicorp/terraform-provider-aws` v6.33
