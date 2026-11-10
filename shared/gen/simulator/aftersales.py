"""Depois da entrega: confirmação, avaliações, gorjeta e incidentes (RN-14, RN-22, RN-24, RN-26; L3).

Cada ação valida o próprio limite no comando (RN-28, fronteiras): fora da janela, é recusada.
Nada aqui muda o status do atendimento nem da entrega (RN-14); só o pedido vai de entregue a concluído.
"""

from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime, timedelta
from decimal import Decimal
from functools import partial

from simulator.context import Context
from simulator.refunds import for_incident
from simulator.rules import (
    can_auto_confirm,
    can_customer_confirm,
    tip_offered,
    within_window,
)
from simulator.sim_params import DELIVERY_REASONS, INCIDENT_REASONS
from simulator.store import (
    Cursor,
    Refused,
    insert_refund,
    load_ledger,
    lock_delivery,
    move_order,
    payment_of_order,
)

ITEM_REASONS = frozenset(INCIDENT_REASONS) - DELIVERY_REASONS
TIP_CHOICES = (2, 3, 5, 5, 5, 8, 10, 10, 15, 20, 30)  # reais; cortado em [tip_min, tip_max]
INCIDENT_MEAN_DELAY_H = 2.0  # abertura do incidente: exponencial, truncada em 24 h (RN-14)


def schedule_after_delivery(
    ctx: Context, order_id: int, delivery_id: int, finished_at: datetime, ro_ids: Sequence[int]
) -> None:
    """Sorteia o que o cliente faz depois da entrega e agenda cada coisa no seu instante."""
    b, t = ctx.params.behavior, ctx.params.timing
    window = t.rating_tip_window
    rng = ctx.rng
    if rng.random() < b.customer_confirms:
        when = finished_at + t.auto_confirm_delay * rng.uniform(0.05, 0.95)
        ctx.schedule(when, "confirm", lambda: confirm(ctx, order_id, "customer"))
    else:
        ctx.schedule(
            finished_at + t.auto_confirm_delay,
            "auto_confirm",
            lambda: confirm(ctx, order_id, "platform"),
        )
    rated_at = None
    if rng.random() < b.driver_rating:
        rated_at = finished_at + window * rng.uniform(0.05, 0.75)
        rating = _rating(ctx)
        comment = _comment(ctx, "driver", rating)
        ctx.schedule(
            rated_at, "rate_driver", lambda: rate_driver(ctx, delivery_id, rating, comment)
        )
    for ro_id in ro_ids:
        if rng.random() < b.restaurant_rating:
            when = finished_at + window * rng.uniform(0.05, 0.95)
            rating = _rating(ctx)
            comment = _comment(ctx, "restaurant", rating)
            ctx.schedule(
                when,
                "rate_restaurant",
                partial(rate_restaurant, ctx, ro_id, rating, comment),
            )
    if rng.random() < b.tip:
        low = rated_at or finished_at  # a gorjeta é oferecida depois da avaliação (RN-26)
        tip_at = low + (finished_at + window - low) * rng.uniform(0.05, 1.0)
        ctx.schedule(tip_at, "tip", lambda: tip(ctx, delivery_id))
    for _ in range(b.max_incidents_per_order):
        if rng.random() < b.incident:
            delay = timedelta(hours=min(rng.expovariate(1 / INCIDENT_MEAN_DELAY_H), 23.9))
            ctx.schedule(finished_at + delay, "open_incident", lambda: open_incident(ctx, order_id))


def _rating(ctx: Context) -> int:
    weights = ctx.params.behavior.rating_weights
    return ctx.rng.choices(list(weights), weights=list(weights.values()))[0]


def _comment(ctx: Context, actor: str, rating: int) -> str | None:
    if ctx.rng.random() >= ctx.params.behavior.rating_comment:
        return None
    band = "low" if rating <= 2 else "mid" if rating == 3 else "high"
    return ctx.rng.choice(ctx.params.texts.rating_comments[actor][band])


# --- Confirmação (RN-24) ---------------------------------------------------------------------


def confirm(ctx: Context, order_id: int, actor: str) -> None:
    """Manual (cliente) e automática (plataforma): duas causas da mesma transição."""
    with ctx.pg.cursor() as cur:
        delivery = lock_delivery(cur, order_id=order_id)
        if delivery.status != "delivered" or delivery.finished_at is None:
            raise Refused(f"pedido {order_id} não está entregue")
        delay = ctx.params.timing.auto_confirm_delay
        allowed = (
            can_customer_confirm(delivery.finished_at, ctx.now, delay)
            if actor == "customer"
            else can_auto_confirm(delivery.finished_at, ctx.now, delay)
        )
        if not allowed:
            raise Refused(f"confirmação de {actor} fora do prazo (RN-24)")
        move_order(cur, order_id, "delivered", "completed", actor, ctx.now)


