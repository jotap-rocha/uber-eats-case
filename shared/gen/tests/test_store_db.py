"""Helpers de escrita contra o Postgres descartável: trava da RN-27, sync do pedido, estoque e dinheiro."""

from __future__ import annotations

from datetime import datetime, timedelta
from decimal import Decimal
from typing import Any

import pytest
from simulator.checks import run_sql_checks
from simulator.geo import Point
from simulator.money import Line, price_purchase
from simulator.refunds import for_restaurant_order
from simulator.store import (
    Refused,
    RouteParams,
    available_stock,
    consume_stock,
    insert_refund,
    load_ledger,
    lock_restaurant_order,
    move_restaurant_order,
    next_id,
    sync_order,
)
from simulator.tracking import tracking_code

from tests.simdb import CITY, fresh_database, needs_db, seed_minimal

D = Decimal
T0 = datetime(2026, 10, 1, 12, 0)
POINTS = {1: Point(D("-23.550000"), D("-46.630000")), 2: Point(D("-23.560000"), D("-46.630000"))}
ROUTE = RouteParams(D("1.3"), 25.0, timedelta(minutes=10))


def _purchase(cur: Any) -> tuple[int, int, int, int]:  # Any: cursor psycopg
    """Compra com dois atendimentos (2 × prato feito no 1, 1 feijoada no 2), como a ADR 009 grava."""
    cur.execute("INSERT INTO checkouts (customer_id, amount) VALUES (7, 1) RETURNING checkout_id")
    checkout_id = cur.fetchone()[0]
    order_id = next_id(cur, "orders", "order_id")
    ro1 = next_id(cur, "restaurant_orders", "restaurant_order_id")
    ro2 = next_id(cur, "restaurant_orders", "restaurant_order_id")
    lines = [Line(ro1, 1, D("10.00"), 2), Line(ro2, 1, D("20.00"), 1)]
    pricing = price_purchase(lines, D("6.99"), D("0.08"), D("0.12"), D("0.0099"))
    cur.execute("UPDATE checkouts SET amount = %s", (pricing.total_amount,))
    cur.execute(
        "INSERT INTO payment_attempts (checkout_id, attempt_number, amount, payment_method, "
        "gateway, result, attempted_at) VALUES (%s, 1, %s, 'pix', 'Stripe', 'approved', %s)",
        (checkout_id, pricing.total_amount, T0),
    )
    cur.execute(
        "INSERT INTO orders (order_id, tracking_code, checkout_id, customer_id, city_id, placed_at) "
        "VALUES (%s, %s, %s, 7, %s, %s)",
        (order_id, tracking_code(order_id, "teste"), checkout_id, CITY, T0),
    )
    cur.execute(
        "INSERT INTO order_status_transitions VALUES (%s, 1, NULL, 'in_analysis', 'customer', "
        "NULL, %s)",
        (order_id, T0),
    )
    for ro, rid, pid, name, price, qty in [
        (ro1, 1, 101, "Prato feito", D("10.00"), 2),
        (ro2, 2, 201, "Feijoada", D("20.00"), 1),
    ]:
        cur.execute(
            "INSERT INTO restaurant_orders (restaurant_order_id, order_id, restaurant_id) "
            "VALUES (%s, %s, %s)",
            (ro, order_id, rid),
        )
        cur.execute(
            "INSERT INTO restaurant_order_status_transitions VALUES (%s, 1, NULL, 'in_analysis', "
            "'customer', NULL, %s)",
            (ro, T0),
        )
        cur.execute(
            "INSERT INTO order_items VALUES (%s, 1, %s, %s, %s, %s, %s)",
            (ro, pid, name, price, qty, price * qty),
        )
    cur.execute(
        "INSERT INTO deliveries (order_id, dropoff_address, dropoff_latitude, dropoff_longitude) "
        "VALUES (%s, 'Rua Destino', -23.570000, -46.640000)",
        (order_id,),
    )
    payment_id = next_id(cur, "payments", "payment_id")
    cur.execute(
        "INSERT INTO payments (payment_id, tracking_code, order_id, checkout_id, attempt_number, "
        "total_amount, tax_rate, service_fee_rate, payment_fee_rate, payment_fee_amount, paid_at) "
        "VALUES (%s, %s, %s, %s, 1, %s, 0.08, 0.12, 0.0099, %s, %s)",
        (
            payment_id,
            tracking_code(payment_id, "teste-pg"),
            order_id,
            checkout_id,
            pricing.total_amount,
            pricing.payment_fee_amount,
            T0,
        ),
    )
    for c in pricing.components:
        cur.execute(
            "INSERT INTO payment_components VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
                payment_id,
                c.component_number,
                c.component_type,
                c.restaurant_order_id,
                c.line_number,
                c.gross_amount,
                c.tax_amount,
            ),
        )
    cur.execute("INSERT INTO receipts VALUES (%s, %s)", (payment_id, T0))
    return order_id, ro1, ro2, payment_id


