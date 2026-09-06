CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_payments
COMMENT "Tabela de pagamentos realizados na plataforma com dados padronizados, tipados e enriquecidos."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.payments)
),

-- 2. NORMALIZAÇÃO
-- Neste caso, os dados já vieram normalizados
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(payment_id AS STRING)                                                                    AS id_pagamento,
    CAST(order_key AS STRING)                                                                     AS id_pedido,
    CAST(invoice_id AS STRING)                                                                    AS id_fatura,
    CAST(amount AS DECIMAL(18, 2))                                                                AS valor_bruto,
    CAST(net_amount AS DECIMAL(18, 2))                                                            AS valor_liquido,
    CAST(tax_amount AS DECIMAL(18, 2))                                                            AS valor_imposto,
    CAST(platform_fee AS DECIMAL(18, 2))                                                          AS taxa_plataforma,
    CAST(provider_fee AS DECIMAL(18, 2))                                                          AS taxa_provedor_cartao,
    CAST(refund_amount AS DECIMAL(18, 2))                                                         AS valor_estornado,
    CAST(method AS STRING)                                                                        AS metodo_pagamento,
    CAST(status AS STRING)                                                                        AS status_pagamento,
    CAST(provider AS STRING)                                                                      AS provedora_cartao,
    CAST(card_brand AS STRING)                                                                    AS bandeira_cartao,
    CAST(card_last4 AS STRING)                                                                    AS ultimos_4_digitos_cartao,
    CAST(wallet_provider AS STRING)                                                               AS carteira_digital,
    CAST(from_unixtime(timestamp / 1000) AS TIMESTAMP)                                            AS data_transacao,
    CAST(card_exp_month AS INT)                                                                   AS mes_expiracao_cartao,
    CAST(card_exp_year AS INT)                                                                    AS ano_expiracao_cartao,
    CAST(captured AS BOOLEAN)                                                                     AS flag_capturado,
    CAST(refunded AS BOOLEAN)                                                                     AS flag_estornado,
    CAST(country AS STRING)                                                                       AS pais_origem,
    CAST(currency AS STRING)                                                                      AS moeda,
    CAST(ip_address AS STRING)                                                                    AS endereco_ip_origem,
    CAST(failure_reason AS STRING)                                                                AS motivo_falha
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleared_table AS (
  SELECT
    TRIM(id_pagamento)                                                                            AS id_pagamento,
    TRIM(id_pedido)                                                                               AS id_pedido,
    TRIM(id_fatura)                                                                               AS id_fatura,
    COALESCE(valor_bruto, 0.00)                                                                   AS valor_bruto,
    COALESCE(valor_liquido, 0.00)                                                                 AS valor_liquido,
    COALESCE(valor_imposto, 0.00)                                                                 AS valor_imposto,
    COALESCE(taxa_plataforma, 0.00)                                                               AS taxa_plataforma,
    COALESCE(taxa_provedor_cartao, 0.00)                                                          AS taxa_provedor_cartao,
    COALESCE(valor_estornado, 0.00)                                                               AS valor_estornado,
    LOWER(TRIM(status_pagamento))                                                                 AS status_pagamento,
    LOWER(TRIM(metodo_pagamento))                                                                 AS metodo_pagamento,
    LOWER(TRIM(bandeira_cartao))                                                                  AS bandeira_cartao,
    LOWER(TRIM(moeda))                                                                            AS moeda,
    COALESCE(data_transacao, CAST('1900-01-01 00:00:00' AS TIMESTAMP))                            AS data_transacao,
    COALESCE(mes_expiracao_cartao, 0)                                                             AS mes_expiracao_cartao,
    COALESCE(ano_expiracao_cartao, 0)                                                             AS ano_expiracao_cartao,
    COALESCE(flag_capturado, FALSE)                                                               AS flag_capturado,
    COALESCE(flag_estornado, FALSE)                                                               AS flag_estornado,
    LOWER(TRIM(pais_origem))                                                                      AS pais_origem,
    LOWER(TRIM(endereco_ip_origem))                                                               AS endereco_ip_origem,
    LOWER(TRIM(provedora_cartao))                                                                 AS provedora_cartao,
    LOWER(TRIM(ultimos_4_digitos_cartao))                                                         AS ultimos_4_digitos_cartao,
    LOWER(TRIM(carteira_digital))                                                                 AS carteira_digital,
    LOWER(TRIM(motivo_falha))                                                                     AS motivo_falha
  FROM
    typed_table
),

-- 5. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                                                                           AS _data_ingestao,
    'kafka-minio'                                                                                 AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table