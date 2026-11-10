"""Template do ShadowTraffic (F5.2): coerente com a DDL do init, com os parâmetros e com o catálogo."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import pytest
from simulator.params import REPO_ROOT, load_parameters
from simulator.seed.catalog import load_catalog

TEMPLATE = REPO_ROOT / "shared" / "gen" / "unified" / "uber-eats.json.template"
DDL = {
    "customers": REPO_ROOT / "shared" / "sql" / "oracle" / "02_create_tables.sh",
    "drivers": REPO_ROOT / "shared" / "sql" / "oracle" / "02_create_tables.sh",
    "restaurants": REPO_ROOT / "shared" / "sql" / "postgres" / "01_catalogo.sql",
}


def _template() -> dict[str, Any]:  # Any: config JSON do ShadowTraffic
    text = TEMPLATE.read_text(encoding="utf-8")
    assert text.count("REPLACE_CITIES_JSON") == 3, (
        "cada cadastro sorteia a cidade da lista injetada"
    )
    text = text.replace("REPLACE_CITIES_JSON", '[{"city_id": 3550308, "lat": -23.5, "lon": -46.6}]')
    text = text.replace("REPLACE_POSTGRES_PORT", "5432").replace("REPLACE_ORACLE_PORT", "1521")
    return json.loads(text)


def _columns(path: Path, table: str) -> dict[str, bool]:
    """Coluna → obrigatória sem default (o gerador precisa preenchê-la)."""
    ddl = path.read_text(encoding="utf-8")
    body = re.search(rf"CREATE TABLE {table} \((.*?)\n\);", ddl, re.DOTALL | re.IGNORECASE)
    assert body, f"{table} não achada em {path.name}"
    cols = {}
    for line in body.group(1).splitlines():
        line = line.strip()
        if not line or line.upper().startswith("CONSTRAINT"):
            continue
        name = line.split()[0].lower()
        upper = line.upper()
        cols[name] = "NOT NULL" in upper and "DEFAULT" not in upper and "IDENTITY" not in upper
    return cols


def test_so_cadastros_e_sem_minio() -> None:
    t = _template()
    assert {g["table"]: g["connection"] for g in t["generators"]} == {
        "customers": "oracle",
        "drivers": "oracle",
        "restaurants": "postgres",
    }
    assert set(t["connections"]) == {"oracle", "postgres"}  # ADR 010


@pytest.mark.parametrize("table", sorted(DDL))
def test_campos_iguais_as_colunas_da_ddl(table: str) -> None:
    """O ShadowTraffic usa a chave do row como nome de coluna, sem alias (skill, item 1)."""
    gen = next(g for g in _template()["generators"] if g["table"] == table)
    cols = _columns(DDL[table], table)
    row = set(gen["row"])
    assert row <= set(cols), f"{table}: campos sem coluna {sorted(row - set(cols))}"
    obrigatorias = {c for c, req in cols.items() if req}
    assert obrigatorias <= row, f"{table}: obrigatórias sem valor {sorted(obrigatorias - row)}"


def test_metas_iguais_aos_parametros() -> None:
    scale = load_parameters().section("scale")
    cities = len(load_parameters().cities)
    metas = {g["table"]: g["localConfigs"]["maxEvents"] for g in _template()["generators"]}
    assert metas == {
        "customers": scale["customers"],
        "drivers": scale["drivers"],
        "restaurants": scale["restaurants_per_city"] * cities,
    }


def test_cozinhas_iguais_ao_catalogo() -> None:
    gen = next(g for g in _template()["generators"] if g["table"] == "restaurants")
    assert set(gen["row"]["cuisine_type"]["choices"]) == set(load_catalog().cuisines)


def test_chave_sequencial_em_vars_id() -> None:
    """O toggle-shadowtraffic.ps1 recalcula vars.id.startingFrom em cada cadastro (skill, item 4)."""
    for gen in _template()["generators"]:
        assert gen["vars"]["id"]["_gen"] == "sequentialInteger"
        key = {"customers": "customer_id", "drivers": "driver_id", "restaurants": "restaurant_id"}[
            gen["table"]
        ]
        assert gen["row"][key] == {"_gen": "var", "var": "id"}


def test_dominios_iguais_aos_check() -> None:
    gens = {g["table"]: g for g in _template()["generators"]}

    def values(field: dict[str, Any]) -> set[Any]:  # Any: escolha do weightedOneOf
        return {c["value"] for c in field["choices"]}

    assert values(gens["customers"]["row"]["gender"]) == {"female", "male", "other", "not_informed"}
    vehicles = {c["value"]["type"] for c in gens["drivers"]["vars"]["vehicle"]["choices"]}
    assert vehicles == {"car", "motorcycle", "scooter"}  # F2, decisão 3: só motorizado
    for table in gens:
        assert values(gens[table]["row"]["status"]) == {"active", "inactive", "suspended"}
