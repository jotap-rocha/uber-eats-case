CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_kafka_events
COMMENT "Tabela de eventos de pedidos normalizada com tratamentos e limpeza na base."
AS
--1. LEITURA STREAMING
WITH bronze_read AS (
  SELECT * FROM STREAM(live.events)
),

-- 2. NORMALIZAÇÃO
normalized AS (
  SELECT
    *,
    get_json_object(event, '$.event_name') AS event_name,
    get_json_object(event, '$.timestamp') AS event_timestamp
  FROM bronze_read
),

-- 3. RENOMEAÇÃO, TIPAGEM E DROP
typed AS (
  SELECT
    event_id AS id_evento,
    payment_id AS id_pagamento,
    CAST(event_name AS STRING) AS tipo_evento,
    CAST(from_unixtime(event_timestamp / 1000) AS timestamp) AS data_evento
  FROM normalized
),

-- 4. LIMPEZA
cleansed AS (
  SELECT
    TRIM(id_evento) AS id_evento,
    TRIM(id_pagamento) AS id_pagamento,
    coalesce(LOWER(TRIM(tipo_evento)), "N/A") AS tipo_evento,
    coalesce(data_evento, CAST('1900-01-01 00:00:00' AS timestamp)) AS data_evento
  FROM typed
),

-- 5. Adição de metadados
silver_table AS (
  SELECT
    *,
    current_timestamp() AS _data_ingestao,
    'kafka-minio' AS _sistema_fonte
  FROM cleansed
)

SELECT * FROM silver_table;