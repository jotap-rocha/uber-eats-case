-- t10_copias_e_valores_dos_repasses: devolve as linhas que violam o invariante; passa com 0 linhas (F5.9 do modelo físico).
-- Roda com search_path = ubereats.
SELECT 'restaurant_payout' AS tabela, rp.restaurant_order_id AS id
FROM restaurant_payouts rp
LEFT JOIN restaurant_orders ro ON ro.restaurant_order_id = rp.restaurant_order_id
LEFT JOIN (SELECT restaurant_order_id, sum(total_amount) AS itens FROM order_items GROUP BY restaurant_order_id) i
  ON i.restaurant_order_id = rp.restaurant_order_id
WHERE ro.restaurant_id IS DISTINCT FROM rp.restaurant_id
   OR i.itens IS DISTINCT FROM rp.items_amount
   OR rp.commission_amount <> round(rp.items_amount * rp.commission_rate, 2)
UNION ALL
SELECT 'driver_payout', dp.delivery_id
FROM driver_payouts dp
JOIN deliveries d ON d.delivery_id = dp.delivery_id
JOIN payments p ON p.order_id = d.order_id
LEFT JOIN payment_components pc ON pc.payment_id = p.payment_id AND pc.component_type = 'delivery_fee'
LEFT JOIN driver_assignments a ON a.delivery_id = dp.delivery_id AND a.release_reason = 'delivery_finished'
WHERE a.driver_id IS DISTINCT FROM dp.driver_id OR a.shift_id IS DISTINCT FROM dp.shift_id
   OR pc.gross_amount IS DISTINCT FROM dp.delivery_fee_amount
   OR dp.payout_amount <> round(dp.delivery_fee_amount * dp.driver_share_rate, 2)
UNION ALL
SELECT 'tip', t.delivery_id
FROM tips t
LEFT JOIN driver_assignments a ON a.delivery_id = t.delivery_id AND a.release_reason = 'delivery_finished'
WHERE a.driver_id IS DISTINCT FROM t.driver_id;
