# DESIGN: Unificação de Identidade Postgres×MinIO (Onda 2)

| Campo | Valor |
|-------|-------|
| **Feature** | UNIFICACAO_IDENTIDADE_POSTGRES_MINIO |
| **Input** | `.claude/sdd/features/DEFINE_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md` |
| **Status** | ✅ Shipped |
| **Data** | 2026-08-24 |

---

## Architecture Overview

```text
┌────────────────────────────────────────────────────────────────────────────────┐
│                    ANTES (3 processos independentes)                           │
├────────────────────────────────────────────────────────────────────────────────┤
│  gen-users ──► Postgres.users (UUID)      gen-drivers ──► Postgres.drivers     │
│  gen-minio ──► MinIO (20 streams, incl. mssql/users, mongodb/users,            │
│                postgres/drivers — cópias desconectadas)                        │
└────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────┐
│                    DEPOIS (1 processo unificado)                               │
├────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│   gen-unified (1 container, 1 config: gen/unified/uber-eats.json)              │
│     connections: { postgres, minio }                                           │
│                                                                                  │
│     ├─ users   (connection: postgres) ── user_id INT sequencial               │
│     ├─ drivers (connection: postgres) ── driver_id INT sequencial             │
│     │           + vehicle_make/model/year, license_number, city (novos)        │
│     │                                                                           │
│     └─ 17 streams MinIO (connection: minio)                                    │
│          kafka/orders.user_key    ──lookup──► postgres.users.user_id           │
│          kafka/orders.driver_key  ──lookup──► postgres.drivers.driver_id       │
│          mongodb/support.user_id  ──lookup──► postgres.users.user_id           │
│          kafka/shift.driver_id/city ──lookup──► postgres.drivers               │
│          kafka/route.driver_id    ──lookup──► postgres.drivers.driver_id       │
│          kafka/route.end_lat/lon  ──lookup──► postgres.users.lat/lon           │
│                                                                                  │
│   (mssql/users, mongodb/users, postgres/drivers — REMOVIDOS)                   │
│                                                                                  │
└────────────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
   Bronze (ods_postgres_users, ods_postgres_drivers — sem mudança de script,
           CDC/SELECT * já propaga colunas novas automaticamente)
                    │
                    ▼
   Silver — 2 scripts de motorista viram 1 (`silver_drivers`); `ingestion_kafka_orders.sql`
           renomeia coluna; demais streams sem mudança estrutural (só o dado muda)
                    │
                    ▼
   Gold — sem mudança (nenhum script atual referenciava as tabelas de motorista)
                    │
                    ▼
   Validação: regenerar + join real no Gold, 8 acceptance tests
                    │
                    ▼
   docs/MODELO_CONCEITUAL_UBER_EATS.md — zero pendências
```

---

## Decisões de Arquitetura (ADRs inline)

### Decisão: Sintaxe de lookup difere por tipo de conexão

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** A documentação oficial do ShadowTraffic mostra que lookups em conexões Postgres usam `"table"` + `path: ["row", campo]`, enquanto lookups em conexões de objeto (MinIO/S3) usam `"bucket"` + `"keyPrefix"` + `path: ["data", campo]`. Todo generator precisa declarar `"connection": "postgres"` ou `"connection": "minio"` explicitamente, já que o config unificado tem mais de uma conexão.

**Escolha:** Seguir exatamente a sintaxe da documentação oficial para cada tipo.

**Consequências:** Todo lookup cruzado (de MinIO para Postgres) muda de forma (`bucket/keyPrefix/path:["data",...]` → `connection/table/path:["row",...]`), não é só trocar o `keyPrefix`.

---

### Decisão: Adicionar `vehicle_make`, `vehicle_model`, `vehicle_year`, `license_number`, `city` ao Postgres real de Motorista

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** `sql/create_drivers_table.sql` não tinha esses campos — só existiam no stream MinIO simulado que está sendo aposentado. `kafka/shift.city`/`region` também dependia do stream aposentado.

**Escolha:** Adicionar os 5 campos à tabela real (`city` novo; `region` não vira coluna — passa a ser constante `"BR"`, mesmo padrão já usado em todas as outras entidades do domínio, já que o projeto é 100% Brasil).

