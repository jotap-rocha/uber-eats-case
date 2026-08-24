# Como Tornar um Projeto Agentic

Este guia explica como usar `data-agentic-ai-for-pipelines` como template fonte para transformar outro repositório em um projeto agentic/SDD.

## Objetivo

Evitar o processo manual de copiar arquivos, corrigir placeholders, ajustar routers, registrar agentes e consertar KBs depois do merge.

O fluxo recomendado é:

```text
template padronizado -> bootstrap -> validação -> projeto agentic pronto
```

## Fonte Canônica

O padrão adotado é:

| Camada | Papel |
|--------|-------|
| `.cursor/` | Fonte canônica de agentes, KBs, comandos e SDD |
| `.github/` | Espelho opcional para GitHub Copilot |
| `.claude/` | Espelho opcional para Claude Code |
| `CONTEXT.md` | Contexto rápido do projeto |
| `.cursorrules` | Regras do assistente |
| `docs/00-INDEX.md` | Índice da documentação |

Quando houver divergência, ajuste primeiro `.cursor/` e depois alinhe os espelhos.

## Pré-Requisitos do Template

Antes de usar o bootstrap, o template `data-agentic-ai-for-pipelines` precisa passar nestas regras:

1. Ter apenas `CURSOR.MD`, sem duplicidade `CURSOR.md`.
2. Usar variáveis padronizadas como `Pipeline de Dados Uber Eats - Portfolio`, `uber-eats-case` e `Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.`.
3. Não manter placeholders legados como `<NOME_DO_PROJETO>` em arquivos principais.
4. Ter `AGENT_ROUTER.yaml` apontando apenas para agentes e `context_paths` existentes.
5. Ter `kb/_index.yaml` listando apenas KBs e entrypoints existentes.
6. Usar comandos SDD reais: `/brainstorm`, `/define`, `/design`, `/build`, `/ship` e `/iterate`.
7. Ter um template de agente expert em `templates/agent-expert.md.j2`.
8. Ter `.github/` e `.claude/` alinhados como espelhos, ou claramente tratados como opcionais.

## Validar o Template Fonte

Execute:

```bash
python data-agentic-ai-for-pipelines/scripts/validate-agentic-template.py \
  --root data-agentic-ai-for-pipelines \
  --mode template
```

Resultado esperado:

```text
validate-agentic-template: OK (template)
```

## Aplicar o Bootstrap em um Projeto

Importante: o template nao deve receber nem gerar comando de execucao do projeto destino. O bootstrap aceita apenas comandos de preparacao/validacao (`--install-command` e `--test-command`). Comandos reais de execucao pertencem ao projeto destino e devem ser documentados manualmente no README desse projeto, quando fizer sentido.

Exemplo para transformar `zabbix_services_availability` em agentic:

```bash
python data-agentic-ai-for-pipelines/scripts/bootstrap-agentic-project.py \
  --target /datalake/workspace/fabiano/zabbix_services_availability \
  --project-name "Zabbix Services Availability" \
  --project-slug "zabbix-services-availability" \
  --description "Pipeline Python de disponibilidade Zabbix para SQL Server BI" \
  --stack "python,data-pipeline,oci-vault,sql-server" 
  
```

Para simular sem escrever:

* Atenção para um projeto do zero, não temos como fazer dry run por não existir estrutura de pastas

```bash
python data-agentic-ai-for-pipelines/scripts/bootstrap-agentic-project.py \
  --target /caminho/do/projeto \
  --project-name "Meu Projeto" \
  --project-slug "meu-projeto" \
  --description "Descricao curta do projeto"   
```

Para sobrescrever arquivos agentic existentes:

```bash
python data-agentic-ai-for-pipelines/scripts/bootstrap-agentic-project.py \
  --target /caminho/do/projeto \
  --project-name "Meu Projeto" \
  --project-slug "meu-projeto" \
  --description "Descricao curta do projeto" \
  --force
```

## O Que o Bootstrap Faz

O script:

- Copia a estrutura agentic do template para o destino.
- Renderiza variáveis `{{...}}` com os dados do projeto.
- Cria o agente expert do projeto em:
  - `.cursor/agents/domain/<project-slug>-expert.md`
  - `.github/agents/domain/<project-slug>-expert.md`
  - `.claude/agents/domain/<project-slug>-expert.md`
- Registra esse agente em:
  - `.cursor/sdd/architecture/AGENT_ROUTER.yaml`
  - `.github/sdd/architecture/AGENT_ROUTER.yaml`
  - `.claude/sdd/architecture/AGENT_ROUTER.yaml`
- Atualiza os routers Markdown em:
  - `.cursor/commands/core/router.md`
  - `.github/commands/core/router.md`
  - `.claude/commands/core/router.md`
- Remove duplicidades `CURSOR.md`.
- Roda a validação final em modo `project`.

## Validar o Projeto Depois

O bootstrap já roda a validação final, mas você pode executar manualmente:

```bash
python data-agentic-ai-for-pipelines/scripts/validate-agentic-template.py \
  --root /caminho/do/projeto \
  --mode project
```

Resultado esperado:

```text
validate-agentic-template: OK (project)
```

## Diferença Entre Template e Projeto

| Modo | Pode conter `Pipeline de Dados Uber Eats - Portfolio`? | Uso |
|------|---------------------------------|-----|
| `template` | Sim | Validar `data-agentic-ai-for-pipelines` antes de aplicar |
| `project` | Não | Validar projeto destino após bootstrap |

## Quando Usar SDD

Use SDD quando a mudança alterar:

- arquitetura;
- contratos de execução;
- persistência;
- segurança;
- troubleshooting;
- fluxo operacional;
- comportamento público.

Fluxo:

```text
/brainstorm -> /define -> /design -> /build -> /ship
```

Para ajustes no meio do caminho:

```text
/iterate
```

## Regra de Ouro

Não copie `data-agentic-ai-for-pipelines` manualmente para novos projetos se o objetivo for padronização.

Use sempre:

```text
bootstrap-agentic-project.py + validate-agentic-template.py
```

Assim o projeto já nasce com agentes, KBs, routers, SDD e documentação alinhados.
