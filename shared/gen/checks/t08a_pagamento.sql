-- t08a_pagamento: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT p.payment_id
FROM payments p
JOIN orders o ON o.order_id = p.order_id
LEFT JOIN (SELECT payment_id, sum(gross_amount) AS bruto, sum(tax_amount) AS imposto
           FROM payment_components GROUP BY payment_id) c ON c.payment_id = p.payment_id
LEFT JOIN payment_attempts a ON a.checkout_id = p.checkout_id AND a.attempt_number = p.attempt_number
LEFT JOIN checkouts k ON k.checkout_id = p.checkout_id
WHERE c.bruto IS DISTINCT FROM p.total_amount
   OR c.imposto IS DISTINCT FROM round(p.total_amount * p.tax_rate, 2)
   OR p.payment_fee_amount <> round(p.total_amount * p.payment_fee_rate, 2)
   OR p.paid_at <> o.placed_at
   OR o.checkout_id <> p.checkout_id
   OR a.result IS DISTINCT FROM 'approved' OR a.amount <> p.total_amount
   OR k.amount IS DISTINCT FROM p.total_amount;
