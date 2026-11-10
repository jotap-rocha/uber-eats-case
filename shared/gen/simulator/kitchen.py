"""Ciclo do atendimento no restaurante: análise, aceite, preparo, pronto, cancelamentos e reposição
(RN-10 a RN-13, RN-27, RN-28, RN-34, RN-37 a RN-40).

Os desfechos concorrentes da análise (cliente cancela, restaurante responde, prazo de 5 minutos) são
agendados todos; vale o que a agenda executar primeiro e os outros são recusados (RN-27).
"""

from __future__ import annotations

import math
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from functools import partial

from simulator.context import Context, sync
from simulator.fleet import on_ready, schedule_outcome
from simulator.refunds import for_restaurant_order
from simulator.rules import (
    END_REASON_FROM,
    END_REASONS,
    can_accept,
    can_auto_reject,
    is_active,
    is_late,
    late_after,
    restock_slots,
)
from simulator.store import (
    Cursor,
    Refused,
    RestaurantOrderRow,
    available_stock,
    consume_stock,
    fits,
    insert_refund,
    load_ledger,
    lock_restaurant_order,
    move_restaurant_order,
    payment_of_order,
    restock,
    statuses_of_order,
    stock_need,
)

RESTAURANT_DROPS = frozenset(
    {"restaurant_declined", "out_of_stock", "analysis_timeout", "restaurant_issue"}
)  # RN-34: o restaurante cancelou ou rejeitou
CANCELLABLE_BEFORE_READY = ("in_analysis", "accepted", "preparing")
MIN_PREP = timedelta(seconds=30)


# --- Análise (RN-28) -------------------------------------------------------------------------


def schedule_analysis(ctx: Context, ro_id: int, sent_at: datetime) -> None:
    """Agenda os desfechos possíveis da análise; o prazo de 5 minutos sempre existe (RN-28)."""
    b, t, d = ctx.params.behavior, ctx.params.timing, ctx.params.delays
    ctx.schedule(sent_at + t.analysis_timeout, "auto_reject", lambda: auto_reject(ctx, ro_id))
    u = ctx.rng.random()
    if u < b.customer_cancels_in_analysis:
        when = sent_at + t.analysis_timeout * ctx.rng.uniform(0.02, 0.98)
        ctx.schedule(when, "customer_cancel", lambda: customer_cancel(ctx, ro_id))
    elif u < b.customer_cancels_in_analysis + b.restaurant_ignores:
        return  # o restaurante não responde: o prazo rejeita sozinho
    else:
        accept = ctx.rng.random() >= b.restaurant_declines / max(
            1e-9, 1 - b.customer_cancels_in_analysis - b.restaurant_ignores
        )
        when = sent_at + ctx.minutes(d.restaurant_response_min)
        ctx.schedule(when, "respond", lambda: respond(ctx, ro_id, accept))


def _drop(ctx: Context, cur: Cursor, ro: RestaurantOrderRow, reason: str) -> None:
    """Cancela ou rejeita o atendimento, devolve o dinheiro e acerta pedido e entrega (RN-10, RN-21)."""
    status, actor = END_REASONS[reason]
    move_restaurant_order(cur, ro, status, actor, ctx.now, reason)
    others = [(i, s) for i, s in statuses_of_order(cur, ro.order_id) if is_active(s)]
    payment_id = payment_of_order(cur, ro.order_id)
    plan = for_restaurant_order(
        load_ledger(cur, payment_id), ro.restaurant_order_id, last_active=not others
    )
    insert_refund(cur, payment_id, "restaurant_order", ro.restaurant_order_id, plan, ctx.now)
    result = sync(ctx, cur, ro.order_id, actor)
    if result.after == "out_for_delivery" and result.before != result.after:
        # o outro atendimento já estava retirado: o motorista segue com o que tem (RN-28)
        cur.execute("SELECT delivery_id FROM deliveries WHERE order_id = %s", (ro.order_id,))
        schedule_outcome(ctx, cur, int(cur.fetchone()[0]))
    if reason in RESTAURANT_DROPS:
        for other_id, other_status in others:
            if other_status in CANCELLABLE_BEFORE_READY and (
                ctx.rng.random() < ctx.params.behavior.customer_cancels_other_after_drop
            ):
                when = ctx.now + ctx.minutes(ctx.params.delays.late_cancel_delay_min)
                ctx.schedule(
                    when,
                    "cancel_other",
                    partial(cancel, ctx, other_id, "other_restaurant_dropped"),
                )


