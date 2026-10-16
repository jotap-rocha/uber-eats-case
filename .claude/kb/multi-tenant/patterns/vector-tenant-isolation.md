# Isolamento de Tenant em Busca Vetorial

## Por que a semântica não garante isolamento

```
Tenant A indexou: "Política de reembolso: devolver em 30 dias"
Tenant B indexou: "Política de reembolso: devolver em 7 dias"

Sem pre-filter de tenant_id:
  query("política de reembolso") → retorna AMBOS os documentos
  → Tenant A pode ver política do Tenant B → VAZAMENTO DE DADOS
```

## Qdrant — pre-filter obrigatório

```python
from qdrant_client.models import Filter, FieldCondition, MatchValue

# CERTO: pre-filter ANTES do semântico
async def search_tenant_safe(
    query: str,
    tenant_id: str,
    collection: str,
    top_k: int = 5,
) -> list[dict]:
    must_filters = [
        FieldCondition(key="tenant_id", match=MatchValue(value=tenant_id))
    ]

    vector = await embedder.aembed_query(query)
    hits = qdrant.search(
        collection_name=collection,
        query_vector=vector,
        query_filter=Filter(must=must_filters),  # aplicado ANTES do semântico
        limit=top_k,
        with_payload=True,
    )
    return [{"content": h.payload["content"], "source": h.id} for h in hits]

# ERRADO: filtrar depois
hits = qdrant.search(collection_name=collection, query_vector=vector, limit=100)
hits_filtered = [h for h in hits if h.payload["tenant_id"] == tenant_id]
# Problema: busca semântica já retornou docs de outros tenants
```

## Payload index obrigatório para tenant_id

```python
from qdrant_client.models import PayloadSchemaType

# Criar ao provisionar a collection
qdrant.create_payload_index(
    collection_name="documentos",
    field_name="tenant_id",
    field_schema=PayloadSchemaType.KEYWORD,
)

# Sem payload index: pre-filter = scan completo = O(n) lento
# Com payload index: pre-filter = O(log n) eficiente
```

## Schema de payload obrigatório

```python
# Todo ponto indexado deve ter tenant_id como campo obrigatório
payload = {
    "tenant_id":   tenant_id,           # isolamento
    "user_id":     user_id,             # rastreabilidade
    "content":     chunk_text,          # grounding
    "source":      f"doc:{doc_id}",     # citação
    "type":        "politica",          # filtro por tipo
    "created_at":  datetime.utcnow().isoformat(),
}
```

## pgvector — pre-filter em SQL

```sql
-- Função com tenant_id como parâmetro obrigatório
CREATE OR REPLACE FUNCTION match_tenant_docs(
  query_embedding vector(1536),
  p_tenant_id     UUID,                    -- sempre obrigatório
  match_threshold FLOAT DEFAULT 0.7,
  match_count     INT DEFAULT 5
)
RETURNS TABLE (id UUID, content TEXT, similarity FLOAT)
LANGUAGE sql STABLE AS $$
  SELECT
    id,
    content,
    1 - (embedding <=> query_embedding) AS similarity
  FROM documentos
  WHERE
    tenant_id = p_tenant_id              -- pre-filter ANTES do semântico
    AND 1 - (embedding <=> query_embedding) > match_threshold
  ORDER BY embedding <=> query_embedding
  LIMIT match_count;
$$;
```

## Ingestão — garantir tenant_id no ponto

```python
async def ingest_document(
    text: str,
    tenant_id: str,     # obrigatório
    source: str,
    doc_type: str,
) -> None:
    if not tenant_id:
        raise ValueError("tenant_id é obrigatório para ingestão")

    chunks = splitter.split_text(text)
    for i, chunk in enumerate(chunks):
        vector = await embedder.aembed_query(chunk)
        qdrant.upsert(
            collection_name="documentos",
            points=[PointStruct(
                id=str(uuid4()),
                vector=vector,
                payload={
                    "tenant_id": tenant_id,   # SEMPRE presente
                    "content": chunk,
                    "source": source,
                    "type": doc_type,
                    "chunk_index": i,
                }
            )]
        )
```

## Anti-padrões

```python
# ERRADO: confiar na semântica para isolamento
results = qdrant.search(collection, vector, limit=5)
# retorna docs de qualquer tenant

# ERRADO: filtrar após a busca
results = qdrant.search(collection, vector, limit=100)
tenant_results = [r for r in results if r.payload["tenant_id"] == tid]
# já buscou dados de outros tenants — violação mesmo que filtre depois

# ERRADO: indexar sem tenant_id
qdrant.upsert(collection, [PointStruct(id=..., vector=..., payload={"content": text})])
# impossível isolar depois sem reindexar tudo
```
