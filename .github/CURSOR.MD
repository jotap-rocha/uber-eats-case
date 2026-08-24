# Pipeline de Dados Uber Eats - Portfolio - Contexto GitHub

> Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.

## Fonte canonica

`.cursor/` e a fonte canonica para agentes, KBs, comandos e SDD. `.github/` e `.claude/` sao espelhos opcionais.

## Roteamento de agentes

Use `.github/commands/core/router.md` como ponto de partida. Para assuntos especificos deste projeto, priorize:

- `.github/agents/domain/uber-eats-case-expert.md`
- `.github/agents/code-quality/python-developer.md` para Python e refatoracao
- `.github/agents/code-quality/code-reviewer.md` para revisao e seguranca
- `.github/agents/workflow/` para SDD

### On-prem DATALAKE (311–314) — transversal

| Agente | Quando |
|--------|--------|
| `.github/agents/data-engineering/big-data-cluster-expert.md` | Cluster, migration-hub, SSH, Airflow 314, `/DATALAKE/dags` |
| `.github/agents/data-engineering/spark-cluster-migration-expert.md` | Migração operacional Standalone → YARN, portação de jobs |
| `.github/agents/dev/big-data-orchestrator.md` | spark-submit, `config/spark.conf`, portacao de job PRD |
| `.github/agents/data-engineering/airflow-dag-builder.md` | Criar ou migrar DAGs TaskFlow 2.11.x |
| `.github/agents/dev/python-project-architect.md` | Classificar projeto dados vs automação, layout OOP, KBs de design |

### Knowledge base — pipelines on-prem (indice: `.github/kb/_index.yaml`)

| Dominio | Entrada |
|---------|---------|
| `migration-hub/` | `.github/kb/migration-hub/index.md` |
| `airflow/` | `.github/kb/airflow/index.md` |
| `design-pipelines-patterns/` | `.github/kb/design-pipelines-patterns/index.md` |
| `design-automation-project-patterns/` | `.github/kb/design-automation-project-patterns/index.md` |
| `dev-python-engineering/` | `.github/kb/dev-python-engineering/index.md` |
| `dev-python-automation/` | `.github/kb/dev-python-automation/index.md` |

## Recursos

| Recurso | Caminho |
|---------|---------|
| Agentes | `.github/agents/` |
| KB | `.github/kb/` |
| Comandos | `.github/commands/` |
| SDD | `.github/sdd/` |
| Contexto rapido | `../CONTEXT.md` |
| README | `../README.md` |
| Docs | `../docs/00-INDEX.md` |

## Projeto

| Campo | Conteudo |
|-------|----------|
| Nome | Pipeline de Dados Uber Eats - Portfolio |
| Slug | uber-eats-case |
| Stack | PostgreSQL + MinIO (fontes), Airbyte (ingestao), Databricks Lakehouse + Delta Live Tables (processamento), Unity Catalog (governanca), Power BI / Databricks AI/BI Genie (consumo) |
| Descricao | Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie. |

## Validacao local

```bash
.\scripts\start-all.ps1
python3 scripts/validate-agent-router.py
```

## SDD

Use `/brainstorm`, `/define`, `/design`, `/build`, `/ship` e `/iterate` conforme `SDD_Guia_Comandos.md`.
