# Usuários, senhas e autenticação

> **Purpose**: Evitar autenticação frágil ou “caseira” em produção.  
> **Confidence**: 0.93

## Preferências

- **SSO corporativo** quando possível: **Entra ID (Azure AD)**, **Okta**, **Keycloak**, etc.
- **MFA** obrigatório ou fortemente recomendado para **administradores** e contas com poder elevado.

## Senhas (quando aplicável)

- **Nunca** persistir senha em texto claro.
- Hash com algoritmo moderno e custo calibrado: **Argon2** (preferência), **bcrypt**, ou **PBKDF2** com parâmetros atuais — mais salt/work factor conforme guia do OWASP Password Storage Cheat Sheet.

## Sessão e tokens

- **Expiração de sessão** e renovação com política clara (idle + absolute timeout quando necessário).
- **Revogar** refresh tokens / sessões em logout, troca de senha ou comprometimento.
- Separar **conta operacional** de **conta administrativa** (contas diferentes ou roles estritas).

## Anti-padrões

- JWT no `localStorage` para APIs sensíveis sem mitigação adicional (risco XSS token theft) — avaliar HttpOnly cookie ou estratégia híbrida com CSRF controlado.
- “Login próprio” sem proteção a brute force, CAPTCHA adaptativo ou lockout progressivo onde fizer sentido.

## Referências cruzadas

- [autorizacao-rbac-abac.md](autorizacao-rbac-abac.md), [frontend-seguro.md](frontend-seguro.md)
