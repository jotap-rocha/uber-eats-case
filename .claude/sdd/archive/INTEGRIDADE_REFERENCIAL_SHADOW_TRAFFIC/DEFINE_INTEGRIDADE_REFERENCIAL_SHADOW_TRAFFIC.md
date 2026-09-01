# DEFINE: Correção de Integridade Referencial do Shadow Traffic (Onda 1)

| Campo | Valor |
|-------|-------|
| **Feature** | INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC |
| **Fase do roadmap** | Fase 0 — Fundação (`docs/plan.md`) |
| **Input** | `.claude/sdd/features/BRAINSTORM_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md` |
| **Status** | ✅ Shipped |
| **Data** | 2026-08-24 |

---

## Problem Statement

O gerador Shadow Traffic (`gen/minio/uber-eats.json`) tem 2 bugs de integridade referencial (payment_key e product_id não referenciam registros reais) e 1 chave de junção ambígua para Restaurante (cnpj vs. restaurant_id), além de Avaliação não se ligar a Usuário/Pedido e Entrega não ter coordenada real de origem — impedindo que o join entre as fontes de dados (critério de saída da Fase 0 em `docs/plan.md`) retorne resultado consistente sem órfãos. A correção completa (incluindo Usuário/Motorista) depende de unificar a geração Postgres real com o MinIO simulado — uma capacidade técnica ainda não verificada do ShadowTraffic — por isso esta feature resolve só o que é seguro dentro do MinIO (Onda 1).

## Target Users

| Usuário | Papel | Dor |
|---------|-------|-----|
| Autor do projeto (portfólio pessoal) | Desenvolvedor/arquiteto de dados validando o pipeline Bronze→Silver→Gold no Databricks | Sem integridade referencial corrigida, o Gold não consegue fazer joins consistentes (pedido↔restaurante hoje funciona por acidente via cnpj; pedido↔pagamento e item↔produto estão quebrados) |

## Goals

| Prioridade | Meta |
|------------|------|
| **MUST** | Corrigir `kafka/orders.payment_key` para fazer lookup em `kafka/payments.payment_id` |
| **MUST** | Corrigir `mongodb/items.product_id` para fazer lookup em `mysql/products.product_id` (formato compatível) |
| **MUST** | Migrar Restaurante para `restaurant_id` como chave de junção em `kafka/orders.restaurant_key` e `mysql/ratings.restaurant_identifier` |
| **MUST** | `mysql/ratings` ganha lookup obrigatório em `kafka/orders.order_id`; remove referência direta a restaurante |
| **MUST** | Adicionar `lat`/`lon` a `mysql/restaurants`; corrigir `kafka/route.start_lat/lon` para lookup real |
| **MUST** | Regerar os dados via Shadow Traffic com o gerador corrigido |
| **MUST** | Ajustar as colunas afetadas nos scripts Silver (`ingestion_kafka_orders.sql`, `ingestion_kafka_ratings.sql`, `ingestion_kafka_route.sql`, `ingestion_mysql_restaurants.sql`, `ingestion_mongodb_items.sql`) |
| **MUST** | Validar com join real na camada Gold (Databricks) que os relacionamentos corrigidos retornam resultado consistente, sem órfãos |
| **MUST** | Atualizar `docs/MODELO_CONCEITUAL_UBER_EATS.md` com o estado real pós-Build e o que fica pendente para Onda 2 (documento usado por outro agente para desenho no Miro) |
| **SHOULD** | Preservar a Bronze/Silver das entidades não afetadas sem alteração (não tocar em `kafka/status`, `kafka/events`, ou os streams fora do modelo core) |

## Success Criteria

- [ ] `kafka/orders.payment_key` e `mongodb/items.product_id` deixam de gerar valor independente — 100% dos registros regerados batem com um registro real de `kafka/payments`/`mysql/products`
- [ ] `kafka/orders.restaurant_key` e `mysql/ratings` usam `restaurant_id`, não mais `cnpj`, em 100% dos registros regerados
- [ ] `mysql/ratings` tem `order_id` preenchido em 100% dos registros regerados (não mais opcional/ausente)
- [ ] `mysql/restaurants` tem `lat`/`lon` em 100% dos registros; `kafka/route.start_lat/lon` corresponde ao `lat`/`lon` do restaurante do pedido associado
- [ ] Query de join no Gold (Databricks) entre pedido↔pagamento, pedido↔restaurante, item↔produto e avaliação↔pedido retorna 0 registros órfãos
- [ ] `docs/MODELO_CONCEITUAL_UBER_EATS.md` reflete literalmente o estado pós-Build, sem discrepância com o gerador/pipeline real

