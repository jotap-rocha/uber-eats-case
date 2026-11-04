-- t03e_status_igual_ultima_transicao: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT o.order_id, o.status, l.to_status
FROM orders o
LEFT JOIN LATERAL (SELECT t.to_status FROM order_status_transitions t
                   WHERE t.order_id = o.order_id ORDER BY t.sequence_number DESC LIMIT 1) l ON true
WHERE l.to_status IS DISTINCT FROM o.status
UNION ALL
SELECT ro.restaurant_order_id, ro.status, l.to_status
FROM restaurant_orders ro
LEFT JOIN LATERAL (SELECT t.to_status FROM restaurant_order_status_transitions t
                   WHERE t.restaurant_order_id = ro.restaurant_order_id ORDER BY t.sequence_number DESC LIMIT 1) l ON true
WHERE l.to_status IS DISTINCT FROM ro.status;
