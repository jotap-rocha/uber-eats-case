-- Fase 1/Azure: fonte trocada de Lakehouse Federation (consulta ao vivo no
-- MongoDB) para a Bronze real via Airbyte -> ADLS Gen2 -- decisao explicita
-- do usuario (ver BRAINSTORM_INGESTAO_AZURE_FASE1.md, Decisao #6, e
-- DESIGN_INGESTAO_AZURE_FASE1.md, item 26 do manifesto). A Lakehouse
-- Federation deixa de ser usada nesta fase.
--
-- Diferente das demais Silver deste projeto, esta tabela e um LIVE TABLE
-- em lote (nao STREAMING) -- o satelite "Perfil de Restaurante" e cadastro
-- estatico (seed unico via mongo/init/), sem CDC, sem stream de mudancas.

CREATE OR REFRESH LIVE TABLE silver.silver_restaurant_profile
COMMENT "Satélite documental do Restaurante (menu + horários de funcionamento). Origem MongoDB, cadastro estático (Onda 3, Etapa 2) — entidade nova, complementa silver_restaurants via restaurant_id."
AS

-- 1. LEITURA (Bronze via Airbyte -> ADLS Gen2, Fase 1/Azure)
WITH source_table AS (
  SELECT * FROM live.bronze_perfil_restaurante
),

-- 2. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(restaurant_id AS STRING)  AS id_restaurante,
    menu                           AS menu,
    horarios                       AS horarios,
    CAST(seeded_at AS TIMESTAMP)   AS data_seed
  FROM
    source_table
),

-- 3. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()  AS _data_ingestao,
    'mongo-ubereats'     AS _sistema_fonte
  FROM
    typed_table
)

SELECT * FROM silver_table;
