-- t05d_turnos_e_entregas_sem_sobreposicao: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT 'shift' AS tipo, s1.shift_id AS a, s2.shift_id AS b
FROM shifts s1 JOIN shifts s2 ON s2.driver_id = s1.driver_id AND s2.shift_id > s1.shift_id
WHERE tsrange(s1.opened_at, coalesce(s1.closed_at, 'infinity'), '[)')
   && tsrange(s2.opened_at, coalesce(s2.closed_at, 'infinity'), '[)')
UNION ALL
SELECT 'assignment', a1.delivery_id, a2.delivery_id
FROM driver_assignments a1 JOIN driver_assignments a2
  ON a2.driver_id = a1.driver_id AND (a2.delivery_id, a2.assignment_number) > (a1.delivery_id, a1.assignment_number)
WHERE tsrange(a1.assigned_at, coalesce(a1.released_at, 'infinity'), '[)')
   && tsrange(a2.assigned_at, coalesce(a2.released_at, 'infinity'), '[)');
