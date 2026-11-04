-- t14b_quantidade_reembolsada: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT r.refund_id, rc.component_number
FROM refunds r
JOIN refund_components rc ON rc.refund_id = r.refund_id
JOIN payment_components pc ON pc.payment_id = r.payment_id AND pc.component_number = rc.component_number
LEFT JOIN incident_items ii ON ii.incident_id = r.incident_id
  AND ii.restaurant_order_id = pc.restaurant_order_id AND ii.line_number = pc.line_number
WHERE r.origin_type = 'incident' AND pc.component_type = 'item'
  AND rc.quantity IS DISTINCT FROM ii.quantity;
