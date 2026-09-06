-- 1. Le o topico Kafka (Debezium publica o envelope sem wrapper de schema --
--    value.converter.schemas.enable=false no connector)
CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_restaurants_raw AS
SELECT
  CAST(value AS STRING) AS json_value
FROM STREAM read_kafka(
  bootstrapServers => 'redpanda:9092',
  subscribe => 'oracle.UBEREATS.RESTAURANTS',
  startingOffsets => 'earliest'
);

-- =================================================================

-- 2. Extrai o envelope Debezium (Oracle retorna nomes de coluna em
--    MAIUSCULO por padrao -- identificadores nao citados na DDL)
CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_restaurants_pre_processed AS
SELECT
  CAST(json_value:after.RESTAURANT_ID AS INT)      AS restaurant_id,
  CAST(json_value:after.UUID AS STRING)            AS uuid,
  CAST(json_value:after.NAME AS STRING)            AS name,
  CAST(json_value:after.ADDRESS AS STRING)         AS address,
  CAST(json_value:after.CITY AS STRING)            AS city,
  CAST(json_value:after.COUNTRY AS STRING)         AS country,
  CAST(json_value:after.PHONE_NUMBER AS STRING)    AS phone_number,
  CAST(json_value:after.CUISINE_TYPE AS STRING)    AS cuisine_type,
  CAST(json_value:after.OPENING_TIME AS STRING)    AS opening_time,
  CAST(json_value:after.CLOSING_TIME AS STRING)    AS closing_time,
  CAST(json_value:after.AVERAGE_RATING AS DECIMAL(3, 1)) AS average_rating,
  CAST(json_value:after.NUM_REVIEWS AS INT)        AS num_reviews,
  CAST(json_value:after.CNPJ AS STRING)            AS cnpj,
  CAST(json_value:after.LAT AS DOUBLE)             AS lat,
  CAST(json_value:after.LON AS DOUBLE)             AS lon,
  CAST(json_value:op AS STRING)                    AS cdc_operation,
  CAST(CAST(json_value:source.ts_ms AS BIGINT) / 1000 AS TIMESTAMP) AS cdc_commit_ts,
  CAST(json_value:source.scn AS STRING)            AS cdc_sequence,
  'oracle-ubereats'                                AS cdc_source_system,
  current_timestamp()                              AS _datetime_ingestion
FROM
  STREAM(live.view_oracle_restaurants_raw)
WHERE
  json_value:after IS NOT NULL OR json_value:op = 'd';

-- =================================================================

-- 3. Ingerir tabela na camada bronze (mesmo padrao de ingest_postgres_drivers.sql,
--    trocando SEQUENCE BY timestamp por SEQUENCE BY SCN -- monotonico no Oracle,
--    evita colisao de ordenacao em rajada de updates)
CREATE OR REFRESH STREAMING TABLE ods_oracle_restaurants
COMMENT "ODS de restaurantes. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 2).";
APPLY CHANGES INTO
  uber_eats.bronze.ods_oracle_restaurants
FROM
  STREAM(live.view_oracle_restaurants_pre_processed)
KEYS(restaurant_id)
APPLY AS DELETE WHEN cdc_operation = 'd'
SEQUENCE BY cdc_sequence
STORED AS SCD TYPE 1;
-- Nota: cdc_operation/cdc_commit_ts/cdc_sequence/cdc_source_system NAO sao
-- excluidos aqui (diferente de _ab_cdc_* no padrao Postgres) -- sao o
-- contrato canonico de CDC que a Silver consome, independente da ferramenta
-- de ingestao (ver DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md).
