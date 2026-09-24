# BUILD REPORT: Diversificação de Fontes de Dados — Etapa 3 (Pedido/Pagamento com mutação real no Oracle)

| Campo | Valor |
|-------|-------|
| **Feature** | DIVERSIFICACAO_FONTES_UBEREATS |
| **Escopo deste Build** | Etapa 3 do DESIGN — Pedido/Pagamento/Item de Pedido/Recibo migram do MinIO simulado para o Oracle real, com mutação de linha (fork+stateMachine+op:update) em `orders`/`payments`. `kafka/status` e `kafka/events` (histórico append-only) são aposentados. Aplicada também a convenção de nomenclatura Silver/Bronze por domínio a **todo** o projeto (instrução explícita do usuário), não só às tabelas desta etapa |
| **Input** | `.claude/sdd/features/DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md` |
| **Data** | 2026-09-06 |

## Summary

| Métrica | Valor |
|---------|-------|
| Arquivos criados | 9 (DDL Oracle de Pedido/Pagamento, 4 Bronze, 4 Silver) |
| Arquivos editados | 3 (`gen/unified/uber-eats.json.template`, `debezium/oracle-connector.json.template`, `pipeline/README.md`) + `.gitignore` |
| Arquivos removidos | 6 (Silver antigas de `kafka_orders`/`kafka_payments`/`kafka_receipts`/`kafka_status`/`kafka_events`/`mongodb_items`) |
| Verificações estáticas | JSON validado após cada edição (`ConvertFrom-Json`) |
| Verificação de integração | **Executada em ambiente real, ponta a ponta** — 2 bugs reais encontrados e corrigidos |

## O que foi validado de verdade (não só código estático)

Ambiente completo (Postgres + Oracle + Redpanda + Kafka Connect + MinIO + MongoDB) subido do zero (`docker-compose down -v` + `up`) para garantir que os PKs sequenciais de `orders`/`payments` nascessem em 1, sem resíduo da Etapa 2:

1. ✅ `sql/oracle/03_create_tables_pedido_pagamento.sh` roda sem erro — 4 tabelas (`orders`, `payments`, `order_items`, `receipts`) criadas com `SUPPLEMENTAL LOG DATA (ALL) COLUMNS`, sem FK, datas como `VARCHAR2` (mesmo padrão da Etapa 2)
2. ✅ **Mutação real fork+stateMachine+op:update funcionando no Oracle** (mecanismo antes só provado no Postgres, na Etapa 1) — `orders` populou com as 9 fases do ciclo de vida (`Order Placed` → ... → `Completed`); `payments` com os 4 estados finais (`pending`/`succeeded`/`failed`/`refunded`)
3. ✅ `order_items` (fork com lookup no `order_id` sequencial do Oracle) e `receipts` (lookup direto) populam corretamente cross-connection
4. ✅ Debezium/Kafka Connect captura os `UPDATE`s reais de status como `"op":"u"` com `before`/`after` completos (confirmado via `rpk topic consume` nos tópicos `oracle.UBEREATS.ORDERS` e `oracle.UBEREATS.PAYMENTS`) — este era o objetivo central da etapa: substituir histórico append-only por mutação de linha capturada via CDC de verdade
5. ✅ **Bônus, gap conhecido desde a Etapa 2 agora fechado:** satélite MongoDB (`mongo-ubereats` + seed `01_perfil_restaurante.js`) testado em ambiente real pela primeira vez — 500 documentos (`RESTAURANT_COUNT`) criados com estrutura de menu + horários íntegra

## Bugs reais encontrados e corrigidos

