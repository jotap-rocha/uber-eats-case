# Airflow — Referência rápida

> Airflow **2.11.x**. Detalhes: `index.md` e conceitos/patterns linkados.

## Tags de classificação (obrigatório — novas DAGs)

Três entradas em `tags=`, **nesta ordem**, em **snake_case** (português sem acento nos identificadores quando aplicável):

1. **Área** — ex.: `data_driven`  
2. **Stack** — ex.: `python`, `spark`, `dbt`  
3. **Frequência** — ex.: `horario` (várias vezes no mesmo dia; **não** implica cron de 1 em 1 h), `diaria`, `mensal`

Detalhe e exemplos: [concepts/dag-metadata-tags.md](concepts/dag-metadata-tags.md).

## TaskFlow vs clássico

| Preferir | Evitar |
|----------|--------|
| `@dag`, `@task`, grafo com `>>` / chamadas | `PythonOperator` gigante só com `callable=` repetido |
| Retorno explícito entre tasks (XCom) | Parsing manual de strings gigantes entre tasks |

## Idempotência

| Evitar | Usar |
|--------|------|
| `datetime.now()` na lógica de dados | `{{ ds }}`, `data_interval_start`, `logical_date` |
| `INSERT INTO` sem chave de dedupe | Overwrite de **partição** / merge idempotente |

## Pipeline (decisão equipa)

| Fase | Função |
|------|--------|
| **Pré-check** | Comparar fonte vs destino (diff esperado) |
| **Carga** | Origem → destino (Spark/SQL/etc.) |
| **Pós-check** | Confirmar sucesso + **nº de linhas** carregadas |

## Resiliência

| Parâmetro DAG/task | Uso típico |
|--------------------|------------|
| `retries` | 2–5 para falhas transitórias |
| `retry_delay` / `retry_exponential_backoff` | Rede, blob storage, SQL timeout |
| `on_failure_callback` | Teams / Slack / e-mail |

## Dynamic tasks

| Caso | API |
|------|-----|
| N tabelas / N paths | `.expand(param=lista)` ou `expand_kwargs` |

## Pitfalls

| Não | Sim |
|-----|-----|
| Mega-task E+T+L num só `@task` | Tasks pequenas + retries focados |
| 10 DAGs quase iguais | 1 DAG + `.expand()` |

## Documentação relacionada

| Tema | Path |
|------|------|
| Índice KB | [index.md](index.md) |
| Tags de classificação | [concepts/dag-metadata-tags.md](concepts/dag-metadata-tags.md) |
| Operação 314 | [migration-hub/data-stack/airflow/README.md](../migration-hub/data-stack/airflow/README.md) |
