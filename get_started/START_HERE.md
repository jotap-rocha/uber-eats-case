# Comece por aqui - Pipeline de Dados Uber Eats - Portfolio

Este repositório usa um formato agentic/SDD. A referencia principal e `.cursor/`; `.github/` e `.claude/` sao espelhos opcionais para outras ferramentas.

## Fontes de verdade

| Recurso | Papel |
|---------|-------|
| `CONTEXT.md` | Contexto rapido |
| `.cursorrules` | Regras do assistente |
| `docs/00-INDEX.md` | Indice de documentacao |
| `.cursor/CURSOR.MD` | Contexto canonico do Cursor |
| `.cursor/commands/core/router.md` | Roteamento de agentes |
| `.cursor/agents/domain/uber-eats-case-expert.md` | Agente especialista do projeto |

## Primeiro passo

1. Leia `CONTEXT.md`.
2. Confirme setup e comandos em `README.md`.
3. Use `DEV_LOOP_Guia_Comandos.md` para entregas no Nivel 2 (requirements → design → `/dev`).
4. Use `SDD_Guia_Comandos.md` para features com rastreabilidade formal (Nivel 3).
5. Se editar `.github/` ou `.claude/`, mantenha alinhado com `.cursor/`.

## Definition of Done de contexto

Se uma mudanca alterar como o projeto e executado, navegado ou depurado, atualize no mesmo PR:

- `CONTEXT.md`
- `README.md` ou `docs/00-INDEX.md`
- `.cursor/CURSOR.MD`
- `.cursor/commands/core/router.md`, se mudar agentes ou prioridades
