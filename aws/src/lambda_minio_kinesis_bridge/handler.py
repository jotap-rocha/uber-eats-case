"""Ponte MinIO -> Kinesis (Decisão 5, DESIGN_INGESTAO_AWS_FASE2.md).

Recebe a notificação de bucket do MinIO (destino Webhook, formato compatível com
S3 Event Notification) e grava um registro no Kinesis Data Stream por objeto
notificado. Não tem lógica de negócio — só ponte de infraestrutura.
"""
from __future__ import annotations

import json
import os

import boto3
from teams_notify import notify_bridge_failure

_kinesis = boto3.client("kinesis")
STREAM_NAME = os.environ["KINESIS_STREAM_NAME"]
EXPECTED_AUTH_TOKEN = os.environ["MINIO_WEBHOOK_AUTH_TOKEN"]


class UnauthorizedWebhookError(Exception):
    """Header Authorization ausente ou não corresponde ao token configurado no MinIO."""


def _authorize(event: dict) -> None:
    headers = {k.lower(): v for k, v in (event.get("headers") or {}).items()}
    token = headers.get("authorization", "")
    if token != EXPECTED_AUTH_TOKEN:
        raise UnauthorizedWebhookError("Authorization header ausente ou inválido")


def _build_payload(record: dict) -> dict:
    return {
        "bucket": record["s3"]["bucket"]["name"],
        "key": record["s3"]["object"]["key"],
        "event_name": record["eventName"],
        "cdc_source_system": "minio-ubereats",
    }


def handler(event: dict, context) -> dict:
    try:
        _authorize(event)
    except UnauthorizedWebhookError as exc:
        return {"statusCode": 401, "body": json.dumps({"error": str(exc)})}

    body = json.loads(event["body"])
    records = body.get("Records", [])

    processed = 0
    for record in records:
        payload = _build_payload(record)
        try:
            _kinesis.put_record(
                StreamName=STREAM_NAME,
                Data=json.dumps(payload).encode("utf-8"),
                PartitionKey=payload["key"],
            )
            processed += 1
        except Exception as exc:
            notify_bridge_failure(payload=payload, error=str(exc))
            raise

    return {"statusCode": 200, "body": json.dumps({"processed": processed})}
