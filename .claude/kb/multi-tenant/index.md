---
domain: multi-tenant
description: Padrões de isolamento multi-tenant — RLS, tenant_id, schema separation, pre-filter vetorial
mcp_validated: "2026-06-27"
confidence: 0.90
---

# KB: Multi-Tenant

Padrões de isolamento entre tenants em sistemas compartilhados.
Princípio central: **tenant isolation é infraestrutura, não lógica de aplicação** — o banco isola, a app não precisa lembrar.

## Conceitos

| Arquivo | Tópico |
|---|---|
| [isolation-models.md](concepts/isolation-models.md) | Shared DB vs Schema separation vs DB separation — quando cada um |
| [tenant-context.md](concepts/tenant-context.md) | Propagar tenant_id via JWT, header, contextvars — sem passar como parâmetro manual |

## Padrões

| Arquivo | Tópico |
|---|---|
| [rls-multi-tenant.md](patterns/rls-multi-tenant.md) | Políticas RLS + índices compostos por tenant_id |
| [vector-tenant-isolation.md](patterns/vector-tenant-isolation.md) | Pre-filter de tenant em Qdrant e pgvector |

## Quick Reference

Ver [quick-reference.md](quick-reference.md) — modelos de isolamento, invariantes (MT-01…MT-05),
hierarquia de identidade. Ler só se a tarefa exigir esse nível de detalhe.