def auto_reject(ctx: Context, ro_id: int) -> None:
    with ctx.pg.cursor() as cur:
        ro = lock_restaurant_order(cur, ro_id)
        if ro.status != "in_analysis" or not can_auto_reject(
            ro.sent_at, ctx.now, ctx.params.timing.analysis_timeout
        ):
            raise Refused(f"atendimento {ro_id}: a rejeição automática já não vale")
        _drop(ctx, cur, ro, "analysis_timeout")


def customer_cancel(ctx: Context, ro_id: int) -> None:
    cancel(ctx, ro_id, "customer_request")


def cancel(ctx: Context, ro_id: int, reason: str) -> None:
    """Cancelamento por motivo (RN-12, RN-13, RN-34): só dos status em que o motivo vale."""
    with ctx.pg.cursor() as cur:
        ro = lock_restaurant_order(cur, ro_id)
        if ro.status not in END_REASON_FROM[reason]:
            raise Refused(f"atendimento {ro_id}: {reason} não vale em {ro.status}")
        if reason == "restaurant_late" and (
            ro.accepted_at is None
            or ro.estimated_prep_min is None
            or not is_late(
                ro.accepted_at, ro.estimated_prep_min, ctx.params.timing.prep_tolerance, ctx.now
            )
        ):
            raise Refused(f"atendimento {ro_id}: ainda não está atrasado (RN-28)")
        _drop(ctx, cur, ro, reason)


def respond(ctx: Context, ro_id: int, accept: bool) -> None:
    with ctx.pg.cursor() as cur:
        ro = lock_restaurant_order(cur, ro_id)
        if ro.status != "in_analysis" or not can_accept(
            ro.sent_at, ctx.now, ctx.params.timing.analysis_timeout
        ):
            raise Refused(f"atendimento {ro_id}: a resposta já não vale (RN-27, RN-28)")
        if not accept:
            _drop(ctx, cur, ro, "restaurant_declined")
            return
        need = stock_need(cur, ro_id)
        if not fits(need, available_stock(cur, ro.restaurant_id)):
            _drop(ctx, cur, ro, "out_of_stock")  # RN-39
            return
        cur.execute(
            "SELECT max(p.prep_time_min) FROM order_items oi "
            "JOIN products p ON p.product_id = oi.product_id WHERE oi.restaurant_order_id = %s",
            (ro_id,),
        )
        estimated = int(cur.fetchone()[0])
        move_restaurant_order(
            cur,
            ro,
            "accepted",
            "restaurant",
            ctx.now,
            columns={"accepted_at": ctx.now, "estimated_prep_min": estimated},
        )
        sync(ctx, cur, ro.order_id, "restaurant")
        plan_preparation(ctx, ro_id, ctx.now, estimated)


# --- Preparo (RN-28, RN-38) ------------------------------------------------------------------


def plan_preparation(ctx: Context, ro_id: int, accepted_at: datetime, estimated: int) -> None:
    """Agenda início, fim do preparo, atraso e cancelamento por falta de insumo (RN-12, RN-13)."""
    b, d, t = ctx.params.behavior, ctx.params.delays, ctx.params.timing
    start = max(ctx.now, accepted_at + ctx.minutes(d.prep_start_delay_min))
    overrun = ctx.rng.lognormvariate(0.0, b.prep_overrun_lognormal_sigma)
    ready = max(start + MIN_PREP, accepted_at + timedelta(minutes=estimated) * overrun)
    ctx.schedule(start, "start_prep", lambda: start_prep(ctx, ro_id))
    ctx.schedule(ready, "ready", lambda: ready_for_pickup(ctx, ro_id))
    late = late_after(accepted_at, estimated, t.prep_tolerance)
    if ready > late and ctx.rng.random() < b.customer_cancels_late:
        when = max(late, ctx.now) + ctx.minutes(d.late_cancel_delay_min)
        ctx.schedule(when, "cancel_late", lambda: cancel(ctx, ro_id, "restaurant_late"))
    if ctx.rng.random() < b.restaurant_issue_after_accept:
        when = start + (ready - start) * ctx.rng.uniform(0.05, 0.95)
        ctx.schedule(when, "restaurant_issue", lambda: cancel(ctx, ro_id, "restaurant_issue"))


