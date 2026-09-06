CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_order_items_raw AS
SELECT
  CAST(value AS STRING) AS json_value
FROM STREAM read_kafka(
  bootstrapServers => 'redpanda:9092',
  subscribe => 'oracle.UBEREATS.ORDER_ITEMS',
  startingOffsets => 'earliest'
);

-- =================================================================

CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_order_items_pre_processed AS
SELECT
  CAST(json_value:after.ORDER_ITEM_ID AS STRING)    AS order_item_id,
  CAST(json_value:after.ORDER_ID AS INT)            AS order_id,
  CAST(json_value:after.RESTAURANT_ID AS INT)       AS restaurant_id,
  CAST(json_value:after.PRODUCT_ID AS STRING)       AS product_id,
  CAST(json_value:after.PRODUCT_NAME AS STRING)     AS product_name,
  CAST(json_value:after.PRODUCT_TYPE AS STRING)     AS product_type,
  CAST(json_value:after.CUISINE_TYPE AS STRING)     AS cuisine_type,
  CAST(json_value:after.IS_VEGETARIAN AS INT)       AS is_vegetarian,
  CAST(json_value:after.IS_COMBO AS INT)            AS is_combo,
  CAST(json_value:after.MODIFIERS AS STRING)        AS modifiers,
  CAST(json_value:after.QUANTITY AS INT)            AS quantity,
  CAST(json_value:after.UNIT_PRICE AS DECIMAL(18, 2)) AS unit_price,
  CAST(json_value:after.DISCOUNT_APPLIED AS DECIMAL(18, 2)) AS discount_applied,
  CAST(json_value:after.SUBTOTAL AS DECIMAL(18, 2)) AS subtotal,
  CAST(json_value:op AS STRING)                     AS cdc_operation,
  CAST(CAST(json_value:source.ts_ms AS BIGINT) / 1000 AS TIMESTAMP) AS cdc_commit_ts,
  CAST(json_value:source.scn AS STRING)             AS cdc_sequence,
  'oracle-ubereats'                                 AS cdc_source_system,
  current_timestamp()                               AS _datetime_ingestion
FROM
  STREAM(live.view_oracle_order_items_raw)
WHERE
  json_value:after IS NOT NULL OR json_value:op = 'd';

-- =================================================================

CREATE OR REFRESH STREAMING TABLE ods_order_items
COMMENT "ODS de itens de pedido. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 3) — antes mongodb/items simulado no MinIO.";
APPLY CHANGES INTO
  uber_eats.bronze.ods_order_items
FROM
  STREAM(live.view_oracle_order_items_pre_processed)
KEYS(order_item_id)
APPLY AS DELETE WHEN cdc_operation = 'd'
SEQUENCE BY cdc_sequence
STORED AS SCD TYPE 1;
