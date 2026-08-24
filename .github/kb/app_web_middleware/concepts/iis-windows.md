# IIS (Internet Information Services) no Windows

> **Propósito**: Referência concisa do IIS como camada web em Windows Server para sites e aplicações.  
> **Confiança**: 0.90  
> **MCP validado**: não aplicável

## Visão geral

O **IIS** é o servidor web da Microsoft. Expõe **sites** com **bindings** (combinação de IP, porta, protocolo e hostname). Aplicações ASP.NET Core podem integrar-se via módulo *hosting* ou correr atrás do IIS como *reverse proxy* (ex. **ARR** — Application Request Routing) para outras stacks.

## Conceitos principais

| Conceito | Descrição |
|----------|-----------|
| Site | Raiz lógica com caminho físico ou reencaminhamento |
| *Application Pool* | Processo worker isolado (versão CLR / pipeline) |
| *Binding* | HTTP/HTTPS, SNI com certificado no HTTPS |
| *web.config* | Configuração XML por site ou pasta |

## Quando usar IIS na borda

- Implementações **.NET** em Windows alinhadas às ferramentas Microsoft.
- Requisitos de **integração** com autenticação Windows ou políticas corporativas já centradas em IIS.
- Necessidade de **ARR** ou regras de URL centralizadas na camada Windows.

## Boas práticas (resumo)

- **Menor privilégio** para identidade do *application pool*.
- **HTTPS** obrigatório para tráfego externo; redireccionar HTTP→HTTPS com regra clara.
- **Separar** ambientes (DEV/TST/PRD) por site ou servidor conforme política.
- **Logs**: W3C logging activo com rotação; correlacionar com logs da app.

## Anti-padrões

- *Application pool* com identidade **demasiado privilegiada**.
- Certificados manuais sem alerta de expiração.
- Expor **gestão remota** do IIS sem rede e ACL restritas.

## Relacionado

- [camada-middleware-aplicacao.md](camada-middleware-aplicacao.md)
- [../patterns/reverse-proxy-upstream.md](../patterns/reverse-proxy-upstream.md)
- Segurança: [../../app_security/concepts/apis-seguras.md](../../app_security/concepts/apis-seguras.md)
