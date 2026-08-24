# NGINX — WebSockets atrás do *reverse proxy* (`map` + `Upgrade`)

> **Propósito**: Pattern **separado** do few-shot `sites-available` — define `map $http_upgrade $connection_upgrade` no contexto `http {}` e headers `Upgrade` / `Connection` só nas *locations* WebSocket.  
> **MCP validado**: não aplicável

## Quando usar

- SPA com hot-reload (Vite/Webpack), *live* logs, chat em tempo real ou qualquer serviço que eleve HTTP a WebSocket (`Connection: Upgrade`).
- Manter [few-shot-nginx-sites-available.md](few-shot-nginx-sites-available.md) sem WebSocket (HTTP/API apenas).

## 1. Bloco `map` no `http {}`

Colocar **uma vez** em `nginx.conf` (ou fragmento incluído por `include /etc/nginx/conf.d/*.conf` **antes** dos `server` que precisem do mapa):

```nginx
map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;
}
```

| Variável | Comportamento |
|----------|----------------|
| Pedido **sem** `Upgrade` | `$connection_upgrade` = `close` — evita *upstream* “pendurado”. |
| Pedido **com** WebSocket | `$connection_upgrade` = `upgrade`. |

## 2. `location` para WebSocket

Exemplo: *upstream* HTTP na mesma app na porta `3000`, caminho `/ws`:

```nginx
upstream app_ws_upstream {
    server 127.0.0.1:3000;
    keepalive 32;
}

server {
    listen 443 ssl http2;
    server_name api.exemplo.internal;

    # ... ssl_certificate, ssl_certificate_key ...

    location /ws {
        proxy_http_version 1.1;
        proxy_set_header Host               $host;
        proxy_set_header X-Real-IP          $remote_addr;
        proxy_set_header X-Forwarded-For    $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto  $scheme;
        proxy_set_header Upgrade            $http_upgrade;
        proxy_set_header Connection         $connection_upgrade;
        proxy_read_timeout 86400;
        proxy_pass http://app_ws_upstream;
    }

    location / {
        proxy_http_version 1.1;
        proxy_set_header Host               $host;
        proxy_set_header X-Forwarded-For    $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto  $scheme;
        proxy_set_header Connection         "";
        proxy_pass http://app_ws_upstream;
    }
}
```

**Timeouts:** WebSockets longos — subir `proxy_read_timeout` (ex. `86400`) só onde necessário.

## 3. Armadilhas

| Problema | Causa típica |
|----------|----------------|
| `502` ao subir WS | Falta `map` ou `proxy_set_header Upgrade` / `Connection`. |
| WS funciona mas HTTP normal falha | `Connection upgrade` em **todas** as *locations* sem `map` — usar `Connection ""` no REST como no few-shot base. |
| *Sticky session* | Se vários *upstreams*, pode ser preciso *ip_hash* ou sessão na app — fora do âmbito deste snippet. |

## Ver também

- [few-shot-nginx-sites-available.md](few-shot-nginx-sites-available.md)
- [reverse-proxy-upstream.md](reverse-proxy-upstream.md)
