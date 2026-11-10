#!/bin/bash
# Usuário e publicação do CDC (F4.2 do modelo físico). Roda uma vez, no init do volume, como o
# dono das tabelas (POSTGRES_USER). A senha vem do shared/gen/.env (env_file do compose); o
# usuário é fixo no template do conector (config/shared/debezium/postgres-connector.json.template).
# Sem "set": a imagem pode dar "source" no script; o ":?" e o ON_ERROR_STOP já param o init.

: "${POSTGRES_DEBEZIUM_PASSWORD:?POSTGRES_DEBEZIUM_PASSWORD ausente no shared/gen/.env}"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" \
     -v dbz_password="$POSTGRES_DEBEZIUM_PASSWORD" <<'EOSQL'
-- Usuário só do CDC: replicação + leitura para o snapshot.
CREATE ROLE dbz_ubereats WITH LOGIN REPLICATION PASSWORD :'dbz_password';
GRANT USAGE ON SCHEMA ubereats TO dbz_ubereats;
GRANT SELECT ON ALL TABLES IN SCHEMA ubereats TO dbz_ubereats;
ALTER DEFAULT PRIVILEGES IN SCHEMA ubereats GRANT SELECT ON TABLES TO dbz_ubereats;

-- Publicação do schema inteiro (Postgres 15+): tabela nova do schema entra sozinha.
CREATE PUBLICATION dbz_ubereats FOR TABLES IN SCHEMA ubereats;
EOSQL
