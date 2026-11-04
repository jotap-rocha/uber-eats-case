"""Distância da entrega (RN-28; L4, decisão 2): menor rota restaurante(s) → cliente."""

from __future__ import annotations

import math
from collections.abc import Sequence
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from itertools import pairwise, permutations

EARTH_RADIUS_KM = 6371.0088


@dataclass(frozen=True)
class Point:
    latitude: Decimal
    longitude: Decimal


@dataclass(frozen=True)
class Stop:
    restaurant_id: int
    point: Point


@dataclass(frozen=True)
class Route:
    restaurant_ids: tuple[int, ...]
    distance_km: Decimal  # cabe em deliveries.distance_km numeric(6,2)


def haversine_km(a: Point, b: Point) -> float:
    lat1, lon1 = math.radians(float(a.latitude)), math.radians(float(a.longitude))
    lat2, lon2 = math.radians(float(b.latitude)), math.radians(float(b.longitude))
    h = (
        math.sin((lat2 - lat1) / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    )
    return 2 * EARTH_RADIUS_KM * math.asin(math.sqrt(h))


def shortest_route(stops: Sequence[Stop], customer: Point, detour_factor: Decimal) -> Route:
    """Testa todas as ordens dos restaurantes; desempate pela sequência de menor restaurant_id.

    A distância é a linha reta × `detour_factor`, arredondada a 0,01 km. Só a distância vai ao
    banco; a geometria é aproximação deliberada (o float não toca em dinheiro: a taxa usa o
    Decimal arredondado).
    """
    if not 1 <= len(stops) <= 2:
        raise ValueError("shortest_route: pedido tem 1 ou 2 restaurantes (RN-03)")
    best: tuple[float, tuple[int, ...]] | None = None
    for order in permutations(stops):
        points = [s.point for s in order] + [customer]
        length = sum(haversine_km(p, q) for p, q in pairwise(points))
        candidate = (round(length, 9), tuple(s.restaurant_id for s in order))
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    distance = (Decimal(repr(best[0])) * detour_factor).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    return Route(restaurant_ids=best[1], distance_km=distance)
