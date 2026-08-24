# Genie Space — knowledge store e instruções

> **Propósito**: Como curar semântica e exemplos para SQL confiável e respostas “Trusted”.
> **Confiança**: 0.92
> **MCP Validated**: null

## Overview

O **knowledge store** é metadado e lógica de negócio **escopados ao Genie Space** (não alteram tabelas UC): descrições e sinônimos, prompt matching, relacionamentos de join e expressões SQL reutilizáveis (medidas, filtros, dimensões). As **instruções** incluem exemplos SQL (estáticos ou com parâmetros `:nome`), funções SQL registradas em UC e blocos de texto geral. Limites: 100 instruções e 200 snippets de knowledge store por espaço.

## O padrão

```sql
-- Exemplo de “query exemplo”: título = pergunta natural típica do usuário
-- SQL = lógica que você quer que a Genie imite ou reutilize
SELECT regiao, SUM(valor) AS receita
FROM vendas.curated.fato_pedido
WHERE data_pedido >= date_trunc('quarter', current_date()) - interval '3 months'
GROUP BY ALL;
```

Parâmetros (`:periodo`, etc.) permitem respostas **Trusted** quando o texto parametrizado coincide com a execução.

## Referência rápida

| Artefato | Função |
|----------|--------|
| Joins no knowledge store | `JOIN` correto entre tabelas do domínio |
| SQL expressions | KPIs e filtros recorrentes |
| Texto (aba Text) | Jargão global, calendário fiscal, idioma/formato |
| Função UC | Lógica oculta; resposta pode ser Trusted; usuários precisam `EXECUTE` |

## Erros comuns

### Errado

Instruções contraditórias ou ambíguas — o modelo é não determinístico; conflitos aumentam respostas incoerentes.

### Certo

Iterar com [best practices](https://docs.databricks.com/aws/en/genie/best-practices): revisar inconsistências, priorizar exemplos que capturam lógica **específica** da empresa.

## Relacionados

- [genie-dados-acesso-e-queries.md](genie-dados-acesso-e-queries.md)
- [../patterns/checklist-configuracao-genie-space.md](../patterns/checklist-configuracao-genie-space.md)

## Fontes

- [Knowledge store](https://docs.databricks.com/aws/en/genie/knowledge-store)
- [Set up and manage — Instructions](https://docs.databricks.com/en/genie/set-up)
