CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_search
COMMENT "Tabela de busca dentro do app da Uber Eats, com dados padronizados, tipados e limpos."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(LIVE.search)
),

-- 2. NORMALIZAÇÃO
-- Neste caso, os dados já vieram normalizados
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(user_id AS STRING)                                         AS id_usuario,
    CAST(search_id AS STRING)                                       AS id_busca,
    CAST(clicked_product_id AS STRING)                              AS id_produto_clicado,
    CAST(filters AS STRING)                                         AS filtros,
    CAST(query_text AS STRING)                                      AS texto_busca,
    CAST(timestamp AS TIMESTAMP)                                    AS data_busca,
    CAST(result_count AS INT)                                       AS quantidade_resultados
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleared_table AS (
  SELECT
    TRIM(id_usuario)                                                AS id_usuario,
    TRIM(id_busca)                                                  AS id_busca,
    TRIM(id_produto_clicado)                                        AS id_produto_clicado,
    LOWER(TRIM(filtros))                                            AS filtros,
    LOWER(TRIM(texto_busca))                                        AS texto_busca,
    COALESCE(data_busca, CAST('1900-01-01' AS TIMESTAMP))           AS data_busca,
    COALESCE(quantidade_resultados, 0)                              AS quantidade_resultados
  FROM
    typed_table
),

-- 5. METADATA
silver_table AS (
  SELECT
    *,
    CURRENT_TIMESTAMP()                                             AS _data_carga,
    'kafka-minio'                                                   AS _sistema_fonte
  FROM
    cleared_table
)

SELECT * FROM silver_table