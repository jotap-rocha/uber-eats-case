# Pipeline de Dados Uber Eats - Portfolio — Contexto para Claude Code

Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.. Repositório agentic com agentes, comandos e knowledge bases para desenvolvimento assistido por IA em Cursor, Claude Code e GitHub Copilot.

---

## Fontes de Verdade

| Recurso | Caminho | Uso |
|---------|---------|-----|
| Contexto rápido | `CONTEXT.md` | Onboarding mínimo e comandos principais |
| Índice de documentação | `docs/00-INDEX.md` | Navegação dos guias do projeto |
| Contexto Claude Code completo | `.claude/CURSOR.md` | Agentes, KBs, comandos e roteamento no ecossistema `.claude/` |
| Roteador de agentes | `.claude/commands/core/router.md` | Escolha de agente e escopo por intenção |
| Arquitetura do roteador | `.claude/sdd/architecture/AGENT_ROUTER.yaml` | Fonte estruturada dos agentes e hints |

---

## Comandos de Verificação

Este projeto não possui hoje uma suite de testes de aplicação na raiz. Use os comandos abaixo como verificação padrão:

```bash
python3 scripts/validate-agent-router.py
python3 install_dev_loop/install_dev_loop.py --dry-run --target .
```

Não há CI configurada no repositório no momento (pode ser adicionada em `.github/workflows/` se necessário).

---

## Dev Loop

O Dev Loop fica em `.claude/dev/` e oferece um fluxo de desenvolvimento nível 2 baseado em PROMPTs versionáveis.

### Quick Start

```bash
# Criar um PROMPT guiado pelo agente prompt-crafter
/dev "descreva o que você quer construir"

# Executar o primeiro PROMPT específico deste repositório
/dev tasks/PROMPT_HELLO_WORLD.md

# Executar o bootstrap do Dev Loop novamente, se precisar revisar a instalação
/dev tasks/PROMPT_INIT_DEV_LOOP.md
```

### Estrutura

```text
.claude/dev/
├── _index.md              # Documentação principal do Dev Loop
├── readme.md              # Visão curta do AgentLoop
├── docs/                  # Documentação de apoio
├── tasks/                 # PROMPT_*.md executáveis
├── templates/             # Templates de PROMPT e PROGRESS
├── examples/              # Exemplos e notas de execuções
├── progress/              # Memória de execução gerada pelo executor
└── logs/                  # Logs finais gerados pelo executor
```

Leia `.claude/dev/_index.md` para detalhes de uso, recuperação de sessão e opções como `--resume`, `--dry-run` e `--mode`.

---

## Convenções de Trabalho

- Responder em português brasileiro, salvo pedido explícito em outro idioma.
- Manter mudanças pequenas, focadas e alinhadas ao padrão existente.
- Não commitar segredos, `.env` real nem inventário local de infraestrutura.
- Ao alterar agentes, comandos ou roteamento, validar com `python3 scripts/validate-agent-router.py`.
- Quando a mudança afetar fluxo de uso, atualizar documentação em `CONTEXT.md`, `docs/00-INDEX.md` ou `.claude/dev/_index.md`, conforme o escopo.
