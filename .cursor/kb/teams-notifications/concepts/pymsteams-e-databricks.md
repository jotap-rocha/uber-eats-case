# pymsteams no Databricks

> **Confiança:** 0.92 · **MCP Validated:** 2026-05-26

## Ainda é necessário `pip install pymsteams` em tempo de execução?

**Sim**, para notebooks e jobs que **não** incluem `pymsteams` na imagem do cluster ou na biblioteca do job.

| Cenário | Instalação |
|---------|------------|
| Notebook interativo | `%pip install pymsteams` na primeira célula, depois **Restart Python** |
| Job com dependência declarada | Adicionar `pymsteams` em `libraries` do job ou `requirements.txt` do wheel — **sem** `%pip` em cada run |
| DLT / pipeline só SQL | Preferir **webhook no Job** que dispara o pipeline (sem Python) ou task separada de notificação |

A biblioteca **não** vem pré-instalada no runtime Databricks padrão. O pacote no PyPI permanece disponível (`pymsteams`, última release estável conhecida: 0.2.x / 0.1.15 conforme ambiente).

### Por que reiniciar o Python após `%pip`?

O interpretador já iniciado **não** recarrega módulos instalados no meio da sessão. Sem restart, é comum:

```text
ModuleNotFoundError: No module named 'pymsteams'
```

No Databricks: **Restart Python** no notebook ou reiniciar o cluster (jobs agendados costumam iniciar sessão limpa após a task de install, se existir).

## O que o pymsteams faz

- Envia **Connector Cards** (MessageCard) para uma **URL de Incoming Webhook**.
- API principal: `pymsteams.connectorcard(webhook_url)` → `.title()`, `.text()`, `.color()`, `.send()`.
- Em falha HTTP, lança `TeamsWebhookException`; o objeto expõe `last_http_status` para diagnóstico.

## Limitações importantes

1. **Connectors O365 em aposentadoria** — a URL antiga “Incoming Webhook” pode deixar de funcionar; o time deve validar se o canal já usa **Workflows** (ver [migracao-connectors-workflows.md](migracao-connectors-workflows.md)).
2. **Tamanho da mensagem** — textos muito longos (tracebacks enormes, milhares de linhas de tabela) podem ser truncados ou rejeitados; preferir resumo + link para log do job.
3. **`df.collect()`** — traz todas as linhas para o driver; usar só para alertas com **poucas** linhas (ver [../patterns/notificar-a-partir-de-dataframe.md](../patterns/notificar-a-partir-de-dataframe.md)).
4. **`verify=False` em HTTPS** — alguns ambientes corporativos usam inspeção SSL; é um **workaround** de rede, não boa prática de segurança global. Documentar exceção com aprovacao de infra se necessário.

## Alternativas (quando pymsteams não bastar)

| Abordagem | Quando |
|-----------|--------|
| `requests.post(webhook_url, json=...)` com payload **Adaptive Card** | Workflow Teams exige JSON específico |
| Notificação nativa do **Job Databricks** (`email_notifications` / `webhook_notifications` no bundle) | Falha do job inteiro, sem lógica no notebook |
| Logic App / Power Automate | Integração corporativa centralizada |
