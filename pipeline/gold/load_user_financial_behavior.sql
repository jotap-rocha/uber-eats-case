CREATE OR REFRESH LIVE TABLE gold.financial_user_financial_behavior
COMMENT "Segmentação e Comportamento Financeiro (LTV). Baseado em snapshot consolidado do perfil."
AS
SELECT
  -- 1. Perfil Demográfico e de Conta
  id_usuario,
  nome_completo,
  cidade,
  estado,
  nivel_assinatura,
  status_conta,
  canal_aquisicao,
  flag_aceita_marketing,
  
  -- 2. Métricas de Engajamento e Tempo
  data_cadastro,
  data_ultimo_pedido,
  
  -- Recência: Quantos dias faz desde a última compra (Calculado apenas se houver data)
  CASE 
    WHEN data_ultimo_pedido IS NOT NULL AND data_ultimo_pedido > '1900-01-01' 
    THEN DATEDIFF(current_date(), data_ultimo_pedido)
    ELSE NULL 
  END AS dias_desde_ultima_compra,

  -- 3. KPIs Financeiros (Já pré-agregados na Silver)
  COALESCE(qtd_total_pedidos, 0) AS qtd_pedidos_pagos,
  ROUND(COALESCE(valor_total_gasto, 0), 2) AS ltv_gmv_total,
  
  -- Ticket Médio do Cliente (Calculado no voo)
  CASE 
    WHEN qtd_total_pedidos > 0 THEN ROUND(valor_total_gasto / qtd_total_pedidos, 2)
    ELSE 0.00 
  END AS ticket_medio_usuario,

  -- 4. Segmentação de Valor (Clusterização RFM Simplificada)
  CASE 
    WHEN valor_total_gasto >= 2000 THEN 'Diamante'
    WHEN valor_total_gasto >= 500  THEN 'Ouro'
    WHEN valor_total_gasto > 0     THEN 'Prata'
    ELSE 'Não comprou'
  END AS segmento_valor,

  current_timestamp() AS _data_processamento

FROM uber_eats.silver.silver_users;