-- t07a_prazo_prometido: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
WITH a AS (
  SELECT order_id,
         count(*) FILTER (WHERE status NOT IN ('cancelled', 'rejected')) AS ativos,
         count(*) FILTER (WHERE status = 'in_analysis')                  AS em_analise,
         max(accepted_at) FILTER (WHERE status NOT IN ('cancelled', 'rejected')) AS ultimo_aceite
  FROM restaurant_orders GROUP BY order_id
)
SELECT d.delivery_id, d.promised_at, a.ativos, a.em_analise
FROM deliveries d JOIN a ON a.order_id = d.order_id
WHERE (a.ativos > 0 AND a.em_analise = 0 AND d.promised_at IS NULL)
   OR (a.em_analise > 0 AND d.promised_at IS NOT NULL)
   OR (d.promised_at < a.ultimo_aceite);
