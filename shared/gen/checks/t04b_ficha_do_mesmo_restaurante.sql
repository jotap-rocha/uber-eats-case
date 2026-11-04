-- t04b_ficha_do_mesmo_restaurante: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT pr.product_id, pr.stock_item_id
FROM product_recipes pr
LEFT JOIN products p ON p.product_id = pr.product_id
LEFT JOIN stock_items s ON s.stock_item_id = pr.stock_item_id
WHERE p.product_id IS NULL OR s.stock_item_id IS NULL OR s.restaurant_id <> p.restaurant_id
UNION ALL
SELECT p.product_id, NULL FROM products p                                  -- todo produto tem ficha (RN-37)
WHERE NOT EXISTS (SELECT 1 FROM product_recipes pr WHERE pr.product_id = p.product_id);
