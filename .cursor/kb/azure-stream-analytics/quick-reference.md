---
domain: azure-stream-analytics
topic: quick-reference
---

# Azure Stream Analytics — Quick Reference

### Janelas

| Janela | Sintaxe | Semântica |
|---|---|---|
| Tumbling | `TumblingWindow(minute, 5)` | blocos fixos sem sobreposição |
| Hopping | `HoppingWindow(minute, 10, 5)` | tamanho 10, avança 5 (sobrepõe) |
| Sliding | `SlidingWindow(minute, 5)` | emite quando o conteúdo muda |
| Session | `SessionWindow(minute, 5, 30)` | agrupa até 5 min de silêncio, máx. 30 |
| Snapshot | `GROUP BY System.Timestamp()` | eventos com o mesmo timestamp |

Fim da janela: `System.Timestamp()`. Janela máxima: 7 dias.

### Query típica

```sql
SELECT p.loja_id, r.regiao, COUNT(*) AS pedidos, SUM(p.valor) AS receita,
       System.Timestamp() AS janela_fim
INTO [saida-adls]
FROM [pedidos-eh] p TIMESTAMP BY p.criado_em
JOIN [ref-lojas] r ON p.loja_id = r.loja_id          -- reference join: sem DATEDIFF
GROUP BY p.loja_id, r.regiao, TumblingWindow(minute, 5)
```

### Reference data (Blob/ADLS)

| Campo | Exemplo |
|---|---|
| Path pattern | `lojas/{date}/{time}/lojas.csv` |
| Date format | `yyyy-MM-dd` (ou `yyyy/MM/dd`, `MM/dd/yyyy`…) |
| Time format | `HH-mm` (ou `HH`, `HH/mm`) |
| Formatos | CSV, JSON · UTF-8 · **sem compressão** |
| Varredura | a cada ~1 min; usa blob quando o relógio alcança o `{date}/{time}` do nome |
| Tamanho | ≤ 300 MB recomendado; 1 SU→50 MB, 3→150 MB, 6+→5 GB (escala V1) |

### Ciclo de vida (az CLI — extensão `stream-analytics`)

```bash
az extension add --name stream-analytics
az stream-analytics job start -g <RG> -n <JOB> --output-start-mode JobStartTime
az stream-analytics job show  -g <RG> -n <JOB> --query jobState -o tsv
az stream-analytics job stop  -g <RG> -n <JOB>
```

`--output-start-mode`: `JobStartTime` | `CustomTime` | `LastOutputEventTime`.

### SU V2 ↔ backend

| UI (V2) | REST/logs/Terraform | Equivalente V1 |
|---|---|---|
| 1/3 | 3 | 1 |
| 2/3 | 7 | 3 |
| 1 | 10 | 6 |
| 2 | 20 | 12 |

(Valor aceito em `streaming_units` do Terraform com `sku_name = "StandardV2"` — **a
validar** contra esta tabela no `plan`.)

### Terraform mínimo

```hcl
resource "azurerm_stream_analytics_job" "job" {
  name                = "<JOB>"
  resource_group_name = azurerm_resource_group.base.name
  location            = azurerm_resource_group.base.location
  sku_name            = "StandardV2"
  streaming_units     = 3               # = 1/3 SU V2 (a validar)
  compatibility_level = "1.2"
  events_out_of_order_policy = "Adjust"
  output_error_policy        = "Stop"
  identity { type = "SystemAssigned" }
  transformation_query = file("${path.module}/query.asaql")
}
```

### Troubleshooting

| Sintoma | Causa |
|---|---|
| Job parado em "Initializing input without a valid reference data blob" | nenhum blob com `{date}/{time}` ≤ start time |
| Reference nova não aplicada | blob sobrescrito (imutável) ou `{date}/{time}` ≤ último lido |
| SU% > 80 | cardinalidade da janela/joins; usar `PARTITION BY` ou subir SU |
| Saída vazia | `TIMESTAMP BY` com eventos antigos + política de late arrival descartando |
