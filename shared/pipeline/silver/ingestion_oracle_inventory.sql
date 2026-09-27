CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_inventory
COMMENT "Tabela de Estoque com controle de disponibilidade de produtos por restaurante. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 2) — antes postgres/inventory simulado no MinIO."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.ods_inventory)
),

-- 2. NORMALIZAÇÃO (Pass-through)
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(stock_id AS STRING)                          AS id_estoque,
    CAST(product_id AS STRING)                        AS id_produto,
    CAST(restaurant_id AS STRING)                     AS id_restaurante,
    CAST(quantity_available AS INT)                   AS quantidade_disponivel,
    CAST(last_updated AS TIMESTAMP)                   AS data_ultima_atualizacao
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleansed_table AS (
  SELECT
    TRIM(id_estoque)                                  AS id_estoque,
    TRIM(id_produto)                                  AS id_produto,
    TRIM(id_restaurante)                              AS id_restaurante,
    COALESCE(quantidade_disponivel, 0)                AS quantidade_disponivel,
    COALESCE(data_ultima_atualizacao, CAST('1900-01-01 00:00:00' AS TIMESTAMP)) AS data_ultima_atualizacao
  FROM
    typed_table
),

-- 5. METADADOS E SKs
silver_table AS (
  SELECT
    *,
    current_timestamp()                               AS _data_ingestao,
    'oracle-ubereats'                                 AS _sistema_fonte
  FROM
    cleansed_table
)

SELECT * FROM silver_table;
