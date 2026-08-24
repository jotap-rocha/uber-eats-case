# Segurança da informação — desenvolvimento de aplicações

> **Propósito**: Boas práticas de segurança para frontend, backend, identidade, autorização, secrets, SQL, APIs, banco, logs e SDLC — referência OWASP-aligned para times de produto.  
> **Projeto local**: Complementa pipelines, APIs e armazenamento deste repositório (ajustar links em `index.md` se criares KB `backend/` ou `supabase/` aqui).

## Navegação — conceitos

| Arquivo | Tema |
|---------|------|
| [concepts/frontend-seguro.md](concepts/frontend-seguro.md) | Secrets no cliente, XSS, HTTPS, CORS, storage |
| [concepts/backend-seguro.md](concepts/backend-seguro.md) | AuthN/Z, validação, rate limit, erros, ambientes |
| [concepts/autenticacao-identidade.md](concepts/autenticacao-identidade.md) | SSO, MFA, hash de senha, sessão, tokens |
| **Segredos em nuvem (OCI)** | [../key-oci/index.md](../key-oci/index.md) — cofre, OCIDs, `key_oci` |
| [concepts/autorizacao-rbac-abac.md](concepts/autorizacao-rbac-abac.md) | RBAC/ABAC, API, menor privilégio |
| [concepts/secrets-gestao.md](concepts/secrets-gestao.md) | Cofres, rotação, o que nunca versionar |
| [concepts/sql-injection-prevencao.md](concepts/sql-injection-prevencao.md) | Parâmetros, allowlist, ORM |
| [concepts/apis-seguras.md](concepts/apis-seguras.md) | REST: HTTPS, limites, paginação, versionamento |
| [concepts/banco-dados-seguro.md](concepts/banco-dados-seguro.md) | Usuários DB, permissões mínimas, criptografia |
| [concepts/logs-auditoria.md](concepts/logs-auditoria.md) | O que logar / não logar, correlação |
| [concepts/desenvolvimento-seguro-sdlc.md](concepts/desenvolvimento-seguro-sdlc.md) | Review, SAST/DAST, dependências, OWASP |

## Padrões

| Arquivo | Uso |
|---------|-----|
| [patterns/consultas-dinamicas-allowlist.md](patterns/consultas-dinamicas-allowlist.md) | ORDER BY / filtros dinâmicos com allowlist |
| [patterns/cofres-secrets-nuvem.md](patterns/cofres-secrets-nuvem.md) | Key Vault, Secrets Manager, Vault, OCI, Databricks |

## Specs

| Arquivo | Uso |
|---------|-----|
| [specs/security-release-checklist.yaml](specs/security-release-checklist.yaml) | Checklist máquina-humano pré-release |

## Referência rápida

- [quick-reference.md](quick-reference.md)

## Trilha de leitura

| Perfil | Ordem sugerida |
|--------|----------------|
| **Full-stack** | frontend-seguro → backend-seguro → apis-seguras → secrets-gestao |
| **Backend/API** | autorizacao-rbac-abac → sql-injection-prevencao → banco-dados-seguro → logs-auditoria |
| **DevOps/Segurança** | secrets-gestao → desenvolvimento-seguro-sdlc → specs/security-release-checklist.yaml |

## Agentes sugeridos

| Agente | Quando |
|--------|--------|
| `code-reviewer` | PR com superfície de segurança |
| `backend-specialist` / `supabase-specialist` | RLS, API, Postgres |
| `kb-architect` | Evoluir esta KB |
