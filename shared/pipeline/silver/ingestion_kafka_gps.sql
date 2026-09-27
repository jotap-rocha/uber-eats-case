CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_gps
COMMENT "Tabela silver de telemetria GPS com dados padronizados, tipados e enriquecidos."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.gps)
),

-- 2. NORMALIZAÇÃO (Pass-through)
-- Como os dados de GPS já vieram colunares (flat) do Airbyte,
-- mantemos a estrutura apenas para padronização do pipeline.
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(gps_id AS STRING)                                    AS id_gps,
    CAST(order_id AS STRING)                                  AS id_pedido,
    CAST(from_unixtime(timestamp / 1000) AS timestamp)        AS data_registro,
    CAST(lat AS double)                                       AS latitude,
    CAST(lon AS double)                                       AS longitude,
    CAST(altitude AS double)                                  AS altitude,
    CAST(speed_kph AS double)                                 AS velocidade_km,
    CAST(accuracy_m AS double)                                AS precisao_metros,
    CAST(direction_deg AS double)                             AS direcao_graus,
    CAST(duration_ms AS long)                                 AS duracao_ms
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleared_table AS (
  SELECT
    TRIM(id_gps)                                                            AS id_gps,
    TRIM(id_pedido)                                                         AS id_pedido,
    COALESCE(data_registro, CAST('1900-01-01 00:00:00' AS timestamp))       AS data_registro,
    COALESCE(latitude, 0.0)                                                 AS latitude,
    COALESCE(longitude, 0.0)                                                AS longitude,
    COALESCE(altitude, 0.0)                                                 AS altitude,
    COALESCE(velocidade_km, 0.0)                                            AS velocidade_km,
    COALESCE(precisao_metros, 0.0)                                          AS precisao_metros,
    COALESCE(direcao_graus, 0.0)                                            AS direcao_graus,
    COALESCE(duracao_ms, 0)                                                 AS duracao_ms
  FROM
    typed_table
),

-- 5. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                                                   AS _data_ingestao,
    'kafka-minio'                                                         AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table