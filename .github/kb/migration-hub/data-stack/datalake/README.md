# Data Lake (Storage) — Azure Data Lake Storage (ADLS Gen2)

## Resumo bem pequeno do passo
Este projeto **não usará HDFS** como camada de armazenamento de dados de negócio.  
O Data Lake (medallion: landing/bronze/silver/gold) ficará no **Azure Data Lake Storage (ADLS Gen2)**.

> Nota: HDFS permanece no cluster para necessidades do runtime (ex.: `hdfs:///spark/eventlogs` do Spark History Server), não como storage do Data Lake.

## Root Path (ADLS)
Definir conta e container (registrar abaixo quando fixado) e usar o padrão:

- `abfss://<container>@<storage-account>.dfs.core.windows.net/datalake/`

**Integração Spark (jars + OAuth + teste `abfss`)**: ver [`../../spark/ADLS-GEN2-SPARK.md`](../../spark/ADLS-GEN2-SPARK.md) e scripts em [`data_stack/adls/`](/DATALAKE/workspace/jp/platform/scripts/data_stack/adls/).

## Camadas (Medallion)
- `.../datalake/landing/<source_system>/`
- `.../datalake/bronze/<source_system>/<table_name>/year=YYYY/month=MM/day=DD/`
- `.../datalake/silver/<domain>/<table_name>/year=YYYY/month=MM/day=DD/`
- `.../datalake/gold/<business_area>/<model_name>/year=YYYY/month=MM/day=DD/`

## Integração (alto nível)
- **Airbyte**: landing/bronze no ADLS (sem pendências operacionais).
- **Spark**: leitura/escrita no ADLS (abfss), e execução on YARN.
- **dbt**: será integrado com **Spark** (Trino fica como possibilidade a avaliar conforme recursos).