@needs_db
def test_ciclo_basico_no_banco() -> None:
    with fresh_database() as conn:
        seed_minimal(conn)
        with conn.transaction(), conn.cursor() as cur:
            order_id, ro1, ro2, payment_id = _purchase(cur)

        accepted = T0 + timedelta(minutes=2)
        with conn.transaction(), conn.cursor() as cur:
            ro = lock_restaurant_order(cur, ro1)
            assert ro.sent_at == T0
            move_restaurant_order(
                cur,
                ro,
                "accepted",
                "restaurant",
                accepted,
                columns={"accepted_at": accepted, "estimated_prep_min": 15},
            )
            sync = sync_order(cur, order_id, "restaurant", accepted, POINTS, ROUTE)
            assert (sync.before, sync.after, sync.froze_promise) == (
                "in_analysis",
                "in_analysis",
                False,
            )
            assert available_stock(cur, 1)[1001] == D(600)  # 1000 − 2 × 200 comprometidos (RN-39)

        with pytest.raises(Refused), conn.transaction(), conn.cursor() as cur:
            move_restaurant_order(
                cur, ro, "rejected", "restaurant", accepted, "restaurant_declined"
            )
        # RN-27: a linha `ro` está velha (in_analysis); a transação inteira voltou

        rejected = T0 + timedelta(minutes=3)
        with conn.transaction(), conn.cursor() as cur:
            other = lock_restaurant_order(cur, ro2)
            move_restaurant_order(
                cur, other, "rejected", "restaurant", rejected, "restaurant_declined"
            )
            ledger = load_ledger(cur, payment_id)
            plan = for_restaurant_order(ledger, ro2, last_active=False)
            insert_refund(cur, payment_id, "restaurant_order", ro2, plan, rejected)
            sync = sync_order(cur, order_id, "restaurant", rejected, POINTS, ROUTE)
            assert (sync.after, sync.froze_promise) == ("preparing", True)
            cur.execute(
                "SELECT promised_at, distance_km FROM deliveries WHERE order_id = %s", (order_id,)
            )
            promised, distance = cur.fetchone()
            # T7: último aceite ativo (12:02) + 15 min + rota ÷ 25 km/h + 10 min de folga
            assert promised == accepted + timedelta(minutes=25, hours=float(distance) / 25)
            reloaded = load_ledger(cur, payment_id)
            assert reloaded.total_refunded == plan.total_amount

        started = T0 + timedelta(minutes=4)
        with conn.transaction(), conn.cursor() as cur:
            ro = lock_restaurant_order(cur, ro1)
            move_restaurant_order(cur, ro, "preparing", "restaurant", started)
            consume_stock(cur, ro1, started)
            sync = sync_order(cur, order_id, "restaurant", started, POINTS, ROUTE)
            assert sync.after == "preparing"  # sem mudança, sem transição nova no pedido
            assert available_stock(cur, 1)[1001] == D(600)  # já baixado, nada comprometido

        conn.execute("SET SESSION CHARACTERISTICS AS TRANSACTION READ ONLY")
        falhas = {r.check: r.sample for r in run_sql_checks(conn) if not r.ok}
        assert not falhas
