-- t03a_encadeamento_pedido: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT t.order_id, t.sequence_number
FROM order_status_transitions t
LEFT JOIN order_status_transitions p
  ON p.order_id = t.order_id AND p.sequence_number = t.sequence_number - 1
WHERE t.sequence_number > 1
  AND (p.order_id IS NULL OR t.from_status IS DISTINCT FROM p.to_status OR t.occurred_at < p.occurred_at);
