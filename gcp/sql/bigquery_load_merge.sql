-- LOAD/MERGE do BigQuery a partir do GCS/Bronze (Etapa 1, Decisão 4,
-- DESIGN_INGESTAO_GCP_FASE3.md). Padrão de referência para `restaurants`;
-- as demais tabelas (drivers, orders, payments, order_items, receipts,
-- products, inventory, perfil_restaurante) replicam o mesmo padrão, trocando
-- o prefixo do GCS e as colunas de negócio.

LOAD DATA INTO `ubereats_bronze.stg_restaurants`
FROM FILES (
  format = 'JSON',
  uris = ['gs://ubereats-fase3-bronze/oracle/restaurants/*.json']
);

MERGE `ubereats_warehouse.restaurants` AS target
USING (
  SELECT *
  FROM `ubereats_bronze.stg_restaurants`
  QUALIFY ROW_NUMBER() OVER (PARTITION BY restaurant_id ORDER BY cdc_sequence DESC) = 1
) AS source
ON target.restaurant_id = source.restaurant_id
WHEN MATCHED AND source.cdc_operation = 'DELETE' THEN DELETE
WHEN MATCHED THEN UPDATE SET
  target.name = source.name,
  target.cuisine_type = source.cuisine_type,
  target.average_rating = source.average_rating,
  target._cdc_commit_ts = source.cdc_commit_ts
WHEN NOT MATCHED AND source.cdc_operation != 'DELETE' THEN
  INSERT (restaurant_id, name, cuisine_type, average_rating, _cdc_commit_ts)
  VALUES (source.restaurant_id, source.name, source.cuisine_type, source.average_rating, source.cdc_commit_ts);
