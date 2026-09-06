CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_shift
COMMENT "Tabela de turnos dentro do app, com dados padronizados, tipados e limpos."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.shift)
),

-- 2. NORMALIZAÇÃO
-- Neste caso, os dados já vieram normalizados
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(shift_id AS STRING)                                          AS id_turno,
    CAST(driver_id AS STRING)                                         AS id_motorista,
    CAST(city AS STRING)                                              AS cidade,
    CAST(region AS STRING)                                            AS pais,
    CAST(device_os AS STRING)                                         AS sistema_operacional,
    CAST(start_time AS TIMESTAMP)                                     AS data_inicio,
    CAST(end_time AS TIMESTAMP)                                       AS data_fim,
    CAST(shift_duration_min AS INT)                                   AS duracao_turno_minutos,
    CAST(earnings_brl AS DECIMAL(18,2))                                AS ganho_em_real,
    CAST(num_orders AS INT)                                           AS quantidade_pedidos,
    CAST(distance_covered_km AS DOUBLE)                               AS distancia_percorrida_km,
    CAST(shift_rating AS DECIMAL(2,2))                                AS avaliacao_turno,
    CAST(shift_type AS STRING)                                        AS tipo_turno,
    CAST(login_method AS STRING)                                      AS metodo_login,
    CAST(available AS BOOLEAN)                                        AS flag_disponivel,
    CAST(issues_reported AS STRING)                                   AS problemas_reportados
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleared_table AS (
  SELECT
    TRIM(id_turno)                                                    AS id_turno,
    TRIM(id_motorista)                                                AS id_motorista,
    LOWER(TRIM(cidade))                                               AS cidade,
    LOWER(TRIM(pais))                                                 AS pais,
    LOWER(TRIM(sistema_operacional))                                  AS sistema_operacional,
    COALESCE(data_inicio, CAST('1900-01-01 00:00:00' AS TIMESTAMP))   AS data_inicio,
    COALESCE(data_fim, CAST('1900-01-01 00:00:00' AS TIMESTAMP))      AS data_fim,
    COALESCE(duracao_turno_minutos, 0)                                AS duracao_turno_minutos,
    COALESCE(ganho_em_real, 0.00)                                     AS ganho_em_real,
    COALESCE(quantidade_pedidos, 0)                                   AS quantidade_pedidos,
    COALESCE(distancia_percorrida_km, 0.00)                           AS distancia_percorrida_km,
    COALESCE(avaliacao_turno, 0.00)                                   AS avaliacao_turno,
    LOWER(TRIM(tipo_turno))                                           AS tipo_turno,
    LOWER(TRIM(metodo_login))                                         AS metodo_login,
    COALESCE(flag_disponivel, false)                                  AS flag_disponivel,
    LOWER(TRIM(problemas_reportados))                                 AS problemas_reportados
  FROM
    typed_table
),

-- 5. METADATA
silver_table AS (
  SELECT
    *,
    current_timestamp()                                               AS _data_ingestao,
    'kafka-minio'                                                     AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table