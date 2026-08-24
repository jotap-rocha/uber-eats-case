# Genie Space — referência rápida

> Tabelas de limite e permissão. Detalhes em `concepts/`.
> **Validação MCP**: null

## Limites numéricos (workspace / espaço)

| Item | Valor típico (doc. Databricks) |
|------|-------------------------------|
| Tabelas ou views por Genie Space | até 30 |
| Instruções por espaço | 100 (cada query exemplo, cada função SQL, bloco geral de texto = 1) |
| Snippets do knowledge store | 200 (descrições, joins, expressões SQL compartilham este teto) |
| Conversas por espaço | até 10.000 |
| Mensagens por conversa | até 10.000 |
| Throughput UI (workspace) | até ~20 perguntas/minuto em todos os espaços |
| Throughput Genie API (preview) | ~5 perguntas/minuto por workspace (best effort) |

## Compute e dados

| Requisito | Detalhe |
|-----------|---------|
| SQL warehouse | Pro ou serverless; criador/editor precisa CAN USE |
| Credenciais embutidas | Ao salvar o warehouse no espaço, credenciais de compute do autor são usadas para **todas** as queries dos usuários |
| Dados | Objetos em UC; `SELECT` nos dados usados |
| Entitlement | Databricks SQL no workspace |

## Permissões do objeto Genie Space

| Nível | Uso típico |
|-------|------------|
| CAN MANAGE | Criador; gestão total |
| CAN EDIT | Configurar dados, knowledge store, instruções, queries sugeridas |
| (usuários finais) | Conforme ACLs do workspace — ver documentação de compartilhamento do espaço |

## Knowledge store vs Instructions

| Tipo | Escopo | Exemplos |
|------|--------|-----------|
| Knowledge store | Só no Genie Space; não altera UC | Sinônimos, joins, medidas/filtros/dimensões, prompt matching |
| Instructions — SQL | Espaço | Queries exemplo (estáticas ou parametrizadas), funções UC |
| Instructions — texto | Espaço | Regras globais de negócio, formato, jargão |

## Trusted

| Ativo | Quando marca Trusted |
|-------|----------------------|
| Query parametrizada | Uso exato do texto parametrizado na resposta |
| Função SQL (UC) | Resposta gerada via função; usuário precisa `EXECUTE` na função |

## URL para iframe (SisFraude / sites externos)

- No workspace: **Genie Space → Share → Embed space** — o `src` do iframe usa o path **`/embed/genie/rooms/<space_id>`** (não confundir com o URL de navegação interna só com `/genie/rooms/`).
- Variáveis no projeto: `VITE_TRILHA_GENIE_VISAO_PRODUTOS_URL`, `VITE_TRILHA_GENIE_SALA_CLIENTE_EMBED_URL` (e outras por sala em `trilhaGenieSpaces.ts`) devem coincidir com o `src` do iframe (HTTPS + `?o=` quando aplicável).

## Links úteis

- [Curate an effective Genie Space (best practices)](https://docs.databricks.com/aws/en/genie/best-practices)
- [Partner-powered AI features](https://docs.databricks.com/aws/en/databricks-ai/partner-powered)
- [Genie Space ACLs](https://docs.databricks.com/aws/en/security/auth/access-control/#genie-space-acls)
