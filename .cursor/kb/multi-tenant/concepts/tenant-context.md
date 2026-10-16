# Tenant Context — Propagação do tenant_id

## Princípio: extrair do JWT, não confiar no body

```
Request HTTP
    ↓
JWT/Token → extrair tenant_id (verificado, assinado)
    ↓
Contextvars / structlog context
    ↓
Toda camada abaixo recebe sem precisar passar explicitamente
```

## Extração do tenant_id via JWT

```python
# FastAPI — middleware de tenant
from fastapi import Request, HTTPException
import jwt

async def extract_tenant(request: Request) -> str:
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token ausente")

    token = auth.removeprefix("Bearer ")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

    tenant_id = payload.get("org_id") or payload.get("tenant_id")
    if not tenant_id:
        raise HTTPException(status_code=403, detail="Token sem tenant_id")

    return tenant_id

# Dependency
async def get_tenant_id(request: Request) -> str:
    return await extract_tenant(request)
```

## Propagação via contextvars (Python)

```python
from contextvars import ContextVar

_tenant_id: ContextVar[str] = ContextVar("tenant_id", default="")

def set_tenant(tenant_id: str):
    _tenant_id.set(tenant_id)

def get_tenant() -> str:
    tenant = _tenant_id.get()
    if not tenant:
        raise RuntimeError("tenant_id não definido no contexto atual")
    return tenant

# No middleware do FastAPI
async def tenant_middleware(request: Request, call_next):
    tenant_id = await extract_tenant(request)
    set_tenant(tenant_id)
    structlog.contextvars.bind_contextvars(tenant_id=tenant_id)
    return await call_next(request)
```

## Uso no service e tools (sem passar como parâmetro)

```python
# Service — pega do contexto, não do parâmetro
class ChatService:
    async def process(self, query: str) -> ServiceResult:
        tenant_id = get_tenant()  # contexto automático
        result = await self.graph.ainvoke({
            "query": query,
            "tenant_id": tenant_id,  # injetado aqui, uma vez
        })
        return ServiceResult(answer=result["answer"])

# Tool de busca — recebe via state, não via parâmetro de request
async def search_node(state: AgentState) -> dict:
    result = await search(
        query=state["query"],
        tenant_id=state["tenant_id"],  # propagado no state do grafo
    )
```

## Supabase — tenant via JWT claim

```typescript
// Frontend: tenant_id vem do JWT automaticamente
const { data: { session } } = await supabase.auth.getSession()
const tenantId = session?.user.app_metadata?.org_id

// RLS usa auth.uid() ou JWT claim — frontend não precisa filtrar
const { data } = await supabase
  .from("casos")
  .select("*")
  // SEM .eq("org_id", tenantId) — RLS já garante isolamento
```

## Anti-padrões

```python
# ERRADO: confiar no tenant_id que vem no body
@router.post("/casos")
async def create_caso(body: CasoCreate):
    await db.execute("INSERT INTO casos (tenant_id, ...) VALUES ($1, ...)",
                     body.tenant_id, ...)  # usuário pode forjar outro tenant_id!

# ERRADO: passar tenant_id por toda a call chain
async def service(query, tenant_id):
    return await repo(query, tenant_id)  # vai passando em todo lugar

def repo(query, tenant_id):
    return await tool(query, tenant_id)

# CERTO: extrair no middleware, propagar via contextvars ou state do grafo
```
