# Reverse proxy para *upstream* da aplicação

> **Propósito**: Padrão reutilizável para expor uma app atrás de IIS, NGINX ou Apache com cabeçalhos e *timeouts* coerentes.  
> **MCP validado**: não aplicável

## Quando usar

- A app escuta apenas em **localhost** ou rede interna e não deve ser exposta diretamente.
- É necessário **TLS na borda**, compressão ou divisão estático/API no mesmo hostname.
- Vários serviços internos precisam do mesmo **nome público** com roteamento por caminho ou subdomínio.

## Contratos com a aplicação

| Item | Acordo |
|------|--------|
| Esquema percebido | A app deve usar `X-Forwarded-Proto` (ou equivalente) para gerar URLs absolutas e cookies `Secure` |
| IP cliente | Confiar em `X-Forwarded-For` apenas de redes onde só o proxy escreve esse cabeçalho |
| *Health check* | Caminho dedicado (ex. `/health`) com resposta rápida e sem dependências pesadas |

## NGINX (exemplo ilustrativo)

```nginx
upstream app_backend {
    server 127.0.0.1:3000;
    keepalive 32;
}

server {
    listen 443 ssl;
    server_name api.exemplo.internal;

    location / {
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 60s;
        proxy_pass http://app_backend;
    }
}
```

## Apache httpd (exemplo ilustrativo)

```apache
<VirtualHost *:443>
    ServerName api.exemplo.internal
    SSLEngine on
    ProxyPreserveHost On
    RequestHeader set X-Forwarded-Proto "https"
    ProxyPass / http://127.0.0.1:3000/
    ProxyPassReverse / http://127.0.0.1:3000/
</VirtualHost>
```

## IIS (orientação)

- Com **ARR**, criar *server farm* apontando para o *host:port* da app e regra de *reverse proxy* no site.
- Garantir que a app recebe **Host** e protocolo corretos (URL Rewrite / ARR conforme versão).
- Validar **failed request tracing** para 502 intermitentes.

## Configuração — parâmetros típicos

| Definição | Valor típico | Nota |
|-----------|--------------|------|
| `proxy_read_timeout` / equivalente | 60–300 s | APIs longas vs UX |
| `client_max_body_size` / `LimitRequestBody` | conforme API | *Uploads* grandes |
| *Keep-alive* para *upstream* | ativado | Reduz latência sob carga |

## Ver também

- [hardening-borda-checklist.md](hardening-borda-checklist.md)
- [../concepts/camada-middleware-aplicacao.md](../concepts/camada-middleware-aplicacao.md)
