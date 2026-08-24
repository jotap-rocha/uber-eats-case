# pyodbc no destino IHMTZBDBI — contorno SSL Java 11

> **Revisão documental:** 2026-06-03  
> **Status:** ✅ **Validado em PRD** — Job 08 (`database_tables_size`)  
> **Projeto:** `data-sql-capacity-evolution-prd`  
> **Relacionado:** [`java11-sqlserver-ssl-dual-cause.md`](java11-sqlserver-ssl-dual-cause.md) · [`sql-capacity-yarn-prd-piloto.md`](sql-capacity-yarn-prd-piloto.md)

## Problema

Após migração para **YARN + OpenJDK 11**, operações JDBC no **destino** `IHMTZBDBI` (`SQL_SERVER_HOSTNAME_DESTINATION`) falham com:

```text
Algorithm constraints check failed on signature algorithm: SHA1withRSA
Certificates do not conform to algorithm constraints
```

| Operação | Driver | Resultado típico |
|----------|--------|------------------|
| Leitura **origem** (ex.: `ISMTZBDPGBL01`) | `mssql-jdbc` via Spark JDBC | ✅ OK |
| DELETE / INSERT **destino** (`IHMTZBDBI`) | `mssql-jdbc` via JVM (Java 11) | ❌ Falha SSL |

O certificado do SQL Server destino usa assinatura legada **SHA1withRSA**. O Java 11 bloqueia no handshake TLS (`AbstractTrustManagerWrapper.checkAlgorithmConstraints`), **independente** de `trustServerCertificate=true`.

## Por que workarounds JVM não bastaram

Foram testadas (sem sucesso no destino):

| Tentativa | Resultado |
|-----------|-----------|
| `-Djdk.certpath.disabledAlgorithms=` vazio | SHA1 continua bloqueado |
| `Security.setProperty()` após `SparkSession` | Cache estático de `DisabledAlgorithmConstraints` |
| javaagent `premain` (`SslPremainAgent`) | Propriedades aplicadas, handshake ainda falha |
| `SslTrustAllInstaller.installGlobally()` | TrustAll não bypassa `checkAlgorithmConstraints` |
| Fallback `encrypt=false` | Destino com **ForceEncryption** — também falha |

**Conclusão:** para **escrita no IHMTZBDBI** com Java 11, contornar a stack SSL da JVM.

## Solução validada — pyodbc (OpenSSL)

Usar **pyodbc** + **ODBC Driver 17 for SQL Server** no **driver Python** para DELETE e INSERT no destino. O OpenSSL do sistema **não** aplica as mesmas restrições de algoritmo do Java 11.

```text
┌─────────────────┐     mssql-jdbc (Java)      ┌──────────────────┐
│  Spark / Job    │ ─────────────────────────► │  SQL Server      │
│  (leitura)      │                            │  ORIGEM          │
└─────────────────┘                            └──────────────────┘

┌─────────────────┐     pyodbc (OpenSSL)       ┌──────────────────┐
│  Driver Python  │ ─────────────────────────► │  IHMTZBDBI       │
│  (DELETE/INSERT)│                            │  DatabaseCapacity│
└─────────────────┘                            └──────────────────┘
```

### Artefactos no repositório

| Ficheiro | Papel |
|----------|-------|
| `src/utils/pyodbc_sqlserver.py` | Connection string, `execute_non_query`, `insert_dataframe` (`fast_executemany`) |
| `src/jobs/08_app_database_tables_size.py` | DELETE e INSERT destino via pyodbc (default); JDBC como fallback |
| `requirements.txt` | `pyodbc==5.3.0` |

### Fluxo no Job 08

1. **Origem:** Spark JDBC (`mssql-jdbc`) — inalterado.
2. **DELETE** (últimos 7 dias): `pyodbc_execute_non_query()` → `IHMTZBDBI`.
3. **INSERT:** `pyodbc_insert_dataframe()` — `df.toPandas()` + `executemany`.
4. Se pyodbc falhar → retenta JDBC (compatibilidade).

### Variáveis de ambiente

| Variável | Default | Efeito |
|----------|---------|--------|
| `SQLCAPACITY_DEST_USE_PYODBC` | `true` | Destino via pyodbc |
| `SQLCAPACITY_ODBC_DRIVER` | auto-detect | Ex.: `ODBC Driver 17 for SQL Server` |
| `SQLCAPACITY_DEST_USE_PYODBC=false` | — | Força JDBC no destino (vai falhar no IHMTZBDBI com Java 11) |

Credenciais destino (inalteradas): `SQL_SERVER_HOSTNAME_DESTINATION`, `SQL_SERVER_DATABASE_CAPACITY_EVOLUTION`, `SQL_SERVER_USER_DESTINATION`, `SQL_SERVER_PASSWORD_DESTINATION` (OCI Vault / `.env`).

### Connection string (referência)

```python
from src.utils.pyodbc_sqlserver import build_pyodbc_connection_string

conn_str = build_pyodbc_connection_string(
    host="IHMTZBDBI",
    port="1433",
    database="DatabaseCapacity",
    user="...",
    password="...",
)
# Encrypt=yes;TrustServerCertificate=yes;
```

## Pré-requisitos no cluster (311–314)

Documentado em [`../../infra/STATUS-AMBIENTE.md`](../../infra/STATUS-AMBIENTE.md):

| Componente | Estado |
|------------|--------|
| `unixODBC` (`libodbc.so.2`) | ✅ nós 311–314 |
| `msodbcsql17` (Microsoft ODBC Driver 17) | ✅ |
| `pyodbc` no venv do projeto | ✅ `requirements.txt` |

