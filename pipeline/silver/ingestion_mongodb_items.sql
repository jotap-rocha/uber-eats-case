CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_mongodb_items
COMMENT "Tabela de detalhes dos pedidos feitos no app, com dados padronizados, tipados e limpos."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.mongodb_items)
),

-- 2. NORMALIZAÇÃO (Pass-through)
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(order_item_id AS STRING)                     AS id_item_pedido,
    CAST(order_id AS STRING)                          AS id_pedido,
    CAST(product_id AS STRING)                        AS id_produto,
    CAST(restaurant_id AS STRING)                     AS id_restaurante,
    CAST(product_name AS STRING)                      AS nome_produto,
    CAST(product_type AS STRING)                      AS tipo_produto,
    CAST(cuisine_type AS STRING)                      AS tipo_cozinha,
    CAST(modifiers AS STRING)                         AS modificadores,
    CAST(unit_price AS DECIMAL(18, 2))                AS preco_unitario,
    CAST(subtotal AS DECIMAL(18, 2))                  AS valor_subtotal,
    CAST(discount_applied AS DECIMAL(18, 2))          AS desconto_aplicado,
    CAST(quantity AS INT)                             AS quantidade,
    CAST(is_combo AS BOOLEAN)                         AS flag_combo,
    CAST(is_vegetarian AS BOOLEAN)                    AS flag_vegetariano,
    CAST(dt_current_timestamp AS TIMESTAMP)           AS data_registro
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleared_table AS (
  SELECT
    TRIM(id_item_pedido)                              AS id_item_pedido,
    TRIM(id_pedido)                                   AS id_pedido,
    TRIM(id_produto)                                  AS id_produto,
    TRIM(id_restaurante)                              AS id_restaurante,
    LOWER(TRIM(nome_produto))                         AS nome_produto,
    LOWER(TRIM(tipo_produto))                         AS tipo_produto,
    LOWER(TRIM(tipo_cozinha))                         AS tipo_cozinha,
    LOWER(TRIM(modificadores))                        AS modificadores,
    COALESCE(preco_unitario, 0.00)                    AS preco_unitario,
    COALESCE(valor_subtotal, 0.00)                    AS valor_subtotal,
    COALESCE(desconto_aplicado, 0.00)                 AS desconto_aplicado,
    COALESCE(quantidade, 0)                           AS quantidade,
    COALESCE(flag_combo, FALSE)                       AS flag_combo,
    COALESCE(flag_vegetariano, FALSE)                 AS flag_vegetariano,
    COALESCE(data_registro, CAST('1900-01-01 00:00:00' AS TIMESTAMP)) AS data_registro
  FROM
    typed_table
),

-- 5. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                                   AS _data_ingestao,
    'mongodb-minio'                                       AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table;