## Acceptance Tests

| ID | Cenário | Given | When | Then |
|----|---------|-------|------|------|
| AT-001 | payment_key correto | Gerador corrigido, dados regerados | Join `silver_kafka_orders` ↔ `silver_kafka_payments` por `id_pagamento` | 0 pedidos sem pagamento correspondente |
| AT-002 | product_id correto | Gerador corrigido, dados regerados | Join `silver_mongodb_items` ↔ `silver_mysql_products` por `id_produto` | 0 itens sem produto correspondente |
| AT-003 | Restaurante por ID | Gerador corrigido, dados regerados | Join `silver_kafka_orders` ↔ `silver_mysql_restaurants` por `id_restaurante` | 0 pedidos sem restaurante correspondente; nenhuma coluna usa `cnpj` como chave de join |
| AT-004 | Avaliação ligada ao pedido | Gerador corrigido, dados regerados | Join `silver_mysql_ratings` ↔ `silver_kafka_orders` por `id_pedido` | 100% das avaliações têm pedido correspondente |
| AT-005 | Coordenada de entrega coerente | Gerador corrigido, dados regerados | Comparar `start_lat/lon` de `silver_kafka_route` com `lat/lon` do restaurante do pedido | Coordenadas batem (mesma origem, não mais aleatória) |
| AT-006 | Modelo documentado atualizado | Build concluído | `docs/MODELO_CONCEITUAL_UBER_EATS.md` é revisado | Reflete as chaves/relacionamentos corrigidos desta feature e indica claramente o que é Onda 2 pendente |

## Out of Scope

- Migrar Usuário/Motorista de `cpf`/`license_number` para o UUID do Postgres real — depende de unificar geração Postgres×MinIO (Onda 2)
- Aposentar `mssql/users`, `mongodb/users`, `postgres/drivers` (MinIO)
- Coordenada de destino da Entrega (depende do lat/lon real do Usuário, que só existe no Postgres real — Onda 2)
- Reconciliar `silver_drivers_profile` (MinIO) com `silver_drivers_performance` (Postgres real via `ods_postgres_drivers`)
- Qualquer alteração em `kafka/status`, `kafka/events`, ou nos streams já fora do modelo core (`mysql/menu`, `mongodb/recommendations`, `kafka/search`)
- Investigação de viabilidade técnica do ShadowTraffic para lookup cruzado entre configs — vira discovery da Onda 2, não desta feature

## Constraints

- Correção deve ficar inteiramente dentro do MinIO (gerador + Silver correspondente) — nenhuma dependência da unificação com Postgres real
- Validação final deve usar o pipeline Databricks real (Silver → Gold), não uma query solta fora do fluxo de produção
- `docs/MODELO_CONCEITUAL_UBER_EATS.md` deve permanecer fiel ao estado real implementado a qualquer momento — é consumido por outro agente para gerar diagrama no Miro

## Assumptions

| ID | Suposição | Impacto se errada | Validada? |
|----|-----------|---------------------|-----------|
| A-001 | O ShadowTraffic consegue reprocessar `gen/minio/uber-eats.json` do zero sem afetar dados já carregados em Postgres real | Se houver acoplamento não previsto, regenerar pode corromper dados do Postgres | [ ] Validar no Build |
| A-002 | Os 5 scripts Silver listados são os únicos que referenciam as colunas afetadas (`user_key`/`restaurant_key`/`payment_key` de orders; `restaurant_identifier` de ratings; `product_id` de items; `start_lat/lon` de route) | Se outro script Silver/Gold também referenciar essas colunas, a correção fica incompleta | [ ] Confirmar via grep no Design |
| A-003 | O Gold atual (`load_order_unit_economics.sql`, `load_restaurant_performance.sql`) pode ser usado como está para validar os joins corrigidos, sem precisar de um Gold novo | Se os joins mudarem de coluna (`cnpj_restaurante` → `id_restaurante`), o Gold também precisa de ajuste, não só o Silver | [ ] Confirmar no Design — provavelmente **falsa**, ver nota abaixo |

**Nota sobre A-003:** os scripts Gold (`load_order_unit_economics.sql`, `load_restaurant_performance.sql`) hoje fazem `JOIN ... ON o.cnpj_restaurante = r.cnpj`. Se a Silver passar a expor `id_restaurante` em vez de `cnpj_restaurante`, o Gold **também** precisa de ajuste — isso deve ser tratado explicitamente no Design, não é opcional.

## Requisitos operacionais de pipeline (mandato)

