"""Banco descartável para os testes do simulador: um database novo por teste, clonado do init.

UBEREATS_SIM_DSN aponta para o Postgres f5-* (contêiner descartável, porta 127.0.0.1:15xxx), cujo
banco foi criado pelo init da regeração (shared/sql/postgres/). O teste nunca escreve nele: clona-o
com CREATE DATABASE ... TEMPLATE e escreve só no clone, que some com o `docker rm -v`.
"""

from __future__ import annotations

import os
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime
from decimal import Decimal
from typing import Any

import pytest

DSN_VAR = "UBEREATS_SIM_DSN"
needs_db = pytest.mark.skipif(
    DSN_VAR not in os.environ,
    reason=f"integração do simulador: defina {DSN_VAR} com o Postgres f5-* descartável",
)

CITY = 3550308
D = Decimal


@contextmanager
def fresh_database() -> Iterator[Any]:  # Any: psycopg.Connection
    psycopg = pytest.importorskip("psycopg")
    from psycopg.conninfo import conninfo_to_dict

    info = conninfo_to_dict(os.environ[DSN_VAR])
    if str(info.get("host")) not in {"127.0.0.1", "localhost"} or not str(
        info.get("port", "")
    ).startswith("15"):
        pytest.fail(f"{DSN_VAR} precisa apontar para o contêiner f5-* (127.0.0.1:15xxx)")
    template = str(info["dbname"])
    clone = f"sim_test_{uuid.uuid4().hex[:12]}"
    with psycopg.connect(**{**info, "dbname": "postgres"}, autocommit=True) as admin:
        admin.execute(f'CREATE DATABASE "{clone}" TEMPLATE "{template}"')
    options = "-c timezone=America/Sao_Paulo -c search_path=ubereats"
    with psycopg.connect(**{**info, "dbname": clone}, autocommit=True, options=options) as conn:
        conn.execute("SET synchronous_commit = off")  # como o simulador: o fsync no HDD pesa metade
        yield conn


def seed_minimal(conn: Any) -> None:  # Any: psycopg.Connection
    """Dois restaurantes na mesma cidade, três produtos com ficha e estoque inicial (T4, T6)."""
    t0 = datetime(2026, 10, 1, 0, 0)
    with conn.transaction(), conn.cursor() as cur:
        cur.execute("INSERT INTO cities VALUES (%s, 'São Paulo', 'SP')", (CITY,))
        for rid, lat in [(1, "-23.550000"), (2, "-23.560000")]:
            cur.execute(
                "INSERT INTO restaurants (restaurant_id, name, cnpj, phone_number, address, "
                "postal_code, latitude, longitude, city_id, cuisine_type, status) VALUES "
                "(%s, %s, %s, '11999999999', 'Rua Teste', '01000000', %s, -46.630000, %s, "
                "'brazilian', 'active')",
                (rid, f"Restaurante {rid}", f"{rid:014d}", D(lat), CITY),
            )
        products = [
            (101, 1, "Prato feito", "mains", D("10.00"), 15),
            (102, 1, "Refrigerante lata", "drinks", D("6.50"), 1),
            (201, 2, "Feijoada", "mains", D("20.00"), 20),
        ]
        for pid, rid, name, kind, price, prep in products:
            cur.execute(
                "INSERT INTO products (product_id, restaurant_id, name, product_type, price, "
                "unit_cost, calories, prep_time_min, is_vegetarian, is_gluten_free, is_active) "
                "VALUES (%s, %s, %s, %s, %s, 1.00, 500, %s, false, true, true)",
                (pid, rid, name, kind, price, prep),
            )
        items = [
            (1001, 1, "Frango", "ingredient", "gram", D(1000)),
            (1002, 1, "Refrigerante lata", "ready", "unit", D(10)),
            (2001, 2, "Feijoada", "prepared", "portion", D(5)),
        ]
        for sid, rid, name, kind, unit, qty in items:
            cur.execute(
                "INSERT INTO stock_items (stock_item_id, restaurant_id, name, kind, unit) "
                "VALUES (%s, %s, %s, %s, %s)",
                (sid, rid, name, kind, unit),
            )
            cur.execute(
                "INSERT INTO stock_movements (stock_item_id, movement_type, quantity, occurred_at) "
                "VALUES (%s, 'restock', %s, %s)",
                (sid, qty, t0),
            )
            cur.execute(
                "UPDATE stock_items SET quantity_on_hand = %s WHERE stock_item_id = %s", (qty, sid)
            )
        for pid, sid, qty in [(101, 1001, D(200)), (102, 1002, D(1)), (201, 2001, D(1))]:
            cur.execute("INSERT INTO product_recipes VALUES (%s, %s, %s)", (pid, sid, qty))
