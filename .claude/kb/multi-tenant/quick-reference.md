---
domain: multi-tenant
topic: quick-reference
---

# Multi-Tenant — Quick Reference

### Modelos de isolamento

| Modelo | Isolamento | Custo | Quando |
|---|---|---|---|
| Shared schema + `tenant_id` | Médio (RLS) | Baixo | SaaS com muitos tenants pequenos |
| Schema separation | Alto | Médio | Compliance forte, poucos tenants |
| DB separation | Total | Alto | Enterprise, dados sensíveis, SLA individual |

### Invariantes

| # | Invariante |
|---|---|
| MT-01 | `tenant_id` como **primeiro** predicado em toda query — nunca como segundo |
| MT-02 | RLS habilitado em toda tabela com dados de tenant |
| MT-03 | Isolamento vetorial via **pre-filter**, nunca via semântica |
| MT-04 | `tenant_id` extraído do JWT/sessão no request — nunca confiado no body |
| MT-05 | Índice composto `(tenant_id, campo_filtro)` em toda tabela grande |

### Hierarquia de identidade

```
Usuário (user_id) → pertence a → Organização (org_id = tenant_id)
                                       ↓
                                 Dados da org (tenant_id = org_id)
```
