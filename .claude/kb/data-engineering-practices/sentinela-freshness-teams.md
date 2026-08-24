# Pattern — Sentinela freshness + Teams

> **Quando usar:** SLA de dados (ex. Gold deve ter ingestão nos últimos N dias).

## Componentes

| Peça | Função |
|------|--------|
| Job independente | Não bloqueia DLT; corre em schedule próprio |
| Query Gold | `max(_ingest_ts)` ou métrica equivalente |
| Threshold | Configurável (`sentinela_stale_days`, default 3) |
| Teams | Card laranja conciso se stale; job termina OK (formato TM-M06) |

## Configuração bundle

```yaml
varonis.sentinela_enabled: "true"
varonis.sentinela_stale_days: "3"
```

## Webhooks

- DSV → `URL_WEBHOOK_{PROJETO}_DSV`
- PRD → `URL_WEBHOOK_{PROJETO}_PRD`

## Smoke test

Antes de PRD, validar webhook com notebook `smoke_test_teams_*.py`.

## Referência

Varonis: `sentinela/freshness.py`, job `sentinela_gold_freshness`, contrato §5.5.
