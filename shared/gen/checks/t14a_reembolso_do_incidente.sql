-- t14a_reembolso_do_incidente: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT i.incident_id, i.status
FROM incidents i LEFT JOIN refunds r ON r.incident_id = i.incident_id
WHERE (i.status = 'upheld') <> (r.refund_id IS NOT NULL)
   OR r.refunded_at <> i.decided_at;
