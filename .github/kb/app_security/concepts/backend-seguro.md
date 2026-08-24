# Backend seguro

> **Purpose**: Camada de confiança: autenticação, autorização, validação e limites.  
> **Confidence**: 0.94

## Pilares

1. **Autenticação forte** — Ver [autenticacao-identidade.md](autenticacao-identidade.md).
2. **Autorização por perfil/permissão** — Cada endpoint sensível verifica papel/recurso (ver [autorizacao-rbac-abac.md](autorizacao-rbac-abac.md)).
3. **Validação de entrada** — Schema (JSON Schema, Zod, Pydantic, etc.) para body, query e path; tipos e intervalos; rejeitar campos extras quando relevante.
4. **Proteção contra SQL Injection** — Ver [sql-injection-prevencao.md](sql-injection-prevencao.md).
5. **Rate limiting** — Por IP/usuário/API key em login, reset de senha e endpoints caros.
6. **Logs de auditoria** — Ações sensíveis com quem/quando/o quê (ver [logs-auditoria.md](logs-auditoria.md)).
7. **Tratamento seguro de erros** — Log completo server-side; resposta ao cliente **sem** detalhes internos.
8. **Criptografia em trânsito** — TLS entre cliente↔API e API↔serviços.
9. **Criptografia em repouso** — Quando política ou LGPD exigir (discos, backups, colunas sensíveis).
10. **Separação DEV / HML / PRD** — Credenciais, dados e URLs isolados; config por ambiente via secrets manager.

## Padronização

- Idempotência e timeouts em chamadas externas; não propagar exceções cruas para o cliente.

## Referências cruzadas

- [apis-seguras.md](apis-seguras.md), [desenvolvimento-seguro-sdlc.md](desenvolvimento-seguro-sdlc.md)
