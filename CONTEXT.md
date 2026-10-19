> **Este repositorio e o projeto `uber-eats-case`, nao o Agent Harness Canonico.**
> Nao copie o guia do repositorio canonico do harness. Refine com `/grill-me`, `/grill-with-docs` ou `harness-architect`.

# Pipeline de Dados Uber Eats - Portfolio - Contexto rapido

> Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.

## O que e este projeto?

Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.

## Estrutura principal

| Componente | Descricao | Observacao |
|------------|-----------|------------|
| `aws/` | Trilha de ingestao AWS (Fase 2) | `aws/src/` (Lambdas), `aws/infra/` (Terraform: DMS, Kinesis, DataSync, Redshift, Glue), `aws/tests/`, `aws/requirements.txt` |
| `azure/` | Trilha de ingestao Azure (Fase 1) | `azure/src/`, `azure/infra/`, `azure/tests/`, `azure/docs/` |
| `gcp/` | Trilha de ingestao GCP (Fase 3) | `gcp/src/`, `gcp/infra/`, `gcp/tests/`, `gcp/docs/`, `gcp/requirements.txt` |
| `shared/` | Comum as 3 nuvens | `shared/pipeline/` (Bronze/Silver/Gold Databricks), `shared/gen/` (ShadowTraffic), `shared/mongo/`, `shared/sql/`, `shared/docs/` |
| `config/` | Dado de conexao/ambiente por nuvem | `config/{aws,azure,gcp,shared}/` — templates de connector Debezium, hadoop-conf, deploy |
| `scripts/` | Scripts auxiliares | Subpastas por assunto: `infra/`, `shadowtraffic/`, `all/`, `ingestion/`, `tooling/`, `lib/` |
| `docs/` | *(nao existe mais na raiz)* | Documentacao movida para `shared/docs/` (comum) e `{cloud}/docs/` (especifica); indice em `shared/docs/00-INDEX.md` |
| `.cursor/` | Agentes, KB, comandos e SDD | Fonte canonica do formato agentic |

## Comandos de validacao

```bash
# Instalar dependencias, se necessario
.\scripts\all\start-all.ps1

# Validar o projeto
python3 scripts/tooling/validate-agent-router.py
```

## Ambientes

| Ambiente | Uso | Observacao |
|----------|-----|------------|
| `local` | Desenvolvimento | Ajustar conforme o projeto |
| `dev` | Testes integrados | Ajustar conforme o projeto |
| `prd` | Producao | Ajustar conforme o projeto |

## Agentic / SDD

| Recurso | Quando usar |
|---------|-------------|
| `get_started/START_HERE.md` | Onboarding do formato agentic |
| `.cursorrules` | Regras do assistente e padroes do projeto |
| `.cursor/CURSOR.MD` | Contexto principal do Cursor |
| `.cursor/commands/core/router.md` | Roteamento de agentes |
| `.cursor/sdd/architecture/` | Contratos SDD |
| `.cursor/sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml` | **Mandatos pipeline** — Teams, drift, quarentena, sentinela |
| `shared/docs/MANDATOS_PIPELINE_DADOS.md` | Guia humano dos mandatos |
| `.cursor/agents/domain/uber-eats-case-expert.md` | Agente especialista deste projeto |
| `get_started/DEV_LOOP_Guia_Comandos.md` | Guia passo a passo do Dev Loop (L2): requirements → design → `/dev` |
| `.cursor/commands/workflow-dev-loop/` | Workflow estruturado: `/devloop-init`, `/devloop-phase`, `/devloop-execute` |
| `get_started/SDD_Guia_Comandos.md` | Guia dos comandos SDD (L3) |
| `agentspec/INSTALL_AGENTSPEC.md` | Instalar Agent Spec do zero em projeto vazio (`install_agentspec.py`) |

## Problemas comuns

| Sintoma | Causa provavel | Onde agir |
|---------|----------------|-----------|
| Falha de validacao local | Dependencias, variaveis ou path | `README.md`, `CONTEXT.md`, `scripts/` |
| Erro de credencial | Secret ausente ou ambiente errado | Documentacao de configuracao do projeto |
| Teste/validacao falha | Contrato ou dependencia quebrada | Logs e comando de validacao |

## Arquivos importantes

