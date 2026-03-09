CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_mysql_menu
COMMENT "Tabela de Seções do Menu (Categorias). Estrutura do cardápio vinda do MySQL, com dados padronizados, tipados e limpos."
AS

-- 1. LEITURA
WITH bronze_table AS (
  -- Confere se o nome na bronze segue o padrão (bronze_mysql_menu)
  SELECT * FROM STREAM(live.mysql_menu)
),

-- 2. NORMALIZAÇÃO (Pass-through)
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(menu_section_id AS STRING)                   AS id_secao_menu,
    CAST(restaurant_id AS STRING)                     AS id_restaurante,
    CAST(name AS STRING)                              AS nome_secao,
    CAST(description AS STRING)                       AS descricao_secao,
    CAST(active AS BOOLEAN)                           AS flag_ativo,
    CAST(dt_current_timestamp AS TIMESTAMP)           AS data_atualizacao
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleansed_table AS (
  SELECT
    TRIM(id_secao_menu)                               AS id_secao_menu,
    TRIM(id_restaurante)                              AS id_restaurante,
    LOWER(TRIM(nome_secao))                           AS nome_secao,
    TRIM(descricao_secao)                             AS descricao_secao,
    COALESCE(flag_ativo, FALSE)                       AS flag_ativo,
    COALESCE(data_atualizacao, CAST('1900-01-01 00:00:00' AS TIMESTAMP)) AS data_atualizacao
  FROM
    typed_table
),

-- 5. METADADOS
silver_table AS (
  SELECT
    id_secao_menu,
    id_restaurante,
    nome_secao,
    COALESCE(descricao_secao, 'Sem descrição')        AS descricao_secao,
    flag_ativo,
    data_atualizacao,
    current_timestamp()                               AS _data_ingestao,
    'mysql-minio'                                     AS _sistema_fonte
  FROM
    cleansed_table
)

SELECT * FROM silver_table;