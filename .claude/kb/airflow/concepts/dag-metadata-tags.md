# Metadados de DAG — tags obrigatórias (área, stack, frequência)

> **Propósito:** Convenção de **`tags`** no parâmetro `tags=` do `@dag` / `DAG()` para classificação na UI, filtros e auditoria (“autos”).  
> **Airflow:** 2.11.x — valores são `list[str]`; usar **snake_case** e vocabulário acordado com o time (área e frequência em **português** quando aplicável).  
> **MCP Validated:** 2026-05-11

---

## Regra geral

Cada DAG nova (ou redesenhada) deve declarar **exactamente três** tags, **nesta ordem**:

| Ordem | Dimensão | Exemplos | Notas |
|-------|-----------|----------|--------|
| 1 | **Área** (negócio / programa) | `data_driven` | Programa ou área dona do fluxo |
| 2 | **Stack** tecnológica principal | `python`, `spark`, `dbt` | Tecnologia dominante do job invocado pela DAG |
| 3 | **Frequência** (classificação de negócio) | `horario`, `diaria`, `mensal` | Ver tabela abaixo — **não** confundir `horario` com “cron de 1 em 1 hora” |

- **Snake_case:** minúsculas; palavras em português sem acento gráfico nos identificadores (ex.: `horario`, `diaria`).  
- **Coerência com `schedule`:** a tag de frequência descreve a **categoria** acordada; o `schedule` real (cron, `timedelta`, etc.) pode ser mais fino (ex.: DAG com tag `horario` e cron **a cada 3 horas**). Documentar excepções em `doc_md` quando útil.

### Frequência — vocabulário (`tags[2]`)

| Tag | Significado |
|-----|-------------|
| `horario` | **Mais de uma execução no mesmo dia** (várias janelas diárias), **sem** impor intervalo de 60 minutos — inclui, por exemplo, execução a cada 2 h ou 3 h. |
| `diaria` | Uma execução por dia (conceito de “dia útil” ou calendário conforme acordo). |
| `mensal` | Uma execução por mês. |

### Stack — vocabulário (`tags[1]`)

| Tag | Uso |
|-----|-----|
| `python` | Job Python (venv, `python -m`, script) |
| `spark` | Spark submit / PySpark |
| `dbt` | `dbt run` / artefactos dbt |

### Área — exemplo (`tags[0]`)

| Tag | Uso |
|-----|-----|
| `data_driven` | Iniciativas do programa Data Driven |

Novas áreas: definir slug único em snake_case e alinhar com naming do time.

---

## Exemplo (Sentinela)

```python
@dag(
    dag_id="sentinela",
    schedule="0 */3 * * *",  # a cada 3 h; tag horario = várias vezes no dia
    tags=["data_driven", "python", "horario"],
    ...
)
def sentinela_monitoring_dag():
    ...
```

---

## Relacionado

- [../quick-reference.md](../quick-reference.md) — secção *Tags de classificação*  
- [../index.md](../index.md) — índice KB  
- Agente `.claude/agents/data-engineering/airflow-dag-builder.md` — contrato obrigatório  
- [../patterns/retries-callbacks-alertas.md](../patterns/retries-callbacks-alertas.md) — callbacks de falha (ex.: Teams)
