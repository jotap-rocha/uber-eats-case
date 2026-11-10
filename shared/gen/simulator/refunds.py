"""Reembolso por origem a partir dos componentes congelados na compra (RN-14, RN-21, RN-30, RN-33).

Puro: recebe os componentes do pagamento e o que já foi devolvido, devolve as linhas de
refund_components. O componente inteiro devolve bruto e imposto exatos; o parcial usa diferença de
acumulados (F5.7 #8), então o total não depende da ordem dos cancelamentos e incidentes (T9).
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from decimal import Decimal

from simulator.money import ZERO, partial_refund

ItemKey = tuple[int, int]  # (restaurant_order_id, line_number)


@dataclass(frozen=True)
class PaidComponent:
    component_number: int
    component_type: str
    restaurant_order_id: int | None
    line_number: int | None
    gross_amount: Decimal
    tax_amount: Decimal
    quantity: int | None  # quantidade comprada do item (item e service_fee); None no delivery_fee

    @property
    def item_key(self) -> ItemKey | None:
        if self.restaurant_order_id is None or self.line_number is None:
            return None
        return (self.restaurant_order_id, self.line_number)


@dataclass
class Refunded:
    """Acumulado já devolvido de um componente."""

    gross: Decimal = ZERO
    tax: Decimal = ZERO
    units: int = 0


@dataclass(frozen=True)
class RefundLine:
    component_number: int
    quantity: int | None  # só em componente `item` (refund_components.quantity, T14b)
    gross_amount: Decimal
    tax_amount: Decimal


@dataclass
class Ledger:
    """Componentes de um pagamento e o acumulado devolvido de cada um."""

    components: tuple[PaidComponent, ...]
    refunded: dict[int, Refunded] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for c in self.components:
            self.refunded.setdefault(c.component_number, Refunded())

    def remaining(self, c: PaidComponent) -> tuple[Decimal, Decimal, int]:
        done = self.refunded[c.component_number]
        units = (c.quantity or 0) - done.units
        return c.gross_amount - done.gross, c.tax_amount - done.tax, units

    def apply(self, lines: Iterable[RefundLine], units: Mapping[int, int] | None = None) -> None:
        """Soma as linhas ao acumulado; `units` = unidades devolvidas por componente."""
        units = units or {}
        for line in lines:
            done = self.refunded[line.component_number]
            done.gross += line.gross_amount
            done.tax += line.tax_amount
        for number, n in units.items():
            self.refunded[number].units += n

    @property
    def total_refunded(self) -> Decimal:
        return sum((r.gross for r in self.refunded.values()), ZERO)


@dataclass(frozen=True)
class RefundPlan:
    lines: tuple[RefundLine, ...]
    units: Mapping[int, int]  # component_number → unidades devolvidas (item e service_fee)

    @property
    def total_amount(self) -> Decimal:
        return sum((ln.gross_amount for ln in self.lines), ZERO)


def _line(
    c: PaidComponent, gross: Decimal, tax: Decimal, quantity: int | None
) -> RefundLine | None:
    if gross < 0 or tax < 0:
        raise ArithmeticError(f"reembolso negativo no componente {c.component_number}")
    if gross == 0:
        if tax != 0:
            raise ArithmeticError(f"imposto sem bruto no componente {c.component_number}")
        return None  # nada a devolver: refund_components exige bruto > 0
    if tax > gross:
        raise ArithmeticError(f"imposto acima do bruto no componente {c.component_number}")
    return RefundLine(
        c.component_number, quantity if c.component_type == "item" else None, gross, tax
    )


def _whole(ledger: Ledger, c: PaidComponent) -> tuple[RefundLine | None, int]:
    gross, tax, units = ledger.remaining(c)
    return _line(c, gross, tax, units if c.quantity else None), max(units, 0)


def _plan(entries: Iterable[tuple[RefundLine | None, int, int]]) -> RefundPlan:
    lines, units = [], {}
    for line, number, n in entries:
        if n:
            units[number] = n
        if line is not None:
            lines.append(line)
    return RefundPlan(tuple(sorted(lines, key=lambda ln: ln.component_number)), units)


def for_restaurant_order(ledger: Ledger, restaurant_order_id: int, last_active: bool) -> RefundPlan:
    """RN-21: itens e taxa de serviço do atendimento; a taxa de entrega só se não restar ativo."""
    entries = []
    for c in ledger.components:
        if c.restaurant_order_id == restaurant_order_id or (
            last_active and c.component_type == "delivery_fee"
        ):
            line, units = _whole(ledger, c)
            entries.append((line, c.component_number, units))
    if not any(e[0] for e in entries):
        raise ValueError("for_restaurant_order: nada a devolver (atendimento já reembolsado?)")
    return _plan(entries)


def for_incident(
    ledger: Ledger, items: Mapping[ItemKey, int], include_delivery_fee: bool
) -> RefundPlan:
    """RN-14: item e taxa de serviço dos itens apontados, na proporção; entrega se o motivo for dela."""
    entries = []
    for c in ledger.components:
        key = c.item_key
        if key is not None and key in items and c.quantity:
            q = items[key]
            done = ledger.refunded[c.component_number]
            gross, tax = partial_refund(c.gross_amount, c.tax_amount, c.quantity, done.units, q)
            entries.append((_line(c, gross, tax, q), c.component_number, q))
        elif include_delivery_fee and c.component_type == "delivery_fee":
            line, _ = _whole(ledger, c)
            entries.append((line, c.component_number, 0))
    missing = set(items) - {c.item_key for c in ledger.components}
    if missing:
        raise ValueError(f"for_incident: itens fora do pagamento {sorted(missing)}")
    return _plan(entries)


def for_remaining(ledger: Ledger) -> RefundPlan:
    """RN-30 (motorista impossibilitado): tudo o que ainda não foi devolvido."""
    entries = []
    for c in ledger.components:
        line, units = _whole(ledger, c)
        entries.append((line, c.component_number, units))
    return _plan(entries)
