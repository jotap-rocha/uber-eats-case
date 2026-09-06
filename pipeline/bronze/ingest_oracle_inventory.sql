CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_inventory_raw AS
SELECT
  CAST(value AS STRING) AS json_value
FROM STREAM read_kafka(
  bootstrapServers => 'redpanda:9092',
  subscribe => 'oracle.UBEREATS.INVENTORY',
  startingOffsets => 'earliest'
);

-- =================================================================

CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_inventory_pre_processed AS
SELECT
  CAST(json_value:after.STOCK_ID AS STRING)             AS stock_id,
  CAST(json_value:after.RESTAURANT_ID AS INT)           AS restaurant_id,
  CAST(json_value:after.PRODUCT_ID AS STRING)           AS product_id,
  CAST(json_value:after.QUANTITY_AVAILABLE AS INT)      AS quantity_available,
  CAST(json_value:after.LAST_UPDATED AS STRING)         AS last_updated,
  CAST(json_value:op AS STRING)                         AS cdc_operation,
  CAST(CAST(json_value:source.ts_ms AS BIGINT) / 1000 AS TIMESTAMP) AS cdc_commit_ts,
  CAST(json_value:source.scn AS STRING)                 AS cdc_sequence,
  'oracle-ubereats'                                     AS cdc_source_system,
  current_timestamp()                                   AS _datetime_ingestion
FROM
  STREAM(live.view_oracle_inventory_raw)
WHERE
  json_value:after IS NOT NULL OR json_value:op = 'd';

-- =================================================================

CREATE OR REFRESH STREAMING TABLE ods_inventory
COMMENT "ODS de estoque. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 2).";
APPLY CHANGES INTO
  uber_eats.bronze.ods_inventory
FROM
  STREAM(live.view_oracle_inventory_pre_processed)
KEYS(stock_id)
APPLY AS DELETE WHEN cdc_operation = 'd'
SEQUENCE BY cdc_sequence
STORED AS SCD TYPE 1;
