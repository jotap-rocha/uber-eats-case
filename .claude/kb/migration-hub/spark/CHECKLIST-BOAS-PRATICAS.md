# Checklist — Boas Práticas Spark (on YARN)

## Resumo bem pequeno do passo
Checklist aplicado no cluster e ajustes feitos para alinhar com boas práticas (usuário dedicado, configs centralizadas, event logs e History Server).

## Passo (código)

```bash
# 1) Usuário dedicado (spark:spark) + variáveis globais
# - Criado usuário/grupo spark
# - JAVA_HOME e PATH exportados em /etc/profile.d (java11.sh e bigdata.sh)

# 2) Java
# - Java 11 (OpenJDK) OK
# - JAVA_HOME setado globalmente (/etc/profile.d) e para o Spark (spark-env.sh)

# 3) Python
# - Python 3.9.23 presente em 311/312/313/314 (compatível com PySpark 3.8+)

# 4) Estrutura de pastas / symlink
# - Spark em /DATALAKE/opt/spark-3.5.2-bin-hadoop3
# - Symlink ativo: /DATALAKE/opt/spark

# 5) Configuração centralizada (spark-defaults.conf)
# - serializer Kryo habilitado
# - eventLog habilitado e persistido no HDFS
# - spark.yarn.archive configurado (evita upload de libs a cada submit)

# 6) Event Logs (HDFS)
hdfs dfs -ls -h /spark/eventlogs

# 7) Spark History Server (311)
/DATALAKE/opt/spark/sbin/start-history-server.sh
curl -I http://127.0.0.1:18080/

# 8) Validação (SparkPi em YARN)
/DATALAKE/opt/spark/bin/spark-submit --master yarn --deploy-mode client \
  --class org.apache.spark.examples.SparkPi \
  /DATALAKE/opt/spark/examples/jars/spark-examples_2.12-3.5.2.jar 2


# 9) Integração com ADLS Gen2 (Azure) — jars + teste abfss
# Os jars vêm do próprio Hadoop 3.3.6 (tools/lib), alinhados ao cluster:
#   bash scripts/data_stack/adls/sync_spark_azure_jars.sh   # (a partir da raiz do repositório)
# Jars copiados para: /DATALAKE/opt/spark/jars/ (hadoop-azure, azure-storage, etc.)
#
# Autenticação OAuth (Service Principal) e teste de leitura/escrita:
#   kb/spark/ADLS-GEN2-SPARK.md
#   scripts/data_stack/adls/test_abfss.sh (requer variáveis de ambiente; YARN no ar)
```


