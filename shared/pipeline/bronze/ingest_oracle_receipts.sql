-- Fase 1/Azure: ver ingest_oracle_orders.sql (mesma mudanca de fonte, Decisao 1/3)
CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_receipts_raw AS
SELECT
  CAST(value AS STRING) AS json_value
FROM STREAM read_files(
  path => 'abfss://bronze@REPLACE_STORAGE_ACCOUNT.dfs.core.windows.net/oracle/oracle.UBEREATS.RECEIPTS/',
  format => 'text'
);

-- =================================================================

CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_receipts_pre_processed AS
SELECT
  CAST(json_value:after.RECEIPT_ID AS STRING)       AS receipt_id,
  CAST(json_value:after.ORDER_ID AS INT)            AS order_id,
  CAST(json_value:after.PAYMENT_ID AS INT)          AS payment_id,
  CAST(json_value:after.TOTAL_AMOUNT AS DECIMAL(18, 2)) AS total_amount,
  CAST(json_value:after.ITEM_COUNT AS INT)          AS item_count,
  CAST(json_value:after.RECEIPT_GENERATED_AT AS STRING) AS receipt_generated_at,
  CAST(json_value:op AS STRING)                     AS cdc_operation,
  CAST(CAST(json_value:source.ts_ms AS BIGINT) / 1000 AS TIMESTAMP) AS cdc_commit_ts,
  CAST(json_value:source.scn AS STRING)             AS cdc_sequence,
  'oracle-ubereats'                                 AS cdc_source_system,
  current_timestamp()                               AS _datetime_ingestion
FROM
  STREAM(live.view_oracle_receipts_raw)
WHERE
  json_value:after IS NOT NULL OR json_value:op = 'd';

-- =================================================================

CREATE OR REFRESH STREAMING TABLE ods_receipts
COMMENT "ODS de recibos. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 3) — antes kafka/receipts simulado no MinIO.";
APPLY CHANGES INTO
  uber_eats.bronze.ods_receipts
FROM
  STREAM(live.view_oracle_receipts_pre_processed)
KEYS(receipt_id)
APPLY AS DELETE WHEN cdc_operation = 'd'
SEQUENCE BY cdc_sequence
STORED AS SCD TYPE 1;
