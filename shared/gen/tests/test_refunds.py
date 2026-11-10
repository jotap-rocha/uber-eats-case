"""Reembolsos por origem (RN-14, RN-21, RN-30, RN-33) e o T9 de ordem (F5.9)."""

from __future__ import annotations

import random
from decimal import Decimal
from itertools import permutations

import pytest
from simulator.money import Line, price_purchase
from simulator.refunds import (
    Ledger,
    PaidComponent,
    RefundPlan,
    for_incident,
    for_remaining,
    for_restaurant_order,
)

D = Decimal
RATES = (D("0.08"), D("0.12"), D("0.0299"))
DELIVERY_FEE = D("7.49")


def ledger_for(lines: list[Line], delivery_fee: Decimal = DELIVERY_FEE) -> Ledger:
    pricing = price_purchase(lines, delivery_fee, *RATES)
    qty = {(ln.restaurant_order_id, ln.line_number): ln.quantity for ln in lines}
    return Ledger(
        tuple(
            PaidComponent(
                c.component_number,
                c.component_type,
                c.restaurant_order_id,
                c.line_number,
                c.gross_amount,
                c.tax_amount,
                qty.get((c.restaurant_order_id, c.line_number))
                if c.restaurant_order_id is not None and c.line_number is not None
                else None,
            )
            for c in pricing.components
        )
    )


def apply(ledger: Ledger, plan: RefundPlan) -> None:
    ledger.apply(plan.lines, plan.units)


def total_paid(ledger: Ledger) -> Decimal:
    return sum((c.gross_amount for c in ledger.components), D(0))


def assert_t9(ledger: Ledger) -> None:
    for c in ledger.components:
        done = ledger.refunded[c.component_number]
        assert D(0) <= done.gross <= c.gross_amount  # T9a
        assert D(0) <= done.tax <= c.tax_amount
    assert ledger.total_refunded <= total_paid(ledger)  # T9b


LINES = [Line(1, 1, D("10.00"), 1), Line(1, 2, D("15.00"), 1), Line(2, 1, D("4.99"), 3)]


def test_cancelamento_parcial_e_total_rn21() -> None:
    ledger = ledger_for(LINES)
    first = for_restaurant_order(ledger, 2, last_active=False)
    assert {ln.component_number for ln in first.lines} == {
        c.component_number for c in ledger.components if c.restaurant_order_id == 2
    }
    apply(ledger, first)
    second = for_restaurant_order(ledger, 1, last_active=True)  # leva a taxa de entrega
    apply(ledger, second)
    assert ledger.total_refunded == total_paid(ledger)  # T9c: estorno exato do pagamento
    assert sum((r.tax for r in ledger.refunded.values()), D(0)) == sum(
        (c.tax_amount for c in ledger.components), D(0)
    )
    with pytest.raises(ValueError):
        for_restaurant_order(ledger, 1, last_active=True)  # nada mais a devolver


def test_incidente_parcial_fecha_o_componente() -> None:
    # 3 × 2,78 = 8,34; taxa de serviço round(8,34 × 0,12) = 1,00, devolvida uma unidade por vez.
    ledger = ledger_for([Line(1, 1, D("2.78"), 3)])
    items, services = [], []
    for _ in range(3):
        plan = for_incident(ledger, {(1, 1): 1}, include_delivery_fee=False)
        item = next(ln for ln in plan.lines if ln.quantity is not None)
        service = next(ln for ln in plan.lines if ln.quantity is None)
        assert item.quantity == 1  # T14b
        items.append(item.gross_amount)
        services.append(service.gross_amount)
        apply(ledger, plan)
    assert items == [D("2.78")] * 3  # bruto do item é preço × quantidade: divide exato
    assert services == [D("0.33"), D("0.34"), D("0.33")]  # diferença de acumulados (F5.7 #8)
    assert_t9(ledger)
    with pytest.raises(ValueError):
        for_incident(ledger, {(1, 1): 1}, include_delivery_fee=False)  # passa do comprado


def test_incidente_de_entrega_e_restante() -> None:
    ledger = ledger_for(LINES)
    late = for_incident(ledger, {}, include_delivery_fee=True)
    assert [ln.component_number for ln in late.lines] == [
        c.component_number for c in ledger.components if c.component_type == "delivery_fee"
    ]
    apply(ledger, late)
    apply(ledger, for_incident(ledger, {(2, 1): 2}, include_delivery_fee=False))
    rest = for_remaining(ledger)  # RN-30: o que sobrou
    apply(ledger, rest)
    assert ledger.total_refunded == total_paid(ledger)
    item_line = next(ln for ln in rest.lines if ln.component_number == 5)
    assert item_line.quantity == 1  # das 3 unidades, 2 já tinham voltado
    assert_t9(ledger)


def _random_lines(rng: random.Random) -> list[Line]:
    lines = []
    for ro in range(1, rng.randint(1, 2) + 1):
        for ln in range(1, rng.randint(1, 4) + 1):
            price = D(rng.randint(100, 6000)) / 100
            lines.append(Line(ro, ln, price, rng.randint(1, 3)))
    return lines


def test_t9_resultado_nao_depende_da_ordem() -> None:
    """Propriedade: todas as permutações de cancelamentos e incidentes fecham no mesmo total."""
    rng = random.Random(9)
    for _ in range(30):
        lines = _random_lines(rng)
        ros = sorted({ln.restaurant_order_id for ln in lines})
        events: list[tuple[str, object]] = [("cancel", ro) for ro in ros[1:]]
        target = [ln for ln in lines if ln.restaurant_order_id == ros[0]]
        for ln in target:  # incidentes de uma unidade até devolver tudo
            events += [("incident", (ln.restaurant_order_id, ln.line_number))] * ln.quantity
        events.append(("late", None))
        events = events[:6]  # 6! = 720 ordens no pior caso
        totals = set()
        for order in permutations(range(len(events))):
            ledger = ledger_for(lines)
            for i in order:
                kind, arg = events[i]
                if kind == "cancel":
                    assert isinstance(arg, int)
                    plan = for_restaurant_order(ledger, arg, last_active=False)
                elif kind == "incident":
                    assert isinstance(arg, tuple)
                    plan = for_incident(ledger, {arg: 1}, include_delivery_fee=False)
                else:
                    plan = for_incident(ledger, {}, include_delivery_fee=True)
                apply(ledger, plan)
                assert_t9(ledger)
            totals.add(tuple((n, r.gross, r.tax) for n, r in sorted(ledger.refunded.items())))
        assert len(totals) == 1
