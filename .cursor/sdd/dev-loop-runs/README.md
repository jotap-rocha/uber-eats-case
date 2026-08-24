# Workflow Dev Loop — runs

Implementação **Nível 2 (Agentic Development)** com estado em disco — **uma fase por conversa** para controlar contexto.

## Localização

```text
.cursor/sdd/dev-loop-runs/{RUN_ID}/
  DEVLOOP_MANIFEST.yaml
  DEVLOOP_LOG.md
  DEVLOOP_SUMMARY.md          # gerado na fase reflect
  artifacts/
    {RUN_ID}_requirements.md
    {RUN_ID}_design.md
  phases/
    gate.md
    requirements.md
    design.md
    craft.md
    prompt_review.md
    execute.md
    reflect.md
```

PROMPT executável: `.cursor/dev/tasks/PROMPT_{RUN_ID}.md` (referenciado no manifest).

## Comandos Cursor

Canônico: `.cursor/commands/workflow-dev-loop/workflow-dev-loop.md`

| Comando | Função |
|---------|--------|
| `/workflow-dev-loop` | Visão geral e ordem dos passos |
| `/devloop-init` | Cria RUN, manifest, stubs de fases e artifacts/ |
| `/devloop-phase` | Executa **uma** fase (gate → … → reflect) |
| `/devloop-craft` | Atalho para fase `craft` |
| `/devloop-execute` | Executa PROMPT via `/dev` (após prompt_review OK) |
| `/devloop-round` | Revalida tarefas falhas pós-execução |
| `/devloop-fixer` | Correção guiada de tarefa do PROMPT |

## Ordem das fases

`gate` → `requirements` → `design` → `craft` → `prompt_review` → `execute` → `reflect`

Contrato: [`.cursor/sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml`](../architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml)

## Relação com `/dev` e SDD

- **`/dev`** — motor de craft e execução do PROMPT; o workflow orquestra e persiste estado.
- **SDD (L3)** — se o gate decidir `escalate_sdd`, usar `/brainstorm`, `/define`, `/design`, `/build` (ver `SDD_Guia_Comandos.md`).
