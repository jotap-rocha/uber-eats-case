# Padrão — Loading por etapas, cache e sensação de velocidade

> **Purpose**: Implementação alinhada à UX de operações longas e telas de dados.  
> **Confidence**: 0.93

## Quando usar

- Chamadas > ~300 ms perceptíveis ou pipelines multi-etapa (warehouse, cluster, SQL pesado).
- Listagens grandes onde primeira pintura importa.

## Blocos de solução

### 1. Skeleton loading

- Espelhe o **layout final** (cards, linhas de tabela), não um spinner solto no centro.
- shadcn: componente `Skeleton`; mantenha mesmas alturas aproximadas para evitar CLS.

### 2. Barra de progresso

- **Determinada**: quando backend informa percentual.
- **Indeterminada**: spinner/barra sem porcentagem para queries sem ETA — prefira honestidade.

### 3. Mensagens de etapa

Lista textual ou stepper com ícones (`CheckCircle2`, `Loader2`):

1. Conectando ao Databricks  
2. Iniciando cluster serverless  
3. Executando consulta  
4. Carregando resultado  

Atualize só quando o backend confirmar transição (polling/WebSocket) para não mentir.

### 4. Carregamento parcial

- Mostrar **shell da página** + dados em cache (React Query `placeholderData`, `initialData`).
- Stream de resultados: primeiras linhas antes do fim do scan.

### 5. Cache

- React Query: `staleTime` alto para dados semi-estáticos; invalidação explícita após mutações.
- HTTP cache / ETag onde aplicável em APIs próprias.

### 6. Paginação

- Server-side para datasets grandes; cliente só quando volume controlado.
- Sempre exibir intervalo e total (ou “mais de X”).

### 7. Lazy loading

- `React.lazy` + `Suspense` para rotas pesadas.
- Imagens: `loading="lazy"`; listas: virtualização ou infinite scroll com footer estável.

## Anti-padrões

- Spinner global bloqueando UI inteira para ação trivial.
- Etapas fake que avançam no `setInterval` sem correlação com job real.

## Referências

- [concepts/percepcao-de-performance.md](../concepts/percepcao-de-performance.md)
- [concepts/feedback-constante.md](../concepts/feedback-constante.md)