Esta feature altera scripts do pipeline medalhão Databricks (Silver `ingestion_kafka_orders.sql`, `ingestion_kafka_ratings.sql`, `ingestion_kafka_route.sql`, `ingestion_mysql_restaurants.sql`, `ingestion_mongodb_items.sql`, e possivelmente Gold) — o sinal `medalhão bronze silver gold` de `PIPELINE_MANDATORY_PRACTICES.yaml` se aplica. Avaliação categoria a categoria:

| Categoria | Status | Justificativa |
|-----------|--------|----------------|
| Contrato de dados (DC-M01-05) | **N/A justificado** | Projeto de portfólio pessoal, sem consumidor externo do contrato — a mudança de schema é comunicada via `docs/MODELO_CONCEITUAL_UBER_EATS.md` (já é requisito MUST desta feature), que cumpre o mesmo papel comunicativo num contexto sem múltiplos times/stakeholders |
| Medalhão e UC (MED-M01-04) | **SHOULD** — MED-M02 aplica | Os scripts Silver tocados já usam projeção explícita (CAST + rename), não `SELECT *` — a correção deve preservar esse padrão nas colunas alteradas. MED-M04 (idempotência) já é atendido pelo padrão `STREAMING LIVE TABLE` existente, sem mudança necessária |
| Qualidade e quarentena (DQ-M01-05) | **N/A justificado** | Esta feature corrige a *origem* dos dados (gerador), não introduz um novo pipeline de qualidade/quarentena — os registros corrigidos não geram inválidos novos que precisem de política de quarentena |
| Schema drift (SD-M01-04) | **N/A justificado** | Não há Auto Loader com schema variável envolvido — o gerador tem schema fixo, e a mudança de coluna é deliberada (correção), não drift não controlado |
| Teams / alertas (TM-M01-06) | **N/A justificado** | Esta feature não altera o comportamento de falha/alerta do pipeline em produção — os padrões de Teams já documentados em `docs/DATABRICKS_TEAMS_PIPELINES.md` permanecem inalterados |
| Observabilidade (OBS-M01-03) | **N/A justificado** | Sem mudança de comportamento operacional/logging — fora do escopo desta correção pontual |
| Segurança (GOV-M01-02) | **N/A justificado** | Nenhum secret ou grant UC novo introduzido |
| Testes (TEST-M01-02) | **SHOULD** — TEST-M02 aplica | Recomenda-se `/pipeline-review-init` como validação adicional após o Build, antes de considerar a Fase 0 encerrada — não obrigatório para esta feature em si, mas relevante ao fechar a Fase 0 como um todo |
| PyODBC (PYODBC-M01-05) | **N/A** | Não há PyODBC/SQL Server nesta feature |

## Clarity Score Breakdown

| Elemento | Score | Justificativa |
|----------|-------|----------------|
| Problem | 3/3 | Claro, específico, com bugs e chaves nomeados exatamente |
| Users | 2/3 | Um único usuário/persona (projeto pessoal) |
| Goals | 3/3 | Priorizados MUST/SHOULD, mensuráveis, ligados a arquivos reais |
| Success | 3/3 | Critérios testáveis via join real no Gold |
| Scope | 3/3 | Onda 1 vs Onda 2 extensivamente delimitado no brainstorm |
| **Total** | **14/15** | Acima do mínimo de 12 — segue para Design sem gaps bloqueantes |

## Open Questions

- ~~A-003 (Gold precisa de ajuste em `cnpj_restaurante` → `id_restaurante`)~~ — resolvida no Design: confirmado, sim, ambos os scripts Gold precisam de ajuste.
- Resolvidas no Design: `payment_key`/`rating_key` não podiam ser "corrigidos" (circularidade) — removidos, não substituídos. `start_lat/lon` da Entrega não consegue amarrar ao restaurante exato do pedido com a mecânica atual do gerador — versão mais fraca (restaurante real genérico) aceita, AT-005 revisado.

## Revision History

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | 2026-08-24 | Documento inicial, extraído de `BRAINSTORM_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md` |
| 1.1 | 2026-08-24 | Status atualizado para Complete (Designed) após `/design` concluído; Open Questions resolvidas |
| 1.2 | 2026-08-24 | Build concluído (código/config); validação de integração (regeneração + join no Gold) pendente de execução manual pelo usuário — ver BUILD_REPORT |
| 1.3 | 2026-09-01 | Shipped e arquivado — validação do modelo relacional feita pelo usuário no Miro (diagrama derivado de `docs/MODELO_CONCEITUAL_UBER_EATS.md`); validação de join real no Gold (AT-001 a AT-005) não foi executada no Databricks, decisão consciente do usuário de aceitar a validação visual do modelo como critério suficiente |

---

## Status: ✅ Shipped
