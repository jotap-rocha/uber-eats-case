CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_drivers
COMMENT "Dimensão única de motorista — cadastro, veículo e performance, fonte Postgres real."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.ods_postgres_drivers)
),

-- 2. NORMALIZAÇÃO (Pass-through)
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(driver_id AS STRING)              AS id_motorista,
    CAST(name AS STRING)                   AS nome_completo,
    CAST(email AS STRING)                  AS email,
    CAST(phone_number AS STRING)           AS telefone,
    CAST(vehicle_type AS STRING)           AS tipo_veiculo,
    CAST(vehicle_make AS STRING)           AS veiculo_fabricante,
    CAST(vehicle_model AS STRING)          AS veiculo_modelo,
    CAST(vehicle_year AS INT)              AS veiculo_ano,
    CAST(license_plate AS STRING)          AS placa_veiculo,
    CAST(license_number AS STRING)         AS numero_cnh,
    CAST(city AS STRING)                   AS cidade,
    CAST(registration_date AS TIMESTAMP)   AS data_registro,
    CAST(total_deliveries AS INT)          AS total_entregas,
    CAST(total_earnings AS DECIMAL(18, 2)) AS total_ganhos,
    CAST(average_rating AS DECIMAL(3, 1))  AS nota_media,
    CAST(last_login AS TIMESTAMP)          AS data_ultimo_login,
    CAST(status AS STRING)                 AS status_conta
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleared_table AS (
  SELECT
    TRIM(id_motorista)                     AS id_motorista,
    TRIM(nome_completo)                    AS nome_completo,
    TRIM(email)                            AS email,
    TRIM(telefone)                         AS telefone,
    TRIM(tipo_veiculo)                     AS tipo_veiculo,
    TRIM(veiculo_fabricante)               AS veiculo_fabricante,
    TRIM(veiculo_modelo)                   AS veiculo_modelo,
    veiculo_ano,
    TRIM(placa_veiculo)                    AS placa_veiculo,
    TRIM(numero_cnh)                       AS numero_cnh,
    LOWER(TRIM(cidade))                    AS cidade,
    COALESCE(data_registro, CAST('1900-01-01 00:00:00' AS TIMESTAMP)) AS data_registro,
    COALESCE(total_entregas, 0)            AS total_entregas,
    COALESCE(total_ganhos, 0.00)           AS total_ganhos,
    COALESCE(nota_media, 0.0)              AS nota_media,
    COALESCE(data_ultimo_login, CAST('1900-01-01 00:00:00' AS TIMESTAMP)) AS data_ultimo_login,
    TRIM(status_conta)                     AS status_conta
  FROM
    typed_table
),

-- 5. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                    AS _data_ingestao,
    'postgres-real'                        AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table;
