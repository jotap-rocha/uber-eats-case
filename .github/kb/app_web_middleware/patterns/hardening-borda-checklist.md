# Checklist de *hardening* na borda web

> **Propósito**: Lista concisa para endurecer TLS, cabeçalhos e exposição na camada IIS / NGINX / Apache.  
> **MCP validado**: não aplicável

## Quando usar

- Antes de **go-live** ou em auditorias periódicas de infraestrutura.
- Após alteração de certificados, cipher suites ou exposição de novos *endpoints*.

## Checklist

| # | Verificação | Notas |
|---|-------------|-------|
| 1 | HTTPS obrigatório para usuários externos | Redirecionamento HTTP→HTTPS documentado |
| 2 | Certificados com cadeia completa e renovação monitorizada | ACME, PKI interna ou alarme de expiração |
| 3 | Versões TLS e cipher suites alinhadas à política | Desativar protocolos legados em PRD |
| 4 | Cabeçalhos de segurança na resposta | `Strict-Transport-Security`, `X-Content-Type-Options`, `Frame-Options` / CSP conforme política |
| 5 | Servir apenas o necessário | Desativar listagens de directório, *status pages* públicas indesejadas |
| 6 | Limites de corpo e rate limiting na borda (se aplicável) | Coordenar com limites da app |
| 7 | Logs de acesso com retenção e PI minimizada | Evitar query strings com dados sensíveis nos logs |
| 8 | Rede entre proxy e app | Firewall interno — só origens do proxy para a porta da app |

## Erros comuns

- Cabeçalhos duplicados ou inconsistentes entre CDN, proxy e app.
- **HSTS** sem plano de rollback se TLS interno ainda não estiver estável em todos os hosts.

## Ver também

- [reverse-proxy-upstream.md](reverse-proxy-upstream.md)
- [../../app_security/specs/security-release-checklist.yaml](../../app_security/specs/security-release-checklist.yaml)
