"""Início do histórico: `--days`, retomada só com pedidos e cobertura do restock inicial."""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta

import pytest
from simulator.__main__ import positive_int
from simulator.engine import (
    default_start,
    initial_start,
    partial_run_error,
    restock_coverage_error,
)
from simulator.params import load_parameters

HOJE = datetime(2026, 11, 10, 15, 30)
RESTOCK_DO_SEED = datetime(2026, 10, 11, 0, 0)  # seed com o padrão de 30 dias


def test_usa_backfill_days_do_parametro() -> None:
    params = load_parameters()
    dias = int(params.section("clock")["backfill_days"])
    assert default_start(params, HOJE) == datetime(2026, 11, 10) - timedelta(days=dias)


def test_days_sobrepoe_o_parametro() -> None:
    assert default_start(load_parameters(), HOJE, 7) == datetime(2026, 11, 3, 0, 0)


def test_sem_pedidos_o_inicio_vem_de_days_mesmo_com_evento_do_seed() -> None:
    """Regressão: o restock do seed contava como "último evento" e o --days era ignorado."""
    inicio = initial_start(
        load_parameters(),
        HOJE,
        days=365,
        resumed=RESTOCK_DO_SEED,
        has_orders=False,
    )
    assert inicio == datetime(2025, 11, 10, 0, 0)


def test_com_pedidos_retoma_do_ultimo_evento() -> None:
    ultimo = datetime(2026, 3, 1, 21, 40)
    inicio = initial_start(load_parameters(), HOJE, days=365, resumed=ultimo, has_orders=True)
    assert inicio == ultimo


def test_com_pedidos_mas_sem_evento_gravado_cai_no_padrao() -> None:
    inicio = initial_start(load_parameters(), HOJE, days=7, resumed=None, has_orders=True)
    assert inicio == datetime(2026, 11, 3, 0, 0)


def test_restock_posterior_ao_inicio_e_recusado() -> None:
    erro = restock_coverage_error(datetime(2025, 11, 10), RESTOCK_DO_SEED)
    assert erro is not None
    assert "--start-day" in erro


def test_restock_no_inicio_ou_antes_passa() -> None:
    inicio = datetime(2025, 11, 10)
    assert restock_coverage_error(inicio, inicio) is None
    assert restock_coverage_error(inicio, datetime(2025, 11, 1)) is None


def test_sem_restock_gravado_nao_recusa() -> None:
    assert restock_coverage_error(datetime(2025, 11, 10), None) is None


def test_restock_do_mesmo_dia_com_hora_nao_e_recusado() -> None:
    assert restock_coverage_error(datetime(2025, 11, 10), datetime(2025, 11, 10, 6, 0)) is None


def test_sem_pedidos_e_so_o_restock_do_seed_nao_e_execucao_parcial() -> None:
    assert partial_run_error(RESTOCK_DO_SEED, RESTOCK_DO_SEED) is None
    assert partial_run_error(None, RESTOCK_DO_SEED) is None


def test_eventos_alem_do_restock_sem_pedidos_sao_execucao_parcial() -> None:
    erro = partial_run_error(datetime(2026, 10, 11, 7, 0), RESTOCK_DO_SEED)
    assert erro is not None
    assert "task 14" in erro


def test_days_aceita_inteiro_positivo() -> None:
    assert positive_int("365") == 365


@pytest.mark.parametrize("valor", ["0", "-5"])
def test_days_recusa_zero_e_negativo(valor: str) -> None:
    with pytest.raises(argparse.ArgumentTypeError):
        positive_int(valor)