| # | Bug | Sintoma | Correção |
|---|-----|---------|----------|
| 1 | Generator `orders` usava `user_key`/`restaurant_key`/`driver_key` como nomes de campo no `row`, mas as colunas reais da tabela Oracle são `user_id`/`restaurant_id`/`driver_id` | `java.sql.BatchUpdateException: ORA-00904: "DRIVER_KEY": invalid identifier` — ShadowTraffic usa a chave do JSON como nome de coluna no INSERT, não um alias lógico | Renomear as 3 chaves de lookup no `row` de `orders` para os nomes reais de coluna; corrigir também `pipeline/bronze/ingest_oracle_orders.sql` (`USER_KEY`→`USER_ID` etc.) e `pipeline/silver/ingestion_oracle_orders.sql` (mesma correção) |
| 2 | Generator `payments` usava `order_key` como nome de campo no `row`, mas a coluna real é `order_id` | `ORA-00904: "ORDER_KEY": invalid identifier` — mesmo mecanismo do bug #1 | Renomear a chave de lookup no `row` de `payments`; corrigir também `pipeline/bronze/ingest_oracle_payments.sql` (`ORDER_KEY`→`ORDER_ID`) e `pipeline/silver/ingestion_oracle_payments.sql` |

Os dois bugs têm a mesma causa raiz: nas Etapas 1 e 2, os nomes `*_key` eram convenção segura porque o Postgres/MySQL alvo aceitava qualquer nome de coluna definido dinamicamente ali perto, ou porque a tabela ainda não existia fisicamente com esse nome exato. A partir da Etapa 3, `orders`/`payments` já existem no Oracle com DDL fixo (`sql/oracle/03_create_tables_pedido_pagamento.sh`), então o nome do campo no `row` do ShadowTraffic passou a precisar bater exatamente com o nome da coluna — o padrão `_key` não tinha mais função e virou bug potencial. Nenhum problema equivalente apareceu em `order_items`/`receipts`, que já nasceram usando os nomes reais de coluna desde a escrita inicial.

**Nenhum outro erro de runtime observado** — nem no ShadowTraffic, nem no Kafka Connect, nem no Oracle, após a correção acima.

## Tasks executadas

| Task | Status | Notas |
|------|--------|-------|
| `sql/oracle/03_create_tables_pedido_pagamento.sh` | ✅ | `orders`, `payments`, `order_items`, `receipts` — sem FK, datas `VARCHAR2`, `txn_timestamp` (não `timestamp`, palavra reservada) |
| `gen/unified/uber-eats.json.template`: migração de `orders`/`payments`/`order_items`/`receipts` para `connection: oracle` + fork+stateMachine em `orders`/`payments` | ✅ | Bugs #1 e #2 corrigidos; `kafka/status` e `kafka/events` removidos por completo (19→17 geradores) |
| `debezium/oracle-connector.json.template`: `table.include.list` estendido | ✅ | Agora inclui as 4 novas tabelas; testado com snapshot inicial completo (638 orders, 788 payments, 14980 order_items, 24 receipts no momento do snapshot) |
| `pipeline/bronze/ingest_oracle_{orders,payments,order_items,receipts}.sql` | ✅ | Contrato canônico de CDC (`cdc_operation`/`cdc_commit_ts`/`cdc_sequence`/`cdc_source_system`), `SEQUENCE BY cdc_sequence` (SCN) — decisivo para `orders`, que sofre 8 UPDATEs de status por ciclo de vida |
| `pipeline/silver/ingestion_oracle_{orders,payments,order_items,receipts}.sql` | ✅ | Substituem `ingestion_kafka_orders`/`ingestion_kafka_payments`/`ingestion_mongodb_items`/`ingestion_kafka_receipts`; `status`/`updated_at` agora refletem mutação real de linha, não mais um stream de eventos separado |
| Remoção de `ingestion_kafka_status.sql`, `ingestion_kafka_events.sql`, `ingestion_kafka_orders.sql`, `ingestion_kafka_payments.sql`, `ingestion_kafka_receipts.sql`, `ingestion_mongodb_items.sql` | ✅ | Histórico append-only aposentado; grep sweep confirmou nenhuma referência residual fora de comentários narrativos |
| Convenção de nomenclatura Silver/Bronze por domínio aplicada a **todo** o projeto | ✅ | Já entregue majoritariamente no commit de rename (`817dade`, anterior a esta etapa); Etapa 3 nasceu as 4 tabelas novas já com o nome de domínio (`silver_orders`, não `silver_kafka_orders`) |
| `pipeline/README.md` | ✅ | Atualizado: tabela de fontes agora reflete Oracle real, MongoDB satélite e MinIO reduzido (Pedido/Pagamento/Item/Recibo saíram); contagem de scripts e descrição do Bronze corrigidas |
| `.gitignore` | ✅ | Adicionadas `gen/unified/uber-eats.json` e `mongo/init/01_perfil_restaurante.js` — arquivos gerados com segredo injetado (senha Oracle) que não estavam ignorados, mesmo padrão já usado para `gen/postgres/drivers.json`/`users.json` |

