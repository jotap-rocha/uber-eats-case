# Microsoft Teams — notificações (ambiente Icatu)

> **Propósito:** padronizar envio de mensagens ao **Microsoft Teams** a partir de **Databricks** (notebooks, jobs, pipelines PySpark) e desenvolvimento local, usando webhooks do time e a biblioteca **`pymsteams`**.
> **MCP Validated:** 2026-05-26
> **Confiança geral:** 0.92 (connectors legados em transição para Workflows — ver conceito de migração)

## Quando usar esta KB

- Alertar canal operacional quando um **job falha** ou quando um **DataFrame está vazio** (regra de negócio).
- Resolver **qual URL de webhook** usar (`URL_WEBHOOK_SENTINEL`, Trilha de Auditoria, etc.).
- Instalar `pymsteams` em **runtime** no Databricks sem quebrar o cluster.
- Evitar vazar segredos, PII ou mensagens duplicadas.

## Navegação

| Seção | Arquivo | Uso |
|-------|---------|-----|
| Quick reference | [quick-reference.md](quick-reference.md) | Consulta rápida no dia a dia |
| pymsteams + Databricks | [concepts/pymsteams-e-databricks.md](concepts/pymsteams-e-databricks.md) | `%pip`, restart, limites da lib |
| Webhooks do ambiente | [concepts/webhooks-ambiente-icatu.md](concepts/webhooks-ambiente-icatu.md) | Chaves `.env`, Sentinel, Trilha |
| Migração Connectors → Workflows | [concepts/migracao-connectors-workflows.md](concepts/migracao-connectors-workflows.md) | Aposentadoria O365 Connectors |
| Instalação e secrets | [patterns/instalacao-e-secrets.md](patterns/instalacao-e-secrets.md) | Databricks Secrets vs `.env` |
| Alerta a partir de DataFrame | [patterns/notificar-a-partir-de-dataframe.md](patterns/notificar-a-partir-de-dataframe.md) | Padrão Trilha / tabela Markdown |
| Falha de pipeline | [patterns/falha-de-pipeline.md](patterns/falha-de-pipeline.md) | `except` + card vermelho |
| Chaves de webhook | [references/chaves-webhook-env.md](references/chaves-webhook-env.md) | Mapa `.env.example` |
| Spec machine-readable | [specs/webhook-keys.yaml](specs/webhook-keys.yaml) | Registro para agentes |

## Relacionado

- KB genérica (checklist medalhão, quando o projeto tiver o domínio `data-engineering-practices`): [../data-engineering-practices/patterns/alertas-pipeline-microsoft-teams.md](../data-engineering-practices/patterns/alertas-pipeline-microsoft-teams.md)
- Segredos: [../app_security/concepts/secrets-gestao.md](../app_security/concepts/secrets-gestao.md)

## Agentes sugeridos

| Agente | Caso |
|--------|------|
| `@spark-expert` / `@databricks-data-engineer` | Notebook ou job Databricks |
| `@python-developer` | Refatorar helper reutilizável |
| `@key-oci-expert` | Quando a URL vier de Vault em vez de `.env` |
