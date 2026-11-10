"""Cache de referência (F0.6): filtro da RN-23 e recarga pelo relógio de parede."""

from __future__ import annotations

from datetime import datetime, time, timedelta
from decimal import Decimal

from simulator.geo import Point
from simulator.reference import CustomerRef, Reference, ReferenceCache, build_reference

D = Decimal
WINDOWS = {1: [(time(11), time(15))], 2: [(time(18), time(23))]}


def test_so_restaurante_com_perfil_e_ficha_entra() -> None:
    ref = build_reference(
        customers=[CustomerRef(7, 3550308, "Rua", Point(D(0), D(0)), datetime(2020, 1, 1))],
        drivers=[],
        restaurants=[(1, 3550308, -23.55, -46.63), (2, 3550308, -23.56, -46.6), (3, 3550308, 0, 0)],
        products=[
            (10, 1, "A", D("5.00"), 5),
            (11, 1, "Sem ficha", D("1.00"), 1),
            (20, 2, "B", D("9"), 9),
        ],
        recipes=[(10, 100, D(1)), (20, 200, D("0.5"))],
        windows={**WINDOWS, 4: [(time(8), time(9))]},
    )
    assert set(ref.restaurants) == {1, 2}  # o 3 não tem perfil (RN-23)
    assert [p.product_id for p in ref.restaurants[1].products] == [
        10
    ]  # sem ficha não vende (RN-37)
    assert ref.restaurants[1].point == Point(D("-23.550000"), D("-46.630000"))
    assert ref.restaurants[1].open_at(datetime(2026, 10, 1, 11, 0))
    assert not ref.restaurants[1].open_at(datetime(2026, 10, 1, 15, 0))
    assert "Rua" not in repr(ref.customers[7])  # endereço fora de log


class CountingLoader:
    def __init__(self) -> None:
        self.calls = 0

    def load(self) -> Reference:
        self.calls += 1
        return Reference({}, {}, {})


def test_cache_recarrega_pelo_relogio_de_parede() -> None:
    loader, now = CountingLoader(), [0.0]
    cache = ReferenceCache(loader, timedelta(minutes=15), monotonic=lambda: now[0])
    cache.get()
    now[0] = 899.0
    cache.get()
    assert loader.calls == 1
    now[0] = 900.0
    cache.get()
    assert loader.calls == 2
