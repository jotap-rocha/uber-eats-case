---
description: KB app_security — consultar boas práticas de segurança no desenvolvimento antes de alterar APIs, auth, SQL, secrets ou dados sensíveis
globs:
  - "src/**"
  - "**/*.py"
  - "**/*.tf"
  - "**/*.yaml"
  - "scripts/**"
  - "**/api/**"
alwaysApply: false
---

# Knowledge Base — Segurança da informação (desenvolvimento)

Quando o trabalho envolver **credenciais**, **autenticação/autorização**, **consultas SQL dinâmicas**, **endpoints HTTP**, **armazenamento no cliente**, **logs** ou **dados sensíveis**, aplicar **KB-first**:

1. Ler o índice [`.claude/kb/app_security/index.md`](mdc:.claude/kb/app_security/index.md) e o conceito aplicável (ex.: `concepts/secrets-gestao.md`, `concepts/sql-injection-prevencao.md`, `concepts/autorizacao-rbac-abac.md`).
2. Para gate de release ou revisão de PR de segurança, usar [`.claude/kb/app_security/specs/security-release-checklist.yaml`](mdc:.claude/kb/app_security/specs/security-release-checklist.yaml) e o resumo [`.claude/kb/app_security/quick-reference.md`](mdc:.claude/kb/app_security/quick-reference.md).
3. **Dados / Postgres / APIs**: se o repo usar RLS ou PostgREST, cruzar com a KB de persistência do projeto — autorização no **servidor**, não só na UI.

## Regras que não podem ser violadas sem decisão explícita de projeto

- Não commitar secrets nem `.env` com valores reais; frontend não carrega connection strings nem service keys com poder elevado.
- Não concatenar entrada do usuário em SQL — parâmetros ou ORM; filtros/`ORDER BY` dinâmicos só com **allowlist** (ver [`patterns/consultas-dinamicas-allowlist.md`](mdc:.claude/kb/app_security/patterns/consultas-dinamicas-allowlist.md)).
- Validar **permissões no backend** em toda rota sensível (esconder botão não basta).

Registro no índice da KB: domínio `app_security` em [`.claude/kb/_index.yaml`](mdc:.claude/kb/_index.yaml). Índice de agentes: [`.claude/agents/README.md`](mdc:.claude/agents/README.md) (seção **Knowledge Base**).
