-- t12_janelas_pos_entrega: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT 'incident' AS origem, i.incident_id AS id
FROM incidents i JOIN deliveries d ON d.order_id = i.order_id
WHERE d.status <> 'delivered' OR i.opened_at NOT BETWEEN d.finished_at AND d.finished_at + interval '24 hours'
UNION ALL
SELECT 'driver_rating', r.delivery_id
FROM driver_ratings r JOIN deliveries d ON d.delivery_id = r.delivery_id
WHERE d.status <> 'delivered' OR r.rated_at NOT BETWEEN d.finished_at AND d.finished_at + interval '20 minutes'
UNION ALL
SELECT 'restaurant_rating', rr.restaurant_order_id
FROM restaurant_ratings rr
JOIN restaurant_orders ro ON ro.restaurant_order_id = rr.restaurant_order_id
JOIN deliveries d ON d.order_id = ro.order_id
WHERE d.status <> 'delivered' OR rr.rated_at NOT BETWEEN d.finished_at AND d.finished_at + interval '20 minutes'
UNION ALL
SELECT 'tip', t.delivery_id
FROM tips t JOIN deliveries d ON d.delivery_id = t.delivery_id
WHERE d.status <> 'delivered' OR t.paid_at NOT BETWEEN d.finished_at AND d.finished_at + interval '20 minutes';
