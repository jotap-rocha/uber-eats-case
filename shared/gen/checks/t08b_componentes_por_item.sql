-- t08b_componentes_por_item: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
WITH itens AS (
  SELECT ro.order_id, oi.restaurant_order_id, oi.line_number, oi.total_amount
  FROM order_items oi JOIN restaurant_orders ro ON ro.restaurant_order_id = oi.restaurant_order_id
)
SELECT p.payment_id, i.restaurant_order_id, i.line_number
FROM payments p JOIN itens i ON i.order_id = p.order_id
LEFT JOIN payment_components ci ON ci.payment_id = p.payment_id AND ci.component_type = 'item'
  AND ci.restaurant_order_id = i.restaurant_order_id AND ci.line_number = i.line_number
LEFT JOIN payment_components cs ON cs.payment_id = p.payment_id AND cs.component_type = 'service_fee'
  AND cs.restaurant_order_id = i.restaurant_order_id AND cs.line_number = i.line_number
WHERE ci.gross_amount IS DISTINCT FROM i.total_amount OR cs.payment_id IS NULL;
