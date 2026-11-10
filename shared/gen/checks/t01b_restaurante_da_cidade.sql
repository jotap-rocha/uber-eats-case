-- t01b_restaurante_da_cidade: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT ro.restaurant_order_id
FROM restaurant_orders ro
JOIN orders o ON o.order_id = ro.order_id
LEFT JOIN restaurants r ON r.restaurant_id = ro.restaurant_id
WHERE r.restaurant_id IS NULL OR r.city_id <> o.city_id;
