#!/bin/bash
# Cria as tabelas de Restaurante, Produto e Estoque no schema UBEREATS
# (Etapa 2 da Onda 3 -- insert-only por enquanto; mutacao real entra
# quando o mesmo padrao fork+stateMachine da Etapa 1 for aplicado aqui).
set -e

sqlplus -s ubereats/"${ORACLE_APP_PASSWORD}"@FREEPDB1 <<'EOSQL'

CREATE TABLE restaurants (
    restaurant_id     NUMBER(10)     PRIMARY KEY,
    uuid              VARCHAR2(36),
    name              VARCHAR2(200),
    address           VARCHAR2(400),
    city              VARCHAR2(100),
    country           VARCHAR2(5),
    phone_number      VARCHAR2(30),
    cuisine_type      VARCHAR2(50),
    opening_time      VARCHAR2(20),
    closing_time      VARCHAR2(20),
    average_rating    NUMBER(3, 1),
    num_reviews       NUMBER(10),
    cnpj              VARCHAR2(30),
    lat               NUMBER(10, 6),
    lon               NUMBER(10, 6)
);

CREATE TABLE products (
    product_id        VARCHAR2(20)   PRIMARY KEY,
    restaurant_id     NUMBER(10),
    name              VARCHAR2(200),
    tags              VARCHAR2(400),
    flavor_profile    VARCHAR2(100),
    cuisine_type      VARCHAR2(50),
    product_type      VARCHAR2(50),
    price             NUMBER(18, 2),
    unit_cost         NUMBER(18, 2),
    calories          NUMBER(10),
    prep_time_min     NUMBER(10),
    is_vegetarian     NUMBER(1),
    is_gluten_free    NUMBER(1),
    created_at        VARCHAR2(30), -- Data/Hora como TEXTO (mesmo padrao de sql/create_users_table.sql -- evita ORA-01843 na conversao implicita do ShadowTraffic)
    updated_at        VARCHAR2(30) -- Data/Hora como TEXTO
    -- Sem FK pra restaurant_id: mesmo padrao do resto do projeto (users/drivers
    -- tambem nao tem FK) -- integridade referencial e validada por join real
    -- no Gold (Ondas 1/2), nao por constraint. FK real causou ORA-02291 real
    -- testando este script: o ShadowTraffic faz lookup por valor JA GERADO
    -- (logico), mas a escrita cross-connection em conexoes/tabelas diferentes
    -- nao e sincronizada fisicamente -- o commit do pai pode nao ter
    -- acontecido ainda quando o filho tenta inserir.
);

CREATE TABLE inventory (
    stock_id          VARCHAR2(36)   PRIMARY KEY,
    restaurant_id     NUMBER(10),
    product_id        VARCHAR2(20),
    quantity_available NUMBER(10),
    last_updated      VARCHAR2(30) -- Data/Hora como TEXTO
    -- Sem FK -- mesmo motivo do comentario em products acima.
);

-- Supplemental logging por tabela, granularidade de coluna-chave --
-- redundante com o ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS de 00_enable_archivelog.sql,
-- mas documentado aqui por clareza (algumas versoes do Debezium preferem log a nivel de tabela).
ALTER TABLE restaurants ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
ALTER TABLE products ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
ALTER TABLE inventory ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

EXIT;
EOSQL
