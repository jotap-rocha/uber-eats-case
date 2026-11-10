"""Dinheiro da compra e dos reembolsos (F5.7; RN-33, T8 e T9)."""

from __future__ import annotations

import random
from decimal import Decimal
from itertools import permutations

import pytest
from simulator.money import (
    Line,
    allocate,
    delivery_fee,
    partial_refund,
    price_purchase,
    round_cents,
    share,
)

D = Decimal


def test_round_half_up_em_centavos() -> None:
    assert round_cents(D("0.005")) == D("0.01")
    assert round_cents(D("0.015")) == D("0.02")  # HALF_EVEN daria 0.02 também; o próximo diferencia
    assert round_cents(D("0.025")) == D("0.03")  # HALF_EVEN daria 0.02
    assert round_cents(D("3.5988")) == D("3.60")


def test_exemplo_da_f57() -> None:
    lines = [
        Line(1, 1, D("10.00"), 1),
        Line(1, 2, D("15.00"), 1),
        Line(1, 3, D("4.99"), 1),
    ]
    p = price_purchase(lines, D("7.49"), D("0.0800"), D("0.1200"), D("0.0099"))
    got = [
        (c.component_type, c.restaurant_order_id, c.line_number, c.gross_amount, c.tax_amount)
        for c in p.components
    ]
    assert got == [
        ("item", 1, 1, D("10.00"), D("0.80")),
        ("service_fee", 1, 1, D("1.20"), D("0.10")),
        ("item", 1, 2, D("15.00"), D("1.20")),
        ("service_fee", 1, 2, D("1.80"), D("0.14")),
        ("item", 1, 3, D("4.99"), D("0.40")),
        ("service_fee", 1, 3, D("0.60"), D("0.05")),
        ("delivery_fee", None, None, D("7.49"), D("0.60")),
    ]
    assert [c.component_number for c in p.components] == list(range(1, 8))
    assert (p.items_amount, p.service_fee_amount, p.total_amount, p.tax_amount) == (
        D("29.99"),
        D("3.60"),
        D("41.08"),
        D("3.29"),
    )
    assert p.payment_fee_amount == D("0.41")


def test_ordem_dos_componentes_independe_da_ordem_de_entrada() -> None:
    lines = [Line(7, 2, D("3.00"), 2), Line(5, 1, D("9.90"), 1), Line(7, 1, D("12.50"), 3)]
    p = price_purchase(lines, D("6.00"), D("0.08"), D("0.12"), D("0.0299"))
    keys = [
        (c.restaurant_order_id, c.line_number) for c in p.components if c.component_type == "item"
    ]
    assert keys == [(5, 1), (7, 1), (7, 2)]


def _compra_sorteada(rng: random.Random) -> list[Line]:
    lines = []
    for ro in range(1, rng.randint(1, 2) + 1):
        for ln in range(1, rng.randint(1, 4) + 1):
            price = D(rng.randint(100, 9999)) / 100
            lines.append(Line(ro, ln, price, rng.randint(1, 3)))
    return lines


def test_invariantes_t8_em_compras_sorteadas() -> None:
    rng = random.Random(20261104)
    for _ in range(2000):
        lines = _compra_sorteada(rng)
        fee = D(rng.randint(499, 2500)) / 100
        p = price_purchase(lines, fee, D("0.0800"), D("0.1200"), D("0.0250"))
        gross = sum(c.gross_amount for c in p.components)
        tax = sum(c.tax_amount for c in p.components)
        service = sum(c.gross_amount for c in p.components if c.component_type == "service_fee")
        assert gross == p.total_amount
        assert tax == round_cents(p.total_amount * D("0.08"))
        assert service == round_cents(p.items_amount * D("0.12"))
        assert all(D(0) <= c.tax_amount <= c.gross_amount for c in p.components)
        assert sum(1 for c in p.components if c.component_type == "delivery_fee") == 1
        item_by_key = {(ln.restaurant_order_id, ln.line_number): ln.total_amount for ln in lines}
        for c in p.components:
            if c.component_type == "item":
                assert c.gross_amount == item_by_key[(c.restaurant_order_id, c.line_number)]


def test_allocate_soma_o_total_e_ultima_absorve() -> None:
    assert allocate(D("3.60"), [D("10.00"), D("15.00"), D("4.99")]) == [
        D("1.20"),
        D("1.80"),
        D("0.60"),
    ]
    assert sum(allocate(D("0.01"), [D(1), D(1), D(1)])) == D("0.01")
    with pytest.raises(ValueError):
        allocate(D("1.00"), [])


def test_partial_refund_tres_incidentes_de_uma_unidade() -> None:
    parts = [partial_refund(D("10.00"), D("0.80"), 3, r, 1) for r in range(3)]
    assert [g for g, _ in parts] == [D("3.33"), D("3.34"), D("3.33")]
    assert sum(g for g, _ in parts) == D("10.00")
    assert sum(t for _, t in parts) == D("0.80")


def test_t9_reembolso_nao_depende_da_ordem() -> None:
    """Todas as ordens de incidentes parciais devolvem o mesmo total e fecham o componente."""
    rng = random.Random(7)
    for _ in range(300):
        quantity_total = rng.randint(2, 6)
        gross = D(rng.randint(1, 50000)) / 100
        tax = round_cents(gross * D("0.08"))
        cuts: list[int] = []
        left = quantity_total
        while left:
            q = rng.randint(1, left)
            cuts.append(q)
            left -= q
        totals = set()
        for order in set(permutations(cuts)):
            refunded, g_sum, t_sum = 0, D(0), D(0)
            for q in order:
                g, t = partial_refund(gross, tax, quantity_total, refunded, q)
                assert g >= 0 and D(0) <= t <= g + D("0.01")
                refunded += q
                g_sum += g
                t_sum += t
            assert (g_sum, t_sum) == (gross, tax)
            totals.add((g_sum, t_sum))
        assert len(totals) == 1


def test_partial_refund_recusa_devolver_mais_que_o_comprado() -> None:
    with pytest.raises(ValueError):
        partial_refund(D("10.00"), D("0.80"), 2, 1, 2)


def test_taxa_de_entrega_e_parcelas() -> None:
    assert delivery_fee(D("3.27"), D("4.99"), D("1.00")) == D("8.26")
    assert share(D("29.99"), D("0.25")) == D("7.50")  # comissão: 7,4975
    assert share(D("7.49"), D("0.80")) == D("5.99")  # parte do motorista: 5,992


@pytest.mark.parametrize(
    "lines,fee",
    [
        ([], D("5.00")),
        ([Line(1, 1, D("1.00"), 1)], D("0")),
        ([Line(1, 1, D("1.001"), 1)], D("5.00")),
        ([Line(1, 1, D("1.00"), 1), Line(1, 1, D("2.00"), 1)], D("5.00")),
    ],
)
def test_price_purchase_recusa_entrada_invalida(lines: list[Line], fee: Decimal) -> None:
    with pytest.raises(ValueError):
        price_purchase(lines, fee, D("0.08"), D("0.12"), D("0.01"))
