# Few-shot — `web.config` com URL Rewrite (IIS)

> **Propósito**: Modelo **interno aprovado para revisão** — redirecionamento HTTP→HTTPS e *stub* de *reverse proxy* (ARR). Substituir hosts, portas e thumbprints pelos valores do ambiente.  
> **MCP validado**: não aplicável

## Quando usar

- Novo *site* IIS precisa de forçar HTTPS na borda.
- Base para estender regras (ex. ARR — Application Request Routing) sobre este arquivo.

## Pré-requisitos

- Módulo **URL Rewrite** instalado.
- Para *proxy* reverso: **ARR** + *proxy* habilitado ao nível do servidor (conforme política).

## Exemplo — redirecionar tudo para HTTPS

Colocar na raiz da aplicação ou no *site* (ajustar `web.config` conforme deploy):

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.webServer>
    <rewrite>
      <rules>
        <rule name="RedirectToHttps" stopProcessing="true">
          <match url="(.*)" />
          <conditions>
            <add input="{HTTPS}" pattern="off" ignoreCase="true" />
          </conditions>
          <action type="Redirect" url="https://{HTTP_HOST}/{R:1}" redirectType="Permanent" />
        </rule>
      </rules>
    </rewrite>
    <!-- Opcional: remover cabeçalho Server em políticas mais estritas (módulo ou outboundRules) -->
  </system.webServer>
</configuration>
```

## Exemplo — encaminhar `/api` para *upstream* (ARR)

Requer **Application Request Routing** e servidor de destino registado na *farm*. Valores ilustrativos:

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.webServer>
    <rewrite>
      <rules>
        <rule name="ReverseProxyApi" stopProcessing="true">
          <match url="^api/(.*)" />
          <action type="Rewrite" url="http://127.0.0.1:3000/{R:1}" />
          <serverVariables>
            <set name="HTTP_X_FORWARDED_PROTO" value="https" />
            <set name="HTTP_X_ORIGINAL_HOST" value="{HTTP_HOST}" />
          </serverVariables>
        </rule>
      </rules>
    </rewrite>
  </system.webServer>
</configuration>
```

**Nota:** variáveis de servidor como `HTTP_X_FORWARDED_PROTO` podem exigir entrada na lista permitida no IIS (`Allowed Server Variables`). Validar na documentação Microsoft para a sua versão.

## Erros frequentes

- *Loop* de redirecção quando o *load balancer* já envia HTTPS mas `{HTTPS}` aparece como `off` — usar cabeçalho do balanceador ou ARR corretamente.
- Regra de *proxy* sem `stopProcessing` e conflito com arquivos estáticos.

## Ver também

- [../concepts/iis-windows.md](../concepts/iis-windows.md)
- [reverse-proxy-upstream.md](reverse-proxy-upstream.md)
