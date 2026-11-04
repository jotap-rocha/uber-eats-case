-- Gerado a partir de shared/docs/modelagem/04-modelo-fisico.md (F1.5). Roda uma vez, no init do volume.

SET search_path TO ubereats;

CREATE INDEX ix_restaurant_orders_live ON restaurant_orders (status, created_at)
  WHERE status IN ('in_analysis', 'accepted', 'preparing', 'ready_for_pickup');   -- prazos da RN-28
CREATE INDEX ix_deliveries_live ON deliveries (status)
  WHERE status IN ('awaiting_assignment', 'assigned', 'in_transit');             -- atribuição (RN-06)
CREATE INDEX ix_deliveries_finished ON deliveries (finished_at)
  WHERE status = 'delivered';                                                    -- relógios de 10 min, 20 min e 24 h
CREATE INDEX ix_shifts_open_city ON shifts (city_id) WHERE status = 'open';      -- motorista livre na cidade (RN-35)
CREATE INDEX ix_driver_assignments_shift ON driver_assignments (shift_id);       -- ganho do turno (RN-36)
CREATE INDEX ix_stock_movements_item ON stock_movements (stock_item_id, occurred_at);
CREATE INDEX ix_product_recipes_stock_item ON product_recipes (stock_item_id);   -- comprometido no aceite (RN-39)
CREATE INDEX ix_products_restaurant ON products (restaurant_id);
CREATE INDEX ix_payment_components_item ON payment_components (restaurant_order_id, line_number)
  WHERE restaurant_order_id IS NOT NULL;                                         -- reembolso por atendimento
CREATE INDEX ix_refunds_payment ON refunds (payment_id);
CREATE INDEX ix_incidents_order ON incidents (order_id);
CREATE INDEX ix_incidents_live ON incidents (status) WHERE status IN ('open', 'in_review');
CREATE INDEX ix_incident_items_item ON incident_items (restaurant_order_id, line_number);  -- teto da RN-14

-- Trigger set_updated_at (F1.0 #7) nas tabelas que têm updated_at; as demais são só INSERT.
DO $$
DECLARE t text;
BEGIN
  FOREACH t IN ARRAY ARRAY['cities', 'restaurants', 'products', 'stock_items', 'product_recipes', 'orders',
                           'restaurant_orders', 'deliveries', 'shifts', 'driver_assignments', 'incidents'] LOOP
    EXECUTE format('CREATE TRIGGER trg_%1$s_updated_at BEFORE UPDATE ON %1$I FOR EACH ROW EXECUTE FUNCTION set_updated_at()', t);
  END LOOP;
END $$;