**Racional:** Confirmado com o usuário — preferência por não perder atributos que já existiam, mesmo que isso exija mais uma migração de schema.

**Alternativas Rejeitadas:**
1. Aceitar a perda dos atributos — rejeitada pelo usuário.
2. Adicionar também uma coluna `country`/`region` — desnecessário, todo o domínio já usa `"BR"` fixo.

---

### Decisão: Reconciliar `silver_drivers_profile` + `silver_drivers_performance` em `silver_drivers`

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** As duas tabelas existiam porque havia duas fontes Bronze desconectadas (`postgres_drivers`, do MinIO; `ods_postgres_drivers`, do Postgres real via CDC). Com a unificação, só `ods_postgres_drivers` continua existindo.

**Escolha:** Um único script `pipeline/silver/ingestion_postgres_drivers.sql` → tabela `silver.silver_drivers`, combinando todos os atributos (cadastrais + veículo + performance). Os dois scripts antigos são removidos.

**Consequências:** Qualquer consumidor futuro do Gold que precisar de dimensão de motorista usa uma única tabela, sem ambiguidade.

---

### Decisão: Remover os arquivos de configuração antigos, não manter como legado

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** `gen/postgres/users.json(.template)`, `gen/postgres/drivers.json(.template)` e `gen/minio/uber-eats.json` deixam de ser usados — substituídos por `gen/unified/uber-eats.json(.template)`.

**Escolha:** Remover os arquivos antigos (não deixar como código morto). O histórico Git preserva o conteúdo se for necessário consultar depois.

**Consequências:** `docker-compose.yml` e `gen/setup-configs.ps1` precisam apontar só para o novo caminho unificado.

---

## File Manifest

| # | Arquivo | Ação | Mudança | Agente |
|---|---------|------|---------|--------|
| 1 | `sql/create_users_table.sql` | Edit | `user_id uuid` → `user_id int` | `@databricks-data-engineer` |
| 2 | `sql/create_drivers_table.sql` | Edit | `driver_id uuid` → `driver_id int`; adiciona `vehicle_make`, `vehicle_model`, `vehicle_year`, `license_number`, `city` | `@databricks-data-engineer` |
| 3 | `gen/unified/uber-eats.json.template` | Create | Config unificado: `connections.postgres` + `connections.minio`; generators `users`/`drivers` (postgres) + 17 streams MinIO com `"connection": "minio"` e lookups cruzados atualizados | (direto) |
| 4 | `gen/postgres/users.json.template`, `drivers.json.template`, `gen/minio/uber-eats.json` | Delete | Substituídos pelo config unificado | (direto) |
| 5 | `gen/setup-configs.ps1` | Edit | Gera `gen/unified/uber-eats.json` a partir do novo template (mesma substituição de credenciais Postgres) | (direto) |
| 6 | `docker-compose.yml` | Edit | Remove `gen-drivers`, `gen-users`, `gen-minio`; adiciona `gen-unified` (depende de `postgres-ubereats` saudável + `minio-setup` concluído) | (direto) |
| 7 | `pipeline/silver/ingestion_kafka_orders.sql` | Edit | Renomeia `cpf_usuario` → `id_usuario` (reflete que agora é o ID real, não CPF) | `@databricks-data-engineer` |
| 8 | `pipeline/silver/ingestion_postgres_drivers.sql` | Create | Substitui os 2 scripts abaixo — tabela única `silver_drivers` | `@databricks-pipeline-architect` |
| 9 | `pipeline/silver/ingestion_postgres_profile.sql`, `ingestion_ods_postgres_performance.sql` | Delete | Reconciliados no novo script único | (direto) |
| 10 | `docs/MODELO_CONCEITUAL_UBER_EATS.md` | Edit | Zero pendências de Onda 2 | (direto) |

