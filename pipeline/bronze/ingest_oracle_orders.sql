CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_orders_raw AS
SELECT
  CAST(value AS STRING) AS json_value
FROM STREAM read_kafka(
  bootstrapServers => 'redpanda:9092',
  subscribe => 'oracle.UBEREATS.ORDERS',
  startingOffsets => 'earliest'
);

-- =================================================================

CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_orders_pre_processed AS
SELECT
  CAST(json_value:after.ORDER_ID AS INT)            AS order_id,
  CAST(json_value:after.USER_ID AS INT)             AS user_id,
  CAST(json_value:after.RESTAURANT_ID AS INT)       AS restaurant_id,
  CAST(json_value:after.DRIVER_ID AS INT)           AS driver_id,
  CAST(json_value:after.ORDER_DATE AS STRING)       AS order_date,
  CAST(json_value:after.TOTAL_AMOUNT AS DECIMAL(18, 2)) AS total_amount,
  CAST(json_value:after.STATUS AS STRING)           AS status,
  CAST(json_value:after.UPDATED_AT AS STRING)       AS updated_at,
  CAST(json_value:op AS STRING)                     AS cdc_operation,
  CAST(CAST(json_value:source.ts_ms AS BIGINT) / 1000 AS TIMESTAMP) AS cdc_commit_ts,
  CAST(json_value:source.scn AS STRING)             AS cdc_sequence,
  'oracle-ubereats'                                 AS cdc_source_system,
  current_timestamp()                               AS _datetime_ingestion
FROM
  STREAM(live.view_oracle_orders_raw)
WHERE
  json_value:after IS NOT NULL OR json_value:op = 'd';

-- =================================================================

-- Ingerir tabela na camada bronze. SEQUENCE BY cdc_sequence (SCN) e
-- decisivo aqui -- Pedido tem 8 UPDATEs de status por ciclo de vida
-- (mesmo mecanismo fork+stateMachine da Etapa 1, agora combinado com
-- Oracle pela primeira vez), timestamp sozinho colidiria com facilidade.
CREATE OR REFRESH STREAMING TABLE ods_orders
COMMENT "ODS de pedidos. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 3) — antes kafka/orders simulado no MinIO, sem mutacao de status.";
APPLY CHANGES INTO
  uber_eats.bronze.ods_orders
FROM
  STREAM(live.view_oracle_orders_pre_processed)
KEYS(order_id)
APPLY AS DELETE WHEN cdc_operation = 'd'
SEQUENCE BY cdc_sequence
STORED AS SCD TYPE 1;