## Pendências (não bloqueantes para fechar a Etapa 3, mas registradas)

1. **Pipeline Bronze→Silver→Gold real no Databricks não foi executado** — validação local cobre Oracle, ShadowTraffic e CDC (Debezium/Redpanda), mas não a leitura via `read_kafka()` dentro do Lakeflow real, que exige um workspace Databricks. Recomenda-se rodar isso antes do `/ship` da feature completa, mesma disciplina já registrada nas Etapas 1/2.
2. **Lakehouse Federation para MongoDB** ainda não validada (depende de uma conexão Unity Catalog criada manualmente na plataforma — fora do alcance de Docker/scripts locais). O seed em si já foi validado nesta etapa (ver item 5 acima).
3. **`docs/MODELO_CONCEITUAL_UBER_EATS.md`** ainda não foi atualizado para refletir o estado final da Onda 3 (Pedido/Pagamento no Oracle, MongoDB satélite) — item pendente do manifest do DESIGN, a fazer antes do `/ship`.

## Pendências antes do commit

Conforme `.claude/skills/git-boas-praticas-versionamento/SKILL.md`, commit é proposto e aguarda confirmação. Sugestão de mensagem:

```text
feat(oracle): migra Pedido/Pagamento para Oracle com mutacao real (Onda 3, Etapa 3)

Orders/payments/order_items/receipts saem do MinIO simulado e passam a
viver no Oracle real. Orders e payments ganham mutacao de linha via
fork+stateMachine+op:update (mesmo mecanismo ja provado no Postgres na
Etapa 1, agora combinado com Oracle pela primeira vez) -- substitui o
historico append-only kafka/status e kafka/events, que sao removidos
por completo junto com as Silver correspondentes.

Bronze/Silver novos leem o CDC via Debezium/Kafka Connect, com o
contrato canonico ja estabelecido na Etapa 2. Adiciona .gitignore para
os artefatos gerados com segredo injetado (uber-eats.json, seed do
Mongo).

Validado ponta a ponta em ambiente real: 2 bugs reais encontrados e
corrigidos (nomes de campo no gerador nao batiam com o nome real da
coluna Oracle em orders/payments). Confirmado via consumo direto dos
topicos Kafka que os UPDATEs de status chegam como CDC real (op:u,
before/after). Satelite MongoDB tambem validado em ambiente real pela
primeira vez (gap pendente desde a Etapa 2).

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```

## Status: ✅ COMPLETE (código + validação de integração ponta a ponta no que é testável localmente)

**Validado de verdade:** Oracle (DDL + mutação real), ShadowTraffic (fork+stateMachine+op:update em Oracle), Debezium/Redpanda (CDC de UPDATE real), MongoDB satélite.
**Não validado:** pipeline Bronze→Silver→Gold completo no Databricks (requer workspace real).
**Recomendo:** antes do `/ship` da feature completa, rodar o pipeline Databricks real e atualizar `docs/MODELO_CONCEITUAL_UBER_EATS.md`.
