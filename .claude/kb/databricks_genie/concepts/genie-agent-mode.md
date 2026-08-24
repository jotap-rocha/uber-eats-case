# Genie Space — Agent mode

> **Propósito**: Resumo do modo agente (preview) para perguntas analíticas mais complexas.
> **Confiança**: 0.88
> **MCP Validated**: null

## Overview

**Agent mode** estende a Genie além de uma única consulta linear: usa raciocínio em múltiplas etapas, pode emitir várias queries SQL e produzir relatórios mais longos com citações. Estado e limites seguem evolução do produto em **Public Preview** — validar sempre a documentação vigente antes de prometer SLAs.

## O padrão

```text
Pergunta complexa → decomposição em sub-perguntas → múltiplas execuções SQL → síntese
```

## Referência rápida

| Uso | Observação |
|-----|------------|
| Exploração hipotética / comparativos | Útil quando uma única SELECT não basta |
| Governança | Mesmos requisitos UC + warehouse; revisar custo e volume de queries |

## Erros comuns

### Errado

Tratar preview como GA em contratos de auditoria ou compliance sem cláusula de mudança de comportamento.

### Certo

Pilotar com conjunto de perguntas de ouro, medir latência/custo e manter human-in-the-loop para decisões críticas.

## Relacionados

- [genie-space-visao-geral.md](genie-space-visao-geral.md)

## Fonte

- [Agent mode in Genie Spaces](https://docs.databricks.com/aws/en/genie/agent-mode)
