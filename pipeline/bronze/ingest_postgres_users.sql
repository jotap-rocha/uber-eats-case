-- 1. Cria uma VIEW de preparação
CREATE TEMPORARY STREAMING LIVE VIEW view_pre_processed_users AS
SELECT
  *,
  current_timestamp()                   AS _datetime_ingestion,
  CAST(_ab_cdc_updated_at AS timestamp) AS _source_updated_at,
  'postgres ubereats'                   AS source_system,
  'public.drivers'                      AS source_table
FROM
  STREAM(uber_eats.raw.users);

-- =================================================================

-- 2. Ingerir tabela na camada bronze
CREATE OR REFRESH STREAMING TABLE ods_postgres_users
COMMENT "ODS de usuários. Esta ODS se refere a tabela users da origem.";
APPLY CHANGES INTO
  uber_eats.bronze.ods_postgres_users
FROM
  STREAM(live.view_pre_processed_users)
KEYS(user_id)
APPLY AS DELETE WHEN _ab_cdc_deleted_at IS NOT NULL            -- Instrui o DLT a deletar fisicamente da Bronze
SEQUENCE BY _ab_cdc_updated_at                                 -- Campo de controle do CDC
COLUMNS * EXCEPT (
    _ab_cdc_lsn,
    _ab_cdc_deleted_at,
    _ab_cdc_updated_at,
    _airbyte_raw_id,
    _airbyte_extracted_at,
    _airbyte_meta,
    _airbyte_generation_id
)                                                              -- Remove colunas de controle desnecessárias
STORED AS SCD TYPE 1;                                          -- mantém apenas o estado atual (ODS)