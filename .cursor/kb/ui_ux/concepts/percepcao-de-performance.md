# Percepção de performance

> **Purpose**: A operação pode demorar; a *experiência* pode parecer rápida.  
> **Confidence**: 0.93

## Ideia central

**Ociosidade percebida** é o inimigo. Ocupar o tempo útil com feedback significativo reduz abandono.

## Técnicas (visão UX)

| Técnica | Efeito psicológico |
|---------|-------------------|
| **Skeleton loading** | Expectativa de estrutura; menos “tela congelada” |
| **Barra de progresso** | Sensação de avanço (melhor com % ou etapas reais) |
| **Mensagens de etapa** | “Etapa 3 de 4” ancora o usuário no processo |
| **Carregamento parcial** | Mostrar cabeçalho/cache enquanto detalhe carrega |
| **Cache** | Retorno instantâneo em revisitas |
| **Paginação** | Menos dados por request → primeira pintura mais rápida |
| **Lazy loading** | Imagens, rotas, subáreas pesadas sob demanda |

## Honestidade

Não simule progresso falso de forma enganosa em operações indeterminadas — use **indeterminado** ou etapas verificáveis.

## Exemplo de cópia de etapas (Databricks / SQL longo)

1. Conectando ao Databricks  
2. Iniciando cluster serverless  
3. Executando consulta  
4. Carregando resultado  

## Referências cruzadas

- [patterns/loading-etapas-e-cache.md](../patterns/loading-etapas-e-cache.md), [feedback-constante.md](feedback-constante.md)
