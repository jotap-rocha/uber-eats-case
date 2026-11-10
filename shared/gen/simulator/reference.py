"""O que o simulador lê e não escreve: cadastros do Oracle, catálogo do Postgres, janelas do Mongo.

Lido de uma vez e guardado em cache, recarregado a cada `profile_cache_refresh_min` de relógio de
parede (F0.6; ADR 009, decisão 5). O histórico corre muito mais rápido que o relógio de parede:
recarregar pelo tempo simulado leria o Oracle milhares de vezes. Nenhum campo de pessoa é logado.
"""

from __future__ import annotations

import logging
import time as systime
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
from functools import cached_property
from typing import Any, Protocol

from simulator.checks import windows_of
from simulator.geo import Point
from simulator.rules import Window, is_open

log = logging.getLogger(__name__)
COORD = Decimal("0.000001")


def _coord(
    value: Any,
) -> Decimal:  # Any: NUMBER(9,6) chega como float no oracledb, Decimal no psycopg
    return Decimal(str(value)).quantize(COORD)


@dataclass(frozen=True)
class CustomerRef:
    customer_id: int
    city_id: int
    address: str  # dropoff_address: cópia na compra (L1b, decisão 8)
    point: Point
    signup_date: datetime

    def __repr__(self) -> str:  # sem endereço nem coordenada em log
        return f"CustomerRef({self.customer_id})"


@dataclass(frozen=True)
class DriverRef:
    driver_id: int
    city_id: int
    registration_date: datetime


@dataclass(frozen=True)
class ProductRef:
    product_id: int
    name: str
    price: Decimal
    prep_time_min: int
    recipe: tuple[tuple[int, Decimal], ...]  # (stock_item_id, quantidade por unidade)


@dataclass(frozen=True)
class RestaurantRef:
    restaurant_id: int
    city_id: int
    point: Point
    windows: tuple[Window, ...]
    products: tuple[ProductRef, ...]

    def open_at(self, at: datetime) -> bool:
        return is_open(self.windows, at.time())


@dataclass(frozen=True)
class Reference:
    customers: Mapping[int, CustomerRef]
    drivers: Mapping[int, DriverRef]
    restaurants: Mapping[int, RestaurantRef]

    @cached_property
    def restaurants_by_city(self) -> dict[int, list[RestaurantRef]]:
        cities: dict[int, list[RestaurantRef]] = {}
        for r in self.restaurants.values():
            cities.setdefault(r.city_id, []).append(r)
        return cities

    @cached_property
    def customers_by_city(self) -> dict[int, list[CustomerRef]]:
        cities: dict[int, list[CustomerRef]] = {}
        for c in self.customers.values():
            cities.setdefault(c.city_id, []).append(c)
        return cities

    @cached_property
    def drivers_by_city(self) -> dict[int, list[DriverRef]]:
        cities: dict[int, list[DriverRef]] = {}
        for d in self.drivers.values():
            cities.setdefault(d.city_id, []).append(d)
        return cities


def build_reference(
    customers: Sequence[CustomerRef],
    drivers: Sequence[DriverRef],
    restaurants: Sequence[tuple[int, int, Any, Any]],  # (id, city_id, lat, lon)
    products: Sequence[
        tuple[int, int, str, Decimal, int]
    ],  # (id, restaurant_id, nome, preço, prep)
    recipes: Sequence[tuple[int, int, Decimal]],  # (product_id, stock_item_id, quantidade)
    windows: Mapping[int, Sequence[Window]],
) -> Reference:
    """Só restaurante com perfil e com produto vendável entra (RN-23; F5.4, restaurante novo)."""
    recipe_by_product: dict[int, list[tuple[int, Decimal]]] = {}
    for product_id, stock_item_id, quantity in recipes:
        recipe_by_product.setdefault(product_id, []).append((stock_item_id, Decimal(quantity)))
    products_by_restaurant: dict[int, list[ProductRef]] = {}
    for product_id, restaurant_id, name, price, prep in products:
        recipe = recipe_by_product.get(product_id)
        if recipe:  # RN-37: produto sem ficha não é vendido
            products_by_restaurant.setdefault(restaurant_id, []).append(
                ProductRef(product_id, name, Decimal(price), int(prep), tuple(sorted(recipe)))
            )
    refs = {}
    for restaurant_id, city_id, lat, lon in restaurants:
        menu = products_by_restaurant.get(restaurant_id)
        win = windows.get(restaurant_id)
        if menu and win:
            refs[restaurant_id] = RestaurantRef(
                restaurant_id,
                city_id,
                Point(_coord(lat), _coord(lon)),
                tuple(sorted(win)),
                tuple(sorted(menu, key=lambda p: p.product_id)),
            )
    return Reference(
        customers={c.customer_id: c for c in customers},
        drivers={d.driver_id: d for d in drivers},
        restaurants=refs,
    )


class ReferenceLoader(Protocol):
    def load(self) -> Reference: ...


class DatabaseLoader:
    """Lê as três fontes; só leitura. `pg` também é a conexão de escrita do simulador."""

    def __init__(
        self, pg: Any, ora: Any, mongo: Any
    ) -> None:  # Any: conexões de drivers diferentes
        self.pg, self.ora, self.mongo = pg, ora, mongo

    def load(self) -> Reference:
        with self.ora.cursor() as cur:
            cur.execute(
                "SELECT customer_id, city_id, address_line1, latitude, longitude, signup_date "
                "FROM customers WHERE status = 'active'"
            )
            customers = [
                CustomerRef(int(i), int(c), a, Point(_coord(la), _coord(lo)), s)
                for i, c, a, la, lo, s in cur.fetchall()
            ]
            cur.execute(
                "SELECT driver_id, city_id, registration_date FROM drivers WHERE status = 'active'"
            )
            drivers = [DriverRef(int(i), int(c), r) for i, c, r in cur.fetchall()]
        with self.pg.cursor() as cur:
            restaurants = cur.execute(
                "SELECT restaurant_id, city_id, latitude, longitude FROM restaurants "
                "WHERE status = 'active'"
            ).fetchall()
            products = cur.execute(
                "SELECT product_id, restaurant_id, name, price, prep_time_min FROM products "
                "WHERE is_active"
            ).fetchall()
            recipes = cur.execute(
                "SELECT product_id, stock_item_id, quantity FROM product_recipes"
            ).fetchall()
        profiles = self.mongo["ubereats"]["restaurant_profiles"].find({}, {"service_windows": 1})
        windows = {int(p["_id"]): windows_of(p) for p in profiles}
        ref = build_reference(customers, drivers, restaurants, products, recipes, windows)
        log.info(
            "referência: %d clientes, %d motoristas, %d restaurantes com perfil e catálogo",
            len(ref.customers),
            len(ref.drivers),
            len(ref.restaurants),
        )
        return ref


class ReferenceCache:
    def __init__(
        self,
        loader: ReferenceLoader,
        refresh: timedelta,
        monotonic: Callable[[], float] = systime.monotonic,
    ) -> None:
        self._loader = loader
        self._refresh_s = refresh.total_seconds()
        self._monotonic = monotonic
        self._value: Reference | None = None
        self._loaded_at = 0.0

    def get(self) -> Reference:
        now = self._monotonic()
        if self._value is None or now - self._loaded_at >= self._refresh_s:
            self._value = self._loader.load()
            self._loaded_at = now
        return self._value
