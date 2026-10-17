---
domain: azure-synapse
topic: merge-scd2
---

# Pattern — merge-scd2 (dimensão histórica no dedicated pool)

SCD Tipo 2: cada mudança de atributo fecha a versão corrente e abre uma nova.
No Synapse dedicated o MERGE **não** tem `OUTPUT`/composable DML e **não** aceita
`WHEN NOT MATCHED INSERT` em tabela com `IDENTITY` → o padrão é **2 passos numa
transação**: (1) MERGE fecha versões alteradas; (2) INSERT abre versões novas.

## 1. Tabela de dimensão

```sql
CREATE TABLE dbo.dim_produto
(
    produto_sk     BIGINT IDENTITY(1,1) NOT NULL,  -- não contíguo, não ordenado
    produto_id     INT            NOT NULL,        -- business key
    nome           NVARCHAR(200)  NULL,
    categoria      NVARCHAR(100)  NULL,
    preco          DECIMAL(18,2)  NULL,
    row_hash       BINARY(32)     NOT NULL,
    valid_from     DATETIME2      NOT NULL,
    valid_to       DATETIME2      NULL,             -- NULL = versão corrente
    is_current     BIT            NOT NULL
)
WITH (DISTRIBUTION = HASH(produto_id), CLUSTERED COLUMNSTORE INDEX);
```

`HASH(business key)`: o join do MERGE fica local à distribuição (sem data movement) e a
chave de distribuição nunca é atualizada.

## 2. Fonte deduplicada com hash

Staging pode ter várias linhas por chave (reprocesso, CDC). MERGE com múltiplos matches
falha → deduplicar antes, ficando com a mais recente.

```sql
IF OBJECT_ID('tempdb..#src') IS NOT NULL DROP TABLE #src;
CREATE TABLE #src WITH (DISTRIBUTION = HASH(produto_id), HEAP) AS
SELECT produto_id, nome, categoria, preco,
       HASHBYTES('SHA2_256',
         CONCAT_WS('|', ISNULL(nome, N'~'), ISNULL(categoria, N'~'),
                        ISNULL(CAST(preco AS NVARCHAR(40)), N'~'))) AS row_hash
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY produto_id
                                 ORDER BY atualizado_em DESC) AS rn
    FROM stg.produto
) d
WHERE rn = 1;
```

`ISNULL(..., '~')` evita que NULL→valor passe despercebido no hash.

## 3. Passo 1 + Passo 2 numa transação

```sql
DECLARE @load_ts DATETIME2 = SYSUTCDATETIME();

BEGIN TRANSACTION;

-- Passo 1: fecha a versão corrente das chaves cujo hash mudou
MERGE dbo.dim_produto AS t
USING #src AS s
   ON t.produto_id = s.produto_id
  AND t.is_current = 1
WHEN MATCHED AND t.row_hash <> s.row_hash THEN
    UPDATE SET t.is_current = 0,
               t.valid_to   = @load_ts;   -- ';' final obrigatório

-- Passo 2: insere versão corrente para chaves novas e para as fechadas no passo 1
INSERT INTO dbo.dim_produto
    (produto_id, nome, categoria, preco, row_hash, valid_from, valid_to, is_current)
SELECT s.produto_id, s.nome, s.categoria, s.preco, s.row_hash,
       @load_ts, NULL, 1
FROM #src AS s
LEFT JOIN dbo.dim_produto AS t
       ON t.produto_id = s.produto_id
      AND t.is_current = 1
WHERE t.produto_id IS NULL;

COMMIT TRANSACTION;
```

Idempotente: rodar de novo com o mesmo staging não fecha nada (hash igual) nem insere
nada (já existe corrente).

Em caso de erro: `ROLLBACK` no orquestrador (Synapse suporta transações explícitas;
`SET XACT_ABORT ON` antes do `BEGIN` faz o rollback automático — **a validar** no seu
build). Transações grandes em DW100c são lentas: carregar em lotes se o staging for enorme.

## 4. Deleções na origem (opcional)

Se a origem manda snapshot completo, chaves ausentes podem ser fechadas:

```sql
MERGE dbo.dim_produto AS t
USING #src AS s ON t.produto_id = s.produto_id
WHEN NOT MATCHED BY SOURCE AND t.is_current = 1 THEN
    UPDATE SET t.is_current = 0, t.valid_to = @load_ts;
```

Só com snapshot completo — com carga incremental isso fecharia tudo que não veio.

## 5. Variante SCD1 (sobrescreve) com MERGE único

Permitido quando o alvo é `HASH` **e não tem `IDENTITY`**:

```sql
MERGE dbo.dim_categoria AS t
USING #src_cat AS s ON t.categoria_id = s.categoria_id
WHEN MATCHED AND t.nome <> s.nome THEN UPDATE SET t.nome = s.nome
WHEN NOT MATCHED BY TARGET THEN INSERT (categoria_id, nome) VALUES (s.categoria_id, s.nome);
```

## 6. Checagens pós-carga

```sql
-- No máximo 1 corrente por chave
SELECT produto_id FROM dbo.dim_produto WHERE is_current = 1
GROUP BY produto_id HAVING COUNT(*) > 1;

-- Versão fechada sem valid_to (inconsistência)
SELECT produto_id FROM dbo.dim_produto
WHERE is_current = 0 AND valid_to IS NULL;
```

Ambas devem retornar 0 linhas — bom candidato a teste de qualidade (KB/agent de data
quality).

## Armadilhas

| Sintoma | Causa |
|---|---|
| "NOT MATCHED ... not supported" | alvo não é HASH ou tem IDENTITY → usar 2 passos |
| Erro de múltiplas linhas no MERGE | staging não deduplicado |
| Linhas em distribuição errada após MERGE | build < 10.0.17829.0 → pause/resume para atualizar |
| Row count "dobrado" | update do MERGE = delete + insert (esperado) |
| `valid_from` diferente entre passos | usar a mesma `@load_ts` nos dois |
