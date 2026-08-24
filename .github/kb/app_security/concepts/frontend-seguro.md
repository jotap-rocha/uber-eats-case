# Frontend seguro

> **Purpose**: Reduzir vazamento de credenciais e XSS na camada que roda no navegador.  
> **Confidence**: 0.94

## O que nunca fazer no código frontend

- Armazenar ou embutir **usuário, senha, token de serviço, connection string** em bundle JS/TS.
- Expor **chaves de API** com poder real no cliente (qualquer um pode extrair do DevTools).
- Confiar em **campos hidden**, `localStorage` ou `sessionStorage` para **autorização** ou dados sensíveis — são manipuláveis pelo usuário.

## HTTPS

- Produção sempre **HTTPS**; cookies sensíveis com flags adequadas (`Secure`, `HttpOnly` quando cookie-based session).
- APIs chamadas pelo browser devem ser TLS; evitar downgrade misto.

## XSS e conteúdo dinâmico

- **Sanitizar** HTML/markdown antes de renderizar.
- No React: **evitar `dangerouslySetInnerHTML`**; se inevitável, usar biblioteca de sanitização madura (ex.: DOMPurify) com política restrita.
- Defesa em profundidade: **Content-Security-Policy (CSP)** reduz impacto de XSS residual.

## Autorização

- UI pode **ocultar** ações por UX; **permissão real** só vale se o **backend** validar em toda rota (ver [autorizacao-rbac-abac.md](autorizacao-rbac-abac.md)).

## CORS

- Configurar **origens permitidas** explicitamente; evitar `Access-Control-Allow-Origin: *` junto de credenciais.
- Preflight e métodos/headers alinhados ao mínimo necessário.

## Mensagens ao usuário

- Não expor **stack traces**, nomes de tabelas internas ou IDs de infraestrutura na UI — usar mensagem genérica + **ID de correlação** para suporte.

## CSRF (sessão por cookie)

- Se autenticação for cookie-based: tokens anti-CSRF ou SameSite cookies conforme arquitetura.

## Referências cruzadas

- [backend-seguro.md](backend-seguro.md), [secrets-gestao.md](secrets-gestao.md)
