-- t04d_baixa_igual_ficha_vezes_quantidade: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
WITH esperado AS (
  SELECT oi.restaurant_order_id, pr.stock_item_id, sum(pr.quantity * oi.quantity) AS qtd
  FROM order_items oi JOIN product_recipes pr ON pr.product_id = oi.product_id
  WHERE EXISTS (SELECT 1 FROM restaurant_order_status_transitions t
                WHERE t.restaurant_order_id = oi.restaurant_order_id AND t.to_status = 'preparing')
  GROUP BY oi.restaurant_order_id, pr.stock_item_id
), gravado AS (
  SELECT restaurant_order_id, stock_item_id, quantity AS qtd
  FROM stock_movements WHERE movement_type = 'consumption'
)
SELECT coalesce(e.restaurant_order_id, g.restaurant_order_id) AS restaurant_order_id,
       coalesce(e.stock_item_id, g.stock_item_id) AS stock_item_id, e.qtd AS esperado, g.qtd AS gravado
FROM esperado e FULL JOIN gravado g
  ON g.restaurant_order_id = e.restaurant_order_id AND g.stock_item_id = e.stock_item_id
WHERE e.qtd IS DISTINCT FROM g.qtd;
