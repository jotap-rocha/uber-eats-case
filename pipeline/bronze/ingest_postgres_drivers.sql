-- 1. Cria uma VIEW de preparação 
CREATE TEMPORARY STREAMING LIVE VIEW view_drivers_pre_processed AS
SELECT
  *,
  current_timestamp() AS _datetime_ingestion,
  CAST(_ab_cdc_updated_at AS timestamp) AS _source_updated_at,
  'postgres ubereats' AS source_system,
  'public.drivers' AS source_table,
  -- Contrato canonico de CDC (Onda 3) -- a Silver deve ler estas 4 colunas,
  -- nunca o formato nativo de uma ferramenta especifica (Airbyte aqui,
  -- Debezium no Oracle) -- ver DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md
  CASE WHEN _ab_cdc_deleted_at IS NOT NULL THEN 'd' ELSE 'u' END AS cdc_operation,
  CAST(_ab_cdc_updated_at AS timestamp) AS cdc_commit_ts,
  CAST(_ab_cdc_lsn AS STRING) AS cdc_sequence,
  'postgres-ubereats' AS cdc_source_system
FROM
  STREAM(uber_eats.raw.drivers);

-- =================================================================

-- 2. Ingerir tabela na camada bronze
CREATE OR REFRESH STREAMING TABLE ods_postgres_drivers
COMMENT "ODS de motoristas. Esta ODS se refere a tabela drivers da origem.";
APPLY CHANGES INTO
  uber_eats.bronze.ods_postgres_drivers
FROM
  STREAM(live.view_drivers_pre_processed)
KEYS(driver_id)
APPLY AS DELETE WHEN _ab_cdc_deleted_at IS NOT NULL            -- Instrui o DLT a deletar fisicamente da Bronze
SEQUENCE BY cdc_sequence                                       -- LSN (Onda 3): evita empate de ordenacao em rajada de UPDATEs
COLUMNS * EXCEPT (
    _ab_cdc_lsn,
    _ab_cdc_deleted_at,
    _ab_cdc_updated_at,
    _airbyte_raw_id,
    _airbyte_extracted_at,
    _airbyte_meta,
    _airbyte_generation_id
)                                                            -- Remove colunas de controle desnecessárias
STORED AS SCD TYPE 1;                                          -- mantém apenas o estado atual (ODS)