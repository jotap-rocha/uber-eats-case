-- t15_atraso_procedente: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT i.incident_id
FROM incidents i JOIN deliveries d ON d.order_id = i.order_id
WHERE i.reason = 'late_delivery' AND i.status = 'upheld'
  AND (d.promised_at IS NULL OR d.finished_at <= d.promised_at);
