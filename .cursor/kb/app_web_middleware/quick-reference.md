# Middleware web — referência rápida

> Consultas rápidas. Detalhes nos conceitos e padrões ligados.

## Por sistema operativo

| SO | Servidor típico | Função principal na borda |
|----|-----------------|---------------------------|
| Windows | **IIS** | Site + *bindings* (HTTP/S), integração com stack Microsoft, extensões (ex. ARR como *reverse proxy*) |
| Linux | **NGINX** | Alto débito, *reverse proxy*, TLS, estáticos, *upstream* com balanceamento |
| Linux | **Apache httpd** | VirtualHost, `mod_proxy`, ecossistema de módulos, `.htaccess` (quando activo) |

## Papéis na camada

| Papel | Descrição curta |
|-------|-----------------|
| Terminação TLS | HTTPS cliente ↔ HTTP interno (ou TLS *end-to-end*) |
| *Reverse proxy* | Encaminha para portas Unix/TCP da app (*upstream*) |
| Servir estáticos | Arquivos públicos sem passar pela app |
| Compressão / cache | `gzip`/`brotli`, cabeçalhos de cache (com política explícita) |

## Cabeçalhos úteis (*upstream*)

| Cabeçalho | Motivo |
|-----------|--------|
| `X-Forwarded-For` | IP original do cliente |
| `X-Forwarded-Proto` | `https` vs `http` visto pelo cliente |
| `Host` | Manter *virtual host* correto na app |

## Matriz de decisão

| Cenário | Tendência |
|---------|-----------|
| Stack .NET no Windows, integração AD/IIS | IIS como frente ou atrás de ARR |
| API Node/Java atrás de Linux, muitas conexões | NGINX |
| Equipa já padronizada em Apache, módulos legados | Apache httpd |

## Armadilhas

| Evitar | Preferir |
|--------|------------|
| Expor porta da app diretamente à Internet sem TLS na borda | TLS na borda ou *passthrough* documentado + firewall |
| *Timeouts* desalinhados (proxy vs app) | Ajustar `proxy_read_timeout` / equivalentes e da app |
| Confiar só no IP sem validar `X-Forwarded-*` | Rede confiável entre proxy e app + documentação de cabeçalhos |

## Ligações

| Tópico | Caminho |
|--------|---------|
| Visão geral | `concepts/camada-middleware-aplicacao.md` |
| Índice completo | `index.md` |
