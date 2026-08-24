# Guia de Comandos SDD - Spec-Driven Development

Este arquivo resume o fluxo SDD usado neste repositório. A referência canônica fica em `.cursor/commands/workflow/` e os artefatos de especificação ficam em `.cursor/sdd/`.

## Fases

| Fase | Comando | Arquivo do comando | Agente principal |
|------|---------|--------------------|------------------|
| 0 | `/brainstorm` | `.cursor/commands/workflow/brainstorm.md` | `.cursor/agents/workflow/brainstorm-agent.md` |
| 1 | `/define` | `.cursor/commands/workflow/define.md` | `.cursor/agents/workflow/define-agent.md` |
| 2 | `/design` | `.cursor/commands/workflow/design.md` | `.cursor/agents/workflow/design-agent.md` |
| 3 | `/build` | `.cursor/commands/workflow/build.md` | `.cursor/agents/workflow/build-agent.md` |
| 4 | `/ship` | `.cursor/commands/workflow/ship.md` | `.cursor/agents/workflow/ship-agent.md` |
| continua | `/iterate` | `.cursor/commands/workflow/iterate.md` | `.cursor/agents/workflow/iterate-agent.md` |

## Uso rapido

```text
/brainstorm

Quero evoluir Pipeline de Dados Uber Eats - Portfolio para <objetivo>. Considere o contexto em `CONTEXT.md` e as restricoes do `README.md`.
```

```text
/define

Transforme o brainstorm em requisitos claros, criterios de aceite e limites de escopo.
```

```text
/design

Crie o design tecnico, manifesto de arquivos, decisoes e plano de validacao.
```

```text
/build

Implemente conforme o design aprovado e atualize a documentacao afetada.
```

```text
/ship

Finalize a entrega, resuma validacoes, riscos residuais e proximos passos.
```

```text
/iterate

Atualize os artefatos SDD porque surgiu uma nova restricao ou decisao.
```

## Regras

- Use `.cursor/agents/domain/uber-eats-case-expert.md` para regras do dominio.
- Consulte KBs relevantes em `.cursor/kb/`.
- Atualize `CONTEXT.md`, `README.md` ou `docs/00-INDEX.md` quando mudar execucao, troubleshooting ou arquitetura.
