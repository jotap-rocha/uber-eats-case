---
domain: aws-msk
topic: serverless-vs-provisioned
---

# MSK Serverless × provisionado

## Os três sabores

| Tipo | O que é | Cobrança principal |
|---|---|---|
| **Serverless** | sem brokers visíveis; escala por partição | cluster-hora + partição-hora + GB in/out + storage |
| **Provisioned — Standard brokers** | brokers `kafka.t3/m5/m7g.*` + EBS | broker-hora + GB-mês de storage |
| **Provisioned — Express brokers** | brokers `express.m7g.*`, storage ilimitado gerenciado | broker-hora + storage/throughput (ver pricing) |

## Quando usar Serverless (default do harness)

- Lab, POC, cargas variáveis ou baixas (< 200 MBps in por cluster).
- Quer zero operação de broker, patch e dimensionamento.
- Aceita **IAM como único mecanismo de auth**.
- Poucos tópicos compactados (limite de **120 partições líderes compactadas**).

## Quando usar provisionado

| Necessidade | Por quê |
|---|---|
| SASL/SCRAM, mTLS ou ACLs Kafka | Serverless só aceita IAM |
| Configs de broker/tópico além das 7 editáveis | Serverless trava o resto (ex.: `segment.bytes`) |
| Throughput alto e constante | broker-hora fica mais barato que GB in/out |
| Mais de 120 partições compactadas, > 2400 partições | limites do Serverless |
| **MSK Data Delivery** (tópico → S3/S3 Tables sem Kafka Connect) | disponível só em **Express brokers** |
| Acesso público (internet) ao broker | opção do provisionado; Serverless é privado (PrivateLink) |

## Rede

- Serverless: até **5 VPCs clientes** por cluster; endpoint privado via PrivateLink.
- Clientes (Connect, Flink, EC2, Lambda) precisam estar nas subnets/VPC configuradas e o
  SG do cluster deve aceitar **9098** do SG deles.
- Laptop de dev: bastion EC2 (Session Manager, sem SSH aberto) ou VPN. **Não** há
  bootstrap público no Serverless.

## Paridade com Event Hubs (Azure)

| Event Hubs (Kafka endpoint) | MSK Serverless |
|---|---|
| Namespace Standard | Cluster Serverless |
| Event hub | Tópico |
| Porta 9093, SASL PLAIN + connection string | Porta **9098**, SASL **IAM** (sem segredo) |
| Throughput units | escala automática por partição |
| Compactação: só tiers Premium/Dedicated (a validar no `azure-event-hubs`) | `cleanup.policy=compact` na criação |
| Kafka Connect self-hosted | **MSK Connect** gerenciado ou self-managed |

## Versão do Kafka

Serverless não expõe versão de broker; clientes Kafka 2.x/3.x funcionam. MSK Connect
roda Kafka Connect **2.7.1 ou 3.7.x** (escolher 3.7.x em projeto novo).

## Custo comparado (ordem de grandeza, lab de 8 h)

| Cenário | Conta |
|---|---|
| Serverless, 6 partições, 1 GB in/out | 8 × 0,75 + 8 × 6 × 0,0015 + 0,10 + 0,05 ≈ **US$ 6,2** |
| + MSK Connect 1 worker × 1 MCU | + 8 × 0,11 ≈ **US$ 0,9** |
| Esquecido 7 dias (só cluster) | 168 × 0,75 ≈ **US$ 126** |

O custo dominante é o **tempo de vida do cluster**, não o volume. Daí a regra de
destroy no mesmo dia.
