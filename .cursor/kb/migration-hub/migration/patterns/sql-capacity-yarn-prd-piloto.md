# Padrão validado — SQL Capacity PRD on YARN (Job 08 piloto)

> **Revisão documental:** 2026-06-03  
> **Status:** ✅ Piloto YARN **OK**; destino `IHMTZBDBI` via **pyodbc** (SSL Java 11 contornado)  
> **Projeto:** `data-sql-capacity-evolution-prd`  
> **Norma geral:** [`portacao-de-job.md`](portacao-de-job.md) · [`../../spark/PADRAO-SPARK-SUBMIT-PROJETO-PRD.md`](../../spark/PADRAO-SPARK-SUBMIT-PROJETO-PRD.md)

## Resumo

Primeiro job do pipeline **SQL Server Capacity Evolution** portado do Standalone legado (`spark://…:7077`) para **Spark on YARN** (cluster **311–314**). O **Job 08** (`database_tables_size`) foi validado via script bash e **Airflow** sem alterar os parâmetros CLI do job.

## O que mudou (código)

| Artefacto | Alteração |
|-----------|-----------|
| `src/management/spark_manager.py` | `mode="cluster"` → master **`yarn`**; dynamic allocation; `HADOOP_CONF_DIR` / `YARN_CONF_DIR`; override `SPARK_MASTER`; SSL Java 11 via `java_ssl_config` |
| `scripts/PRD/run_prd__08_app_database_tables_size__08.sh` | `--master yarn`; env Hadoop; dynamic allocation; rollback Standalone via `SPARK_MASTER`; flags SSL driver/executor |
| `src/utils/java_ssl_config.py` | Política SSL SHA1withRSA (leitura JDBC; workarounds JVM) |
| `src/utils/pyodbc_sqlserver.py` | **DELETE/INSERT destino IHMTZBDBI** via ODBC (contorna certificado Java 11) |
| `src/jobs/08_app_database_tables_size.py` | Destino pyodbc (default); JDBC fallback |
| `jvm-lib/icatu-spark-ssl-helper.jar` | javaagent premain (reforço SSL driver — complementar) |
| `config/java.security.ssl-relaxed` | Override merge Java security (referência documental) |

Jobs **01–07** ainda usam scripts com Standalone — replicar o padrão do Job 08 quando for a vez de cada um.

## SparkManager (Python)

Comportamento após a portação:

