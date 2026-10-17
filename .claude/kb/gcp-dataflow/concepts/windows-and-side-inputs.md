---
domain: gcp-dataflow
topic: windows-and-side-inputs
---

# Janelas, watermark e side inputs

Equivalência com Stream Analytics:

| Stream Analytics | Beam / Dataflow |
|---|---|
| `TumblingWindow(minute, 5)` | `window.FixedWindows(300)` |
| `HoppingWindow(minute, 10, 5)` | `window.SlidingWindows(600, 300)` |
| `SessionWindow(...)` | `window.Sessions(gap_size)` |
| `TIMESTAMP BY col` | `beam.Map(lambda e: TimestampedValue(e, e["ts"]))` / timestamp attr da fonte |
| Late arrival policy | `allowed_lateness` + triggers |
| Reference data input | **Side input** |
| Reference path pattern `{date}/{time}` | Caminho calculado na função de load (ver pattern) |

## Janelas

```python
from apache_beam import window
from apache_beam.transforms import trigger

agg = (events
  | beam.WindowInto(window.FixedWindows(300),
                    trigger=trigger.AfterWatermark(late=trigger.AfterCount(1)),
                    allowed_lateness=600,
                    accumulation_mode=trigger.AccumulationMode.ACCUMULATING)
  | beam.Map(lambda e: (e["produto_id"], e["valor"]))
  | beam.CombinePerKey(sum))
```

- **Watermark**: estimativa do runner de "todo evento até T chegou". Janela dispara no
  watermark; dados atrasados dentro de `allowed_lateness` geram painéis extras.
- Kafka: timestamp do evento vem do registro (`LogAppendTime`/`CreateTime`) ou de campo do
  payload — definir explicitamente.

## Side inputs

Dado adicional, **pequeno**, disponível inteiro para cada worker durante o processamento do
main input.

| Vista | Quando |
|---|---|
| `AsSingleton` | Um objeto (ex.: dict `{produto_id: atributos}`) |
| `AsDict` | PCollection de pares `(k, v)` |
| `AsIter` / `AsList` | Coleção pequena iterada |

Regras:

- Side input é **materializado e broadcast** — mantenha em MB (dezenas, no máximo). Tabela
  grande → lookup/join por chave ou `Enrichment` transform (BigQuery/Bigtable) — **a
  validar** por versão do SDK.
- Main input e side input precisam de **janelas compatíveis**: com side input em janela
  global e main input em janelas fixas, cada janela vê o **último painel** disparado do side
  input.
- Side input **estático** (lido uma vez no início) não reflete mudança do arquivo → para
  reference data que muda, use o pattern **slowly-changing** (`PeriodicImpulse` + janela
  global com trigger repetido).

## Por que não ler o GCS dentro do `DoFn` a cada elemento

Latência e custo de operação Classe B por evento. Se precisar sem side input: cache no
`DoFn.setup()` com TTL — aceitável, mas cada worker recarrega independentemente.
