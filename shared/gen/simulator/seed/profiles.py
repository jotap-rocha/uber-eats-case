"""Perfil do restaurante no MongoDB (F3; RN-23, RN-41): janelas e cardápio com todos os produtos dele.

Determinístico por restaurante. O seed só regrava o documento quando janelas ou cardápio mudam,
para não gerar evento de CDC a cada execução; o created_at do documento existente é mantido.
"""

from __future__ import annotations

import random
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from simulator.seed.catalog import SECTIONS, Catalog

# Janelas possíveis (hora de Brasília). Nenhuma abre antes das 06:00: o restock inicial é às 00:00 (F5.4).
TWO_WINDOWS = (
    (("11:00", "15:00"), ("18:00", "23:00")),
    (("10:30", "14:30"), ("17:30", "22:00")),
    (("11:30", "15:30"), ("19:00", "23:30")),
)
ONE_WINDOW = (
    (("10:00", "22:00"),),
    (("11:00", "23:00"),),
    (("17:00", "23:30"),),
    (("06:30", "14:00"),),
)
HIGHLIGHT_SHARE = 0.15


@dataclass(frozen=True)
class MenuProduct:
    product_id: int
    name: str
    product_type: str


def build_profile(
    restaurant_id: int,
    cuisine_type: str,
    products: Sequence[MenuProduct],
    catalog: Catalog,
    two_windows_share: float,
) -> dict[str, Any]:  # Any: documento BSON (sem datas; quem grava acrescenta created_at/updated_at)
    if not products:
        raise ValueError(f"restaurante {restaurant_id} sem produtos: rode o seed de catálogo antes")
    rng = random.Random(f"profile:{restaurant_id}")
    options = TWO_WINDOWS if rng.random() < two_windows_share else ONE_WINDOW
    windows = rng.choice(options)
    ordered = sorted(products, key=lambda p: (SECTIONS.index(p.product_type), p.name, p.product_id))
    menu = []
    for order, product in enumerate(ordered, start=1):
        dish = catalog.dish(cuisine_type, product.name)
        menu.append(
            {
                "product_id": product.product_id,
                "section": product.product_type,
                "display_order": order,
                "highlighted": rng.random() < HIGHLIGHT_SHARE,
                "customizations": list(dish.customizations) if dish else [],
            }
        )
    return {
        "_id": restaurant_id,
        "service_windows": [{"start_time": a, "end_time": b} for a, b in windows],
        "menu_items": menu,
    }


def same_content(
    existing: Mapping[str, Any] | None, profile: Mapping[str, Any]
) -> bool:  # Any: BSON
    if existing is None:
        return False
    keys = ("service_windows", "menu_items")
    return all(_plain(existing.get(k)) == _plain(profile[k]) for k in keys)


def _plain(value: Any) -> Any:  # Any: BSON aninhado; Int64 compara igual a int
    if isinstance(value, Mapping):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_plain(v) for v in value]
    return value
