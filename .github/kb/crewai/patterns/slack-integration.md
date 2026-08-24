# Padrão: Slack (resumos e alertas)

> **Problema:** stakeholders precisam de notificação sem expor prompts ou dados sensíveis.
> **MCP validado:** 2026-04-13

## Quando usar

- Pós-processamento do `crew.kickoff()` (recomendado): enviar só **sumário** aprovado.
- Ou **tool** dedicada `post_to_slack(channel, text)` com allowlist de canais.

## Implementação

```python
import os
from slack_sdk import WebClient  # exemplo

def notify_summary(result_text: str):
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    client.chat_postMessage(
        channel=os.environ["SLACK_INCIDENT_CHANNEL"],
        text=result_text[:3000],  # limite Slack
    )
```

## Configuração

| Definição | Nota |
|-----------|------|
| Conteúdo | Nunca enviar credenciais ou dumps completos. |
| Allowlist | `channel` fixo por ambiente (dev/staging/prod). |

## Ver também

- [triage-investigation-report.md](triage-investigation-report.md)
