# NGINX no Linux

> **Propósito**: Descrever o NGINX como servidor web e *reverse proxy* típico em Linux.  
> **Confiança**: 0.92  
> **MCP validado**: não aplicável

## Visão geral

O **NGINX** usa modelo **event-driven** com baixo consumo por conexão, sendo muito usado para **terminação TLS**, **reverse proxy** e servir **estáticos**. A configuração declarativa concentra-se em directivas `http`, `server` e `location`.

## Blocos essenciais

| Bloco | Papel |
|-------|-------|
| `http` | Contexto global HTTP |
| `server` | Virtual host (hostname, TLS, *listen*) |
| `location` | Regras por caminho ou expressão |
| `upstream` | Grupo de backends com balanceamento |

## Boas práticas (resumo)

- Um arquivo por site ou *include* organizado em `/etc/nginx/conf.d/`.
- TLS moderno: protocols e cipher suites alinhados à política de segurança (documentação oficial NGINX + Mozilla guidelines como referência externa).
- Definir explicitamente **`proxy_set_header`** para `Host`, `X-Forwarded-For`, `X-Forwarded-Proto` quando a app precisa do contexto original.
- Afinar **`proxy_read_timeout`** e **`client_max_body_size`** em função da API.

## SisFraude — certificados TLS no Linux (nginx)

**Fluxo canônico:** o browser acede **`https://<domínio>/`** (nginx na **443**); o nginx serve os estáticos do **`dist/`** e faz **`proxy_pass`** de **`/api`** para **`127.0.0.1:8787`**. A API Express deve usar **`API_LISTEN_HOST=127.0.0.1`** e **`API_TRUST_PROXY=1`**. **Não** configurar `DEV_TLS_*` no Vite quando só o nginx termina TLS (evita dois certificados activos para o mesmo uso).

| Item | Valor |
|------|--------|
| Pasta no servidor | `/etc/nginx/certs/` |
| Certificado / cadeia (PEM) | `Icatu_Seguros_Publico_2048_ano2026.pem` → `ssl_certificate` |
| Chave privada (PEM) | `Icatu_Seguros_Publico_2048.key` → `ssl_certificate_key` |
| Convenção por SO | **Linux:** `.pem` + `.key`. **Windows:** entrega típica em `.crt`; na borda Linux usar PEM em `.pem` + `.key`. |
| Deploy | `npm run stack:prd` (build + API); copiar **`dist/`** para o `root` do nginx; `nginx -t` + reload. |

Exemplo de virtual host no repositório: `deploy/nginx/conf.d/sisfraude.host-install.example.conf`. Não colocar chave privada em `/etc/pki/ca-trust/source/anchors/` (âncoras de CA).

## SisFraude — diferença dev vs prd (proxy `/api`)

| Item | `dev:with-api` (`http://localhost:8443/`) | `stack:prd` + nginx (`https://<domínio>/`) |
|------|-------------------------------------------|-------------------------------------------|
| Quem termina TLS | (nada / Vite opcional) | **nginx** na **443** |
| Quem proxy `/api` | **Vite** (config em `vite.config.ts`) | **nginx** (`location /api`) |
| Quem injeta `Authorization: Bearer` | **Vite** (a partir do `.env`, server-side; não vai ao bundle) | **nginx** (`proxy_set_header Authorization` — Opção A, recomendada) **ou** o **bundle** se `VITE_SISFRAUDE_API_BEARER_TOKEN` for definido antes do `npm run build` (Opção B, legado) |
| Porta da API | sempre `127.0.0.1:8787` | sempre `127.0.0.1:8787` (`DEV_SERVER_PORT=8443` é só a porta do Vite; **não** usar no `proxy_pass`) |
| Timeout do proxy | `1_800_000 ms` hardcoded no Vite | `proxy_read_timeout 1800s; proxy_send_timeout 1800s;` no nginx |

> **Regra de ouro:** `API_PORT = 8787` (Express, sempre PRD) **≠** `DEV_SERVER_PORT = 8443` (Vite, só dev).

## SisFraude — Bearer Token: divergência DEV vs PRD (CRÍTICO para suporte)

O Express valida sempre `SISFRAUDE_API_BEARER_TOKEN` lido do **`.env`**. A diferença está em **quem injeta** o header `Authorization: Bearer …` no pedido HTTP que chega à API.