# --- Avaliações e gorjeta (RN-22, RN-26) -----------------------------------------------------


def _delivered_in_window(ctx: Context, cur: Cursor, delivery_id: int) -> datetime:
    delivery = lock_delivery(cur, delivery_id=delivery_id)
    window = ctx.params.timing.rating_tip_window
    if (
        delivery.status != "delivered"
        or delivery.finished_at is None
        or not within_window(delivery.finished_at, ctx.now, window)
    ):
        raise Refused(f"entrega {delivery_id} fora da janela de avaliação e gorjeta (RN-26)")
    return delivery.finished_at


def _driver_and_customer(cur: Cursor, delivery_id: int) -> tuple[int, int]:
    cur.execute(
        "SELECT a.driver_id, o.customer_id FROM driver_assignments a "
        "JOIN deliveries d ON d.delivery_id = a.delivery_id "
        "JOIN orders o ON o.order_id = d.order_id "
        "WHERE a.delivery_id = %s AND a.release_reason = 'delivery_finished'",
        (delivery_id,),
    )
    row = cur.fetchone()
    if row is None:
        raise Refused(f"entrega {delivery_id} sem atribuição finalizada")
    return int(row[0]), int(row[1])


def rate_driver(ctx: Context, delivery_id: int, rating: int, comment: str | None) -> None:
    with ctx.pg.cursor() as cur:
        _delivered_in_window(ctx, cur, delivery_id)
        driver_id, customer_id = _driver_and_customer(cur, delivery_id)
        cur.execute(
            "INSERT INTO driver_ratings (delivery_id, driver_id, customer_id, rating, comment, "
            "rated_at) VALUES (%s, %s, %s, %s, %s, %s)",
            (delivery_id, driver_id, customer_id, rating, comment, ctx.now),
        )


def rate_restaurant(
    ctx: Context, restaurant_order_id: int, rating: int, comment: str | None
) -> None:
    with ctx.pg.cursor() as cur:
        cur.execute(
            "SELECT ro.restaurant_id, ro.status, d.delivery_id, o.customer_id "
            "FROM restaurant_orders ro JOIN orders o ON o.order_id = ro.order_id "
            "JOIN deliveries d ON d.order_id = o.order_id WHERE ro.restaurant_order_id = %s",
            (restaurant_order_id,),
        )
        row = cur.fetchone()
        if row is None or row[1] != "picked_up":
            raise Refused("avaliação do restaurante só de atendimento retirado (RN-26)")
        _delivered_in_window(ctx, cur, int(row[2]))
        cur.execute(
            "INSERT INTO restaurant_ratings (restaurant_order_id, restaurant_id, customer_id, "
            "rating, comment, rated_at) VALUES (%s, %s, %s, %s, %s, %s)",
            (restaurant_order_id, row[0], row[3], rating, comment, ctx.now),
        )


def tip(ctx: Context, delivery_id: int) -> None:
    money = ctx.money
    with ctx.pg.cursor() as cur:
        _delivered_in_window(ctx, cur, delivery_id)
        cur.execute("SELECT rating FROM driver_ratings WHERE delivery_id = %s", (delivery_id,))
        row = cur.fetchone()
        if not tip_offered(None if row is None else int(row[0])):
            raise Refused("nota do motorista 3 ou menor: gorjeta não oferecida (RN-26)")
        driver_id, _ = _driver_and_customer(cur, delivery_id)
        amount = min(max(Decimal(ctx.rng.choice(TIP_CHOICES)), money.tip_min), money.tip_max)
        cur.execute(
            "INSERT INTO tips (delivery_id, driver_id, amount, paid_at) VALUES (%s, %s, %s, %s)",
            (delivery_id, driver_id, amount, ctx.now),
        )


# --- Incidentes (RN-14) ----------------------------------------------------------------------

REMAINING_LINES = """
SELECT oi.restaurant_order_id, oi.line_number,
       oi.quantity - coalesce((SELECT sum(ii.quantity) FROM incident_items ii
                               JOIN incidents i ON i.incident_id = ii.incident_id
                               WHERE ii.restaurant_order_id = oi.restaurant_order_id
                                 AND ii.line_number = oi.line_number AND i.status <> 'dismissed'), 0)
FROM order_items oi JOIN restaurant_orders ro ON ro.restaurant_order_id = oi.restaurant_order_id
WHERE ro.order_id = %s AND ro.status = 'picked_up'
ORDER BY 1, 2
"""


