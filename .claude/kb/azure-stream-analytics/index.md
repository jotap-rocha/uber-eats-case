---
domain: azure-stream-analytics
description: Azure Stream Analytics como stream processing gerenciado — query SQL (SAQL) com TIMESTAMP BY e janelas, reference data em Blob/ADLS com path pattern {date}/{time}, Managed Identity, custo por Streaming Unit (SU V2) e parar o job para não pagar
mcp_validated: "2026-10-16"
confidence: 0.8
---

# KB: Azure Stream Analytics (ASA)

Job gerenciado que roda uma query SQL contínua: **inputs** (stream: Event Hubs, IoT Hub,
Blob/ADLS; reference: Blob/ADLS, SQL Database) → **query** → **outputs** (ADLS, Synapse,
SQL, Event Hubs, Power BI…). Sem cluster: compute em **Streaming Units (SU)**.

## Papel

`role: stream-processing` — enriquecer, filtrar e agregar em janela os eventos do
`streaming` (Event Hubs) usando lookup em reference data do `object-storage`, gravando o
resultado no lake ou no warehouse.

## Capability map

| Pergunta | Onde achar |
|---|---|
| Sintaxe: `TIMESTAMP BY`, janelas, multi-step, `PARTITION BY` | [concepts/query-language.md](concepts/query-language.md) |
| SU V1 vs V2, memória, custo, start/stop | [concepts/streaming-units-cost.md](concepts/streaming-units-cost.md) |
| Reference data em ADLS com `{date}/{time}` | [patterns/reference-data.md](patterns/reference-data.md) |
| Cheatsheet | [quick-reference.md](quick-reference.md) |

## Custo e free tier

- **Sem free tier**; consome o crédito de avaliação (**US$ 200 / 30 dias**).
- Cobrança por **SU-hora enquanto o job está em execução (Running)**. Job criado e
  **parado não cobra SU** (confirmar na página de preço — **a validar** para o SKU
  StandardV2 na região). Ordem de grandeza: centavos a poucas dezenas de centavos de
  dólar por SU V2-hora — **a validar** na calculadora.
- O que queima crédito: job esquecido **Running** (cobra mesmo sem eventos), SUs acima
  do necessário, vários jobs de teste ligados.
- Menor configuração: **1/3 SU V2** (StandardV2) — suficiente para Event Hub de 2
  partições em lab.
- Parar: `az stream-analytics job stop -g <RG> -n <JOB>`. Terraform cria o job
  **parado**; iniciar é ação explícita (CLI ou `azurerm_stream_analytics_job_schedule`).
- Regra: **criar → start → testar → stop no mesmo dia**; fim do estudo →
  `terraform destroy`. Containers auto-criados (snapshot de reference SQL) somem no
  restart.

## SI

- Job com **Managed Identity** (`identity { type = "SystemAssigned" }`) e
  `authentication_mode = "Msi"` em inputs/outputs: sem storage key nem connection string
  no job.
- MI com `Storage Blob Data Reader` no container de reference e `Contributor` só no de
  saída; `Azure Event Hubs Data Receiver` no event hub de entrada.
- Consumer group **dedicado** ao job no event hub (não `$Default`).
- Query não deve projetar PII além do necessário (minimização); nada de PII em nome de
  arquivo de saída.
- Placeholders: `<STORAGE_ACCOUNT>`, `<NAMESPACE>`, `<JOB>`, `<RG>`.

## Por que este serviço

| Alternativa | Por que não (aqui) |
|---|---|
| Spark Structured Streaming (Databricks/Synapse Spark) | Mais flexível, mas cluster ligado custa mais e exige código; ASA resolve enrich + janela com SQL |
| Microsoft Fabric Real-Time Intelligence (Eventstream/KQL) | Outro produto e modelo de capacidade; fora do escopo |
| Azure Functions | Sem estado de janela/temporal join nativo |
| Flink (HDInsight on AKS / próprio) | Operar cluster; exagero para lab |

## Learning path

1. `concepts/query-language.md`
2. `concepts/streaming-units-cost.md` — antes do primeiro start
3. `patterns/reference-data.md`

## Quick Reference

Ver [quick-reference.md](quick-reference.md).
