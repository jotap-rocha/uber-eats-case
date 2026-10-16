# Contrato de dados — {{DATASET_NAME}}

> **Versão do contrato:** 1.0.0 — {{DATE}}  
> **Changelog:** [`CHANGELOG-data-contract-{{DATASET_SLUG}}.md`](CHANGELOG-data-contract-{{DATASET_SLUG}}.md)  
> **Dicionário normativo:** {{LINK_DICIONARIO_GOVERNANCA}}

---

## 1. Identificação

| Campo | Valor |
|-------|--------|
| **Domínio** | {{DOMINIO}} |
| **Dataset** | {{DATASET_NAME}} |
| **Owner dados** | {{OWNER_SI}} |
| **Owner engenharia** | {{OWNER_ENG}} |
| **Pipeline** | {{PIPELINE_NAME}} |
| **Frequência / SLA** | {{CRON_OU_SLA}} |

## 2. Tabelas Unity Catalog

| Camada | DSV | PRD |
|--------|-----|-----|
| Bronze | `{{CATALOG_DSV}}.bronze.{{TABLE_LEAF}}` | `{{CATALOG_PRD}}.bronze.{{TABLE_LEAF}}` |
| Bronze quarentena | `..._quarentena` | `..._quarentena` |
| Silver | `...silver.{{TABLE_LEAF}}` | `...` |
| Silver quarentena | `..._quarentena` | `...` |
| Gold | `...gold.{{TABLE_LEAF}}` | `...` |
| Métricas quarentena | `..._quarentena_metricas` | `...` |

## 3. Schema e cabeçalhos origem

| Header origem | Coluna UC | Tipo |
|---------------|-----------|------|
| {{HEADER_SI}} | {{coluna_snake}} | {{TIPO}} |

## 4. Política de evolução

### 4.1 Compatível (sem código)
- Novos ficheiros com **mesmos cabeçalhos**

### 4.2 Incompatível (processo obrigatório)
- Renomear/remover cabeçalho
- Nova coluna Silver/Gold
- Alterar tipo semântico

**Processo:** governança → código → CHANGELOG → deploy → reprocessamento

## 5. Schema drift

| Evento | Comportamento |
|--------|---------------|
| Coluna extra na origem | {{RESCUE_OU_FAIL}} → quarentena `schema_rescue` → Teams |
| Adoptar coluna | Runbook §5.6 — código + deploy + path novo landing |

Ver: [`guia-schema-drift-{{PROJETO}}.md`](guia-schema-drift-{{PROJETO}}.md)

## 6. Qualidade e quarentena

| Camada | Política |
|--------|----------|
| Bronze | `_corrupt_record` → quarentena `bronze_corrupt_record` |
| Bronze | `_rescued_data` → quarentena `schema_rescue` |
| Silver | Regras negócio → quarentena `silver_*` |

**Quarentena histórica:** trilha auditoria; não migra automaticamente.

## 7. Alertas Teams

| Evento | Canal |
|--------|-------|
| Falha DLT/job | Webhook DSV/PRD |
| Schema drift pós-run | Card laranja |
| Freshness Gold > N dias | Sentinela |

Webhooks: `URL_WEBHOOK_{{PROJETO}}_DSV`, `URL_WEBHOOK_{{PROJETO}}_PRD`

## 8. Idempotência e reprocessamento

| Aspeto | Política |
|--------|----------|
| SK | {{POLITICA_SK}} |
| Silver | {{APPEND_OU_MERGE}} |
| Gold | {{APPLY_CHANGES_OU_MERGE}} |
| Reprocessamento | Path **novo** na landing; job `max_retries: 0` |

## 9. Observabilidade

- Logs JSON: `run_id`, camada, outcome
- Sentinela: `max(_ingest_ts)` Gold vs {{N}} dias
- Dashboards: `docs/dashboards/`

---

## Histórico

| Versão | Data | Alteração |
|--------|------|-----------|
| 1.0.0 | {{DATE}} | Baseline |
