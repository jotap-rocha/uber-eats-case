"""Laço do simulador: uma fila de ações por instante, um escritor, uma transação por ação (F5.5).

Histórico simulado primeiro, tempo real depois, pelo mesmo laço: o relógio injetado salta no
histórico e espera no tempo real (F5.6). Parar e religar retoma pelo estado do banco (F5.10):
o relógio volta ao último evento gravado e as entidades vivas ganham novos passos.
"""

from __future__ import annotations

import logging
import random
from datetime import datetime, time, timedelta
from functools import partial
from typing import Any

from simulator.aftersales import confirm, decide_incident, review_incident
from simulator.agenda import Task
from simulator.clock import SimClock
from simulator.context import Context
from simulator.fleet import close_shift, dispatch, schedule_outcome, shift_tick
from simulator.kitchen import (
    ensure_restock_planned,
    plan_preparation,
    ready_for_pickup,
    schedule_analysis,
)
from simulator.params import Parameters
from simulator.purchase import purchase_tick
from simulator.reference import ReferenceCache, ReferenceLoader
from simulator.sim_params import sim_params
from simulator.store import Refused

log = logging.getLogger(__name__)
PROGRESS_EVERY = 5000

LAST_EVENT = """
SELECT max(t) FROM (
  SELECT max(placed_at) t FROM orders
  UNION ALL SELECT max(occurred_at) FROM order_status_transitions
  UNION ALL SELECT max(occurred_at) FROM restaurant_order_status_transitions
  UNION ALL SELECT max(occurred_at) FROM stock_movements
  UNION ALL SELECT max(opened_at) FROM shifts
  UNION ALL SELECT max(closed_at) FROM shifts
  UNION ALL SELECT max(assigned_at) FROM driver_assignments
  UNION ALL SELECT max(released_at) FROM driver_assignments
  UNION ALL SELECT max(finished_at) FROM deliveries
  UNION ALL SELECT max(attempted_at) FROM payment_attempts
  UNION ALL SELECT max(refunded_at) FROM refunds
  UNION ALL SELECT max(paid_at) FROM tips
  UNION ALL SELECT max(rated_at) FROM driver_ratings
  UNION ALL SELECT max(rated_at) FROM restaurant_ratings
  UNION ALL SELECT max(opened_at) FROM incidents
  UNION ALL SELECT max(review_started_at) FROM incidents
  UNION ALL SELECT max(decided_at) FROM incidents
) s
"""


def resume_point(pg: Any) -> datetime | None:  # Any: conexão psycopg
    """Último instante de negócio gravado: o relógio retoma dali (F5.10)."""
    row = pg.execute(LAST_EVENT).fetchone()
    return None if row is None else row[0]


def default_start(params: Parameters, today: datetime, days: int | None = None) -> datetime:
    """Meia-noite de `days` dias atrás; sem `days`, usa `clock.backfill_days`."""
    if days is None:
        days = int(params.section("clock")["backfill_days"])
    return datetime.combine((today - timedelta(days=days)).date(), time(0, 0))


def initial_start(
    params: Parameters,
    today: datetime,
    *,
    days: int | None,
    resumed: datetime | None,
    has_orders: bool,
) -> datetime:
    """Retoma do último evento só se já há pedidos; antes disso o restock do seed não é histórico."""
    if has_orders and resumed is not None:
        return resumed
    return default_start(params, today, days)


def restock_coverage_error(start: datetime, first_restock: datetime | None) -> str | None:
    """Mensagem de erro se o histórico começa antes do restock inicial (saldo negativo, T6)."""
    if first_restock is None or first_restock.date() <= start.date():
        return None
    return (
        f"o restock inicial ({first_restock:%Y-%m-%d}) é posterior ao início do histórico "
        f"({start:%Y-%m-%d}); refazer o seed com --start-day {start:%Y-%m-%d} apaga a operação "
        "gerada e pede confirmação (task 14 da regeração)"
    )


def partial_run_error(resumed: datetime | None, first_restock: datetime | None) -> str | None:
    """Sem pedidos mas com eventos além do restock inicial: uma execução parou antes do 1º pedido."""
    if resumed is None or first_restock is None or resumed <= first_restock:
        return None
    return (
        f"há eventos de operação até {resumed:%Y-%m-%d %H:%M} mas nenhum pedido; "
        "limpe a operação (task 14) antes de começar o histórico de novo"
    )


def build_context(
    pg: Any,  # Any: conexão psycopg
    loader: ReferenceLoader,
    params: Parameters,
    *,
    start: datetime,
    seed: int | None,
    salts: tuple[str, str],
    clock: SimClock | None = None,
) -> Context:
    sp = sim_params(params)
    return Context(
        pg=pg,
        params=sp,
        money=params.money,
        cache=ReferenceCache(loader, sp.timing.profile_cache_refresh),
        rng=random.Random(seed),
        clock=clock or SimClock(start),
        salt_order=salts[0],
        salt_payment=salts[1],
        start=start,
    )


