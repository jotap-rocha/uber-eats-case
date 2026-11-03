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
| `shared/docs/modelagem/` | Regras de negocio (RN-01 a RN-42), modelo conceitual e modelo logico (L0 a L4 aprovadas; fisico pendente) |
| `docs/adr/` | Decisoes arquiteturais; as de modelagem sao ADR 006 (dominios Oracle/Postgres), 007 (estoque e gerador hibrido) e 008 (historico de status) |

## Proximos passos recomendados

1. Modelagem: o modelo logico esta fechado (L0 a L4). Proximo: modelo fisico (DDL Postgres, Oracle e MongoDB; decimal e fuso no Debezium; codigo de rastreio; arquivo de parametros) e depois a regeracao dos dados do zero (ADR 006).
2. Gerador atual congelado (Oracle Free no teto de 12 GB): nao religar o `gen-unified` contra o Oracle atual, que segue tratado como producao ate a regeracao. Registrar as contagens por tabela como linha de base.
3. Fase 1 (Azure): codigo construido mas nunca aplicado. Ordem: base de ingestao (Terraform, Event Hubs, ADLS) -> Synapse -> Databricks -> Stream Analytics. Ver `.claude/sdd/reports/BUILD_REPORT_INGESTAO_AZURE_FASE1.md`.
4. Depois: validar e arquivar GCP (Fase 3), validar AWS (Fase 2) e montar o README comparativo (Fase 4).
5. Usar SDD para mudancas relevantes: `/brainstorm`, `/define`, `/design`, `/build`, `/ship`.
6. Evoluir o agente `.cursor/agents/domain/uber-eats-case-expert.md` quando regras de negocio mudarem (o arquivo ainda nao existe em `.claude/agents/domain/`).

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
| Teto do Oracle | Limite de 12 GB da edicao Free (`ORA-12954`), causado quase so por `ORDER_ITEMS`. A ADR 006 o resolve movendo pedido e catalogo para o Postgres | Cap de 12 GB | Nao e bug do gerador |
| ShadowTraffic | Gerador de dados sinteticos (`gen-unified`) | gen-unified | |
| Dev Loop / SDD | Fluxos de desenvolvimento do projeto: PROMPTs L2 (`/dev`) e fases L3 (`/brainstorm` a `/ship`) | | |
| Dominio Pedido e catalogo | Pedido, item de pedido, pagamento, recibo, produto, estoque e restaurante. Ficam juntos na mesma fonte por coerencia de negocio | | Nao inclui cliente nem motorista |
| Dominio Pessoas | Cliente (quem pede; hoje `users`) e motorista (quem entrega). Referenciados pelo pedido, mas fora do dominio dele | | Nao e o dominio de pedido |
| Cliente | Quem compra: dono de checkouts, pedidos, incidentes e avaliacoes. Tem uma cidade (RN-35). Renomeia o antigo Usuario | Usuario (nome antigo) | Nao e o motorista |
| Pedido | Compra de um unico cliente, com um ou mais itens, que pode envolver mais de um restaurante | Order | Nao tem um restaurante unico |
| Item de pedido | Linha de um atendimento (e, por ele, do pedido): um produto em uma quantidade. Guarda copia do nome e do preco da compra (RN-32) | | Nao e o produto em si |
| Item de estoque | O que o restaurante estoca: o proprio produto pronto, um pre-pronto (feijao cozido) ou um insumo (arroz). Tem unidade e saldo | Insumo (caso particular) | Nao e o produto vendido |
| Ficha tecnica | Quanto de cada item de estoque um produto consome por unidade vendida. Todo produto tem ao menos uma linha | Receita | Nao e o cardapio |
| Movimento de estoque | Mudanca do saldo: baixa quando o atendimento entra em preparo, ou reposicao fora das janelas de funcionamento (ADR 007) | | Nao acontece no checkout |
| Atendimento | Parte de um pedido que cabe a um restaurante: um por restaurante e por pedido, com ciclo de vida proprio (aceite, preparo, pronto, retirado, cancelado). O status do pedido e derivado dos atendimentos | Sub-pedido | Nao e o pedido inteiro |
| Perfil de restaurante | Satelite documental do restaurante: cardapio (apresentacao) e horarios de funcionamento | | Nao e o cadastro do restaurante nem fonte de preco |
| Menu (cardapio) | Apresentacao dos produtos de um restaurante (secao, ordem, destaque, customizacoes). Referencia o produto; nao define nome nem preco proprios | Cardapio | Nao e uma segunda fonte de verdade de produto/preco |
| Tentativa de pagamento | Toda tentativa de pagar um checkout, aprovada ou recusada (valor, resultado, motivo da recusa, momento). A recusada nunca tem pedido; a aprovada gera o pagamento e o pedido (RN-15) | | Nao e o pagamento do pedido |
| Cancelamento | Fim de um atendimento antes da retirada, com motivo (`end_reason`), quem agiu (cliente, restaurante ou plataforma) e momento, registrado no atendimento e na sua transicao de status. O pedido so e cancelado quando todos os atendimentos sao cancelados | Cancelamento parcial | Nao e uma tabela propria nem um status do pedido por si so; o motorista nunca cancela |
| Incidente | Reclamacao sobre um pedido entregue, aberta em ate 24 h. Motivos: item faltando, item errado, qualidade do alimento, atraso, pedido nao recebido e motorista impossibilitado (os tres ultimos, de entrega, devolvem a taxa de entrega; os de item nao). Tem desfecho: a plataforma o marca como procedente ou improcedente; so o procedente gera reembolso, sem mudar o status do pedido | | Nao e atendimento generico; nao existe em pedido nao entregue |
| Avaliacao | Nota de 1 a 5 com comentario livre opcional, ate 20 min apos a finalizacao da entrega. Duas: do motorista (uma por entrega) e do restaurante (uma por atendimento retirado). Nota do motorista 3 ou menor: a gorjeta nao e oferecida | | Nao e obrigatoria; ausente nunca conta como zero |
| Reembolso | Evento posterior ao pagamento, com uma unica origem: cancelamento ou rejeicao de atendimento, incidente procedente ou estorno por motorista impossibilitado (RN-30). O pagamento nunca muda | Estorno | Nao e outro pagamento |
| Repasse | Valor devido a restaurante (itens do atendimento retirado menos comissao) ou a motorista (parcela da taxa de entrega). Obrigacao reconhecida, sem liquidacao | | Nao e a gorjeta, que vai direto ao motorista |
| Gorjeta | Valor livre e opcional pago pelo cliente ao motorista depois da entrega, a parte do pedido. No maximo uma por pedido entregue | | Nao compoe o valor do pedido nem passa por reembolso |
| Intencao de compra (checkout) | Agrupa as tentativas de pagamento de uma compra; gera no maximo um pedido e um pagamento principal | Checkout | Nao e o pedido |
| Turno | Periodo em que o motorista esta disponivel para entregas, aberto e fechado por ele (ou fechado pela plataforma quando ele fica impossibilitado). So motorista ativo abre turno; nao se fecha com entrega atribuida | | Nao e escala planejada nem registra ganho proprio (ganho e derivado das entregas) |
| Atribuicao de motorista | Ligacao de um motorista a uma entrega, com momento de inicio e de liberacao. A vigente e a atual; um motorista tem no maximo uma atribuicao vigente (uma entrega por vez) | Atribuicao | Nao e agrupamento de entregas: duas coletas so acontecem quando o mesmo pedido tem dois restaurantes |
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

