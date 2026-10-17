---
domain: aws-managed-flink
topic: reference-data
---

# Pattern: reference data (enriquecer stream com dados do S3)

## Problema

Enriquecer eventos do MSK/Kinesis (ex.: `pedidos`) com uma tabela de referência (ex.:
`lojas` → região, gerente) que vive no S3. No Stream Analytics isso é um **reference
data input** com path pattern e refresh; no Flink **não existe input especial** — a
reference data é uma tabela, e a escolha do **tipo de join** define atualização e estado.

## Decisão

| Opção | Atualização da referência | Estado no Flink | Quando |
|---|---|---|---|
| **A. Regular join com tabela S3 bounded** | só no restart da aplicação | tabela inteira + stream (TTL!) | arquivo pequeno, muda raramente (default de lab) |
| **B. Lookup join** (JDBC/Hive) | consulta externa com cache TTL | só cache | referência em banco; não serve para arquivo S3 puro |
| **C. Temporal join com tópico compactado** | contínua, versionada no tempo do evento | versões por chave | referência muda com frequência; já há MSK |
| **D. Broadcast state (DataStream)** | reload periódico custom do S3 | cópia em cada task | lógica custom, Java/PyFlink DataStream |

**Importante:** o connector `filesystem` **não** implementa lookup — `FOR SYSTEM_TIME AS
OF` sobre tabela S3 pura não funciona. Para S3 use A, C (carregando o arquivo no tópico)
ou D.

## Layout no S3

```
s3://<BUCKET>/reference/lojas/lojas.csv          # versão atual (substituída inteira)
s3://<BUCKET>/reference/lojas/_history/dt=…/     # histórico opcional
```

Role da aplicação: `s3:GetObject` em `reference/*` + `s3:ListBucket` com prefixo `reference/`.

## A. Regular join com tabela bounded (mais simples)

```sql
CREATE TABLE lojas (
  loja_id STRING,
  regiao  STRING,
  gerente STRING
) WITH (
  'connector' = 'filesystem',
  'path' = 's3://<BUCKET>/reference/lojas/',
  'format' = 'csv',
  'csv.ignore-parse-errors' = 'true'
);

INSERT INTO pedidos_enriquecidos
SELECT p.pedido_id, p.loja_id, l.regiao, p.valor, p.ts_evento
FROM pedidos AS p
LEFT JOIN lojas AS l ON p.loja_id = l.loja_id;
```

- A tabela S3 é lida **uma vez** (bounded); o join mantém lojas + pedidos em estado.
  Defina TTL para o lado do stream não crescer para sempre:
  `SET 'table.exec.state.ttl' = '1 h';` (cuidado: TTL também expira a referência se não
  for acessada — **risco a validar** com o volume real; alternativa: hints de TTL por
  tabela, Flink ≥ 1.18).
- Saída é **updating** (o LEFT JOIN pode retratar linhas): o sink precisa aceitar
  upsert/retract (Kafka `upsert-kafka`, JDBC com PK). Sink `filesystem` append-only
  **não** aceita — para S3 prefira INNER JOIN com referência carregada ou opção C.
- Atualizar a referência = substituir o arquivo + **restart** da aplicação
  (`stop-application` → `start-application`).
- `'source.monitor-interval' = '10 min'` transforma a fonte em unbounded que **descobre
  arquivos novos** (não relê alterados) — útil para referência append-only. **A validar**
  o comportamento no runtime gerenciado.

## B. Lookup join (referência em banco)

```sql
CREATE TABLE lojas_db (
  loja_id STRING, regiao STRING, PRIMARY KEY (loja_id) NOT ENFORCED
) WITH (
  'connector' = 'jdbc',
  'url' = 'jdbc:postgresql://<HOST>:5432/<DB>',
  'table-name' = 'lojas',
  'username' = '<DB_USER>',                 -- injetar em runtime; senha via Secrets Manager
  'lookup.cache' = 'PARTIAL',
  'lookup.partial-cache.expire-after-write' = '10 min',
  'lookup.partial-cache.max-rows' = '10000'
);

SELECT p.pedido_id, l.regiao
FROM pedidos AS p
JOIN lojas_db FOR SYSTEM_TIME AS OF p.proc_time AS l
  ON p.loja_id = l.loja_id;
```

Exige `proc_time AS PROCTIME()` na fonte. Senha **nunca** no DDL versionado: leia do
Secrets Manager no `main` e monte o DDL em memória (não logar o DDL montado).

## C. Temporal join com tópico compactado (referência versionada)

Um job batch (ou o próprio time) publica `lojas.csv` no tópico compactado
`cadastro.lojas` (chave = `loja_id`; ver `aws-msk/concepts/topics-and-quotas.md`).

```sql
CREATE TABLE lojas_versionada (
  loja_id STRING, regiao STRING, atualizado_em TIMESTAMP(3),
  PRIMARY KEY (loja_id) NOT ENFORCED,
  WATERMARK FOR atualizado_em AS atualizado_em
) WITH (
  'connector' = 'upsert-kafka',
  'topic' = 'cadastro.lojas',
  'properties.bootstrap.servers' = '<BOOTSTRAP>:9098',
  'properties.security.protocol' = 'SASL_SSL',
  'properties.sasl.mechanism' = 'AWS_MSK_IAM',
  'properties.sasl.jaas.config' = 'software.amazon.msk.auth.iam.IAMLoginModule required;',
  'properties.sasl.client.callback.handler.class' = 'software.amazon.msk.auth.iam.IAMClientCallbackHandler',
  'key.format' = 'raw',
  'value.format' = 'json'
);

SELECT p.pedido_id, l.regiao
FROM pedidos AS p
LEFT JOIN lojas_versionada FOR SYSTEM_TIME AS OF p.ts_evento AS l
  ON p.loja_id = l.loja_id;
```

- Cada pedido pega a versão da loja **vigente no tempo do evento** — o equivalente mais
  fiel ao reference data com snapshot por data do ASA.
- Saída append-only (event-time temporal join) → serve para sink S3.
- Watermark da referência precisa avançar; referência parada pode segurar o join —
  **risco a validar** (`table.exec.source.idle-timeout`).

## D. Broadcast state (DataStream)

Fonte custom que relê `s3://<BUCKET>/reference/lojas/` a cada N minutos → `broadcast()`
→ `KeyedBroadcastProcessFunction` enriquece o stream. Flexível (reload sem restart),
porém mais código e teste. Use se A/C não atenderem.

## Critérios de aceite

- [ ] Pedido com `loja_id` conhecido sai com `regiao` preenchida.
- [ ] Pedido com `loja_id` desconhecido: comportamento definido (LEFT → `NULL`, ou descarte).
- [ ] Atualização da referência reflete no output dentro do SLA definido
      (A: após restart; B: ≤ TTL do cache; C: imediato pelo tempo de evento).
- [ ] Estado (`lastCheckpointSize`) estável após 1 h de carga.

## Anti-padrões

| Errado | Certo |
|---|---|
| `FOR SYSTEM_TIME AS OF` em tabela `filesystem` | A, C ou D |
| Regular join sem TTL em stream infinito | `table.exec.state.ttl` ou temporal join |
| Credencial JDBC no `environment_properties` | Secrets Manager lido no runtime |
| Recarregar referência "editando" o objeto sem restart (opção A) | restart ou opção C/D |
