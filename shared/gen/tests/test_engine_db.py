"""Histórico curto no Postgres descartável, T1 a T16 e T6c ao final; parada e retomada (F5.10)."""

from __future__ import annotations

import dataclasses
from datetime import datetime, time, timedelta
from decimal import Decimal
from typing import Any

from simulator.checks import check_t06_restock_windows, run_sql_checks
from simulator.clock import SimClock
from simulator.engine import bootstrap, build_context, recover, resume_point, run
from simulator.geo import Point
from simulator.params import City, load_parameters
from simulator.reference import CustomerRef, DriverRef, Reference, build_reference
from simulator.seed.catalog import load_catalog
from simulator.seed.writers import seed_catalog

from tests.simdb import CITY, fresh_database, needs_db

START = datetime(2026, 10, 1, 0, 0)
WINDOWS = {  # hora de Brasília, [início, fim)
    "one": [(time(10), time(23))],
    "two": [(time(11), time(15)), (time(18), time(23))],
}
CUISINES = ("brazilian", "italian", "japanese", "burger")
N_RESTAURANTS, N_CUSTOMERS, N_DRIVERS = 8, 300, 60
FAR_FUTURE = datetime(2035, 1, 1)


def _params() -> Any:  # Any: Parameters
    base = load_parameters()
    raw = {
        **base.raw,
        "scale": {**base.raw["scale"], "restaurants_per_city": N_RESTAURANTS},
        "demand": {**base.raw["demand"], "peak_orders_per_hour_per_city": 14},
        "behavior": {  # eventos raros ficam frequentes para o teste exercitar todos os caminhos
            **base.raw["behavior"],
            "driver_gives_up": 0.2,
            "driver_unable": 0.04,
            "customer_absent": 0.05,
            "restaurant_declines": 0.08,
            "restaurant_issue_after_accept": 0.04,
            "incident": 0.3,
            "customer_cancels_late": 0.6,
            "prep_overrun_lognormal_sigma": 0.6,
        },
    }
    sp = City(CITY, "São Paulo", "SP", Decimal("-23.550520"), Decimal("-46.633308"))
    return dataclasses.replace(base, raw=raw, cities=(sp,))


def _seed(conn: Any) -> dict[int, list[tuple[time, time]]]:
    windows: dict[int, list[tuple[time, time]]] = {}
    with conn.transaction(), conn.cursor() as cur:
        cur.execute("INSERT INTO cities VALUES (%s, 'São Paulo', 'SP')", (CITY,))
        for rid in range(1, N_RESTAURANTS + 1):
            windows[rid] = WINDOWS["two" if rid % 2 else "one"]
            cur.execute(
                "INSERT INTO restaurants (restaurant_id, name, cnpj, phone_number, address, "
                "postal_code, latitude, longitude, city_id, cuisine_type, status) VALUES "
                "(%s, %s, %s, '11999999999', 'Rua Teste', '01000000', %s, %s, %s, %s, 'active')",
                (
                    rid,
                    f"Restaurante {rid}",
                    f"{rid:014d}",
                    Decimal("-23.55") - Decimal(rid) / 200,
                    Decimal("-46.63") + Decimal(rid) / 300,
                    CITY,
                    CUISINES[rid % len(CUISINES)],
                ),
            )
    return windows


class Loader:
    """Lê restaurantes e catálogo do Postgres como o DatabaseLoader; cadastros do Oracle em memória."""

    def __init__(self, conn: Any, windows: dict[int, list[tuple[time, time]]]) -> None:
        self.conn, self.windows = conn, windows
        self.customers = [
            CustomerRef(
                i,
                CITY,
                f"Rua {i}",
                Point(
                    Decimal("-23.55") + Decimal(i % 50) / 300,
                    Decimal("-46.63") - Decimal(i % 30) / 300,
                ),
                datetime(2020, 1, 1),
            )
            for i in range(1, N_CUSTOMERS + 1)
        ]
        self.drivers = [DriverRef(i, CITY, datetime(2021, 1, 1)) for i in range(1, N_DRIVERS + 1)]

    def load(self) -> Reference:
        with self.conn.cursor() as cur:
            restaurants = cur.execute(
                "SELECT restaurant_id, city_id, latitude, longitude FROM restaurants"
            ).fetchall()
            products = cur.execute(
                "SELECT product_id, restaurant_id, name, price, prep_time_min FROM products"
            ).fetchall()
            recipes = cur.execute(
                "SELECT product_id, stock_item_id, quantity FROM product_recipes"
            ).fetchall()
        return build_reference(
            self.customers, self.drivers, restaurants, products, recipes, self.windows
        )


