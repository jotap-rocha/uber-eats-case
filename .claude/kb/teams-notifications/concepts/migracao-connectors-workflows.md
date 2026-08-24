# Migração: O365 Connectors → Teams Workflows

> **Confiança:** 0.88 · **MCP Validated:** 2026-05-26

## Contexto

A Microsoft está **aposentando** os **Office 365 Connectors** (Incoming Webhook clássico no Teams). O `pymsteams` foi desenhado para esse tipo de endpoint (MessageCard / Connector Card).

Referências oficiais:

- [Retirement of Office 365 connectors within Microsoft Teams](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/)

Prazos e detalhes mudam; **validar com infraestrutura** se as URLs em `.env` ainda são connectors legados ou já apontam para **Workflows** (“Post to a channel when a webhook request is received”).

## Impacto no time

| Situação | O que fazer |
|----------|-------------|
| Webhook antigo ainda funciona | Manter `pymsteams` + monitorar comunicados de TI |
| HTTP 410 / mensagem de connector desativado | Migrar URL para Workflow; pode exigir **Adaptive Card** em JSON |
| Novo canal | Criar **Workflow**, não “Incoming Webhook” legado |

## pymsteams após migração

- Se o novo endpoint aceitar o mesmo formato **MessageCard**, o código pode **continuar igual**.
- Se o Workflow exigir **Adaptive Card**, usar `requests.post` com payload documentado pelo template do Power Automate, ou adaptador interno.

## Checklist com infra

1. Confirmar tipo de URL de cada chave (`URL_WEBHOOK_SENTINEL`, Trilha, etc.).
2. Testar `card.send()` com mensagem “ping”.
3. Registrar data limite de migração corporativa.
4. Atualizar esta KB quando a URL base mudar.