**Sem alteração** (confirmado no Design): `pipeline/bronze/ingest_postgres_users.sql`, `ingest_postgres_drivers.sql` (CDC `SELECT *` já propaga colunas novas automaticamente); `pipeline/silver/ingestion_postgres_users.sql` (já expõe `id_usuario`, `lat`, `lon`); `pipeline/silver/ingestion_kafka_route.sql` (já trata `end_lat/lon` genericamente); scripts Gold (nenhum referenciava dimensão de motorista).

---

## Content Patterns

### `gen/unified/uber-eats.json.template` — esqueleto

```jsonc
{
  "generators": [
    {
      "name": "users",
      "connection": "postgres",
      "table": "users",
      "row": { /* mesmo conteúdo de users.json.template, com user_id: sequentialInteger */ }
    },
    {
      "name": "drivers",
      "connection": "postgres",
      "table": "drivers",
      "row": {
        "driver_id": { "_gen": "sequentialInteger", "startingFrom": 1 },
        /* ...campos existentes... */
        "vehicle_make": { "_gen": "string", "expr": "#{Company.name}" },
        "vehicle_model": { "_gen": "string", "expr": "#{Commerce.productName}" },
        "vehicle_year": { "_gen": "uniformDistribution", "bounds": [1980, 2024], "decimals": 0 },
        "license_number": { "_gen": "string", "expr": "#{bothify '??#######'}" },
        "city": { "_gen": "string", "expr": "#{Address.city}" }
      }
    },
    {
      "bucket": "uber-eats",
      "connection": "minio",
      "bucketConfigs": { "keyPrefix": "kafka/orders/", "format": "jsonl" },
      "data": {
        "user_key": {
          "_gen": "lookup", "connection": "postgres",
          "table": "users", "path": ["row", "user_id"]
        },
        "restaurant_key": { /* já corrigido na Onda 1, sem mudança */ },
        "driver_key": {
          "_gen": "lookup", "connection": "postgres",
          "table": "drivers", "path": ["row", "driver_id"]
        }
        /* ...demais campos sem mudança... */
      }
    }
    /* ...demais 16 streams MinIO, cada um com "connection": "minio" adicionado... */
  ],
  "connections": {
    "postgres": {
      "kind": "postgres",
      "connectionConfigs": {
        "host": "REPLACE_POSTGRES_HOST", "port": REPLACE_POSTGRES_PORT,
        "db": "REPLACE_POSTGRES_DB", "username": "REPLACE_POSTGRES_USER",
        "password": "REPLACE_POSTGRES_PASSWORD", "sslmode": "disable"
      }
    },
    "minio": {
      "kind": "s3",
      "connectionConfigs": { "endpoint": "http://minio-ubereats:9000", "pathStyleAccess": true }
    }
  }
}
```

### `mongodb/support.user_id`, `kafka/shift.driver_id`/`city`, `kafka/route.driver_id`/`end_lat`/`end_lon` — mesmo padrão de lookup cruzado

```jsonc
"user_id":   { "_gen": "lookup", "connection": "postgres", "table": "users",   "path": ["row", "user_id"] },
"driver_id": { "_gen": "lookup", "connection": "postgres", "table": "drivers", "path": ["row", "driver_id"] },
"city":      { "_gen": "lookup", "connection": "postgres", "table": "drivers", "path": ["row", "city"] },
"region":    { "_gen": "oneOf", "choices": ["BR"] },
"end_lat":   { "_gen": "lookup", "connection": "postgres", "table": "users", "path": ["row", "lat"] },
"end_lon":   { "_gen": "lookup", "connection": "postgres", "table": "users", "path": ["row", "lon"] }
```

### `sql/create_users_table.sql` / `create_drivers_table.sql`

```sql
-- users: trocar
user_id           uuid PRIMARY KEY,
-- por
user_id           int PRIMARY KEY,
```

```sql
-- drivers: trocar
driver_id           uuid PRIMARY KEY,
-- por
driver_id           int PRIMARY KEY,
-- e adicionar antes do fechamento:
    vehicle_make      text,
    vehicle_model     text,
    vehicle_year      int,
    license_number    text,
    city              text
```

### `docker-compose.yml` — novo serviço único

