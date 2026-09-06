CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_products_raw AS
SELECT
  CAST(value AS STRING) AS json_value
FROM STREAM read_kafka(
  bootstrapServers => 'redpanda:9092',
  subscribe => 'oracle.UBEREATS.PRODUCTS',
  startingOffsets => 'earliest'
);

-- =================================================================

CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_products_pre_processed AS
SELECT
  CAST(json_value:after.PRODUCT_ID AS STRING)       AS product_id,
  CAST(json_value:after.RESTAURANT_ID AS INT)       AS restaurant_id,
  CAST(json_value:after.NAME AS STRING)             AS name,
  CAST(json_value:after.TAGS AS STRING)             AS tags,
  CAST(json_value:after.FLAVOR_PROFILE AS STRING)   AS flavor_profile,
  CAST(json_value:after.CUISINE_TYPE AS STRING)     AS cuisine_type,
  CAST(json_value:after.PRODUCT_TYPE AS STRING)     AS product_type,
  CAST(json_value:after.PRICE AS DECIMAL(18, 2))    AS price,
  CAST(json_value:after.UNIT_COST AS DECIMAL(18, 2)) AS unit_cost,
  CAST(json_value:after.CALORIES AS INT)            AS calories,
  CAST(json_value:after.PREP_TIME_MIN AS INT)       AS prep_time_min,
  CAST(json_value:after.IS_VEGETARIAN AS INT)       AS is_vegetarian,
  CAST(json_value:after.IS_GLUTEN_FREE AS INT)      AS is_gluten_free,
  CAST(json_value:after.CREATED_AT AS STRING)       AS created_at,
  CAST(json_value:after.UPDATED_AT AS STRING)       AS updated_at,
  CAST(json_value:op AS STRING)                     AS cdc_operation,
  CAST(CAST(json_value:source.ts_ms AS BIGINT) / 1000 AS TIMESTAMP) AS cdc_commit_ts,
  CAST(json_value:source.scn AS STRING)             AS cdc_sequence,
  'oracle-ubereats'                                 AS cdc_source_system,
  current_timestamp()                               AS _datetime_ingestion
FROM
  STREAM(live.view_oracle_products_raw)
WHERE
  json_value:after IS NOT NULL OR json_value:op = 'd';

-- =================================================================

CREATE OR REFRESH STREAMING TABLE ods_oracle_products
COMMENT "ODS de produtos. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 2).";
APPLY CHANGES INTO
  uber_eats.bronze.ods_oracle_products
FROM
  STREAM(live.view_oracle_products_pre_processed)
KEYS(product_id)
APPLY AS DELETE WHEN cdc_operation = 'd'
SEQUENCE BY cdc_sequence
STORED AS SCD TYPE 1;
