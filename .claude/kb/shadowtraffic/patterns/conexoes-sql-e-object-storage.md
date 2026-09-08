# Configuração de conexões: Oracle/Postgres (SQL) e S3/MinIO

> **Purpose**: Referência de configuração das 3 connections reais deste projeto, para editar `gen/unified/uber-eats.json.template` sem adivinhar chaves.
> **MCP Validated**: 2026-09-07 — fonte: docs.shadowtraffic.io/connections/{s3,oracle}/

## When to Use

- Adicionando um novo generator a uma connection já existente (`postgres`, `oracle`, `minio`).
- Adicionando uma **nova** connection (ex.: um 4º sistema de origem).
- Depurando erro de conexão/gravação do ShadowTraffic.

## Implementation — S3 / MinIO (connection `minio`, kind `s3`)

```json
"minio": {
  "kind": "s3",
  "connectionConfigs": {
    "endpoint": "http://minio-ubereats:9000",
    "pathStyleAccess": true
  }
}
```

- `endpoint` + `pathStyleAccess: true` é o padrão específico para compatibilidade com MinIO (S3 real não precisa disso).
- Credenciais **não** vão no JSON — vêm de env: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION` (ou `AWS_SESSION_TOKEN`).
- Cada generator que grava em S3/MinIO define `bucket` + `bucketConfigs` (`keyPrefix` obrigatório, `format`: `json`/`jsonl`/`parquet`/`log`; este projeto usa sempre `jsonl`). Objetos ficam nomeados `<keyPrefix>-<ulid>.<sufixo>`, ordenáveis por nome (ULID monotônico).

## Implementation — Oracle (connection `oracle`)

```json
"oracle": {
  "kind": "oracle",
  "connectionConfigs": {
    "host": "REPLACE_ORACLE_HOST",
    "port": REPLACE_ORACLE_PORT,
    "db": "REPLACE_ORACLE_SERVICE",
    "username": "REPLACE_ORACLE_USER",
    "password": "REPLACE_ORACLE_PASSWORD"
  }
}
```

- `db` = o service name Oracle (`FREEPDB1` neste projeto, via `ORACLE_SERVICE`).
- `tablePolicy` (não setado aqui → default `create`): `create` | `dropAndCreate` | `manual`. Ver nuance em `patterns/nome-de-campo-igual-a-coluna-real.md`.
- DML: por padrão só `INSERT`; `op: "update"`/`"delete"` exigem `where` mapeando coluna→valor de filtro (usado extensivamente em `orders`/`payments`, ver `concepts/mutacao-real-fork-statemachine.md`).
- Transações a cada 20ms ou 500 linhas (o que vier primeiro) — não configurável por generator individual neste projeto.
- Tipos default se a tabela for auto-criada: UUID/string → `VARCHAR2(4000)`, distribuição numérica → `FLOAT(126)`, boolean → `VARCHAR2(4000)` — por isso os generators deste projeto usam `sqlHint` para tipos mais específicos (ex.: `NUMBER(10) PRIMARY KEY`) quando a criação automática seria usada.

## Implementation — Postgres (connection `postgres`)

```json
"postgres": {
  "kind": "postgres",
  "connectionConfigs": {
    "host": "REPLACE_POSTGRES_HOST",
    "port": REPLACE_POSTGRES_PORT,
    "db": "REPLACE_POSTGRES_DB",
    "username": "REPLACE_POSTGRES_USER",
    "password": "REPLACE_POSTGRES_PASSWORD",
    "sslmode": "disable"
  }
}
```

Mesmas regras gerais de nome-de-coluna e `op: update`/`where` da connection Oracle se aplicam (mecanismo genérico do ShadowTraffic para destinos SQL).

## Configuration

| Setting | Default | Description |
|---|---|---|
| `bucketConfigs.format` | — (obrigatório) | `json` \| `jsonl` \| `parquet` \| `log` — projeto usa sempre `jsonl` |
| `connectionConfigs.pathStyleAccess` | `false` | Precisa ser `true` para MinIO |
| `tablePolicy` (SQL) | `create` | `create` \| `dropAndCreate` \| `manual` |

## See Also

- [conceitos-fundamentais](../concepts/conceitos-fundamentais.md)
- [nome-de-campo-igual-a-coluna-real](nome-de-campo-igual-a-coluna-real.md)
