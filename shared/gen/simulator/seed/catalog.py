"""Catálogo coerente por restaurante (F5.4): produtos, itens de estoque, fichas e estoque inicial.

Determinístico por restaurante (o sorteio usa o restaurant_id como semente): rodar de novo gera o
mesmo catálogo, e a gravação com ON CONFLICT DO NOTHING fica idempotente.
"""

from __future__ import annotations

import math
import random
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any

import yaml

from simulator.money import round_cents
from simulator.params import REPO_ROOT

CATALOG_FILE = REPO_ROOT / "shared" / "gen" / "reference" / "catalog.yaml"
SECTIONS = ("starters", "mains", "sides", "desserts", "drinks", "combos")  # F3.1
KINDS = {"ingredient": "gram", "prepared": "portion"}  # kind → unit (F1.1)
ID_BLOCK = 100  # product_id e stock_item_id = restaurant_id × 100 + n


@dataclass(frozen=True)
class Dish:
    name: str
    section: str
    price: Decimal
    calories: int
    prep_time_min: int
    is_vegetarian: bool
    is_gluten_free: bool
    ready: bool
    recipe: tuple[tuple[str, str, Decimal], ...]  # (item de estoque, kind, quantidade)
    customizations: tuple[str, ...]


@dataclass(frozen=True)
class Catalog:
    shared: tuple[Dish, ...]
    cuisines: Mapping[str, tuple[Dish, ...]]

    def dish(self, cuisine_type: str, name: str) -> Dish | None:
        for dish in (*self.cuisines.get(cuisine_type, ()), *self.shared):
            if dish.name == name:
                return dish
        return None


def _dish(raw: Mapping[str, Any]) -> Dish:  # Any: entrada do YAML
    ready = bool(raw.get("ready", False))
    recipe_raw = raw.get("recipe", {})
    if ready == bool(recipe_raw):
        raise ValueError(f"{raw['name']}: ou ready, ou recipe (RN-37)")
    if raw["section"] not in SECTIONS:
        raise ValueError(f"{raw['name']}: seção fora da lista {SECTIONS}")
    recipe = tuple(
        (item, kind, Decimal(str(qty))) for item, (kind, qty) in recipe_raw.items() if kind in KINDS
    )
    if len(recipe) != len(recipe_raw):
        raise ValueError(f"{raw['name']}: kind de item fora de {sorted(KINDS)}")
    price = Decimal(raw["price"])
    if price <= 0 or price != round_cents(price):
        raise ValueError(f"{raw['name']}: preço inválido")
    return Dish(
        name=raw["name"],
        section=raw["section"],
        price=price,
        calories=int(raw["calories"]),
        prep_time_min=int(raw["prep"]),
        is_vegetarian=bool(raw["veg"]),
        is_gluten_free=bool(raw["gf"]),
        ready=ready,
        recipe=recipe,
        customizations=tuple(raw.get("custom", ())),
    )


def load_catalog(path: Path = CATALOG_FILE) -> Catalog:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    shared = tuple(_dish(d) for d in raw["shared"])
    cuisines = {name: tuple(_dish(d) for d in dishes) for name, dishes in raw["cuisines"].items()}
    for name, dishes in cuisines.items():
        names = [d.name for d in (*dishes, *shared)]
        if len(set(names)) != len(names):
            raise ValueError(f"cozinha {name}: prato repetido")
    return Catalog(shared, cuisines)


@dataclass(frozen=True)
class Product:
    product_id: int
    restaurant_id: int
    name: str
    product_type: str  # a seção do cardápio
    price: Decimal
    unit_cost: Decimal
    calories: int
    prep_time_min: int
    is_vegetarian: bool
    is_gluten_free: bool


@dataclass(frozen=True)
class StockItem:
    stock_item_id: int
    restaurant_id: int
    name: str
    kind: str
    unit: str


@dataclass(frozen=True)
class Recipe:
    product_id: int
    stock_item_id: int
    quantity: Decimal


@dataclass(frozen=True)
class RestaurantCatalog:
    products: tuple[Product, ...]
    stock_items: tuple[StockItem, ...]
    recipes: tuple[Recipe, ...]


