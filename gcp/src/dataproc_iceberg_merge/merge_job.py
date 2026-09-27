"""Job PySpark: materializa/mantém as tabelas Iceberg do BigLake a partir dos
arquivos brutos do GCS/Bronze (Decisão 5, DESIGN_INGESTAO_GCP_FASE3.md).

Mesmo papel que o Glue Crawler cumpriu na Fase 2/AWS, mas via job explícito -
o GCP não tem um crawler equivalente que também escreva formato Iceberg
verdadeiro (manifests/snapshots). Usa o contrato canônico de CDC
(cdc_operation/cdc_commit_ts/cdc_sequence/cdc_source_system) para idempotência,
mesmo princípio do APPLY CHANGES INTO já usado no Databricks deste projeto
(Onda 3).
"""
from __future__ import annotations

import argparse

from pyspark.sql import SparkSession


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bronze-bucket", required=True)
    parser.add_argument("--connection", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument(
        "--tables",
        nargs="*",
        default=["postgres/drivers", "oracle/restaurants", "mongodb/perfil_restaurante"],
        help="Prefixos de tabela dentro do GCS/Bronze a materializar nesta execução",
    )
    return parser.parse_args()


def merge_table(spark: SparkSession, *, bronze_bucket: str, table_prefix: str, connection: str, dataset: str) -> None:
    table_name = table_prefix.split("/")[-1]
    source_path = f"gs://{bronze_bucket}/{table_prefix}/*.json"
    target_table = f"`{dataset}`.`{table_name}`"

    staging = spark.read.json(source_path)
    staging.createOrReplaceTempView("staging_source")

    spark.sql(
        f"""
        CREATE TABLE IF NOT EXISTS {target_table}
        USING ICEBERG
        WITH CONNECTION `{connection}`
        AS SELECT * FROM staging_source WHERE 1=0
        """
    )

    spark.sql(
        f"""
        MERGE INTO {target_table} AS target
        USING (
          SELECT *
          FROM staging_source
          QUALIFY ROW_NUMBER() OVER (
            PARTITION BY id ORDER BY cdc_sequence DESC
          ) = 1
        ) AS source
        ON target.id = source.id
        WHEN MATCHED AND source.cdc_operation = 'DELETE' THEN DELETE
        WHEN MATCHED THEN UPDATE SET *
        WHEN NOT MATCHED AND source.cdc_operation != 'DELETE' THEN INSERT *
        """
    )


def main() -> None:
    args = parse_args()
    spark = SparkSession.builder.appName("ubereats-fase3-iceberg-merge").getOrCreate()

    for table_prefix in args.tables:
        merge_table(
            spark,
            bronze_bucket=args.bronze_bucket,
            table_prefix=table_prefix,
            connection=args.connection,
            dataset=args.dataset,
        )

    spark.stop()


if __name__ == "__main__":
    main()
