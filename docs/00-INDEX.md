# Indice da documentacao - Pipeline de Dados Uber Eats - Portfolio

Este arquivo faz parte do triangulo de contexto: `CONTEXT.md` + `.cursorrules` + `docs/00-INDEX.md`.

## Inicio rapido

| Recurso | Descricao |
|---------|-----------|
| [`../README.md`](../README.md) | Visao geral e setup |
| [`../CONTEXT.md`](../CONTEXT.md) | Contexto rapido |
| [`../get_started/START_HERE.md`](../get_started/START_HERE.md) | Onboarding agentic |
| [`../get_started/DEV_LOOP_Guia_Comandos.md`](../get_started/DEV_LOOP_Guia_Comandos.md) | Guia passo a passo Dev Loop (L2) |
| [`../.cursor/commands/workflow-dev-loop/`](../.cursor/commands/workflow-dev-loop/) | Workflow `/workflow-dev-loop` e comandos `devloop-*` |
| [`../get_started/SDD_Guia_Comandos.md`](../get_started/SDD_Guia_Comandos.md) | Guia de comandos SDD (L3) |
| [`../get_started/HOW_TO_USE_AGENTS.md`](../get_started/HOW_TO_USE_AGENTS.md) | Como usar agentes |
| [`../.cursor/kb/teams-notifications/index.md`](../.cursor/kb/teams-notifications/index.md) | Alertas Microsoft Teams (pymsteams, webhooks Sentinel/Trilha) |
| [`DATABRICKS_TEAMS_PIPELINES.md`](DATABRICKS_TEAMS_PIPELINES.md) | **Macro** — Databricks: Teams, DSV/PRD, smoke test, job sem retry |
| [`MANDATOS_PIPELINE_DADOS.md`](MANDATOS_PIPELINE_DADOS.md) | **Mandatos obrigatórios** — contrato, quarentena, drift, Teams, sentinela |
| [`data-contract-TEMPLATE.md`](data-contract-TEMPLATE.md) | Template contrato de dados versionado |
| [`../.cursor/kb/teams-notifications/patterns/databricks-ambientes-e-smoke-test.md`](../.cursor/kb/teams-notifications/patterns/databricks-ambientes-e-smoke-test.md) | KB agentes (mesmo conteúdo macro) |
| [`../.env.example`](../.env.example) | Modelo de variaveis `URL_WEBHOOK_*` (copiar para `.env`) |
| [`../.cursor/agents/domain/teams-notifications-expert.md`](../.cursor/agents/domain/teams-notifications-expert.md) | Agente especialista em alertas Teams em pipelines |

## Recursos Cursor / SDD

| Recurso | Descricao |
|---------|-----------|
| [`../.cursor/CURSOR.MD`](../.cursor/CURSOR.MD) | Contexto canonico |
| [`../.cursor/agents/domain/uber-eats-case-expert.md`](../.cursor/agents/domain/uber-eats-case-expert.md) | Agente especialista |
| [`../.cursor/commands/core/router.md`](../.cursor/commands/core/router.md) | Router de agentes |
| [`../.cursor/sdd/architecture/AGENT_ROUTER.yaml`](../.cursor/sdd/architecture/AGENT_ROUTER.yaml) | Router estruturado |
| [`../.cursor/sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml`](../.cursor/sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml) | Mandatos pipeline Databricks/Spark |
| [`../.cursor/kb/data-engineering-practices/index.md`](../.cursor/kb/data-engineering-practices/index.md) | KB patterns operacionais |

## Instalacao greenfield (Agent Spec)

| Recurso | Descricao |
|---------|-----------|
| [`../agentspec/INSTALL_AGENTSPEC.md`](../agentspec/INSTALL_AGENTSPEC.md) | Instalar SDD + Dev Loop + agentes/KB em projeto vazio |
| [`../agentspec/install_agentspec.py`](../agentspec/install_agentspec.py) | Script CLI de instalacao |
| [`../get_started/AGENTIC_UPGRADE_Guia.md`](../get_started/AGENTIC_UPGRADE_Guia.md) | **Atualizar** projeto ja agentic (audit → apply → validate + `/intake`) |
| [`../agentspec/INSTALL_UPGRADE.md`](../agentspec/INSTALL_UPGRADE.md) | Referencia tecnica do upgrade (flags, politica de merge) |
| [`../agentspec/upgrade_agentic.py`](../agentspec/upgrade_agentic.py) | Script CLI de upgrade com relatorio em `.agentic-upgrade/` |
| [`../install_dev_loop/INSTALL_DEV_LOOP.md`](../install_dev_loop/INSTALL_DEV_LOOP.md) | Apenas workflow Dev Loop em projeto que ja tem `.cursor/` |

## Guias do projeto

| Arquivo | Descricao | Quando usar |
|---------|-----------|-------------|
| `inventario-ambiente.md.example` | Template de inventario local | Copiar para `docs/inventario-ambiente.md` quando necessario |
| [`GUIA_SKILLS_KB_SDD_DEVLOOP.md`](GUIA_SKILLS_KB_SDD_DEVLOOP.md) | Convenção Skill vs KB, estudo de caso e integração ao SDD/Dev Loop; portabilidade Claude Code/Cursor/Copilot | Criar Skill nova, ou entender como Skill/KB se ligam ao SDD e ao Dev Loop |