| Arquivo | Descricao |
|---------|-----------|
| `README.md` | Visao geral e setup |
| `CONTEXT.md` | Onboarding rapido |
| `.cursorrules` | Regras automaticas do Cursor |
| `.cursor/CURSOR.MD` | Contexto principal para agentes |
| `shared/docs/00-INDEX.md` | Indice da documentacao |

## Proximos passos recomendados

1. Geracao de dados encerrada (Oracle Free atingiu o teto de 12 GB). Congelar o `gen-unified` e registrar as contagens por tabela como linha de base.
2. Fase 1 (Azure): codigo construido mas nunca aplicado. Ordem: base de ingestao (Terraform, Event Hubs, ADLS) -> Synapse -> Databricks -> Stream Analytics. Ver `.claude/sdd/reports/BUILD_REPORT_INGESTAO_AZURE_FASE1.md`.
3. Depois: validar e arquivar GCP (Fase 3), validar AWS (Fase 2) e montar o README comparativo (Fase 4).
4. Usar SDD para mudancas relevantes: `/brainstorm`, `/define`, `/design`, `/build`, `/ship`.
5. Evoluir o agente `.cursor/agents/domain/uber-eats-case-expert.md` quando regras de negocio mudarem (o arquivo ainda nao existe em `.claude/agents/domain/`).

---

## Glossario de dominio

> Iniciado pelo install-harness. Refinar com `/grill-with-docs` junto ao especialista de dominio.

### Termos do dominio

| Termo | Definicao | Sinonimos | O que NAO e |
|---|---|---|---|
| Fase 0 (Fundacao) | Ambiente local com 4 fontes (Postgres, Oracle, MongoDB, MinIO) e CDC real. Fonte unica do dado para as 3 clouds | Fundacao, ambiente local | Nao migra para a nuvem |
| Onda 1 / 2 / 3 | Etapas da Fase 0: integridade referencial; unificacao de identidade Postgres x MinIO; diversificacao de fontes | | Nao sao fases das clouds |
| Trilho real-time | Caminho do CDC ate o barramento (Event Hub, Kinesis, Pub/Sub) que alimenta o Kappa | Trilho Kappa | Nao le o storage batch |
| Trilho batch | Caminho ate o storage (ADLS, S3, GCS) que alimenta Warehouse e Lakehouse | Landing batch | Nao alimenta o Kappa |
| Contrato canonico de CDC | Campos `cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system` na Bronze, iguais para qualquer ferramenta de ingestao | Contrato CDC | Nao e o formato nativo (`_ab_cdc_*`, `op/before/after`) |
| Captura unica | Uma so captura CDC por fonte; o trilho batch consome o mesmo topico | | Nao e uma segunda conexao/replication slot |
| Warehouse | Arquitetura dimensional (estrela, SCD2): Synapse, Redshift, BigQuery | DW | Nao e o Lakehouse |
| Lakehouse | Arquitetura medalhao sobre storage aberto: Databricks (Azure), Glue/Iceberg/Athena (AWS), BigLake/Dataproc (GCP) | | |
| Kappa | Arquitetura so de streaming: Event Hubs + Stream Analytics, Kinesis, Pub/Sub + Dataflow | | Nao e Lambda (nao mistura trilho batch) |
| Bronze / Silver / Gold | Camadas do medalhao: dado bruto, limpo e deduplicado, agregado para consumo | | |
| SCD2 | Dimensao com historico de versoes por linha | SCD tipo 2 | |
| Teto do Oracle | Limite de 12 GB da edicao Free (`ORA-12954`) | Cap de 12 GB | Nao e bug do gerador |
| ShadowTraffic | Gerador de dados sinteticos (`gen-unified`) | gen-unified | |
| Dev Loop / SDD | Fluxos de desenvolvimento do projeto: PROMPTs L2 (`/dev`) e fases L3 (`/brainstorm` a `/ship`) | | |
| Dominio Pedido e catalogo | Pedido, item de pedido, pagamento, recibo, produto, estoque e restaurante. Ficam juntos na mesma fonte por coerencia de negocio | | Nao inclui usuario nem motorista |
| Dominio Pessoas | Usuario (quem pede) e motorista (quem entrega). Referenciados pelo pedido, mas fora do dominio dele | | Nao e o dominio de pedido |
| Pedido | Compra de um unico cliente, com um ou mais itens, que pode envolver mais de um restaurante | Order | Nao tem um restaurante unico |
| Item de pedido | Linha de um pedido: um produto em uma quantidade. Pertence a um pedido e referencia um produto | | Nao e o produto em si |
| Atendimento | Parte de um pedido que cabe a um restaurante: um por restaurante e por pedido, com ciclo de vida proprio (aceite, preparo, pronto, retirado, cancelado). O status do pedido e derivado dos atendimentos | Sub-pedido | Nao e o pedido inteiro |
| Perfil de restaurante | Satelite documental do restaurante: cardapio (apresentacao) e horarios de funcionamento | | Nao e o cadastro do restaurante nem fonte de preco |
| Menu (cardapio) | Apresentacao dos produtos de um restaurante (secao, ordem, destaque, customizacoes). Referencia o produto; nao define nome nem preco proprios | Cardapio | Nao e uma segunda fonte de verdade de produto/preco |
| Tentativa de pagamento | Registro de um pagamento recusado de um cliente (valor, motivo, momento), sem pedido associado, porque o pedido so existe com pagamento aprovado | | Nao e o pagamento do pedido |
| Cancelamento | Evento proprio, com motivo, quem cancelou (cliente ou restaurante) e momento, ligado a um atendimento. O pedido so e cancelado quando todos os atendimentos sao cancelados | Cancelamento parcial | Nao e apenas um valor de status do pedido; o motorista nunca cancela |
| Incidente | Reclamacao sobre um pedido apos a retirada (atraso, item errado, item faltando). Tem desfecho: a plataforma o marca como procedente ou improcedente; so o procedente gera cancelamento e devolucao | | Nao e atendimento generico |
| Gorjeta | Valor livre e opcional pago pelo cliente ao motorista depois da entrega, a parte do pedido. No maximo uma por pedido entregue | | Nao compoe o valor do pedido nem passa por reembolso |
| Intencao de compra (checkout) | Agrupa as tentativas de pagamento de uma compra; gera no maximo um pedido e um pagamento principal | Checkout | Nao e o pedido |
| Pedido nao entregue | Estado terminal de um pedido que nao chega ao cliente, com motivo (cliente ausente ou motorista impossibilitado) | | Nao e cancelado |
| Em coleta | Status do pedido quando ao menos um atendimento ja foi retirado e outro ainda nao | | Nao e "a caminho", que so comeca com tudo recolhido |
| Cancelamento legitimo por atraso | Direito do cliente de cancelar um atendimento aceito cujo preparo passou do estimado mais 50% | | Nao exige arbitragem |

