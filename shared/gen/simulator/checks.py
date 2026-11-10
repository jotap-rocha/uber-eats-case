"""Testes de verificação da regeração (F5.9 do modelo físico; catálogo 2 da L4).

Cada invariante devolve as violações: passa com zero. As consultas do Postgres ficam em
shared/gen/checks/*.sql; o que cruza bancos (T6 janelas, T17, T18, T19) são funções puras sobre
dados já lidos, testáveis offline. A amostra de violação leva só chaves e status, nunca dado de
pessoa (CLAUDE.md, dados e fontes).
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass, field
from datetime import datetime, time
from itertools import pairwise
from pathlib import Path
from typing import Any, Protocol

CHECKS_DIR = Path(__file__).resolve().parents[1] / "checks"
SAMPLE_SIZE = 5


@dataclass(frozen=True)
class Violations:
    check: str
    count: int
    sample: tuple[tuple[Any, ...], ...] = field(default=())  # Any: linhas de consulta heterogêneas

    @property
    def ok(self) -> bool:
        return self.count == 0


class Cursor(Protocol):
    def execute(self, query: str) -> Any: ...  # Any: o retorno varia entre drivers DB-API
    def fetchall(self) -> list[tuple[Any, ...]]: ...


class Connection(Protocol):
    def cursor(self) -> Any: ...  # Any: context manager de cursor do driver


def sql_checks(directory: Path = CHECKS_DIR) -> dict[str, str]:
    """Nome → consulta, em ordem (t01a ... t16)."""
    return {p.stem: p.read_text(encoding="utf-8") for p in sorted(directory.glob("t*.sql"))}


def run_sql_checks(conn: Connection, checks: Mapping[str, str] | None = None) -> list[Violations]:
    """Roda cada consulta numa transação só de leitura do chamador; não escreve nada."""
    results = []
    for name, query in (checks or sql_checks()).items():
        with conn.cursor() as cur:
            cur.execute("SET search_path TO ubereats")
            cur.execute(query)
            rows = cur.fetchall()
        results.append(Violations(name, len(rows), tuple(tuple(r) for r in rows[:SAMPLE_SIZE])))
    return results


def _violations(name: str, rows: Sequence[tuple[Any, ...]]) -> Violations:
    return Violations(name, len(rows), tuple(rows[:SAMPLE_SIZE]))


# --- T17: referências ao Oracle e cidades idênticas -----------------------------------------


@dataclass(frozen=True)
class CrossBankRefs:
    """Ids lidos no Postgres que apontam para o Oracle (ext → Oracle.*)."""

    customer_refs: Mapping[str, set[int]]  # "orders.customer_id" → ids
    driver_refs: Mapping[str, set[int]]  # "shifts.driver_id" → ids
    order_cities: Sequence[tuple[int, int, int]]  # (order_id, customer_id, city_id)
    shift_cities: Sequence[tuple[int, int, int]]  # (shift_id, driver_id, city_id)


def check_t17(
    refs: CrossBankRefs,
    customer_city: Mapping[int, int],
    driver_city: Mapping[int, int],
    pg_cities: Iterable[tuple[int, str, str]],
    oracle_cities: Iterable[tuple[int, str, str]],
) -> list[Violations]:
    """L0 #10 e #11. A cidade atual vale como cidade na compra porque o ShadowTraffic nunca a muda (F5.5)."""
    missing_c = [
        (col, i)
        for col, ids in refs.customer_refs.items()
        for i in sorted(ids - customer_city.keys())
    ]
    missing_d = [
        (col, i) for col, ids in refs.driver_refs.items() for i in sorted(ids - driver_city.keys())
    ]
    pg, ora = set(pg_cities), set(oracle_cities)
    cities_diff = [("so_postgres", *c) for c in sorted(pg - ora)] + [
        ("so_oracle", *c) for c in sorted(ora - pg)
    ]
    order_city = [
        (o, c, city)
        for o, c, city in refs.order_cities
        if c in customer_city and customer_city[c] != city
    ]
    shift_city = [
        (s, d, city)
        for s, d, city in refs.shift_cities
        if d in driver_city and driver_city[d] != city
    ]
    return [
        _violations("t17a_cliente_existe", missing_c),
        _violations("t17b_motorista_existe", missing_d),
        _violations("t17c_cidades_identicas", cities_diff),
        _violations("t17d_cidade_do_pedido", order_city),
        _violations("t17e_cidade_do_turno", shift_city),
    ]


# --- T18 e T19: perfis do MongoDB ------------------------------------------------------------


def check_t18(
    profiles: Iterable[Mapping[str, Any]],  # Any: documento BSON já decodificado
    product_restaurant: Mapping[int, int],
    restaurant_ids: Iterable[int],
) -> list[Violations]:
    """RN-23: cardápio só com produtos existentes do próprio restaurante; todo restaurante tem perfil."""
    profiles = list(profiles)
    bad_product, repeated = [], []
    for doc in profiles:
        seen: set[int] = set()
        for item in doc["menu_items"]:
            pid = int(item["product_id"])
            if product_restaurant.get(pid) != int(doc["_id"]):
                bad_product.append((int(doc["_id"]), pid))
            if pid in seen:
                repeated.append((int(doc["_id"]), pid))
            seen.add(pid)
    with_profile = {int(d["_id"]) for d in profiles}
    without = [(r,) for r in sorted(set(restaurant_ids) - with_profile)]
    orphans = [(r,) for r in sorted(with_profile - set(restaurant_ids))]
    return [
        _violations("t18a_produto_do_restaurante", bad_product),
        _violations("t18b_produto_repetido_no_perfil", repeated),
        _violations("t18c_restaurante_sem_perfil", without),
        _violations("t18d_perfil_sem_restaurante", orphans),
    ]


def _hhmm(value: str) -> time:
    hour, minute = value.split(":")
    return time(int(hour), int(minute))


def windows_of(doc: Mapping[str, Any]) -> list[tuple[time, time]]:  # Any: documento BSON
    return sorted((_hhmm(w["start_time"]), _hhmm(w["end_time"])) for w in doc["service_windows"])


def check_t19(profiles: Iterable[Mapping[str, Any]]) -> Violations:
    """F3.2: end_time > start_time e janelas sem sobreposição (o validador não vê isso)."""
    rows = []
    for doc in profiles:
        windows = windows_of(doc)
        for start, end in windows:
            if end <= start:
                rows.append(
                    (int(doc["_id"]), "fim_antes_do_inicio", start.isoformat(), end.isoformat())
                )
        for (_, end1), (start2, _) in pairwise(windows):
            if start2 < end1:
                rows.append((int(doc["_id"]), "sobreposicao", end1.isoformat(), start2.isoformat()))
    return _violations("t19_janelas_validas", rows)


def check_t06_restock_windows(
    restocks: Iterable[
        tuple[int, int, datetime]
    ],  # (stock_movement_id, restaurant_id, occurred_at)
    windows_by_restaurant: Mapping[int, Sequence[tuple[time, time]]],
) -> Violations:
    """RN-40: reposição só fora das janelas ([início, fim) na hora de Brasília, sem fuso)."""
    rows = []
    for movement_id, restaurant_id, occurred_at in restocks:
        windows = windows_by_restaurant.get(restaurant_id)
        if windows is None:
            rows.append((movement_id, restaurant_id, "restaurante_sem_perfil"))
            continue
        at = occurred_at.time()
        if any(start <= at < end for start, end in windows):
            rows.append((movement_id, restaurant_id, occurred_at.isoformat(sep=" ")))
    return _violations("t06c_reposicao_fora_das_janelas", rows)
