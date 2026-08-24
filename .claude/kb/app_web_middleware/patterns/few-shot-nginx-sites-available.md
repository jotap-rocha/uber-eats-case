# Few-shot — NGINX `sites-available` (Debian/Ubuntu)

> **Propósito**: Arquivo de *site* **completo** para revisão única — TLS + *upstream* para API Node/.NET/Java atrás de `127.0.0.1`. Ajustar paths de certificado e nomes.  
> **MCP validado**: não aplicável

## Quando usar

- Activar com `ln -s /etc/nginx/sites-available/app-api /etc/nginx/sites-enabled/` após `nginx -t`.
- Substituir `api.exemplo.internal` e paths `/etc/ssl/certs/...` pelos valores reais.
- **WebSocket** (Vite HMR, chat, etc.): manter este arquivo só HTTP/API; adicionar `map $http_upgrade $connection_upgrade` no `http {}` e *location* para `/ws` conforme [nginx-websocket-proxy-map.md](nginx-websocket-proxy-map.md).

## Arquivo sugerido: `/etc/nginx/sites-available/app-api`

```nginx
# Upstream da aplicação (porta interna)
upstream app_api_upstream {
    server 127.0.0.1:3000;
    keepalive 32;
}

# Redireccionar HTTP → HTTPS
server {
    listen 80;
    listen [::]:80;
    server_name api.exemplo.internal;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name api.exemplo.internal;

    # Certificados — substituir pelos paths da PKI / Let's Encrypt
    ssl_certificate     /etc/ssl/certs/api.exemplo.internal.fullchain.pem;
    ssl_certificate_key /etc/ssl/private/api.exemplo.internal.key;

    # Baseline TLS (ajustar à política de segurança)
    ssl_protocols TLSv1.2 TLSv1.3;

    add_header X-Content-Type-Options nosniff always;

    client_max_body_size 25m;

    location / {
        proxy_http_version 1.1;
        proxy_set_header Host              $host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Connection "";

        proxy_read_timeout 120s;
        proxy_connect_timeout 10s;
        proxy_send_timeout 120s;

        proxy_pass http://app_api_upstream;
    }

    location /health {
        access_log off;
        default_type text/plain;
        return 200 "ok\n";
    }
}
```

## Pós-instalação

```bash
sudo nginx -t && sudo systemctl reload nginx
```

## Ver também

- [../concepts/nginx-linux.md](../concepts/nginx-linux.md)
- [reverse-proxy-upstream.md](reverse-proxy-upstream.md)
- [hardening-borda-checklist.md](hardening-borda-checklist.md)
