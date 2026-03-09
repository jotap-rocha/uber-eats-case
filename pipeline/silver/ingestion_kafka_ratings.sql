CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_mysql_ratings
COMMENT "Tabela de Avaliações com notas dadas aos restaurantes (identificados por CNPJ)"
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.mysql_ratings)
),

-- 2. NORMALIZAÇÃO (Pass-through)
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(rating_id AS STRING)                         AS id_avaliacao,
    CAST(uuid AS STRING)                              AS id_usuario,
    CAST(restaurant_identifier AS STRING)             AS cnpj_restaurante,
    CAST(rating AS DECIMAL(3, 1))                     AS nota_avaliacao,
    CAST(timestamp AS TIMESTAMP)                      AS data_avaliacao
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleansed_table AS (
  SELECT
    TRIM(id_avaliacao)                                AS id_avaliacao,
    TRIM(id_usuario)                                  AS id_usuario,
    TRIM(cnpj_restaurante)                            AS cnpj_restaurante,
    COALESCE(nota_avaliacao, 0.0)                     AS nota_avaliacao,
    COALESCE(data_avaliacao, CAST('1900-01-01 00:00:00' AS TIMESTAMP)) AS data_avaliacao
  FROM
    typed_table
),

-- 5. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                               AS _data_ingestao,
    'mysql-minio'                                     AS _sistema_fonte
  FROM
    cleansed_table
)

SELECT * FROM silver_table;