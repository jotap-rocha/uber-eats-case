CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_restaurants
COMMENT "Tabela de Restaurantes (Dimensão). Dados cadastrais limpos, unificando ID interno e CNPJ. Origem Oracle via Debezium/Kafka Connect (Onda 3, Etapa 2) — antes mysql/restaurants simulado no MinIO."
AS

-- 1. LEITURA
WITH bronze_table AS (
  SELECT * FROM STREAM(live.ods_restaurants)
),

-- 2. NORMALIZAÇÃO (Pass-through)
normalized_table AS (
  SELECT * FROM bronze_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(uuid AS STRING)                              AS id_uuid,
    CAST(restaurant_id AS INT)                        AS id_restaurante,
    CAST(name AS STRING)                              AS nome_restaurante,
    CAST(city AS STRING)                              AS cidade,
    CAST(address AS STRING)                           AS endereco,
    CAST(country AS STRING)                           AS pais,
    CAST(cnpj AS STRING)                              AS cnpj_sujo,
    CAST(phone_number AS STRING)                      AS telefone_sujo,
    CAST(cuisine_type AS STRING)                      AS tipo_cozinha,
    CAST(num_reviews AS INT)                          AS qtd_avaliacoes_historico,
    CAST(average_rating AS DECIMAL(3, 1))             AS nota_media,
    CAST(opening_time AS STRING)                      AS horario_abertura,
    CAST(closing_time AS STRING)                      AS horario_fechamento,
    CAST(lat AS DOUBLE)                               AS latitude,
    CAST(lon AS DOUBLE)                               AS longitude
  FROM
    normalized_table
),

-- 4. LIMPEZA
cleansed_table AS (
  SELECT
    TRIM(id_uuid)                                     AS id_uuid,
    CAST(id_restaurante AS STRING)                    AS id_restaurante,
    TRIM(nome_restaurante)                            AS nome_restaurante,
    LOWER(TRIM(cidade))                               AS cidade,
    TRIM(endereco)                                    AS endereco,
    LOWER(TRIM(pais))                                 AS pais,
    LOWER(TRIM(tipo_cozinha))                         AS tipo_cozinha,
    regexp_replace(cnpj_sujo, '[^0-9]', '')           AS cnpj,
    regexp_replace(telefone_sujo, '[^0-9]', '')       AS telefone,
    COALESCE(qtd_avaliacoes_historico, 0)             AS qtd_avaliacoes_historico,
    COALESCE(nota_media, 0.0)                         AS nota_media,
    COALESCE(horario_abertura, '00:00')               AS horario_abertura,
    COALESCE(horario_fechamento, '00:00')             AS horario_fechamento,
    COALESCE(latitude, 0.0)                           AS latitude,
    COALESCE(longitude, 0.0)                          AS longitude
  FROM
    typed_table
),

-- 5. METADADOS E SKs
silver_table AS (
  SELECT
    *,
    current_timestamp()                               AS _data_ingestao,
    'oracle-ubereats'                                 AS _sistema_fonte
  FROM
    cleansed_table
)

SELECT * FROM silver_table;
