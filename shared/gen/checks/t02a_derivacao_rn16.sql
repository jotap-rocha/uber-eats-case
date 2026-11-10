-- t02a_derivacao_rn16: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
WITH a AS (
  SELECT order_id,
         count(*) FILTER (WHERE status NOT IN ('cancelled', 'rejected')) AS ativos,
         count(*) FILTER (WHERE status = 'picked_up')                    AS retirados,
         count(*) FILTER (WHERE status = 'ready_for_pickup')             AS prontos,
         count(*) FILTER (WHERE status = 'in_analysis')                  AS em_analise
  FROM restaurant_orders GROUP BY order_id
), d AS (
  SELECT o.order_id, o.status,
         CASE WHEN a.ativos = 0                THEN 'cancelled'
              WHEN a.retirados = a.ativos      THEN 'out_for_delivery'
              WHEN a.retirados > 0             THEN 'partially_picked_up'
              WHEN a.prontos = a.ativos        THEN 'ready_for_pickup'
              WHEN a.prontos > 0               THEN 'partially_ready'
              WHEN a.em_analise > 0            THEN 'in_analysis'
              ELSE 'preparing' END AS derivado
  FROM orders o JOIN a ON a.order_id = o.order_id
)
SELECT * FROM d
WHERE (status NOT IN ('delivered', 'completed', 'undelivered') AND status <> derivado)
   OR (status IN ('delivered', 'completed', 'undelivered') AND derivado <> 'out_for_delivery');
