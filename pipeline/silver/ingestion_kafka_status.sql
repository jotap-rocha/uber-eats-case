CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_kafka_status
COMMENT "Tabela com status dos pedidos, com dados padronizados, tipados e limpos."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.status)
), 

-- 2. NORMALIZAÇÃO
normalized_table AS (
  SELECT
    *,
    get_json_object(status, '$.status_name')                                  AS status_name,
    get_json_object(status, '$.timestamp')                                    AS timestamp
  FROM
    bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(status_id AS STRING)                                                 AS id_status,
    CAST(order_identifier AS STRING)                                          AS id_pedido,
    CAST(status_name AS STRING)                                               AS status,
    CAST(from_unixtime(timestamp / 1000, 'yyyy-MM-dd HH:mm:ss') AS TIMESTAMP) AS data_hora
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleared_table AS (
  SELECT
    TRIM(id_status)                                                           AS id_status,
    TRIM(id_pedido)                                                           AS id_pedido,
    LOWER(TRIM(status))                                                       AS status,
    COALESCE(data_hora, CAST('1900-01-01 00:00:00' AS TIMESTAMP))             AS data_hora
  FROM
    typed_table
),

-- 5. METADATA
silver_table AS (
  SELECT
    *,
    current_timestamp()                                                       AS _data_ingestao,
    'kafka_minio'                                                             AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table