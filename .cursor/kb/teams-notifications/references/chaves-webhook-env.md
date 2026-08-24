# Referência: chaves de webhook no `.env`

Arquivo modelo: **`.env.example`** na raiz do repositório.

| Chave | Ambiente | Finalidade |
|-------|----------|------------|
| `URL_WEBHOOK_SENTINEL` | Geral (tipicamente PRD; confirmar com ops) | Alertas Sentinel / monitorização |
| `URL_WEBHOOK_TRILHA_AUDITORIA_DSV` | DSV | Trilha de Auditoria — testes |
| `URL_WEBHOOK_TRILHA_AUDITORIA_PRD` | PRD | Trilha de Auditoria — produção |
| `URL_TRILHA_DSV_NOVO` | DSV | Webhook alternativo Trilha |

## Procedimento para novo desenvolvedor

1. Copiar `.env.example` → `.env`.
2. Colar URLs fornecidas pelo time (Teams / infra).
3. Confirmar que `.env` está no `.gitignore`.
4. Rodar ping de teste (ver [../patterns/instalacao-e-secrets.md](../patterns/instalacao-e-secrets.md)).

## Mapeamento para Databricks Secrets (sugestão)

| Variável `.env` | Secret key (exemplo) |
|-----------------|----------------------|
| `URL_WEBHOOK_SENTINEL` | `url_webhook_sentinel` |
| `URL_WEBHOOK_TRILHA_AUDITORIA_PRD` | `url_webhook_trilha_auditoria_prd` |

O scope é definido por plataforma (ex.: `varonis`, `sql-capacity`).
