-- Redshift Serverless — COPY/MERGE a partir do S3/Bronze (Etapa 1, item 8).
-- Mesmo padrão da Fase 1 (Synapse COPY INTO do ADLS Gen2): Redshift nunca recebe
-- target DMS nativo, só lê do S3 (Decisão 2, DESIGN_INGESTAO_AWS_FASE2.md).
--
-- Projeta as 4 colunas canônicas de CDC (docs/data-contract-cdc-aws-dms.md) desde
-- o staging, para o MERGE não depender do formato nativo do DMS.

-- ---------------------------------------------------------------------------
-- Staging: 1 tabela por entidade, schema espelhando o S3/Bronze + colunas canônicas
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS staging.stg_drivers (
    driver_id           BIGINT,
    name                VARCHAR(256),
    status              VARCHAR(32),
    total_deliveries    INT,
    total_earnings      DECIMAL(12, 2),
    average_rating      DECIMAL(3, 2),
    cdc_operation       CHAR(1),      -- I/U/D (coluna Op do DMS S3 target)
    cdc_commit_ts       TIMESTAMP,
    cdc_sequence        VARCHAR(64),  -- transaction_id + transaction_record_id combinados
    cdc_source_system   VARCHAR(32)
);

COPY staging.stg_drivers
FROM 's3://{{BRONZE_BUCKET}}/postgres/drivers/'
IAM_ROLE '{{REDSHIFT_S3_READ_ROLE_ARN}}'
FORMAT AS PARQUET;

-- MERGE (upsert por chave, mais recente por cdc_sequence — evita que um evento
-- fora de ordem sobrescreva um mais novo).
MERGE INTO warehouse.dim_drivers AS target
USING (
    SELECT *
    FROM staging.stg_drivers
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY driver_id ORDER BY cdc_sequence DESC
    ) = 1
) AS source
ON target.driver_id = source.driver_id
WHEN MATCHED AND source.cdc_operation = 'D' THEN DELETE
WHEN MATCHED THEN UPDATE SET
    status = source.status,
    total_deliveries = source.total_deliveries,
    total_earnings = source.total_earnings,
    average_rating = source.average_rating
WHEN NOT MATCHED AND source.cdc_operation != 'D' THEN INSERT (
    driver_id, name, status, total_deliveries, total_earnings, average_rating
) VALUES (
    source.driver_id, source.name, source.status,
    source.total_deliveries, source.total_earnings, source.average_rating
);

-- Repetir o mesmo padrão (staging + COPY + MERGE) para as demais entidades de
-- Postgres/Oracle/MongoDB no /build — este arquivo documenta o padrão de referência,
-- não a lista exaustiva de todas as tabelas do modelo conceitual.
