# PostgreSQL - Documentacao Tecnica

PostgreSQL 15 configurado como banco OLTP para dados transacionais (drivers e users).

---

## Especificacoes Tecnicas

| Item | Valor |
|------|-------|
| **Imagem Docker** | `postgres:15` |
| **Porta Exposta** | `5432` |
| **Database** | `ubereats_db` |
| **Usuario** | `usrUberEats` |
| **Senha** | `supersecret` |
| **Volume** | `postgres_data` (persistente) |

---

## Configuracoes Especiais

### WAL Level (Logical)

O PostgreSQL esta configurado com `wal_level=logical` para suportar:
- **Change Data Capture (CDC)**: Captura de mudancas em tempo real
- **Replicacao Logica**: Para ingestao no Databricks via Airbyte

```yaml
# docker-compose.yml
command: >
  postgres
  -c wal_level=logical
```

---

## Estrutura do Banco de Dados

### Tabela: `drivers`

Armazena informacoes dos motoristas/entregadores.

```sql
CREATE TABLE drivers (
    driver_id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(50),
    vehicle_type VARCHAR(50),
    license_plate VARCHAR(20),
    registration_date TIMESTAMP,
    total_deliveries INTEGER DEFAULT 0,
    total_earnings NUMERIC(10, 2) DEFAULT 0.00,
    average_rating NUMERIC(3, 1),
    last_login TIMESTAMP,
    status VARCHAR(20)
);
```

**Campos principais:**
- `driver_id`: Identificador unico (UUID)
- `vehicle_type`: Car, Motorcycle, Bicycle, Scooter
- `status`: Active, Inactive, Banned
- `total_earnings`: Ganhos totais em reais

---

### Tabela: `users`

Armazena informacoes dos usuarios/clientes.

```sql
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    name VARCHAR(255),
    username VARCHAR(100) UNIQUE,
    email VARCHAR(255) UNIQUE NOT NULL,
    email_verified BOOLEAN DEFAULT FALSE,
    phone_number VARCHAR(50),
    phone_verified BOOLEAN DEFAULT FALSE,
    -- ... (mais de 30 campos)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Campos principais:**
- `user_id`: Identificador unico (UUID)
- `subscription_tier`: Free, Basic, Premium
- `total_orders`: Numero de pedidos realizados
- `total_spend`: Valor total gasto
- `lat/lon`: Localizacao geografica

---

## Como Acessar

### Via DBeaver (Recomendado)

1. Baixe o DBeaver Community: https://dbeaver.io/download/
2. Crie uma nova conexao PostgreSQL:
   - **Host**: `localhost`
   - **Port**: `5432`
   - **Database**: `ubereats_db`
   - **Username**: `usrUberEats`
   - **Password**: `supersecret`

### Via psql (CLI)

```powershell
# Executar query diretamente
docker exec postgres-ubereats psql -U usrUberEats -d ubereats_db -c "SELECT COUNT(*) FROM drivers;"

# Entrar no psql interativo
docker exec -it postgres-ubereats psql -U usrUberEats -d ubereats_db
```

### Via Python (psycopg2)

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ubereats_db",
    user="usrUberEats",
    password="supersecret"
)

cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM drivers;")
print(cur.fetchone())
conn.close()
```

---

## Queries Uteis

### Verificar Contagem de Registros

```sql
SELECT 'drivers' as tabela, COUNT(*) as registros FROM drivers
UNION ALL
SELECT 'users', COUNT(*) FROM users;
```

### Top 10 Motoristas por Entregas

```sql
SELECT name, total_deliveries, total_earnings, average_rating
FROM drivers
ORDER BY total_deliveries DESC
LIMIT 10;
```

### Usuarios Premium Ativos

```sql
SELECT name, email, subscription_tier, total_orders, total_spend
FROM users
WHERE subscription_tier = 'Premium'
  AND status = 'Active'
ORDER BY total_spend DESC
LIMIT 10;
```

### Estatisticas Gerais

