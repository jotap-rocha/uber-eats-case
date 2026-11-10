"""Regras de estado e de prazo, puras (RN-06 a RN-42; tabelas de transição das regras).

O simulador consulta estas funções dentro de cada comando, antes de gravar: todo limite é validado
no próprio comando, não só pelo agendador (RN-28, fronteiras). Sem I/O aqui.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from datetime import datetime, time, timedelta
from itertools import pairwise

# --- Atendimento -----------------------------------------------------------------------------

RO_DROPPED = frozenset({"cancelled", "rejected"})
RO_CANCELLABLE_BY_RESTAURANT = frozenset({"accepted", "preparing"})  # RN-13: até o fim do preparo
RO_TRANSITIONS = frozenset(
    {
        ("in_analysis", "accepted"),
        ("in_analysis", "rejected"),
        ("in_analysis", "cancelled"),
        ("accepted", "preparing"),
        ("accepted", "cancelled"),
        ("preparing", "cancelled"),
        ("preparing", "ready_for_pickup"),
        ("ready_for_pickup", "picked_up"),
    }
)

# end_reason → (status, ator) (L1b, tabela de motivos).
END_REASONS = {
    "restaurant_declined": ("rejected", "restaurant"),
    "out_of_stock": ("rejected", "restaurant"),
    "analysis_timeout": ("rejected", "platform"),
    "customer_request": ("cancelled", "customer"),
    "restaurant_late": ("cancelled", "customer"),
    "other_restaurant_dropped": ("cancelled", "customer"),
    "restaurant_issue": ("cancelled", "restaurant"),
}
# De onde cada motivo pode sair (RN-12, RN-13, RN-34; tabela de transições).
END_REASON_FROM = {
    "restaurant_declined": frozenset({"in_analysis"}),
    "out_of_stock": frozenset({"in_analysis"}),
    "analysis_timeout": frozenset({"in_analysis"}),
    "customer_request": frozenset({"in_analysis"}),
    "restaurant_late": frozenset({"accepted", "preparing"}),
    "other_restaurant_dropped": frozenset({"in_analysis", "accepted", "preparing"}),
    "restaurant_issue": RO_CANCELLABLE_BY_RESTAURANT,
}


def allowed_ro_transition(from_status: str, to_status: str) -> bool:
    return (from_status, to_status) in RO_TRANSITIONS


def is_active(status: str) -> bool:
    return status not in RO_DROPPED


# --- Pedido (RN-16) --------------------------------------------------------------------------

ORDER_DERIVED = frozenset(
    {
        "in_analysis",
        "preparing",
        "partially_ready",
        "ready_for_pickup",
        "partially_picked_up",
        "out_for_delivery",
        "cancelled",
    }
)
ORDER_BEFORE_DELIVERY = ORDER_DERIVED - {"out_for_delivery", "cancelled"}


def derive_order_status(statuses: Sequence[str]) -> str:
    """RN-16: condições em ordem, a primeira verdadeira vale; só os atendimentos ativos contam."""
    if not statuses:
        raise ValueError("derive_order_status: pedido sem atendimento (RN-04)")
    active = [s for s in statuses if is_active(s)]
    if not active:
        return "cancelled"
    picked = sum(s == "picked_up" for s in active)
    ready = sum(s == "ready_for_pickup" for s in active)
    if picked == len(active):
        return "out_for_delivery"
    if picked:
        return "partially_picked_up"
    if ready == len(active):
        return "ready_for_pickup"
    if ready:
        return "partially_ready"
    if "in_analysis" in active:
        return "in_analysis"
    return "preparing"


# --- Prazos (RN-24, RN-26, RN-28) -----------------------------------------------------------


def analysis_deadline(sent_at: datetime, timeout: timedelta) -> datetime:
    return sent_at + timeout


def can_accept(sent_at: datetime, at: datetime, timeout: timedelta) -> bool:
    """O aceite depois do limite é recusado; no limite exato vale o que chegou primeiro (RN-27)."""
    return at <= analysis_deadline(sent_at, timeout)


def can_auto_reject(sent_at: datetime, at: datetime, timeout: timedelta) -> bool:
    return at >= analysis_deadline(sent_at, timeout)


def late_after(accepted_at: datetime, estimated_prep_min: int, tolerance: float) -> datetime:
    """A partir de quando o atendimento está atrasado: estimado + tolerância, contado do aceite."""
    return accepted_at + timedelta(minutes=estimated_prep_min * (1 + tolerance))


def is_late(accepted_at: datetime, estimated_prep_min: int, tolerance: float, at: datetime) -> bool:
    return at > late_after(accepted_at, estimated_prep_min, tolerance)  # "passando do" estimado


def travel_time(distance_km: float, speed_kmh: float) -> timedelta:
    if speed_kmh <= 0 or distance_km < 0:
        raise ValueError("travel_time: velocidade positiva e distância não negativa")
    return timedelta(hours=distance_km / speed_kmh)


@dataclass(frozen=True)
class AcceptedRO:
    accepted_at: datetime
    estimated_prep_min: int


def promised_at(
    active: Iterable[AcceptedRO], distance_km: float, speed_kmh: float, slack: timedelta
) -> datetime:
    """RN-28: maior estimado + rota ÷ velocidade + folga, a partir do último aceite ativo.

    A base é o último `accepted_at` entre os ativos (decisão do bloco 5, 2026-11-09): recalculável
    só com as colunas gravadas, mesmo quando o congelamento vem de o outro atendimento cair.
    """
    active = list(active)
    if not active:
        raise ValueError("promised_at: sem atendimento ativo aceito")
    base = max(ro.accepted_at for ro in active)
    longest = max(ro.estimated_prep_min for ro in active)
    return base + timedelta(minutes=longest) + travel_time(distance_km, speed_kmh) + slack


def promise_due(statuses: Sequence[str]) -> bool:
    """Congela quando há ativo e nenhum ainda em análise (T7a)."""
    active = [s for s in statuses if is_active(s)]
    return bool(active) and "in_analysis" not in active


def within_window(finished_at: datetime, at: datetime, window: timedelta) -> bool:
    """Janelas do pós-entrega, limite inclusivo (RN-14, RN-26; T12)."""
    return finished_at <= at <= finished_at + window


def can_customer_confirm(finished_at: datetime, at: datetime, delay: timedelta) -> bool:
    return finished_at <= at < finished_at + delay


def can_auto_confirm(finished_at: datetime, at: datetime, delay: timedelta) -> bool:
    return at >= finished_at + delay


def tip_offered(driver_rating: int | None) -> bool:
    """RN-26: nota do motorista 3 ou menor tira a opção de gorjeta."""
    return driver_rating is None or driver_rating > 3


def can_give_up(assignment_number: int, any_picked_up: bool, max_give_ups: int) -> bool:
    """RN-07: só antes da primeira retirada, e a atribuição seguinte a 3 desistências não se desfaz."""
    return not any_picked_up and assignment_number <= max_give_ups


# --- Janelas de funcionamento e reposição (RN-40, RN-41) ------------------------------------

Window = tuple[time, time]


def is_open(windows: Sequence[Window], at: time) -> bool:
    return any(start <= at < end for start, end in windows)


def _shift(t: time, minutes: int) -> time:
    total = max(0, t.hour * 60 + t.minute + minutes)
    return time(total // 60, total % 60)


def restock_slots(windows: Sequence[Window], lead_min: int = 60) -> list[time]:
    """Antes da primeira janela do dia e no meio do intervalo entre janelas, nunca durante o serviço."""
    ordered = sorted(windows)
    if not ordered:
        return []
    slots = [_shift(ordered[0][0], -lead_min)]
    for (_, end), (start, _) in pairwise(ordered):
        gap = (start.hour * 60 + start.minute) - (end.hour * 60 + end.minute)
        if gap > 0:
            slots.append(_shift(end, gap // 2))
    return [s for s in slots if not is_open(ordered, s)]
