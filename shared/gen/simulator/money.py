"""Dinheiro da compra e dos reembolsos (RN-09, RN-19 a RN-21, RN-29, RN-33; F5.7).

Tudo em Decimal com ROUND_HALF_UP para centavos, o mesmo resultado do round(numeric, 2) do
Postgres e do round do Spark para valores positivos: os testes T8 a T10 recalculam sem divergir.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")
ZERO = Decimal("0.00")


def round_cents(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def share(base: Decimal, rate: Decimal) -> Decimal:
    """Parcela única: custo do meio de pagamento, comissão, parte do motorista (F5.7 #6)."""
    return round_cents(base * rate)


def allocate(total: Decimal, weights: Sequence[Decimal]) -> list[Decimal]:
    """Rateia `total` na proporção dos pesos; cada parcela arredondada e a última absorve a diferença (RN-33)."""
    if not weights:
        raise ValueError("allocate: sem pesos")
    weight_sum = sum(weights, ZERO)
    if weight_sum <= 0 or any(w < 0 for w in weights):
        raise ValueError("allocate: pesos precisam ser não negativos com soma positiva")
    parts = [round_cents(total * w / weight_sum) for w in weights[:-1]]
    parts.append(total - sum(parts, ZERO))
    return parts


def delivery_fee(distance_km: Decimal, base: Decimal, per_km: Decimal) -> Decimal:
    """Taxa de entrega = base + R$/km × distância estimada na compra; congelada (F5, decisão 4)."""
    if distance_km < 0:
        raise ValueError("delivery_fee: distância negativa")
    return round_cents(base + per_km * distance_km)


@dataclass(frozen=True)
class Line:
    """Item do pedido como entra no cálculo (order_items)."""

    restaurant_order_id: int
    line_number: int
    unit_price: Decimal
    quantity: int

    @property
    def total_amount(self) -> Decimal:
        return self.unit_price * self.quantity  # RN-32: preço da compra × quantidade


@dataclass(frozen=True)
class Component:
    """Linha de payment_components."""

    component_number: int
    component_type: str
    restaurant_order_id: int | None
    line_number: int | None
    gross_amount: Decimal
    tax_amount: Decimal


@dataclass(frozen=True)
class PurchasePricing:
    components: tuple[Component, ...]
    items_amount: Decimal
    service_fee_amount: Decimal
    delivery_fee_amount: Decimal
    total_amount: Decimal
    tax_amount: Decimal
    payment_fee_amount: Decimal


def price_purchase(
    lines: Sequence[Line],
    delivery_fee_amount: Decimal,
    tax_rate: Decimal,
    service_fee_rate: Decimal,
    payment_fee_rate: Decimal,
) -> PurchasePricing:
    """Componentes do pagamento, congelados na compra (F5.7 #2 a #6).

    Ordem: para cada item em (restaurant_order_id, line_number), `item` e `service_fee`;
    `delivery_fee` por último. O último componente absorve a diferença do imposto.
    """
    if not lines:
        raise ValueError("price_purchase: compra sem itens")
    if delivery_fee_amount <= 0:
        raise ValueError("price_purchase: toda compra tem taxa de entrega positiva (RN-20)")
    for line in lines:
        if (
            line.quantity < 1
            or line.unit_price <= 0
            or line.unit_price != round_cents(line.unit_price)
        ):
            raise ValueError(f"price_purchase: item inválido {line}")
    keys = [(ln.restaurant_order_id, ln.line_number) for ln in lines]
    if len(set(keys)) != len(keys):
        raise ValueError("price_purchase: item repetido")

    ordered = sorted(lines, key=lambda ln: (ln.restaurant_order_id, ln.line_number))
    item_amounts = [ln.total_amount for ln in ordered]
    items_amount = sum(item_amounts, ZERO)
    service_fee_amount = share(items_amount, service_fee_rate)
    service_parts = allocate(service_fee_amount, item_amounts)

    targets: list[tuple[str, int | None, int | None, Decimal]] = []
    for line, item_gross, service_gross in zip(ordered, item_amounts, service_parts, strict=True):
        targets.append(("item", line.restaurant_order_id, line.line_number, item_gross))
        targets.append(("service_fee", line.restaurant_order_id, line.line_number, service_gross))
    targets.append(("delivery_fee", None, None, delivery_fee_amount))

    total_amount = items_amount + service_fee_amount + delivery_fee_amount
    tax_amount = share(total_amount, tax_rate)
    taxes = [share(gross, tax_rate) for *_, gross in targets[:-1]]
    taxes.append(tax_amount - sum(taxes, ZERO))
    last_gross = targets[-1][3]
    if not ZERO <= taxes[-1] <= last_gross:
        raise ArithmeticError(
            "price_purchase: imposto absorvido fora de [0, bruto] no último componente"
        )

    components = tuple(
        Component(n, ctype, ro_id, line_no, gross, tax)
        for n, ((ctype, ro_id, line_no, gross), tax) in enumerate(
            zip(targets, taxes, strict=True), start=1
        )
    )
    return PurchasePricing(
        components=components,
        items_amount=items_amount,
        service_fee_amount=service_fee_amount,
        delivery_fee_amount=delivery_fee_amount,
        total_amount=total_amount,
        tax_amount=tax_amount,
        payment_fee_amount=share(total_amount, payment_fee_rate),
    )


def partial_refund(
    gross: Decimal, tax: Decimal, quantity_total: int, already_refunded: int, quantity: int
) -> tuple[Decimal, Decimal]:
    """Reembolso de `quantity` de `quantity_total` unidades, com `already_refunded` já devolvidas.

    Diferença de acumulados (F5.7 #8): round(G·(r+q)/Q) − round(G·r/Q). Fecha exatamente o
    componente quando todas as unidades voltam, em qualquer ordem (T9).
    """
    if quantity_total < 1 or quantity < 1 or already_refunded < 0:
        raise ValueError("partial_refund: quantidades inválidas")
    if already_refunded + quantity > quantity_total:
        raise ValueError("partial_refund: devolve mais do que foi comprado (RN-14)")

    def cumulative(amount: Decimal, units: int) -> Decimal:
        return round_cents(amount * units / quantity_total)

    after, before = already_refunded + quantity, already_refunded
    return (
        cumulative(gross, after) - cumulative(gross, before),
        cumulative(tax, after) - cumulative(tax, before),
    )
