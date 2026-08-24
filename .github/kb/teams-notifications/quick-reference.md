# Quick Reference — Teams (Icatu)

## Instalação (Databricks)

```python
%pip install pymsteams
# Reiniciar Python na sessão (Databricks: Restart Python / reiniciar cluster se necessário)
```

## URL do webhook (local)

| Variável `.env` | Uso típico |
|-----------------|------------|
| `URL_WEBHOOK_SENTINEL` | Alertas **Sentinel** / monitorização operacional |
| `URL_WEBHOOK_TRILHA_AUDITORIA_DSV` | Trilha de Auditoria — **DSV** |
| `URL_WEBHOOK_TRILHA_AUDITORIA_PRD` | Trilha de Auditoria — **PRD** |
| `URL_TRILHA_DSV_NOVO` | Canal alternativo Trilha (DSV) |

Copiar valores de `.env.example` → `.env` (`.env` no `.gitignore`).

## Envio mínimo

```python
import os
import pymsteams

url = os.environ["URL_WEBHOOK_SENTINEL"].strip()
card = pymsteams.connectorcard(url)
card.title("Título")
card.text("Corpo da mensagem")
card.send()
```

## Regras rápidas

| Fazer | Evitar |
|-------|--------|
| Webhook só em `.env` / Databricks Secret | URL no Git |
| `collect()` só com **poucas** linhas para o card | `df.collect()` em DataFrame grande |
| Canal **DSV** ≠ canal **PRD** | Mesmo webhook em todos os ambientes |
| Testar com mensagem "ping" | PII (CPF completo) em canal amplo sem política |

## Troubleshooting

| Sintoma | Ação |
|---------|------|
| `ModuleNotFoundError: pymsteams` | Rodar `%pip install` + **Restart Python** |
| HTTP 4xx no `send()` | URL expirada ou connector migrado → ver [migracao-connectors-workflows.md](concepts/migracao-connectors-workflows.md) |
| Mensagem não aparece | Ver `card.last_http_status` (atributo pymsteams) |
| SSL / certificado corporativo | Ver nota `verify=False` em [notificar-a-partir-de-dataframe.md](patterns/notificar-a-partir-de-dataframe.md) |
