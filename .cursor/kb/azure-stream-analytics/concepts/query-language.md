---
domain: azure-stream-analytics
topic: query-language
---

# Linguagem de query do Stream Analytics (SAQL)

Subconjunto de T-SQL com extensões temporais. Cada input/output é referenciado pelo
**alias** configurado no job (entre colchetes se tiver hífen).

## Estrutura

```sql
WITH etapa1 AS (
    SELECT ... FROM [input] TIMESTAMP BY campo_evento
)
SELECT ... INTO [output1] FROM etapa1 ...
SELECT ... INTO [output2] FROM etapa1 ...     -- vários SELECT INTO no mesmo job
```

- `INTO` define o output; um job pode ter vários outputs.
- `WITH` cria etapas (multi-step); útil para reaproveitar e para juntar várias
  reference data (só se junta reference com stream, uma por etapa).

## Tempo: aplicação vs chegada

| Cláusula | Tempo usado |
|---|---|
| sem `TIMESTAMP BY` | horário de chegada no Event Hubs (`EventEnqueuedUtcTime`) |
| `TIMESTAMP BY criado_em` | tempo do evento (aplicação) — padrão recomendado |
| `TIMESTAMP BY criado_em OVER loja_id` | relógio independente por chave (substreams) |

Com tempo de aplicação entram as políticas do job:
`events_late_arrival_max_delay_in_seconds`, `events_out_of_order_max_delay_in_seconds`,
`events_out_of_order_policy` (`Adjust` | `Drop`). Evento fora da tolerância é ajustado
ou descartado — causa clássica de "saída vazia" em teste com dados antigos.

## Janelas (GROUP BY)

```sql
-- Tumbling: contagem a cada 5 min
SELECT loja_id, COUNT(*) AS n, System.Timestamp() AS fim
FROM [pedidos] TIMESTAMP BY criado_em
GROUP BY loja_id, TumblingWindow(minute, 5)

-- Hopping: média móvel de 10 min atualizada a cada 1 min
GROUP BY loja_id, HoppingWindow(minute, 10, 1)

-- Session: sessões de navegação com 5 min de inatividade, máx. 1 h
GROUP BY usuario_id, SessionWindow(minute, 5, 60)
```

Unidades: `second`, `minute`, `hour`, `day` (e abreviações). Tamanho máximo de janela:
7 dias. Memória cresce com a **cardinalidade** (nº de grupos por janela), não com o
tamanho da janela.

## Joins

| Tipo | Exige limite de tempo? | Exemplo |
|---|---|---|
| Stream × **reference** | **não** | `JOIN [ref] r ON s.k = r.k` |
| Stream × stream (temporal) | **sim** (`DATEDIFF`) | `ON a.id = b.id AND DATEDIFF(minute, a, b) BETWEEN 0 AND 10` |

## Funções temporais úteis

```sql
-- Último valor por chave nos últimos 10 min
SELECT sensor_id, LAG(temp) OVER (PARTITION BY sensor_id LIMIT DURATION(minute, 10)) AS anterior
FROM [leituras] TIMESTAMP BY ts

-- Primeiro evento por chave numa janela de 1 h (dedupe)
WHERE ISFIRST(hour, 1) OVER (PARTITION BY pedido_id) = 1
```

## Paralelismo

`PARTITION BY PartitionId` faz cada partição do Event Hub ser processada de forma
independente (embarrassingly parallel) quando a chave de grupo/join está alinhada com a
chave de partição do producer. Sem isso, SU extra pode não ajudar.

```sql
SELECT PartitionId, loja_id, COUNT(*) AS n
INTO [saida]
FROM [pedidos] PARTITION BY PartitionId TIMESTAMP BY criado_em
GROUP BY PartitionId, loja_id, TumblingWindow(minute, 5)
```

`compatibility_level = "1.2"` alinha o particionamento de input e output
automaticamente em vários casos (**a validar** para o output escolhido).

## Tipos e conversões

- Tipos: `bigint`, `float`, `nvarchar(max)`, `datetime`, `bit`, `record`, `array`.
- `TRY_CAST(campo AS bigint)` evita falha do job por evento malformado.
- JSON aninhado: `GetRecordPropertyValue`, `GetArrayElement`, `CROSS APPLY GetArrayElements(...)`.

## Teste local

Portal (*Test query* com amostra) ou extensão Stream Analytics do VS Code (execução
local com arquivos de amostra) — validar a query antes de pagar SU.