def _violations(conn: Any, windows: dict[int, list[tuple[time, time]]]) -> dict[str, Any]:
    conn.execute("SET SESSION CHARACTERISTICS AS TRANSACTION READ ONLY")
    try:
        results = run_sql_checks(conn)
        with conn.cursor() as cur:
            restocks = cur.execute(
                "SELECT m.stock_movement_id, s.restaurant_id, m.occurred_at FROM stock_movements m "
                "JOIN stock_items s ON s.stock_item_id = m.stock_item_id WHERE m.movement_type = 'restock'"
            ).fetchall()
        results.append(check_t06_restock_windows(restocks, windows))
    finally:
        conn.execute("SET SESSION CHARACTERISTICS AS TRANSACTION READ WRITE")
    return {r.check: (r.count, r.sample) for r in results if not r.ok}


def _counts(conn: Any) -> dict[str, int]:
    queries = {
        "orders": "SELECT count(*) FROM orders",
        "abandoned_checkouts": "SELECT count(*) FROM checkouts c WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.checkout_id = c.checkout_id)",
        "completed": "SELECT count(*) FROM orders WHERE status = 'completed'",
        "cancelled": "SELECT count(*) FROM orders WHERE status = 'cancelled'",
        "undelivered": "SELECT count(*) FROM orders WHERE status = 'undelivered'",
        "rejected_ro": "SELECT count(*) FROM restaurant_orders WHERE status = 'rejected'",
        "refunds": "SELECT count(*) FROM refunds",
        "gave_up": "SELECT count(*) FROM driver_assignments WHERE release_reason = 'driver_gave_up'",
        "incidents": "SELECT count(*) FROM incidents",
        "tips": "SELECT count(*) FROM tips",
        "ratings": "SELECT count(*) FROM driver_ratings",
        "consumption": "SELECT count(*) FROM stock_movements WHERE movement_type = 'consumption'",
        "restocks_after_seed": "SELECT count(*) FROM stock_movements WHERE movement_type = 'restock' AND occurred_at > '2026-10-01 00:00'",
    }
    return {name: int(conn.execute(sql).fetchone()[0]) for name, sql in queries.items()}


@needs_db
def test_historico_curto_passa_nos_invariantes_e_retoma() -> None:
    params = _params()
    with fresh_database() as conn:
        windows = _seed(conn)
        seed_catalog(conn, params, load_catalog(), START.date())
        loader = Loader(conn, windows)
        clock = SimClock(START, wall=lambda: FAR_FUTURE, sleep=lambda s: False)
        ctx = build_context(
            conn, loader, params, start=START, seed=11, salts=("so", "sp"), clock=clock
        )
        bootstrap(ctx)
        done = run(ctx, until=START + timedelta(days=2))
        assert done > 500

        counts = _counts(conn)
        assert _violations(conn, windows) == {}
        for name in (
            "orders",
            "completed",
            "refunds",
            "incidents",
            "tips",
            "ratings",
            "consumption",
        ):
            assert counts[name] > 0, (name, counts)
        assert counts["rejected_ro"] > 0 and counts["gave_up"] > 0, counts
        assert counts["restocks_after_seed"] > 0, counts

        # Parada e retomada pelo estado do banco (F5.10): o relógio volta ao último evento gravado.
        resumed = resume_point(conn)
        assert resumed is not None and START < resumed <= START + timedelta(days=2, hours=24)
        clock2 = SimClock(resumed, wall=lambda: FAR_FUTURE, sleep=lambda s: False)
        ctx2 = build_context(
            conn, loader, params, start=START, seed=12, salts=("so", "sp"), clock=clock2
        )
        bootstrap(ctx2)
        recover(ctx2)
        run(ctx2, until=resumed + timedelta(days=1))
        assert _violations(conn, windows) == {}
        assert _counts(conn)["orders"] > counts["orders"]


def _digest(conn: Any) -> tuple[Any, ...]:
    return (
        _counts(conn),
        conn.execute(
            "SELECT sum(total_amount), count(DISTINCT tracking_code) FROM payments"
        ).fetchone(),
        conn.execute(
            "SELECT string_agg(tracking_code, ',' ORDER BY order_id) FROM orders"
        ).fetchone(),
    )


@needs_db
def test_mesma_semente_mesmo_resultado() -> None:
    """`--seed` torna a geração reprodutível: mesmos pedidos, valores e códigos de rastreio."""
    params = _params()
    digests = []
    for seed in (5, 5, 6):
        with fresh_database() as conn:
            windows = _seed(conn)
            seed_catalog(conn, params, load_catalog(), START.date())
            clock = SimClock(START, wall=lambda: FAR_FUTURE, sleep=lambda s: False)
            ctx = build_context(
                conn,
                Loader(conn, windows),
                params,
                start=START,
                seed=seed,
                salts=("so", "sp"),
                clock=clock,
            )
            bootstrap(ctx)
            run(ctx, until=START + timedelta(hours=14))
            digests.append(_digest(conn))
    assert digests[0][0]["orders"] > 0
    assert digests[0] == digests[1]
    assert digests[0] != digests[2]
