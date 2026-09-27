"""Testes de contrato da Fase 1/Azure (item 30 do manifesto de
DESIGN_INGESTAO_AZURE_FASE1.md).

Valida que:
1. O mapeamento canonico de CDC (docs/data-contract-cdc-azure.md) extrai
   corretamente as 4 colunas a partir de um registro Airbyte (Postgres) e de
   um envelope Debezium (Oracle) -- mesmos campos que o Kafka Connect Sink
   Connector (debezium/adls-sink-connector.json.template) precisa preservar
   ao gravar no ADLS.
2. Os templates JSON dos conectores Kafka Connect (source Oracle e sink ADLS)
   sao JSON valido e tem as chaves de configuracao esperadas pelo DESIGN.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MAPPING_MODULE_PATH = REPO_ROOT / "src" / "azure" / "cdc_contract" / "mapping.py"


def _load_mapping_module():
    spec = importlib.util.spec_from_file_location("azure_cdc_mapping", MAPPING_MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


mapping = _load_mapping_module()


def test_map_postgres_record_update():
    record = {
        "driver_id": 42,
        "_ab_cdc_deleted_at": None,
        "_ab_cdc_updated_at": "2026-09-12T10:00:00Z",
        "_ab_cdc_lsn": "0/1A2B3C4",
    }

    result = mapping.map_postgres_record(record)

    assert result["cdc_operation"] == "u"
    assert result["cdc_commit_ts"] == "2026-09-12T10:00:00Z"
    assert result["cdc_sequence"] == "0/1A2B3C4"
    assert result["cdc_source_system"] == "postgres-ubereats"


def test_map_postgres_record_delete():
    record = {
        "driver_id": 42,
        "_ab_cdc_deleted_at": "2026-09-12T11:00:00Z",
        "_ab_cdc_updated_at": "2026-09-12T11:00:00Z",
        "_ab_cdc_lsn": "0/1A2B3C5",
    }

    result = mapping.map_postgres_record(record)

    assert result["cdc_operation"] == "d"


def test_map_oracle_record():
    payload = {
        "op": "u",
        "after": {"ORDER_ID": 1, "STATUS": "DELIVERED"},
        "source": {"ts_ms": 1757670000000, "scn": "123456789"},
    }

    result = mapping.map_oracle_record(payload)

    assert result["cdc_operation"] == "u"
    assert result["cdc_commit_ts"] == 1757670000000
    assert result["cdc_sequence"] == "123456789"
    assert result["cdc_source_system"] == "oracle-ubereats"


def test_canonical_fields_constant_matches_mapping_output():
    postgres_result = mapping.map_postgres_record(
        {"_ab_cdc_deleted_at": None, "_ab_cdc_updated_at": None, "_ab_cdc_lsn": None}
    )
    assert set(mapping.CANONICAL_FIELDS) == set(postgres_result.keys())


def test_oracle_connector_azure_template_is_valid_json_with_expected_keys():
    template_path = REPO_ROOT / "debezium" / "oracle-connector-azure.json.template"
    config = json.loads(template_path.read_text(encoding="utf-8"))["config"]

    assert config["connector.class"] == "io.debezium.connector.oracle.OracleConnector"
    assert "REPLACE_EVENTHUB_NAMESPACE" in config["schema.history.internal.kafka.bootstrap.servers"]
    assert config["schema.history.internal.producer.security.protocol"] == "SASL_SSL"


def test_adls_sink_connector_template_is_valid_json_with_expected_keys():
    template_path = REPO_ROOT / "debezium" / "adls-sink-connector.json.template"
    config = json.loads(template_path.read_text(encoding="utf-8"))["config"]

    assert config["connector.class"] == "io.confluent.connect.hdfs.HdfsSinkConnector"
    assert config["store.url"].startswith("abfss://bronze@")
    topics = config["topics"].split(",")
    assert "postgres.public.drivers" in topics
    assert "oracle.UBEREATS.ORDERS" in topics
