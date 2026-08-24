# Autorização e controle de acesso

> **Purpose**: Estar logado ≠ poder executar a ação. Este é um dos controles mais críticos.  
> **Confidence**: 0.95

## Modelos

- **RBAC** — Acesso por **papéis** (ex.: `analyst`, `manager`, `admin`).
- **ABAC** — Atributos (empresa, linha de negócio, dono do recurso, sensibilidade) quando RBAC não basta.

## Exemplo de cenários distintos

| Usuário | Permissão típica |
|---------|-------------------|
| A | Ver pipeline apenas **DEV** |
| B | Executar pipeline **PRD** |
| C | Somente **consultar logs** |
| D | **Administrar permissões** |

## Boas práticas

- Validar **autorização em toda API** — não apenas na montagem do menu.
- **Não confiar** em UI escondida: chamadas diretas (curl, Postman, DevTools) contornam o frontend.
- Bloquear **acesso direto por URL/API** sem checagem server-side.
- **Menor privilégio** — Default deny; liberar explicitamente.

## Exemplo ruim

> “Escondi o botão Excluir, então está seguro.”

**Errado.** O cliente pode invocar `DELETE /recurso/:id` diretamente.

## APIs e recursos

- Checar **papéis + escopo do recurso** (multi-tenant: empresa X só vê dados de X — no SisFraude, alinhar a RLS Supabase quando usar Postgres).

## Referências cruzadas

- [backend-seguro.md](backend-seguro.md), [apis-seguras.md](apis-seguras.md)
