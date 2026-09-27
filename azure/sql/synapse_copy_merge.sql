-- Padrao de referencia (tabela orders) -- demais tabelas (drivers, users,
-- restaurants, products, inventory, payments, order_items, receipts,
-- perfil_restaurante) replicam a mesma estrutura: staging + COPY INTO +
-- MERGE dedupe por cdc_sequence. Fonte: ADLS Gen2/Bronze, alimentado pelo
-- Kafka Connect Sink Connector (Postgres/Oracle) e pelo Airbyte
-- (MongoDB/MinIO) -- ver DESIGN, Decisao 1.

CREATE TABLE staging.stg_orders
WITH (DISTRIBUTION = ROUND_ROBIN, HEAP)
AS
SELECT TOP 0 * FROM warehouse.orders;

COPY INTO staging.stg_orders
FROM 'https://ubereatsfase1bronze.dfs.core.windows.net/bronze/oracle/oracle.UBEREATS.ORDERS/'
WITH (
    FILE_TYPE = 'JSON',
    CREDENTIAL = (IDENTITY = 'Managed Identity')
);

MERGE INTO warehouse.orders AS target
USING (
    SELECT *
    FROM staging.stg_orders
    QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY cdc_sequence DESC) = 1
) AS source
ON target.order_id = source.order_id
WHEN MATCHED AND source.cdc_operation = 'd' THEN DELETE
WHEN MATCHED THEN UPDATE SET
    target.status           = source.status,
    target.total_amount     = source.total_amount,
    target._cdc_commit_ts   = source.cdc_commit_ts,
    target._cdc_sequence    = source.cdc_sequence
WHEN NOT MATCHED AND source.cdc_operation != 'd' THEN
    INSERT (order_id, user_id, restaurant_id, driver_id, status, total_amount, _cdc_commit_ts, _cdc_sequence)
    VALUES (source.order_id, source.user_id, source.restaurant_id, source.driver_id,
            source.status, source.total_amount, source.cdc_commit_ts, source.cdc_sequence);

TRUNCATE TABLE staging.stg_orders;
