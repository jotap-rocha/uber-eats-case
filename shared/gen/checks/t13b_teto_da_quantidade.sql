-- t13b_teto_da_quantidade: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT ii.restaurant_order_id, ii.line_number, oi.quantity, sum(ii.quantity) AS reclamado
FROM incident_items ii
JOIN incidents i ON i.incident_id = ii.incident_id
JOIN order_items oi ON oi.restaurant_order_id = ii.restaurant_order_id AND oi.line_number = ii.line_number
WHERE i.status <> 'dismissed'
GROUP BY ii.restaurant_order_id, ii.line_number, oi.quantity
HAVING sum(ii.quantity) > oi.quantity;
