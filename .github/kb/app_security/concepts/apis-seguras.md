# APIs seguras (REST e afins)

> **Purpose**: Superfície HTTP endurecida: transporte, authZ e limites.  
> **Confidence**: 0.94

## Transporte

- **HTTPS obrigatório** em produção; redirecionar HTTP→HTTPS.

## Autenticação e autorização

- Autenticar **todos** os endpoints sensíveis (não depender de “obscuridade”).
- Autorizar por **endpoint e recurso** (ex.: só dono ou admin pode `DELETE`).

## Limites e validação

- **Rate limit** (login, busca pesada, exportação).
- **Validação de payload** — tamanho máximo do body; rejeitar JSON gigante.
- **Paginação obrigatória** em listagens grandes — `limit` máximo server-side.

## Resposta

- **Minimizar dados** — não retornar campos internos ou PII desnecessária.
- **Versionamento** (`/v1/`) para mudanças breaking com migração controlada.

## Auditoria

- Registrar ações sensíveis (ver [logs-auditoria.md](logs-auditoria.md)).

## GraphQL / RPC

- Limites de profundidade/custo, introspection desabilitada em PRD se aplicável, authZ por resolver.

## Referências cruzadas

- [backend-seguro.md](backend-seguro.md), [autorizacao-rbac-abac.md](autorizacao-rbac-abac.md)