- `mode="cluster"` ou `"yarn"` → **`yarn`**
- `mode="local[1]"` → local (testes)
- `SPARK_MASTER` no ambiente → **override** (ex.: rollback `spark://islnx011.drmtz.com.br:7077`)
- Configs YARN adicionais: `spark.submit.deployMode=client`, `spark.dynamicAllocation.enabled=true`, `maxExecutors=3`, `spark.sql.adaptive.enabled=true`
- TLS/JDBC, Delta e WASB **mantidos** como antes
- SSL Java 11: ver secção [SSL Java 11 — destino SQL Server](#ssl-java-11--destino-sql-server)

Os jobs **não precisam** mudar a chamada `SparkManager(..., mode=spark_config.mode)` — `mode="cluster"` continua válido.

## SSL Java 11 — destino SQL Server (IHMTZBDBI)

Após migração para YARN (OpenJDK 11), operações JDBC no **destino** (`SQL_SERVER_HOSTNAME_DESTINATION` = `IHMTZBDBI`) falham com `SHA1withRSA` quando usam **mssql-jdbc** na JVM — mesmo com `trustServerCertificate=true`.

**Solução validada:** escrita no destino via **pyodbc** + ODBC Driver 17 (OpenSSL). Leitura na **origem** continua com Spark JDBC.

→ [`pyodbc-destino-ihmtzbdbi.md`](pyodbc-destino-ihmtzbdbi.md) (padrão operacional)  
→ [`java11-sqlserver-ssl-dual-cause.md`](java11-sqlserver-ssl-dual-cause.md) (causa raiz e tentativas JVM)

Resumo operacional:

| Operação | Stack |
|----------|-------|
| Leitura origem | Spark JDBC + `mssql-jdbc` |
| DELETE / INSERT destino | **pyodbc** (`SQLCAPACITY_DEST_USE_PYODBC=true`, default) |
| Fallback | JDBC (só funciona após renovação do certificado destino) |

Variáveis:

```bash
export SQLCAPACITY_DEST_USE_PYODBC=true          # default
export SQLCAPACITY_ODBC_DRIVER="ODBC Driver 17 for SQL Server"  # opcional
```

**Não** é necessário reiniciar YARN/History Server — reexecutar o job.

## Script bash (Job 08 — referência)

Variáveis-chave no wrapper:

```bash
SPARK_HOME="/DATALAKE/opt/spark"
HADOOP_CONF_DIR="/DATALAKE/opt/hadoop/etc/hadoop"
YARN_CONF_DIR="${HADOOP_CONF_DIR}"
SPARK_MASTER="${SPARK_MASTER:-yarn}"
SPARK_DEPLOY_MODE="${SPARK_DEPLOY_MODE:-client}"
YARN_MAX_EXECUTORS="${YARN_MAX_EXECUTORS:-3}"
```

`spark-submit` em YARN (**sem** `--num-executors` / `--total-executor-cores`):

```bash
"${SPARK_HOME}/bin/spark-submit" \
  --master yarn \
  --deploy-mode client \
  --conf spark.dynamicAllocation.enabled=true \
  --conf spark.dynamicAllocation.maxExecutors=3 \
  --conf spark.sql.adaptive.enabled=true \
  --conf spark.pyspark.driver.python="${PROJECT_ROOT}.venv/bin/python" \
  --conf spark.pyspark.python="${PROJECT_ROOT}.venv/bin/python" \
  --jars "${REQUIRED_JARS}" \
  ...
```

Standalone legado: exportar `SPARK_MASTER=spark://islnx011.drmtz.com.br:7077` — o script reactiva `--num-executors`.

## Comando validado (manual ou Airflow)

**Não é necessário** mudar os parâmetros do job na DAG:

```bash
bash '/datalake/workspace/prd/data-sql-capacity-evolution-prd/scripts/PRD/run_prd__08_app_database_tables_size__08.sh' \
  --instancia "ISMTZBDPGBL01\MSSQLSERVER" \
  --database "PGBL" \
  --esteira "PRODUÇÃO" \
  --timeout 1800
```

| Parâmetro Airflow | Precisa mudar? |
|-------------------|----------------|
| `--instancia`, `--database`, `--esteira`, `--timeout` | **Não** |
| Path do script | **Não** (`/datalake/...` ≡ `/DATALAKE/...`) |
| Variável `SPARK_MASTER` na DAG/Connection | **Sim, se existir** — remover ou definir `yarn` |

## Pré-requisitos operacionais

```bash
yarn node -list   # três NM (312/313/314) REGISTERED
```

Monitorização:

- YARN RM: http://islnx311.drmtz.com.br:8088/
- History Server: http://islnx311.drmtz.com.br:18080/

## Checklist para replicar nos jobs 01–07

1. Copiar bloco **Caminhos (cluster YARN)** + **YARN_SPARK_CONFS** do script do Job 08.
2. **Destino IHMTZBDBI:** integrar `src/utils/pyodbc_sqlserver.py` para DELETE/INSERT — ver [`pyodbc-destino-ihmtzbdbi.md`](pyodbc-destino-ihmtzbdbi.md) e [`pyodbc-destino-hibrido-pyspark.md`](pyodbc-destino-hibrido-pyspark.md) (distribuído vs driver).
3. Manter `.venv` do projeto em `spark.pyspark.python` (dependências PySpark/OCI/**pyodbc** do repo).
4. Confirmar `SparkManager` já em YARN (commit partilhado em `src/management/`).
5. Testar um job manualmente antes de alterar a task Airflow.
6. Actualizar matriz em [`../prd-jobs-test-and-matrix.md`](../prd-jobs-test-and-matrix.md).

## Anti-padrões (confirmados na migração)

| Evitar | Motivo |
|--------|--------|
| `--master spark://islnx311:7077` | Porta **7077 refused** no 311 — cluster novo é YARN |
| `--master spark://…:8040` | 8040 é NodeManager, **não** master Spark |
| `SPARK_MASTER` legado na DAG | Sobrescreve o default `yarn` do script |
| `--num-executors` fixo em YARN | Preferir dynamic allocation (KB cluster) |

## Agente Cursor

Para portar o próximo job ou depurar YARN: `@.cursor/agents/data-engineering/spark-cluster-migration-expert.md`
