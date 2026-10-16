# Modelos de Isolamento Multi-Tenant

## Comparativo

| Critério | Shared Schema | Schema Separation | DB Separation |
|---|---|---|---|
| Isolamento | RLS (software) | Schema (DB) | Hardware |
| Vazamento de dados | Possível se RLS falhar | Improvável | Impossível |
| Número de tenants | Ilimitado | Centenas | Dezenas |
| Custo por tenant | Mínimo | Baixo | Alto |
| Migrations | 1 migration para todos | N migrations | N migrations + N DBs |
| Compliance (LGPD/SOC2) | Precisa evidenciar RLS | Mais fácil evidenciar | Trivial evidenciar |
| Backup por tenant | Complexo (filter) | Por schema | Por DB |

## Modelo 1: Shared Schema (mais comum em SaaS)

```sql
-- Toda tabela tem tenant_id
CREATE TABLE casos (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id   UUID NOT NULL REFERENCES tenants(id),
  titulo      TEXT NOT NULL,
  status      TEXT NOT NULL,
  created_at  TIMESTAMPTZ DEFAULT now()
);

-- Índice composto — tenant_id sempre primeiro
CREATE INDEX idx_casos_tenant_status ON casos (tenant_id, status);
CREATE INDEX idx_casos_tenant_created ON casos (tenant_id, created_at DESC);

-- RLS como barreira
ALTER TABLE casos ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON casos
  USING (tenant_id = current_setting('app.current_tenant')::uuid);
```

```python
# Configurar tenant no início do request
async def set_tenant_context(conn: asyncpg.Connection, tenant_id: str):
    await conn.execute("SET LOCAL app.current_tenant = $1", tenant_id)
```

## Modelo 2: Schema Separation

```sql
-- Criar schema por tenant
CREATE SCHEMA tenant_abc;
CREATE SCHEMA tenant_xyz;

-- Mesma estrutura de tabela em cada schema
CREATE TABLE tenant_abc.casos (...);
CREATE TABLE tenant_xyz.casos (...);

-- search_path por conexão
SET search_path TO tenant_abc;
SELECT * FROM casos;  -- acessa tenant_abc.casos automaticamente
```

```python
async def get_tenant_conn(pool, tenant_id: str):
    conn = await pool.acquire()
    await conn.execute(f"SET search_path TO tenant_{tenant_id.replace('-', '_')}")
    return conn
```

## Modelo 3: DB Separation

```python
# Pool separado por tenant
TENANT_POOLS: dict[str, asyncpg.Pool] = {}

async def get_pool(tenant_id: str) -> asyncpg.Pool:
    if tenant_id not in TENANT_POOLS:
        dsn = get_tenant_dsn(tenant_id)  # DSN por tenant em config/secret manager
        TENANT_POOLS[tenant_id] = await asyncpg.create_pool(dsn, min_size=1, max_size=5)
    return TENANT_POOLS[tenant_id]
```

## Quando migrar entre modelos

| Gatilho | Ação |
|---|---|
| Tenant pede LGPD Art. 46 (medidas técnicas) | Schema separation |
| Tenant quer SLA de DB individualizado | DB separation |
| Audit trail por tenant exigido | Schema separation (mais fácil de auditar) |
| Tenant > 10M linhas (performance crítica) | Schema ou DB separation |
| Custo do modelo atual inviável | Shared schema (consolidar) |