```sql
-- Drivers
SELECT 
    COUNT(*) as total_drivers,
    AVG(total_deliveries) as avg_deliveries,
    AVG(total_earnings) as avg_earnings,
    AVG(average_rating) as avg_rating
FROM drivers
WHERE status = 'Active';

-- Users
SELECT 
    COUNT(*) as total_users,
    AVG(total_orders) as avg_orders,
    AVG(total_spend) as avg_spend,
    COUNT(CASE WHEN subscription_tier = 'Premium' THEN 1 END) as premium_users
FROM users
WHERE status = 'Active';
```

---

## Scripts SQL

Os scripts SQL de criacao de tabelas estao localizados em:

```
sql/
├── create_drivers_table.sql
├── create_users_table.sql
└── cdc configure/
    └── database-cdc-config.sql
```

Esses scripts sao executados **automaticamente** quando o volume do Postgres e criado pela primeira vez (via `docker-entrypoint-initdb.d`).

---

## Monitoramento e Logs

### Ver Logs do Postgres

```powershell
# Logs em tempo real
docker-compose logs -f postgres-ubereats

# Ultimas 50 linhas
docker logs postgres-ubereats --tail 50
```

### Verificar Health Check

```powershell
docker inspect postgres-ubereats --format='{{.State.Health.Status}}'
```

### Verificar Conexoes Ativas

```sql
SELECT 
    pid,
    usename,
    application_name,
    client_addr,
    state,
    query_start
FROM pg_stat_activity
WHERE datname = 'ubereats_db';
```

---

## Backup e Restore

### Backup Completo

```powershell
# Backup do banco inteiro
docker exec postgres-ubereats pg_dump -U usrUberEats ubereats_db > backup_ubereats.sql

# Backup apenas de uma tabela
docker exec postgres-ubereats pg_dump -U usrUberEats -t drivers ubereats_db > backup_drivers.sql
```

### Restore

```powershell
# Restore completo
cat backup_ubereats.sql | docker exec -i postgres-ubereats psql -U usrUberEats ubereats_db

# Restore de uma tabela
cat backup_drivers.sql | docker exec -i postgres-ubereats psql -U usrUberEats ubereats_db
```

---

## Troubleshooting

### Container nao inicia

```powershell
# Verificar logs de erro
docker logs postgres-ubereats

# Remover volume corrompido (DESTRUTIVO!)
docker-compose down -v
docker-compose up -d postgres-ubereats
```

### Porta 5432 em uso

```powershell
# Descobrir o que esta usando a porta
netstat -ano | findstr "5432"

# Ou mude a porta no docker-compose.yml:
# ports:
#   - "5433:5432"  # Expoe na porta 5433
```

### Conexao recusada

```powershell
# Verifique se o container esta healthy
docker ps | findstr postgres

# Teste a conexao
docker exec postgres-ubereats pg_isready -U usrUberEats
```

---

## Performance e Otimizacao

### Indices Recomendados

```sql
-- Drivers
CREATE INDEX idx_drivers_status ON drivers(status);
CREATE INDEX idx_drivers_vehicle_type ON drivers(vehicle_type);
CREATE INDEX idx_drivers_rating ON drivers(average_rating);

-- Users
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_status ON users(status);
CREATE INDEX idx_users_subscription ON users(subscription_tier);
CREATE INDEX idx_users_location ON users(lat, lon);
```

### Vacuum e Analyze

```sql
-- Limpar espaco e atualizar estatisticas
VACUUM ANALYZE drivers;
VACUUM ANALYZE users;
```

---

## Integracao com Airbyte

O PostgreSQL esta preparado para ingestao via Airbyte com:
- **WAL Level**: `logical` (para CDC)
- **Porta exposta**: `5432`
- **Credenciais**: Configuradas

Consulte [../airbyte/README.md](../airbyte/README.md) para configurar a conexao.

---

## Links

- PostgreSQL: https://www.postgresql.org/docs/15/
- DBeaver: https://dbeaver.io/
- psycopg2: https://www.psycopg.org/

