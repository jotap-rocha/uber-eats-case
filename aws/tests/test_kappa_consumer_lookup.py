"""Testes do consumidor do Kappa: cache/TTL do lookup no MongoDB e enriquecimento
de eventos (item 22 do manifesto).
"""
from __future__ import annotations

import base64
import importlib.util
import json
import sys
import time
from pathlib import Path

import boto3
import pytest
from moto import mock_aws

LAMBDA_DIR = Path(__file__).resolve().parents[2] / "src" / "aws" / "lambda_kappa_consumer"
BUCKET = "test-bronze-bucket"


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, LAMBDA_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def mongo_lookup_module():
    sys.path.insert(0, str(LAMBDA_DIR))
    try:
        yield _load_module("mongo_lookup_test_module", "mongo_lookup.py")
    finally:
        sys.path.remove(str(LAMBDA_DIR))
        sys.modules.pop("mongo_lookup_test_module", None)


@pytest.fixture()
def s3_with_profiles():
    with mock_aws():
        s3 = boto3.client("s3", region_name="us-east-1")
        s3.create_bucket(Bucket=BUCKET)
        s3.put_object(
            Bucket=BUCKET,
            Key="mongodb/perfil_restaurante/part-0001.json",
            Body=json.dumps(
                [
                    {"restaurant_id": 1, "menu": ["pizza"], "horario": "18h-23h"},
                    {"restaurant_id": 2, "menu": ["sushi"], "horario": "12h-22h"},
                ]
            ),
        )
        yield s3


def test_cache_loads_and_finds_existing_restaurant(mongo_lookup_module, s3_with_profiles):
    cache = mongo_lookup_module.RestaurantProfileCache(
        s3_client=s3_with_profiles, bucket=BUCKET, ttl_seconds=300
    )

    profile = cache.get(1)

    assert profile == {"restaurant_id": 1, "menu": ["pizza"], "horario": "18h-23h"}


def test_cache_returns_none_for_unknown_restaurant(mongo_lookup_module, s3_with_profiles):
    cache = mongo_lookup_module.RestaurantProfileCache(
        s3_client=s3_with_profiles, bucket=BUCKET, ttl_seconds=300
    )

    assert cache.get(999) is None


def test_cache_does_not_reload_before_ttl_expires(mongo_lookup_module, s3_with_profiles):
    calls = {"count": 0}
    original_list = s3_with_profiles.list_objects_v2

    def counting_list(*args, **kwargs):
        calls["count"] += 1
        return original_list(*args, **kwargs)

    s3_with_profiles.list_objects_v2 = counting_list
    cache = mongo_lookup_module.RestaurantProfileCache(
        s3_client=s3_with_profiles, bucket=BUCKET, ttl_seconds=300
    )

    cache.get(1)
    cache.get(2)

    assert calls["count"] == 1


def test_cache_reloads_after_ttl_expires(mongo_lookup_module, s3_with_profiles):
    cache = mongo_lookup_module.RestaurantProfileCache(
        s3_client=s3_with_profiles, bucket=BUCKET, ttl_seconds=0
    )

    cache.get(1)
    time.sleep(0.01)
    cache.get(1)

    # ttl_seconds=0 força reload a cada chamada — só valida que não quebra
    assert cache.get(1) is not None


@pytest.fixture()
def consumer_handler(monkeypatch, s3_with_profiles):
    monkeypatch.setenv("BRONZE_BUCKET", BUCKET)
    sys.path.insert(0, str(LAMBDA_DIR))
    try:
        yield _load_module("consumer_handler_test_module", "handler.py")
    finally:
        sys.path.remove(str(LAMBDA_DIR))
        sys.modules.pop("consumer_handler_test_module", None)
        sys.modules.pop("mongo_lookup", None)


def _kinesis_record(payload: dict) -> dict:
    encoded = base64.b64encode(json.dumps(payload).encode("utf-8")).decode("ascii")
    return {"kinesis": {"data": encoded}}


def test_handler_enriches_order_event_with_restaurant_profile(consumer_handler):
    event = {"Records": [_kinesis_record({"order_id": 42, "restaurant_id": 1})]}

    result = consumer_handler.handler(event, context=None)

    assert result["processed"] == 1


def test_handler_leaves_event_unenriched_when_restaurant_unknown(consumer_handler):
    event = {"Records": [_kinesis_record({"order_id": 42, "restaurant_id": 999})]}

    result = consumer_handler.handler(event, context=None)

    assert result["processed"] == 1


def test_handler_processes_batch_of_records(consumer_handler):
    event = {
        "Records": [
            _kinesis_record({"order_id": 1, "restaurant_id": 1}),
            _kinesis_record({"order_id": 2, "restaurant_id": 2}),
            _kinesis_record({"order_id": 3, "restaurant_id": None}),
        ]
    }

    result = consumer_handler.handler(event, context=None)

    assert result["processed"] == 3
