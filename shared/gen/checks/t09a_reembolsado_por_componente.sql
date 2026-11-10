-- t09a_reembolsado_por_componente: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT r.payment_id, rc.component_number
FROM refund_components rc
JOIN refunds r ON r.refund_id = rc.refund_id
LEFT JOIN payment_components pc ON pc.payment_id = r.payment_id AND pc.component_number = rc.component_number
GROUP BY r.payment_id, rc.component_number, pc.gross_amount, pc.tax_amount
HAVING pc.gross_amount IS NULL OR sum(rc.gross_amount) > pc.gross_amount OR sum(rc.tax_amount) > pc.tax_amount;
