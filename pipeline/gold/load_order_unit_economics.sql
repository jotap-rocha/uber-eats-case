CREATE OR REFRESH LIVE TABLE gold.financial_order_unit_economics
COMMENT "Dataset focado em rentabilidade unitária por pedido. Integra Kafka, Postgres e MySQL."
AS
WITH orders_metrics AS (
  SELECT
    o.id_pedido,
    o.id_restaurante,
    o.id_motorista,
    p.valor_bruto AS valor_bruto,
    p.valor_imposto,
    p.taxa_plataforma AS custo_plataforma,
    p.taxa_provedor_cartao AS taxa_provedor_cartao,
    p.valor_estornado
  FROM silver_kafka_orders o
  INNER JOIN silver_kafka_payments p ON o.id_pedido = p.id_pedido
  WHERE
    p.status_pagamento = 'succeeded'             -- Apenas o que foi pago de fato
    AND p.valor_imposto < (p.valor_bruto * 0.15) -- Imposto deve ser menor que 15% do valor bruto
    AND p.valor_estornado <= p.valor_bruto       -- Estorno nunca pode ser maior que o valor pago
)
SELECT
  m.*,
  r.nome_restaurante,
  r.cidade AS cidade_restaurante,
  -- CÁLCULO GOLD 1: Margem de Contribuição (O que sobra em $ após pagar todos os custos diretos)
  (m.valor_bruto - m.valor_imposto - m.custo_plataforma - m.taxa_provedor_cartao) AS margem_contribuicao,
  -- CÁLCULO GOLD 2: Taxa de Retenção (Take Rate Líquido em %)
  -- Pega a Margem (fatia do bolo) e divide pelo Valor Bruto (bolo inteiro)
  round((margem_contribuicao / NULLIF(m.valor_bruto, 0)) * 100, 2) AS taxa_de_retencao,
  current_timestamp() AS _data_processamento
FROM orders_metrics m
LEFT JOIN silver_restaurants r ON m.id_restaurante = r.id_restaurante;