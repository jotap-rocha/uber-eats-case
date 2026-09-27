CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_receipts
COMMENT "Tabela de recibos com dados padronizados, tipados e limpos. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 3) — antes kafka/receipts simulado no MinIO."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.ods_receipts)
),

-- 2. NORMALIZAÇÃO
-- Neste caso, os dados já vieram normalizados
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(order_id AS STRING)                                  AS id_pedido,
    CAST(payment_id AS STRING)                                AS id_pagamento,
    CAST(receipt_id AS STRING)                                AS id_recibo,
    CAST(item_count AS INT)                                   AS quantidade_itens,
    CAST(total_amount AS DECIMAL(18, 2))                      AS valor_bruto,
    CAST(receipt_generated_at AS TIMESTAMP)                   AS data_geracao_recibo
  FROM
    normalized_table
),

-- 4. LIMPEZA

cleared_table AS (
  SELECT
    TRIM(id_pedido)                                                 AS id_pedido,
    TRIM(id_pagamento)                                              AS id_pagamento,
    TRIM(id_recibo)                                                 AS id_recibo,
    COALESCE(quantidade_itens, 0)                                   AS quantidade_itens,
    COALESCE(valor_bruto, 0)                                        AS valor_bruto,
    COALESCE(data_geracao_recibo, CAST('1900-01-01' AS TIMESTAMP))  AS data_geracao_recibo
  FROM
    typed_table
),

-- 5. METADATA
silver_table AS (
  SELECT
    *,
    current_timestamp()                                             AS _data_ingestao,
    'oracle-ubereats'                                               AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table
