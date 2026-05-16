CREATE OR REFRESH LIVE TABLE gold.financial_restaurant_performance
COMMENT "Performance agregada por restaurante: Volume de vendas, Ticket Médio e Receita gerada para a plataforma."
AS
WITH transacoes_validas AS (
  SELECT
    o.id_pedido,
    o.cnpj_restaurante,
    p.valor_bruto,
    p.taxa_plataforma,
    p.valor_imposto
  FROM uber_eats.silver.silver_kafka_orders o
  INNER JOIN uber_eats.silver.silver_kafka_payments p ON o.id_pedido = p.id_pedido
  WHERE 
    p.status_pagamento = 'succeeded' 
    AND p.valor_imposto < (p.valor_bruto * 0.15) 
)
SELECT 
  -- Dados Cadastrais do Restaurante (Dimensão)
  r.cnpj,
  r.nome_restaurante,
  r.cidade AS cidade_restaurante,
  r.tipo_cozinha,
  r.nota_media AS avaliacao_app,
  
  -- KPIs Financeiros e Operacionais (Agregações)
  COUNT(DISTINCT t.id_pedido) AS qtd_pedidos_pagos,
  
  ROUND(SUM(t.valor_bruto), 2) AS gmv_total_vendido,
  
  ROUND(SUM(t.taxa_plataforma), 2) AS total_comissao_plataforma,
  
  -- Ticket Médio: Divide o total vendido pela quantidade de pedidos
  ROUND(SUM(t.valor_bruto) / COUNT(DISTINCT t.id_pedido), 2) AS ticket_medio,
  
  -- Take Rate Médio do Restaurante: Quantos % da venda desse restaurante fica com a gente
  ROUND((SUM(t.taxa_plataforma) / NULLIF(SUM(t.valor_bruto), 0)) * 100, 2) AS take_rate_restaurante_pct,

  current_timestamp() AS _data_processamento
  
FROM uber_eats.silver.silver_mysql_restaurants r
-- Usamos LEFT JOIN para garantir que até os restaurantes que não venderam nada apareçam (com valores zerados/nulos)
LEFT JOIN transacoes_validas t ON r.cnpj = t.cnpj_restaurante
GROUP BY 
  r.cnpj,
  r.nome_restaurante,
  r.cidade,
  r.tipo_cozinha,
  r.nota_media;