def open_incident(ctx: Context, order_id: int) -> None:
    with ctx.pg.cursor() as cur:
        delivery = lock_delivery(cur, order_id=order_id)
        if (
            delivery.status != "delivered"
            or delivery.finished_at is None
            or not within_window(delivery.finished_at, ctx.now, ctx.params.timing.incident_window)
        ):
            raise Refused(f"pedido {order_id}: incidente fora da janela de 24 h (RN-14)")
        cur.execute(REMAINING_LINES, (order_id,))
        lines = [(int(r), int(n), int(q)) for r, n, q in cur.fetchall() if q > 0]
        cur.execute(
            "SELECT 1 FROM incidents WHERE order_id = %s AND reason = ANY(%s)",
            (order_id, sorted(DELIVERY_REASONS)),
        )
        has_delivery_incident = cur.fetchone() is not None
        reason = _pick_reason(ctx, bool(lines), has_delivery_incident)
        if reason is None:
            raise Refused(f"pedido {order_id}: nenhum incidente possível agora")
        items = _pick_items(ctx, reason, lines)
        cur.execute("SELECT customer_id FROM orders WHERE order_id = %s", (order_id,))
        customer_id = cur.fetchone()[0]
        cur.execute(
            "INSERT INTO incidents (order_id, customer_id, reason, description, opened_at) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING incident_id",
            (
                order_id,
                customer_id,
                reason,
                ctx.rng.choice(ctx.params.texts.incident_descriptions[reason]),
                ctx.now,
            ),
        )
        incident_id = int(cur.fetchone()[0])
        for ro_id, line_number, quantity in items:
            cur.execute(
                "INSERT INTO incident_items (incident_id, restaurant_order_id, line_number, quantity) "
                "VALUES (%s, %s, %s, %s)",
                (incident_id, ro_id, line_number, quantity),
            )
    d = ctx.params.delays
    ctx.schedule(
        ctx.now + ctx.minutes(d.incident_review_delay_min),
        "review_incident",
        lambda: review_incident(ctx, incident_id),
    )


def _pick_reason(ctx: Context, has_items: bool, has_delivery_incident: bool) -> str | None:
    shares = ctx.params.behavior.incident_reason_share
    for _ in range(8):
        reason = ctx.rng.choices(list(shares), weights=list(shares.values()))[0]
        if reason in DELIVERY_REASONS and has_delivery_incident:
            continue  # um incidente de entrega por pedido (L3, decisão 6)
        if reason != "late_delivery" and not has_items:
            continue  # sem item com saldo (teto da RN-14)
        return reason
    return None


def _pick_items(
    ctx: Context, reason: str, lines: list[tuple[int, int, int]]
) -> list[tuple[int, int, int]]:
    if reason == "late_delivery":
        return []
    if reason == "not_received":
        return list(lines)  # todos os itens com saldo, gravados pelo simulador (L3)
    chosen = ctx.rng.sample(lines, ctx.rng.randint(1, min(2, len(lines))))
    return [(r, n, ctx.rng.randint(1, q)) for r, n, q in sorted(chosen)]


def review_incident(ctx: Context, incident_id: int) -> None:
    with ctx.pg.cursor() as cur:
        cur.execute(
            "UPDATE incidents SET status = 'in_review', review_started_at = %s "
            "WHERE incident_id = %s AND status = 'open'",
            (ctx.now, incident_id),
        )
        if cur.rowcount != 1:
            raise Refused(f"incidente {incident_id} já não está aberto (RN-27)")
    d = ctx.params.delays
    ctx.schedule(
        ctx.now + ctx.minutes(d.incident_decision_delay_min),
        "decide_incident",
        lambda: decide_incident(ctx, incident_id),
    )


def decide_incident(ctx: Context, incident_id: int) -> None:
    """Procedente gera exatamente um reembolso, na mesma transação (L3); improcedente nenhum."""
    with ctx.pg.cursor() as cur:
        cur.execute(
            "SELECT i.order_id, i.reason, d.finished_at, d.promised_at FROM incidents i "
            "JOIN deliveries d ON d.order_id = i.order_id "
            "WHERE i.incident_id = %s AND i.status = 'in_review' FOR UPDATE OF i",
            (incident_id,),
        )
        row = cur.fetchone()
        if row is None:
            raise Refused(f"incidente {incident_id} já não está em análise (RN-27)")
        order_id, reason, finished_at, promised_at = row
        upheld = ctx.rng.random() < ctx.params.behavior.incident_upheld
        if reason == "late_delivery" and (promised_at is None or finished_at <= promised_at):
            upheld = False  # atraso só procede se houve atraso de fato (T15)
        cur.execute(
            "UPDATE incidents SET status = %s, decided_at = %s WHERE incident_id = %s",
            ("upheld" if upheld else "dismissed", ctx.now, incident_id),
        )
        if not upheld:
            return
        cur.execute(
            "SELECT restaurant_order_id, line_number, quantity FROM incident_items "
            "WHERE incident_id = %s",
            (incident_id,),
        )
        items = {(int(r), int(n)): int(q) for r, n, q in cur.fetchall()}
        payment_id = payment_of_order(cur, order_id)
        plan = for_incident(
            load_ledger(cur, payment_id), items, include_delivery_fee=reason in DELIVERY_REASONS
        )
        insert_refund(cur, payment_id, "incident", incident_id, plan, ctx.now)
