-- t06b_saldo_nunca_negativo_no_tempo: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT stock_item_id, stock_movement_id, saldo FROM (
  SELECT stock_item_id, stock_movement_id,
         sum(CASE movement_type WHEN 'restock' THEN quantity ELSE -quantity END)
           OVER (PARTITION BY stock_item_id ORDER BY occurred_at, stock_movement_id) AS saldo
  FROM stock_movements) x
WHERE saldo < 0;