def start_prep(ctx: Context, ro_id: int) -> None:
    with ctx.pg.cursor() as cur:
        ro = lock_restaurant_order(cur, ro_id)
        if ro.status != "accepted":
            raise Refused(f"atendimento {ro_id}: o preparo já não começa (RN-27)")
        move_restaurant_order(cur, ro, "preparing", "restaurant", ctx.now)
        consume_stock(cur, ro_id, ctx.now)  # a baixa nasce no preparo (RN-38)
        sync(ctx, cur, ro.order_id, "restaurant")


def ready_for_pickup(ctx: Context, ro_id: int) -> None:
    with ctx.pg.cursor() as cur:
        ro = lock_restaurant_order(cur, ro_id)
        if ro.status != "preparing":
            raise Refused(f"atendimento {ro_id}: já não está em preparo (RN-27)")
        move_restaurant_order(cur, ro, "ready_for_pickup", "restaurant", ctx.now)
        sync(ctx, cur, ro.order_id, "restaurant")
        on_ready(ctx, cur, ro_id, ro.order_id, ro.driver_arrived_at is not None)


# --- Reposição (RN-40) -----------------------------------------------------------------------


def plan_restock_day(ctx: Context, restaurant_id: int, day: date) -> None:
    """Agenda a reposição do dia fora das janelas e o planejamento do dia seguinte."""
    restaurant = ctx.cache.get().restaurants.get(restaurant_id)
    if restaurant is None:
        return
    for slot in restock_slots(restaurant.windows):
        when = datetime.combine(day, slot)
        if when >= ctx.now:
            ctx.schedule(
                when, "restock", lambda: restock_restaurant(ctx, restaurant_id), always=True
            )
    next_day = day + timedelta(days=1)
    ctx.schedule(
        datetime.combine(next_day, time(0, 0)),
        "plan_restock",
        lambda: plan_restock_day(ctx, restaurant_id, next_day),
        always=True,
    )


def ensure_restock_planned(ctx: Context) -> None:
    for restaurant_id in ctx.cache.get().restaurants:
        if restaurant_id not in ctx.restock_planned:
            ctx.restock_planned.add(restaurant_id)
            plan_restock_day(ctx, restaurant_id, ctx.now.date())


def restock_restaurant(ctx: Context, restaurant_id: int) -> None:
    """Repõe até cobrir `restock_target_days` de consumo médio os itens abaixo do gatilho."""
    s = ctx.params.stock
    window_start = ctx.now - timedelta(days=s.consumption_window_days)
    observed_days = min(
        float(s.consumption_window_days),
        max(1.0, (ctx.now - ctx.start).total_seconds() / 86400),
    )
    with ctx.pg.cursor() as cur:
        cur.execute(
            "SELECT s.stock_item_id, s.quantity_on_hand, coalesce(c.consumed, 0) FROM stock_items s "
            "LEFT JOIN (SELECT stock_item_id, sum(quantity) AS consumed FROM stock_movements "
            "           WHERE movement_type = 'consumption' AND occurred_at > %s "
            "           GROUP BY stock_item_id) c ON c.stock_item_id = s.stock_item_id "
            "WHERE s.restaurant_id = %s",
            (window_start, restaurant_id),
        )
        for item_id, on_hand, consumed in cur.fetchall():
            if consumed <= 0:
                continue
            target = Decimal(math.ceil(float(consumed) / observed_days * s.restock_target_days))
            if on_hand < target * Decimal(str(s.restock_trigger)):
                restock(cur, item_id, target - on_hand, ctx.now)
