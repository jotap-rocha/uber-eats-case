-- t13a_item_do_incidente: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT ii.incident_id, ii.restaurant_order_id, ii.line_number
FROM incident_items ii
JOIN incidents i ON i.incident_id = ii.incident_id
LEFT JOIN restaurant_orders ro ON ro.restaurant_order_id = ii.restaurant_order_id
LEFT JOIN order_items oi ON oi.restaurant_order_id = ii.restaurant_order_id AND oi.line_number = ii.line_number
WHERE oi.restaurant_order_id IS NULL OR ro.order_id <> i.order_id OR ro.status <> 'picked_up';
