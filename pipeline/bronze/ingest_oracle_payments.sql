CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_payments_raw AS
SELECT
  CAST(value AS STRING) AS json_value
FROM STREAM read_kafka(
  bootstrapServers => 'redpanda:9092',
  subscribe => 'oracle.UBEREATS.PAYMENTS',
  startingOffsets => 'earliest'
);

-- =================================================================

CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_payments_pre_processed AS
SELECT
  CAST(json_value:after.PAYMENT_ID AS INT)          AS payment_id,
  CAST(json_value:after.ORDER_ID AS INT)            AS order_id,
  CAST(json_value:after.AMOUNT AS DECIMAL(18, 2))   AS amount,
  CAST(json_value:after.CURRENCY AS STRING)         AS currency,
  CAST(json_value:after.METHOD AS STRING)           AS method,
  CAST(json_value:after.PROVIDER AS STRING)         AS provider,
  CAST(json_value:after.CARD_BRAND AS STRING)       AS card_brand,
  CAST(json_value:after.CARD_LAST4 AS STRING)       AS card_last4,
  CAST(json_value:after.CARD_EXP_MONTH AS INT)      AS card_exp_month,
  CAST(json_value:after.CARD_EXP_YEAR AS INT)       AS card_exp_year,
  CAST(json_value:after.WALLET_PROVIDER AS STRING)  AS wallet_provider,
  CAST(json_value:after.STATUS AS STRING)           AS status,
  CAST(json_value:after.FAILURE_REASON AS STRING)   AS failure_reason,
  CAST(json_value:after.REFUNDED AS INT)            AS refunded,
  CAST(json_value:after.REFUND_AMOUNT AS DECIMAL(18, 2)) AS refund_amount,
  CAST(json_value:after.CAPTURED AS INT)            AS captured,
  CAST(json_value:after.CAPTURE_TIMESTAMP AS STRING) AS capture_timestamp,
  CAST(json_value:after.PLATFORM_FEE AS DECIMAL(18, 2)) AS platform_fee,
  CAST(json_value:after.PROVIDER_FEE AS DECIMAL(18, 2)) AS provider_fee,
  CAST(json_value:after.TAX_AMOUNT AS DECIMAL(18, 2))   AS tax_amount,
  CAST(json_value:after.NET_AMOUNT AS DECIMAL(18, 2))   AS net_amount,
  CAST(json_value:after.RECEIPT_URL AS STRING)      AS receipt_url,
  CAST(json_value:after.INVOICE_ID AS STRING)       AS invoice_id,
  CAST(json_value:after.COUNTRY AS STRING)          AS country,
  CAST(json_value:after.IP_ADDRESS AS STRING)       AS ip_address,
  CAST(json_value:after.USER_AGENT AS STRING)       AS user_agent,
  CAST(json_value:after.TXN_TIMESTAMP AS STRING)    AS txn_timestamp,
  CAST(json_value:op AS STRING)                     AS cdc_operation,
  CAST(CAST(json_value:source.ts_ms AS BIGINT) / 1000 AS TIMESTAMP) AS cdc_commit_ts,
  CAST(json_value:source.scn AS STRING)             AS cdc_sequence,
  'oracle-ubereats'                                 AS cdc_source_system,
  current_timestamp()                               AS _datetime_ingestion
FROM
  STREAM(live.view_oracle_payments_raw)
WHERE
  json_value:after IS NOT NULL OR json_value:op = 'd';

-- =================================================================

CREATE OR REFRESH STREAMING TABLE ods_payments
COMMENT "ODS de pagamentos. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 3) — antes kafka/payments simulado no MinIO, sem mutacao de status.";
APPLY CHANGES INTO
  uber_eats.bronze.ods_payments
FROM
  STREAM(live.view_oracle_payments_pre_processed)
KEYS(payment_id)
APPLY AS DELETE WHEN cdc_operation = 'd'
SEQUENCE BY cdc_sequence
STORED AS SCD TYPE 1;
