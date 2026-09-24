"""Alerta Teams para falha da ponte MinIO->Pub/Sub (mandato SHOULD, TM-M01 do DEFINE).

A ponte é o único componente customizado do desenho de ingestão da Fase 3
(todo o resto é conector gerenciado: Datastream, Storage Transfer Service,
Debezium Server) - maior risco de falha silenciosa, por isso o alerta é
recomendado mesmo sem SLA de produção 24/7. Mesmo padrão já usado na Fase 2/AWS.
"""
from __future__ import annotations

import json
import os
import urllib.request

TEAMS_WEBHOOK_URL = os.environ.get("TEAMS_WEBHOOK_URL", "")


def notify_bridge_failure(payload: dict, error: str) -> None:
    if not TEAMS_WEBHOOK_URL:
        return

    card = {
        "text": (
            "**Falha na ponte MinIO -> Pub/Sub**\n\n"
            f"- Bucket/key: `{payload.get('bucket')}/{payload.get('key')}`\n"
            f"- Erro: `{error}`"
        )
    }

    request = urllib.request.Request(
        TEAMS_WEBHOOK_URL,
        data=json.dumps(card).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    urllib.request.urlopen(request, timeout=5)
