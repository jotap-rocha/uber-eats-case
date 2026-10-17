---
domain: aws-redshift
description: Amazon Redshift Serverless como warehouse — namespace/workgroup, base RPU mínimo (4), crédito de trial US$ 300, COPY do S3 com IAM role, MERGE para SCD2, controle de custo (base/max RPU, usage limits) e por que não provisionado nem Athena
mcp_validated: "2026-10-16"
confidence: 0.85
---

# KB: Amazon Redshift Serverless

Paridade com `azure-synapse` (Dedicated SQL Pool): mesmo papel, mesmos tópicos — carga em
massa, MERGE/SCD2, custo e "pausa".

## Papel

`role: warehouse` — data warehouse analítico gerenciado: recebe a camada curada do S3 via
`COPY`, aplica `MERGE` (SCD1/SCD2) e serve SQL para BI. Sem cluster para dimensionar:
paga RPU-hora só quando há query rodando.

## Capability map

| Pergunta | Onde achar |
|---|---|
| Namespace × workgroup, rede, RPU? | [concepts/serverless-model.md](concepts/serverless-model.md) |
| Como controlar custo (base/max RPU, usage limit)? | [concepts/cost-controls.md](concepts/cost-controls.md) |
| Carga em massa do S3 (`COPY` + IAM role)? | [patterns/bulk-load.md](patterns/bulk-load.md) |
| SCD2 com `MERGE`? | [patterns/merge-scd2.md](patterns/merge-scd2.md) |
| Cheatsheet? | [quick-reference.md](quick-reference.md) |

## Custo e free tier

| Item | Valor (us-east-1, validado 2026-10-16) |
|---|---|
| Compute | **US$ 0,375 por RPU-hora**, cobrança por segundo, **mínimo 60 s** por uso |
| Storage gerenciado | US$ 0,024 / GB-mês |
| **Free trial** | **US$ 300 de crédito, expira em 90 dias** — só para quem nunca usou Redshift Serverless |
| Free Tier da conta (2025) | créditos US$ 100 + até US$ 100; ver `aws-terraform` |

- **O que queima rápido:** base RPU alto. Com base 8 RPU, 1 h de query = 8 × 0,375 =
  **US$ 3/h**; com o default de **128 RPU** = **US$ 48/h**. Sempre fixe `base_capacity`.
- **"Pausar":** não existe pause — workgroup **ocioso não cobra RPU**, só storage. Mas
  qualquer conexão de BI/agendador que rode query "acorda" o compute.
- **Limitar:** `base_capacity = 4|8`, `max_capacity` (teto de RPU) e **usage limit**
  diário em RPU-horas com ação `deactivate` (desliga queries de usuário).
- **Destruir:** `terraform destroy` do workgroup + namespace (snapshot final opcional —
  snapshot também cobra storage).
- **Regra:** criar → testar → destruir no mesmo dia; **AWS Budgets** ativo antes do
  `apply` (ver `aws-terraform/patterns/cost-guardrails.md`).

## SI

- Acesso ao S3 pelo `COPY`: **IAM role associada ao namespace** (`IAM_ROLE default` ou ARN
  com `<AWS_ACCOUNT_ID>`), nunca `ACCESS_KEY_ID`/`CREDENTIALS` com chave no SQL.
- Senha admin: ative o atributo `manage_admin_password` (valor `true`, gerida no Secrets Manager) — nunca em tfvars.
- Workgroup `publicly_accessible = false`; acesso via VPC/SG ou Query Editor v2 com IAM.
- Role do `COPY` com `s3:GetObject`/`s3:ListBucket` **só** no prefixo `curated/`.
- PII: mascaramento via Dynamic Data Masking ou views — nunca em log de query compartilhado.

## Por que este serviço

| Alternativa (AWS) | Por que não aqui |
|---|---|
| Redshift **provisionado** (RA3/DC2) | Cobra por nó-hora mesmo ocioso; pause/resume manual; mínimo de nó caro para lab. Serverless = zero compute ocioso + trial US$ 300 |
| **Athena** | Ótimo para ad-hoc sobre S3, mas sem tabelas gerenciadas com MERGE transacional sobre warehouse (só via Iceberg), cobra por TB lido e não é o "DW com SCD2" pedido pelo papel |
| Aurora/RDS Postgres | OLTP, não colunar/MPP |
| Snowflake/Databricks SQL na AWS | Fora do provider nativo; ver KB `cloud-platforms` |

## Learning path

1. `concepts/serverless-model.md`
2. `concepts/cost-controls.md` (antes de criar qualquer workgroup)
3. `patterns/bulk-load.md` → `patterns/merge-scd2.md`

## Fontes validadas (2026-10-16)

- docs.aws.amazon.com/redshift/latest/mgmt/serverless-capacity.html (base 4–512/1024)
- docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-max-rpu.html (usage limits)
- docs.aws.amazon.com/redshift/latest/dg/r_MERGE.html · copy-parameters-authorization.html
- aws.amazon.com/redshift/pricing (RPU-hora, trial US$ 300/90 dias)
