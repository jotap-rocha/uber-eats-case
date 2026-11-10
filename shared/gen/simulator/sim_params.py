"""Parâmetros do simulador lidos do parameters.yaml (F5.8 e a seção `simulation`), já validados.

Probabilidades e tempos são float (não tocam em dinheiro); dinheiro continua em MoneyParams.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import timedelta
from decimal import Decimal
from pathlib import Path
from typing import Any

import yaml

from simulator.params import (
    DEFAULT_PARAMETERS,
    PAYMENT_METHODS,
    REPO_ROOT,
    Parameters,
    load_parameters,
)

INCIDENT_REASONS = (
    "missing_item",
    "wrong_item",
    "food_quality",
    "late_delivery",
    "not_received",
    "driver_unable",
)
DELIVERY_REASONS = frozenset({"late_delivery", "not_received", "driver_unable"})  # L3, decisão 6


def _prob(value: Any, name: str) -> float:  # Any: valor cru do YAML
    p = float(value)
    if not 0.0 <= p <= 1.0:
        raise ValueError(f"{name}: probabilidade fora de [0, 1] ({p})")
    return p


def _range(value: Any, name: str) -> tuple[float, float]:  # Any: valor cru do YAML
    low, high = (float(v) for v in value)
    if not 0 <= low <= high:
        raise ValueError(f"{name}: intervalo inválido [{low}, {high}]")
    return low, high


def _int_range(value: Any, name: str) -> tuple[int, int]:  # Any: valor cru do YAML
    low, high = (int(v) for v in value)
    if not 1 <= low <= high:
        raise ValueError(f"{name}: intervalo inválido [{low}, {high}]")
    return low, high


def _shares(raw: Mapping[str, Any], keys: tuple[str, ...], name: str) -> dict[str, float]:
    if set(raw) != set(keys):
        raise ValueError(f"{name}: esperado {sorted(keys)}, lido {sorted(raw)}")
    shares = {k: _prob(raw[k], f"{name}.{k}") for k in keys}
    if abs(sum(shares.values()) - 1.0) > 1e-9:
        raise ValueError(f"{name}: as frações precisam somar 1")
    return shares


@dataclass(frozen=True)
class Demand:
    peak_orders_per_hour_per_city: float
    hourly_factor: Mapping[int, float]
    second_restaurant_share: float
    items_per_restaurant_order: tuple[int, int]
    quantity_per_item: tuple[int, int]
    drivers_per_hourly_order: float

    def orders_per_hour(self, hour: int) -> float:
        return self.peak_orders_per_hour_per_city * self.hourly_factor[hour]


@dataclass(frozen=True)
class Behavior:
    attempt_declined: float
    max_payment_attempts: int
    customer_cancels_in_analysis: float
    restaurant_declines: float
    restaurant_ignores: float
    restaurant_issue_after_accept: float
    prep_overrun_lognormal_sigma: float
    driver_gives_up: float
    customer_absent: float
    driver_unable: float
    customer_confirms: float
    incident: float
    incident_upheld: float
    driver_rating: float
    restaurant_rating: float
    tip: float
    shift_hours: tuple[float, float]
    payment_method_share: Mapping[str, float]
    customer_cancels_late: float
    customer_cancels_other_after_drop: float
    rating_weights: Mapping[int, float]
    rating_comment: float
    max_incidents_per_order: int
    incident_reason_share: Mapping[str, float]


@dataclass(frozen=True)
class Timing:
    incident_window: timedelta
    rating_tip_window: timedelta
    auto_confirm_delay: timedelta
    analysis_timeout: timedelta
    prep_tolerance: float
    max_restaurants_per_order: int
    max_driver_give_ups: int
    average_speed_kmh: float
    promise_slack: timedelta
    route_detour_factor: Decimal
    profile_cache_refresh: timedelta


@dataclass(frozen=True)
class Delays:
    payment_retry_s: tuple[float, float]
    restaurant_response_min: tuple[float, float]
    prep_start_delay_min: tuple[float, float]
    driver_to_restaurant_min: tuple[float, float]
    pickup_handover_min: tuple[float, float]
    travel_lognormal_sigma: float
    customer_absent_wait_min: tuple[float, float]
    incident_review_delay_min: tuple[float, float]
    incident_decision_delay_min: tuple[float, float]
    late_cancel_delay_min: tuple[float, float]
    shift_open_jitter_min: tuple[float, float]


@dataclass(frozen=True)
class Stock:
    restock_target_days: int
    restock_trigger: float
    consumption_window_days: int


@dataclass(frozen=True)
class Texts:
    rating_comments: Mapping[str, Mapping[str, tuple[str, ...]]]  # ator → faixa → frases
    incident_descriptions: Mapping[str, tuple[str, ...]]  # motivo → frases


@dataclass(frozen=True)
class SimParams:
    demand: Demand
    behavior: Behavior
    timing: Timing
    delays: Delays
    stock: Stock
    texts: Texts


def _load_texts(text: Mapping[str, Any]) -> Texts:
    comments = yaml.safe_load((REPO_ROOT / text["rating_comment_by_band"]).read_text("utf-8"))
    incidents = yaml.safe_load(
        (REPO_ROOT / text["incident_description_by_reason"]).read_text("utf-8")
    )
    if set(comments) != {"driver", "restaurant"} or any(
        set(bands) != {"low", "mid", "high"} or not all(bands.values())
        for bands in comments.values()
    ):
        raise ValueError(
            "rating_comments: esperado driver/restaurant × low/mid/high, sem lista vazia"
        )
    if set(incidents) != set(INCIDENT_REASONS) or not all(incidents.values()):
        raise ValueError("incident_descriptions: uma lista não vazia por motivo do incidente")
    return Texts(
        rating_comments={
            a: {b: tuple(v) for b, v in bands.items()} for a, bands in comments.items()
        },
        incident_descriptions={r: tuple(v) for r, v in incidents.items()},
    )


def _delays(raw: Mapping[str, Any]) -> Delays:  # Any: valores crus do YAML
    def r(key: str) -> tuple[float, float]:
        return _range(raw[key], key)

    return Delays(
        payment_retry_s=r("payment_retry_s"),
        restaurant_response_min=r("restaurant_response_min"),
        prep_start_delay_min=r("prep_start_delay_min"),
        driver_to_restaurant_min=r("driver_to_restaurant_min"),
        pickup_handover_min=r("pickup_handover_min"),
        travel_lognormal_sigma=float(raw["travel_lognormal_sigma"]),
        customer_absent_wait_min=r("customer_absent_wait_min"),
        incident_review_delay_min=r("incident_review_delay_min"),
        incident_decision_delay_min=r("incident_decision_delay_min"),
        late_cancel_delay_min=r("late_cancel_delay_min"),
        shift_open_jitter_min=r("shift_open_jitter_min"),
    )


def sim_params(params: Parameters) -> SimParams:
    demand, behavior = params.section("demand"), params.section("behavior")
    timing, delays = params.section("timing"), params.section("simulation")
    stock, text = params.section("stock"), params.section("text")
    factors = demand["hourly_factor"]
    default = float(demand["default_hourly_factor"])
    weights = {
        int(k): _prob(v, f"rating_weights.{k}") for k, v in behavior["rating_weights"].items()
    }
    if set(weights) != {1, 2, 3, 4, 5} or abs(sum(weights.values()) - 1) > 1e-9:
        raise ValueError("rating_weights: notas 1 a 5 com soma 1 (RN-26)")
    parsed = SimParams(
        demand=Demand(
            peak_orders_per_hour_per_city=float(demand["peak_orders_per_hour_per_city"]),
            hourly_factor={
                h: float(factors.get(str(h), factors.get(f"{h:02d}", default))) for h in range(24)
            },
            second_restaurant_share=_prob(
                demand["second_restaurant_share"], "second_restaurant_share"
            ),
            items_per_restaurant_order=_int_range(demand["items_per_restaurant_order"], "items"),
            quantity_per_item=_int_range(demand["quantity_per_item"], "quantity_per_item"),
            drivers_per_hourly_order=float(demand["drivers_per_hourly_order"]),
        ),
        behavior=Behavior(
            attempt_declined=_prob(behavior["attempt_declined"], "attempt_declined"),
            max_payment_attempts=int(behavior["max_payment_attempts"]),
            customer_cancels_in_analysis=_prob(behavior["customer_cancels_in_analysis"], "cancel"),
            restaurant_declines=_prob(behavior["restaurant_declines"], "restaurant_declines"),
            restaurant_ignores=_prob(behavior["restaurant_ignores"], "restaurant_ignores"),
            restaurant_issue_after_accept=_prob(behavior["restaurant_issue_after_accept"], "issue"),
            prep_overrun_lognormal_sigma=float(behavior["prep_overrun_lognormal_sigma"]),
            driver_gives_up=_prob(behavior["driver_gives_up"], "driver_gives_up"),
            customer_absent=_prob(behavior["customer_absent"], "customer_absent"),
            driver_unable=_prob(behavior["driver_unable"], "driver_unable"),
            customer_confirms=_prob(behavior["customer_confirms"], "customer_confirms"),
            incident=_prob(behavior["incident"], "incident"),
            incident_upheld=_prob(behavior["incident_upheld"], "incident_upheld"),
            driver_rating=_prob(behavior["driver_rating"], "driver_rating"),
            restaurant_rating=_prob(behavior["restaurant_rating"], "restaurant_rating"),
            tip=_prob(behavior["tip"], "tip"),
            shift_hours=_range(behavior["shift_hours"], "shift_hours"),
            payment_method_share=_shares(
                behavior["payment_method_share"], PAYMENT_METHODS, "payment_method_share"
            ),
            customer_cancels_late=_prob(behavior["customer_cancels_late"], "customer_cancels_late"),
            customer_cancels_other_after_drop=_prob(
                behavior["customer_cancels_other_after_drop"], "customer_cancels_other_after_drop"
            ),
            rating_weights=weights,
            rating_comment=_prob(behavior["rating_comment"], "rating_comment"),
            max_incidents_per_order=int(behavior["max_incidents_per_order"]),
            incident_reason_share=_shares(
                behavior["incident_reason_share"], INCIDENT_REASONS, "incident_reason_share"
            ),
        ),
        timing=Timing(
            incident_window=timedelta(hours=float(timing["incident_window_h"])),
            rating_tip_window=timedelta(minutes=float(timing["rating_tip_window_min"])),
            auto_confirm_delay=timedelta(minutes=float(timing["auto_confirm_delay_min"])),
            analysis_timeout=timedelta(minutes=float(timing["analysis_timeout_min"])),
            prep_tolerance=float(timing["prep_tolerance"]),
            max_restaurants_per_order=int(timing["max_restaurants_per_order"]),
            max_driver_give_ups=int(timing["max_driver_give_ups"]),
            average_speed_kmh=float(timing["average_speed_kmh"]),
            promise_slack=timedelta(minutes=float(timing["promise_slack_min"])),
            route_detour_factor=params.route_detour_factor,
            profile_cache_refresh=timedelta(minutes=float(timing["profile_cache_refresh_min"])),
        ),
        delays=_delays(delays),
        stock=Stock(
            restock_target_days=int(stock["restock_target_days"]),
            restock_trigger=_prob(stock["restock_trigger"], "restock_trigger"),
            consumption_window_days=int(stock["consumption_window_days"]),
        ),
        texts=_load_texts(text),
    )
    if parsed.timing.max_restaurants_per_order != 2:
        raise ValueError("max_restaurants_per_order: a RN-03 fixa 2 (o DDL e a rota supõem isso)")
    b = parsed.behavior
    if b.customer_cancels_in_analysis + b.restaurant_declines + b.restaurant_ignores > 1:
        raise ValueError("behavior: desfechos da análise somam mais que 1")
    if b.customer_absent + b.driver_unable > 1:
        raise ValueError("behavior: desfechos da entrega somam mais que 1")
    if b.max_payment_attempts < 1 or b.max_incidents_per_order < 0:
        raise ValueError("behavior: max_payment_attempts ≥ 1 e max_incidents_per_order ≥ 0")
    return parsed


def load_sim_params(path: Path = DEFAULT_PARAMETERS) -> SimParams:
    return sim_params(load_parameters(path))
