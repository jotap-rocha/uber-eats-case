# Genie Space — visão geral

> **Propósito**: Definir o que é uma “sala” Genie (Genie Space) e o fluxo de valor para o negócio.
> **Confiança**: 0.92
> **MCP Validated**: null

## Overview

**Genie Space** é um objeto no workspace Databricks: interface de chat onde usuários de negócio fazem perguntas em linguagem natural sobre dados estruturados. O sistema gera SQL (e pode exibir resultados) com base nos ativos e instruções configurados no espaço. Não substitui análise causal ou consultoria (“por que caiu?” / “que incentivo oferecer?”) quando a documentação restringe a dados estruturados e consultas.

## O padrão

```text
Usuário (NL) → Genie Space (contexto: tabelas UC + knowledge store + exemplos SQL + texto)
            → SQL Warehouse (Pro / serverless)
            → Unity Catalog (SELECT conforme permissões)
            → Resposta (tabela / narrativa; opcionalmente Trusted)
```

## Referência rápida

| Entrada | Saída | Notas |
|---------|--------|-------|
| “Receita por região no último trimestre” | SQL + resultado | Depende de colunas, joins e sinônimos no knowledge store |
| Pergunta fora dos dados | Recusa ou resposta limitada | Reforçar instruções e exemplos para o domínio |

## Erros comuns

### Errado

Assumir que só as “30 tabelas” do espaço existem para o motor: a documentação indica que **permissões UC** podem permitir joins a outras tabelas se o prompt ou metadados referenciarem — o espaço define contexto padrão, não um sandbox de segurança isolado por lista.

### Certo

Tratar Genie como **camada semântica + UX**: curadoria (knowledge store, exemplos, texto) **e** grants UC mínimos necessários para cada persona.

## Relacionados

- [genie-requisitos-permissoes-limites.md](genie-requisitos-permissoes-limites.md)
- [genie-knowledge-store-e-instrucoes.md](genie-knowledge-store-e-instrucoes.md)
- [../patterns/checklist-configuracao-genie-space.md](../patterns/checklist-configuracao-genie-space.md)

## Fonte

- [What is a Genie Space](https://docs.databricks.com/genie/)
- [Talk to Genie](https://docs.databricks.com/aws/en/genie/talk-to-genie)
