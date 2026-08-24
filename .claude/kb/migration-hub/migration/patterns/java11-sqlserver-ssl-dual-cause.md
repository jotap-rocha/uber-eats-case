# Java 11 + SQL Server — SSL SHA1withRSA (duas causas)

> **Revisão documental:** 2026-06-03  
> **Contexto:** Migração Standalone (Java 8) → **YARN + OpenJDK 11** (cluster 311–314)  
> **Projeto piloto:** `data-sql-capacity-evolution-prd` — Job 08  
> **Solução operacional validada (destino IHMTZBDBI):** [`pyodbc-destino-ihmtzbdbi.md`](pyodbc-destino-ihmtzbdbi.md)  
> **Relacionado:** [`sql-capacity-yarn-prd-piloto.md`](sql-capacity-yarn-prd-piloto.md) · [`../../infra/java/01-java-11-openjdk.md`](../../infra/java/01-java-11-openjdk.md)

## Sintoma típico

Leitura JDBC na **origem** OK; **DELETE/INSERT no destino** falham:

```text
Certificates do not conform to algorithm constraints
Algorithm constraints check failed on signature algorithm: SHA1withRSA
```

Mesmo com `encrypt=true` e `trustServerCertificate=true` na URL JDBC.

## Por que aparece na migração

| Ambiente | Java | Comportamento |
|----------|------|---------------|
| Cluster legado (`islnx011:7077`) | **Java 8** | Aceita certificados SHA1withRSA |
| Cluster novo (311–314, YARN) | **OpenJDK 11.0.25** | Rejeita SHA1withRSA por **duas** restrições independentes |

`trustServerCertificate=true` **não** contorna validação de **algoritmo de assinatura** — só afeta confiança na cadeia CA.

## As duas causas (obrigatório tratar ambas)

O Java 11 aplica restrições em **dois pontos** distintos. Corrigir só um deixa o erro activo.

| # | Propriedade | Default Java 11 (resumo) | Efeito se ignorada |
|---|-------------|--------------------------|---------------------|
| **1** | `jdk.certpath.disabledAlgorithms` | inclui `SHA1 jdkCA & usage TLSServer` | Bloqueia certificados SHA1 no path PKIX |
| **2** | **`jdk.jar.disabledAlgorithms`** | **inclui `SHA1`** | **Bloqueia assinatura `SHA1withRSA` no handshake TLS** ← causa mais frequente após migração |

### Erro enganoso com `-D` vazio

`-Djdk.certpath.disabledAlgorithms=` (string vazia) **não** remove as restrições no OpenJDK 11.0.25 — o runtime mantém o default.  
`java.security.properties` **sozinho** também pode não propagar para a JVM do driver em YARN client mode.

## Solução validada para escrita no destino (2026-06-03)

Workarounds **JVM** (certpath, jar, TrustAll, javaagent premain) **não resolvem** o handshake TLS para `IHMTZBDBI` — o JDK continua a executar `checkAlgorithmConstraints` sobre certificados SHA1withRSA.

**Padrão adoptado:** DELETE e INSERT no destino via **pyodbc** (OpenSSL), mantendo **mssql-jdbc** apenas para leitura Spark na origem.

→ Documentação completa: [`pyodbc-destino-ihmtzbdbi.md`](pyodbc-destino-ihmtzbdbi.md)

| Artefacto | Papel |
|-----------|-------|
| `src/utils/pyodbc_sqlserver.py` | API reutilizável (connection string, DELETE, INSERT) |
| `SQLCAPACITY_DEST_USE_PYODBC=true` | Default — destino via ODBC |
| Job 08 | Piloto validado (100 linhas DELETE + INSERT, exit 0) |

As camadas JVM abaixo permanecem como **contexto histórico** e para leituras JDBC distribuídas; **não** substituem pyodbc no destino IHMTZBDBI.

## Workarounds JVM tentados (insuficientes para IHMTZBDBI)

### Camada 1 — **Não** usar `java.security.properties` no startup do spark-submit

No OpenJDK 11 RHEL, `-Djava.security.properties==/path` **no arranque da JVM** quebra `MessageDigest SHA-1` → Spark não inicia (`InternalError: SHA-1 not available`).

| Onde | Como |
|------|------|
| `spark-submit` | Apenas flags simples (TLS protocols, checkRevocation) — **sem** `java.security.properties` |
| Após `SparkSession` | `Security.setProperty()` via `apply_jvm_ssl_relaxation(spark)` |
| Destino IHMTZBDBI | `SslTrustAllInstaller.installGlobally()` via `icatu-spark-ssl-helper.jar` |

Arquivo `config/java.security.ssl-relaxed` permanece como **referência documental**; propriedades com espaços **não** vão na linha de comando.

### Camada 2 — Runtime `Security.setProperty` (driver)

Chamado em `spark_manager.py` após `getOrCreate()` — seguro porque a JVM já iniciou.

### Camada 3 — TrustAll para destino IHMTZBDBI (Job 08)

Quando merge + `Security.setProperty` ainda falham (servidor com **ForceEncryption**):

- JAR: `jvm-lib/icatu-spark-ssl-helper.jar` (`SslTrustAllInstaller.installGlobally()`)
- Activo por default para hosts: `IHMTZBDBI`, `IHMTZBDBI.DRMTZ.COM.BR`
- Desligar: `export SQLCAPACITY_SSL_TRUST_ALL=false`
- Outros hosts: `export SQLCAPACITY_SSL_TRUST_ALL_HOSTS=HOST1,HOST2`

