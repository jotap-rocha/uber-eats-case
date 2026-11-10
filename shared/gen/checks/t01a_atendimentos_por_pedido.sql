-- t01a_atendimentos_por_pedido: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT o.order_id, count(ro.restaurant_order_id) AS n
FROM orders o LEFT JOIN restaurant_orders ro ON ro.order_id = o.order_id
GROUP BY o.order_id
HAVING count(ro.restaurant_order_id) NOT BETWEEN 1 AND 2;
