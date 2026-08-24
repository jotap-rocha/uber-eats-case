# Padrão — consultas dinâmicas com allowlist

> **Purpose**: ORDER BY, filtros e colunas selecionáveis sem SQL Injection.  
> **Confidence**: 0.95

## Problema

Permitir que o cliente envie nomes de colunas ou expressões SQL livres abre vetor de **SQL Injection** e exfiltração por erro.

## Solução: allowlist no servidor

### Campos permitidos (exemplo)

```text
nome, data_criacao, status
```

### ORDER BY seguro (pseudo-código)

```typescript
const ALLOWED_SORT = { nome: "nome", data_criacao: "data_criacao", status: "status" } as const;
const dir = input.dir === "desc" ? "DESC" : "ASC";
const column = ALLOWED_SORT[input.sortKey]; // falha se undefined
if (!column) throw new ValidationError("invalid_sort");
// Montar query apenas com `column` e `dir` vindos da allowlist — nunca concatenar input.sortKey cru
```

### Regras

- **Nunca** interpolar `input.orderBy` direto na string SQL.
- Direções: enum estrito (`ASC` | `DESC`).
- Para filtros dinâmicos: mapa de campo → operador permitido (`eq`, `gte`) + bind dos **valores**.

## ORMs

- Preferir APIs tipadas; quando usar `orderByRaw`, só com valores já validados pela allowlist.

## Referências

- [concepts/sql-injection-prevencao.md](../concepts/sql-injection-prevencao.md)