Verificação rápida:

```bash
source /DATALAKE/workspace/prd/data-sql-capacity-evolution-prd/.venv/bin/activate
python -c "import pyodbc; print([d for d in pyodbc.drivers() if 'SQL Server' in d])"
# Esperado: ['ODBC Driver 17 for SQL Server']
```

Teste de conectividade (sem expor senha no log):

```bash
cd /DATALAKE/workspace/prd/data-sql-capacity-evolution-prd
source .venv/bin/activate && export PYTHONPATH=$PWD
python -c "
from dotenv import load_dotenv; load_dotenv('.env')
from src.utils import key_oci
from src.utils.pyodbc_sqlserver import build_pyodbc_connection_string
import pyodbc
cs = build_pyodbc_connection_string(
    host=key_oci.return_secret('SQL_SERVER_HOSTNAME_DESTINATION'),
    port='1433',
    database=key_oci.return_secret('SQL_SERVER_DATABASE_CAPACITY_EVOLUTION'),
    user=key_oci.return_secret('SQL_SERVER_USER_DESTINATION'),
    password=key_oci.return_secret('SQL_SERVER_PASSWORD_DESTINATION'),
)
with pyodbc.connect(cs, timeout=30) as c:
    c.claude().execute('SELECT @@VERSION')
    print('OK')
"
```

## Resultado validado (Job 08 — 2026-06-03)

Comando:

```bash
bash '/DATALAKE/workspace/prd/data-sql-capacity-evolution-prd/scripts/PRD/run_prd__08_app_database_tables_size__08.sh' \
  --instancia "ISMTZBDPGBL01\MSSQLSERVER" --database "PGBL" \
  --esteira "PRODUÇÃO" --timeout 1800
```

| Etapa | Resultado |
|-------|-----------|
| Leitura origem | 100 tabelas via JDBC Spark |
| DELETE destino | 100 linhas via **pyodbc** |
| INSERT destino | 100 registros em ~2,4s via **pyodbc** |
| Exit code | **0** |

## Replicar nos jobs 01–07

Ao portar cada job para YARN:

1. Importar funções de `src/utils/pyodbc_sqlserver.py`.
2. Usar pyodbc para **DELETE** e **INSERT/append** no destino `IHMTZBDBI`.
3. Manter JDBC Spark para **leitura na origem** (certificados origem geralmente OK).
4. Avaliar volume: Job 08 usa `toPandas()` (~100 linhas). Jobs com **milhões de linhas** precisam de estratégia de batch (`fetchmany` / partições) — não copiar cegamente o padrão do Job 08.

Checklist:

```text
[ ] pyodbc + ODBC Driver 17 disponíveis no nó de submit
[ ] SQLCAPACITY_DEST_USE_PYODBC=true (default)
[ ] DELETE destino migrado para pyodbc
[ ] INSERT destino migrado para pyodbc (ou fallback JDBC documentado)
[ ] Teste manual spark-submit → YARN COMPLETED
[ ] Matriz actualizada em prd-jobs-test-and-matrix.md
```

## Limitações e alternativas

| Aspecto | Nota |
|---------|------|
| **`toPandas()` no driver** | INSERT **não** usa processamento distribuído — materializa tudo no driver antes do `executemany` |
| Volume Job 08 (~100 linhas) | Adequado; executors ficam ociosos só na fase de escrita |
| Jobs 01–07 / milhões de linhas | Avaliar memória do driver antes de replicar; considerar `foreachPartition` ou certificado renovado |
| Duas stacks de conexão | Origem JDBC Spark + destino pyodbc — job **continua** PySpark |
| Solução definitiva | **Renovar certificado SSL** no SQL Server `IHMTZBDBI` (SHA-256+) — permite voltar a `df.write.jdbc` distribuído |

### O que é distribuído vs não (resumo)

| Fase | PySpark distribuído? |
|------|---------------------|
| Leitura origem (JDBC Spark) | ✅ Sim |
| Transformações (`DataProcessor`, casts, etc.) | ✅ Sim |
| DELETE destino (pyodbc) | ❌ Driver apenas |
| INSERT destino (`toPandas` + pyodbc) | ❌ Driver apenas |

Documentação modelo híbrido: [`pyodbc-destino-hibrido-pyspark.md`](pyodbc-destino-hibrido-pyspark.md)

## Anti-padrões

| Evitar | Motivo |
|--------|--------|
| Insistir só em flags JVM para destino IHMTZBDBI | Validado: não resolve SHA1withRSA no handshake |
| `-Djdk.jar.disabledAlgorithms=...` inline no bash | Quebra JVM (`ClassNotFoundException: MD5`) |
| Desactivar pyodbc sem certificado renovado | INSERT/DELETE destino volta a falhar |
| pyodbc na origem sem necessidade | Origem JDBC Spark funciona; manter separação origem/destino |

## Referências cruzadas

- Causa raiz SSL Java: [`java11-sqlserver-ssl-dual-cause.md`](java11-sqlserver-ssl-dual-cause.md)
- Piloto YARN Job 08: [`sql-capacity-yarn-prd-piloto.md`](sql-capacity-yarn-prd-piloto.md)
- ODBC no cluster: [`../../infra/STATUS-AMBIENTE.md`](../../infra/STATUS-AMBIENTE.md)
- Agente migração: `@.claude/agents/data-engineering/spark-cluster-migration-expert.md`
- Código: `src/utils/pyodbc_sqlserver.py`, `src/jobs/08_app_database_tables_size.py`
- Modelo híbrido: [`pyodbc-destino-hibrido-pyspark.md`](pyodbc-destino-hibrido-pyspark.md)
