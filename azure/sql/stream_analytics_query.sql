-- Query do job Stream Analytics (Etapa 4). Le os 3 inputs de stream
-- (Postgres/Oracle/MinIO, todos do Event Hub), enriquece eventos de Pedido
-- via reference data input do MongoDB (Decisao 6 do DESIGN), e projeta o
-- resultado unificado com as colunas canonicas de CDC ja usadas desde a
-- Onda 3 -- ver docs/data-contract-cdc-azure.md.

WITH postgres_events AS (
    SELECT
        after.driver_id AS entity_id,
        'postgres' AS cdc_source_system,
        op AS cdc_operation,
        source.ts_ms AS cdc_commit_ts,
        source.lsn AS cdc_sequence,
        after AS payload
    FROM [postgres-input]
),
oracle_events AS (
    SELECT
        after.ORDER_ID AS entity_id,
        'oracle' AS cdc_source_system,
        op AS cdc_operation,
        source.ts_ms AS cdc_commit_ts,
        source.scn AS cdc_sequence,
        after AS payload
    FROM [oracle-input]
),
minio_events AS (
    SELECT
        [key] AS entity_id,
        'minio' AS cdc_source_system,
        event_name AS cdc_operation,
        System.Timestamp() AS cdc_commit_ts,
        CAST(NULL AS nvarchar(max)) AS cdc_sequence,
        [key] AS payload
    FROM [minio-input]
),
unified AS (
    SELECT * FROM postgres_events
    UNION ALL
    SELECT * FROM oracle_events
    UNION ALL
    SELECT * FROM minio_events
)

SELECT
    unified.entity_id,
    unified.cdc_source_system,
    unified.cdc_operation,
    unified.cdc_commit_ts,
    unified.cdc_sequence,
    unified.payload,
    refdata.menu AS restaurante_menu,
    refdata.horarios AS restaurante_horarios
INTO [enriched-output-placeholder]
FROM unified
LEFT JOIN [mongodb-perfil-restaurante-refdata] AS refdata
    ON unified.payload.restaurant_id = refdata.restaurant_id
