#!/bin/bash
# Cria as tabelas de Pedido, Pagamento, Item de Pedido e Recibo no schema
# UBEREATS (Etapa 3 da Onda 3). order_id/payment_id migram de UUID para
# NUMBER sequencial (mesma convencao ja usada em restaurant_id/product_id
# desde as Ondas 1/2). Sem FK (mesmo motivo documentado em
# 02_create_tables.sh: lookup do ShadowTraffic e logico, nao sincronizado
# fisicamente entre conexoes/tabelas). Datas como VARCHAR2 (ORA-01843,
# mesmo motivo de 02_create_tables.sh). "timestamp" e palavra reservada no
# Oracle -- campo do pagamento chama-se txn_timestamp.
set -e

sqlplus -s ubereats/"${ORACLE_APP_PASSWORD}"@FREEPDB1 <<'EOSQL'

CREATE TABLE orders (
    order_id          NUMBER(10)     PRIMARY KEY,
    user_id           NUMBER(10),
    restaurant_id     NUMBER(10),
    driver_id         NUMBER(10),
    order_date        VARCHAR2(30),
    total_amount      NUMBER(18, 2),
    status            VARCHAR2(30),
    updated_at        VARCHAR2(30)
);
ALTER TABLE orders ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

CREATE TABLE payments (
    payment_id        NUMBER(10)     PRIMARY KEY,
    order_id          NUMBER(10),
    amount            NUMBER(18, 2),
    currency          VARCHAR2(5),
    method            VARCHAR2(20),
    provider          VARCHAR2(20),
    card_brand        VARCHAR2(20),
    card_last4        VARCHAR2(4),
    card_exp_month    NUMBER(2),
    card_exp_year     NUMBER(4),
    wallet_provider   VARCHAR2(20),
    status            VARCHAR2(20),
    failure_reason    VARCHAR2(50),
    refunded          NUMBER(1),
    refund_amount     NUMBER(18, 2),
    captured          NUMBER(1),
    capture_timestamp VARCHAR2(30),
    platform_fee      NUMBER(18, 2),
    provider_fee      NUMBER(18, 2),
    tax_amount        NUMBER(18, 2),
    net_amount        NUMBER(18, 2),
    receipt_url       VARCHAR2(200),
    invoice_id        VARCHAR2(30),
    country           VARCHAR2(5),
    ip_address        VARCHAR2(20),
    user_agent        VARCHAR2(200),
    txn_timestamp     VARCHAR2(30)
);
ALTER TABLE payments ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

CREATE TABLE order_items (
    order_item_id     VARCHAR2(36)   PRIMARY KEY,
    order_id          NUMBER(10),
    restaurant_id     NUMBER(10),
    product_id        VARCHAR2(20),
    product_name      VARCHAR2(200),
    product_type      VARCHAR2(20),
    cuisine_type      VARCHAR2(50),
    is_vegetarian     NUMBER(1),
    is_combo          NUMBER(1),
    modifiers         VARCHAR2(100),
    quantity          NUMBER(5),
    unit_price        NUMBER(18, 2),
    discount_applied  NUMBER(18, 2),
    subtotal          NUMBER(18, 2)
);
ALTER TABLE order_items ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

CREATE TABLE receipts (
    receipt_id            VARCHAR2(36) PRIMARY KEY,
    order_id              NUMBER(10),
    payment_id            NUMBER(10),
    total_amount          NUMBER(18, 2),
    item_count            NUMBER(5),
    receipt_generated_at  VARCHAR2(30)
);
ALTER TABLE receipts ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

EXIT;
EOSQL
