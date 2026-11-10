"""Escritas comuns no Postgres, sempre dentro da transação de uma ação (F5.5; ADR 008 e 009).

Toda mudança de status faz `UPDATE ... WHERE status = <de>` e grava a transição com
sequence_number = último + 1, na mesma transação: a trava da RN-27. Quem perde a corrida recebe
Refused, a transação volta inteira e nada fica pela metade.

Os nomes de coluna montados em SQL vêm de listas fixas deste módulo, nunca de entrada externa.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Any

from simulator.geo import Point, Stop, shortest_route
from simulator.refunds import Ledger, PaidComponent, Refunded, RefundPlan
from simulator.rules import (
    ORDER_BEFORE_DELIVERY,
    AcceptedRO,
    allowed_ro_transition,
    derive_order_status,
    is_active,
    promise_due,
    promised_at,
)

Cursor = Any  # psycopg.Cursor: o pacote não depende do tipo concreto do driver


class Refused(Exception):
    """O comando não vale mais no estado atual (RN-27, prazos da RN-28): nada é gravado."""


# Colunas que cada UPDATE pode mexer (allowlist; F1.2).
RO_COLUMNS = frozenset({"accepted_at", "estimated_prep_min", "driver_arrived_at", "picked_up_at"})


def next_id(cur: Cursor, table: str, column: str) -> int:
    """Reserva o próximo valor da identidade, para o código de rastreio sair antes do INSERT (F0.3)."""
    if (table, column) not in {
        ("orders", "order_id"),
        ("payments", "payment_id"),
        ("restaurant_orders", "restaurant_order_id"),
    }:
        raise ValueError(f"next_id: {table}.{column} fora da lista")
    cur.execute("SELECT nextval(pg_get_serial_sequence(%s, %s))", (f"ubereats.{table}", column))
    return int(cur.fetchone()[0])


# --- Atendimento -----------------------------------------------------------------------------


@dataclass(frozen=True)
class RestaurantOrderRow:
    restaurant_order_id: int
    order_id: int
    restaurant_id: int
    status: str
    sent_at: datetime  # linha 1 das transições: começa o prazo de análise (RN-28)
    accepted_at: datetime | None
    estimated_prep_min: int | None
    driver_arrived_at: datetime | None
    picked_up_at: datetime | None


def lock_restaurant_order(cur: Cursor, restaurant_order_id: int) -> RestaurantOrderRow:
    cur.execute(
        "SELECT ro.restaurant_order_id, ro.order_id, ro.restaurant_id, ro.status, t.occurred_at, "
        "ro.accepted_at, ro.estimated_prep_min, ro.driver_arrived_at, ro.picked_up_at "
        "FROM restaurant_orders ro "
        "JOIN restaurant_order_status_transitions t "
        "  ON t.restaurant_order_id = ro.restaurant_order_id AND t.sequence_number = 1 "
        "WHERE ro.restaurant_order_id = %s FOR UPDATE OF ro",
        (restaurant_order_id,),
    )
    row = cur.fetchone()
    if row is None:
        raise Refused(f"atendimento {restaurant_order_id} não existe")
    return RestaurantOrderRow(*row)


def move_restaurant_order(
    cur: Cursor,
    ro: RestaurantOrderRow,
    to_status: str,
    actor: str,
    at: datetime,
    reason: str | None = None,
    columns: Mapping[str, Any] | None = None,  # Any: valores das colunas da allowlist
) -> None:
    if not allowed_ro_transition(ro.status, to_status):
        raise Refused(
            f"atendimento {ro.restaurant_order_id}: {ro.status} → {to_status} não permitido"
        )
    columns = dict(columns or {})
    if set(columns) - RO_COLUMNS:
        raise ValueError(f"colunas fora da allowlist: {sorted(set(columns) - RO_COLUMNS)}")
    sets = ", ".join(f"{c} = %s" for c in columns)
    cur.execute(
        "UPDATE restaurant_orders SET status = %s, end_reason = %s"
        + (f", {sets}" if sets else "")
        + " WHERE restaurant_order_id = %s AND status = %s",
        (to_status, reason, *columns.values(), ro.restaurant_order_id, ro.status),
    )
    if cur.rowcount != 1:
        raise Refused(f"atendimento {ro.restaurant_order_id} já não está em {ro.status} (RN-27)")
    cur.execute(
        "INSERT INTO restaurant_order_status_transitions "
        "(restaurant_order_id, sequence_number, from_status, to_status, actor, reason, occurred_at) "
        "SELECT %s, coalesce(max(sequence_number), 0) + 1, %s, %s, %s, %s, %s "
        "FROM restaurant_order_status_transitions WHERE restaurant_order_id = %s",
        (ro.restaurant_order_id, ro.status, to_status, actor, reason, at, ro.restaurant_order_id),
    )


def set_restaurant_order(cur: Cursor, restaurant_order_id: int, **columns: Any) -> None:
    """Muda coluna sem mudar status (chegada do motorista, RN-17). Any: valores da allowlist."""
    if not columns or set(columns) - RO_COLUMNS:
        raise ValueError("set_restaurant_order: colunas fora da allowlist")
    sets = ", ".join(f"{c} = %s" for c in columns)
    cur.execute(
        f"UPDATE restaurant_orders SET {sets} WHERE restaurant_order_id = %s",
        (*columns.values(), restaurant_order_id),
    )


# --- Pedido e entrega ------------------------------------------------------------------------


def move_order(
    cur: Cursor,
    order_id: int,
    from_status: str,
    to_status: str,
    actor: str,
    at: datetime,
    reason: str | None = None,
) -> None:
    cur.execute(
        "UPDATE orders SET status = %s WHERE order_id = %s AND status = %s",
        (to_status, order_id, from_status),
    )
    if cur.rowcount != 1:
        raise Refused(f"pedido {order_id} já não está em {from_status} (RN-27)")
    cur.execute(
        "INSERT INTO order_status_transitions "
        "(order_id, sequence_number, from_status, to_status, actor, reason, occurred_at) "
        "SELECT %s, coalesce(max(sequence_number), 0) + 1, %s, %s, %s, %s, %s "
        "FROM order_status_transitions WHERE order_id = %s",
        (order_id, from_status, to_status, actor, reason, at, order_id),
    )


@dataclass(frozen=True)
class DeliveryRow:
    delivery_id: int
    order_id: int
    status: str
    dropoff: Point
    distance_km: Decimal | None
    promised_at: datetime | None
    finished_at: datetime | None


def lock_delivery(
    cur: Cursor, *, delivery_id: int | None = None, order_id: int | None = None
) -> DeliveryRow:
    key, value = ("delivery_id", delivery_id) if delivery_id is not None else ("order_id", order_id)
    cur.execute(
        "SELECT delivery_id, order_id, status, dropoff_latitude, dropoff_longitude, distance_km, "
        f"promised_at, finished_at FROM deliveries WHERE {key} = %s FOR UPDATE",
        (value,),
    )
    row = cur.fetchone()
    if row is None:
        raise Refused(f"entrega de {key}={value} não existe")
    d_id, o_id, status, lat, lon, dist, promised, finished = row
    return DeliveryRow(d_id, o_id, status, Point(lat, lon), dist, promised, finished)


def move_delivery(
    cur: Cursor,
    delivery_id: int,
    from_status: str,
    to_status: str,
    at: datetime,
    *,
    finished: bool = False,
    failure_reason: str | None = None,
) -> None:
    cur.execute(
        "UPDATE deliveries SET status = %s, failure_reason = %s"
        + (", finished_at = %s" if finished else "")
        + " WHERE delivery_id = %s AND status = %s",
        (to_status, failure_reason, *((at,) if finished else ()), delivery_id, from_status),
    )
    if cur.rowcount != 1:
        raise Refused(f"entrega {delivery_id} já não está em {from_status} (RN-27)")


@dataclass(frozen=True)
class OrderSync:
    order_id: int
    before: str
    after: str
    froze_promise: bool


@dataclass(frozen=True)
class RouteParams:
    detour_factor: Decimal
    speed_kmh: float
    slack: timedelta


def sync_order(
    cur: Cursor,
    order_id: int,
    actor: str,
    at: datetime,
    restaurant_points: Mapping[int, Point],
    route: RouteParams,
) -> OrderSync:
    """Status do pedido pela RN-16, estado da entrega (T2b) e congelamento do prazo (T7).

    Chamada depois de toda mudança de atendimento, na mesma transação. O ator da transição do pedido
    é o do evento do atendimento que a provocou (L1b).
    """
    cur.execute("SELECT status FROM orders WHERE order_id = %s FOR UPDATE", (order_id,))
    before = cur.fetchone()[0]
    cur.execute(
        "SELECT restaurant_id, status, accepted_at, estimated_prep_min FROM restaurant_orders "
        "WHERE order_id = %s ORDER BY restaurant_order_id",
        (order_id,),
    )
    ros = cur.fetchall()
    after = before
    if before in ORDER_BEFORE_DELIVERY:
        after = derive_order_status([s for _, s, _, _ in ros])
        if after != before:
            move_order(cur, order_id, before, after, actor, at)
    delivery = lock_delivery(cur, order_id=order_id)
    if after != before and after == "out_for_delivery":
        move_delivery(cur, delivery.delivery_id, "assigned", "in_transit", at)
    elif after != before and after == "cancelled":
        cur.execute(
            "UPDATE driver_assignments SET released_at = %s, release_reason = 'delivery_cancelled' "
            "WHERE delivery_id = %s AND released_at IS NULL",
            (at, delivery.delivery_id),
        )
        move_delivery(cur, delivery.delivery_id, delivery.status, "cancelled", at)
    froze = False
    if delivery.promised_at is None and promise_due([s for _, s, _, _ in ros]):
        active = [(r, a, e) for r, s, a, e in ros if is_active(s)]
        stops = [Stop(r, restaurant_points[r]) for r, _, _ in active]
        distance = shortest_route(stops, delivery.dropoff, route.detour_factor).distance_km
        promise = promised_at(
            [AcceptedRO(a, e) for _, a, e in active], float(distance), route.speed_kmh, route.slack
        )
        cur.execute(
            "UPDATE deliveries SET distance_km = %s, promised_at = %s "
            "WHERE delivery_id = %s AND promised_at IS NULL",
            (distance, promise, delivery.delivery_id),
        )
        froze = True
    return OrderSync(order_id, before, after, froze)


# --- Estoque (RN-37 a RN-39) -----------------------------------------------------------------


def available_stock(cur: Cursor, restaurant_id: int) -> dict[int, Decimal]:
    """Saldo menos o comprometido por atendimentos aceitos e ainda não em preparo (RN-39)."""
    cur.execute(
        "SELECT s.stock_item_id, s.quantity_on_hand - coalesce(c.q, 0) "
        "FROM stock_items s LEFT JOIN ("
        "  SELECT pr.stock_item_id, sum(pr.quantity * oi.quantity) AS q "
        "  FROM restaurant_orders ro "
        "  JOIN order_items oi ON oi.restaurant_order_id = ro.restaurant_order_id "
        "  JOIN product_recipes pr ON pr.product_id = oi.product_id "
        "  WHERE ro.status = 'accepted' AND ro.restaurant_id = %s GROUP BY pr.stock_item_id"
        ") c ON c.stock_item_id = s.stock_item_id WHERE s.restaurant_id = %s",
        (restaurant_id, restaurant_id),
    )
    return {int(i): Decimal(q) for i, q in cur.fetchall()}


def stock_need(cur: Cursor, restaurant_order_id: int) -> dict[int, Decimal]:
    """Ficha técnica × quantidade, por item de estoque (RN-38; T4d)."""
    cur.execute(
        "SELECT pr.stock_item_id, sum(pr.quantity * oi.quantity) FROM order_items oi "
        "JOIN product_recipes pr ON pr.product_id = oi.product_id "
        "WHERE oi.restaurant_order_id = %s GROUP BY pr.stock_item_id",
        (restaurant_order_id,),
    )
    return {int(i): Decimal(q) for i, q in cur.fetchall()}


def fits(need: Mapping[int, Decimal], available: Mapping[int, Decimal]) -> bool:
    return all(available.get(item, Decimal(0)) >= q for item, q in need.items())


def consume_stock(cur: Cursor, restaurant_order_id: int, at: datetime) -> None:
    """Baixa ao entrar em preparo, um movimento por item (RN-38); o CHECK de saldo ≥ 0 é a rede."""
    for item, quantity in sorted(stock_need(cur, restaurant_order_id).items()):
        cur.execute(
            "INSERT INTO stock_movements (stock_item_id, movement_type, quantity, restaurant_order_id, "
            "occurred_at) VALUES (%s, 'consumption', %s, %s, %s)",
            (item, quantity, restaurant_order_id, at),
        )
        cur.execute(
            "UPDATE stock_items SET quantity_on_hand = quantity_on_hand - %s WHERE stock_item_id = %s",
            (quantity, item),
        )


def restock(cur: Cursor, stock_item_id: int, quantity: Decimal, at: datetime) -> None:
    cur.execute(
        "INSERT INTO stock_movements (stock_item_id, movement_type, quantity, occurred_at) "
        "VALUES (%s, 'restock', %s, %s)",
        (stock_item_id, quantity, at),
    )
    cur.execute(
        "UPDATE stock_items SET quantity_on_hand = quantity_on_hand + %s WHERE stock_item_id = %s",
        (quantity, stock_item_id),
    )


# --- Dinheiro (L2) ---------------------------------------------------------------------------


def load_ledger(cur: Cursor, payment_id: int) -> Ledger:
    """Componentes congelados e o acumulado devolvido de cada um (unidades do item valem para a taxa
    de serviço da mesma linha)."""
    cur.execute(
        "SELECT pc.component_number, pc.component_type, pc.restaurant_order_id, pc.line_number, "
        "pc.gross_amount, pc.tax_amount, oi.quantity FROM payment_components pc "
        "LEFT JOIN order_items oi ON oi.restaurant_order_id = pc.restaurant_order_id "
        "  AND oi.line_number = pc.line_number "
        "WHERE pc.payment_id = %s ORDER BY pc.component_number",
        (payment_id,),
    )
    components = tuple(PaidComponent(*row) for row in cur.fetchall())
    cur.execute(
        "SELECT rc.component_number, sum(rc.gross_amount), sum(rc.tax_amount), "
        "coalesce(sum(rc.quantity), 0) FROM refund_components rc "
        "JOIN refunds r ON r.refund_id = rc.refund_id WHERE r.payment_id = %s "
        "GROUP BY rc.component_number",
        (payment_id,),
    )
    done = {int(n): (g, t, int(q)) for n, g, t, q in cur.fetchall()}
    units_by_item = {
        c.item_key: done[c.component_number][2]
        for c in components
        if c.component_type == "item" and c.component_number in done
    }
    refunded = {}
    for c in components:
        g, t, _ = done.get(c.component_number, (Decimal(0), Decimal(0), 0))
        refunded[c.component_number] = Refunded(g, t, units_by_item.get(c.item_key, 0))
    return Ledger(components, refunded)


ORIGIN_COLUMN = {
    "restaurant_order": "restaurant_order_id",
    "incident": "incident_id",
    "driver_unable": "delivery_id",
}


def insert_refund(
    cur: Cursor, payment_id: int, origin_type: str, origin_id: int, plan: RefundPlan, at: datetime
) -> int:
    if not plan.lines:
        raise Refused(f"reembolso {origin_type} {origin_id} sem valor a devolver")
    column = ORIGIN_COLUMN[origin_type]
    cur.execute(
        f"INSERT INTO refunds (payment_id, origin_type, {column}, total_amount, refunded_at) "
        "VALUES (%s, %s, %s, %s, %s) RETURNING refund_id",
        (payment_id, origin_type, origin_id, plan.total_amount, at),
    )
    refund_id = int(cur.fetchone()[0])
    for line in plan.lines:
        cur.execute(
            "INSERT INTO refund_components (refund_id, component_number, quantity, gross_amount, "
            "tax_amount) VALUES (%s, %s, %s, %s, %s)",
            (refund_id, line.component_number, line.quantity, line.gross_amount, line.tax_amount),
        )
    return refund_id


def payment_of_order(cur: Cursor, order_id: int) -> int:
    cur.execute("SELECT payment_id FROM payments WHERE order_id = %s", (order_id,))
    row = cur.fetchone()
    if row is None:
        raise Refused(f"pedido {order_id} sem pagamento (RN-11)")
    return int(row[0])


def statuses_of_order(cur: Cursor, order_id: int) -> Sequence[tuple[int, str]]:
    cur.execute(
        "SELECT restaurant_order_id, status FROM restaurant_orders WHERE order_id = %s "
        "ORDER BY restaurant_order_id",
        (order_id,),
    )
    return [(int(i), s) for i, s in cur.fetchall()]
