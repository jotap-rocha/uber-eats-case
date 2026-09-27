"""Testes da Lambda ponte MinIO -> Kinesis (item 21 do manifesto).

Carrega handler.py por caminho de arquivo (evita colidir com o módulo "handler"
da outra Lambda, que tem o mesmo nome) e usa moto para mockar o Kinesis real.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import boto3
import pytest
from moto import mock_aws

LAMBDA_DIR = (
    Path(__file__).resolve().parents[2] / "src" / "aws" / "lambda_minio_kinesis_bridge"
)
STREAM_NAME = "test-kappa-stream"
AUTH_TOKEN = "test-token"


@pytest.fixture()
def bridge_handler(monkeypatch):
    monkeypatch.setenv("KINESIS_STREAM_NAME", STREAM_NAME)
    monkeypatch.setenv("MINIO_WEBHOOK_AUTH_TOKEN", AUTH_TOKEN)
    monkeypatch.setenv("TEAMS_WEBHOOK_URL", "")

    sys.path.insert(0, str(LAMBDA_DIR))
    try:
        spec = importlib.util.spec_from_file_location(
            "bridge_handler_module", LAMBDA_DIR / "handler.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        yield module
    finally:
        sys.path.remove(str(LAMBDA_DIR))
        sys.modules.pop("bridge_handler_module", None)
        sys.modules.pop("teams_notify", None)


def _webhook_event(*, key: str = "orders/2026/09/10/obj123.json", auth: str = AUTH_TOKEN) -> dict:
    return {
        "headers": {"Authorization": auth},
        "body": json.dumps(
            {
                "Records": [
                    {
                        "eventName": "s3:ObjectCreated:Put",
                        "s3": {
                            "bucket": {"name": "ubereats-minio-bucket"},
                            "object": {"key": key},
                        },
                    }
                ]
            }
        ),
    }


@mock_aws
def test_handler_puts_record_on_valid_webhook(bridge_handler):
    kinesis = boto3.client("kinesis", region_name="us-east-1")
    kinesis.create_stream(StreamName=STREAM_NAME, ShardCount=1)

    response = bridge_handler.handler(_webhook_event(), context=None)

    assert response["statusCode"] == 200
    assert json.loads(response["body"])["processed"] == 1

    shard_id = kinesis.describe_stream(StreamName=STREAM_NAME)["StreamDescription"]["Shards"][0]["ShardId"]
    shard_iterator = kinesis.get_shard_iterator(
        StreamName=STREAM_NAME, ShardId=shard_id, ShardIteratorType="TRIM_HORIZON"
    )["ShardIterator"]
    records = kinesis.get_records(ShardIterator=shard_iterator)["Records"]

    assert len(records) == 1
    payload = json.loads(records[0]["Data"])
    assert payload["key"] == "orders/2026/09/10/obj123.json"
    assert payload["cdc_source_system"] == "minio-ubereats"


@mock_aws
def test_handler_rejects_missing_or_wrong_auth_token(bridge_handler):
    kinesis = boto3.client("kinesis", region_name="us-east-1")
    kinesis.create_stream(StreamName=STREAM_NAME, ShardCount=1)

    response = bridge_handler.handler(_webhook_event(auth="wrong-token"), context=None)

    assert response["statusCode"] == 401


@mock_aws
def test_handler_processes_multiple_records_in_one_webhook_call(bridge_handler):
    kinesis = boto3.client("kinesis", region_name="us-east-1")
    kinesis.create_stream(StreamName=STREAM_NAME, ShardCount=1)

    event = {
        "headers": {"Authorization": AUTH_TOKEN},
        "body": json.dumps(
            {
                "Records": [
                    {
                        "eventName": "s3:ObjectCreated:Put",
                        "s3": {"bucket": {"name": "b"}, "object": {"key": "a.json"}},
                    },
                    {
                        "eventName": "s3:ObjectCreated:Put",
                        "s3": {"bucket": {"name": "b"}, "object": {"key": "b.json"}},
                    },
                ]
            }
        ),
    }

    response = bridge_handler.handler(event, context=None)

    assert json.loads(response["body"])["processed"] == 2
