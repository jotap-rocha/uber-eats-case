# Padrão: falha de pipeline Databricks — sem retry + alerta Teams detalhado

> **Confiança:** 0.95  
> **Relacionado:** [teams-notifications/patterns/falha-de-pipeline.md](../../teams-notifications/patterns/falha-de-pipeline.md), [teams-notifications/patterns/databricks-ambientes-e-smoke-test.md](../../teams-notifications/patterns/databricks-ambientes-e-smoke-test.md), [concepts/jobs-workflows-triggers-notifications.md](../concepts/jobs-workflows-triggers-notifications.md)

## Política obrigatória (Icatu / pipelines operacionais)

| Regra | Motivo |
|-------|--------|
| **Não configurar retry** automático no Job, task ou biblioteca (tenacity, loops manuais) para falha de pipeline | Retry mascara erro estrutural, duplica escrita parcial e atrasa análise |
| **Falhar imediatamente** após exceção não recuperável | Analista corrige na origem (código, dados, permissão) |
| **Notificar Teams** antes de `raise` (ou no `except` único) | Canal operacional com contexto para achar etapa e tabela |
| **Reexecutar só manualmente** após correção | Nova run limpa (`repair` pontual só se política de plataforma exigir) |

**Exceções** (documentar no PR se aplicar): APIs externas transitórias com idempotência comprovada — não usar para transformação medallion nem MERGE em Delta.

---

## Configuração Job / DAB (sem retry)

```yaml
# databricks.yml — job e cada task
resources:
  jobs:
    meu_pipeline_medallion:
      max_retries: 0
      retry_on_timeout: false
      tasks:
        - task_key: bronze_ingest
          max_retries: 0
          retry_on_timeout: false
          notebook_task:
            notebook_path: ./notebooks/bronze_ingest
        - task_key: silver_transform
          depends_on: [{ task_key: bronze_ingest }]
          max_retries: 0
          notebook_task:
            notebook_path: ./notebooks/silver_transform
```

API REST equivalente: omitir `max_retries` ou definir `0`; não usar `repair` automático em CI.

---

## Notificação Teams — campos obrigatórios

A mensagem deve permitir ao analista localizar o problema **sem abrir o workspace primeiro**:

| Campo | Exemplo | Origem sugerida |
|-------|---------|-----------------|
| Pipeline / job | `orders_medallion_prd` | Nome fixo no código ou `dbutils.widgets` |
| **Camada (medallion)** | `bronze`, `silver`, `gold` | Passo DLT ou fase do job |
| **Processo** | `ingestao_cloudfiles_raw` | Nome lógico da etapa no código |
| Etapa / task | `silver_transform` | `task_key`, função DLT |
| Tabela alvo | `catalog.silver.orders` | FQCN Unity Catalog |
| **Função / ficheiro** | `bronze_ingest.py:128` · `read_raw()` | Traceback filtrado ao pacote do projeto |
| Ambiente | `prd` / `dsv` | Widget, tag do bundle, `var.env` |
| Run ID | `123456789` | `dbutils.notebook.entry_point.getDbutils().notebook().getContext().currentRunId().get()` |
| Tipo e mensagem do erro | `AnalysisException: ...` | `type(e).__name__`, `str(e)` |
| Traceback | últimos ~3500 chars | `traceback.format_exc()` |

Webhook operacional: **`URL_WEBHOOK_SENTINEL`** (ver KB `teams-notifications`).

---

## Código de referência (notebook / wheel)

```python
from __future__ import annotations

import os
import traceback
from dataclasses import dataclass

import pymsteams


@dataclass(frozen=True)
class PipelineFailureContext:
    pipeline_name: str
    stage: str
    table: str
    environment: str = "prd"
    job_name: str | None = None
    task_key: str | None = None
    run_id: str | None = None
    extra: str | None = None


def _current_run_id() -> str | None:
    try:
        from pyspark.dbutils import DBUtils

        ctx = DBUtils().notebook.entry_point.getDbutils().notebook().getContext()
        return str(ctx.currentRunId().get())
    except Exception:
        return None


def notify_teams_pipeline_failure(
    ctx: PipelineFailureContext,
    error: BaseException,
    *,
    webhook_env_key: str = "URL_WEBHOOK_SENTINEL",
    verify_ssl: bool = True,
) -> None:
    url = os.environ[webhook_env_key].strip()
    card = pymsteams.connectorcard(url, verify=verify_ssl)
    card.title(f"Falha pipeline Databricks — {ctx.pipeline_name}")
    card.color("A32120")

    lines = [
        f"**Ambiente:** `{ctx.environment}`",
        f"**Etapa / task:** `{ctx.stage}`" + (f" (`{ctx.task_key}`)" if ctx.task_key else ""),
        f"**Tabela:** `{ctx.table}`",
    ]
    if ctx.job_name:
        lines.append(f"**Job:** `{ctx.job_name}`")
    rid = ctx.run_id or _current_run_id()
    if rid:
        lines.append(f"**Run ID:** `{rid}`")
    lines.append(f"**Erro:** `{type(error).__name__}` — {error!s}")
    if ctx.extra:
        lines.append(f"**Contexto adicional:**\n{ctx.extra}")

    tb = traceback.format_exc()
    if tb and tb.strip() != "NoneType: None\n":
        lines.append(f"**Traceback (trecho):**\n```\n{tb[-3500:]}\n```")

    card.text("\n\n".join(lines))
    card.send()


def run_stage(stage_name: str, table: str, fn, *, pipeline_name: str, environment: str = "prd"):
    """Wrapper: notifica Teams e re-lança — sem retry."""
    try:
        return fn()
    except Exception as e:
        notify_teams_pipeline_failure(
            PipelineFailureContext(
                pipeline_name=pipeline_name,
                stage=stage_name,
                table=table,
                environment=environment,
                run_id=_current_run_id(),
            ),
            e,
        )
        raise
```

Uso:

```python
run_stage(
    "silver_transform",
    "analytics.silver.orders",
    lambda: silver_transform(spark),
    pipeline_name="orders_medallion",
    environment="prd",
)
```

---

## DLT / Lakeflow

- Expectation `@dlt.expect_or_fail` pode parar o pipeline — tratar como falha definitiva e garantir hook Teams no notebook de orquestração ou job pai que dispara o pipeline.
- **Não** depender só de `email_notifications` do workspace — complementar com `notify_teams_pipeline_failure` no código.

---

## Checklist

```text
[ ] max_retries: 0 e retry_on_timeout: false no job e em cada task
[ ] Sem tenacity/loop de retry na transformação medallion
[ ] Teams inclui etapa, tabela, run_id e erro
[ ] Webhook via secret (URL_WEBHOOK_SENTINEL), nunca URL no código
[ ] Após correção, re-run manual (nova execução), não retry silencioso
```
