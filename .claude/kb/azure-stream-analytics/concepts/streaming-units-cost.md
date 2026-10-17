---
domain: azure-stream-analytics
topic: streaming-units-cost
---

# Streaming Units, custo e start/stop

## SU V1 vs SU V2

| Modelo | Status | Granularidade |
|---|---|---|
| SU V1 (`Standard`) | a ser descontinuado | 1, 3, 6, 12, 18… (6 SU = 1 nó) |
| **SU V2** (`StandardV2`) | **recomendado** | 1/3, 2/3, 1, 2, 3… (1 SU V2 = 1 nó) |

Na API/logs/Terraform o V2 aparece ×10: 1/3 → `3`, 2/3 → `7`, 1 → `10`, 2 → `20`.
Use sempre StandardV2 em projeto novo.

## Quanto SU usar

- Comece com **1/3 SU V2** em lab (Event Hub de 2 partições) ou 1 SU V2 para 4–8
  partições sem `PARTITION BY`.
- ~7 MB/s de input por SU (referência da doc); muitas partições no Event Hub consomem
  recurso mesmo sem tráfego → não crie 32 partições "por via das dúvidas".
- Métrica **SU % Utilization** (memória): manter < 80 %; alerta em 80 %. Watermark
  delay e backlogged events mostram falta de CPU que o SU% não mostra.
- O que consome memória: cardinalidade das janelas, temporal joins (eventos dentro do
  `DATEDIFF`), funções analíticas (`LAG`/`ISFIRST`), buffer de out-of-order, **cada
  reference join mantém uma cópia** da reference (× partições se `PARTITION BY`), UDF
  JavaScript.

## Cobrança

| Estado do job | Cobra SU? |
|---|---|
| Created / Stopped | não (**a validar** na página de preço para StandardV2) |
| Starting / Running | sim, por SU-hora, **com ou sem eventos** |
| Failed | verificar — tratar como "parar e investigar" |

Outros custos indiretos: storage do lake (output/reference), Event Hubs (TU), e
storage account do job (checkpoints, snapshot de reference SQL).

## Start / stop

```bash
az extension add --name stream-analytics            # uma vez
az stream-analytics job start -g <RG> -n <JOB> --output-start-mode JobStartTime
az stream-analytics job stop  -g <RG> -n <JOB>
az stream-analytics job list  -g <RG> --query "[].{job:name, estado:jobState}" -o table
```

| `--output-start-mode` | Uso |
|---|---|
| `JobStartTime` | começa agora |
| `CustomTime` (+ `--output-start-time`) | reprocessar a partir de um instante |
| `LastOutputEventTime` | retomar de onde parou (após stop) |

Terraform:
- `azurerm_stream_analytics_job` cria o job **sem iniciar**.
- `azurerm_stream_analytics_job_schedule` inicia o job no apply — em lab, **evite**:
  deixa o job Running sem você perceber. Prefira start manual pela CLI.
- Alterar query/inputs exige o job **parado**.

## Guardrails

1. Budget + alerta na assinatura.
2. Script de fim de sessão: `job stop` em todos os jobs do RG (loop sobre `job list`).
3. Tag `ttl = "same-day"` no job.
4. Alerta de métrica SU% > 80 % só em ambiente que fica ligado.
