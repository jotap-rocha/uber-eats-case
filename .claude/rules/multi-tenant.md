---
paths:
  - "**/tenant*/**"
  - "**/multi_tenant/**"
  - "**/rls/**"
  - "**/org*/**"
  - "**/membership*/**"
---

# Regras de Multi-Tenant — Invariantes de Isolamento

Esta rule carrega ao tocar arquivos de tenant, RLS, organização ou membership.
São invariantes de segurança — uma violação pode causar vazamento de dados entre tenants.

## Os 5 invariantes

### MT-01 — tenant_id como primeiro predicado em toda query

Índices compostos funcionam melhor quando o campo mais seletivo vem primeiro.
`tenant_id` + filtro > filtro + `tenant_id` em performance.

```sql
-- CERTO: tenant_id primeiro
WHERE tenant_id = $1 AND status = $2

-- ERRADO: tenant_id no meio
WHERE status = $2 AND tenant_id = $1

-- ERRADO: sem tenant_id
WHERE status = $2  -- sem tenant = todos os dados de todos os tenants
```

### MT-02 — RLS habilitado em toda tabela com dados de tenant

Sem RLS, qualquer chamada direta ao banco (bypass da app) expõe dados de todos os tenants.

```sql
-- OBRIGATÓRIO em toda tabela com dados de tenant
ALTER TABLE {tabela} ENABLE ROW LEVEL SECURITY;
ALTER TABLE {tabela} FORCE ROW LEVEL SECURITY;

-- Verificar quais tabelas estão sem RLS
SELECT tablename FROM pg_tables
WHERE schemaname = 'public'
  AND tablename NOT IN (
    SELECT tablename FROM pg_policies GROUP BY tablename
  );
```

### MT-03 — Isolamento vetorial via pre-filter, nunca via semântica

Documentos de tenants diferentes podem ser semanticamente idênticos.
A similaridade semântica não garante isolamento — apenas o pre-filter de metadados garante.

```python
# ERRADO: confiar na semântica
hits = qdrant.search(collection, vector, limit=5)
# pode retornar docs de qualquer tenant

# CERTO: pre-filter ANTES do semântico
hits = qdrant.search(
    collection,
    vector,
    query_filter=Filter(must=[FieldCondition(key="tenant_id", match=MatchValue(value=tenant_id))]),
    limit=5,
)
```

### MT-04 — tenant_id extraído do JWT/sessão, nunca do body

O body da request é controlado pelo cliente — pode ser forjado.
O JWT é assinado pelo servidor e verificado antes de qualquer processamento.

```python
# ERRADO: confiar no tenant_id do body
@router.post("/casos")
async def create_caso(body: CasoCreate):
    await db.execute("INSERT INTO casos (tenant_id) VALUES ($1)", body.tenant_id)  # forjável!

# CERTO: extrair do JWT verificado
@router.post("/casos")
async def create_caso(
    body: CasoCreate,
    tenant_id: str = Depends(get_tenant_id),  # do JWT, não do body
):
    await db.execute("INSERT INTO casos (tenant_id) VALUES ($1)", tenant_id)
```

### MT-05 — Índice composto (tenant_id, campo_filtro) em toda tabela grande

Sem índice, o pre-filter de tenant causa scan completo.
Com índice, o banco vai direto ao subconjunto do tenant.

```sql
-- OBRIGATÓRIO ao criar tabela com tenant_id
CREATE INDEX idx_{tabela}_tenant_status   ON {tabela} (tenant_id, status);
CREATE INDEX idx_{tabela}_tenant_created  ON {tabela} (tenant_id, created_at DESC);

-- Verificar queries sem índice adequado
EXPLAIN (ANALYZE) SELECT * FROM casos WHERE tenant_id = $1 AND status = $2;
-- Deve mostrar "Index Scan" ou "Bitmap Index Scan", nunca "Seq Scan" em produção
```

---

## Checklist de revisão multi-tenant

Antes de qualquer PR que toque dados de tenant:

- [ ] Toda nova tabela tem `tenant_id NOT NULL` + `ENABLE ROW LEVEL SECURITY`
- [ ] Políticas RLS criadas para todas as operações (SELECT, INSERT, UPDATE, DELETE)
- [ ] UPDATE tem `USING` + `WITH CHECK` (evita mudar tenant_id para outro tenant)
- [ ] Índice composto `(tenant_id, ...)` criado antes do merge
- [ ] Busca vetorial com pre-filter de `tenant_id` (não filtro pós-busca)
- [ ] `tenant_id` extraído do JWT no middleware — não aceito do body

## Referências

- `.claude/kb/multi-tenant/index.md` — visão geral e modelos de isolamento
- `.claude/kb/multi-tenant/patterns/rls-multi-tenant.md` — políticas prontas
- `.claude/kb/multi-tenant/patterns/vector-tenant-isolation.md` — Qdrant e pgvector
- `.claude/kb/supabase/concepts/rls.md` — RLS no Supabase
