# Genie Space — requisitos, permissões e limites

> **Propósito**: Checklist técnico e de governança antes de criar ou auditar um Genie Space.
> **Confiança**: 0.93
> **MCP Validated**: null

## Overview

Genie Space exige dados em **Unity Catalog**, compute **SQL warehouse Pro ou serverless**, entitlement **Databricks SQL** e permissões explícitas sobre o objeto espaço (criação/edição) e sobre os dados (`SELECT`). Limites de capacidade e throughput protegem o workspace; feature de IA parceira exige habilitação em conta/workspace.

## O padrão

```text
Pré-requisitos:
  UC metastore + tabelas/views com descrições úteis
  Warehouse (recomendado serverless) com CAN USE para quem configura
  SELECT nos objetos de negócio relevantes
Pós-criação:
  Embutir warehouse → credenciais do autor passam a executar queries de todos os usuários do chat
```

## Referência rápida

| Item | Valor / regra |
|------|----------------|
| Tabelas/views no espaço | até 30 |
| Throughput UI | ~20 perguntas/minuto / workspace (todos os espaços) |
| Genie API | preview; ~5 perguntas/minuto / workspace |
| Conversas / mensagens | 10.000 / 10.000 por conversa |

## Erros comuns

### Errado

Dar CAN EDIT a usuários que não deveriam ver dados sensíveis: o warehouse do espaço roda com credenciais embutidas do configurador — combinar com grants amplos em UC.

### Certo

Princípio do menor privilégio em UC; revisar **quem** salva o warehouse no espaço; separar espaços por domínio de dados ou por persona.

## Relacionados

- [genie-space-visao-geral.md](genie-space-visao-geral.md)
- [genie-dados-acesso-e-queries.md](genie-dados-acesso-e-queries.md)
- [../../databricks/concepts/sql-warehouse.md](../../databricks/concepts/sql-warehouse.md)
- [../../databricks/concepts/unity-catalog.md](../../databricks/concepts/unity-catalog.md)

## Fontes

- [Set up and manage a Genie Space](https://docs.databricks.com/en/genie/set-up)
- [Entitlements](https://docs.databricks.com/aws/en/security/auth/entitlements)
- [Genie Space ACLs](https://docs.databricks.com/aws/en/security/auth/access-control/#genie-space-acls)
- [Partner-powered AI features](https://docs.databricks.com/aws/en/databricks-ai/partner-powered)
