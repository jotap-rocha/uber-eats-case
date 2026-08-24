# Conceito — legado vs novo ambiente

> **Revisão documental:** 2026-04-24

## Armazenamento

- **Dados de negócio:** **Azure Data Lake Storage Gen2** (`abfss://…`). O **HDFS** do cluster serve para **runtime** (ex.: event logs Spark em `hdfs:///spark/eventlogs`), **não** como fonte canónica de dados analíticos ([`../../planning.md`](../../planning.md), [`../../naming_conventions.md`](../../naming_conventions.md)).

## Processamento e runtime

- **Spark on YARN**, versões fixadas no [`../../inventory.md`](../../inventory.md).
- **Python** padronizado em **3.11.x** (`bigdata-py311` nos nós documentados).

## Orquestração

- **Apache Airflow** no nó **314** (metadata **PostgreSQL** local no 314), executor `LocalExecutor`.
- **DAGs** em `/DATALAKE/dags`; lógica de negócio em **`workspace/prd/<projeto>/`** com **um venv por projeto**, não misturada com o repositório de documentação.

## dbt

- Cliente no **314** (venv `bigdata-py311`), execução Spark via **YARN** (`method: session`); detalhes em [`../../data-stack/dbt/README.md`](../../data-stack/dbt/README.md).

## Identidade e SO

- Operação humana nos nós: **`hadoop`**. Identidade por pessoa na **Web UI do Airflow** (logins em [`../../team.md`](../../team.md)); Spark/dbt sem usuário Linux extra por pessoa — ver [`../../naming_conventions.md`](../../naming_conventions.md).
