-- t03d_transicoes_permitidas_pedido: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT t.order_id, t.sequence_number, t.from_status, t.to_status
FROM order_status_transitions t
WHERE t.from_status IS NOT NULL
  AND NOT (
       (t.from_status IN ('in_analysis', 'preparing', 'partially_ready', 'ready_for_pickup', 'partially_picked_up')
        AND t.to_status IN ('in_analysis', 'preparing', 'partially_ready', 'ready_for_pickup', 'partially_picked_up',
                            'out_for_delivery', 'cancelled')
        AND t.to_status <> t.from_status)
    OR (t.from_status = 'out_for_delivery' AND t.to_status IN ('delivered', 'undelivered'))
    OR (t.from_status = 'delivered' AND t.to_status = 'completed'));
