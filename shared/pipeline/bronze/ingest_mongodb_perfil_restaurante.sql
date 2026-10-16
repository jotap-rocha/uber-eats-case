-- Bronze do satelite MongoDB "Perfil de Restaurante" (Fase 1/Azure).
-- Fonte estatica (snapshot/full-refresh via Airbyte, sem CDC -- decisao da
-- Onda 3). Substitui a leitura direta por Lakehouse Federation usada na
-- Fase 0 -- ver DESIGN_INGESTAO_AZURE_FASE1.md, Decisao 3 (item 25 do
-- manifesto) e docs/azure/airbyte-mongodb-adls-config.md (path particionado
-- por data).
--
-- Arquivo novo -- nao existia Bronze para esta entidade antes desta feature
-- (a Silver lia direto da Lakehouse Federation).

CREATE OR REFRESH LIVE TABLE bronze.bronze_perfil_restaurante
COMMENT "Bronze do satelite Perfil de Restaurante (MongoDB, Airbyte -> ADLS Gen2). Fonte estatica, sem CDC — mantem so a carga mais recente por restaurant_id."
AS

WITH raw_files AS (
  SELECT
    *,
    _metadata.file_path              AS _source_file,
    _metadata.file_modification_time AS _file_modification_time
  FROM read_files(
    'abfss://bronze@REPLACE_STORAGE_ACCOUNT.dfs.core.windows.net/mongodb/perfil_restaurante/',
    format => 'json'
  )
),

latest_only AS (
  SELECT *
  FROM raw_files
  QUALIFY ROW_NUMBER() OVER (PARTITION BY restaurant_id ORDER BY _file_modification_time DESC) = 1
)

SELECT
  *,
  current_timestamp() AS _datetime_ingestion,
  'mongodb-ubereats'  AS cdc_source_system
FROM latest_only;
