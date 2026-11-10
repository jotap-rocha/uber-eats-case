"""Frota: turnos, atribuição, chegada e retirada, desfecho da entrega e repasses (RN-06, RN-07, RN-17,
RN-24, RN-29, RN-30, RN-31, RN-35, RN-36, RN-42; L1b e L2).

O motorista leva uma entrega por vez. Quem desiste continua no turno, mas nunca volta à entrega de
que desistiu (T5c). Motorista impossibilitado fecha o turno na mesma transação (RN-42).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import timedelta
from functools import partial

from simulator.aftersales import schedule_after_delivery
from simulator.context import Context, sync
from simulator.money import share
from simulator.refunds import for_remaining
from simulator.rules import can_give_up, is_active, travel_time
from simulator.store import (
    Cursor,
    Refused,
    insert_refund,
    load_ledger,
    lock_delivery,
    lock_restaurant_order,
    move_delivery,
    move_order,
    move_restaurant_order,
    payment_of_order,
    set_restaurant_order,
)

WAITING_DELIVERIES = """
SELECT d.delivery_id, d.order_id FROM deliveries d JOIN orders o ON o.order_id = d.order_id
WHERE d.status = 'awaiting_assignment' AND o.city_id = %s
  AND EXISTS (SELECT 1 FROM restaurant_orders ro
              WHERE ro.order_id = o.order_id AND ro.status = 'ready_for_pickup')
ORDER BY d.delivery_id
"""
FREE_SHIFTS = """
SELECT s.shift_id, s.driver_id FROM shifts s
WHERE s.status = 'open' AND s.city_id = %s AND s.opened_at <= %s
  AND NOT EXISTS (SELECT 1 FROM driver_assignments a
                  WHERE a.driver_id = s.driver_id AND a.released_at IS NULL)
  AND NOT EXISTS (SELECT 1 FROM driver_assignments a
                  WHERE a.delivery_id = %s AND a.driver_id = s.driver_id)
