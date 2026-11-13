# 00 — Ideia: azure-warehouse

## Ideia (palavras do usuário, 2026-11-11)

> Vamos detalhar as 3 arquiteturas da Azure (Warehouse, Lakehouse e Kappa) e começar a subir o ambiente
> Azure. A arquitetura multicloud já está definida no roadmap (v2.2, Fase 1) e na ADR 012. O rascunho de
> planejamento da conta está em `azure/docs/PLANEJAMENTO_CONTA_AZURE.md`.
>
> - Warehouse: modelo dimensional e SCD2 sobre as 28 tabelas do Postgres e as 3 do Oracle, COPY INTO + MERGE
>   no Synapse Dedicated.
> - Lakehouse: Bronze, Silver e Gold no Databricks sobre o ADLS, com o contrato CDC canônico (`cdc_operation`,
>   `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`) e eventos `r` tratados como `c`.
> - Kappa: definir o problema de negócio (ele fixa as tabelas do conector dedicado e os event hubs, no máximo
>   10 no Standard) e o enriquecimento com o MongoDB.
>
> Pontos abertos: sink do Kafka Connect até o ADLS, acesso do Databricks Free Edition ao ADLS e o ajuste do
> Terraform em `azure/infra/fase1-ingestao/`.

**Fontes (não duplicadas aqui):** handoff de 2026-11-11 (fora do repo, em
`%TEMP%\handoff-azure-3-arquiteturas.md`; o conteúdo relevante vai para o `01-grill.md`),
[roadmap multi-cloud v2.2, Fase 1](../../../shared/docs/ROADMAP_ARQUITETURA_MULTICLOUD.md),
[ADR 012](../../../docs/adr/012-captura-dedicada-ao-kappa-na-fase-1.md),
[modelo físico](../../../shared/docs/modelagem/04-modelo-fisico.md),
[planejamento da conta](../../../azure/docs/PLANEJAMENTO_CONTA_AZURE.md).

## Escopo revisto pelo usuário (2026-11-12)

> Não quero planejar modelagem agora, pois preciso ver o dado primeiro. Quero planejar o provisionamento da
> conta, recursos e integrações que precisarão ser feitos. [...] Queria criar um agente de negócio, que me
> ajudasse a avaliar se a solução resolvia o problema de negócio.

- **Dentro:** conta Azure e pré-requisitos, recursos das 3 arquiteturas (Terraform), integrações (Debezium e
  Airbyte locais até o ADLS, Synapse lendo o ADLS, Databricks lendo o ADLS, conector dedicado até o Event Hubs,
  Stream Analytics com reference data) e o **agente-cliente**.
- **Fora (por ora):** modelo dimensional, Silver/Gold e lógica do Kappa. Voltam depois de o usuário ver o dado
  na Bronze.
- **Problema de negócio de cada arquitetura:** já definido em
  `shared/docs/OBJETIVOS_DE_NEGOCIO_POR_ARQUITETURA.md` (aceito em 2026-11-02, commit `a20172e`, só na branch
  local `feat/objetivos-de-negocio`, fora da `main`). Warehouse: fechamento financeiro e conciliação de
  repasses. Lakehouse: retenção do cliente e qualidade percebida. Kappa: torre de controle operacional por
  cidade. O documento é a base do agente-cliente, que ainda não existe.

## SI Assessment

Nível: **a**, dado 100% sintético (simulador e ShadowTraffic). Sem `[AVISO_LGPD]` nem `rules/pii.md`.
Implicações: valem as `rules/seguranca.md` e os invariantes do `CLAUDE.md` (não imprimir registros crus de
`customers`/`drivers`, segredos fora do git, bancos locais tratados como produção, nunca escrever em PRD).
Específico desta fase: credenciais da conta Azure e do service principal só em `.tfvars` fora do git ou em
variável de ambiente.

## Tipo de projeto

