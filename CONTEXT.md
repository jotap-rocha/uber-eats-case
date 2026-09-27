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

1. Completar detalhes especificos do dominio no `README.md` e em `shared/docs/`.
2. Usar SDD para mudancas relevantes: `/brainstorm`, `/define`, `/design`, `/build`, `/ship`.
3. Evoluir o agente `.cursor/agents/domain/uber-eats-case-expert.md` quando regras de negocio mudarem.
