-- t05b_desistencia: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT a.delivery_id, a.assignment_number
FROM driver_assignments a
JOIN deliveries d ON d.delivery_id = a.delivery_id
LEFT JOIN LATERAL (SELECT min(ro.picked_up_at) AS primeira_retirada
                   FROM restaurant_orders ro WHERE ro.order_id = d.order_id) f ON true
WHERE a.release_reason = 'driver_gave_up'
  AND (a.assignment_number >= 4 OR a.released_at > f.primeira_retirada);
