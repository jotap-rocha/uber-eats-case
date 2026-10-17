---
domain: aws-s3
topic: zone-layout
---

# Layout de zonas no S3

## S3 não tem diretório

S3 é chave-valor plano: `raw/kafka/x/dt=2026-10-16/part-0.json` é **uma chave**. "Pastas"
são prefixos. Consequências:

- Permissão por "pasta" = condição em prefixo (`s3:prefix`) ou ARN `bucket/raw/*`.
- Renomear "pasta" = copiar + apagar cada objeto (caro). Planeje nomes antes.
- Sem namespace hierárquico como o ADLS Gen2 — rename atômico de diretório **não existe**
  em bucket de uso geral. (Buckets de diretório / S3 Express One Zone são outro produto.)

## Zonas

| Zona | Conteúdo | Escritor | Leitores | Retenção |
|---|---|---|---|---|
| `landing/` | arquivos brutos de fontes batch (CSV/JSON) | ingestão | ETL | 7–30 dias (lifecycle) |
| `raw/` | cópia imutável, append-only | Kafka Connect, ingestão | ETL, Flink | longa / Glacier |
| `curated/` | Parquet limpo, tipado, PII pseudonimizada | ETL (Spark/Glue/dbt) | Redshift COPY, Athena | longa |
| `reference/` | tabelas pequenas de lookup | ETL / time de negócio | Flink | versão atual + histórico curto |
| `tmp/` | scratch de jobs | jobs | jobs | 1 dia |

Um bucket com prefixos (lab) **ou** um bucket por zona (produção: policies e
replicação mais simples). Não misture dados de ambientes diferentes no mesmo bucket.

## Partições (estilo Hive)

```
curated/vendas/pedidos/dt=2026-10-16/part-00000.snappy.parquet
raw/kafka/vendas.pedidos.v1/dt=2026-10-16/vendas.pedidos.v1+0+0000001000.json
```

- `chave=valor` é entendido por Glue Catalog/Athena/Spark/Redshift Spectrum.
- Particione por data de **evento** em curated, data de **ingestão** em raw.
- Evite cardinalidade alta (`cliente_id=`) — explode número de prefixos e arquivos.

## Tamanho de arquivo

- Alvo 128 MB–1 GB em curated (Parquet/Snappy). Milhares de arquivos de KB = custo de
  request alto e COPY/scan lento.
- Kafka Connect: `flush.size` + `rotate.schedule.interval.ms` controlam o tamanho/frequência.

## Lifecycle

```hcl
resource "aws_s3_bucket_lifecycle_configuration" "lake" {
  bucket = aws_s3_bucket.lake.id
  rule {
    id     = "expira-landing"
    status = "Enabled"
    filter { prefix = "landing/" }
    expiration { days = 14 }
  }
  rule {
    id     = "expira-tmp"
    status = "Enabled"
    filter { prefix = "tmp/" }
    expiration { days = 1 }
  }
  rule {
    id     = "versoes-antigas"
    status = "Enabled"
    filter {}
    noncurrent_version_expiration { noncurrent_days = 30 }
    abort_incomplete_multipart_upload { days_after_initiation = 7 }
  }
}
```

## Versionamento

- Ligar em `raw/`/`curated/` de produção (proteção contra delete acidental).
- Em lab, versionamento + sem lifecycle = custo escondido e `BucketNotEmpty` no destroy.

## Nomes

- Bucket: globalmente único, minúsculo, sem `_` — ex.: `<ORG>-<PROJETO>-lake-<AMBIENTE>`.
- Não codificar `<AWS_ACCOUNT_ID>` real em nome versionado em doc pública.
