-- t05c_motorista_nao_volta: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT delivery_id, driver_id FROM driver_assignments
GROUP BY delivery_id, driver_id HAVING count(*) > 1;
