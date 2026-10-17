---
domain: azure-adls-gen2
topic: zone-layout
---

# Layout de zonas no lake

## Um container por zona

| Container | Alias | Conteúdo | Quem escreve | Quem lê |
|---|---|---|---|---|
| `bronze` | raw | dado como chegou (JSON/Avro/CSV), imutável, append-only | ingestão (Kafka Connect, Capture, ASA) | jobs silver |
| `silver` | curated | limpo, tipado, deduplicado, Parquet/Delta | jobs Spark | warehouse, jobs gold |
| `gold` | — | agregados/modelos de consumo | jobs gold | BI, warehouse |
| `reference` | — | lookup para stream (CSV/JSON versionado por data) | job batch | Stream Analytics |
| `sandbox` | — | exploração descartável | humanos | humanos |

Por que container (e não pasta) por zona: RBAC no escopo container é o isolamento barato
e forte; lifecycle policy por container fica simples.

Nomenclatura alternativa `raw/curated/consumption` é equivalente — **escolha uma** e
registre no `CLAUDE.md` do projeto.

## Convenção de path

```
<zona>/<dominio>/<entidade>/[<particao>=<valor>/...]<arquivo>

bronze/vendas/pedidos/ingest_date=2026-10-16/part-0000.json
silver/vendas/pedidos/dt=2026-10-16/part-0000.snappy.parquet
gold/vendas/receita_diaria/dt=2026-10-16/part-0000.snappy.parquet
reference/produtos/2026-10-16/08-00/produtos.csv      # {date}/{time} do Stream Analytics
```

- Partição estilo Hive (`chave=valor`) → Spark/Synapse fazem partition pruning.
- Partição por data de **ingestão** no bronze; por data de **negócio** no silver/gold.
- Evitar partição de alta cardinalidade (ex.: por cliente) — gera milhões de arquivos
  pequenos (custo de transação + lentidão).
- Tamanho-alvo de arquivo no silver/gold: 128 MB–1 GB (Synapse COPY rende melhor ≥ 256 MB).

## Imutabilidade e reprocesso

- Bronze nunca é sobrescrito: reprocessar = ler bronze de novo e reescrever silver.
- Reference data do Stream Analytics é imutável por design: nova versão = novo blob com
  `{date}/{time}` maior (ver KB `azure-stream-analytics`).
- Sobrescrita no silver/gold por partição (`dt=`) inteira, nunca arquivo a arquivo.

## Lifecycle (custo)

| Zona | Política sugerida em lab |
|---|---|
| bronze | mover para Cool após 30 dias; apagar após N dias se dado reproduzível |
| sandbox | apagar após 7 dias |
| silver/gold | Hot |

Em lab de um dia, o destroy do RG resolve; lifecycle importa quando o lake sobrevive.

## PII por zona

- Bronze: PII crua possível → acesso só da ingestão e do job silver.
- Silver: PII pseudonimizada/mascarada quando não necessária downstream (minimização LGPD).
- Gold: sem PII direta.
- Nunca PII em nome de arquivo/diretório (aparece em logs de acesso e listagens).
