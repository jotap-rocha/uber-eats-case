"""Gate da regeração (F5.3, passos 8 e 11): T1 a T19 nos três bancos, só leitura.

python -m simulator.gate  → imprime cada verificação com a contagem e uma amostra de chaves
(nunca dado de pessoa) e sai com código 1 se alguma falhar.
"""

from __future__ import annotations

import sys
from typing import Any

from simulator.checks import (
    CrossBankRefs,
    Violations,
    check_t06_restock_windows,
    check_t17,
    check_t18,
    check_t19,
    run_sql_checks,
    windows_of,
)
from simulator.db import Settings, connect_mongo, connect_oracle, connect_postgres

# ext → Oracle.* no Postgres (F1, comentários "ext →"): T17.
CUSTOMER_REFS = ("orders", "checkouts", "incidents", "driver_ratings", "restaurant_ratings")
DRIVER_REFS = ("shifts", "driver_assignments", "driver_payouts", "tips", "driver_ratings")


def _ids(cur: Any, table: str, column: str) -> set[int]:  # Any: cursor psycopg
    cur.execute(
        f"SELECT DISTINCT {column} FROM {table}"
    )  # nomes fixos acima, nunca entrada externa
    return {row[0] for row in cur.fetchall()}


def collect(
    pg: Any, ora: Any, mongo: Any
) -> list[Violations]:  # Any: conexões de drivers diferentes
    results = run_sql_checks(pg)
    with pg.cursor() as cur:
        refs = CrossBankRefs(
            customer_refs={f"{t}.customer_id": _ids(cur, t, "customer_id") for t in CUSTOMER_REFS},
            driver_refs={f"{t}.driver_id": _ids(cur, t, "driver_id") for t in DRIVER_REFS},
            order_cities=cur.execute(
                "SELECT order_id, customer_id, city_id FROM orders"
            ).fetchall(),
            shift_cities=cur.execute("SELECT shift_id, driver_id, city_id FROM shifts").fetchall(),
        )
        pg_cities = cur.execute("SELECT city_id, name, state_code FROM cities").fetchall()
        products = dict(cur.execute("SELECT product_id, restaurant_id FROM products").fetchall())
        restaurant_ids = [
            r[0] for r in cur.execute("SELECT restaurant_id FROM restaurants").fetchall()
        ]
        restocks = cur.execute(
            "SELECT m.stock_movement_id, s.restaurant_id, m.occurred_at FROM stock_movements m "
            "JOIN stock_items s ON s.stock_item_id = m.stock_item_id WHERE m.movement_type = 'restock'"
        ).fetchall()
    with ora.cursor() as cur:
        customer_city = dict(cur.execute("SELECT customer_id, city_id FROM customers").fetchall())
        driver_city = dict(cur.execute("SELECT driver_id, city_id FROM drivers").fetchall())
        ora_cities = [
            tuple(r) for r in cur.execute("SELECT city_id, name, state_code FROM cities").fetchall()
        ]
    profiles = list(
        mongo["ubereats"]["restaurant_profiles"].find({}, {"service_windows": 1, "menu_items": 1})
    )
    windows = {int(p["_id"]): windows_of(p) for p in profiles}
    results += check_t17(refs, customer_city, driver_city, pg_cities, ora_cities)
    results += check_t18(profiles, products, restaurant_ids)
    results.append(check_t19(profiles))
    results.append(check_t06_restock_windows(restocks, windows))
    return results


def main() -> int:
    settings = Settings.load()
    with (
        connect_postgres(settings) as pg,
        connect_oracle(settings) as ora,
        connect_mongo(settings) as mongo,
    ):
        # A conexão do pacote é autocommit; o read_only do psycopg só vale com transação, então a
        # sessão inteira fica só leitura no próprio Postgres.
        pg.execute("SET SESSION CHARACTERISTICS AS TRANSACTION READ ONLY")
        results = collect(pg, ora, mongo)
    failed = [r for r in results if not r.ok]
    for r in results:
        print(
            f"{'ok   ' if r.ok else 'FALHA'} {r.check}: {r.count}"
            + ("" if r.ok else f"  amostra={r.sample}")
        )
    print(f"\n{len(results) - len(failed)} de {len(results)} verificações passaram")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
