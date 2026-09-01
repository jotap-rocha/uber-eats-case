# BUILD REPORT: Correção de Integridade Referencial do Shadow Traffic (Onda 1)

| Campo | Valor |
|-------|-------|
| **Feature** | INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC |
| **Input** | `.claude/sdd/features/DESIGN_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md` |
| **Data** | 2026-08-24 |

## Summary

| Métrica | Valor |
|---------|-------|
| Tasks de código/config | 7/7 completas |
| Arquivos editados | 7 (1 gerador, 3 Silver, 2 Gold, 1 doc) |
| Verificações estáticas | 4/4 passaram |
| Verificações de integração | **Pendentes — exigem execução manual do usuário** |

## Tasks com atribuição de agente

| Task | Agente | Status | Notas |
|------|--------|--------|-------|
| Editar `gen/minio/uber-eats.json` | (direto) | ✅ | 6 mudanças: remove `payment_key`/`rating_key`, migra `restaurant_key`, corrige `product_id`, adiciona `lat`/`lon` a restaurantes, corrige `route.start_lat/lon`, adiciona `order_id` a ratings |
| Editar `ingestion_kafka_orders.sql` | (direto) | ✅ | Manifesto indicava `@databricks-data-engineer`; executado direto por já ter o conteúdo exato definido no Design |
| Editar `ingestion_kafka_ratings.sql` | (direto) | ✅ | Idem — inclui correção do nome enganoso `id_usuario` → `id_avaliacao_uuid` |
| Editar `ingestion_mysql_restaurants.sql` | (direto) | ✅ | Adiciona `latitude`/`longitude` |
| Editar `load_order_unit_economics.sql` | (direto) | ✅ | Join por `id_restaurante` |
| Editar `load_restaurant_performance.sql` | (direto) | ✅ | Join por `id_restaurante`; `cnpj` mantido como atributo de saída |
| Editar `docs/MODELO_CONCEITUAL_UBER_EATS.md` | (direto) | ✅ | Reflete estado real pós-Build + pendências Onda 2 |

## Verificação estática (executada agora)

| ID | Verificação | Resultado |
|----|--------------|-----------|
| V-001 | Gerador sem `payment_key`/`rating_key` | ✅ Pass — 0 ocorrências |
| — | JSON válido (`json.load`) | ✅ Pass — 20 generators preservados |
| — | Nenhuma referência solta a `cnpj_restaurante`/`id_classificacao`/`restaurant_identifier` no pipeline | ✅ Pass — 0 ocorrências |
| — | `silver_mysql_ratings` não é consumido por nenhum Gold existente | ✅ Confirmado — renomear suas colunas não quebra nada downstream |

## Verificação de integração — PENDENTE (requer ambiente rodando)

Não tenho acesso para regenerar dados via Shadow Traffic nem executar o pipeline Databricks a partir desta sessão. Os itens abaixo (V-002 a V-007 do Design) precisam ser executados manualmente antes de considerar a feature pronta para `/ship`:

| ID | O que fazer | Comando/local |
|----|-------------|----------------|
| V-002 | Regenerar dados | `.\scripts\start-all.ps1` (ou reiniciar só o gerador Shadow Traffic conforme `docs/automacao/README.md`) |
| V-003 | Rodar pipeline Databricks completo | Bronze → Silver → Gold no workspace, usando os scripts editados |
| V-004 | Join pedido↔pagamento sem órfãos | `SELECT COUNT(*) FROM silver_kafka_orders o LEFT JOIN silver_kafka_payments p ON o.id_pedido=p.id_pedido WHERE p.id_pedido IS NULL` → esperado 0 |
| V-005 | Join item↔produto sem órfãos | `SELECT COUNT(*) FROM silver_mongodb_items i LEFT JOIN silver_mysql_products pr ON i.id_produto=pr.id_produto WHERE pr.id_produto IS NULL` → esperado 0 |
| V-006 | Join pedido↔restaurante sem órfãos | `SELECT COUNT(*) FROM silver_kafka_orders o LEFT JOIN silver_mysql_restaurants r ON o.id_restaurante=r.id_restaurante WHERE r.id_restaurante IS NULL` → esperado 0 |
| V-007 | Avaliação↔pedido | `SELECT COUNT(*) FROM silver_mysql_ratings rt LEFT JOIN silver_kafka_orders o ON rt.id_pedido=o.id_pedido WHERE o.id_pedido IS NULL` → esperado 0 |
| V-008 | Gold executa sem erro | Rodar `load_order_unit_economics` e `load_restaurant_performance`; conferir resultado não-vazio |

**Risco técnico a observar durante a regeneração:** `mysql/ratings.order_id` faz lookup em `kafka/orders`, que aparece **depois** de `mysql/ratings` no array de generators do JSON. Um precedente no próprio arquivo (`postgres/inventory` já referencia `mysql/restaurants`/`mysql/products`, que também vêm depois) sugere que o ShadowTraffic tolera isso, mas **não foi confirmado para este caso específico** — se a regeneração falhar ou gerar `order_id` vazio em `mysql/ratings`, mover o bloco `mysql/ratings` para depois de `kafka/orders` no array resolve.

## Issues Encountered

Nenhum na parte de código. O risco técnico acima (ordem de geração) é o único ponto não verificável sem rodar o ambiente de verdade.

## Pendências antes do commit

Conforme `.claude/skills/git-boas-praticas-versionamento/SKILL.md`, commit é proposto e aguarda confirmação. Sugestão de mensagem:

```text
fix(pipeline): corrige integridade referencial do Shadow Traffic (Onda 1)

Remove payment_key/rating_key de kafka/orders (eram circulares); migra
Restaurante para restaurant_id como chave de junção; liga Avaliação ao
Pedido; corrige product_id de item de pedido; adiciona lat/lon a
restaurantes e liga a origem da Entrega a coordenada real. Ajusta Silver
e Gold correspondentes. Atualiza docs/MODELO_CONCEITUAL_UBER_EATS.md
com o estado real e as pendências da Onda 2 (unificação Postgres×MinIO).
```

## Status: ⚠️ COMPLETE (código) — validação de integração pendente

**Não recomendo `/ship` ainda** — o `Definition of Done` desta feature (Success Criteria do Define) exige confirmar 0 órfãos via join real no Gold, o que só o usuário pode executar no ambiente Databricks. Após rodar V-002 a V-008 e confirmar os resultados, retomar com `/ship`.