| Ambiente | Quem injeta | Lê o `.env` automaticamente? |
|---|---|---|
| **DEV** (`npm run dev:with-api`) | **Vite** (proxy `/api` em `vite.config.ts`) | **Sim** — basta editar o `.env` e reiniciar o Vite |
| **PRD** (browser → nginx → Express) | **nginx** (`proxy_set_header Authorization`) | **NÃO** — valor tem que ser **literalmente escrito** no `sisfraude.conf` |

**Sintoma do erro:** **HTTP 401** + `{"ok":false,"error":"Autenticação necessária: envie Authorization: Bearer …"}` mesmo com `.env` correto e `sisfraude-api` a correr.

**Causa raiz:** o nginx é um processo independente e o seu `EnvironmentFile` não inclui o `.env` do projeto. Não há mecanismo de "leitura automática" — o operador tem que manter os dois arquivos em sincronia manualmente.

**Procedimento de rotação:**

> O token é um valor opaco gerado por `openssl rand -hex 32` (32 bytes / 256 bits, codificados em hex → 64 chars `[0-9a-f]`). Não é JWT. Alternativa equivalente: `python3 -c "import secrets; print(secrets.token_hex(32))"`. **Não usar** `-base64` (`+`/`/`/`=` causam escape em `proxy_set_header`).

```bash
NEW=$(openssl rand -hex 32)

# 1) .env (Express valida)
sudo -u trauditapp sed -i.bak -E \
  "s|^SISFRAUDE_API_BEARER_TOKEN=.*|SISFRAUDE_API_BEARER_TOKEN=\"${NEW}\"|" \
  /TRILHAAUDITORIA/workspace/fabiano/fraud-investigator-hub-main/.env

# 2) sisfraude.conf (nginx injeta)
sudo sed -i.bak -E \
  "s|(proxy_set_header\s+Authorization\s+\"Bearer\s+)[^\"]+(\";)|\1${NEW}\2|" \
  /etc/nginx/conf.d/sisfraude.conf

# 3) Restart ordenado (API primeiro, depois nginx)
sudo systemctl restart sisfraude-api
sudo nginx -t && sudo systemctl reload nginx

# 4) Smoke test
bash /TRILHAAUDITORIA/workspace/fabiano/fraud-investigator-hub-main/scripts/prd-smoke.sh
```

> Janela de inconsistência (passos 2-4) ≈ 1-2 s; aceitável em manutenção. Para horário crítico, encadear num único `bash -c '…'` ou `systemd-run`.

**Alternativa (não recomendada — Opção B legado):** definir `VITE_SISFRAUDE_API_BEARER_TOKEN` no `.env` antes do `npm run build`. O token entra no bundle JS público — visível em `/assets/*.js`. Rotação implica rebuild + rsync da SPA inteira.

## SisFraude — `proxy_pass` sem `/` final

O Express monta as rotas em `/api/*` (`server/index.ts` → `app.use("/api/databricks", …)`). Para o caminho original ser preservado, o `proxy_pass` **não pode ter URI** (nem mesmo `/`):

```nginx
# OK — preserva /api/databricks/...
location /api { proxy_pass http://sisfraude_api; }

# ERRADO — substitui /api por "/", o backend recebe /databricks/... e devolve 404
location /api { proxy_pass http://sisfraude_api/; }
```

Sintoma do erro: `404 Not Found` com body `Cannot GET /databricks/...` (sem o prefixo `/api`).

## SisFraude — SELinux em RHEL/AlmaLinux/Rocky

Em SO Red Hat com SELinux em **Enforcing** (default em RHEL 9), o nginx **não tem permissão** para abrir socket TCP para o backend local. Sintoma típico no `/var/log/nginx/error.log`:

```
connect() to 127.0.0.1:8787 failed (13: Permission denied) while connecting to upstream
```

> **`(13: Permission denied)`** = SELinux. **`(111: Connection refused)`** = API caída. Distinção crítica.

Configuração persistente (uma única vez):

```bash
sudo setsebool -P httpd_can_network_connect 1
sudo dnf install -y policycoreutils-python-utils
sudo semanage port -a -t http_port_t -p tcp 8787 \
  || sudo semanage port -m -t http_port_t -p tcp 8787
```

