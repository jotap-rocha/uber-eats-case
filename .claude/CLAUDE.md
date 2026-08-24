# Pipeline de Dados Uber Eats - Portfolio - Claude Code

Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.

A fonte canonica do formato agentic e `.cursor/`. Use `.claude/` como espelho para Claude Code.

## Leia primeiro

- `CONTEXT.md`
- `README.md`
- `docs/00-INDEX.md`
- `.cursor/CURSOR.MD`

## Agente principal

Use `.claude/agents/domain/uber-eats-case-expert.md` para regras do dominio deste projeto.

## Regras

- Responda em portugues brasileiro.
- Nao adicione segredos.
- Preserve contratos operacionais existentes.
- Atualize documentacao quando mudar execucao, troubleshooting ou arquitetura.
