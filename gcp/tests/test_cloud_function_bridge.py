"""Testes da Cloud Function ponte MinIO -> Pub/Sub (item 30 do manifesto).

Carrega main.py por caminho de arquivo (evita colidir com módulos de mesmo
nome de outras features) e mockar o PublisherClient do Pub/Sub, sem depender
de credenciais/rede real do GCP.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

FUNCTION_DIR = (
    Path(__file__).resolve().parents[2] / "src" / "gcp" / "cloud_function_minio_pubsub_bridge"
)
TOPIC_ID = "test-minio-bridge-topic"
AUTH_TOKEN = "test-token"


class _FakeRequest:
    def __init__(self, *, headers: dict, json_body: dict):
        self.headers = headers
        self._json_body = json_body

    def get_json(self, silent: bool = False):
        return self._json_body


@pytest.fixture()
def bridge_module(monkeypatch):
    monkeypatch.setenv("PUBSUB_TOPIC_MINIO", TOPIC_ID)
    monkeypatch.setenv("MINIO_WEBHOOK_AUTH_TOKEN", AUTH_TOKEN)
    monkeypatch.setenv("TEAMS_WEBHOOK_URL", "")

    fake_future = MagicMock()
    fake_future.result.return_value = None
    fake_publisher = MagicMock()
    fake_publisher.publish.return_value = fake_future
    fake_publisher.topic_path.return_value = f"projects/test-project/topics/{TOPIC_ID}"

    fake_pubsub_module = MagicMock()
    fake_pubsub_module.PublisherClient.return_value = fake_publisher
    monkeypatch.setitem(sys.modules, "google.cloud.pubsub_v1", fake_pubsub_module)
    monkeypatch.setitem(sys.modules, "functions_framework", MagicMock(http=lambda fn: fn))

    sys.path.insert(0, str(FUNCTION_DIR))
    try:
        spec = importlib.util.spec_from_file_location("bridge_main_module", FUNCTION_DIR / "main.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module._fake_publisher = fake_publisher
        yield module
    finally:
        sys.path.remove(str(FUNCTION_DIR))
        sys.modules.pop("bridge_main_module", None)
        sys.modules.pop("teams_notify", None)


def _webhook_request(*, key: str = "oracle/orders/2026/09/11/obj123.json", auth: str = f"Bearer {AUTH_TOKEN}") -> _FakeRequest:
    return _FakeRequest(
        headers={"Authorization": auth},
        json_body={
            "Records": [
                {
                    "eventName": "s3:ObjectCreated:Put",
                    "s3": {"bucket": {"name": "uber-eats"}, "object": {"key": key}},
                }
            ]
        },
    )


def test_handler_publishes_message_on_valid_webhook(bridge_module):
    body, status = bridge_module.handler(_webhook_request())

    assert status == 200
    assert body["processed"] == 1
    bridge_module._fake_publisher.publish.assert_called_once()
    _, published_bytes = bridge_module._fake_publisher.publish.call_args[0]
    payload = json.loads(published_bytes)
    assert payload["key"] == "oracle/orders/2026/09/11/obj123.json"
    assert payload["cdc_source_system"] == "minio-ubereats"


def test_handler_rejects_missing_or_wrong_auth_token(bridge_module):
    _body, status = bridge_module.handler(_webhook_request(auth="Bearer wrong-token"))

    assert status == 401
    bridge_module._fake_publisher.publish.assert_not_called()


def test_handler_processes_multiple_records_in_one_webhook_call(bridge_module):
    request = _FakeRequest(
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json_body={
            "Records": [
                {"eventName": "s3:ObjectCreated:Put", "s3": {"bucket": {"name": "b"}, "object": {"key": "a.json"}}},
                {"eventName": "s3:ObjectCreated:Put", "s3": {"bucket": {"name": "b"}, "object": {"key": "b.json"}}},
            ]
        },
    )

    body, status = bridge_module.handler(request)

    assert status == 200
    assert body["processed"] == 2
    assert bridge_module._fake_publisher.publish.call_count == 2
