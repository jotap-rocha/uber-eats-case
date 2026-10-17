---
domain: aws-redshift
topic: merge-scd2
---

# Pattern: SCD2 com `MERGE` no Redshift

## Problema

Manter histórico (SCD tipo 2) de uma dimensão a partir da staging carregada por `COPY`
(ver `bulk-load.md`). Paridade com o pattern de MERGE/SCD2 do Synapse.

## Restrições do `MERGE` no Redshift (validadas na doc)

| Restrição | Impacto no SCD2 |
|---|---|
| Só **um** `WHEN MATCHED` (UPDATE **ou** DELETE) e um `WHEN NOT MATCHED` (INSERT) | não dá para "fechar e inserir" a mesma chave num único match |
| Linha do alvo **não pode** casar com várias linhas da fonte | fonte deduplicada por chave de merge |
| Sem `WITH` (CTE) no MERGE | use subquery ou tabela temporária |
| Fonte não pode referenciar o alvo em subquery | prepare a fonte **antes** numa temp table |
| `match_condition` = predicados de igualdade | case por coluna(s) de chave, não por expressão |

Por isso o SCD2 usa o truque da **fonte preparada com chave de merge nula** para as
linhas a inserir.

## Tabela de dimensão

```sql
CREATE TABLE IF NOT EXISTS dw.dim_cliente (
  sk            VARCHAR(32)  NOT NULL,   -- md5(cliente_id || valid_from)
  cliente_id    BIGINT       NOT NULL,
  nome          VARCHAR(200),
  cidade        VARCHAR(100),
  row_hash      VARCHAR(32)  NOT NULL,   -- md5 dos atributos rastreados
  valid_from    TIMESTAMP    NOT NULL,
  valid_to      TIMESTAMP,
  is_current    BOOLEAN      NOT NULL
)
DISTKEY (cliente_id) SORTKEY (cliente_id, valid_from);
```

## Passo 1 — preparar a fonte (temp table, fora do MERGE)

```sql
CREATE TEMP TABLE src_scd2 AS
WITH stg AS (
  SELECT cliente_id, nome, cidade, atualizado_em,
         md5(coalesce(nome,'') || '|' || coalesce(cidade,'')) AS row_hash,
         row_number() OVER (PARTITION BY cliente_id ORDER BY atualizado_em DESC) AS rn
  FROM staging.clientes
),
dedup AS (SELECT * FROM stg WHERE rn = 1),
mudou AS (                                   -- novos ou com atributo alterado
  SELECT d.*, cur.sk AS sk_atual
  FROM dedup d
  LEFT JOIN dw.dim_cliente cur
    ON cur.cliente_id = d.cliente_id AND cur.is_current
  WHERE cur.sk IS NULL OR cur.row_hash <> d.row_hash
)
-- (a) linha que FECHA a versão atual: merge_sk = sk atual
SELECT sk_atual AS merge_sk, cliente_id, nome, cidade, row_hash, atualizado_em
FROM mudou WHERE sk_atual IS NOT NULL
UNION ALL
-- (b) linha que INSERE a nova versão: merge_sk NULL nunca casa
SELECT NULL::VARCHAR(32), cliente_id, nome, cidade, row_hash, atualizado_em
FROM mudou;
```

## Passo 2 — MERGE

```sql
BEGIN;

MERGE INTO dw.dim_cliente
USING src_scd2 s
ON dw.dim_cliente.sk = s.merge_sk
WHEN MATCHED THEN UPDATE SET
  valid_to   = s.atualizado_em,
  is_current = false
WHEN NOT MATCHED THEN INSERT
  (sk, cliente_id, nome, cidade, row_hash, valid_from, valid_to, is_current)
VALUES
  (md5(s.cliente_id::VARCHAR || '|' || s.atualizado_em::VARCHAR),
   s.cliente_id, s.nome, s.cidade, s.row_hash, s.atualizado_em, NULL, true);

COMMIT;
ANALYZE dw.dim_cliente;
```

Como funciona:

- Linhas (a) casam com o `sk` da versão corrente → `UPDATE` fecha a versão.
- Linhas (b) têm `merge_sk` nulo → nunca casam → `INSERT` da nova versão.
- Cliente novo só gera (b). Cliente sem mudança não aparece na fonte.
- Cada `sk` do alvo casa com no máximo uma linha (a) → sem erro de múltiplos matches.

## Alternativa: duas instruções na mesma transação

Mais legível para revisão; mesmo resultado:

```sql
BEGIN;
UPDATE dw.dim_cliente SET valid_to = s.atualizado_em, is_current = false
FROM src_scd2 s
WHERE dw.dim_cliente.sk = s.merge_sk;

INSERT INTO dw.dim_cliente (sk, cliente_id, nome, cidade, row_hash, valid_from, valid_to, is_current)
SELECT md5(cliente_id::VARCHAR || '|' || atualizado_em::VARCHAR),
       cliente_id, nome, cidade, row_hash, atualizado_em, NULL, true
FROM src_scd2 WHERE merge_sk IS NULL;
COMMIT;
```

## SCD1 (sobrescrever) — forma simplificada

Se alvo e fonte têm as mesmas colunas na mesma ordem:

```sql
MERGE INTO dw.dim_produto USING staging.produto
ON dw.dim_produto.produto_id = staging.produto.produto_id
REMOVE DUPLICATES;
```

`REMOVE DUPLICATES` é mais rápido que `WHEN MATCHED/NOT MATCHED`.

## Testes de aceite

```sql
-- no máximo 1 versão corrente por chave
SELECT cliente_id FROM dw.dim_cliente WHERE is_current GROUP BY 1 HAVING count(*) > 1;
-- nenhuma versão fechada sem valid_to
SELECT count(*) FROM dw.dim_cliente WHERE NOT is_current AND valid_to IS NULL;
```

Ambas devem retornar vazio/0. **Risco a validar:** reprocessar a mesma staging duas vezes
deve ser idempotente (o filtro `row_hash <>` garante; teste com carga repetida).
