"""Demanda e compra: o simulador cria a compra inteira numa transação (ADR 009; F0.1).

Checkout, tentativas, pedido, atendimentos, itens, entrega, linha 1 das duas transições, pagamento,
componentes e recibo nascem juntos. Tentativa recusada sem aprovação deixa só checkout e tentativas:
não há pedido (RN-11, RN-15). O dinheiro vem de money.py, em Decimal.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal

from simulator.context import Context
from simulator.geo import Stop, shortest_route
from simulator.kitchen import schedule_analysis
from simulator.money import Line, delivery_fee, price_purchase
from simulator.reference import CustomerRef, ProductRef, Reference, RestaurantRef
from simulator.store import Cursor, available_stock, fits, next_id
from simulator.tracking import tracking_code

CARD_BRANDS = ("Visa", "Mastercard", "Elo")
WALLET_PROVIDERS = ("Apple Pay", "Google Pay")
GATEWAYS = ("Stripe", "Adyen", "Pagar.me")
DECLINES_CARD = (
    "insufficient_funds",
    "card_declined",
    "expired_card",
    "suspected_fraud",
    "processing_error",
)
DECLINES_OTHER = ("insufficient_funds", "suspected_fraud", "processing_error")
CUSTOMER_TRIES = 20


@dataclass(frozen=True)
class PlannedLine:
    product: ProductRef
    quantity: int


@dataclass(frozen=True)
class PlannedRO:
    restaurant: RestaurantRef
    lines: tuple[PlannedLine, ...]


@dataclass(frozen=True)
class Attempt:
    method: str
    card_brand: str | None
    wallet_provider: str | None
    gateway: str
    declined: str | None  # motivo da recusa, ou None se aprovada
    at: datetime


def purchase_tick(ctx: Context, city_id: int) -> None:
    """Processo de chegada de compras de uma cidade: exponencial com a taxa da hora (F5.8)."""
    rate = ctx.params.demand.orders_per_hour(ctx.now.hour) / 3600
    gap = ctx.rng.expovariate(rate) if rate > 0 else 3600.0
    ctx.schedule(
        ctx.now + timedelta(seconds=gap),
        "purchase",
        lambda: purchase_tick(ctx, city_id),
        always=True,
    )
    purchase(ctx, city_id)


def _pick_customer(ctx: Context, ref: Reference, city_id: int, at: datetime) -> CustomerRef | None:
    pool = ref.customers_by_city.get(city_id)
    if not pool:
        return None
    for _ in range(CUSTOMER_TRIES):
        customer = ctx.rng.choice(pool)
        if customer.signup_date <= at:  # cliente já cadastrado na data (F5.6)
            return customer
    return None


def _choose_lines(
    ctx: Context, restaurant: RestaurantRef, available: dict[int, Decimal]
) -> tuple[PlannedLine, ...]:
    """Produto sem estoque não entra em um novo checkout (RN-37); a quantidade cai até caber."""
    demand = ctx.params.demand
    wanted = ctx.rng.randint(*demand.items_per_restaurant_order)
    menu = list(restaurant.products)
    ctx.rng.shuffle(menu)
    lines: list[PlannedLine] = []
    for product in menu:
        if len(lines) >= wanted:
            break
        quantity = ctx.rng.randint(*demand.quantity_per_item)
        while quantity >= 1:
            need = {item: q * quantity for item, q in product.recipe}
            if fits(need, available):
                for item, amount in need.items():
                    available[item] -= amount
                lines.append(PlannedLine(product, quantity))
                break
            quantity -= 1
    return tuple(lines)


def _draw_attempts(ctx: Context, at: datetime) -> list[Attempt]:
    b = ctx.params.behavior
    methods = list(b.payment_method_share)
    weights = list(b.payment_method_share.values())
    drawn: list[tuple[str, str | None]] = []
    for _ in range(b.max_payment_attempts):
        method = ctx.rng.choices(methods, weights=weights)[0]
        declined = None
        if ctx.rng.random() < b.attempt_declined:
            declined = ctx.rng.choice(DECLINES_CARD if method == "card" else DECLINES_OTHER)
        drawn.append((method, declined))
        if declined is None:
            break
    times = [at]
    for _ in drawn[:-1]:
        times.insert(0, times[0] - ctx.seconds(ctx.params.delays.payment_retry_s))
    return [
        Attempt(
            method,
            ctx.rng.choice(CARD_BRANDS) if method == "card" else None,
            ctx.rng.choice(WALLET_PROVIDERS) if method == "wallet" else None,
            ctx.rng.choice(GATEWAYS),
            declined,
            when,
        )
        for (method, declined), when in zip(drawn, times, strict=True)
    ]


def purchase(ctx: Context, city_id: int) -> None:
    ref = ctx.cache.get()
    at = ctx.now
    open_now = [r for r in ref.restaurants_by_city.get(city_id, []) if r.open_at(at)]
    if not open_now:
        ctx.stats["skip:sem_restaurante_aberto"] += 1
        return
    customer = _pick_customer(ctx, ref, city_id, at)
    if customer is None:
        ctx.stats["skip:sem_cliente"] += 1
        return
    chosen = [ctx.rng.choice(open_now)]
    others = [r for r in open_now if r is not chosen[0]]
    if others and ctx.rng.random() < ctx.params.demand.second_restaurant_share:
        chosen.append(ctx.rng.choice(others))
    with ctx.pg.cursor() as cur:
        planned = []
        for restaurant in sorted(chosen, key=lambda r: r.restaurant_id):
            lines = _choose_lines(ctx, restaurant, available_stock(cur, restaurant.restaurant_id))
            if lines:
                planned.append(PlannedRO(restaurant, lines))
        if not planned:
            ctx.stats["skip:sem_estoque"] += 1
            return
        _write(ctx, cur, customer, planned)


def _write(ctx: Context, cur: Cursor, customer: CustomerRef, planned: list[PlannedRO]) -> None:
    at, money = ctx.now, ctx.money
    stops = [Stop(p.restaurant.restaurant_id, p.restaurant.point) for p in planned]
    route = shortest_route(stops, customer.point, ctx.params.timing.route_detour_factor)
    fee = delivery_fee(route.distance_km, money.delivery_fee_base, money.delivery_fee_per_km)
    attempts = _draw_attempts(ctx, at)
    last = attempts[-1]
    approved = last.declined is None

    # Compra recusada em todas as tentativas não tem pedido: ids de atendimento só valem se aprovar.
    ro_ids = (
        [next_id(cur, "restaurant_orders", "restaurant_order_id") for _ in planned]
        if approved
        else list(range(1, len(planned) + 1))
    )
    lines = [
        Line(ro_id, number, ln.product.price, ln.quantity)
        for ro_id, p in zip(ro_ids, planned, strict=True)
        for number, ln in enumerate(p.lines, start=1)
    ]
    pricing = price_purchase(
        lines, fee, money.tax_rate, money.service_fee_rate, money.payment_fee_rate[last.method]
    )
    cur.execute(
        "INSERT INTO checkouts (customer_id, amount) VALUES (%s, %s) RETURNING checkout_id",
        (customer.customer_id, pricing.total_amount),
    )
    checkout_id = int(cur.fetchone()[0])
    for number, a in enumerate(attempts, start=1):
        cur.execute(
            "INSERT INTO payment_attempts (checkout_id, attempt_number, amount, payment_method, "
            "card_brand, wallet_provider, gateway, result, decline_reason, attempted_at) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                checkout_id,
                number,
                pricing.total_amount,
                a.method,
                a.card_brand,
                a.wallet_provider,
                a.gateway,
                "declined" if a.declined else "approved",
                a.declined,
                a.at,
            ),
        )
    if not approved:
        ctx.stats["checkout_abandonado"] += 1
        return

    order_id = next_id(cur, "orders", "order_id")
    cur.execute(
        "INSERT INTO orders (order_id, tracking_code, checkout_id, customer_id, city_id, placed_at) "
        "VALUES (%s, %s, %s, %s, %s, %s)",
        (
            order_id,
            tracking_code(order_id, ctx.salt_order),
            checkout_id,
            customer.customer_id,
            planned[0].restaurant.city_id,
            at,
        ),
    )
    cur.execute(
        "INSERT INTO order_status_transitions (order_id, sequence_number, from_status, to_status, "
        "actor, occurred_at) VALUES (%s, 1, NULL, 'in_analysis', 'customer', %s)",
        (order_id, at),
    )
    for ro_id, p in zip(ro_ids, planned, strict=True):
        cur.execute(
            "INSERT INTO restaurant_orders (restaurant_order_id, order_id, restaurant_id) "
            "VALUES (%s, %s, %s)",
            (ro_id, order_id, p.restaurant.restaurant_id),
        )
        cur.execute(
            "INSERT INTO restaurant_order_status_transitions (restaurant_order_id, sequence_number, "
            "from_status, to_status, actor, occurred_at) VALUES (%s, 1, NULL, 'in_analysis', 'customer', %s)",
            (ro_id, at),
        )
        for number, ln in enumerate(p.lines, start=1):
            cur.execute(
                "INSERT INTO order_items (restaurant_order_id, line_number, product_id, product_name, "
                "unit_price, quantity, total_amount) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    ro_id,
                    number,
                    ln.product.product_id,
                    ln.product.name,
                    ln.product.price,
                    ln.quantity,
                    ln.product.price * ln.quantity,
                ),
            )
    cur.execute(
        "INSERT INTO deliveries (order_id, dropoff_address, dropoff_latitude, dropoff_longitude) "
        "VALUES (%s, %s, %s, %s)",
        (order_id, customer.address, customer.point.latitude, customer.point.longitude),
    )
    payment_id = next_id(cur, "payments", "payment_id")
    cur.execute(
        "INSERT INTO payments (payment_id, tracking_code, order_id, checkout_id, attempt_number, "
        "total_amount, tax_rate, service_fee_rate, payment_fee_rate, payment_fee_amount, paid_at) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (
            payment_id,
            tracking_code(payment_id, ctx.salt_payment),
            order_id,
            checkout_id,
            len(attempts),
            pricing.total_amount,
            money.tax_rate,
            money.service_fee_rate,
            money.payment_fee_rate[last.method],
            pricing.payment_fee_amount,
            at,
        ),
    )
    for c in pricing.components:
        cur.execute(
            "INSERT INTO payment_components (payment_id, component_number, component_type, "
            "restaurant_order_id, line_number, gross_amount, tax_amount) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
                payment_id,
                c.component_number,
                c.component_type,
                c.restaurant_order_id,
                c.line_number,
                c.gross_amount,
                c.tax_amount,
            ),
        )
    cur.execute("INSERT INTO receipts (payment_id, issued_at) VALUES (%s, %s)", (payment_id, at))
    ctx.stats["compra"] += 1
    for ro_id in ro_ids:
        schedule_analysis(ctx, ro_id, at)
