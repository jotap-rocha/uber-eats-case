# Middleware web — borda da aplicação

> **Propósito**: Documentar a camada na borda HTTP entre clientes e aplicações — servidores web e *reverse proxies* típicos por SO (**IIS** no Windows; **NGINX** ou **Apache httpd** no Linux).  
> **MCP validado**: não aplicável (KB interna; confirmar versões nos docs oficiais ao implementar).

## Navegação — conceitos

| Arquivo | Tema |
|----------|------|
| [concepts/camada-middleware-aplicacao.md](concepts/camada-middleware-aplicacao.md) | Papel da camada, fluxo TLS → proxy → *upstream*, termos |
| [concepts/iis-windows.md](concepts/iis-windows.md) | IIS em Windows — *sites*, *bindings*, ARR, integração ASP.NET |
| [concepts/nginx-linux.md](concepts/nginx-linux.md) | NGINX no Linux — event-driven, `server`/`location`, *upstream*; **SisFraude:** TLS em `/etc/nginx/certs/` (`.pem` + `.key`) |
| [concepts/apache-httpd-linux.md](concepts/apache-httpd-linux.md) | Apache httpd — MPM, VirtualHost, `mod_proxy` |

## Padrões

| Arquivo | Uso |
|----------|-----|
| [patterns/reverse-proxy-upstream.md](patterns/reverse-proxy-upstream.md) | Encaminhar tráfego para app Node/Java/.NET atrás do proxy |
| [patterns/hardening-borda-checklist.md](patterns/hardening-borda-checklist.md) | Cabeçalhos, TLS, limites e superfície mínima na borda |
| [patterns/few-shot-iis-web-config-url-rewrite.md](patterns/few-shot-iis-web-config-url-rewrite.md) | Few-shot `web.config` + URL Rewrite / *stub* ARR |
| [patterns/few-shot-nginx-sites-available.md](patterns/few-shot-nginx-sites-available.md) | Few-shot `sites-available` NGINX completo (TLS + *upstream*) |
| [patterns/nginx-websocket-proxy-map.md](patterns/nginx-websocket-proxy-map.md) | WebSockets: `map $http_upgrade $connection_upgrade` no `http {}` |
| [patterns/few-shot-apache-sites-available.md](patterns/few-shot-apache-sites-available.md) | Few-shot Apache `sites-available` completo |

## Specs

| Arquivo | Uso |
|----------|-----|
| [specs/borda-web-checklist.yaml](specs/borda-web-checklist.yaml) | Checklist máquina-humano para revisão de *deploy* na borda |

## Referência rápida

- [quick-reference.md](quick-reference.md)

## Trilha de leitura

| Perfil | Ordem sugerida |
|--------|----------------|
| **DevOps / plataforma** | camada-middleware-aplicacao → reverse-proxy-upstream → hardening-borda-checklist |
| **Windows / .NET** | iis-windows → reverse-proxy-upstream → specs/borda-web-checklist.yaml |
| **Linux** | nginx-linux **ou** apache-httpd-linux → reverse-proxy-upstream → hardening-borda-checklist |

## Agentes sugeridos

| Agente | Quando |
|--------|--------|
| `kb-architect` | Criar/auditar domínios KB ou evolução em massa da estrutura |
| `web-edge-specialist` | Perguntas IIS / NGINX / Apache e configs na borda (`tools`: Read, Grep) |
| `backend-specialist` | Alinhar contratos HTTP com a app atrás do proxy |

## Relacionado

- Segurança HTTP/API na app: [`.claude/kb/app_security/`](../app_security/index.md)
- Arquitetura geral: [`.claude/kb/architecture/`](../architecture/index.md)
