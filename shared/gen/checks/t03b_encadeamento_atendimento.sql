-- t03b_encadeamento_atendimento: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT t.restaurant_order_id, t.sequence_number
FROM restaurant_order_status_transitions t
LEFT JOIN restaurant_order_status_transitions p
  ON p.restaurant_order_id = t.restaurant_order_id AND p.sequence_number = t.sequence_number - 1
WHERE t.sequence_number > 1
  AND (p.restaurant_order_id IS NULL OR t.from_status IS DISTINCT FROM p.to_status OR t.occurred_at < p.occurred_at);
