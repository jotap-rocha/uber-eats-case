# Destino IHMTZBDBI — modelo híbrido PySpark + pyodbc

> **Revisão documental:** 2026-06-03  
> **Status:** Padrão adoptado a partir do **Job 08** (YARN + OpenJDK 11)  
> **Escopo:** escrita no SQL Server destino `IHMTZBDBI` / `DatabaseCapacity`  
> **Migração cluster:** [`pyodbc-destino-ihmtzbdbi.md`](pyodbc-destino-ihmtzbdbi.md)

## Resposta rápida

| Pergunta | Resposta |
|----------|----------|
| O job deixa de ser PySpark? | **Não** — continua `spark-submit`, `SparkSession`, executors |
| pyodbc substitui o Spark inteiro? | **Não** — só **DELETE** e **INSERT no destino** |
| Há processamento distribuído na inserção? | **Não** — INSERT colapsa no **driver** (`toPandas()` + `executemany`) |
| Há processamento distribuído antes da inserção? | **Sim** — leitura origem e transformações usam Spark normalmente |

## Por que este modelo existe

No cluster **YARN + Java 11**, o driver JDBC **`mssql-jdbc`** falha no destino com certificado legado **SHA1withRSA** (`Algorithm constraints check failed`). A **origem** (outros servidores SQL) continua OK via Spark JDBC.

**pyodbc** usa **OpenSSL** no processo Python e contorna as restrições da JVM — sem abandonar o pipeline PySpark.

## Arquitectura por fase

```text
┌─────────────────────────────────────────────────────────────────────────┐
│  FASE DISTRIBUÍDA (PySpark / YARN)                                       │
├─────────────────────────────────────────────────────────────────────────┤
│  spark-submit → SparkSession → executors                                 │
│  Leitura origem:  df.read.format("jdbc")  +  mssql-jdbc (Java)         │
│  Transformações:  DataProcessor, withColumn, cast, count, collect      │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │  Spark DataFrame pronto
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  FASE NO DRIVER (Python puro — NÃO distribuída)                          │
├─────────────────────────────────────────────────────────────────────────┤
│  DELETE destino:  pyodbc + SQL (execute)                                 │
│  INSERT destino:  df.toPandas() → pyodbc fast_executemany                │
│  Conexão:         ODBC Driver 17 + OpenSSL → IHMTZBDBI                   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Comparação: JDBC Spark vs pyodbc (destino)

| Aspecto | `df.write.jdbc` (legado / certificado OK) | pyodbc (actual IHMTZBDBI) |
|---------|-------------------------------------------|---------------------------|
| Onde corre o INSERT | Executors (paralelo por partição) | **Driver apenas** |
| Conexões SQL | Várias | **Uma** |
| Memória na escrita | Particionada nos executors | **Toda no driver** (`toPandas()`) |
| Stack SSL | JVM / mssql-jdbc | OpenSSL / ODBC |
| Job continua PySpark? | Sim | **Sim** |

## Código de referência

| Artefacto | Papel |
|-----------|-------|
| `src/utils/pyodbc_sqlserver.py` | `build_pyodbc_connection_string`, `execute_non_query`, `insert_dataframe` |
| `src/jobs/08_app_database_tables_size.py` | Piloto: pyodbc default no destino; JDBC fallback |
| `src/utils/connections_classes.py` | `SQLServerWriter` — JDBC Spark (fallback / origem) |

Trecho crítico do INSERT (materialização no driver):

```python
pdf = dataframe.toPandas()  # driver — não distribuído
cursor.fast_executemany = True
cursor.executemany(insert_sql, batch)
```

## Variáveis de ambiente

```bash
export SQLCAPACITY_DEST_USE_PYODBC=true   # default
export SQLCAPACITY_ODBC_DRIVER="ODBC Driver 17 for SQL Server"  # opcional
export SQLCAPACITY_DEST_USE_PYODBC=false  # força JDBC — falha no IHMTZBDBI com Java 11
```

## Implicações por job

| Job | Volume típico destino | Adequação do padrão actual |
|-----|----------------------|----------------------------|
| **08** | ~100 linhas / banco | ✅ Ideal |
| **01–07** | Por servidor, variável | ⚠️ Avaliar `toPandas()` — OK se linhas cabem na memória do driver |
| Jobs massivos (milhões de linhas) | Alto | ❌ Não copiar cegamente — ver alternativas abaixo |

### Sinais de que o driver está no limite

- `OutOfMemoryError` no driver após `toPandas()`
- INSERT lento mas CPU dos executors ociosa
- Log mostra materialização de milhões de linhas no driver

## Alternativas futuras (não implementadas)

| Abordagem | Distribuído? | Quando considerar |
|-----------|--------------|-------------------|
| Renovar certificado IHMTZBDBI (SHA-256) | ✅ com `df.write.jdbc` | **Solução definitiva** |
| `foreachPartition` + pyodbc por executor | ✅ parcial | Volume alto + certificado ainda legado |
| Staging ADLS + carga batch externa | ✅ leitura/escrita ficheiro | Volumes muito grandes |
| Manter cluster legado Java 8 só para escrita | ✅ JDBC | Temporário — não recomendado |

## Checklist ao replicar nos jobs 01–07

```text
[ ] Job continua spark-submit + SparkSession (não converter para script Python puro)
[ ] Leitura origem: Spark JDBC (mssql-jdbc) — inalterado
[ ] DELETE destino: pyodbc via pyodbc_sqlserver.execute_non_query
[ ] INSERT destino: pyodbc via pyodbc_sqlserver.insert_dataframe
[ ] Estimar row_count antes de toPandas() — driver memory
[ ] ODBC Driver 17 + pyodbc no venv do nó de submit
[ ] Log deve indicar "(pyodbc)" no DELETE/INSERT de sucesso
[ ] Documentar excepção se volume exigir outro desenho
```

## Anti-padrões

| Evitar | Motivo |
|--------|--------|
| Assumir que pyodbc = job Python sem Spark | Perde-se leitura/transformação distribuída |
| Assumir INSERT distribuído com pyodbc actual | `toPandas()` colapsa no driver |
| Usar pyodbc na **origem** sem necessidade | Origem JDBC Spark funciona |
| `toPandas()` em DataFrames gigantes | OOM no driver |
| Desactivar pyodbc no YARN sem certificado renovado | DELETE/INSERT destino falham de novo |

## Referências cruzadas

- SSL / causa raiz Java 11: [`java11-sqlserver-ssl-dual-cause.md`](java11-sqlserver-ssl-dual-cause.md)
- Operacional ODBC / comandos: [`pyodbc-destino-ihmtzbdbi.md`](pyodbc-destino-ihmtzbdbi.md)
- Piloto YARN Job 08: [`sql-capacity-yarn-prd-piloto.md`](sql-capacity-yarn-prd-piloto.md)
- Conceitos legado vs novo: [`../concepts/legado-vs-novo.md`](../concepts/legado-vs-novo.md)
- Agente migração: `@.cursor/agents/data-engineering/spark-cluster-migration-expert.md`
