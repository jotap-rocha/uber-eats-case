# RLS Multi-Tenant — Políticas e Índices

## Setup completo para shared schema

```sql
-- 1. Tabela de tenants
CREATE TABLE tenants (
  id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  nome       TEXT NOT NULL,
  slug       TEXT NOT NULL UNIQUE,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 2. Tabela de membros (bridge user ↔ tenant)
CREATE TABLE tenant_members (
  user_id   UUID NOT NULL REFERENCES auth.users(id),
  tenant_id UUID NOT NULL REFERENCES tenants(id),
  role      TEXT NOT NULL DEFAULT 'member' CHECK (role IN ('owner', 'admin', 'member', 'viewer')),
  PRIMARY KEY (user_id, tenant_id)
);
ALTER TABLE tenant_members ENABLE ROW LEVEL SECURITY;
CREATE POLICY "proprio_membership"
  ON tenant_members FOR SELECT USING (user_id = auth.uid());

-- 3. Tabela de dados com tenant_id
CREATE TABLE casos (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id   UUID NOT NULL REFERENCES tenants(id),
  titulo      TEXT NOT NULL,
  status      TEXT NOT NULL DEFAULT 'aberto',
  created_at  TIMESTAMPTZ DEFAULT now()
);

-- 4. RLS na tabela de dados
ALTER TABLE casos ENABLE ROW LEVEL SECURITY;
FORCE ROW LEVEL SECURITY;  -- bloqueia até o owner da tabela

-- Política: membro do tenant vê dados do tenant
CREATE POLICY "tenant_member_select"
ON casos FOR SELECT
USING (
  tenant_id IN (
    SELECT tenant_id FROM tenant_members WHERE user_id = auth.uid()
  )
);

-- Política: membro pode inserir apenas no seu tenant
CREATE POLICY "tenant_member_insert"
ON casos FOR INSERT
WITH CHECK (
  tenant_id IN (
    SELECT tenant_id FROM tenant_members WHERE user_id = auth.uid()
  )
);

-- Política: apenas admin/owner pode deletar
CREATE POLICY "tenant_admin_delete"
ON casos FOR DELETE
USING (
  EXISTS (
    SELECT 1 FROM tenant_members
    WHERE user_id = auth.uid()
      AND tenant_id = casos.tenant_id
      AND role IN ('owner', 'admin')
  )
);
```

## Índices obrigatórios

```sql
-- tenant_id SEMPRE primeiro no índice composto
CREATE INDEX idx_casos_tenant_status   ON casos (tenant_id, status);
CREATE INDEX idx_casos_tenant_created  ON casos (tenant_id, created_at DESC);

-- Para subquery de membros (usada em toda política RLS)
CREATE INDEX idx_members_user_tenant   ON tenant_members (user_id, tenant_id);
CREATE INDEX idx_members_tenant        ON tenant_members (tenant_id);
```

## Verificar eficiência da política RLS

```sql
-- Analisar plano com RLS ativo
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT * FROM casos WHERE status = 'aberto' LIMIT 20;
-- Verificar se usa idx_casos_tenant_status (index scan, não seq scan)
```

## asyncpg com app.current_tenant (alternativa ao Supabase RLS)

```python
# Configurar variável de sessão no início de cada conexão
async def execute_as_tenant(pool: asyncpg.Pool, tenant_id: str, query: str, *args):
    async with pool.acquire() as conn:
        async with conn.transaction():
            await conn.execute("SET LOCAL app.current_tenant = $1", tenant_id)
            return await conn.fetch(query, *args)

# Política RLS usando a variável de sessão
# CREATE POLICY tenant_isolation ON casos
#   USING (tenant_id = current_setting('app.current_tenant', true)::uuid);
```

## Checklist de RLS multi-tenant

- [ ] `tenant_id` com `NOT NULL` + FK para tabela de tenants
- [ ] `ENABLE ROW LEVEL SECURITY` + `FORCE ROW LEVEL SECURITY` em toda tabela
- [ ] Políticas separadas por operação (SELECT, INSERT, UPDATE, DELETE)
- [ ] UPDATE tem `USING` (para ler) + `WITH CHECK` (para não mudar tenant)
- [ ] Índice composto `(tenant_id, campo_filtro)` — tenant_id SEMPRE primeiro
- [ ] Índice na tabela de membros `(user_id, tenant_id)`
- [ ] Testado com simulação de usuário via `SET LOCAL ROLE`
