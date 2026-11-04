-- t11_repasse_so_quando_devido: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT 'restaurant_payout_indevido' AS caso, rp.restaurant_order_id AS id
FROM restaurant_payouts rp JOIN restaurant_orders ro ON ro.restaurant_order_id = rp.restaurant_order_id
WHERE ro.status <> 'picked_up'
UNION ALL
SELECT 'restaurant_payout_faltando', ro.restaurant_order_id
FROM restaurant_orders ro
WHERE ro.status = 'picked_up'
  AND NOT EXISTS (SELECT 1 FROM restaurant_payouts rp WHERE rp.restaurant_order_id = ro.restaurant_order_id)
UNION ALL
SELECT CASE WHEN dp.delivery_id IS NULL THEN 'driver_payout_faltando' ELSE 'driver_payout_indevido' END,
       coalesce(dp.delivery_id, d.delivery_id)
FROM deliveries d FULL JOIN driver_payouts dp ON dp.delivery_id = d.delivery_id
WHERE (dp.delivery_id IS NOT NULL)
   <> (d.status = 'delivered' OR (d.status = 'undelivered' AND d.failure_reason = 'customer_absent'))
UNION ALL
SELECT 'tip_indevida', t.delivery_id
FROM tips t JOIN deliveries d ON d.delivery_id = t.delivery_id
WHERE d.status <> 'delivered';