**c**, pipeline de dados em nuvem (Azure), com três arquiteturas sobre as mesmas fontes locais:

| Arquitetura | Stack prevista |
|---|---|
| Warehouse | ADLS Gen2 (landing) → Synapse Dedicated SQL Pool DW100c, `COPY INTO` + `MERGE`, SCD2 |
| Lakehouse | ADLS Gen2 → Databricks (Free Edition, a confirmar acesso) com Lakeflow/DLT e Unity Catalog |
| Kappa | Debezium dedicado → Event Hubs Standard → Stream Analytics, reference data do MongoDB |

Comum: Terraform (`azure/infra/`), budget alert, Debezium e Airbyte locais (Fase 0).

## Runtime Pipeline (gate 4a)

| Campo | Valor |
|---|---|
| Runtime | databricks |
| Declaração | humana (2026-11-11) |
| Notas | O runtime Spark é o do Lakehouse. Warehouse (Synapse) e Kappa (Stream Analytics) são SQL gerenciado e não passam por este gate |

## AI-DEV-KIT (gate 4a-bis)

| Campo | Valor |
|---|---|
| Instalado | sim |
| Declaração | humana (2026-11-11) |
| Status gate | aprovado |

## Medallion Gates (brainstorm)

| Item | Resposta |
|---|---|
| Camada-alvo | Multi-camada (Bronze, Silver, Gold) no Lakehouse; Warehouse e Kappa têm camadas próprias (a detalhar no grill) |
| Entidades/tabelas | Postgres (28): `cities`, `restaurants`, `products`, `stock_items`, `product_recipes`, `stock_movements`, `orders`, `restaurant_orders`, `order_items`, `order_status_transitions`, `restaurant_order_status_transitions`, `deliveries`, `shifts`, `driver_assignments`, `checkouts`, `payment_attempts`, `payments`, `payment_components`, `refunds`, `refund_components`, `restaurant_payouts`, `driver_payouts`, `tips`, `receipts`, `incidents`, `incident_items`, `driver_ratings`, `restaurant_ratings`. Oracle (3): `CITIES`, `CUSTOMERS`, `DRIVERS`. MongoDB (1): `restaurant_profiles` |
| Colunas ou amostra | DDL no [modelo físico](../../../shared/docs/modelagem/04-modelo-fisico.md): F1 (Postgres), F2.2 (Oracle), F3.1 e F3.2 (MongoDB); tipos na Bronze em F4.6 |
| `_source_system` | `postgres-ubereats`, `oracle-ubereats`, `mongodb-ubereats` (coluna `cdc_source_system`, F4.6) |
| Formato-fonte | Eventos Debezium (JSON, envelope `op/before/after/source`) e registros Airbyte (`_ab_cdc_*`); formato no ADLS a decidir no grill (sink) |
| JSON aninhado | Sim: envelope Debezium e documento do perfil (cardápio, horários). Bronze fiel, a Silver normaliza |
| SDDs separados | Não por branch (o usuário mantém tudo em `feat/planejamento-conta-azure`). As três arquiteturas entram como blocos de tasks do mesmo projeto, na ordem Warehouse → Lakehouse → Kappa |
| Genie / NL | A decidir no grill (o roadmap cita Genie como consumo) |
| Semântica / ontologia | A decidir no grill |

## Git

O usuário pediu para não criar outra branch: todo o projeto fica em `feat/planejamento-conta-azure`
(fora do tronco; passa no GIT_PREFLIGHT).

## Próximos passos

1. `/grill-with-docs`, uma pergunta por vez, na ordem Warehouse → Lakehouse → Kappa, e depois os pontos
   abertos (sink até o ADLS, Free Edition no ADLS, Terraform).
2. `harness-define` salva em `01-grill.md` (com as 10 perguntas obrigatórias de pipeline).
3. `/to-prd`, `/harness-architect`, `/to-tasks`, depois `harness-build` task a task.
