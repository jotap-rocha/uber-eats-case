-- Athena — Glue Catalog + Iceberg sobre o S3/Bronze (Etapa 2, item 11).
-- Zero ingestão nova: mesma Bronze já populada na Etapa 1 (Decisão 2 do DESIGN).

-- ---------------------------------------------------------------------------
-- DDL: tabela Iceberg explícita (o crawler do Glue gera schema Hive por padrão;
-- Iceberg exige CREATE TABLE explícito com TBLPROPERTIES).
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS bronze.drivers (
    driver_id           bigint,
    name                string,
    status              string,
    total_deliveries    int,
    total_earnings      decimal(12, 2),
    average_rating      decimal(3, 2),
    cdc_operation       string,
    cdc_commit_ts       timestamp,
    cdc_sequence        string,
    cdc_source_system   string
)
LOCATION 's3://{{BRONZE_BUCKET}}/postgres/drivers/'
TBLPROPERTIES (
    'table_type' = 'ICEBERG',
    'format' = 'parquet'
);

-- Repetir para as demais entidades no /build.

-- ---------------------------------------------------------------------------
-- Validação de integridade — mesma disciplina das Ondas 1/2/3: 0 registros órfãos
-- em joins entre entidades relacionadas (ex. Item de Pedido -> Pedido).
-- ---------------------------------------------------------------------------

SELECT COUNT(*) AS orphan_order_items
FROM bronze.order_items oi
LEFT JOIN bronze.orders o ON oi.order_id = o.order_id
WHERE o.order_id IS NULL
  AND oi.cdc_operation != 'D';

-- ---------------------------------------------------------------------------
-- Validação da cópia do MongoDB usada pelo lookup do consumidor do Kappa
-- (Decisão 4 do DESIGN) — confirma que todo restaurant_id referenciado por um
-- Pedido tem perfil correspondente antes de considerar o lookup confiável.
-- ---------------------------------------------------------------------------

SELECT COUNT(*) AS orders_sem_perfil_restaurante
FROM bronze.orders o
LEFT JOIN bronze.perfil_restaurante pr ON o.restaurant_id = pr.restaurant_id
WHERE pr.restaurant_id IS NULL;
