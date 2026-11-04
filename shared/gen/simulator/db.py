"""Conexões com as três fontes, a partir do shared/gen/.env (F5.2).

O .env aponta os hosts pelos nomes dos contêineres (é o que o ShadowTraffic usa dentro do compose).
O seed e o simulador rodam no Windows (F5.2), então o host padrão é 127.0.0.1 (não "localhost": no
Windows ele resolve primeiro para ::1, e a porta publicada só em IPv4 deixa a conexão pendurada); SIMULATOR_<FONTE>_HOST
e SIMULATOR_<FONTE>_PORT mudam isso sem tocar no .env. Nenhuma senha é registrada em log.
"""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

from simulator.params import REPO_ROOT

if TYPE_CHECKING:
    import oracledb
    import psycopg
    import pymongo

DEFAULT_ENV = REPO_ROOT / "shared" / "gen" / ".env"
TIME_ZONE = "America/Sao_Paulo"  # F0, decisão 3


def read_env_file(path: Path) -> dict[str, str]:
    """KEY=VALUE por linha, como o setup-configs.ps1 lê; ignora comentário e linha sem '='."""
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


@dataclass(frozen=True)
class Settings:
    env: Mapping[str, str] = field(repr=False)  # tem senhas: fora do repr e de qualquer log

    @classmethod
    def load(cls, path: Path = DEFAULT_ENV) -> Settings:
        return cls({**read_env_file(path), **os.environ})

    def _get(self, key: str) -> str:
        value = self.env.get(key)
        if not value:
            raise KeyError(f"{key} ausente no shared/gen/.env e no ambiente")
        return value

    def _host_port(self, source: str, default_port_key: str) -> tuple[str, int]:
        host = self.env.get(f"SIMULATOR_{source}_HOST", "127.0.0.1")
        port = self.env.get(f"SIMULATOR_{source}_PORT") or self._get(default_port_key)
        return host, int(port)

    def postgres_conninfo(self) -> dict[str, Any]:  # Any: kwargs do psycopg.connect
        host, port = self._host_port("POSTGRES", "POSTGRES_PORT")
        return {
            "host": host,
            "port": port,
            "dbname": self._get("POSTGRES_DB"),
            "user": self._get("POSTGRES_USERNAME"),
            "password": self._get("POSTGRES_PASSWORD"),
            "options": f"-c timezone={TIME_ZONE} -c search_path=ubereats",
            "connect_timeout": 10,
        }

    def oracle_conninfo(self) -> dict[str, Any]:  # Any: kwargs do oracledb.connect
        host, port = self._host_port("ORACLE", "ORACLE_PORT")
        return {
            "user": self._get("ORACLE_APP_USERNAME"),
            "password": self._get("ORACLE_APP_PASSWORD"),
            "dsn": f"{host}:{port}/{self._get('ORACLE_SERVICE')}",
            "tcp_connect_timeout": 10,
        }

    def mongo_uri(self) -> str:
        host, port = self._host_port("MONGO", "MONGO_PORT")
        return f"mongodb://{host}:{port}/?directConnection=true"  # F4.4


def connect_postgres(settings: Settings) -> psycopg.Connection[tuple[Any, ...]]:
    import psycopg

    # autocommit: cada escrita abre a própria transação (conn.transaction()), uma por unidade de negócio.
    return psycopg.connect(**settings.postgres_conninfo(), autocommit=True)


def connect_oracle(settings: Settings) -> oracledb.Connection:
    import oracledb

    # O gatilho de logon do schema fixa NLS ISO e o fuso de Brasília (F2.1).
    return oracledb.connect(**settings.oracle_conninfo())


def connect_mongo(settings: Settings) -> pymongo.MongoClient[dict[str, Any]]:
    import pymongo

    return pymongo.MongoClient(settings.mongo_uri(), tz_aware=True, serverSelectionTimeoutMS=10000)
