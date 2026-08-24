# Genie Space — dados, acesso e queries sugeridas

> **Propósito**: Comportamento dos ativos no espaço, sugestões automáticas de queries e implicações de segurança.
> **Confiança**: 0.91
> **MCP Validated**: null

## Overview

Ao adicionar tabelas/views, a Genie pode sugerir **queries populares** do workspace associadas a esses ativos (notificação na aba Data das instruções). A revisão exige CAN VIEW na query sugerida e CAN EDIT no espaço. A aba **Configure > Data** lista colunas, tipos, descrições e amostra. Importante: **controle de acesso é UC** — a lista de até 30 objetos orienta o contexto, mas usuários podem, conforme grants e prompt, envolver outras tabelas (ex.: joins ou edição de SQL) se tiverem permissão.

## O padrão

```text
Adicionar ativos UC ao espaço
  → Genie busca queries comuns (credencial de quem configura)
  → Aceitar / rejeitar sugestões → viram exemplos editáveis
Manter views “amigáveis à Genie” para joins que não aparecem nas queries históricas
```

## Referência rápida

| Situação | Ação recomendada |
|----------|------------------|
| Sem sugestões | Verificar CAN VIEW em queries relevantes; uso prévio das tabelas |
| View dedicada ao chat | Adicionar a view ao espaço; documentar no knowledge store |
| Excesso de exposição | Restringir SELECT UC; não depender só da lista de 30 tabelas |

## Erros comuns

### Errado

Achar que “não coloquei a tabela X no espaço” impede qualquer acesso a X.

### Certo

Auditar **grants** e instruções que mencionam objetos externos; alinhar product owners sobre escopo do espaço.

## Relacionados

- [genie-requisitos-permissoes-limites.md](genie-requisitos-permissoes-limites.md)
- [../../databricks/concepts/security.md](../../databricks/concepts/security.md)

## Fontes

- [Set up and manage — Manage data objects](https://docs.databricks.com/en/genie/set-up)
- [Query ACLs](https://docs.databricks.com/aws/en/security/auth/access-control/#query)
