CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_route
COMMENT "Tabela de rotas que os motoristas tomaram, segundo o aplicativo, com dados padronizados, tipados e limpos"
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.route)
),

-- 2. NORMALIZAÇÃO
-- Neste caso, os dados já vieram normalizados
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(order_id AS STRING)                                      AS id_pedido,
    CAST(route_id AS STRING)                                      AS id_rota,
    CAST(driver_id AS STRING)                                     AS id_motorista,
    CAST(start_time AS TIMESTAMP)                                 AS tempo_inicial,
    CAST(start_lat AS DOUBLE)                                     AS latitude_inicial,
    CAST(start_lon AS DOUBLE)                                     AS longitude_inicial,
    CAST(end_lat AS DOUBLE)                                       AS latitude_final,
    CAST(end_lon AS DOUBLE)                                       AS longitude_final,
    CAST(end_time AS TIMESTAMP)                                   AS tempo_final,
    CAST(distance_km AS DECIMAL(6, 2))                            AS distancia_km
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleared_table AS (
  SELECT
    TRIM(id_pedido)                                               AS id_pedido,
    TRIM(id_rota)                                                 AS id_rota,
    COALESCE(id_motorista, 0)                                     AS id_motorista,
    COALESCE(tempo_inicial, CAST('1900-01-01' AS TIMESTAMP))      AS tempo_inicial,
    COALESCE(latitude_inicial, 0.0)                               AS latitude_inicial,
    COALESCE(longitude_inicial, 0.0)                              AS longitude_inicial,
    COALESCE(latitude_final, 0.0)                                 AS latitude_final,
    COALESCE(longitude_final, 0.0)                                AS longitude_final,
    COALESCE(tempo_final, CAST('1900-01-01' AS TIMESTAMP))        AS tempo_final
  FROM
    typed_table
),

-- 5. METADATA
silver_table AS (
  SELECT
    *,
    current_timestamp()                                           AS _data_ingestao,
    'kafka-minio'                                                 AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table