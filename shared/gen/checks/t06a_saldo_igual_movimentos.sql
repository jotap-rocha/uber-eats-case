-- t06a_saldo_igual_movimentos: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT s.stock_item_id, s.quantity_on_hand, coalesce(m.saldo, 0) AS saldo
FROM stock_items s
LEFT JOIN (SELECT stock_item_id,
                  sum(CASE movement_type WHEN 'restock' THEN quantity ELSE -quantity END) AS saldo
           FROM stock_movements GROUP BY stock_item_id) m ON m.stock_item_id = s.stock_item_id
WHERE s.quantity_on_hand <> coalesce(m.saldo, 0);
