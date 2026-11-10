#!/bin/bash
# Tabelas do domínio Pessoas no schema UBEREATS (F2 do modelo físico; ADR 006).
# Gerado a partir de shared/docs/modelagem/04-modelo-fisico.md (F2.1 e F2.2). Roda uma vez, no init
# do banco (/container-entrypoint-initdb.d, F5.1), depois do 01_create_user.sh. O usuário UBEREATS
# é criado pela imagem (APP_USER/APP_USER_PASSWORD do compose).
set -euo pipefail

sqlplus -s ubereats/"${ORACLE_APP_PASSWORD}"@FREEPDB1 <<'EOSQL'
WHENEVER SQLERROR EXIT SQL.SQLCODE
SET FEEDBACK OFF


CREATE TABLE cities (
  city_id     NUMBER(9)           NOT NULL,
  name        VARCHAR2(100 CHAR)  NOT NULL,
  state_code  CHAR(2 CHAR)        NOT NULL,
  created_at  TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  updated_at  TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  CONSTRAINT pk_cities PRIMARY KEY (city_id),
  CONSTRAINT ck_cities_city_id CHECK (city_id BETWEEN 1000000 AND 5999999),
  CONSTRAINT ck_cities_state_code CHECK (REGEXP_LIKE(state_code, '^[A-Z]{2}$'))
);

CREATE TABLE customers (
  customer_id     NUMBER(18)          NOT NULL,
  first_name      VARCHAR2(60 CHAR)   NOT NULL,
  last_name       VARCHAR2(80 CHAR)   NOT NULL,
  email           VARCHAR2(150 CHAR)  NOT NULL,
  email_verified  NUMBER(1)           NOT NULL,
  phone_number    VARCHAR2(20 CHAR)   NOT NULL,
  phone_verified  NUMBER(1)           NOT NULL,
  address_line1   VARCHAR2(200 CHAR)  NOT NULL,
  address_line2   VARCHAR2(100 CHAR),
  postal_code     CHAR(8 CHAR)        NOT NULL,
  latitude        NUMBER(9,6)         NOT NULL,
  longitude       NUMBER(9,6)         NOT NULL,
  city_id         NUMBER(9)           NOT NULL,
  date_of_birth   DATE                NOT NULL,
  gender          VARCHAR2(20 CHAR)   NOT NULL,
  status          VARCHAR2(20 CHAR)   NOT NULL,
  signup_date     TIMESTAMP           NOT NULL,
  last_login      TIMESTAMP           NOT NULL,
  created_at      TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  updated_at      TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  CONSTRAINT pk_customers PRIMARY KEY (customer_id),
  CONSTRAINT uq_customers_email UNIQUE (email),
  CONSTRAINT ck_customers_flags CHECK (email_verified IN (0, 1) AND phone_verified IN (0, 1)),
  CONSTRAINT ck_customers_postal_code CHECK (REGEXP_LIKE(postal_code, '^[0-9]{8}$')),
  CONSTRAINT ck_customers_coords CHECK (latitude BETWEEN -90 AND 90 AND longitude BETWEEN -180 AND 180),
  CONSTRAINT ck_customers_birth CHECK (date_of_birth = TRUNC(date_of_birth)),
  CONSTRAINT ck_customers_gender CHECK (gender IN ('female', 'male', 'other', 'not_informed')),
  CONSTRAINT ck_customers_status CHECK (status IN ('active', 'suspended', 'inactive')),
  CONSTRAINT ck_customers_login CHECK (last_login >= signup_date)
);

CREATE TABLE drivers (
  driver_id          NUMBER(18)          NOT NULL,
  first_name         VARCHAR2(60 CHAR)   NOT NULL,
  last_name          VARCHAR2(80 CHAR)   NOT NULL,
  email              VARCHAR2(150 CHAR)  NOT NULL,
  phone_number       VARCHAR2(20 CHAR)   NOT NULL,
  vehicle_type       VARCHAR2(20 CHAR)   NOT NULL,
  vehicle_make       VARCHAR2(50 CHAR)   NOT NULL,
  vehicle_model      VARCHAR2(50 CHAR)   NOT NULL,
  vehicle_year       NUMBER(9)           NOT NULL,
  license_plate      CHAR(7 CHAR)        NOT NULL,
  license_number     CHAR(11 CHAR)       NOT NULL,
  city_id            NUMBER(9)           NOT NULL,
  status             VARCHAR2(20 CHAR)   NOT NULL,
  registration_date  TIMESTAMP           NOT NULL,
  last_login         TIMESTAMP           NOT NULL,
  created_at         TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  updated_at         TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  CONSTRAINT pk_drivers PRIMARY KEY (driver_id),
  CONSTRAINT uq_drivers_license_plate UNIQUE (license_plate),
  CONSTRAINT uq_drivers_license_number UNIQUE (license_number),
  CONSTRAINT ck_drivers_vehicle_type CHECK (vehicle_type IN ('car', 'motorcycle', 'scooter')),
  CONSTRAINT ck_drivers_vehicle_year CHECK (vehicle_year BETWEEN 1990 AND 2100),
  CONSTRAINT ck_drivers_license_plate CHECK (REGEXP_LIKE(license_plate, '^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$')),
  CONSTRAINT ck_drivers_license_number CHECK (REGEXP_LIKE(license_number, '^[0-9]{11}$')),
  CONSTRAINT ck_drivers_status CHECK (status IN ('active', 'suspended', 'inactive')),
  CONSTRAINT ck_drivers_login CHECK (last_login >= registration_date)
);

CREATE INDEX ix_drivers_city_status ON drivers (city_id, status);

CREATE OR REPLACE TRIGGER trg_cities_updated_at
  BEFORE UPDATE ON cities FOR EACH ROW
BEGIN
  IF :NEW.updated_at = :OLD.updated_at THEN
    :NEW.updated_at := CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP);
  END IF;
END;
/

CREATE OR REPLACE TRIGGER trg_customers_updated_at
  BEFORE UPDATE ON customers FOR EACH ROW
BEGIN
  IF :NEW.updated_at = :OLD.updated_at THEN
    :NEW.updated_at := CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP);
  END IF;
END;
/

CREATE OR REPLACE TRIGGER trg_drivers_updated_at
  BEFORE UPDATE ON drivers FOR EACH ROW
BEGIN
  IF :NEW.updated_at = :OLD.updated_at THEN
    :NEW.updated_at := CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP);
  END IF;
END;
/

CREATE OR REPLACE TRIGGER trg_ubereats_logon
  AFTER LOGON ON ubereats.SCHEMA
BEGIN
  EXECUTE IMMEDIATE q'[ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD']';
  EXECUTE IMMEDIATE q'[ALTER SESSION SET NLS_TIMESTAMP_FORMAT = 'YYYY-MM-DD HH24:MI:SS.FF']';
  EXECUTE IMMEDIATE q'[ALTER SESSION SET TIME_ZONE = 'America/Sao_Paulo']';
END;
/

EXIT;
EOSQL
