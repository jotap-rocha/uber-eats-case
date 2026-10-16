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

(preencher com `/grill-with-docs`)