def run_task(ctx: Context, task: Task) -> None:
    ctx.stats[f"acao:{task.name}"] += 1
    try:
        with ctx.pg.transaction():
            task.run()
    except Refused as exc:  # RN-27: perdeu a corrida; a transação voltou inteira
        ctx.discard_pending()
        ctx.stats[f"recusada:{task.name}"] += 1
        log.debug("%s recusada em %s: %s", task.name, ctx.now, exc)
    except BaseException:
        ctx.discard_pending()
        log.error("falha em %s às %s", task.name, ctx.now)
        raise
    else:
        ctx.commit_pending()


def run(ctx: Context, *, until: datetime | None = None, max_events: int | None = None) -> int:
    """Executa ações na ordem do tempo até `until`, o limite de eventos ou a parada pedida."""
    done = 0
    while ctx.agenda:
        when = ctx.agenda.peek_time()
        assert when is not None
        if (until is not None and when > until) or (max_events is not None and done >= max_events):
            break
        if not ctx.clock.advance_to(when):
            break
        run_task(ctx, ctx.agenda.pop())
        done += 1
        if done % PROGRESS_EVERY == 0:
            log.info("%d ações, relógio em %s, %d na agenda", done, ctx.now, len(ctx.agenda))
    return done


def bootstrap(ctx: Context) -> None:
    """Relógios que não terminam: compras por cidade, turnos, manutenção do que vem do cadastro."""
    ref = ctx.cache.get()
    for city_id in sorted(ref.restaurants_by_city):
        ctx.schedule(ctx.now, "purchase", partial(purchase_tick, ctx, city_id), always=True)
    ctx.schedule(ctx.now, "shift_tick", partial(shift_tick, ctx), always=True)
    ctx.schedule(ctx.now, "maintenance", partial(maintenance, ctx), always=True)


def maintenance(ctx: Context) -> None:
    ctx.schedule(
        ctx.now + timedelta(hours=1), "maintenance", partial(maintenance, ctx), always=True
    )
    ensure_restock_planned(ctx)


def recover(ctx: Context) -> None:
    """Dá novos passos ao que ficou vivo no banco (parada anterior): sorteios novos, mesmas regras."""
    with ctx.pg.cursor() as cur:
        cur.execute(
            "SELECT ro.restaurant_order_id, ro.status, ro.accepted_at, ro.estimated_prep_min, "
            "ro.order_id, t.occurred_at FROM restaurant_orders ro "
            "JOIN restaurant_order_status_transitions t "
            "  ON t.restaurant_order_id = ro.restaurant_order_id AND t.sequence_number = 1 "
            "WHERE ro.status IN ('in_analysis', 'accepted', 'preparing') ORDER BY 1"
        )
        for ro_id, status, accepted_at, estimated, _order_id, sent_at in cur.fetchall():
            if status == "in_analysis":
                schedule_analysis(ctx, ro_id, sent_at)
            elif status == "accepted":
                plan_preparation(ctx, ro_id, accepted_at, estimated)
            else:
                span = (0.5, max(1.0, float(estimated)))
                ctx.schedule(
                    ctx.now + ctx.minutes(span), "ready", partial(ready_for_pickup, ctx, ro_id)
                )
        cur.execute("SELECT delivery_id FROM deliveries WHERE status = 'in_transit'")
        for (delivery_id,) in cur.fetchall():
            schedule_outcome(ctx, cur, delivery_id)
        cur.execute(
            "SELECT o.order_id, d.finished_at FROM orders o JOIN deliveries d ON d.order_id = o.order_id "
            "WHERE o.status = 'delivered'"
        )
        for order_id, finished_at in cur.fetchall():
            when = finished_at + ctx.params.timing.auto_confirm_delay
            ctx.schedule(when, "auto_confirm", partial(confirm, ctx, order_id, "platform"))
        cur.execute(
            "SELECT incident_id, status FROM incidents WHERE status IN ('open', 'in_review')"
        )
        for incident_id, status in cur.fetchall():
            step = review_incident if status == "open" else decide_incident
            ctx.schedule(
                ctx.now + ctx.minutes((5.0, 60.0)), "incident", partial(step, ctx, incident_id)
            )
        cur.execute("SELECT shift_id FROM shifts WHERE status = 'open'")
        for (shift_id,) in cur.fetchall():
            hours = ctx.rng.uniform(0.0, ctx.params.behavior.shift_hours[1])
            ctx.schedule(
                ctx.now + timedelta(hours=hours), "close_shift", partial(close_shift, ctx, shift_id)
            )
        cur.execute("SELECT DISTINCT city_id FROM orders")
        cities = [int(r[0]) for r in cur.fetchall()]
    ctx.commit_pending()
    for city_id in cities:
        with ctx.pg.transaction():
            dispatch(ctx, city_id)
        ctx.commit_pending()
