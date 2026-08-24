# PROMPT: Inicialização pós-install Agent Spec

> Execute após `python3 agentspec/install_agentspec.py` em um projeto greenfield.

## Objetivo

Completar o bootstrap do projeto **Pipeline de Dados Uber Eats - Portfolio** (`uber-eats-case`): validar a instalação, ajustar documentação mínima e orientar o primeiro ciclo de trabalho (Dev Loop ou SDD).

## Contexto

- Repositório com Agent Spec instalado (`.cursor/`, guias, scripts de validação).
- Agente expert: `.cursor/agents/domain/uber-eats-case-expert.md`
- Triângulo de contexto: `CONTEXT.md`, `.cursorrules`, `docs/00-INDEX.md`

## Tarefas

1. **Validar instalação**
   - Executar `python3 scripts/validate-agent-router.py`
   - Executar `python3 scripts/validate-agentic-template.py --root . --mode project`
   - Reportar erros e corrigir paths quebrados em KB ou comandos, se houver.

2. **Revisar placeholders**
   - Confirmar que `Pipeline de Dados Uber Eats - Portfolio`, `uber-eats-case` e `Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.` foram substituídos em `CONTEXT.md`, `README.md` e `.cursorrules`.
   - Se restarem `{{...}}`, atualizar com os valores corretos do projeto.

3. **Ajustar README e CONTEXT**
   - Adicionar comando real de setup em `README.md` (substituir comentário genérico de install).
   - Em `CONTEXT.md`, listar 3–5 comandos slash que o time usará no dia a dia.

4. **Inventário de ambiente (opcional)**
   - Se o projeto usa Databricks/Spark/cloud, copiar `docs/inventario-ambiente.md.example` → `docs/inventario-ambiente.md` e preencher sem segredos.

5. **Primeiro fluxo sugerido**
   - Para tarefa pequena (Nível 2): `/workflow-dev-loop` → `/devloop-init uber-eats-case-bootstrap`
   - Para feature com documentação formal (Nível 3): `/brainstorm` com escopo da primeira entrega

## Critérios de conclusão

- [ ] Validações do router e do template passam sem erro
- [ ] Nenhum `{{PROJECT_*}}` residual nos arquivos públicos
- [ ] `CONTEXT.md` reflete o domínio real do projeto
- [ ] Time sabe qual comando usar: Dev Loop vs SDD vs review de pipeline

## Referências

- `START_HERE.md`
- `MANUAL_AGENTES.md`
- `DEV_LOOP_Guia_Comandos.md`
- `SDD_Guia_Comandos.md`
- `.cursor/commands/core/router.md`
