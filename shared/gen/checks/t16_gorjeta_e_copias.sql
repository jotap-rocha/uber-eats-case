-- t16_gorjeta_e_copias: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT 'tip_depois_de_nota_baixa' AS caso, t.delivery_id AS id
FROM tips t JOIN driver_ratings r ON r.delivery_id = t.delivery_id
WHERE r.rating <= 3 AND t.paid_at >= r.rated_at
UNION ALL
SELECT 'driver_rating_copia', r.delivery_id
FROM driver_ratings r
JOIN deliveries d ON d.delivery_id = r.delivery_id
JOIN orders o ON o.order_id = d.order_id
LEFT JOIN driver_assignments a ON a.delivery_id = r.delivery_id AND a.release_reason = 'delivery_finished'
WHERE a.driver_id IS DISTINCT FROM r.driver_id OR o.customer_id <> r.customer_id
UNION ALL
SELECT 'restaurant_rating_copia', rr.restaurant_order_id
FROM restaurant_ratings rr
JOIN restaurant_orders ro ON ro.restaurant_order_id = rr.restaurant_order_id
JOIN orders o ON o.order_id = ro.order_id
WHERE ro.restaurant_id <> rr.restaurant_id OR o.customer_id <> rr.customer_id
UNION ALL
SELECT 'incident_copia', i.incident_id
FROM incidents i JOIN orders o ON o.order_id = i.order_id
WHERE o.customer_id <> i.customer_id;