```yaml
  gen-unified:
    image: shadowtraffic/shadowtraffic:latest
    container_name: gen-unified
    depends_on:
      postgres-ubereats:
        condition: service_healthy
      minio-setup:
        condition: service_completed_successfully
    volumes:
      - ./gen/unified/uber-eats.json:/home/config.json:ro
    env_file: ./gen/.env
    command: --config /home/config.json
```

### `pipeline/silver/ingestion_postgres_drivers.sql` (novo, reconciliado)

```sql
CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_drivers
COMMENT "Dimensão única de motorista — cadastro, veículo e performance, fonte Postgres real."
AS
WITH bronze_table AS (
  SELECT * FROM STREAM(live.ods_postgres_drivers)
),
typed_table AS (
  SELECT
    CAST(driver_id AS STRING)          AS id_motorista,
    CAST(name AS STRING)               AS nome_completo,
    CAST(email AS STRING)              AS email,
    CAST(phone_number AS STRING)       AS telefone,
    CAST(vehicle_type AS STRING)       AS tipo_veiculo,
    CAST(vehicle_make AS STRING)       AS veiculo_fabricante,
    CAST(vehicle_model AS STRING)      AS veiculo_modelo,
    CAST(vehicle_year AS INT)          AS veiculo_ano,
    CAST(license_plate AS STRING)      AS placa_veiculo,
    CAST(license_number AS STRING)     AS numero_cnh,
    CAST(city AS STRING)               AS cidade,
    CAST(registration_date AS TIMESTAMP) AS data_registro,
    CAST(total_deliveries AS INT)      AS total_entregas,
    CAST(total_earnings AS DECIMAL(18, 2)) AS total_ganhos,
    CAST(average_rating AS DECIMAL(3, 1))  AS nota_media,
    CAST(last_login AS TIMESTAMP)      AS data_ultimo_login,
    CAST(status AS STRING)             AS status_conta
  FROM bronze_table
),
silver_table AS (
  SELECT *, current_timestamp() AS _data_ingestao, 'postgres-real' AS _sistema_fonte
  FROM typed_table
)
SELECT * FROM silver_table;
```

---

## Estratégia de Verificação

| ID | Verificação | Como checar | Cobre |
|----|--------------|--------------|-------|
| V-001 | Config unificado válido | `python -c "import json; json.load(open('gen/unified/uber-eats.json.template'))"` (ignorando placeholders `REPLACE_*` como strings) | Estrutural |
| V-002 | Arquivos antigos removidos | `ls gen/postgres/users.json.template gen/minio/uber-eats.json` → erro esperado | ADR remoção |
| V-003 | Docker compose só com 1 gerador | `grep -c "shadowtraffic/shadowtraffic" docker-compose.yml` → 1 | AT-001 |
| V-004 | Schema com PK int + campos novos | `grep "user_id.*int\|driver_id.*int\|vehicle_make\|city" sql/*.sql` | AT-002 |
| V-005 | Join pedido↔usuário/motorista sem órfãos | Rodar pipeline completo no Databricks, join por `id_usuario`/`id_motorista` | AT-003, AT-004 |
| V-006 | Streams aposentados | `grep -c "mssql/users\|mongodb/users\|postgres/drivers" gen/unified/uber-eats.json.template` → 0 | AT-005 |
| V-007 | Destino da Entrega | Comparar `end_lat/lon` de `silver_kafka_route` com `lat/lon` de `silver_postgres_users` | AT-006 |
| V-008 | Dimensão única de motorista | `silver_drivers` existe; `silver_drivers_profile`/`silver_drivers_performance` não existem mais | AT-007 |
| V-009 | Documentação sem pendência | Revisão manual de `docs/MODELO_CONCEITUAL_UBER_EATS.md` | AT-008 |

---

## Atualização de Status (após Build)

Ao concluir o BUILD, atualizar `DEFINE_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md` e este `DESIGN` para refletir o que foi de fato verificável nesta sessão (código/config) vs. o que exige execução manual (regeneração + validação Databricks), seguindo o mesmo padrão da Onda 1.

---

## Status: ⚠️ Complete (Built) — validação de integração pendente

**Próximo passo:** Regenerar dados (exige recriar volume Postgres) + validar joins no Databricks; depois `/ship`
