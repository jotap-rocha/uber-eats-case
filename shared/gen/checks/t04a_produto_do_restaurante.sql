-- t04a_produto_do_restaurante: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT oi.restaurant_order_id, oi.line_number
FROM order_items oi
JOIN restaurant_orders ro ON ro.restaurant_order_id = oi.restaurant_order_id
LEFT JOIN products p ON p.product_id = oi.product_id
WHERE p.product_id IS NULL OR p.restaurant_id <> ro.restaurant_id;
