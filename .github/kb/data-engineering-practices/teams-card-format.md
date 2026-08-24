# Pattern — Cards Microsoft Teams (formato conciso)

> **Quando usar:** todos os alertas Teams operacionais em pipelines Databricks.

## Princípio — dois tiers

| Tier | Cards | Regra |
|------|-------|-------|
| **A — Operacional** | conclusão, schema drift, sentinela, smoke | Resumo no topo · métricas · 3 passos · sem texto meta |
| **B — Debug** | falha DLT | Resumo acionável (Tier A) + separador `---` + stack/traceback |

**Anti-patterns:** listar contrato completo, secção "Como interpretar", duplicar drift no card verde, repetir metadados (`Pipeline`, `Ambiente`) em cada linha.

---

## Tier A — Cards operacionais

### Conclusão ingestão (verde / vermelho)

**Função:** `build_ingest_completion_message()`  
**Título:** `Varonis ingestão — concluída com sucesso` | `Varonis ingestão — falhou (STATUS)`

```text
✅ Ingestão concluída

`dsv` · `varonis` · job bronze_ingest_varonis · DLT SUCCESS

⚠️ Schema drift detectado — detalhes no card laranja enviado nesta execução.
```

### Schema drift (laranja)

**Função:** `build_schema_drift_message()`  
**Título:** `Varonis — schema drift (N col. · M quarentena)`

Ver secção detalhada: [teams-schema-drift-card-format.md](./teams-schema-drift-card-format.md).

### Sentinela Gold stale (laranja)

**Função:** `build_gold_stale_message()`  
**Título:** `Varonis Sentinela — Gold stale (8.5d · limite 3d)`

```text
⚠️ Gold stale — freshness abaixo do SLA

8.5 dias sem ingestão (limite 3) · `dsv` / `varonis`

Tabela: varonis.gold.tb_...
Último _ingest_ts: 2026-06-01 ...
Linhas Gold: 1.200

Próximo passo
1. Verificar job bronze_ingest_varonis (última execução SUCCESS?)
2. Confirmar export novo na landing RAW (SI)
3. Se job falhou → corrigir e reprocessar manualmente
```

### Smoke test (verde)

**Função:** `send_smoke_ping()` em `teams_smoke.py`  
**Título:** `Smoke test Varonis — Teams OK`

```text
✅ Smoke test OK — webhook Teams validado

`dsv` · `varonis` · env:URL_WEBHOOK_...
Timestamp: ...

Mensagem propositada — ignorar em produção.
```

---

## Tier B — Falha DLT (vermelho)

**Função:** `build_failure_message()`  
**Título:** `Varonis DLT — falha em bronze / ingestao_cloudfiles_raw`

**Topo (acionável — ~8 linhas):**

```text
❌ Falha DLT — pipeline interrompido

bronze / ingestao_cloudfiles_raw · varonis.bronze.tb_...
`dsv` · `varonis`

Erro: ValueError — mensagem resumida (1 linha)

Onde corrigir:
`bronze_arquivos_sensiveis` em `src/.../dlt_medallion_pipeline.py`
Origem: linha X em ...
```

**Detalhe (após `---`):** mensagem completa, stack `varonis_pipeline`, traceback final.

---

## Helpers partilhados

| Helper | Uso |
|--------|-----|
| `_format_columns_brief()` | Máx. 4 colunas + `(+N)` |
| `_format_int_pt()` | Milhares pt-BR (`28.811`) |
| `_truncate_one_line()` | Resumo de erro no card de falha |

---

## Implementação de referência

Repositório: `databricks-varonis-dataflow-prd` → `teams_notify.py`, `teams_smoke.py`

## Mandatos

| ID | Regra |
|----|-------|
| **TM-M05** | Card acionável (camada, tabela, run_id) |
| **TM-M06** | Formato conciso Tier A/B para **todos** os tipos de card Teams |