def build_catalog(
    restaurant_id: int, cuisine_type: str, catalog: Catalog, products_range: Sequence[int]
) -> RestaurantCatalog:
    """Sorteia os pratos do restaurante e monta a ficha de cada um com itens do próprio restaurante (T4)."""
    if cuisine_type not in catalog.cuisines:
        raise ValueError(f"cozinha {cuisine_type!r} sem pratos em catalog.yaml")
    rng = random.Random(f"catalog:{restaurant_id}")
    cuisine = list(catalog.cuisines[cuisine_type])
    pool = cuisine + list(catalog.shared)
    wanted = min(rng.randint(products_range[0], products_range[1]), len(pool))
    mains = [d for d in cuisine if d.section in ("mains", "combos")]
    first = rng.choice(mains)  # todo restaurante vende ao menos um prato principal
    rest = rng.sample([d for d in pool if d is not first], wanted - 1)
    dishes = sorted([first, *rest], key=lambda d: (SECTIONS.index(d.section), d.name))
    if len(dishes) >= ID_BLOCK:
        raise ValueError("catálogo maior que o bloco de ids por restaurante")

    products, recipes = [], []
    items: dict[str, StockItem] = {}

    def stock_item(name: str, kind: str, unit: str) -> StockItem:
        if name not in items:
            if len(items) + 1 >= ID_BLOCK:
                raise ValueError("itens de estoque além do bloco de ids por restaurante")
            items[name] = StockItem(
                restaurant_id * ID_BLOCK + len(items) + 1, restaurant_id, name, kind, unit
            )
        existing = items[name]
        if (existing.kind, existing.unit) != (kind, unit):
            raise ValueError(f"item {name!r} com kind ou unidade diferente entre pratos")
        return existing

    for n, dish in enumerate(dishes, start=1):
        product_id = restaurant_id * ID_BLOCK + n
        cost_share = Decimal(rng.randint(28, 42)) / 100
        products.append(
            Product(
                product_id=product_id,
                restaurant_id=restaurant_id,
                name=dish.name,
                product_type=dish.section,
                price=dish.price,
                unit_cost=round_cents(dish.price * cost_share),
                calories=dish.calories,
                prep_time_min=dish.prep_time_min,
                is_vegetarian=dish.is_vegetarian,
                is_gluten_free=dish.is_gluten_free,
            )
        )
        if dish.ready:
            # Produto pronto: o item de estoque é ele mesmo, uma unidade por venda (ADR 007, decisão 2).
            recipes.append(
                Recipe(product_id, stock_item(dish.name, "ready", "unit").stock_item_id, Decimal(1))
            )
        else:
            for item_name, kind, quantity in dish.recipe:
                item = stock_item(item_name, kind, KINDS[kind])
                recipes.append(Recipe(product_id, item.stock_item_id, quantity))
    return RestaurantCatalog(tuple(products), tuple(items.values()), tuple(recipes))


def daily_units_per_product(params: Mapping[str, Any], products_in_restaurant: int) -> Decimal:
    """Venda média esperada por produto e dia, a partir do ritmo de compras (F5.8)."""
    demand, scale = params["demand"], params["scale"]
    factors = demand["hourly_factor"]
    day_factor = sum(
        float(factors.get(f"{h:02d}", factors.get(str(h), demand["default_hourly_factor"])))
        for h in range(24)
    )
    orders_per_restaurant = (
        demand["peak_orders_per_hour_per_city"] * day_factor / scale["restaurants_per_city"]
    )
    restaurant_orders = orders_per_restaurant * (1 + demand["second_restaurant_share"])
    lines = sum(demand["items_per_restaurant_order"]) / 2
    quantity = sum(demand["quantity_per_item"]) / 2
    units = restaurant_orders * lines * quantity / products_in_restaurant
    return Decimal(str(round(units, 3)))


def initial_stock(rc: RestaurantCatalog, daily_units: Decimal, days: int) -> dict[int, Decimal]:
    """Quantidade do restock inicial por item: ficha × venda diária × dias, arredondada para cima."""
    need: dict[int, Decimal] = {item.stock_item_id: Decimal(0) for item in rc.stock_items}
    for recipe in rc.recipes:
        need[recipe.stock_item_id] += recipe.quantity * daily_units * days
    return {item_id: Decimal(max(1, math.ceil(q))) for item_id, q in need.items()}
