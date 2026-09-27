#!/bin/bash
# O usuario UBEREATS ja e criado automaticamente pela imagem gvenzl/oracle-free
# via as env vars APP_USER/APP_USER_PASSWORD (docker-compose.yml) -- nao criar
# de novo aqui, so garantir os grants extras que a app precisa.
#
# C##DBZUSER (usuario comum do Debezium, compartilhado entre todos os PDBs)
# so pode ser criado a partir do CDB$ROOT -- ORA-65050 se tentado dentro de
# um PDB (bug real encontrado testando este script: a sessao ainda estava
# em FREEPDB1 da etapa anterior).
set -e

sqlplus -s / as sysdba <<EOSQL
ALTER SESSION SET CONTAINER = FREEPDB1;

GRANT CONNECT, RESOURCE TO ubereats;
GRANT CREATE SESSION, CREATE TABLE, CREATE SEQUENCE TO ubereats;

ALTER SESSION SET CONTAINER = CDB\$ROOT;

CREATE USER c##dbzuser IDENTIFIED BY "${ORACLE_DBZ_PASSWORD}"
  DEFAULT TABLESPACE users
  QUOTA UNLIMITED ON users
  CONTAINER = ALL;

GRANT CREATE SESSION TO c##dbzuser CONTAINER = ALL;
GRANT SET CONTAINER TO c##dbzuser CONTAINER = ALL;
GRANT SELECT ON V_\$DATABASE TO c##dbzuser CONTAINER = ALL;
GRANT FLASHBACK ANY TABLE TO c##dbzuser CONTAINER = ALL;
GRANT SELECT ANY TABLE TO c##dbzuser CONTAINER = ALL;
GRANT SELECT_CATALOG_ROLE TO c##dbzuser CONTAINER = ALL;
GRANT EXECUTE_CATALOG_ROLE TO c##dbzuser CONTAINER = ALL;
GRANT SELECT ANY TRANSACTION TO c##dbzuser CONTAINER = ALL;
GRANT LOGMINING TO c##dbzuser CONTAINER = ALL;
GRANT CREATE TABLE TO c##dbzuser CONTAINER = ALL;
GRANT LOCK ANY TABLE TO c##dbzuser CONTAINER = ALL;
GRANT CREATE SEQUENCE TO c##dbzuser CONTAINER = ALL;
GRANT EXECUTE ON DBMS_LOGMNR TO c##dbzuser CONTAINER = ALL;
GRANT SELECT ANY DICTIONARY TO c##dbzuser CONTAINER = ALL;

EXIT;
EOSQL
