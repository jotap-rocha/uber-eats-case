"""Testes do consumidor do Kappa: lookup no BigLake Iceberg (MongoDB) e
enriquecimento de eventos (item 31 do manifesto).
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

DATAFLOW_DIR = Path(__file__).resolve().parents[2] / "src" / "gcp" / "dataflow_kappa_consumer"


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, DATAFLOW_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def mongo_lookup_module():
    sys.path.insert(0, str(DATAFLOW_DIR))
    try:
        yield _load_module("mongo_lookup_test_module", "mongo_lookup.py")
    finally:
        sys.path.remove(str(DATAFLOW_DIR))
        sys.modules.pop("mongo_lookup_test_module", None)


def _fake_bigquery_client(rows: list[dict]):
    client = MagicMock()
    result = MagicMock()
    result.result.return_value = rows
    client.query.return_value = result
    return client


def test_load_restaurant_profiles_indexes_by_restaurant_id(mongo_lookup_module):
    rows = [
        {"restaurant_id": 1, "menu": ["pizza"], "horarios": "18h-23h"},
        {"restaurant_id": 2, "menu": ["sushi"], "horarios": "12h-22h"},
    ]
    client = _fake_bigquery_client(rows)

    profiles = mongo_lookup_module.load_restaurant_profiles(bigquery_client=client)

    assert profiles[1]["menu"] == ["pizza"]
    assert profiles[2]["horarios"] == "12h-22h"


def test_load_restaurant_profiles_empty_table(mongo_lookup_module):
    client = _fake_bigquery_client([])

    profiles = mongo_lookup_module.load_restaurant_profiles(bigquery_client=client)

    assert profiles == {}


@pytest.fixture()
def enrich_dofn(monkeypatch):
    fake_beam = MagicMock()

    class _FakeDoFn:
        def process(self, *args, **kwargs):
            raise NotImplementedError

    fake_beam.DoFn = _FakeDoFn
    monkeypatch.setitem(sys.modules, "apache_beam", fake_beam)
    monkeypatch.setitem(sys.modules, "apache_beam.options.pipeline_options", MagicMock())

    sys.path.insert(0, str(DATAFLOW_DIR))
    try:
        module = _load_module("pipeline_test_module", "pipeline.py")
        yield module.EnrichWithRestaurantProfile()
    finally:
        sys.path.remove(str(DATAFLOW_DIR))
        sys.modules.pop("pipeline_test_module", None)
        sys.modules.pop("mongo_lookup", None)


def test_enrich_adds_profile_when_restaurant_known(enrich_dofn):
    element = json.dumps({"order_id": 42, "restaurant_id": 1}).encode("utf-8")
    profiles = {1: {"menu": ["pizza"]}}

    result = list(enrich_dofn.process(element, profiles))

    assert result[0]["restaurant_profile"] == {"menu": ["pizza"]}


def test_enrich_leaves_event_unenriched_when_restaurant_unknown(enrich_dofn):
    element = json.dumps({"order_id": 42, "restaurant_id": 999}).encode("utf-8")
    profiles = {1: {"menu": ["pizza"]}}

    result = list(enrich_dofn.process(element, profiles))

    assert "restaurant_profile" not in result[0]
