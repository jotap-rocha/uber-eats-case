"""Cache em memória com TTL da cópia do MongoDB no S3/Bronze (Decisão 4,
DESIGN_INGESTAO_AWS_FASE2.md).

O MongoDB é estático (satélite "Perfil de Restaurante", sem CDC — decisão da
Onda 3), então o consumidor do Kappa não precisa reler o S3 a cada evento: carrega
uma vez por cold start / a cada CACHE_TTL_SECONDS, evitando o custo de um serviço
de cache dedicado (ex. DynamoDB) para uma tabela de referência pequena (~500 docs).
"""
from __future__ import annotations

import json
import time
from typing import Any

import boto3

CACHE_TTL_SECONDS = 300
MONGO_PREFIX = "mongodb/perfil_restaurante/"


class RestaurantProfileCache:
    """Cache de "Perfil de Restaurante" (menu + horários) por `restaurant_id`."""

    def __init__(self, s3_client=None, bucket: str = "", ttl_seconds: int = CACHE_TTL_SECONDS):
        self._s3 = s3_client or boto3.client("s3")
        self._bucket = bucket
        self._ttl_seconds = ttl_seconds
        self._data: dict[Any, dict] | None = None
        self._loaded_at: float = 0.0

    def _is_stale(self) -> bool:
        return self._data is None or (time.time() - self._loaded_at) >= self._ttl_seconds

    def _load(self) -> dict[Any, dict]:
        response = self._s3.list_objects_v2(Bucket=self._bucket, Prefix=MONGO_PREFIX)
        profiles: dict[Any, dict] = {}
        for obj in response.get("Contents", []):
            body = self._s3.get_object(Bucket=self._bucket, Key=obj["Key"])["Body"].read()
            for doc in json.loads(body):
                profiles[doc["restaurant_id"]] = doc
        return profiles

    def get(self, restaurant_id) -> dict | None:
        if self._is_stale():
            self._data = self._load()
            self._loaded_at = time.time()
        return self._data.get(restaurant_id)
