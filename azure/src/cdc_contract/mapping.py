"""Mapeamento do contrato canonico de CDC para a Fase 1/Azure.

Documenta em codigo o mesmo mapeamento descrito em docs/data-contract-cdc-azure.md
-- Postgres (Airbyte) e Oracle (Debezium), sem nenhum campo novo em relacao a
Onda 3. Usado para validar (via teste) que o Kafka Connect Sink Connector
(debezium/adls-sink-connector.json.template) preserva os campos necessarios
ao gravar no ADLS.
"""

from __future__ import annotations

from typing import Any


def map_postgres_record(record: dict[str, Any]) -> dict[str, Any]:
    """Extrai as 4 colunas canonicas de um registro Airbyte (Postgres CDC)."""
    deleted_at = record.get("_ab_cdc_deleted_at")
    return {
        "cdc_operation": "d" if deleted_at is not None else "u",
        "cdc_commit_ts": record.get("_ab_cdc_updated_at"),
        "cdc_sequence": record.get("_ab_cdc_lsn"),
        "cdc_source_system": "postgres-ubereats",
    }


def map_oracle_record(payload: dict[str, Any]) -> dict[str, Any]:
    """Extrai as 4 colunas canonicas de um envelope Debezium (Oracle CDC)."""
    source = payload.get("source", {})
    return {
        "cdc_operation": payload.get("op"),
        "cdc_commit_ts": source.get("ts_ms"),
        "cdc_sequence": source.get("scn"),
        "cdc_source_system": "oracle-ubereats",
    }


CANONICAL_FIELDS = ("cdc_operation", "cdc_commit_ts", "cdc_sequence", "cdc_source_system")
