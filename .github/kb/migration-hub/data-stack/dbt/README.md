# dbt — Spark on YARN (projeto + ambiente)

> **Revisão documental:** 2026-04-29

## Código do repositório

O **esqueleto** do projeto dbt (`datalake_dbt`) e templates de perfil estão em:

- **[`dbt/datalake_dbt/`](/DATALAKE/workspace/jp/platform/dbt/datalake_dbt/)** — modelos, `dbt_project.yml`
- **[`profiles.yml.template`](/DATALAKE/workspace/jp/platform/dbt/profiles/profiles.yml.template)** — copiar para `~/.dbt/profiles.yml`

---

## Resumo

O **dbt** é usado como camada de transformação (ELT) sobre **Apache Spark on YARN**.

## Versão alvo

- **dbt-core:** **1.9.3**
- **dbt-spark:** **1.9.3**

**Instalação:** pacotes Python. Sem PyPI: mirror interno ou *wheelhouse* em `/DATALAKE/downloads`.

## Estratégia de execução

Com `spark.master yarn` e `deployMode client`, usar **`method: session`** (dbt-spark): o driver cria `SparkSession` e envia trabalho ao YARN.

- **314 (Airflow):** executar dbt no edge; venv `bigdata-py311`, utilizador típico **`airflow`** para tasks; admin SO **`hadoop`**.
- **311:** validação / clone do repo; mesmo venv e `profiles.yml`, outro host.

> Alternativa futura: Spark Thrift Server + `method: thrift` (mais serviço e recurso).

### PySpark sem pip extra

Usar PySpark em `$SPARK_HOME/python` com o wrapper:

- `/DATALAKE/workspace/jp/platform/scripts/data_stack/dbt/dbt_spark_env.sh`

## Instalação do dbt

Venv padrão: `/DATALAKE/opt/venvs/bigdata-py311`

## Perfis (`profiles.yml`)

Adapter **dbt-spark**, **`method: session`**. Caminho típico: `~/.dbt/profiles.yml` (template no repo acima).

### Identidade / targets

Processo no SO: **`hadoop`** ou **`airflow`**. *Targets* no `profiles.yml` para rastreio (ex. convenção `usr_dbt_*`) — ver [`naming_conventions.md`](../../naming_conventions.md).

## Storage

- Dados de negócio: **ADLS (`abfss`)**, não HDFS analítico.
- HDFS: runtime/logs (ex. `hdfs:///spark/eventlogs`).

## Pré-requisitos

- Python 3.11 + venv
- Spark on YARN
- Pacotes dbt instalados (PyPI ou mirror)

## Status (ambiente)

- **dbt 1.9.3** no `bigdata-py311` em **311** e **314** (no 314, pip como **`airflow`** onde aplicável).
- Validação: `dbt debug` / `dbt run` no **311**; no **314** completar `profiles.yml` do utilizador de execução e *smoke* `dbt run` com YARN no ar para considerar “100% operacional” no edge.
