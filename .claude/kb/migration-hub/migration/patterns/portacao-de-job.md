# Padrão — portação de um job

> **Revisão documental:** 2026-06-03  
> **Norma completa:** [`../../planning.md`](../../planning.md) (secção “Migração de jobs” e “Job piloto”).

Use esta página como **checklist**; não substitui o planejamento nem os guias de Spark/ADLS/Airflow.

> **Piloto validado (SQL Capacity PRD, Job 08):** ver [`sql-capacity-yarn-prd-piloto.md`](sql-capacity-yarn-prd-piloto.md).

## Antes de portar cada job

| Item | Notas |
|------|--------|
| Versão Spark / Scala / Python | Alinhar com **3.5.2 / 2.12 / 3.11.11** (ver [`../../inventory.md`](../../inventory.md)) |
| Paths de dados | **`abfss://`** (ADLS) vs `hdfs://` — atualizar para o root documentado |
| JARs extras / `--packages` | Cluster ou `spark.yarn.jars` / archive |
| Agendamento | Cron/Airflow antigo → **DAG** no Airflow **314** |
| Segredos | Service Principal / connection strings **fora do Git**; Airflow **Connections** ou env no submit |
| JDBC SQL Server (Java 11) | **Destino IHMTZBDBI:** usar **pyodbc** para DELETE/INSERT — [`pyodbc-destino-ihmtzbdbi.md`](pyodbc-destino-ihmtzbdbi.md). Causa SSL: [`java11-sqlserver-ssl-dual-cause.md`](java11-sqlserver-ssl-dual-cause.md) |
| Validação | Contagem de linhas / checksum em amostra; comparar **schema** |

## Piloto (recomendado)

1. Escolher pipeline de **baixo risco** (leitura ou escrita em **prefixo de teste** no ADLS).
2. **`spark-submit` manual** antes de automatizar com DAG.
3. Critérios de aceite: job **completa no YARN** sem `FAILED`; saída no ADLS **conferível**; logs no **History Server**; tempo dentro de faixa acordada ([`../../planning.md`](../../planning.md)).

## Depois do piloto

- Automatizar com DAG em `/DATALAKE/dags`, pausada ou não produtiva até acordo explícito (Fase G).
