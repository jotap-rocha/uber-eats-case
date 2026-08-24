# Camada de middleware na borda da aplicação

> **Propósito**: Definir o que se entende por “middleware” na **borda HTTP** (servidor web / *reverse proxy*) e como se relaciona com a aplicação.  
> **Confiança**: 0.92  
> **MCP validado**: não aplicável

## Visão geral

Neste contexto, **middleware de aplicação na borda** é o software que recebe pedidos HTTP(S) dos clientes e decide o que fazer a seguir: servir arquivos estáticos, terminar TLS, aplicar políticas (compressão, *rate limit* na borda) e encaminhar para o processo da aplicação (*upstream*). Não confundir com *middleware* interno de frameworks (ex. pipeline ASP.NET ou Express), que corre **dentro** do processo da app.

Fluxo típico: **Cliente → TLS → servidor web/proxy → aplicação** (porta interna ou *socket*).

## Responsabilidades comuns

| Área | Na borda | Na aplicação |
|------|----------|--------------|
| TLS / certificados | Terminação ou *passthrough* | Opcional *mTLS* interno |
| Autenticação de usuário | SSO na borda (opcional) | Sessão, JWT, cookies |
| Autorização de negócio | Raramente | Regra de domínio |
| Logs de acesso | Log por pedido (*access log*) | Logs de negócio / correlação |
| Limite de corpo / tempo | Limites de conexão e *timeout* | Validação de payload |

## Escolha por ambiente

- **Windows Server**: **IIS** é o padrão para hospedar sites e aplicações integradas ao ecossistema Microsoft; *reverse proxy* avançado pode usar extensões como ARR.
- **Linux**: **NGINX** e **Apache httpd** são as opções mais frequentes; NGINX é comum para *reverse proxy* e alto paralelismo; Apache para cenários com módulos e configuração por VirtualHost.

## Referência rápida

| Termo | Significado |
|-------|-------------|
| *Upstream* | Serviço da app (porta local, Unix *socket*) |
| *Binding* (IIS) | IP + porta + protocolo + certificado |
| VirtualHost (Apache) | Múltiplos nomes no mesmo processo |
| `server` block (NGINX) | Equivalente lógico ao VirtualHost |

## Erros frequentes

- Tratar o proxy como “caixa preta” sem alinhar **cabeçalhos encaminhados** (`X-Forwarded-*`, `Host`) com o que a app espera.
- **Timeouts** só ajustados num lado — cliente vê 502/504 sem diagnóstico claro.
- **TLS** na borda com cipher suites obsoletos ou certificados não renovados por automatismo.

## Relacionado

- [iis-windows.md](iis-windows.md)
- [nginx-linux.md](nginx-linux.md)
- [apache-httpd-linux.md](apache-httpd-linux.md)
- [../patterns/reverse-proxy-upstream.md](../patterns/reverse-proxy-upstream.md)
