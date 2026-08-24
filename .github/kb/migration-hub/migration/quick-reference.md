# Migração — referência rápida

> **Revisão documental:** 2026-06-03

## Paths fixos (314 / DATALAKE)

| O quê | Onde |
|-------|------|
| DAGs Airflow (carregadas pelo scheduler) | `/DATALAKE/dags` |
| Código por projeto (venv por projeto) | `/DATALAKE/workspace/prd/<projeto>/` |
| Documentação, scripts, `kb/`, `dbt/` exemplo | `/DATALAKE/workspace/jp/big_data_project` |
| Segredos Airflow (fora de Git) | `/DATALAKE/var/airflow/secrets/` no 314 |

## Versões alvo (resumo)

Ver [`inventory.md`](../inventory.md). Alinhamento típico: Spark **3.5.2**, Python **3.11.11**, dbt **1.9.3**, Airflow **2.11.1**, Postgres **15**.

## Comandos de verificação

```bash
# No 311 como hadoop, com bigdata.sh carregado:
/DATALAKE/workspace/jp/big_data_project/scripts/infra/validate_cluster.sh

# Incluir SparkPi on YARN (mais lento):
RUN_SPARK_PI=1 /DATALAKE/workspace/jp/big_data_project/scripts/infra/validate_cluster.sh
```

Objetivo: **exit 0** com HDFS/YARN no ar (ver [`../planning.md`](../planning.md)).

## Critério “pode começar a clonar” (Fase G)

Fases **A, B, D (311–314), E** verdes; **C** quando for testar Spark. **Nenhuma** execução agendada **produtiva** até testes Python → Spark → **piloto único** concluídos ([`../planning.md`](../planning.md)).

## SQL Capacity PRD — Job 08 on YARN (validado)

```bash
bash '/datalake/workspace/prd/data-sql-capacity-evolution-prd/scripts/PRD/run_prd__08_app_database_tables_size__08.sh' \
  --instancia "SERVIDOR\MSSQLSERVER" --database "PGBL" --esteira "PRODUÇÃO" --timeout 1800
```

- **Airflow:** mesmo comando — **não** alterar parâmetros CLI; garantir que `SPARK_MASTER` legado **não** está na DAG.
- **Detalhe YARN:** [`patterns/sql-capacity-yarn-prd-piloto.md`](patterns/sql-capacity-yarn-prd-piloto.md)
- **SSL Java 11 (SHA1withRSA):** [`patterns/java11-sqlserver-ssl-dual-cause.md`](patterns/java11-sqlserver-ssl-dual-cause.md)
- **Destino IHMTZBDBI (solução validada):** [`patterns/pyodbc-destino-ihmtzbdbi.md`](patterns/pyodbc-destino-ihmtzbdbi.md) — DELETE/INSERT via **pyodbc**; origem continua **mssql-jdbc**

## Links úteis

- Checklist edge: [`../data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md`](../data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md)
- Acessos humanos (F5): [`acess_links.md`](../acess_links.md)
