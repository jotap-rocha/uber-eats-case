CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_kafka_orders
COMMENT "Tabela de pedidos da Uber com dados padronizados, tipados e enriquecidos."
AS
-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.orders)
),

-- 2. NORMALIZAÇÃO (Pass-through)
-- Neste caso, os dados já vieram normalizados
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(order_id AS STRING)                                                        AS id_pedido,
    CAST(user_key AS STRING)                                                        AS cpf_usuario,
    CAST(driver_key AS STRING)                                                      AS id_motorista,
    CAST(order_date AS TIMESTAMP)                                                   AS data_pedido,
    CAST(rating_key AS STRING)                                                      AS id_classificacao,
    CAST(payment_key AS STRING)                                                     AS id_pagamento,
    CAST(total_amount AS DECIMAL(18, 2))                                            AS valor_pedido,
    CAST(restaurant_key AS STRING)                                                  AS cnpj_restaurante
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleared_table AS (
  SELECT
    TRIM(id_pedido)                                                                 AS id_pedido,
    TRIM(cpf_usuario)                                                               AS cpf_usuario,
    TRIM(id_motorista)                                                              AS id_motorista,
    COALESCE(data_pedido, CAST('1900-01-01 00:00:00' AS TIMESTAMP))                 AS data_pedido,
    TRIM(id_classificacao)                                                          AS id_classificacao,
    TRIM(id_pagamento)                                                              AS id_pagamento,
    COALESCE(valor_pedido, 0.00)                                                    AS valor_pedido,
    TRIM(cnpj_restaurante)                                                          AS cnpj_restaurante
  FROM
    typed_table
),

-- 5. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                                                             AS _data_ingestao,
    'kafka-minio'                                                                   AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table