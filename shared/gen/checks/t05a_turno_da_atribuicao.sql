-- t05a_turno_da_atribuicao: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT a.delivery_id, a.assignment_number
FROM driver_assignments a
JOIN deliveries d ON d.delivery_id = a.delivery_id
JOIN orders o ON o.order_id = d.order_id
LEFT JOIN shifts s ON s.shift_id = a.shift_id
WHERE s.shift_id IS NULL OR s.driver_id <> a.driver_id OR s.city_id <> o.city_id
   OR a.assigned_at < s.opened_at OR a.assigned_at > coalesce(s.closed_at, 'infinity');
