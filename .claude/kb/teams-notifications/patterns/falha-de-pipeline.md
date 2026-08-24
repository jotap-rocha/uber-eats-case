# Padrão: alerta de falha de pipeline

> **Confiança:** 0.95

## Quando usar

- Exceção não tratada em notebook ou job PySpark.
- Falha após validação de qualidade (ex.: expect DLT falhou e política exige notificar).
- Timeout ou erro de infraestrutura com contexto de `run_id`.

## Webhook recomendado

**`URL_WEBHOOK_SENTINEL`** para falhas operacionais genéricas. Trilha de Auditoria só quando o domínio for regras de auditoria.

## Código

```python
import os
import traceback

import pymsteams


def notify_teams_failure(
    *,
    pipeline_name: str,
    error: BaseException,
    webhook_env_key: str = "URL_WEBHOOK_SENTINEL",
    extra_context: str | None = None,
    verify_ssl: bool = True,
) -> None:
    url = os.environ[webhook_env_key].strip()
    card = pymsteams.connectorcard(url, verify=verify_ssl)
    card.title(f"Falha: {pipeline_name}")
    card.color("A32120")
    body = f"**Erro:** `{type(error).__name__}`\n\n```{str(error)}```"
    if extra_context:
        body += f"\n\n**Contexto:**\n{extra_context}"
    tb = traceback.format_exc()
    if tb and tb.strip() != "NoneType: None\n":
        body += f"\n\n**Traceback (últimos 3500 chars):**\n```{tb[-3500:]}```"
    card.text(body)
    card.send()


try:
    ...  # pipeline
except Exception as e:
    notify_teams_failure(
        pipeline_name="varonis_dlt_medallion",
        error=e,
        extra_context="target=prd",
    )
    raise
```

## Job Databricks sem Python

Se não houver hook no código, configurar no bundle:

```yaml
# databricks.yml (exemplo — ajustar destination id do workspace)
email_notifications:
  on_failure:
    - user@empresa.com
webhook_notifications:
  on_failure:
    - id: "<webhook_destination_id>"
```

Complementa — não substitui — alertas de regra de negócio com DataFrame.
