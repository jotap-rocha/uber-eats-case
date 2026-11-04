-- t03c_transicoes_permitidas_atendimento: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT t.restaurant_order_id, t.sequence_number, t.from_status, t.to_status
FROM restaurant_order_status_transitions t
WHERE t.from_status IS NOT NULL
  AND (t.from_status, t.to_status) NOT IN (VALUES
    ('in_analysis', 'accepted'), ('in_analysis', 'rejected'), ('in_analysis', 'cancelled'),
    ('accepted', 'preparing'), ('accepted', 'cancelled'), ('preparing', 'cancelled'),
    ('preparing', 'ready_for_pickup'), ('ready_for_pickup', 'picked_up'));
