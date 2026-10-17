---
domain: gcp-bigquery
topic: merge-scd2
---

# Pattern: SCD Tipo 2 com `MERGE`

## Problema

Manter histórico de atributos de uma dimensão (ex.: segmento e plano do cliente) em uma única
operação atômica: fechar a versão vigente que mudou e inserir a nova versão.

## Solução

`MERGE` com fonte "duplicada" via `UNION ALL`:

- Linha com `merge_key = chave` → casa com a versão vigente → `UPDATE` fecha a versão.
- Linha com `merge_key = NULL` (só para chaves que mudaram) → nunca casa → `INSERT` da nova
  versão.
- Chave nova → `merge_key` não casa → `INSERT` da primeira versão.

Requer projeto com billing (sandbox não permite DML).

## 1. Dimensão

```sql
CREATE TABLE IF NOT EXISTS `<GCP_PROJECT_ID>.dw.dim_cliente` (
  cliente_sk  STRING    NOT NULL,   -- GENERATE_UUID()
  cliente_id  STRING    NOT NULL,   -- chave de negócio
  segmento    STRING,
  plano       STRING,
  row_hash    INT64     NOT NULL,
  valid_from  TIMESTAMP NOT NULL,
  valid_to    TIMESTAMP,
  is_current  BOOL      NOT NULL
)
CLUSTER BY cliente_id;
```

## 2. Staging com hash

```sql
CREATE OR REPLACE TEMP TABLE stg AS
SELECT cliente_id, segmento, plano,
       FARM_FINGERPRINT(TO_JSON_STRING(STRUCT(segmento, plano))) AS row_hash,
       CURRENT_TIMESTAMP() AS loaded_at
FROM `<GCP_PROJECT_ID>.staging.clientes`
QUALIFY ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY updated_at DESC) = 1;
```

`QUALIFY` garante **uma linha por chave** — sem isso o `MERGE` falha com
"UPDATE/MERGE must match at most one source row".

`TEMP TABLE` exige execução em script/sessão (mesmo job multi-statement).

## 3. MERGE

```sql
MERGE `<GCP_PROJECT_ID>.dw.dim_cliente` AS t
USING (
  SELECT s.cliente_id AS merge_key, s.* FROM stg AS s
  UNION ALL
  SELECT NULL AS merge_key, s.*
  FROM stg AS s
  JOIN `<GCP_PROJECT_ID>.dw.dim_cliente` AS d
    ON d.cliente_id = s.cliente_id AND d.is_current
  WHERE d.row_hash != s.row_hash
) AS src
ON t.cliente_id = src.merge_key AND t.is_current
WHEN MATCHED AND t.row_hash != src.row_hash THEN
  UPDATE SET valid_to = src.loaded_at, is_current = FALSE
WHEN NOT MATCHED THEN
  INSERT (cliente_sk, cliente_id, segmento, plano, row_hash,
          valid_from, valid_to, is_current)
  VALUES (GENERATE_UUID(), src.cliente_id, src.segmento, src.plano, src.row_hash,
          src.loaded_at, NULL, TRUE);
```

Sem mudança (`row_hash` igual) → a linha casa, mas nenhuma cláusula age → no-op.

## 4. Deletes na origem (opcional)

```sql
WHEN NOT MATCHED BY SOURCE AND t.is_current THEN
  UPDATE SET valid_to = CURRENT_TIMESTAMP(), is_current = FALSE
```

Só use se o staging for **snapshot completo**; com carga incremental fecharia tudo que não
veio no lote.

## 5. Verificação

```sql
-- no máximo 1 versão vigente por chave
SELECT cliente_id FROM `<GCP_PROJECT_ID>.dw.dim_cliente`
WHERE is_current GROUP BY cliente_id HAVING COUNT(*) > 1;   -- esperado: 0 linhas

-- intervalos sem sobreposição
SELECT cliente_id FROM (
  SELECT cliente_id, valid_from,
         LAG(valid_to) OVER (PARTITION BY cliente_id ORDER BY valid_from) AS prev_to
  FROM `<GCP_PROJECT_ID>.dw.dim_cliente`)
WHERE prev_to IS NOT NULL AND prev_to > valid_from;          -- esperado: 0 linhas
```

## Custo

`MERGE` lê a dimensão inteira (ou as partições/clusters tocados) + staging. Dimensão
clusterizada por `cliente_id` reduz bytes; em lab, use `maximum_bytes_billed` no job.

## SI

Se a dimensão tiver PII (nome, e-mail, CPF): fora do `row_hash` só se não for histórico; em
qualquer caso, policy tags/mascaramento na leitura. Nunca logar valores da linha no orquestrador.

## Anti-patterns

- `UPDATE` + `INSERT` em dois statements sem transação (janela de inconsistência).
- Comparar coluna a coluna com `!=` (NULL quebra a comparação) — use hash.
- `valid_to = '9999-12-31'` e `NULL` misturados na mesma tabela.