Arquivo de merge (prioridade):

| Prioridade | Path |
|------------|------|
| 1 | `config/java.security.ssl-relaxed` (repo — **inclui jdk.jar**) |
| 2 | `/DATALAKE/opt/spark/conf/dynatrace-sqlserver-java.security` (cluster — pode faltar jdk.jar) |

### Camada 2 — Runtime na JVM do driver

`Security.setProperty()` após `SparkSession.getOrCreate()` — garante política mesmo se `--driver-java-options` não propagar:

- Módulo: `src/utils/java_ssl_config.py` → `apply_jvm_ssl_relaxation(spark)`
- Chamado em: `src/management/spark_manager.py`

> JDBC **write** e **DELETE via JVM** (`DriverManager.getConnection`) correm no **driver** em `deployMode=client`. Executors precisam das mesmas flags para leituras JDBC distribuídas.

### Camada 3 — Fallback applicativo (destino)

Se SSL persistir após camadas 1–2, retentar com `encrypt=false` (padrão jobs 01–07):

- Job 08: DELETE e INSERT no **destino** com retry automático
- Origem mantém `encrypt=true` quando o certificado origem é válido

Desactivar workaround global: `export SPARK_JAVA_SSL_RELAXED=false`

## Onde configurar no SQL Capacity PRD

| Artefacto | Papel |
|-----------|-------|
| `scripts/PRD/run_prd__08_*.sh` | `--driver-java-options`, `SPARK_DRIVER_JAVA_OPTS`, `spark.executor.extraJavaOptions` |
| `src/management/spark_manager.py` | `spark.driver/extraJavaOptions` + `apply_jvm_ssl_relaxation` |
| `src/utils/java_ssl_config.py` | Fonte única das propriedades SSL |
| `config/java.security.ssl-relaxed` | Override merge (inclui **jdk.jar.disabledAlgorithms**) |

Override por ambiente:

```bash
export SPARK_JAVA_SECURITY_FILE=/caminho/custom.security
export SPARK_JAVA_SSL_OPTS="-Djdk.certpath.disabledAlgorithms=MD2, MD5 ..."
export SPARK_JAVA_SSL_RELAXED=false   # desliga workaround
```

## Diagnóstico rápido

```bash
# Confirmar Java do Spark
/DATALAKE/opt/spark/bin/spark-submit --version 2>&1 | head -5

# Verificar se -D directo funciona (system property visível)
java -Djdk.jar.disabledAlgorithms="MD2, MD5, RSA keySize < 1024, DSA keySize < 1024" \
  -XshowSettings:properties -version 2>&1 | grep jdk.jar.disabledAlgorithms

# Teste sqlcmd no host destino (se sqlcmd falhar → problema no servidor SQL)
sqlcmd -S <HOST_DESTINO> -U <user> -P '<senha>' -Q "SELECT @@SERVERNAME"
```

| Resultado | Interpretação |
|-----------|---------------|
| Origem OK, destino falha SHA1 | Certificado **destino** legado + Java 11 — aplicar as **duas** propriedades |
| sqlcmd também falha | Corrigir certificado no **SQL Server** (solução definitiva) |
| Só Spark falha | Ajustar JVM (este documento) |

## Solução definitiva (recomendada)

Renovar certificado SSL no **SQL Server destino** com assinatura **SHA256** (ou superior).  
Workarounds no cliente são **temporários** e reduzem restrições de algoritmo — documentar data de revisão.

## Checklist ao portar jobs 01–07 para YARN

1. **Destino IHMTZBDBI:** replicar padrão **pyodbc** — [`pyodbc-destino-ihmtzbdbi.md`](pyodbc-destino-ihmtzbdbi.md).
2. Replicar bloco YARN/SSL do script Job 08 (`JAVA_SSL_SPARK_ARGS` + javaagent premain).
3. Confirmar `SparkManager` partilhado (já inclui `java_ssl_config`).
4. Testar **origem** (JDBC Spark) e **destino** (pyodbc) separadamente.
5. **Não** reiniciar YARN/History Server entre tentativas — cada `spark-submit` = JVM nova.

## Anti-padrões

| Evitar | Motivo |
|--------|--------|
| Só `-Djdk.certpath.disabledAlgorithms=` vazio | Não remove SHA1 no OpenJDK 11 |
| `-Djava.security.properties==/path` no **startup** spark-submit | Quebra `SHA-1` — `InternalError: SHA-1 not available` |
| `-Djdk.jar.disabledAlgorithms=...` **inline** no bash/spark-submit | Quebra JVM: `ClassNotFoundException: MD5` |
| Só `trustServerCertificate=true` | Não bypassa algorithm constraints |
| Reiniciar serviços Spark/YARN para “aplicar” SSL | JVM do job é efémera — corrigir flags e reexecutar |
| `encrypt=false` permanente sem alinhamento segurança | Usar só como fallback; preferir certificado no servidor |

## Referências cruzadas

- **Solução pyodbc destino:** [`pyodbc-destino-ihmtzbdbi.md`](pyodbc-destino-ihmtzbdbi.md)
- KB SQL Capacity (domínio): `.claude/kb/sql-capacity-prd/patterns/ssl-java-configuration.md`
- Guia rápido repo: `docs/ssl-troubleshooting-quick-guide.md`
- Código: `src/utils/pyodbc_sqlserver.py`
- Agente migração: `@.claude/agents/data-engineering/spark-cluster-migration-expert.md`
