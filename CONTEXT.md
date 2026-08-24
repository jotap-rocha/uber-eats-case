# Pipeline de Dados Uber Eats - Portfolio - Contexto rapido

> Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.

## O que e este projeto?

Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.

## Estrutura principal

| Componente | Descricao | Observacao |
|------------|-----------|------------|
| `src/` | Codigo-fonte principal | Ajuste conforme a estrutura real do projeto |
| `scripts/` | Scripts auxiliares | Validacoes, automacoes e utilitarios |
| `docs/` | Documentacao complementar | Indice em `docs/00-INDEX.md` |
| `.cursor/` | Agentes, KB, comandos e SDD | Fonte canonica do formato agentic |

## Comandos de validacao

```bash
# Instalar dependencias, se necessario
.\scripts\start-all.ps1

# Validar o projeto
python3 scripts/validate-agent-router.py
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
| `docs/MANDATOS_PIPELINE_DADOS.md` | Guia humano dos mandatos |
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
| `docs/00-INDEX.md` | Indice da documentacao |

## Proximos passos recomendados

1. Completar detalhes especificos do dominio no `README.md` e em `docs/`.
2. Usar SDD para mudancas relevantes: `/brainstorm`, `/define`, `/design`, `/build`, `/ship`.
3. Evoluir o agente `.cursor/agents/domain/uber-eats-case-expert.md` quando regras de negocio mudarem.
