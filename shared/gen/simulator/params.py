"""Leitura de shared/gen/parameters.yaml e de shared/gen/reference/cities.csv (F5.8)."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_PARAMETERS = REPO_ROOT / "shared" / "gen" / "parameters.yaml"

PAYMENT_METHODS = ("card", "pix", "wallet")


def _rate(value: Any, name: str) -> Decimal:
    if not isinstance(value, str):
        raise TypeError(f"{name}: dinheiro e percentual vão entre aspas no YAML (lido {value!r})")
    rate = Decimal(value)
    if not Decimal(0) <= rate <= Decimal(1):
        raise ValueError(f"{name}: percentual fora de [0, 1] ({rate})")
    return rate


def _money(value: Any, name: str) -> Decimal:
    if not isinstance(value, str):
        raise TypeError(f"{name}: dinheiro vai entre aspas no YAML (lido {value!r})")
    amount = Decimal(value)
    if amount < 0 or amount != amount.quantize(Decimal("0.01")):
        raise ValueError(f"{name}: valor em centavos e não negativo ({amount})")
    return amount


@dataclass(frozen=True)
class MoneyParams:
    tax_rate: Decimal
    service_fee_rate: Decimal
    payment_fee_rate: dict[str, Decimal]
    commission_rate: Decimal
    driver_share_rate: Decimal
    delivery_fee_base: Decimal
    delivery_fee_per_km: Decimal
    tip_min: Decimal
    tip_max: Decimal

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> MoneyParams:
        if raw.get("rounding") != "ROUND_HALF_UP":
            raise ValueError("money.rounding: só ROUND_HALF_UP é suportado (F5, decisão 4)")
        fees = raw["payment_fee_rate"]
        if set(fees) != set(PAYMENT_METHODS):
            raise ValueError(
                f"money.payment_fee_rate: esperado {PAYMENT_METHODS}, lido {sorted(fees)}"
            )
        params = cls(
            tax_rate=_rate(raw["tax_rate"], "tax_rate"),
            service_fee_rate=_rate(raw["service_fee_rate"], "service_fee_rate"),
            payment_fee_rate={m: _rate(fees[m], f"payment_fee_rate.{m}") for m in PAYMENT_METHODS},
            commission_rate=_rate(raw["commission_rate"], "commission_rate"),
            driver_share_rate=_rate(raw["driver_share_rate"], "driver_share_rate"),
            delivery_fee_base=_money(raw["delivery_fee_base"], "delivery_fee_base"),
            delivery_fee_per_km=_money(raw["delivery_fee_per_km"], "delivery_fee_per_km"),
            tip_min=_money(raw["tip_min"], "tip_min"),
            tip_max=_money(raw["tip_max"], "tip_max"),
        )
        if not Decimal(0) < params.tip_min <= params.tip_max:
            raise ValueError("money: tip_min precisa ser positivo e ≤ tip_max (RN-22)")
        return params


@dataclass(frozen=True)
class City:
    city_id: int
    name: str
    state_code: str
    center_latitude: Decimal
    center_longitude: Decimal


@dataclass(frozen=True)
class Parameters:
    raw: dict[str, Any]
    money: MoneyParams
    route_detour_factor: Decimal
    cities: tuple[City, ...]

    def section(self, name: str) -> dict[str, Any]:
        value = self.raw[name]
        if not isinstance(value, dict):
            raise TypeError(f"seção {name} ausente ou inválida")
        return value


def load_cities(path: Path) -> tuple[City, ...]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    cities = tuple(
        City(
            city_id=int(r["city_id"]),
            name=r["name"],
            state_code=r["state_code"],
            center_latitude=Decimal(r["center_latitude"]),
            center_longitude=Decimal(r["center_longitude"]),
        )
        for r in rows
    )
    ids = [c.city_id for c in cities]
    if not cities or len(set(ids)) != len(ids):
        raise ValueError(f"{path}: lista de cidades vazia ou com código repetido")
    for c in cities:
        # Mesmos limites dos CHECK de cities (F1.1 e F2.2).
        if not (
            1000000 <= c.city_id <= 5999999 and len(c.state_code) == 2 and c.state_code.isupper()
        ):
            raise ValueError(f"{path}: cidade inválida {c.city_id}")
    return cities


def load_parameters(path: Path = DEFAULT_PARAMETERS) -> Parameters:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    timing = raw["timing"]
    return Parameters(
        raw=raw,
        money=MoneyParams.from_dict(raw["money"]),
        route_detour_factor=Decimal(str(timing["route_detour_factor"])),
        cities=load_cities(REPO_ROOT / raw["scale"]["cities_file"]),
    )
