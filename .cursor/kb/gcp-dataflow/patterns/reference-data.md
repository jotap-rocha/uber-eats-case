---
domain: gcp-dataflow
topic: reference-data
---

# Pattern: reference data slowly-changing a partir do GCS

## Problema

Enriquecer eventos de streaming (Kafka) com uma tabela de referência pequena (ex.: cadastro
de produtos) que é republicada no GCS de tempos em tempos, **sem reiniciar o job**.
Equivale ao *reference data input* com *path pattern* do Stream Analytics.

## Solução

Side input em **janela global** alimentado por `PeriodicImpulse`: a cada intervalo, recarrega
o arquivo do GCS e emite um novo painel; o main input passa a ver a versão mais recente.
Pattern documentado pelo Beam ("slowly updating side inputs").

## Layout no GCS

```
gs://<BUCKET>-ref/produtos/current.json            # ponteiro fixo (sobrescrito)
gs://<BUCKET>-ref/produtos/2026/10/16/produtos.json  # versão datada (path pattern)
```

Publicação **atômica**: escrever a versão datada e depois copiar para `current.json`
(objeto GCS é substituído por inteiro — leitores nunca veem arquivo parcial).

## Pipeline (Python)

```python
import json
import time
from datetime import datetime, timezone

import apache_beam as beam
from apache_beam.io.filesystems import FileSystems
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms import trigger, window
from apache_beam.transforms.periodicsequence import PeriodicImpulse

REF_PREFIX = "gs://<BUCKET>-ref/produtos"
REFRESH_S = 600  # 10 min


def ref_path(_tick) -> str:
    # path pattern por data (UTC). Alternativa: f"{REF_PREFIX}/current.json"
    d = datetime.now(timezone.utc)
    return f"{REF_PREFIX}/{d:%Y/%m/%d}/produtos.json"


def load_ref(path: str) -> dict:
    with FileSystems.open(path) as f:
        rows = json.loads(f.read().decode("utf-8"))
    return {r["produto_id"]: r for r in rows}


def enrich(evento: dict, ref: dict) -> dict:
    p = ref.get(evento["produto_id"], {})
    return {**evento, "categoria": p.get("categoria"), "ref_hit": bool(p)}


def run(argv=None):
    opts = PipelineOptions(argv, streaming=True)
    with beam.Pipeline(options=opts) as p:
        ref = (
            p
            | "Tick" >> PeriodicImpulse(fire_interval=REFRESH_S, apply_windowing=False)
            | "Path" >> beam.Map(ref_path)
            | "Load" >> beam.Map(load_ref)
            | "GlobalWin" >> beam.WindowInto(
                window.GlobalWindows(),
                trigger=trigger.Repeatedly(trigger.AfterProcessingTime(1)),
                accumulation_mode=trigger.AccumulationMode.DISCARDING,
            )
        )

        eventos = p | "ReadKafka" >> read_events()  # ReadFromKafka/Managed IO (ver nota)

        (
            eventos
            | "Win" >> beam.WindowInto(window.FixedWindows(60))
            | "Enrich" >> beam.Map(enrich, ref=beam.pvalue.AsSingleton(ref))
            | "ToBQ" >> write_bq()  # WriteToBigQuery (Storage Write API)
        )
```

`read_events()`/`write_bq()` ficam no código do projeto. Leitura de Managed Kafka em Python
usa `ReadFromKafka` (cross-language, Java expansion service) com config SASL OAUTHBEARER
ou `beam.managed.Read(beam.managed.KAFKA, ...)` — **a validar** por versão do SDK.

## Por que cada peça

| Peça | Motivo |
|---|---|
| `PeriodicImpulse(apply_windowing=False)` | Emite um tick por intervalo, indefinidamente |
| `GlobalWindows` + `Repeatedly(AfterProcessingTime)` | Cada recarga vira um painel novo da mesma janela |
| `DISCARDING` | O painel novo **substitui** o anterior (não acumula versões) |
| `AsSingleton` | Main input recebe o dict inteiro |

## Riscos / a validar

- Entre o deploy e o 1º tick o side input pode estar vazio → `AsSingleton` bloqueia o main
  input até o 1º painel (comportamento esperado do Beam; **a validar** latência inicial).
  `PeriodicImpulse` dispara imediatamente no start.
- Arquivo do dia ainda não publicado (path pattern) → `load_ref` falha. Fallback para
  `current.json` em `try/except FileNotFoundError` e métrica de contagem de falhas.
- Tamanho: manter o dict em poucos MB; acima disso use lookup (`Enrichment` com BigQuery/
  Bigtable).
- Timing exato de propagação do novo painel para todos os workers: **a validar em carga**.

## Permissões

Worker SA: `roles/storage.objectViewer` no bucket `<BUCKET>-ref` (ver
`gcp-gcs/patterns/service-identity-access.md`).

## Verificação

1. Publicar `produtos.json` v1; subir o job; conferir `ref_hit = true` no BigQuery.
2. Publicar v2 com categoria alterada; após ≤ `REFRESH_S` + latência, eventos novos saem com
   a categoria nova.
3. `SELECT COUNTIF(NOT ref_hit)/COUNT(*)` — taxa de misses.

## Custo

Um job streaming 24/7: limitar `--max_num_workers`. **Drain** ao fim do teste; cancel se não
precisar do buffer. Leitura do GCS a cada 10 min = custo desprezível (Classe B).
