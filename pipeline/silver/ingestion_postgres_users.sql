CREATE OR REFRESH STREAMING LIVE TABLE silver.silver_users
COMMENT "Tabela de Usuários. Visão unificada do perfil, métricas de gastos e status de assinatura."
AS

-- 1. LEITURA
WITH source_table AS (
  SELECT * FROM STREAM(live.ods_users)
),

-- 2. NORMALIZAÇÃO (Pass-through)
normalized_table AS (
  SELECT * FROM source_table
),

-- 3. RENOMEAÇÃO E TIPAGEM
typed_table AS (
  SELECT
    CAST(user_id AS STRING)                           AS id_usuario,
    CAST(first_name AS STRING)                        AS nome_primeiro,
    CAST(last_name AS STRING)                         AS sobrenome,
    CAST(name AS STRING)                              AS nome_completo,
    CAST(username AS STRING)                          AS usuario_login,
    CAST(email AS STRING)                             AS email,
    CAST(phone_number AS STRING)                      AS telefone,
    CAST(gender AS STRING)                            AS genero,
    CAST(date_of_birth AS DATE)                       AS data_nascimento,
    CAST(address_line1 AS STRING)                     AS endereco_linha1,
    CAST(address_line2 AS STRING)                     AS endereco_linha2,
    CAST(city AS STRING)                              AS cidade,
    CAST(state AS STRING)                             AS estado,
    CAST(country AS STRING)                           AS pais,
    CAST(postal_code AS STRING)                       AS cep,
    CAST(lat AS DOUBLE)                               AS latitude,
    CAST(lon AS DOUBLE)                               AS longitude,
    CAST(timezone AS STRING)                          AS fuso_horario,
    CAST(total_orders AS INT)                         AS qtd_total_pedidos,
    CAST(total_spend AS DECIMAL(18, 2))               AS valor_total_gasto,
    CAST(average_rating AS DECIMAL(3, 1))             AS nota_media_usuario,
    CAST(status AS STRING)                            AS status_conta,
    CAST(subscription_tier AS STRING)                 AS nivel_assinatura,
    CAST(roles AS STRING)                             AS perfis_acesso,
    CAST(referral_code AS STRING)                     AS codigo_indicacao,
    CAST(referral_source AS STRING)                   AS canal_aquisicao,
    CAST(preferred_language AS STRING)                AS idioma_preferido,
    CAST(phone_verified AS BOOLEAN)                   AS flag_telefone_verificado,
    CAST(email_verified AS BOOLEAN)                   AS flag_email_verificado,
    CAST(marketing_opt_in AS BOOLEAN)                 AS flag_aceita_marketing,
    CAST(two_factor_enabled AS BOOLEAN)               AS flag_2fa_ativo,
    CAST(has_active_payment_method AS BOOLEAN)        AS flag_pagamento_ativo,
    CAST(payment_methods_count AS INT)                AS qtd_metodos_pagamento,
    CAST(ip_address AS STRING)                        AS ip_cadastro,
    CAST(device_type AS STRING)                       AS tipo_dispositivo,
    CAST(app_version AS STRING)                       AS versao_app,
    CAST(created_at AS TIMESTAMP)                     AS data_criacao_registro,
    CAST(updated_at AS TIMESTAMP)                     AS data_atualizacao_registro,
    CAST(signup_date AS TIMESTAMP)                    AS data_cadastro,
    CAST(last_login AS TIMESTAMP)                     AS data_ultimo_login,
    CAST(last_order_date AS TIMESTAMP)                AS data_ultimo_pedido,
    CAST(subscription_renewal_date AS TIMESTAMP)      AS data_renovacao_assinatura

  FROM
    normalized_table
),

-- 4. LIMPEZA
cleansed_table AS (
  SELECT
    TRIM(id_usuario)                                  AS id_usuario,
    TRIM(nome_primeiro)                               AS nome_primeiro,
    TRIM(sobrenome)                                   AS sobrenome,
    TRIM(nome_completo)                               AS nome_completo,
    LOWER(TRIM(email))                                AS email,
    TRIM(telefone)                                    AS telefone,
    UPPER(TRIM(genero))                               AS genero,
    LOWER(TRIM(cidade))                               AS cidade,
    UPPER(TRIM(estado))                               AS estado,
    LOWER(TRIM(pais))                                 AS pais,
    COALESCE(qtd_total_pedidos, 0)                    AS qtd_total_pedidos,
    COALESCE(valor_total_gasto, 0.00)                 AS valor_total_gasto,
    COALESCE(nota_media_usuario, 5.0)                 AS nota_media_usuario,
    COALESCE(flag_telefone_verificado, FALSE)         AS flag_telefone_verificado,
    COALESCE(flag_email_verificado, FALSE)            AS flag_email_verificado,
    COALESCE(flag_aceita_marketing, FALSE)            AS flag_aceita_marketing,
    COALESCE(flag_2fa_ativo, FALSE)                   AS flag_2fa_ativo,
    COALESCE(flag_pagamento_ativo, FALSE)             AS flag_pagamento_ativo,
    COALESCE(data_cadastro, CAST('1900-01-01 00:00:00' AS TIMESTAMP)) AS data_cadastro,
    data_nascimento,
    endereco_linha1,
    endereco_linha2,
    cep,
    latitude,
    longitude,
    fuso_horario,
    usuario_login,
    status_conta,
    nivel_assinatura,
    perfis_acesso,
    codigo_indicacao,
    canal_aquisicao,
    idioma_preferido,
    qtd_metodos_pagamento,
    ip_cadastro,
    tipo_dispositivo,
    versao_app,
    data_criacao_registro,
    data_atualizacao_registro,
    data_ultimo_login,
    data_ultimo_pedido,
    data_renovacao_assinatura

  FROM
    typed_table
),

-- 5. METADADOS
silver_table AS (
  SELECT
    *,
    current_timestamp()                               AS _data_ingestao,
    'postgres-ods'                                    AS _sistema_fonte
  FROM
    cleansed_table
)

SELECT * FROM silver_table;