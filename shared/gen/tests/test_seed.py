"""Seeds (F5.4): catálogo coerente por restaurante, estoque inicial, perfis e conexões."""

from __future__ import annotations

from decimal import Decimal
from pathlib import Path

import pytest
from simulator.checks import check_t18, check_t19
from simulator.db import Settings, read_env_file
from simulator.params import load_parameters
from simulator.seed.catalog import (
    ID_BLOCK,
    build_catalog,
    daily_units_per_product,
    initial_stock,
    load_catalog,
)
from simulator.seed.profiles import MenuProduct, build_profile, same_content

CATALOG = load_catalog()
PARAMS = load_parameters()
RANGE = PARAMS.section("scale")["products_per_restaurant"]


def test_catalogo_de_referencia() -> None:
    assert set(CATALOG.cuisines) == {
        "brazilian",
        "italian",
        "japanese",
        "burger",
        "arabic",
        "healthy",
    }
    for dishes in CATALOG.cuisines.values():
        assert any(d.section in ("mains", "combos") for d in dishes)


@pytest.mark.parametrize("cuisine", sorted(CATALOG.cuisines))
def test_catalogo_coerente_em_muitos_restaurantes(cuisine: str) -> None:
    for restaurant_id in range(1, 201):
        rc = build_catalog(restaurant_id, cuisine, CATALOG, RANGE)
        products = {p.product_id: p for p in rc.products}
        items = {s.stock_item_id: s for s in rc.stock_items}
        assert RANGE[0] <= len(products) <= RANGE[1] or len(products) == len(
            CATALOG.cuisines[cuisine]
        ) + len(CATALOG.shared)
        assert any(p.product_type in ("mains", "combos") for p in products.values())
        assert all(
            pid // ID_BLOCK == restaurant_id for pid in products
        )  # bloco de ids do restaurante
        assert all(s.restaurant_id == restaurant_id for s in items.values())  # T4b
        assert len({s.name for s in items.values()}) == len(items)  # único (restaurant_id, name)
        assert {r.product_id for r in rc.recipes} == set(products)  # todo produto tem ficha (RN-37)
        assert all(r.stock_item_id in items and r.quantity > 0 for r in rc.recipes)
        assert all(Decimal(0) <= p.unit_cost < p.price for p in products.values())
        for r in rc.recipes:
            item = items[r.stock_item_id]
            if item.kind == "ready":  # produto pronto: o item é ele mesmo, 1 unidade
                assert (item.name, item.unit, r.quantity) == (
                    products[r.product_id].name,
                    "unit",
                    1,
                )


def test_catalogo_e_deterministico() -> None:
    assert build_catalog(42, "burger", CATALOG, RANGE) == build_catalog(
        42, "burger", CATALOG, RANGE
    )
    assert build_catalog(42, "burger", CATALOG, RANGE) != build_catalog(
        43, "burger", CATALOG, RANGE
    )


def test_cozinha_desconhecida() -> None:
    with pytest.raises(ValueError, match="sem pratos"):
        build_catalog(1, "francesa", CATALOG, RANGE)


def test_estoque_inicial() -> None:
    rc = build_catalog(7, "italian", CATALOG, RANGE)
    daily = daily_units_per_product(PARAMS.raw, len(rc.products))
    assert Decimal("0.1") < daily < Decimal(20)
    stock = initial_stock(rc, daily, 2)
    assert set(stock) == {s.stock_item_id for s in rc.stock_items}
    assert all(q >= 1 and q == q.to_integral_value() for q in stock.values())


def _perfil(restaurant_id: int, cuisine: str) -> tuple[dict[str, object], dict[int, int]]:
    rc = build_catalog(restaurant_id, cuisine, CATALOG, RANGE)
    menu = [MenuProduct(p.product_id, p.name, p.product_type) for p in rc.products]
    share = float(PARAMS.section("scale")["restaurants_with_two_windows"])
    return build_profile(restaurant_id, cuisine, menu, CATALOG, share), {
        p.product_id: restaurant_id for p in rc.products
    }


def test_perfis_passam_t18_e_t19() -> None:
    perfis, produtos = [], {}
    for rid, cuisine in enumerate(sorted(CATALOG.cuisines) * 30, start=1):
        perfil, prods = _perfil(rid, cuisine)
        perfis.append(perfil)
        produtos.update(prods)
        assert [i["display_order"] for i in perfil["menu_items"]] == list(range(1, len(prods) + 1))  # type: ignore[index]
    assert all(r.ok for r in check_t18(perfis, produtos, range(1, len(perfis) + 1)))
    assert check_t19(perfis).ok
    janelas = [len(p["service_windows"]) for p in perfis]  # type: ignore[arg-type]
    assert 1 in janelas and 2 in janelas
    abertura = min(w["start_time"] for p in perfis for w in p["service_windows"])  # type: ignore[attr-defined]
    assert abertura >= "06:00"  # o restock inicial é às 00:00, antes de qualquer janela


def test_perfil_deterministico_e_comparacao() -> None:
    a, _ = _perfil(5, "japanese")
    b, _ = _perfil(5, "japanese")
    assert a == b
    assert same_content({**a, "created_at": "x"}, b)
    assert not same_content(None, b)
    assert not same_content({**a, "service_windows": []}, b)


def test_env_e_conexoes(tmp_path: Path) -> None:
    env = tmp_path / ".env"
    env.write_text(
        "# comentário\nPOSTGRES_PORT=5432\nPOSTGRES_DB=ubereats\nPOSTGRES_USERNAME=app\n"
        "POSTGRES_PASSWORD='segredo'\nMONGO_PORT=27017\nlinha sem igual\n",
        encoding="utf-8",
    )
    values = read_env_file(env)
    assert values["POSTGRES_PASSWORD"] == "segredo" and "linha sem igual" not in values
    settings = Settings(values)
    info = settings.postgres_conninfo()
    assert (info["host"], info["port"]) == ("127.0.0.1", 5432)
    assert "timezone=America/Sao_Paulo" in info["options"]
    assert settings.mongo_uri() == "mongodb://127.0.0.1:27017/?directConnection=true"
    override = Settings(
        {**values, "SIMULATOR_POSTGRES_HOST": "outro", "SIMULATOR_POSTGRES_PORT": "15433"}
    )
    assert (override.postgres_conninfo()["host"], override.postgres_conninfo()["port"]) == (
        "outro",
        15433,
    )
    assert "segredo" not in repr(settings)
    with pytest.raises(KeyError, match="ORACLE_PORT ausente"):
        settings.oracle_conninfo()
