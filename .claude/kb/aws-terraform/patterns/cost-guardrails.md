---
domain: aws-terraform
topic: cost-guardrails
---

# Pattern: guard-rails de custo (Budgets + tags + teardown)

## Problema

Serviços de dados serverless da AWS cobram por hora mesmo ociosos (MSK Serverless
cluster-hora + partição-hora; Flink KPU-hora enquanto RUNNING). Crédito de conta nova
some em dias se algo ficar ligado.

## 1. Budget antes de tudo

```hcl
resource "aws_budgets_budget" "lab" {
  name         = "<PROJETO>-lab"
  budget_type  = "COST"
  limit_amount = "20"
  limit_unit   = "USD"
  time_unit    = "MONTHLY"

  cost_filter {
    name   = "TagKeyValue"
    values = ["user:Projeto$<PROJETO>"]   # exige a tag ativada como cost allocation tag
  }

  dynamic "notification" {
    for_each = [50, 80, 100]
    content {
      comparison_operator        = "GREATER_THAN"
      threshold                  = notification.value
      threshold_type             = "PERCENTAGE"
      notification_type          = "ACTUAL"
      subscriber_email_addresses = [var.alert_email]   # via tfvars não versionado
    }
  }
}
```

- Budget é **alerta**, não corte: não desliga nada sozinho. **A validar:** Budget
  Actions (aplicar SCP/IAM policy ao estourar) se quiser corte automático.
- Sem o filtro de tag o budget vale para a conta inteira — ok para conta de lab.
- Tag de cost allocation precisa ser ativada no Billing (até 24h para aparecer).

## 2. Tags padrão (identificam órfãos)

```hcl
provider "aws" {
  region = var.region
  default_tags {
    tags = { Projeto = var.projeto, Ambiente = "lab", Dono = var.dono, TTL = "1d" }
  }
}
```

```bash
aws resourcegroupstaggingapi get-resources \
  --tag-filters Key=Projeto,Values=<PROJETO> --query 'ResourceTagMappingList[].ResourceARN'
```

## 3. Ciclo "criar → testar → destruir no mesmo dia"

```bash
terraform apply tfplan
# testes / evidências
terraform destroy -auto-approve=false     # revise a lista antes de confirmar
aws resourcegroupstaggingapi get-resources --tag-filters Key=Projeto,Values=<PROJETO>
```

| Recurso | Para "pausar" | Para zerar custo |
|---|---|---|
| MSK Serverless | não existe pausa | `destroy` |
| MSK Connect connector | não existe pausa | `destroy` do connector |
| Redshift Serverless | ocioso = sem RPU-hora (paga storage) | `destroy` do workgroup/namespace |
| Managed Flink | `stop-application` | `stop` ou `destroy` |
| S3 | n/a | esvaziar + `destroy` (ou lifecycle de expiração) |

## 4. Recursos do Free plan

Em conta no **Free plan** (modelo de créditos 2025) serviços "paid-only" exigem
upgrade para Paid plan — **a validar** por serviço antes de planejar a stack.

## Checklist antes do `apply`

- [ ] Budget criado e e-mail confirmado
- [ ] `default_tags` com `Projeto` e `TTL`
- [ ] Usage limit no Redshift / max RPU definido (ver `aws-redshift`)
- [ ] Horário de destroy anotado
