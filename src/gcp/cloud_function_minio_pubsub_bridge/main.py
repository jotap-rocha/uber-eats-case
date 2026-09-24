"""Ponte MinIO -> Pub/Sub (Decisão 7, DESIGN_INGESTAO_GCP_FASE3.md).

Recebe a notificação de bucket do MinIO (destino Webhook, formato compatível
com S3 Event Notification) e publica uma mensagem no Pub/Sub por objeto
notificado. Não tem lógica de negócio - só ponte de infraestrutura, mesmo
papel da Lambda ponte da Fase 2/AWS.
"""
from __future__ import annotations

import json
import os

import functions_framework
from google.cloud import pubsub_v1
from teams_notify import notify_bridge_failure

PROJECT_ID = os.environ["GCP_PROJECT_ID"]
TOPIC_ID = os.environ["PUBSUB_TOPIC_MINIO"]
EXPECTED_AUTH_TOKEN = os.environ["MINIO_WEBHOOK_AUTH_TOKEN"]

_publisher = pubsub_v1.PublisherClient()


class UnauthorizedWebhookError(Exception):
    """Header Authorization ausente ou não corresponde ao token configurado no MinIO."""


def _authorize(request) -> None:
    token = request.headers.get("Authorization", "")
    if token != f"Bearer {EXPECTED_AUTH_TOKEN}":
        raise UnauthorizedWebhookError("Authorization header ausente ou inválido")


def _build_payload(record: dict) -> dict:
    return {
        "bucket": record["s3"]["bucket"]["name"],
        "key": record["s3"]["object"]["key"],
        "event_name": record["eventName"],
        "cdc_source_system": "minio-ubereats",
    }


@functions_framework.http
def handler(request):
    try:
        _authorize(request)
    except UnauthorizedWebhookError as exc:
        return ({"error": str(exc)}, 401)

    body = request.get_json(silent=True) or {}
    records = body.get("Records", [])

    topic_path = _publisher.topic_path(PROJECT_ID, TOPIC_ID)
    processed = 0
    for record in records:
        payload = _build_payload(record)
        try:
            future = _publisher.publish(topic_path, json.dumps(payload).encode("utf-8"))
            future.result(timeout=10)
            processed += 1
        except Exception as exc:
            notify_bridge_failure(payload=payload, error=str(exc))
            raise

    return ({"processed": processed}, 200)
