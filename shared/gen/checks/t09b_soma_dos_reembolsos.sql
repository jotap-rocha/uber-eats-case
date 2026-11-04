-- t09b_soma_dos_reembolsos: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT 'refund' AS nivel, r.refund_id AS id
FROM refunds r
LEFT JOIN (SELECT refund_id, sum(gross_amount) AS bruto FROM refund_components GROUP BY refund_id) c
  ON c.refund_id = r.refund_id
WHERE c.bruto IS DISTINCT FROM r.total_amount
UNION ALL
SELECT 'payment', p.payment_id
FROM payments p JOIN refunds r ON r.payment_id = p.payment_id
GROUP BY p.payment_id, p.total_amount HAVING sum(r.total_amount) > p.total_amount;
