-- t04c_baixa_do_mesmo_restaurante: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT m.stock_movement_id
FROM stock_movements m
JOIN stock_items s ON s.stock_item_id = m.stock_item_id
JOIN restaurant_orders ro ON ro.restaurant_order_id = m.restaurant_order_id
WHERE s.restaurant_id <> ro.restaurant_id;
