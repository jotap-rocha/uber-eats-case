# Databricks Genie Space — Base de conhecimento

> **Propósito**: Conceitos da “sala” Genie (Genie Space) no Databricks — chat em linguagem natural sobre dados governados, requisitos de UC/SQL warehouse, knowledge store, instruções e governança.
> **Validação MCP**: null (fonte primária: documentação oficial Databricks, abril/2026)

## Navegação rápida

### Conceitos

| Arquivo | Conteúdo |
|---------|-----------|
| [concepts/genie-space-visao-geral.md](concepts/genie-space-visao-geral.md) | O que é Genie Space, público-alvo, fluxo pergunta → SQL → resposta |
| [concepts/genie-requisitos-permissoes-limites.md](concepts/genie-requisitos-permissoes-limites.md) | Unity Catalog, warehouse, throughput, capacidade, entitlements, ACLs |
| [concepts/genie-knowledge-store-e-instrucoes.md](concepts/genie-knowledge-store-e-instrucoes.md) | Knowledge store, exemplos SQL, funções UC, Trusted, parâmetros, texto |
| [concepts/genie-dados-acesso-e-queries.md](concepts/genie-dados-acesso-e-queries.md) | Ativos no espaço, UC além da lista, sugestões de queries, instruções sem conflito |
| [concepts/genie-agent-mode.md](concepts/genie-agent-mode.md) | Agent mode (preview): raciocínio multi-etapas e relatórios |

### Padrões

| Arquivo | Conteúdo |
|---------|-----------|
| [patterns/checklist-configuracao-genie-space.md](patterns/checklist-configuracao-genie-space.md) | Checklist para publicar um espaço com qualidade e governança |

## Agente Cursor (este repositório)

- [`databricks-genie-specialist`](../../agents/databricks/databricks-genie-specialist.md) — persona KB-first para configurar e auditar Genie Spaces.

## Relação com outros domínios

- [Databricks (plataforma)](../databricks/index.md) — Unity Catalog, SQL warehouse, segurança.
- [Trilha de Auditoria](../trilha_auditoria/index.md) — modelo de dados e views quando forem expostas à Genie.

## Incorporar no SisFraude (iframe)

- Lista de salas: **`/lab/genie`**; cada sala: **`/lab/genie/<spaceId>`** (ex.: `sala-cliente`, `visao-produtos`).
- Registro e metadados: `src/config/trilhaGenieSpaces.ts`; URLs em `VITE_TRILHA_GENIE_*` no `.env` (path **`/embed/genie/rooms/<id>`** a partir de **Share → Embed**). Ver `quick-reference.md`.

## Documentação oficial (referência)

- [What is a Genie Space](https://docs.databricks.com/genie/)
- [Set up and manage a Genie Space](https://docs.databricks.com/en/genie/set-up)
- [Use a Genie Space](https://docs.databricks.com/aws/en/genie/talk-to-genie)
- [Knowledge store](https://docs.databricks.com/aws/en/genie/knowledge-store)
- [Genie API](https://docs.databricks.com/api/workspace/genie)