Validação:

```bash
getsebool httpd_can_network_connect          # → on
sudo semanage port -l | grep '^http_port_t' | grep -w 8787
```

> Ambos os comandos são incluídos no `deploy/systemd/install.sh` (idempotente).

## SisFraude — operação em produção (systemd)

A API Express deve correr sob **systemd** em PRD (reinício automático + boot + journal):

- Template: [`deploy/systemd/sisfraude-api.service.template`](../../../../deploy/systemd/sisfraude-api.service.template).
- Instalador (root): `sudo bash deploy/systemd/install.sh` — detecta nvm/PATH, gera a unit a partir do template, aplica SELinux mínimo e dá `enable --now`.
- Smoke test: `bash scripts/prd-smoke.sh` (exit codes distintos por causa: 10 API caída, 20 SELinux, 30 strip `/api`, 40 Bearer ausente, 50/60 Databricks).

## SisFraude — cache do `index.html` (deploy não aparece no browser)

A SPA (Vite) emite assets com **hash no nome** (`/assets/<name>-<hash>.<ext>`) — cache-bust automático. O **`index.html`**, porém, tem nome fixo e mapeia o entry-point para o hash atual. Sem `Cache-Control` explícito, o browser pode servir o `index.html` antigo a partir do cache, e portanto carregar o entry-point antigo, **mesmo após `rsync dist/`** no servidor.

**Sintoma típico no SisFraude:** após `npm run build && rsync dist/ /var/www/sisfraude/`, novos componentes do Login (ex.: gate offline `useApiHealth` + `<ServiceUnavailable />`) **não aparecem** — só após `Ctrl+Shift+R` ou ao fechar/reabrir o tab.

**Regra canônica no `sisfraude.conf`:**

```nginx
location = /index.html {
    add_header Cache-Control "no-cache, no-store, must-revalidate" always;
    add_header Pragma        "no-cache" always;
    add_header Expires       "0" always;
    expires    -1;
}

location ^~ /assets/ {
    expires    1y;
    add_header Cache-Control "public, max-age=31536000, immutable" always;
    access_log off;
    try_files  $uri =404;
}
```

Aplicar: `sudo nginx -t && sudo systemctl reload nginx`.
Validar: `curl -ksI -H "Host: …" https://127.0.0.1/ | grep -i cache-control`.

> A regra `location = /index.html` cobre **também** os fallbacks do SPA (`/dashboard`, `/login`, etc.) porque `try_files … /index.html` dispara um *internal redirect* que volta a entrar no `location = /index.html`. Daí não ser preciso repetir `add_header` em `location /`.

## Erros frequentes

| Sintoma | Causa típica |
|---------|--------------|
| **502** com `(13: Permission denied)` | SELinux a bloquear `connect()` do nginx → boolean `httpd_can_network_connect` + `semanage port` |
| **502** com `(111: Connection refused)` | API caída ou a escutar em outro host (`API_LISTEN_HOST`) |
| **502** com `127.0.0.1:8443 failed` | `proxy_pass` aponta para a porta do Vite dev em vez de `:8787` |
| **404** + `Cannot GET /databricks/...` | `proxy_pass http://…/;` com `/` final faz strip do `/api` |
| **401** + `Autenticação necessária` | Bearer ausente — injetar no nginx (Opção A) ou rebuild (Opção B). **Nota:** o nginx **NÃO lê o `.env`** — o token tem que estar literal no `sisfraude.conf`. Ver seção «Bearer Token: divergência DEV vs PRD» |
| **200** mas SPA antiga após `rsync dist/` | `index.html` sem `Cache-Control: no-cache` — browser cacheia o entry antigo |
| **504** Gateway Timeout | `proxy_read_timeout` < duração da query Databricks (subir para `1800s`) |
| **413** Request Entity Too Large | `client_max_body_size` muito baixo (subir para `25m`) |
| *Loop* de redirecionamento HTTPS | `X-Forwarded-Proto` não está correto |

## Relacionado

- [camada-middleware-aplicacao.md](camada-middleware-aplicacao.md)
- [../patterns/reverse-proxy-upstream.md](../patterns/reverse-proxy-upstream.md)
- [../patterns/hardening-borda-checklist.md](../patterns/hardening-borda-checklist.md)
