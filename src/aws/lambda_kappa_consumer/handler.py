"""Consumidor do Kappa (Decisão 3, DESIGN_INGESTAO_AWS_FASE2.md).

Lê eventos do Kinesis via event source mapping (invocação automática por lote) e
enriquece eventos de Pedido com o "Perfil de Restaurante" (menu + horários),
lido da cópia estática do MongoDB já aterrissada no S3/Bronze pelo trilho batch
(Etapa 1) — o MongoDB nunca entra pelo Kinesis (Decisão do DEFINE/brainstorm).
"""
from __future__ import annotations

import base64
import json
import os

from mongo_lookup import RestaurantProfileCache

BRONZE_BUCKET = os.environ["BRONZE_BUCKET"]

_cache = RestaurantProfileCache(bucket=BRONZE_BUCKET)


def _decode_record(record: dict) -> dict:
    raw = base64.b64decode(record["kinesis"]["data"])
    return json.loads(raw)


def _enrich(payload: dict) -> dict:
    restaurant_id = payload.get("restaurant_id")
    if restaurant_id is not None:
        profile = _cache.get(restaurant_id)
        if profile is not None:
            payload["restaurant_profile"] = profile
    return payload


def handler(event: dict, context) -> dict:
    enriched = [_enrich(_decode_record(record)) for record in event["Records"]]

    # Destino final (novo stream, Firehose, log estruturado) — detalhar no /build
    # seguinte, quando o formato de consumo downstream do Kappa for definido.
    return {"processed": len(enriched)}
