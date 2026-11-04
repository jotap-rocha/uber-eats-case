-- t09c_estorno_total: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT p.payment_id, o.status
FROM orders o
JOIN payments p ON p.order_id = o.order_id
JOIN deliveries d ON d.order_id = o.order_id
LEFT JOIN (SELECT payment_id, sum(total_amount) AS devolvido FROM refunds GROUP BY payment_id) r
  ON r.payment_id = p.payment_id
WHERE (o.status = 'cancelled' OR (o.status = 'undelivered' AND d.failure_reason = 'driver_unable'))
  AND r.devolvido IS DISTINCT FROM p.total_amount;
