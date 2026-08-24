# SQL Injection — prevenção

> **Purpose**: Impedir execução de SQL arbitrário via entrada do usuário.  
> **Confidence**: 0.96

## Regra de ouro

**Nunca** montar SQL concatenando strings com entrada do usuário.

### Exemplo perigoso

```python
sql = "SELECT * FROM users WHERE name = '" + user_input + "'"
```

### Parâmetros (prepared statements)

```python
cursor.execute(
    "SELECT * FROM users WHERE name = ?",
    (user_input,),
)
```

Mesmo princípio em drivers Node (`$1`, `?`), Java `PreparedStatement`, etc.

## ORM e query builders

- ORMs costumam parametrizar automaticamente — **ainda assim** evitar APIs que interpolam SQL cru (`raw()` sem bind).

## Filtros e ORDER BY dinâmicos

- **Allowlist** de colunas e direções permitidas.
- Nunca permitir que o cliente envie livremente `ORDER BY qualquer_coisa` ou expressões `WHERE` arbitrárias.

Ver [patterns/consultas-dinamicas-allowlist.md](../patterns/consultas-dinamicas-allowlist.md).

## No ecossistema Postgres / Supabase

- PostgREST: usar políticas e tipos; evitar RPC que concatena SQL.
- Apps que montam SQL no servidor: revisão obrigatória de todo trecho dinâmico.

## Referências cruzadas

- [banco-dados-seguro.md](banco-dados-seguro.md), [backend-seguro.md](backend-seguro.md)
