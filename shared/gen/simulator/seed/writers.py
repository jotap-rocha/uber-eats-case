"""Gravação dos seeds nos bancos (F5.3, passos 6 e 8). Idempotente: rodar de novo não duplica nada."""

from __future__ import annotations

import logging
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import UTC, date, datetime, time
from typing import Any

from bson.int64 import Int64

from simulator.params import City, Parameters
from simulator.seed.catalog import Catalog, build_catalog, daily_units_per_product, initial_stock
from simulator.seed.profiles import MenuProduct, build_profile, same_content

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class SeedCount:
    target: str
    written: int
    skipped: int


# Any nas conexões: psycopg, oracledb e pymongo não compartilham um tipo comum; cada função usa o seu.


def seed_cities(pg: Any, ora: Any, cities: Iterable[City]) -> list[SeedCount]:
    """Mesma lista nos dois bancos, a partir do CSV (F5.4): idênticas por construção (T17)."""
    rows = [(c.city_id, c.name, c.state_code) for c in cities]
    with pg.transaction(), pg.cursor() as cur:
        written_pg = 0
        for row in rows:
            cur.execute(
                "INSERT INTO cities (city_id, name, state_code) VALUES (%s, %s, %s) "
                "ON CONFLICT (city_id) DO NOTHING",
                row,
            )
            written_pg += cur.rowcount
    with ora.cursor() as cur:
        written_ora = 0
        for row in rows:
            cur.execute(
                "MERGE INTO cities t USING (SELECT :1 city_id, :2 name, :3 state_code FROM dual) s "
                "ON (t.city_id = s.city_id) "
                "WHEN NOT MATCHED THEN INSERT (city_id, name, state_code) VALUES (s.city_id, s.name, s.state_code)",
                row,
            )
            written_ora += cur.rowcount
    ora.commit()
    return [
        SeedCount("postgres.cities", written_pg, len(rows) - written_pg),
        SeedCount("oracle.CITIES", written_ora, len(rows) - written_ora),
    ]


def seed_catalog(pg: Any, params: Parameters, catalog: Catalog, start_day: date) -> list[SeedCount]:
    """Uma transação por restaurante: produtos, itens, fichas e o restock inicial (T4, T6)."""
    scale = params.section("scale")
    days = int(params.section("stock")["restock_target_days"])
    restock_at = datetime.combine(start_day, time(0, 0))  # antes de qualquer janela (F5.4, F5.6)
    totals = {"products": 0, "stock_items": 0, "product_recipes": 0, "restocks": 0}
    attempted = {"products": 0, "stock_items": 0, "product_recipes": 0}
    skipped_restock = 0
    with pg.cursor() as cur:
        cur.execute("SELECT restaurant_id, cuisine_type FROM restaurants ORDER BY restaurant_id")
        restaurants = cur.fetchall()
    for restaurant_id, cuisine_type in restaurants:
        rc = build_catalog(restaurant_id, cuisine_type, catalog, scale["products_per_restaurant"])
        stock = initial_stock(rc, daily_units_per_product(params.raw, len(rc.products)), days)
        attempted["products"] += len(rc.products)
        attempted["stock_items"] += len(rc.stock_items)
        attempted["product_recipes"] += len(rc.recipes)
        with pg.transaction(), pg.cursor() as cur:
            for p in rc.products:
                cur.execute(
                    "INSERT INTO products (product_id, restaurant_id, name, product_type, price, unit_cost, "
                    "calories, prep_time_min, is_vegetarian, is_gluten_free, is_active) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, true) ON CONFLICT (product_id) DO NOTHING",
                    (
                        p.product_id,
                        p.restaurant_id,
                        p.name,
                        p.product_type,
                        p.price,
                        p.unit_cost,
                        p.calories,
                        p.prep_time_min,
                        p.is_vegetarian,
                        p.is_gluten_free,
                    ),
                )
                totals["products"] += cur.rowcount
            for s in rc.stock_items:
                cur.execute(
                    "INSERT INTO stock_items (stock_item_id, restaurant_id, name, kind, unit) "
                    "VALUES (%s, %s, %s, %s, %s) ON CONFLICT (stock_item_id) DO NOTHING",
                    (s.stock_item_id, s.restaurant_id, s.name, s.kind, s.unit),
                )
                totals["stock_items"] += cur.rowcount
            for r in rc.recipes:
                cur.execute(
                    "INSERT INTO product_recipes (product_id, stock_item_id, quantity) VALUES (%s, %s, %s) "
                    "ON CONFLICT (product_id, stock_item_id) DO NOTHING",
                    (r.product_id, r.stock_item_id, r.quantity),
                )
                totals["product_recipes"] += cur.rowcount
            for item_id, quantity in stock.items():
                cur.execute(
                    "SELECT 1 FROM stock_movements WHERE stock_item_id = %s LIMIT 1", (item_id,)
                )
                if cur.fetchone():
                    skipped_restock += 1
                    continue
                cur.execute(
                    "INSERT INTO stock_movements (stock_item_id, movement_type, quantity, occurred_at) "
                    "VALUES (%s, 'restock', %s, %s)",
                    (item_id, quantity, restock_at),
                )
                cur.execute(
                    "UPDATE stock_items SET quantity_on_hand = quantity_on_hand + %s WHERE stock_item_id = %s",
                    (quantity, item_id),
                )
                totals["restocks"] += 1
    counts = [SeedCount(f"postgres.{k}", totals[k], attempted[k] - totals[k]) for k in attempted]
    counts.append(
        SeedCount("postgres.stock_movements(restock inicial)", totals["restocks"], skipped_restock)
    )
    log.info("catálogo: %d restaurantes", len(restaurants))
    return counts


def seed_profiles(pg: Any, mongo: Any, params: Parameters, catalog: Catalog) -> list[SeedCount]:
    """Um perfil por restaurante com todos os produtos dele (RN-23, T18); só regrava o que mudou."""
    share = float(params.section("scale")["restaurants_with_two_windows"])
    with pg.cursor() as cur:
        cur.execute("SELECT restaurant_id, cuisine_type FROM restaurants ORDER BY restaurant_id")
        restaurants = cur.fetchall()
        cur.execute(
            "SELECT restaurant_id, product_id, name, product_type FROM products ORDER BY product_id"
        )
        by_restaurant: dict[int, list[MenuProduct]] = {}
        for restaurant_id, product_id, name, product_type in cur.fetchall():
            by_restaurant.setdefault(restaurant_id, []).append(
                MenuProduct(product_id, name, product_type)
            )
    collection = mongo["ubereats"]["restaurant_profiles"]
    written = skipped = 0
    now = datetime.now(UTC)
    for restaurant_id, cuisine_type in restaurants:
        profile = build_profile(
            restaurant_id, cuisine_type, by_restaurant.get(restaurant_id, []), catalog, share
        )
        existing = collection.find_one({"_id": Int64(restaurant_id)})
        if same_content(existing, profile):
            skipped += 1
            continue
        doc = {
            "_id": Int64(restaurant_id),
            "service_windows": profile["service_windows"],
            "menu_items": [
                {**item, "product_id": Int64(item["product_id"])} for item in profile["menu_items"]
            ],
            "created_at": existing["created_at"] if existing else now,
            "updated_at": now,
        }
        collection.replace_one({"_id": doc["_id"]}, doc, upsert=True)
        written += 1
    return [SeedCount("mongodb.restaurant_profiles", written, skipped)]
