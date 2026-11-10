-- t08c_taxas_do_pagamento: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT p.payment_id
FROM payments p
LEFT JOIN (SELECT payment_id,
                  sum(gross_amount) FILTER (WHERE component_type = 'item')         AS itens,
                  sum(gross_amount) FILTER (WHERE component_type = 'service_fee')  AS servico,
                  count(*)          FILTER (WHERE component_type = 'delivery_fee') AS entregas
           FROM payment_components GROUP BY payment_id) c ON c.payment_id = p.payment_id
WHERE c.entregas IS DISTINCT FROM 1
   OR c.servico IS DISTINCT FROM round(c.itens * p.service_fee_rate, 2);
