# Airbyte — MinIO → ADLS Gen2 (Azure, Fase 1)

> Extensão nova do trilho batch — o roadmap v1.4 só tinha o MinIO no trilho real-time (notificação nativa → Event Hub). Ver `BRAINSTORM_INGESTAO_AZURE_FASE1.md` (ideia inicial) e `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`, seção "Fase 1 — Arquitetura de Ingestão" (v1.9).

## Configurar a source "S3" (MinIO) — já existe

Reaproveita a source S3/MinIO já configurada em `docs/airbyte/README.md` — nenhuma mudança na source, só um novo destino/conexão.

## Configurar o destino "Azure Blob Storage" — já existe

Reaproveita o mesmo destino "Azure Blob Storage" configurado em `docs/azure/airbyte-mongodb-adls-config.md`.

## Criar a conexão (MinIO → ADLS)

1. Connections → + New connection
2. Selecione: S3/MinIO → Azure Blob Storage
3. Configure:
   - **Frequency**: `Every 15 minutes` (mesma frequência já usada na sync MinIO → Databricks da Fase 0, `docs/airbyte/README.md`)
   - **Sync mode**: `Full Refresh | Overwrite`
   - **Destination path**: `minio/{{ stream_name }}/` — preserva o prefixo do stream (`kafka/gps`, `kafka/route`, `mysql/menu`, etc.) dentro do container `bronze`
4. Selecione os streams desejados (mesmos já usados nas sync existentes — `kafka/gps`, `kafka/ratings`, `kafka/route`, `kafka/search`, `kafka/shift`, `mysql/menu`)
5. Set up connection

## Validação

1. Rodar a sync manualmente ("Sync now").
2. Confirmar que os objetos aparecem em `abfss://bronze@<storage-account>.dfs.core.windows.net/minio/<stream>/`.
3. Confirmar que os scripts Silver atualizados (`pipeline/silver/ingestion_kafka_*.sql`, `ingestion_mysql_menu.sql`) conseguem ler do novo path ADLS — ver `DESIGN_INGESTAO_AZURE_FASE1.md`, item 27 do manifesto.
