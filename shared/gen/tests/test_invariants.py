"""T1 a T19 (F5.9): consultas versionadas, verificações entre bancos e o gate contra o Postgres."""

from __future__ import annotations

import os
import re
from datetime import datetime, time

import pytest
from simulator.checks import (
    CrossBankRefs,
    check_t06_restock_windows,
    check_t17,
    check_t18,
    check_t19,
    run_sql_checks,
    sql_checks,
)

DML = re.compile(
    r"\b(insert|update|delete|merge|drop|truncate|alter|create|grant)\b", re.IGNORECASE
)


def _sem_comentarios(sql: str) -> str:
    return "\n".join(line for line in sql.splitlines() if not line.lstrip().startswith("--"))


def test_consultas_versionadas() -> None:
    checks = sql_checks()
    assert len(checks) == 36
    assert {name[:3] for name in checks} == {f"t{n:02d}" for n in range(1, 17)}
    for name, sql in checks.items():
        body = _sem_comentarios(sql).strip()
        assert body.split()[0].upper() in {"SELECT", "WITH"}, name
        assert not DML.search(body), f"{name}: consulta de verificação não escreve"
        assert body.endswith(";") and body.count(";") == 1, name


# --- T17 --------------------------------------------------------------------------------------

CIDADES = [(3550308, "São Paulo", "SP"), (3304557, "Rio de Janeiro", "RJ")]


def test_t17_ok() -> None:
    refs = CrossBankRefs(
        customer_refs={"orders.customer_id": {1, 2}, "checkouts.customer_id": {1, 2, 3}},
        driver_refs={"shifts.driver_id": {10}},
        order_cities=[(100, 1, 3550308), (101, 2, 3304557)],
        shift_cities=[(500, 10, 3550308)],
    )
    results = check_t17(refs, {1: 3550308, 2: 3304557, 3: 3550308}, {10: 3550308}, CIDADES, CIDADES)
    assert all(r.ok for r in results)


def test_t17_violacoes() -> None:
    refs = CrossBankRefs(
        customer_refs={"orders.customer_id": {1, 99}},
        driver_refs={"tips.driver_id": {77}},
        order_cities=[(100, 1, 3304557)],
        shift_cities=[(500, 10, 3304557)],
    )
    oracle = [(3550308, "São Paulo", "SP"), (3304557, "Rio de Janeiro ", "RJ")]
    results = {r.check: r for r in check_t17(refs, {1: 3550308}, {10: 3550308}, CIDADES, oracle)}
    assert results["t17a_cliente_existe"].sample == (("orders.customer_id", 99),)
    assert results["t17b_motorista_existe"].sample == (("tips.driver_id", 77),)
    assert results["t17c_cidades_identicas"].count == 2  # nome com espaço a mais nas duas direções
    assert results["t17d_cidade_do_pedido"].sample == ((100, 1, 3304557),)
    assert results["t17e_cidade_do_turno"].sample == ((500, 10, 3304557),)


# --- T18 e T19 --------------------------------------------------------------------------------


def _perfil(rid: int, produtos: list[int], janelas: list[tuple[str, str]]) -> dict[str, object]:
    return {
        "_id": rid,
        "service_windows": [{"start_time": a, "end_time": b} for a, b in janelas],
        "menu_items": [{"product_id": p} for p in produtos],
    }


def test_t18() -> None:
    perfis = [
        _perfil(1, [10, 11], [("11:00", "15:00")]),
        _perfil(2, [20, 20, 10], [("18:00", "23:00")]),
    ]
    results = {r.check: r for r in check_t18(perfis, {10: 1, 11: 1, 20: 2}, [1, 2, 3])}
    assert results["t18a_produto_do_restaurante"].sample == ((2, 10),)
    assert results["t18b_produto_repetido_no_perfil"].sample == ((2, 20),)
    assert results["t18c_restaurante_sem_perfil"].sample == ((3,),)
    assert results["t18d_perfil_sem_restaurante"].ok


def test_t19() -> None:
    ok = [_perfil(1, [], [("18:00", "23:00"), ("11:00", "15:00")])]
    assert check_t19(ok).ok
    ruins = [
        _perfil(2, [], [("15:00", "11:00")]),
        _perfil(3, [], [("11:00", "15:00"), ("14:30", "20:00")]),
    ]
    result = check_t19(ruins)
    assert {row[:2] for row in result.sample} == {(2, "fim_antes_do_inicio"), (3, "sobreposicao")}


def test_t06_reposicao_fora_das_janelas() -> None:
    janelas = {1: [(time(11), time(15)), (time(18), time(23))]}
    restocks = [
        (1, 1, datetime(2026, 11, 4, 0, 0)),  # antes da primeira janela
        (2, 1, datetime(2026, 11, 4, 15, 0)),  # fim da janela é aberto: pode repor às 15:00
        (3, 1, datetime(2026, 11, 4, 12, 30)),  # durante o almoço: viola
        (4, 9, datetime(2026, 11, 4, 3, 0)),  # restaurante sem perfil: viola
    ]
    result = check_t06_restock_windows(restocks, janelas)
    assert [row[0] for row in result.sample] == [3, 4]


# --- Gate contra um Postgres de verdade (F5.3, passos 8 e 11) ---------------------------------

DSN_VAR = "UBEREATS_CHECKS_DSN"


@pytest.mark.skipif(
    DSN_VAR not in os.environ,
    reason=f"gate da regeração: defina {DSN_VAR} para rodar as consultas num Postgres (só leitura)",
)
def test_invariantes_no_postgres() -> None:
    psycopg = pytest.importorskip(
        "psycopg", reason="driver do Postgres: pip install -r shared/gen/requirements.txt"
    )
    with psycopg.connect(os.environ[DSN_VAR]) as conn:
        conn.read_only = True
        results = run_sql_checks(conn)
    falhas = {r.check: (r.count, r.sample) for r in results if not r.ok}
    assert not falhas, f"invariantes violados: {falhas}"
