-- t02b_entrega_do_pedido: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT o.order_id, o.status, d.status AS delivery_status
FROM orders o LEFT JOIN deliveries d ON d.order_id = o.order_id
WHERE d.delivery_id IS NULL
   OR (o.status = 'out_for_delivery') <> (d.status = 'in_transit')
   OR (o.status = 'cancelled') <> (d.status = 'cancelled')
   OR (o.status IN ('delivered', 'completed')) <> (d.status = 'delivered')
   OR (o.status = 'undelivered') <> (d.status = 'undelivered');
