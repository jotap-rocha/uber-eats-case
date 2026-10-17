---
domain: gcp-managed-kafka
description: Google Cloud Managed Service for Apache Kafka — cluster (mín. 3 vCPU, 1–8 GiB/vCPU), custo por vCPU/RAM-hora, auth SASL_SSL (OAUTHBEARER com ADC ou PLAIN com SA), porta 9092, tópicos compactados, Connect clusters gerenciados com sink GCS; sink HDFS = risco a validar
mcp_validated: "2026-10-16"
confidence: 0.7
---

# KB: Managed Service for Apache Kafka (streaming GCP)

Paridade com `azure-event-hubs` (endpoint Kafka, SASL_SSL, tópicos compactados, Kafka Connect).
Diferença: aqui é **Apache Kafka de verdade** (brokers gerenciados), não um endpoint compatível.

## Papel

`role: streaming` — broker de eventos gerenciado com protocolo Kafka nativo. Produtores/
consumidores Kafka padrão; Connect clusters gerenciados levam dados para GCS/BigQuery;
Dataflow (`gcp-dataflow`) consome direto.

## Capability map

| Pergunta | Onde achar |
|---|---|
| Tamanho mínimo, custo, rede (VPC/subnet)? | [concepts/cluster-sizing-cost.md](concepts/cluster-sizing-cost.md) |
| Mecanismos SASL, IAM, bootstrap 9092? | [concepts/auth-and-network.md](concepts/auth-and-network.md) |
| Tópicos compactados e Connect clusters? | [concepts/topics-and-connect.md](concepts/topics-and-connect.md) |
| `client.properties` OAUTHBEARER / PLAIN | [patterns/kafka-client-auth.md](patterns/kafka-client-auth.md) |
| Sink GCS (gerenciado) e sink HDFS (risco) | [patterns/kafka-connect-sink.md](patterns/kafka-connect-sink.md) |
| Cheatsheet | [quick-reference.md](quick-reference.md) |

## Learning path

1. `## Custo e free tier` abaixo — **antes** de criar o cluster
2. `concepts/cluster-sizing-cost.md` → `concepts/auth-and-network.md`
3. `patterns/kafka-client-auth.md` — produzir/consumir da VM/Cloud Shell na VPC
4. `concepts/topics-and-connect.md` → `patterns/kafka-connect-sink.md`

## Custo e free tier

- **Sem free tier.** O serviço não está no Always Free; só o crédito do **Free Trial
  (US$ 300 / 90 dias, conta nova)** cobre.
- **Cobrança:** compute em DCUs (≈ 0,6 DCU por vCPU + 0,1 DCU por GiB RAM; ~US$ 0,09/DCU-hora
  em `us-central1`) + storage (Persistent Disk dos brokers / armazenamento) + transferência
  entre zonas. Valores de **referência — a validar** em `cloud.google.com/managed-service-for-apache-kafka/pricing`.
- **Cluster mínimo** (3 vCPU, 3 GiB) ≈ 2,1 DCU ≈ **US$ 0,19/h ≈ US$ 140/mês** ligado —
  ordem de grandeza, **a validar**. Cobra 24/7 enquanto existir, com ou sem tráfego.
- **Connect cluster** é recurso separado e **também cobra por hora** (sem desconto de CUD).
  O tutorial oficial usa 12 vCPU / 12 GiB (≈ 8,4 DCU ≈ US$ 0,75/h — **a validar**); mínimo
  aceito **a validar**.
- **Não há pausa.** Para parar a cobrança: **deletar** connectors → Connect cluster → cluster.
  Scale-down existe, mas o piso é 3 vCPU.
- **Budgets:** budget com alertas (50/90/100%) antes de criar; budget não desliga nada.
- **Regra:** criar → testar → destruir **no mesmo dia**. Este é o recurso mais caro do kit.

```bash
gcloud managed-kafka connectors delete <CONNECTOR> --connect-cluster=<CONNECT_CLUSTER> --location=<REGION>
gcloud managed-kafka connect-clusters delete <CONNECT_CLUSTER> --location=<REGION>
gcloud managed-kafka clusters delete <CLUSTER> --location=<REGION>
```

## SI

- Clientes autenticam com **identidade Google** (ADC/SA anexada) via OAUTHBEARER —
  preferido. `roles/managedkafka.client` para o principal cliente.
- SASL PLAIN com chave de SA (base64) só em teste e **nunca** versionado: o password vem de
  env/Secret Manager. Preferir PLAIN com **access token** curto.
- TLS sempre (`SASL_SSL`); cluster acessível apenas via subnets da VPC (acesso público é opção
  separada com allowlist de IP — evitar).
- Connect cluster usa o service agent
  `service-<PROJECT_NUMBER>@gcp-sa-managedkafka.iam.gserviceaccount.com` — papel só no
  bucket de destino.
- Placeholders: `<GCP_PROJECT_ID>`, `<REGION>`, `<CLUSTER>`, `<SA_EMAIL>`, `<BUCKET>`.

## Por que este serviço

| Alternativa (GCP) | Por que não como padrão |
|---|---|
| **Pub/Sub** | Não é Kafka: sem protocolo/cliente Kafka, sem tópico compactado, sem Kafka Connect nativo. Mais barato e serverless (10 GiB/mês grátis) — escolha se o requisito **não** for Kafka |
| Kafka self-managed em GCE/GKE | Operação de brokers, upgrades, discos — custo humano; só para plugin não suportado (ex.: HDFS sink) |
| Confluent Cloud (Marketplace) | Kafka gerenciado de terceiro; billing/contrato separados, fora do escopo "nativo GCP" |
| Pub/Sub Lite | Descontinuado — não usar |

Escolhido porque o requisito é **endpoint Kafka + Kafka Connect** (paridade com Event Hubs
Kafka no Azure).
