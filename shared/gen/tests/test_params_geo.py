"""Parâmetros versionados (F5.8), lista de cidades (F5.4) e menor rota (L4, decisão 2)."""

from __future__ import annotations

from decimal import Decimal

import pytest
from simulator.geo import Point, Stop, haversine_km, shortest_route
from simulator.params import MoneyParams, load_parameters

D = Decimal


def test_parametros_carregam_em_decimal() -> None:
    p = load_parameters()
    assert p.money.tax_rate == D("0.0800")
    assert p.money.payment_fee_rate["pix"] == D("0.0099")
    assert p.money.delivery_fee_base == D("4.99")
    assert p.route_detour_factor == D("1.3")
    assert p.section("timing")["analysis_timeout_min"] == 5


def test_cidades_do_csv() -> None:
    cities = load_parameters().cities
    assert [c.city_id for c in cities] == [3550308, 3304557, 3106200, 4106902, 4314902]
    assert {c.state_code for c in cities} == {"SP", "RJ", "MG", "PR", "RS"}


def test_dinheiro_em_float_e_recusado() -> None:
    raw = load_parameters().section("money") | {"tax_rate": 0.08}
    with pytest.raises(TypeError, match="aspas"):
        MoneyParams.from_dict(raw)


def test_arredondamento_diferente_e_recusado() -> None:
    raw = load_parameters().section("money") | {"rounding": "ROUND_HALF_EVEN"}
    with pytest.raises(ValueError, match="ROUND_HALF_UP"):
        MoneyParams.from_dict(raw)


SE = Point(D("-23.550520"), D("-46.633308"))  # Praça da Sé
PAULISTA = Point(D("-23.561414"), D("-46.655881"))


def test_haversine_ordem_de_grandeza() -> None:
    assert 2.4 < haversine_km(SE, PAULISTA) < 2.7


def test_rota_de_um_restaurante() -> None:
    route = shortest_route([Stop(10, SE)], PAULISTA, D("1.3"))
    assert route.restaurant_ids == (10,)
    assert route.distance_km == (D(repr(round(haversine_km(SE, PAULISTA), 9))) * D("1.3")).quantize(
        D("0.01")
    )


def test_rota_de_dois_escolhe_a_menor() -> None:
    perto = Point(D("-23.560000"), D("-46.650000"))
    longe = Point(D("-23.540000"), D("-46.620000"))
    route = shortest_route([Stop(1, perto), Stop(2, longe)], PAULISTA, D("1.0"))
    assert route.restaurant_ids == (2, 1)  # passa no mais longe primeiro e termina perto do cliente


def test_empate_vai_para_o_menor_restaurant_id() -> None:
    mesmo = Point(D("-23.550000"), D("-46.640000"))
    route = shortest_route([Stop(9, mesmo), Stop(3, mesmo)], PAULISTA, D("1.3"))
    assert route.restaurant_ids == (3, 9)


def test_rota_recusa_tres_restaurantes() -> None:
    with pytest.raises(ValueError):
        shortest_route([Stop(1, SE), Stop(2, SE), Stop(3, SE)], PAULISTA, D("1.3"))
