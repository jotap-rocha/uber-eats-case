"""Alerta Teams para falha da ponte MinIO->Kinesis (mandato SHOULD, TM-M01 do DEFINE).

A ponte é o único componente customizado do desenho de ingestão da Fase 2 (todo
o resto é conector gerenciado: DMS, DataSync) — maior risco de falha silenciosa,
por isso o alerta é recomendado mesmo sem SLA de produção 24/7.
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
            "**Falha na ponte MinIO -> Kinesis**\n\n"
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
