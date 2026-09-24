"""Lookup do 'Perfil de Restaurante' na tabela Iceberg do BigLake (Decisão 6,
DESIGN_INGESTAO_GCP_FASE3.md).

O MongoDB é estático (satélite "Perfil de Restaurante", sem CDC - decisão da
Onda 3), então o consumidor do Kappa não precisa reler a fonte a cada evento:
carrega periodicamente (side input do Beam), com o mesmo papel do
cache-com-TTL da Lambda consumidora da AWS (RestaurantProfileCache).
"""
from __future__ import annotations

from typing import Any

TABLE_FQN = "biglake_iceberg.perfil_restaurante"


def load_restaurant_profiles(bigquery_client=None) -> dict[Any, dict]:
    """Carrega todos os perfis de restaurante da tabela Iceberg do BigLake.

    `bigquery_client` é injetável para permitir teste sem credenciais reais do
    GCP - se omitido, cria um `google.cloud.bigquery.Client()` real.
    """
    if bigquery_client is None:
        from google.cloud import bigquery

        bigquery_client = bigquery.Client()

    query = f"SELECT restaurant_id, menu, horarios FROM `{TABLE_FQN}`"
    rows = bigquery_client.query(query).result()
    return {row["restaurant_id"]: dict(row) for row in rows}
