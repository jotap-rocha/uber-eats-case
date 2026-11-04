-- t07b_aceite_registrado_no_cancelado: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT ro.restaurant_order_id
FROM restaurant_orders ro
WHERE ro.accepted_at IS NULL
  AND EXISTS (SELECT 1 FROM restaurant_order_status_transitions t
              WHERE t.restaurant_order_id = ro.restaurant_order_id AND t.to_status = 'accepted');