ORDER BY s.shift_id
"""
SHIFT_RETRY = timedelta(minutes=5)
CLOSE_FAILED_SHIFT = "driver_unable"


@dataclass(frozen=True)
class Assignment:
    number: int
    driver_id: int
    shift_id: int


def current_assignment(cur: Cursor, delivery_id: int) -> Assignment | None:
    cur.execute(
        "SELECT assignment_number, driver_id, shift_id FROM driver_assignments "
        "WHERE delivery_id = %s AND released_at IS NULL",
        (delivery_id,),
    )
    row = cur.fetchone()
    return None if row is None else Assignment(int(row[0]), int(row[1]), int(row[2]))


def release_assignment(cur: Cursor, delivery_id: int, reason: str, ctx: Context) -> None:
    cur.execute(
        "UPDATE driver_assignments SET released_at = %s, release_reason = %s "
        "WHERE delivery_id = %s AND released_at IS NULL",
        (ctx.now, reason, delivery_id),
    )


# --- Turnos (RN-36, RN-42) -------------------------------------------------------------------


def shift_tick(ctx: Context) -> None:
    """A cada hora, abre turnos até cobrir a demanda esperada da cidade (RN-35: motorista da cidade)."""
    now = ctx.now
    ctx.schedule(
        now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1),
        "shift_tick",
        lambda: shift_tick(ctx),
        always=True,
    )
    ref = ctx.cache.get()
    d = ctx.params.demand
    with ctx.pg.cursor() as cur:
        cur.execute("SELECT driver_id, city_id FROM shifts WHERE status = 'open'")
        open_rows = cur.fetchall()
    open_drivers = {int(r[0]) for r in open_rows}
    for city_id, drivers in sorted(ref.drivers_by_city.items()):
        target = math.ceil(d.drivers_per_hourly_order * d.orders_per_hour(now.hour))
        missing = target - sum(1 for r in open_rows if r[1] == city_id)
        pool = [
            x for x in drivers if x.driver_id not in open_drivers and x.registration_date <= now
        ]
        for driver in ctx.rng.sample(pool, min(len(pool), max(0, missing))):
            jitter = ctx.minutes(ctx.params.delays.shift_open_jitter_min)
            ctx.schedule(
                now + jitter,
                "open_shift",
                partial(open_shift, ctx, driver.driver_id, city_id),
                always=True,
            )


def open_shift(ctx: Context, driver_id: int, city_id: int) -> None:
    with ctx.pg.cursor() as cur:
        cur.execute("SELECT 1 FROM shifts WHERE driver_id = %s AND status = 'open'", (driver_id,))
        if cur.fetchone():
            raise Refused(f"motorista {driver_id} já tem turno aberto (RN-42)")
        cur.execute(
            "INSERT INTO shifts (driver_id, city_id, status, opened_at) "
            "VALUES (%s, %s, 'open', %s) RETURNING shift_id",
            (driver_id, city_id, ctx.now),
        )
        shift_id = int(cur.fetchone()[0])
    hours = ctx.rng.uniform(*ctx.params.behavior.shift_hours)
    ctx.schedule(
        ctx.now + timedelta(hours=hours), "close_shift", lambda: close_shift(ctx, shift_id)
    )
    dispatch(ctx, city_id)


def close_shift(ctx: Context, shift_id: int) -> None:
    with ctx.pg.cursor() as cur:
        cur.execute(
            "SELECT driver_id, status FROM shifts WHERE shift_id = %s FOR UPDATE", (shift_id,)
        )
        row = cur.fetchone()
        if row is None or row[1] != "open":
            raise Refused(f"turno {shift_id} já está fechado")
        cur.execute(
            "SELECT 1 FROM driver_assignments WHERE driver_id = %s AND released_at IS NULL",
            (row[0],),
        )
        if cur.fetchone():  # com entrega atribuída o turno não fecha (RN-42): tenta de novo
            ctx.schedule(ctx.now + SHIFT_RETRY, "close_shift", lambda: close_shift(ctx, shift_id))
            return
        cur.execute(
            "UPDATE shifts SET status = 'closed', closed_at = %s, close_reason = 'driver_closed' "
            "WHERE shift_id = %s",
            (ctx.now, shift_id),
        )


# --- Atribuição (RN-06, RN-07) ---------------------------------------------------------------


def dispatch(ctx: Context, city_id: int) -> None:
    """Atribui motorista às entregas que esperam, na ordem de chegada; chamada quando algo libera."""
    with ctx.pg.cursor() as cur:
        cur.execute(WAITING_DELIVERIES, (city_id,))
        for delivery_id, order_id in cur.fetchall():
            _assign(ctx, cur, int(delivery_id), int(order_id), city_id)


def _assign(ctx: Context, cur: Cursor, delivery_id: int, order_id: int, city_id: int) -> bool:
    cur.execute(FREE_SHIFTS, (city_id, ctx.now, delivery_id))
    candidates = cur.fetchall()
    if not candidates:
        return False
    shift_id, driver_id = ctx.rng.choice(candidates)
    cur.execute(
        "SELECT coalesce(max(assignment_number), 0) + 1 FROM driver_assignments WHERE delivery_id = %s",
        (delivery_id,),
    )
    number = int(cur.fetchone()[0])
    cur.execute(
        "INSERT INTO driver_assignments (delivery_id, assignment_number, driver_id, shift_id, "
        "assigned_at) VALUES (%s, %s, %s, %s, %s)",
        (delivery_id, number, driver_id, shift_id, ctx.now),
    )
    move_delivery(cur, delivery_id, "awaiting_assignment", "assigned", ctx.now)
    cur.execute(
        "SELECT min(restaurant_order_id) FROM restaurant_orders "
        "WHERE order_id = %s AND status = 'ready_for_pickup'",
        (order_id,),
    )
    first_ready = int(cur.fetchone()[0])  # empate vale o de menor identificador (RN-06)
    delays = ctx.params.delays
    to_restaurant = ctx.minutes(delays.driver_to_restaurant_min)
    ctx.schedule(ctx.now + to_restaurant, "arrive", lambda: arrive(ctx, first_ready, number))
    if ctx.rng.random() < ctx.params.behavior.driver_gives_up and can_give_up(
        number, False, ctx.params.timing.max_driver_give_ups
    ):
        when = ctx.now + to_restaurant * ctx.rng.uniform(0.1, 0.9)
        ctx.schedule(when, "give_up", lambda: give_up(ctx, delivery_id, number))
    return True


def give_up(ctx: Context, delivery_id: int, number: int) -> None:
    """RN-07: só antes da primeira retirada; a entrega volta a aguardar e o motorista não volta a ela."""
    with ctx.pg.cursor() as cur:
        delivery = lock_delivery(cur, delivery_id=delivery_id)
        assignment = current_assignment(cur, delivery_id)
        if delivery.status != "assigned" or assignment is None or assignment.number != number:
            raise Refused(f"entrega {delivery_id}: a atribuição {number} já não vale")
        cur.execute(
            "SELECT count(*) FROM restaurant_orders WHERE order_id = %s AND status = 'picked_up'",
            (delivery.order_id,),
        )
        if not can_give_up(number, cur.fetchone()[0] > 0, ctx.params.timing.max_driver_give_ups):
            raise Refused(f"entrega {delivery_id}: desistência fora da regra (RN-07)")
        release_assignment(cur, delivery_id, "driver_gave_up", ctx)
        cur.execute(
            "UPDATE restaurant_orders SET driver_arrived_at = NULL "
            "WHERE order_id = %s AND picked_up_at IS NULL",
            (delivery.order_id,),
        )
        move_delivery(cur, delivery_id, "assigned", "awaiting_assignment", ctx.now)
        cur.execute("SELECT city_id FROM orders WHERE order_id = %s", (delivery.order_id,))
        city_id = int(cur.fetchone()[0])
    dispatch(ctx, city_id)


# --- Chegada e retirada (RN-17) --------------------------------------------------------------


def _schedule_pickup(ctx: Context, ro_id: int, number: int) -> None:
    delay = ctx.minutes(ctx.params.delays.pickup_handover_min)
    ctx.schedule(ctx.now + delay, "pickup", lambda: pickup(ctx, ro_id, number))


def arrive(ctx: Context, ro_id: int, number: int) -> None:
    with ctx.pg.cursor() as cur:
        ro = lock_restaurant_order(cur, ro_id)
        delivery = lock_delivery(cur, order_id=ro.order_id)
        assignment = current_assignment(cur, delivery.delivery_id)
        if (
            delivery.status != "assigned"
            or assignment is None
            or assignment.number != number
            or not is_active(ro.status)
            or ro.status == "picked_up"
        ):
            raise Refused(f"atendimento {ro_id}: a chegada do motorista já não vale")
        set_restaurant_order(cur, ro_id, driver_arrived_at=ctx.now)
        if ro.status == "ready_for_pickup":
            _schedule_pickup(ctx, ro_id, number)


def on_ready(ctx: Context, cur: Cursor, ro_id: int, order_id: int, arrived: bool) -> None:
    """Atendimento ficou pronto: busca motorista se a entrega espera, ou retira se ele já está lá."""
    delivery = lock_delivery(cur, order_id=order_id)
    if delivery.status == "awaiting_assignment":
        cur.execute("SELECT city_id FROM orders WHERE order_id = %s", (order_id,))
        dispatch(ctx, int(cur.fetchone()[0]))
    elif delivery.status == "assigned" and arrived:
        assignment = current_assignment(cur, delivery.delivery_id)
        if assignment is not None:
            _schedule_pickup(ctx, ro_id, assignment.number)


def pickup(ctx: Context, ro_id: int, number: int) -> None:
    with ctx.pg.cursor() as cur:
        ro = lock_restaurant_order(cur, ro_id)
        delivery = lock_delivery(cur, order_id=ro.order_id)
        assignment = current_assignment(cur, delivery.delivery_id)
        if (
            ro.status != "ready_for_pickup"
            or ro.driver_arrived_at is None
            or delivery.status != "assigned"
            or assignment is None
            or assignment.number != number
        ):
            raise Refused(f"atendimento {ro_id}: a retirada já não vale")
        move_restaurant_order(
            cur, ro, "picked_up", "driver", ctx.now, columns={"picked_up_at": ctx.now}
        )
        _restaurant_payout(ctx, cur, ro_id, ro.restaurant_id)
        result = sync(ctx, cur, ro.order_id, "driver")
        if result.after == "out_for_delivery":
            schedule_outcome(ctx, cur, delivery.delivery_id)
            return
        cur.execute(
            "SELECT min(restaurant_order_id) FROM restaurant_orders WHERE order_id = %s "
            "AND status NOT IN ('picked_up', 'cancelled', 'rejected')",
            (ro.order_id,),
        )
        next_ro = cur.fetchone()[0]
    if next_ro is not None:  # a espera do motorista no próximo restaurante é evento medido (RN-17)
        travel = ctx.minutes(ctx.params.delays.driver_to_restaurant_min)
        ctx.schedule(ctx.now + travel, "arrive", lambda: arrive(ctx, int(next_ro), number))


def _restaurant_payout(ctx: Context, cur: Cursor, ro_id: int, restaurant_id: int) -> None:
    """Devido na retirada, só de atendimento retirado (RN-29); comissão congelada na linha."""
    cur.execute(
        "SELECT sum(total_amount) FROM order_items WHERE restaurant_order_id = %s", (ro_id,)
    )
    items = cur.fetchone()[0]
    rate = ctx.money.commission_rate
    commission = share(items, rate)
    cur.execute(
        "INSERT INTO restaurant_payouts (restaurant_order_id, restaurant_id, items_amount, "
        "commission_rate, commission_amount, payout_amount, due_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (ro_id, restaurant_id, items, rate, commission, items - commission, ctx.now),
    )


# --- Desfecho da entrega (RN-24, RN-25, RN-29, RN-30) ----------------------------------------


def schedule_outcome(ctx: Context, cur: Cursor, delivery_id: int) -> None:
    b, t = ctx.params.behavior, ctx.params.timing
    cur.execute("SELECT distance_km FROM deliveries WHERE delivery_id = %s", (delivery_id,))
    distance = float(cur.fetchone()[0])
    noise = ctx.rng.lognormvariate(0.0, ctx.params.delays.travel_lognormal_sigma)
    travel = max(travel_time(distance, t.average_speed_kmh) * noise, timedelta(minutes=1))
    u = ctx.rng.random()
    if u < b.driver_unable:
        kind, when = "driver_unable", ctx.now + travel * ctx.rng.uniform(0.2, 0.8)
    elif u < b.driver_unable + b.customer_absent:
        wait = ctx.minutes(ctx.params.delays.customer_absent_wait_min)
        kind, when = "customer_absent", ctx.now + travel + wait
    else:
        kind, when = "delivered", ctx.now + travel
    ctx.schedule(when, kind, lambda: finish_delivery(ctx, delivery_id, kind))


def finish_delivery(ctx: Context, delivery_id: int, kind: str) -> None:
    now = ctx.now
    with ctx.pg.cursor() as cur:
        delivery = lock_delivery(cur, delivery_id=delivery_id)
        assignment = current_assignment(cur, delivery_id)
        if delivery.status != "in_transit" or assignment is None:
            raise Refused(f"entrega {delivery_id} já não está a caminho (RN-27)")
        order_id = delivery.order_id
        if kind == "delivered":
            move_delivery(cur, delivery_id, "in_transit", "delivered", now, finished=True)
            move_order(cur, order_id, "out_for_delivery", "delivered", "driver", now)
        elif kind == "customer_absent":
            move_delivery(
                cur,
                delivery_id,
                "in_transit",
                "undelivered",
                now,
                finished=True,
                failure_reason="customer_absent",
            )
            move_order(
                cur, order_id, "out_for_delivery", "undelivered", "driver", now, "customer_absent"
            )
        else:
            move_delivery(
                cur,
                delivery_id,
                "in_transit",
                "undelivered",
                now,
                finished=True,
                failure_reason="driver_unable",
            )
            move_order(
                cur, order_id, "out_for_delivery", "undelivered", "platform", now, "driver_unable"
            )
        release_assignment(cur, delivery_id, "delivery_finished", ctx)
        payment_id = payment_of_order(cur, order_id)
        if kind == "driver_unable":
            cur.execute(
                "UPDATE shifts SET status = 'closed', closed_at = %s, close_reason = %s "
                "WHERE shift_id = %s AND status = 'open'",
                (now, CLOSE_FAILED_SHIFT, assignment.shift_id),
            )
            plan = for_remaining(
                load_ledger(cur, payment_id)
            )  # estorno total, da plataforma (RN-30)
            insert_refund(cur, payment_id, "driver_unable", delivery_id, plan, now)
        else:
            _driver_payout(ctx, cur, delivery_id, payment_id, assignment)
        cur.execute(
            "SELECT o.city_id, array_agg(ro.restaurant_order_id ORDER BY ro.restaurant_order_id) "
            "FROM orders o JOIN restaurant_orders ro ON ro.order_id = o.order_id "
            "WHERE o.order_id = %s AND ro.status = 'picked_up' GROUP BY o.city_id",
            (order_id,),
        )
        city_id, ro_ids = cur.fetchone()
    if kind == "delivered":
        schedule_after_delivery(ctx, order_id, delivery_id, now, ro_ids)
    dispatch(ctx, int(city_id))


def _driver_payout(
    ctx: Context, cur: Cursor, delivery_id: int, payment_id: int, assignment: Assignment
) -> None:
    """Parcela fixa da taxa de entrega; devida na entrega e no cliente ausente (RN-29)."""
    cur.execute(
        "SELECT gross_amount FROM payment_components WHERE payment_id = %s "
        "AND component_type = 'delivery_fee'",
        (payment_id,),
    )
    fee = cur.fetchone()[0]
    rate = ctx.money.driver_share_rate
    cur.execute(
        "INSERT INTO driver_payouts (delivery_id, driver_id, shift_id, delivery_fee_amount, "
        "driver_share_rate, payout_amount, due_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (
            delivery_id,
            assignment.driver_id,
            assignment.shift_id,
            fee,
            rate,
            share(fee, rate),
            ctx.now,
        ),
    )
