"""Regras puras: RN-16, transições, prazos da RN-28 (inclusive o congelamento do promised_at, T7)."""

from __future__ import annotations

from datetime import datetime, time, timedelta
from itertools import product

import pytest
from simulator.rules import (
    END_REASON_FROM,
    END_REASONS,
    RO_TRANSITIONS,
    AcceptedRO,
    allowed_ro_transition,
    can_accept,
    can_auto_confirm,
    can_auto_reject,
    can_customer_confirm,
    can_give_up,
    derive_order_status,
    is_late,
    is_open,
    promise_due,
    promised_at,
    restock_slots,
    tip_offered,
    travel_time,
    within_window,
)

T0 = datetime(2026, 10, 1, 12, 0)
RO_STATUSES = (
    "in_analysis",
    "accepted",
    "preparing",
    "ready_for_pickup",
    "picked_up",
    "cancelled",
    "rejected",
)

# Tabela "Pedido com dois atendimentos" das regras (01-regras-de-negocio.md), linha a linha.
TWO = {
    ("cancelled", "rejected"): "cancelled",
    ("in_analysis", "cancelled"): "in_analysis",
    ("accepted", "rejected"): "preparing",
    ("preparing", "cancelled"): "preparing",
    ("ready_for_pickup", "cancelled"): "ready_for_pickup",
    ("picked_up", "rejected"): "out_for_delivery",
    ("in_analysis", "in_analysis"): "in_analysis",
    ("in_analysis", "accepted"): "in_analysis",
    ("in_analysis", "preparing"): "in_analysis",
    ("in_analysis", "ready_for_pickup"): "partially_ready",
    ("in_analysis", "picked_up"): "partially_picked_up",
    ("accepted", "preparing"): "preparing",
    ("preparing", "preparing"): "preparing",
    ("accepted", "ready_for_pickup"): "partially_ready",
    ("preparing", "picked_up"): "partially_picked_up",
    ("ready_for_pickup", "ready_for_pickup"): "ready_for_pickup",
    ("ready_for_pickup", "picked_up"): "partially_picked_up",
    ("picked_up", "picked_up"): "out_for_delivery",
}


@pytest.mark.parametrize(("pair", "expected"), TWO.items())
def test_derivacao_rn16_tabela_das_regras(pair: tuple[str, str], expected: str) -> None:
    assert derive_order_status(list(pair)) == expected
    assert derive_order_status(list(reversed(pair))) == expected  # a ordem não importa


def test_derivacao_rn16_um_atendimento() -> None:
    expected = {
        "in_analysis": "in_analysis",
        "accepted": "preparing",
        "preparing": "preparing",
        "ready_for_pickup": "ready_for_pickup",
        "picked_up": "out_for_delivery",
        "cancelled": "cancelled",
        "rejected": "cancelled",
    }
    for status, order in expected.items():
        assert derive_order_status([status]) == order
    with pytest.raises(ValueError):
        derive_order_status([])


def test_derivacao_cobre_todas_as_combinacoes() -> None:
    for pair in product(RO_STATUSES, repeat=2):
        derive_order_status(list(pair))  # nenhuma combinação fica sem resposta


def test_transicoes_iguais_ao_t03c() -> None:
    assert len(RO_TRANSITIONS) == 8
    assert not allowed_ro_transition("ready_for_pickup", "cancelled")  # RN-13
    assert not allowed_ro_transition("picked_up", "cancelled")  # RN-14
    for reason, (status, _) in END_REASONS.items():
        for origin in END_REASON_FROM[reason]:
            assert allowed_ro_transition(origin, status), reason


def test_prazo_de_analise_no_limite_exato() -> None:
    timeout = timedelta(minutes=5)
    limit = T0 + timeout
    assert can_accept(T0, limit, timeout) and can_auto_reject(T0, limit, timeout)  # RN-27 decide
    assert not can_accept(T0, limit + timedelta(seconds=1), timeout)
    assert not can_auto_reject(T0, limit - timedelta(seconds=1), timeout)


def test_atraso_passando_do_estimado_mais_tolerancia() -> None:
    limit = T0 + timedelta(minutes=30)  # 20 min × 1,5
    assert not is_late(T0, 20, 0.5, limit)
    assert is_late(T0, 20, 0.5, limit + timedelta(seconds=1))


def test_promised_at_formula_rn28() -> None:
    ros = [AcceptedRO(T0, 20), AcceptedRO(T0 + timedelta(minutes=3), 15)]
    got = promised_at(ros, distance_km=5.0, speed_kmh=25, slack=timedelta(minutes=10))
    # último aceite (12:03) + maior estimado (20) + 5 km a 25 km/h (12 min) + folga (10)
    assert got == datetime(2026, 10, 1, 12, 45)


def test_promised_at_congelado_pelo_atendimento_que_cai() -> None:
    """T7: A aceito, B rejeitado depois; a base continua sendo o aceite de A (decisão 2026-11-09)."""
    statuses_before = ["accepted", "in_analysis"]
    statuses_after = ["accepted", "rejected"]
    assert not promise_due(statuses_before)
    assert promise_due(statuses_after)
    frozen = promised_at([AcceptedRO(T0, 20)], 0.0, 25, timedelta(minutes=10))
    assert frozen == T0 + timedelta(minutes=30)
    assert frozen >= T0  # T7a: nunca antes do último aceite
    assert not promise_due(["cancelled", "rejected"])  # sem ativo: sem prazo


def test_travel_time() -> None:
    assert travel_time(12.5, 25) == timedelta(minutes=30)
    with pytest.raises(ValueError):
        travel_time(1, 0)


def test_janelas_pos_entrega_inclusivas() -> None:
    window = timedelta(minutes=20)
    assert within_window(T0, T0 + window, window)
    assert not within_window(T0, T0 + window + timedelta(seconds=1), window)
    assert not within_window(T0, T0 - timedelta(seconds=1), window)


def test_confirmacao_manual_e_automatica_nao_se_sobrepoem() -> None:
    delay = timedelta(minutes=10)
    at = T0 + delay
    assert not can_customer_confirm(T0, at, delay) and can_auto_confirm(T0, at, delay)
    assert can_customer_confirm(T0, at - timedelta(seconds=1), delay)


def test_gorjeta_e_desistencia() -> None:
    assert tip_offered(None) and tip_offered(4) and not tip_offered(3)
    assert can_give_up(3, any_picked_up=False, max_give_ups=3)
    assert not can_give_up(4, any_picked_up=False, max_give_ups=3)
    assert not can_give_up(1, any_picked_up=True, max_give_ups=3)


def test_reposicao_fora_das_janelas() -> None:
    two = [(time(11), time(15)), (time(18), time(23))]
    assert restock_slots(two) == [time(10), time(16, 30)]
    assert restock_slots([(time(6, 30), time(14))]) == [time(5, 30)]
    assert restock_slots([(time(0, 30), time(14))]) == [time(0, 0)]
    for slots, windows in [(restock_slots(two), two)]:
        assert not any(is_open(windows, s) for s in slots)
    assert is_open(two, time(11)) and not is_open(two, time(15))  # [início, fim)
