# Airbyte — MongoDB (snapshot) → ADLS Gen2 (Azure, Fase 1)

> Substitui a Lakehouse Federation usada hoje na Fase 0 (`pipeline/silver/ingestion_mongo_perfil_restaurante.sql`) por ingestão real — decisão explícita do usuário (ver `BRAINSTORM_INGESTAO_AZURE_FASE1.md`, Decisão #6). Path particionado por data, não overwrite-in-place — necessário para o reference data input do Stream Analytics (ver `DESIGN_INGESTAO_AZURE_FASE1.md`, Decisão 6).

## Configurar o destino "Azure Blob Storage"

1. Destinations → + New destination → **Azure Blob Storage**
2. Preencha:
   - **Endpoint domain name**: `<AZURE_STORAGE_ACCOUNT_NAME>.blob.core.windows.net` (o mesmo Storage Account com hierarchical namespace habilitado — ADLS Gen2 é compatível com o endpoint Blob)
   - **Azure Blob Storage container name**: `bronze`
   - **Azure Blob Storage account key**: chave do Storage Account (`infra/azure/fase1-ingestao/storage_account.tf`)
   - **Format**: `JSONL`
3. Test connection → Set up

## Criar a conexão (MongoDB → ADLS)

1. Connections → + New connection
2. Selecione: MongoDB (fonte já usada para `perfil_restaurante`) → Azure Blob Storage
3. Configure:
   - **Frequency**: diária (fonte estática — CDC seria decorativo, mesma decisão da AWS/GCP)
   - **Sync mode**: `Full Refresh | Overwrite`
   - **Destination path**: `mongodb/perfil_restaurante/{{ now.year }}/{{ now.month }}/{{ now.day }}/perfil_restaurante.json` — path particionado por data (não overwrite-in-place do mesmo arquivo), para casar com o `path_pattern` configurado no reference data input do Stream Analytics (`mongodb/perfil_restaurante/{date}/perfil_restaurante.json`)
4. Selecione o stream `perfil_restaurante`
5. Set up connection

## Validação

1. Rodar a sync manualmente ("Sync now").
2. Confirmar que o arquivo aparece em `abfss://bronze@<storage-account>.dfs.core.windows.net/mongodb/perfil_restaurante/<ano>/<mes>/<dia>/perfil_restaurante.json`.
3. Confirmar que a Bronze do Databricks (`pipeline/bronze/ingest_mongodb_perfil_restaurante.sql`) e o Synapse (`sql/azure/synapse_copy_merge.sql`) conseguem ler o arquivo.