### Acronimos e siglas

| Sigla | Significado |
|---|---|
| CDC | Change Data Capture |
| ADLS | Azure Data Lake Storage Gen2 |
| DLT | Delta Live Tables (Lakeflow Spark Declarative Pipelines) |
| DAB | Databricks Asset Bundles |
| DMS | AWS Database Migration Service |
| SCD | Slowly Changing Dimension |
| SDD | Spec-Driven Development |
| UC | Unity Catalog |
| LSN / SCN | Numero de sequencia do log (Postgres / Oracle) |

### Regras de negocio implicitas

- **Ciclo de vida do pedido (dado atual):** Order Placed -> In Analysis -> Accepted -> Preparing -> Ready for Pickup -> Picked Up -> Out for Delivery -> Delivered -> Completed. Cada transicao e um evento de mudanca. O dado atual nao tem cancelamento nem rejeicao: lacuna conhecida, a ser coberta pelo evento de cancelamento.
- **Historico de transicoes e valor de negocio:** a duracao entre estados (preparo, espera pela retirada, entrega) alimenta os indicadores de entrega. A Silver nao deve descartar esse historico (decisao de modelagem em aberto: SCD2 ou tabela de eventos).
- **Menu referencia produto:** o menu de um restaurante e so apresentacao; o item vendavel e o produto, que carrega nome e preco. Hoje o seed do perfil nao respeita isso (itens genericos, sem `product_id`): ajuste pendente.
- **Perfil de restaurante e satelite:** a ligacao com o restaurante e logica, por `restaurant_id`, sem FK. A cobertura do perfil pode ser menor que a do cadastro (500 perfis x ~622 restaurantes, a confirmar).
- **Integridade e logica:** nao ha FK fisica em nenhum banco; a coerencia entre entidades e garantida pelo gerador e validada na Silver.
