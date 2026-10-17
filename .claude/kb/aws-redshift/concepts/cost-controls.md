---
domain: aws-redshift
topic: cost-controls
---

# Controle de custo no Redshift Serverless

## As 4 alavancas

| Alavanca | Onde | Efeito |
|---|---|---|
| `base_capacity` | workgroup | custo por hora de query (RPU × US$ 0,375) |
| `max_capacity` | workgroup | teto de escala automática |
| Usage limit (RPU-horas) | workgroup | orçamento por dia/semana/mês com ação |
| `destroy` | Terraform | zera compute **e** storage |

## Conta rápida

| Base RPU | Custo por hora ativa (us-east-1) |
|---|---|
| 4 | US$ 1,50 |
| 8 | US$ 3,00 |
| 32 | US$ 12,00 |
| 128 (default!) | US$ 48,00 |

Com o trial de US$ 300: base 8 ≈ 100 h de query ativa. Base 128 ≈ 6 h.

## Usage limits

- Até **4 limites** por workgroup; frequência **daily | weekly | monthly**; valor em
  RPU-horas.
- Ações: **Log to system table** (`SYS_QUERY_HISTORY.usage_limit`), **Alert** (SNS) e
  **Turn off user queries** (desliga processamento — o único que corta de fato).
- Terraform: `breach_action = "log" | "emit-metric" | "deactivate"`.

```bash
aws redshift-serverless create-usage-limit \
  --resource-arn arn:aws:redshift-serverless:<REGION>:<AWS_ACCOUNT_ID>:workgroup/<WG_ID> \
  --usage-type serverless-compute --amount 8 --period daily --breach-action deactivate
```

Padrão de lab: um limite `daily` com `deactivate` + um `monthly` com `emit-metric`
alimentando alarme/SNS.

## "Pausa"

- Não há `pause` como no Synapse Dedicated Pool. Ocioso já não cobra compute.
- O risco é **não ficar ocioso**: dashboards com refresh, Airflow sensor, conexões que
  rodam `SELECT 1`. Desligue agendamentos fora do horário de teste.
- Para garantir zero: usage limit `deactivate` ou `terraform destroy`.

## Monitorar

```sql
-- RPU por minuto nas últimas horas
SELECT end_time, compute_capacity, charged_seconds
FROM sys_serverless_usage
WHERE end_time > dateadd(hour, -6, getdate())
ORDER BY end_time DESC;
```

- CloudWatch: `ComputeCapacity` / `ComputeSeconds` em `AWS/Redshift-Serverless`.
- AWS Budgets com filtro de serviço "Amazon Redshift" como segunda linha de defesa.

## Teardown

```bash
terraform destroy -target=aws_redshiftserverless_usage_limit.daily \
                  -target=aws_redshiftserverless_workgroup.dw \
                  -target=aws_redshiftserverless_namespace.dw
```

Snapshots manuais e de recovery point cobram storage — liste e apague o que não precisa:
`aws redshift-serverless list-snapshots --namespace-name <PROJETO>-dw`.