- **Ciclo de vida do pedido (dado atual):** Order Placed -> In Analysis -> Accepted -> Preparing -> Ready for Pickup -> Picked Up -> Out for Delivery -> Delivered -> Completed. Cada transicao e um evento de mudanca. O dado atual nao tem cancelamento nem rejeicao: lacuna conhecida. No modelo novo o pedido e o atendimento nascem `in_analysis` (sem "Order Placed") e ganham `cancelled`/`rejected` (modelo logico L1b).
- **Historico de transicoes e valor de negocio:** a duracao entre estados (preparo, espera pela retirada, entrega) alimenta os indicadores de entrega. A Silver nao deve descartar esse historico (decisao fechada na ADR 008: tabelas de transicao de pedido e atendimento, gravadas na mesma transacao; a Silver nao deriva esse historico do CDC).
- **Menu referencia produto:** o menu de um restaurante e so apresentacao; o item vendavel e o produto, que carrega nome e preco. Hoje o seed do perfil nao respeita isso (itens genericos, sem `product_id`): ajuste pendente.
- **Perfil de restaurante e satelite:** a ligacao com o restaurante e logica, por `restaurant_id`, sem FK. A cobertura do perfil pode ser menor que a do cadastro (500 perfis x ~622 restaurantes, a confirmar). No modelo novo todo restaurante tem perfil (RN-23); a regeracao corrige a cobertura.
- **Integridade e logica:** nao ha FK fisica em nenhum banco; a coerencia entre entidades e garantida pelo gerador e validada na Silver.
