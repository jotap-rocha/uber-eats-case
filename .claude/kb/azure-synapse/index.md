---
domain: azure-synapse
description: Azure Synapse Dedicated SQL Pool (DW100c) como warehouse — COPY INTO do ADLS Gen2 por Managed Identity, MERGE para SCD2 (limites do dialeto), distribuição HASH, custo e pausa/retomada via CLI; por que não Serverless nem Fabric
mcp_validated: "2026-10-16"
confidence: 0.85
---

# KB: Azure Synapse (Dedicated SQL Pool)

Warehouse relacional MPP do Synapse Analytics workspace: dados em tabelas distribuídas
(60 distribuições), compute medido em **DWU** (`DW100c` = menor nível), pausável.

## Papel

`role: warehouse` — camada **gold/curated** consultável por SQL: carga em massa a partir
do `object-storage` (ADLS Gen2) com `COPY INTO`, dimensões históricas com MERGE/SCD2,
fatos para BI. O compute pode (e deve) ser pausado fora da janela de uso.

## Capability map

| Pergunta | Onde achar |
|---|---|
| Distribuição, índices, DWU, workspace vs "formerly SQL DW" | [concepts/dedicated-pool.md](concepts/dedicated-pool.md) |
| Quanto custa, como pausar/retomar, o que o Terraform não faz | [concepts/cost-and-pause.md](concepts/cost-and-pause.md) |
| Carregar Parquet/CSV do ADLS | [patterns/bulk-load.md](patterns/bulk-load.md) |
| SCD2 com MERGE (e o que o MERGE do Synapse não suporta) | [patterns/merge-scd2.md](patterns/merge-scd2.md) |
| Cheatsheet | [quick-reference.md](quick-reference.md) |

## Custo e free tier

- **Não há free tier** para Dedicated SQL Pool. Em conta nova, consome os **US$ 200 /
  30 dias** de crédito de avaliação.
- **Compute** (DWU) é cobrado **por hora enquanto Online**; pausado = compute zero.
  **Storage** é cobrado sempre (pausado ou não) até o pool ser **excluído**.
- `DW100c` ligado custa na ordem de **US$ 1–1,5/hora** (≈ US$ 900+/mês se esquecido)
  — conferir na calculadora para a região (**a validar**). Esquecer o pool ligado num fim
  de semana queima boa parte do crédito.
- Pausar/retomar: `az synapse sql pool pause|resume` (ver quick-reference). O provider
  Terraform **não tem** atributo de pausa — pausa é operação, não estado declarado.
- Workspace Synapse em si (sem pool) e o Serverless SQL têm custos próprios
  (Serverless = por TB processado); não usar o Serverless por engano em query pesada.
- Regra: **criar → carregar → testar → pausar no mesmo dia**; ao terminar o estudo,
  `terraform destroy` (pausado ainda paga storage).
- **Risco a validar:** assinatura de avaliação pode ter cota baixa de DWU por região —
  checar antes de planejar (`az synapse sql pool create` falha com erro de cota).

## SI

- Admin SQL (`sql_administrator_login`) só para bootstrap; senha via Key Vault/variável
  sensível do Terraform, nunca em `.tfvars` versionado. Preferir **Entra ID admin**.
- Carga lê o ADLS com **Managed Identity do workspace** (`Storage Blob Data
  Contributor`/`Reader` na conta/container) — sem SAS nem storage key no SQL.
- Usuário de carga: `INSERT` + `ADMINISTER DATABASE BULK OPERATIONS`; consumidores BI:
  `SELECT` no schema gold.
- PII: mascarar na exibição (Dynamic Data Masking ou view); nunca PII em logs de carga.
- Placeholders only: `<SUBSCRIPTION_ID>`, `<STORAGE_ACCOUNT>`, `<WORKSPACE>`.

## Por que este serviço

| Alternativa (Azure) | Por que não (aqui) |
|---|---|
| **Serverless SQL pool** | Sem tabelas físicas gerenciadas: lê arquivos (OPENROWSET/external tables/CETAS) e **não faz MERGE/UPDATE** em tabela própria → não serve para SCD2. Cobra por TB lido, imprevisível em query exploratória |
| **Microsoft Fabric Warehouse** | Outro produto, modelo de **capacidade** (F SKU) e trial próprio; fora do escopo do briefing. A Microsoft recomenda Fabric para workloads **novos** — registrar como decisão (ADR) se o projeto for além de estudo |
| Azure SQL Database | OLTP, não MPP; sem COPY INTO do lake no mesmo modelo |
| Databricks SQL | Coberto pela KB `databricks`; papel de lakehouse, não este |

## Learning path

1. `concepts/dedicated-pool.md` — distribuição e índices (decide performance do MERGE)
2. `concepts/cost-and-pause.md` — antes de criar qualquer pool
3. `patterns/bulk-load.md` — staging via COPY INTO
4. `patterns/merge-scd2.md` — dimensão histórica

## Quick Reference

Ver [quick-reference.md](quick-reference.md).
