# Retries, callbacks e alertas proactivos

> **Ideia:** automação não é só disparar o job — é **absorver falhas transitórias** e **avisar humanos** quando algo não recupera sozinho.

## Retries na DAG e nas tasks

Definir ao nível da `@dag` (defaults) ou por `@task`:

```python
@dag(
    default_args={
        "retries": 3,
        "retry_delay": timedelta(minutes=5),
        "retry_exponential_backoff": True,
        "max_retry_delay": timedelta(minutes=60),
    },
    ...
)
def minha_dag():
    ...
```

**Quando faz sentido:** timeouts de rede, picos em SQL Server, Azure Storage, YARN momentaneamente cheio.  
**Quando não:** erro de dados (schema drift) — retries só atrasam o alarme; melhor falhar rápido + callback.

## Callbacks

| Hook | Uso |
|------|-----|
| `on_failure_callback` | Teams / Slack / e-mail na primeira falha **final** (após esgotar retries). |
| `on_retry_callback` | Opcional — métricas ou log estruturado em cada retry. |
| `sla_miss_callback` | Quando duração ou `sla` definido é violado. |

Função típica recebe `context` com `dag_run`, `task_instance`, excepção, etc. — enviar payload mínimo (DAG id, task id, logical date, link para Airflow UI).

### Padrão DATALAKE (`/DATALAKE/dags`)

Novas DAGs devem usar o callback centralizado **`utils.send.failure`** (MessageCard Microsoft Teams), definido em `dags/utils/send.py`:

```python
from utils.send import failure

@dag(
    default_args={
        "owner": "...",
        "on_failure_callback": failure,
        ...
    },
    ...
)
```

Alterações ao webhook ou ao formato da mensagem: editar **`send.py`**, não cada DAG individualmente. Ver agente **airflow-dag-builder** (contrato obrigatório).

## SLA

- Definir **`sla`** em tasks críticas para detetar **atraso** mesmo sem falha técnica.
- Combinar com **monitorização externa** (métricas do scheduler) em ambientes **LocalExecutor** com poucos workers.

## Boas práticas no cluster Data Lake

- Callbacks **idempotentes** (webhook pode ser chamado mais de uma vez em retries mal configurados).
- **Sem segredos** em código da DAG — usar Connections / Variables / vault conforme [**EDGE-314**](../migration-hub/data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md).

## Relacionado

- [pipeline-pre-check-load-post-check.md](pipeline-pre-check-load-post-check.md).  
- [quick-reference.md](../quick-reference.md).
