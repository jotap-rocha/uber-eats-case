-- Queries de validação de integridade — Etapa 2 (Lakehouse), mesma disciplina
-- das Ondas 1/2/3 e da Fase 2/AWS: 0 órfãos entre as tabelas Iceberg do
-- BigLake materializadas pelo job Dataproc (src/gcp/dataproc_iceberg_merge).

-- 1. Contagem por tabela (smoke test pós-MERGE)
SELECT 'restaurants' AS tabela, COUNT(*) AS total FROM `biglake_iceberg.restaurants`
UNION ALL
SELECT 'orders', COUNT(*) FROM `biglake_iceberg.orders`
UNION ALL
SELECT 'perfil_restaurante', COUNT(*) FROM `biglake_iceberg.perfil_restaurante`;

-- 2. Órfãos: Pedido sem Restaurante correspondente (Oracle -> Oracle, mesma conexão)
SELECT o.order_id, o.restaurant_id
FROM `biglake_iceberg.orders` AS o
LEFT JOIN `biglake_iceberg.restaurants` AS r ON o.restaurant_id = r.restaurant_id
WHERE r.restaurant_id IS NULL;

-- 3. Órfãos: Perfil de Restaurante (MongoDB) sem Restaurante correspondente (Oracle)
--    — validação cross-connection equivalente à já feita na Onda 3 e na Fase 2/AWS.
SELECT p.restaurant_id
FROM `biglake_iceberg.perfil_restaurante` AS p
LEFT JOIN `biglake_iceberg.restaurants` AS r ON p.restaurant_id = r.restaurant_id
WHERE r.restaurant_id IS NULL;
