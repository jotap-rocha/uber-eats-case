---
domain: aws-managed-flink
description: Amazon Managed Service for Apache Flink como stream processing — aplicações Flink 1.20 (Java/PyFlink/Flink SQL) e Studio (Zeppelin, Flink 1.15), fontes MSK/Kinesis, reference data do S3 (join com tabela bounded, lookup join, temporal join, broadcast), custo por KPU-hora e stop da aplicação
mcp_validated: "2026-10-16"
confidence: 0.75
---

# KB: Amazon Managed Service for Apache Flink

Paridade com `azure-stream-analytics` (sintaxe SQL de stream, reference data input, path
pattern). Aqui a linguagem é **Flink SQL / Table API** — não existe "reference input"
nativo: reference data é uma **tabela** que se junta ao stream.

## Papel

`role: stream-processing` — processamento contínuo gerenciado: lê do `streaming` (MSK ou
Kinesis), enriquece com reference data do `object-storage` (S3), agrega em janelas e
grava no S3/MSK.

## Capability map

| Pergunta | Onde achar |
|---|---|
| Aplicação × Studio, KPU, paralelismo, ciclo de vida? | [concepts/application-model.md](concepts/application-model.md) |
| Fontes/sinks (MSK com IAM, Kinesis, S3) e janelas? | [concepts/sources-sinks-and-windows.md](concepts/sources-sinks-and-windows.md) |
| Reference data do S3 (equivalente ao reference input do ASA)? | [patterns/reference-data.md](patterns/reference-data.md) |
| Cheatsheet? | [quick-reference.md](quick-reference.md) |

## Custo e free tier

| Item (us-east-1, validado 2026-10-16) | Preço |
|---|---|
| **KPU-hora** (1 KPU = 1 vCPU + 4 GB) | **US$ 0,11**, cobrança por segundo |
| KPU de orquestração | **+1 KPU por aplicação** (sempre) |
| Running application storage | 50 GB por KPU, US$ 0,10/GB-mês |
| Studio notebook (modo interativo) | **+2 KPUs** (orquestração + ambiente) + 50 GB |
| Backups duráveis (snapshots) | por GB-mês (opcional) |

- **Free tier:** o serviço não tem uso gratuito; consome créditos da conta (modelo 2025
  — ver `aws-terraform`). **A validar** se Free plan permite criar a aplicação.
- **O que queima rápido:** aplicação em `RUNNING` cobra KPU-hora mesmo sem eventos.
  Mínimo realista: paralelismo 1 → 1 KPU + 1 orquestração = **2 KPU ≈ US$ 0,22/h ≈ US$ 5,3/dia**.
  Studio aberto: 1 + 2 = 3 KPU ≈ US$ 0,33/h. Autoscaling ligado pode multiplicar.
- **Pausar:** `aws kinesisanalyticsv2 stop-application` → sai de `RUNNING`, para de cobrar
  KPU (**a validar** se storage/backups continuam cobrando no estado `READY`). Studio:
  parar o notebook.
- **Limitar:** `parallelism = 1`, `parallelism_per_kpu = 1`, `auto_scaling_enabled = false` em lab.
- **Destruir:** `terraform destroy` da aplicação (snapshots são apagados com ela —
  confirme se precisa guardar).
- **Regra:** criar → testar → stop/destroy no mesmo dia; **AWS Budgets** ativo antes.

## SI

- **Service execution role** da aplicação (trust `kinesisanalytics.amazonaws.com`) dá
  acesso a MSK (IAM, `kafka-cluster:*` mínimo), Kinesis, S3 (`reference/*` leitura,
  sink escrita) e CloudWatch Logs. Sem access key em properties.
- Segredos (ex.: senha JDBC de lookup) via **Secrets Manager** lido na inicialização —
  nunca em `environment_properties` (aparecem no console/API em claro).
- Aplicação em VPC (subnets privadas) quando lê MSK; SG com saída para 9098.
- Não logar payload com PII nos operadores; CloudWatch Logs em nível `INFO`/`WARN`.

## Por que este serviço

| Alternativa (AWS) | Por que não aqui |
|---|---|
| Kinesis Data Analytics **for SQL** (legado, tinha "reference data source" do S3) | Descontinuado (fim anunciado para jan/2026 — a validar data); migrar para Flink |
| AWS Glue Streaming (Spark Structured Streaming) | Micro-batch, cobra DPU-hora com mínimo maior; bom se o time é Spark-first |
| EMR / EKS com Flink self-managed | Operação de cluster, checkpoints e upgrades por conta do time |
| Lambda consumindo MSK/Kinesis | Sem estado/janelas robustas; ok só para transformação stateless simples |

## Learning path

1. `concepts/application-model.md`
2. `concepts/sources-sinks-and-windows.md`
3. `patterns/reference-data.md`

## Fontes validadas (2026-10-16)

- aws.amazon.com/managed-service-apache-flink/pricing (KPU, orquestração, Studio)
- docs.aws.amazon.com/managed-flink/latest/java/flink-1-20.html (1.20.5; Studio só 1.15)
- docs.aws.amazon.com/managed-flink/latest/java/how-it-works.html
- Semântica de joins: documentação Apache Flink 1.20 (lookup/temporal/regular join) — conhecimento, não re-consultado
