# Spark e Azure Data Lake Storage (Gen2) — `abfss://`

## Resumo

Integração para leitura/escrita em **ADLS Gen2** a partir do Spark **3.5.2 on YARN**, usando os mesmos jars do **Hadoop 3.3.6** instalado no cluster (evita mistura ad hoc de versões).

## Jars no classpath do Spark

Script idempotente (copia de `HADOOP_HOME/share/hadoop/tools/lib` → `SPARK_HOME/jars`):

- [`sync_spark_azure_jars.sh`](/DATALAKE/workspace/jp/platform/scripts/data_stack/adls/sync_spark_azure_jars.sh)

Jars incluídos: `hadoop-azure`, `hadoop-azure-datalake`, `azure-storage`, `azure-data-lake-store-sdk`, `azure-keyvault-core`.

## Configuração (OAuth2 — Service Principal)

Defina credenciais **fora do Git** (variáveis de ambiente no submit, ou `spark.hadoop.*` via `--conf`).

Propriedades Hadoop (prefixo `spark.hadoop.` no Spark) por conta de armazenamento:

| Propriedade | Exemplo |
|-------------|---------|
| `fs.azure.account.auth.type.<account>.dfs.core.windows.net` | `OAuth` |
| `fs.azure.account.oauth.provider.type.<account>.dfs.core.windows.net` | `org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider` |
| `fs.azure.account.oauth2.client.id.<account>.dfs.core.windows.net` | Client ID do app registration |
| `fs.azure.account.oauth2.client.secret.<account>.dfs.core.windows.net` | Secret |
| `fs.azure.account.oauth2.client.endpoint.<account>.dfs.core.windows.net` | `https://login.microsoftonline.com/<tenant>/oauth2/token` |

Fragmento comentado: [`adls_spark_defaults.fragment.conf`](/DATALAKE/workspace/jp/platform/scripts/data_stack/adls/adls_spark_defaults.fragment.conf).

## Teste mínimo (read/write)

Com **YARN e HDFS no ar** e variáveis exportadas:

- `AZURE_STORAGE_ACCOUNT`, `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`
- `ABFSS_TEST_PREFIX` — ex.: `abfss://<container>@<account>.dfs.core.windows.net/datalake/_spark_abfss_test`

Executar:

```bash
cd /DATALAKE/workspace/jp/big_data_project/scripts/data_stack/adls
./test_abfss.sh
```

O job PySpark grava e relê um parquet sob o prefixo (subpasta `validate_<applicationId>`).

## Documentação relacionada

- Estrutura do lake: [`../data-stack/datalake/README.md`](../data-stack/datalake/README.md)
