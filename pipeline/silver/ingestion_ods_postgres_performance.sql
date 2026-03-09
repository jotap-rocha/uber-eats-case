CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_drivers_performance
COMMENT "Tabela Silver de Motoristas (Performance). Dados operacionais: Ganhos, Status e Avaliação."
AS

-- 1. LEITURA
WITH source_ods AS (
  SELECT * FROM STREAM(live.ods_postgres_drivers)
),

-- 2. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(driver_id AS STRING)                         AS id_motorista,
    
    -- Status e Operação
    CAST(status AS STRING)                            AS status_conta, -- banned, active...
    CAST(last_login AS TIMESTAMP)                     AS data_ultimo_login,
    CAST(registration_date AS TIMESTAMP)              AS data_registro,
    
    -- Financeiro e Métricas
    CAST(total_earnings AS DECIMAL(18, 2))            AS total_ganhos,
    CAST(total_deliveries AS INT)                     AS total_entregas,
    CAST(average_rating AS DECIMAL(3, 1))             AS nota_media,
    
    -- Dados de Contato (Redundante, mas útil para validação)
    CAST(email AS STRING)                             AS email,
    CAST(phone_number AS STRING)                      AS telefone,
    
    -- Veículo (Resumo)
    CAST(vehicle_type AS STRING)                      AS tipo_veiculo_operacional,
    CAST(license_plate AS STRING)                     AS placa_veiculo

  FROM source_ods
),

-- 3. LIMPEZA
cleansed_table AS (
  SELECT
    TRIM(id_motorista)                                AS id_motorista,
    LOWER(TRIM(status_conta))                         AS status_conta,
    LOWER(TRIM(email))                                AS email,
    
    -- Tratamento Financeiro
    COALESCE(total_ganhos, 0.00)                      AS total_ganhos,
    COALESCE(total_entregas, 0)                       AS total_entregas,
    COALESCE(nota_media, 0.0)                         AS nota_media,
    
    -- Datas
    COALESCE(data_ultimo_login, CAST('1900-01-01 00:00:00' AS TIMESTAMP)) AS data_ultimo_login,
    
    -- Pass-through
    data_registro,
    telefone,
    tipo_veiculo_operacional,
    placa_veiculo
  FROM typed_table
),

-- 4. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                               AS _data_ingestao,
    'ods-postgres-performance'                        AS _sistema_fonte
  FROM cleansed_table
)

SELECT * FROM silver_table;