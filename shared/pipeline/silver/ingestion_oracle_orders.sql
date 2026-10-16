CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_orders
COMMENT "Tabela de pedidos da Uber com dados padronizados, tipados e enriquecidos. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 3) — status agora é mutação real da linha (fork+stateMachine), não mais um stream de eventos separado (kafka/status, aposentado)."
AS
-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.ods_orders)
),

-- 2. NORMALIZAÇÃO (Pass-through)
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(order_id AS STRING)                                                        AS id_pedido,
    CAST(user_id AS STRING)                                                         AS id_usuario,
    CAST(driver_id AS STRING)                                                       AS id_motorista,
    CAST(order_date AS TIMESTAMP)                                                   AS data_pedido,
    CAST(total_amount AS DECIMAL(18, 2))                                            AS valor_pedido,
    CAST(restaurant_id AS STRING)                                                   AS id_restaurante,
    CAST(status AS STRING)                                                          AS status_pedido,
    CAST(updated_at AS TIMESTAMP)                                                   AS data_atualizacao
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleared_table AS (
  SELECT
    TRIM(id_pedido)                                                                 AS id_pedido,
    TRIM(id_usuario)                                                                AS id_usuario,
    TRIM(id_motorista)                                                              AS id_motorista,
    COALESCE(data_pedido, CAST('1900-01-01 00:00:00' AS TIMESTAMP))                 AS data_pedido,
    COALESCE(valor_pedido, 0.00)                                                    AS valor_pedido,
    TRIM(id_restaurante)                                                            AS id_restaurante,
    COALESCE(status_pedido, 'Order Placed')                                         AS status_pedido,
    COALESCE(data_atualizacao, data_pedido)                                         AS data_atualizacao
  FROM
    typed_table
),

-- 5. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                                                             AS _data_ingestao,
    'oracle-ubereats'                                                               AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table
