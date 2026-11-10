"""Fundação do simulador: código de rastreio (F0.3), relógio (F5.6), agenda (F5.5) e parâmetros."""

from __future__ import annotations

import re
from datetime import datetime, timedelta

import pytest
from simulator.agenda import Agenda, Task
from simulator.clock import SimClock
from simulator.params import load_parameters
from simulator.sim_params import DELIVERY_REASONS, INCIDENT_REASONS, load_sim_params, sim_params
from simulator.tracking import tracking_code

FORMATO = re.compile(r"^[0-9A-HJKMNP-TV-Z]{12}$")  # o mesmo CHECK de orders e payments (F1.2)
T0 = datetime(2026, 10, 1, 0, 0)


def test_tracking_formato_e_determinismo() -> None:
    codes = {tracking_code(i, "sal-teste") for i in range(1, 5001)}
    assert len(codes) == 5000
    assert all(FORMATO.match(c) for c in codes)
    assert tracking_code(42, "sal-teste") == tracking_code(42, "sal-teste")
    assert tracking_code(42, "sal-teste") != tracking_code(42, "outro-sal")


def test_tracking_valor_conhecido() -> None:
    # Fixa o algoritmo: mudar a forma de calcular muda o código de todo pedido já gravado.
    # Conferido à parte: 60 bits mais altos de sha256("abc:1"), 5 bits por caractere.
    assert tracking_code(1, "abc") == "QZ7GQ75YKP10"


@pytest.mark.parametrize(("entity_id", "salt"), [(0, "s"), (-1, "s"), (1, "")])
def test_tracking_recusa_entrada_invalida(entity_id: int, salt: str) -> None:
    with pytest.raises(ValueError):
        tracking_code(entity_id, salt)


class FakeWall:
    def __init__(self, now: datetime) -> None:
        self.now = now
        self.sleeps: list[float] = []

    def __call__(self) -> datetime:
        return self.now

    def sleep(self, seconds: float) -> bool:
        self.sleeps.append(seconds)
        self.now += timedelta(seconds=seconds)
        return False


def test_relogio_historico_nao_dorme() -> None:
    wall = FakeWall(T0 + timedelta(days=30))
    clock = SimClock(T0, wall=wall, sleep=wall.sleep)
    assert clock.advance_to(T0 + timedelta(days=29))
    assert clock.now == T0 + timedelta(days=29) and wall.sleeps == []
    assert not clock.realtime


def test_relogio_tempo_real_espera_o_relogio_de_parede() -> None:
    wall = FakeWall(T0)
    clock = SimClock(T0, wall=wall, sleep=wall.sleep)
    assert clock.advance_to(T0 + timedelta(seconds=75))
    assert clock.now == T0 + timedelta(seconds=75)
    assert sum(wall.sleeps) == pytest.approx(75) and max(wall.sleeps) <= 30
    assert clock.realtime


def test_relogio_nunca_volta_e_para_limpo() -> None:
    wall = FakeWall(T0)
    clock = SimClock(T0 + timedelta(hours=1), wall=lambda: T0, sleep=lambda s: True)
    assert clock.advance_to(T0)  # no passado: fica onde está
    assert clock.now == T0 + timedelta(hours=1)
    assert not clock.advance_to(T0 + timedelta(hours=2))  # parada pedida durante a espera
    assert clock.now == T0 + timedelta(hours=1)
    del wall


def test_agenda_por_instante_e_ordem_de_chegada() -> None:
    agenda = Agenda()
    seen: list[str] = []
    for name, minutes in [("b", 5), ("a", 1), ("c", 5), ("d", 0)]:
        agenda.push(Task(T0 + timedelta(minutes=minutes), name, lambda n=name: seen.append(n)))
    assert agenda.peek_time() == T0
    while agenda:
        agenda.pop().run()
    assert seen == ["d", "a", "b", "c"]
    assert agenda.peek_time() is None


def test_parametros_do_simulador() -> None:
    p = load_sim_params()
    assert p.timing.analysis_timeout == timedelta(minutes=5)  # regras fixas (RN-28, RN-24, RN-26)
    assert p.timing.auto_confirm_delay == timedelta(minutes=10)
    assert p.timing.rating_tip_window == timedelta(minutes=20)
    assert p.timing.incident_window == timedelta(hours=24)
    assert p.timing.max_driver_give_ups == 3
    assert p.demand.orders_per_hour(12) == 30 and p.demand.orders_per_hour(4) == 30 * 0.2
    assert set(p.behavior.incident_reason_share) == set(INCIDENT_REASONS)
    assert DELIVERY_REASONS < set(INCIDENT_REASONS)
    assert all(p.texts.incident_descriptions[r] for r in INCIDENT_REASONS)


def test_parametros_invalidos_sao_recusados() -> None:
    params = load_parameters()
    raw = {**params.raw, "behavior": {**params.raw["behavior"], "tip": 1.5}}
    with pytest.raises(ValueError, match="tip"):
        sim_params(type(params)(raw, params.money, params.route_detour_factor, params.cities))
    shares = {"card": 0.5, "pix": 0.3, "wallet": 0.1}
    raw = {**params.raw, "behavior": {**params.raw["behavior"], "payment_method_share": shares}}
    with pytest.raises(ValueError, match="somar 1"):
        sim_params(type(params)(raw, params.money, params.route_detour_factor, params.cities))
