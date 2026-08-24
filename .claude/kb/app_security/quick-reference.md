# App security — referência rápida

> **Confidence**: 0.92 (consolidado OWASP/indústria; validar políticas internas)

## Checklist resumido

- [ ] Não há secrets no frontend.
- [ ] Não há secrets no Git (nem `.env` commitado).
- [ ] Backend valida toda entrada relevante.
- [ ] Backend autoriza toda ação sensível (não só o menu).
- [ ] SQL usa parâmetros / ORM seguro; filtros dinâmicos com allowlist.
- [ ] APIs em HTTPS; HSTS em produção quando aplicável.
- [ ] CORS restrito a origens conhecidas (não `*` com credenciais).
- [ ] Usuário do banco com privilégio mínimo (não `sysadmin`).
- [ ] Logs não expõem senhas, tokens, connection strings, PII integral.
- [ ] Erros ao usuário final são genéricos; detalhe técnico só server-side/correlation id.
- [ ] Auditoria em ações críticas (quem, quando, o quê, resultado).
- [ ] Rate limit em APIs públicas ou sensíveis.
- [ ] Dependências monitoradas e atualizadas (supply chain).
- [ ] DEV / HML / PRD separados; sem dados reais sensíveis em DEV.

Versão estruturada: [specs/security-release-checklist.yaml](specs/security-release-checklist.yaml).

## Lembretes curtos

| Risco | Regra |
|-------|--------|
| XSS | Sanitizar HTML; CSP; evitar `dangerouslySetInnerHTML` sem sanitização forte |
| AuthZ | Esconder botão ≠ segurança — validar em **toda** API |
| SQLi | Nunca concatenar input em SQL — usar bind parameters |
| Secrets | Cofre central + rotação — não logar nem printar |

## OWASP

Consultar **OWASP Top 10**, **ASVS** (verificação de aplicações) e **Cheat Sheets** para profundidade por controle.
