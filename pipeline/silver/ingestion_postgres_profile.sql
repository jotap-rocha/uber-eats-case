CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_drivers_profile
COMMENT "Tabela Silver de Motoristas (Perfil). Dados cadastrais: Nome, Endereço e Detalhes do Veículo."
AS

-- 1. LEITURA
WITH source_minio AS (
  SELECT * FROM STREAM(live.postgres_drivers) -- Ajuste o nome conforme sua bronze
),

-- 2. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(driver_id AS STRING)                         AS id_motorista,
    CAST(uuid AS STRING)                              AS id_uuid,
    
    -- Dados Pessoais
    CAST(first_name AS STRING)                        AS nome_primeiro,
    CAST(last_name AS STRING)                         AS sobrenome,
    CAST(date_birth AS DATE)                          AS data_nascimento,
    CAST(phone_number AS STRING)                      AS telefone_cadastro,
    
    -- Localização
    CAST(city AS STRING)                              AS cidade,
    CAST(country AS STRING)                           AS pais, -- Typo na origem 'contry'? Mantemos corrigido aqui?
    
    -- Detalhes do Veículo (Mais rico que na ODS)
    CAST(vehicle_make AS STRING)                      AS veiculo_fabricante, -- Ex: Honda
    CAST(vehicle_model AS STRING)                     AS veiculo_modelo,     -- Ex: Civic
    CAST(vehicle_year AS INT)                         AS veiculo_ano,
    CAST(vehicle_type AS STRING)                      AS veiculo_categoria,  -- Ex: Carro, Moto
    CAST(license_number AS STRING)                    AS numero_cnh          -- Ou RENAVAM? Pelo nome parece CNH.
  FROM source_minio
),

-- 3. LIMPEZA
cleansed_table AS (
  SELECT
    TRIM(id_motorista)                                AS id_motorista,
    TRIM(id_uuid)                                     AS id_uuid,
    
    -- Padronização
    TRIM(nome_primeiro)                               AS nome_primeiro,
    TRIM(sobrenome)                                   AS sobrenome,
    LOWER(TRIM(cidade))                               AS cidade,
    LOWER(TRIM(pais))                                 AS pais,
    
    -- Veículo
    UPPER(TRIM(veiculo_fabricante))                   AS veiculo_fabricante,
    UPPER(TRIM(veiculo_modelo))                       AS veiculo_modelo,
    COALESCE(veiculo_ano, 0)                          AS veiculo_ano,
    
    -- Dados Sensíveis (Mantemos trim, talvez mascarar na Gold?)
    TRIM(telefone_cadastro)                           AS telefone_cadastro,
    TRIM(numero_cnh)                                  AS numero_cnh,
    
    data_nascimento,
    veiculo_categoria

  FROM typed_table
),

-- 4. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                               AS _data_ingestao,
    'minio-postgres-profile'                          AS _sistema_fonte
  FROM cleansed_table
)

SELECT * FROM silver_table;