---
domain: azure-synapse
topic: cost-and-pause
---

# Custo e pausa do Dedicated SQL Pool

## O que é cobrado

| Componente | Quando cobra | Para de cobrar com |
|---|---|---|
| Compute (DWU-hora) | pool **Online** | `pause` |
| Storage do pool (dados + snapshots) | sempre | `delete` do pool |
| Geo-backup | se `geo_backup_policy_enabled = true` | desligar em lab |
| Serverless SQL | por TB processado | não rodar query |
| Workspace Synapse | sem custo próprio relevante; storage do ADLS default cobra | destroy |

Fonte: learn.microsoft.com, "Pause and resume compute in dedicated SQL pool" — "You
won't be charged for compute resources while the database is paused. However, you will
continue to be charged for storage."

## Ordem de grandeza (a validar na calculadora da região)

| SKU | ≈ US$/hora ligado | Esquecido 1 fim de semana (60 h) |
|---|---|---|
| DW100c | 1,0–1,5 | 60–90 |
| DW200c | 2,0–3,0 | 120–180 |

Com crédito de avaliação de US$ 200, um DW100c esquecido ligado acaba com o crédito em
poucos dias.

## Rotina segura de lab

```bash
# Início da sessão
az synapse sql pool resume -n dwlab --workspace-name <WORKSPACE> -g <RG>
az synapse sql pool wait --sql-pool-name dwlab --workspace-name <WORKSPACE> -g <RG> \
  --custom "status=='Online'"     # sintaxe do --custom a validar no seu az

# ... COPY INTO, MERGE, testes ...

# Fim da sessão (sempre)
az synapse sql pool pause -n dwlab --workspace-name <WORKSPACE> -g <RG>
az synapse sql pool show  -n dwlab --workspace-name <WORKSPACE> -g <RG> --query status -o tsv
```

Fim do estudo: `terraform destroy` (pausado ainda paga storage).

## Guardrails recomendados

1. **Budget + alerta** na assinatura (Cost Management) em 50/80/100 % do crédito.
2. **Pausa agendada**: Automation runbook / Logic App / pipeline do próprio Synapse que
   chama a REST de pause todo dia à noite — rede de segurança para esquecimento.
3. Tag `ttl = "same-day"` no pool para a skill de custo achar.
4. Pipeline de carga começa com `resume` e termina com `pause` (try/finally).

## Terraform e pausa

`azurerm_synapse_sql_pool` não expõe estado pausado: o `apply` cria o pool **Online**.
Logo após o apply, pausar via `az`. Um `plan` posterior não detecta "pausado" como drift.
Escalar DWU pelo Terraform (`sku_name`) funciona, mas exige o pool Online.

## Sinais de que algo está queimando crédito

- `az synapse sql pool list -g <RG> --workspace-name <WORKSPACE> --query "[].{n:name,s:status}"`
  mostrando `Online` fora do horário de uso.
- Cost Management → custo por recurso com linha "SQL Pool – DWU" crescendo diariamente.
