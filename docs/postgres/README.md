# PostgreSQL - Banco OLTP

PostgreSQL 15 com dados transacionais (drivers e users).

---

## Credenciais

```
Host: localhost
Port: 5432
Database: ubereats_db
User: usrUberEats
Password: supersecret
```

---

## Tabelas

### drivers

```sql
CREATE TABLE drivers (
    driver_id UUID PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    phone_number VARCHAR(50),
    vehicle_type VARCHAR(50),
    total_deliveries INTEGER,
    total_earnings NUMERIC(10, 2),
    average_rating NUMERIC(3, 1),
    status VARCHAR(20)
);
```

### users

```sql
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    phone_number VARCHAR(50),
    subscription_tier VARCHAR(20),
    total_orders INTEGER,
    total_spend NUMERIC(10, 2),
    lat NUMERIC(10, 8),
    lon NUMERIC(11, 8),
    status VARCHAR(20)
);
```

---

## Como Acessar

### DBeaver (recomendado)

1. Baixe: https://dbeaver.io/download/
2. Crie conexao PostgreSQL com as credenciais acima

### CLI (psql)

```powershell
# Query direta
docker exec postgres-ubereats psql -U usrUberEats -d ubereats_db -c "SELECT COUNT(*) FROM drivers;"

# Modo interativo
docker exec -it postgres-ubereats psql -U usrUberEats -d ubereats_db
```

---

## Queries Uteis

```sql
-- Contagem
SELECT 'drivers' as tabela, COUNT(*) as registros FROM drivers
UNION ALL
SELECT 'users', COUNT(*) FROM users;

-- Verificar health
SELECT pg_is_in_recovery();
```

---

## Troubleshooting

### Container nao inicia

```powershell
docker logs postgres-ubereats
```

### Porta em uso

```powershell
netstat -ano | findstr "5432"
```

### Conexao recusada

```powershell
docker exec postgres-ubereats pg_isready -U usrUberEats
```

---

## Links

- PostgreSQL: https://www.postgresql.org/docs/15/
- DBeaver: https://dbeaver.io/
