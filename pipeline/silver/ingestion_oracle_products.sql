CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_products
COMMENT "Tabela de Produtos e preços, custos e classificações dietéticas, com dados padronizados, tipados e limpos. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 2) — antes mysql/products simulado no MinIO."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.ods_oracle_products)
),

-- 2. NORMALIZAÇÃO (Pass-through)
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(product_id AS STRING)                        AS id_produto,
    CAST(restaurant_id AS STRING)                     AS id_restaurante,
    CAST(name AS STRING)                              AS nome_produto,
    CAST(tags AS STRING)                              AS tags_produto,
    CAST(flavor_profile AS STRING)                    AS perfil_sabor,
    CAST(cuisine_type AS STRING)                      AS tipo_cozinha,
    CAST(product_type AS STRING)                      AS tipo_produto,
    CAST(price AS DECIMAL(18, 2))                     AS preco_venda,
    CAST(unit_cost AS DECIMAL(18, 2))                 AS custo_unitario,
    CAST(calories AS INT)                             AS calorias,
    CAST(prep_time_min AS INT)                        AS tempo_preparo_min,
    CAST(is_vegetarian AS BOOLEAN)                    AS flag_vegetariano,
    CAST(is_gluten_free AS BOOLEAN)                   AS flag_gluten_free,
    CAST(created_at AS TIMESTAMP)                     AS data_criacao,
    CAST(updated_at AS TIMESTAMP)                     AS data_atualizacao
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleansed_table AS (
  SELECT
    TRIM(id_produto)                                  AS id_produto,
    TRIM(id_restaurante)                              AS id_restaurante,
    LOWER(TRIM(nome_produto))                         AS nome_produto,
    LOWER(TRIM(tipo_cozinha))                         AS tipo_cozinha,
    LOWER(TRIM(tipo_produto))                         AS tipo_produto,
    LOWER(TRIM(perfil_sabor))                         AS perfil_sabor,
    LOWER(TRIM(tags_produto))                         AS tags_produto,
    COALESCE(preco_venda, 0.00)                       AS preco_venda,
    COALESCE(custo_unitario, 0.00)                    AS custo_unitario,
    COALESCE(calorias, 0)                             AS calorias,
    COALESCE(tempo_preparo_min, 0)                    AS tempo_preparo_min,
    COALESCE(flag_vegetariano, FALSE)                 AS flag_vegetariano,
    COALESCE(flag_gluten_free, FALSE)                 AS flag_gluten_free,
    COALESCE(data_criacao, CAST('1900-01-01 00:00:00' AS TIMESTAMP)) AS data_criacao,
    COALESCE(data_atualizacao, CAST('1900-01-01 00:00:00' AS TIMESTAMP)) AS data_atualizacao
  FROM
    typed_table
),

-- 5. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                               AS _data_ingestao,
    'oracle-ubereats'                                 AS _sistema_fonte
  FROM
    cleansed_table
)

SELECT * FROM silver_table;
