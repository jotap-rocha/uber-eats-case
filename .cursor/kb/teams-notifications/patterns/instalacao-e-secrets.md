# Padrão: instalação e gestão de secrets

> **Confiança:** 0.95

## Fluxo recomendado no Databricks (notebook)

```python
# Célula 1 — dependência (uma vez por sessão ou por job)
%pip install pymsteams

# Célula 2 — após Restart Python
import os

import pymsteams

# Preferir secret em PRD; em dev local, os.environ após dotenv
try:
    webhook_url = dbutils.secrets.get("SCOPE", "URL_WEBHOOK_SENTINEL")
except Exception:
    webhook_url = os.environ["URL_WEBHOOK_SENTINEL"].strip()

def send_teams_text(title: str, body: str, *, color: str | None = None) -> None:
    card = pymsteams.connectorcard(webhook_url)
    card.title(title)
    if color:
        card.color(color)
    card.text(body)
    card.send()
```

## Job agendado (sem `%pip` em todo run)

Declarar biblioteca no **Databricks Asset Bundle** ou no job:

```yaml
libraries:
  - pypi:
      package: pymsteams>=0.2.0
```

Ou empacotar em `requirements.txt` do wheel do projeto.

## Matriz ambiente × secret

| Ambiente | URL da Trilha | URL Sentinel |
|----------|---------------|--------------|
| DSV | `URL_WEBHOOK_TRILHA_AUDITORIA_DSV` | `URL_WEBHOOK_SENTINEL` (canal de teste se existir) |
| PRD | `URL_WEBHOOK_TRILHA_AUDITORIA_PRD` | `URL_WEBHOOK_SENTINEL` |

Nunca commitar `.env` com valores reais.

## Teste de conectividade

```python
send_teams_text("Teste KB teams-notifications", "Ping — pode ignorar.")
```

Se falhar, inspecionar `card.last_http_status` antes de reexecutar o pipeline.
