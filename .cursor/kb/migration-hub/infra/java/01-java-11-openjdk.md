# Java 11 (OpenJDK)

## Resumo bem pequeno do passo
Instalar Java 11 (OpenJDK) e validar. Obrigatório para Hadoop/Spark.

## Passo (código)

```bash
# Instalar (RHEL 9)
sudo dnf install -y java-11-openjdk java-11-openjdk-devel

# Validar
java -version
javac -version

# Descobrir JAVA_HOME (se precisar)
readlink -f "$(which java)" | sed 's|/bin/java$||'
```

## JDBC / SQL Server — restrições SSL (migração)

OpenJDK 11 rejeita certificados com assinatura **SHA1withRSA** por **duas** propriedades independentes:

| Propriedade | Papel |
|-------------|-------|
| `jdk.certpath.disabledAlgorithms` | Path PKIX — default bloqueia SHA1 em certpath |
| **`jdk.jar.disabledAlgorithms`** | **Handshake TLS** — default inclui **SHA1** |

Pipelines migrados de Java 8 (Standalone) para YARN + Java 11 podem ver leitura JDBC OK na origem e falha no destino.

**Documentação completa (migration-hub):** [`../../migration/patterns/java11-sqlserver-ssl-dual-cause.md`](../../migration/patterns/java11-sqlserver-ssl-dual-cause.md)

**Solução validada destino IHMTZBDBI (SQL Capacity):** [`../../migration/patterns/pyodbc-destino-ihmtzbdbi.md`](../../migration/patterns/pyodbc-destino-ihmtzbdbi.md)

**Arquivo cluster (merge):** `/DATALAKE/opt/spark/conf/dynatrace-sqlserver-java.security`
