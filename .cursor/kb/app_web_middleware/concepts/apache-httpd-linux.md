# Apache httpd no Linux

> **Propósito**: Referência breve do Apache HTTP Server (*httpd*) como camada web em Linux.  
> **Confiança**: 0.90  
> **MCP validado**: não aplicável

## Visão geral

O **Apache httpd** serve HTTP(S) com modelo baseado em **MPM** (*prefork*, *worker*, *event* — conforme pacote e SO). A separação por **VirtualHost** permite múltiplos sites no mesmo daemon. O encaminhamento para a app usa frequentemente **`mod_proxy`** e **`mod_proxy_http`** (ou `mod_proxy_uwsgi` / *sockets*).

## Componentes úteis

| Peça | Função |
|------|--------|
| `VirtualHost` | IP/porta/nome de servidor |
| `ProxyPass` / `ProxyPassReverse` | *Reverse proxy* para *upstream* |
| `mod_ssl` | HTTPS e parâmetros TLS |
| `.htaccess` | Overrides por pasta (impacto em performance — preferir config principal quando possível) |

## Boas práticas (resumo)

- Preferir configuração em **`conf-available` / `sites-available`** (Debian/Ubuntu) ou equivalente com ativação explícita.
- Manter **`ServerName`** e **`ServerAlias`** coerentes com certificados e DNS.
- Com `mod_proxy`, definir cabeçalhos encaminhados (`X-Forwarded-*`) alinhados com a app.
- Monitorizar **slots** do MPM sob carga (ligações vs workers disponíveis).

## Anti-padrões

- Centenas de rewrites em `.htaccess` sem revisão.
- **ProxyPass** para destino errado em ambientes (copiar config de PRD para DEV sem alterar *upstream*).

## Relacionado

- [camada-middleware-aplicacao.md](camada-middleware-aplicacao.md)
- [nginx-linux.md](nginx-linux.md) — comparação de uso típico na mesma camada
- [../patterns/reverse-proxy-upstream.md](../patterns/reverse-proxy-upstream.md)
