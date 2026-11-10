"""Contexto compartilhado pelas ações do simulador (F5.5): um processo, um escritor.

Cada ação agendada roda numa transação. O que ela agenda só entra na agenda depois do commit
(`pending`): se a ação for recusada (RN-27) e a transação voltar, os passos seguintes não existem.
"""

from __future__ import annotations

import random
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Any

from simulator.agenda import Agenda, Task
from simulator.clock import SimClock
from simulator.geo import Point
from simulator.params import MoneyParams
from simulator.reference import ReferenceCache
from simulator.sim_params import SimParams
from simulator.store import Cursor, OrderSync, RouteParams, sync_order


@dataclass
class Context:
    pg: Any  # psycopg.Connection em autocommit; cada ação abre a própria transação
    params: SimParams
    money: MoneyParams
    cache: ReferenceCache
    rng: random.Random
    clock: SimClock
    salt_order: str = field(repr=False)
    salt_payment: str = field(repr=False)
    start: datetime
    agenda: Agenda = field(default_factory=Agenda)
    stats: Counter[str] = field(default_factory=Counter)
    pending: list[Task] = field(default_factory=list)
    restock_planned: set[int] = field(default_factory=set)

    @property
    def now(self) -> datetime:
        return self.clock.now

    @property
    def route(self) -> RouteParams:
        t = self.params.timing
        return RouteParams(t.route_detour_factor, t.average_speed_kmh, t.promise_slack)

    def schedule(
        self, when: datetime, name: str, fn: Callable[[], None], *, always: bool = False
    ) -> None:
        """`always` empurra direto (relógios que não dependem do commit da ação)."""
        task = Task(max(when, self.now), name, fn)
        if always:
            self.agenda.push(task)
        else:
            self.pending.append(task)

    def commit_pending(self) -> None:
        for task in self.pending:
            self.agenda.push(task)
        self.pending.clear()

    def discard_pending(self) -> None:
        self.pending.clear()

    def minutes(self, bounds: tuple[float, float]) -> timedelta:
        return timedelta(minutes=self.rng.uniform(*bounds))

    def seconds(self, bounds: tuple[float, float]) -> timedelta:
        return timedelta(seconds=self.rng.uniform(*bounds))


def sync(ctx: Context, cur: Cursor, order_id: int, actor: str) -> OrderSync:
    """Status do pedido, da entrega e prazo prometido depois de uma mudança de atendimento."""
    cur.execute(
        "SELECT r.restaurant_id, r.latitude, r.longitude FROM restaurants r "
        "JOIN restaurant_orders ro ON ro.restaurant_id = r.restaurant_id WHERE ro.order_id = %s",
        (order_id,),
    )
    points = {int(i): Point(lat, lon) for i, lat, lon in cur.fetchall()}
    return sync_order(cur, order_id, actor, ctx.now, points, ctx.route)
