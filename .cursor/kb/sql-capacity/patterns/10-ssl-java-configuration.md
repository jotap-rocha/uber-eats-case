# ☕ Configuração Java para SSL - Resolução de Problemas

> **Última atualização:** Janeiro/2026  
> **Arquivo relacionado:** `09-certificados-ssl.md`

## Visão Geral

O erro "Certificates do not conform to algorithm constraints" pode ter **duas causas principais**:

1. **Problema no Servidor SQL Server** (menos comum)
   - Certificado do servidor usa algoritmos incompatíveis
   - Requer correção no servidor SQL Server

2. **Problema no Ambiente Java** (mais comum quando SSMS funciona)
   - **Java tem restrições mais rígidas que SSMS**
   - SSMS pode aceitar certificados que Java rejeita
   - Restrições de algoritmo do Java são mais estritas
   - Pode ser ajustado no lado do cliente

### ⚠️ Importante: Diferença entre SSMS e Java

**Por que SSMS funciona mas Java não?**

- **SSMS (SQL Server Management Studio):** Usa bibliotecas SSL do Windows, que são mais permissivas
- **Java/Spark:** Usa bibliotecas SSL do Java, que têm restrições mais rígidas de algoritmo
- **Resultado:** Um certificado pode ser aceito pelo SSMS mas rejeitado pelo Java

**Solução:** Relaxar restrições do Java (já implementado no projeto)

---

## 🔍 Diagnóstico: Onde Está o Problema?

### Teste 1: Verificar se Outros Clientes Conectam

```bash
# Testar com sqlcmd (se disponível no servidor cliente)
sqlcmd -S EXEMPLO-SQL-INTEGRACAO.EXEMPLO.CORP -U usr_sql_capacity -P <senha> -Q "SELECT @@SERVERNAME"

# Se sqlcmd funcionar mas Spark não:
# → Problema está no ambiente Java/Spark
# Se sqlcmd também falhar:
# → Problema está no servidor SQL Server
```

### Teste 2: Verificar Configurações Java Atuais

O projeto já configura algumas propriedades Java para SSL. Verifique se estão sendo aplicadas:

```python
# Verificar configurações atuais do Spark
# As configurações estão em src/management/spark_manager.py:
# -Djdk.tls.client.protocols=TLSv1.2,TLSv1.3
# -Djdk.certpath.disabledAlgorithms=MD2,MD5,RC4,DES
# -Dcom.sun.net.ssl.checkRevocation=false
```

### Teste 3: Verificar Versão do Java

```bash
# No servidor onde o Spark roda
java -version

# Verificar se é Java 8, 11, 17, etc.
# Versões mais novas têm restrições mais rígidas
```

---

## 🎯 Onde Resolver o Problema?

### Cenário 1: Problema no Servidor SQL Server (Mais Comum)

**Sintomas:**
- Erro ocorre mesmo com `encrypt=false`
- Outros clientes também têm problemas
- Erro menciona "algorithm constraints" ou "certificate"

**Onde resolver:** **No servidor SQL Server** (lado servidor)

**Ações:**
1. Verificar certificado no servidor SQL Server
2. Atualizar certificado para algoritmos compatíveis
3. Verificar se `ForceEncryption=1` está habilitado
4. Configurar certificado válido no SQL Server Configuration Manager

**Consulte:** `.cursor/kb/sql-capacity/09-certificados-ssl.md` (seção "Solução Definitiva")

---

### Cenário 2: Problema no Ambiente Java (Menos Comum)

**Sintomas:**
- Outros clientes conectam normalmente
- Apenas Spark/PySpark tem problema
- Erro específico de "algorithm constraints" do Java

**Onde resolver:** **No ambiente Java do cliente** (onde Spark roda)

**Ações:**
1. Ajustar restrições de algoritmo do Java
2. Adicionar certificados ao truststore Java
3. Configurar propriedades Java adicionais

---

## 🛠️ Solução: Ajustar Configurações Java (Lado Cliente)

### ✅ Solução Implementada no Projeto

O projeto **já implementa** configurações Java relaxadas para contornar problemas de algoritmo:

**Arquivo:** `src/management/spark_manager.py`

**Configurações aplicadas:**
```python
.config("spark.driver.extraJavaOptions", 
        "--add-opens java.base/java.nio=ALL-UNNAMED "
        "-Doracle.net.ns.level=FINE "
        "-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3 "
        "-Djdk.certpath.disabledAlgorithms=MD2,MD5 "  # Removido RC4,DES
        "-Dcom.sun.net.ssl.checkRevocation=false "
        "-Djdk.tls.legacyAlgorithms= ")  # Permite algoritmos legados
```

**O que foi feito:**
1. ✅ Removido `RC4,DES` das restrições (mantendo apenas `MD2,MD5`)
2. ✅ Adicionado `-Djdk.tls.legacyAlgorithms= ` (permite algoritmos legados)
3. ✅ Mantido `-Dcom.sun.net.ssl.checkRevocation=false` (desabilita verificação de revogação)

**Impacto na segurança:**
- ⚠️ Leve redução de segurança (permite algoritmos mais antigos)
- ✅ Ainda bloqueia algoritmos realmente inseguros (MD2, MD5)
- ✅ Mantém TLS 1.2 e 1.3 (protocolos seguros)

### Opção 1: Relaxar Restrições de Algoritmo (Já Implementado)

⚠️ **ATENÇÃO:** As configurações já estão relaxadas no projeto. Se ainda houver problemas, pode ser necessário relaxar ainda mais (não recomendado).

#### Configurações Atuais (já aplicadas)

```python
# src/management/spark_manager.py
.config("spark.driver.extraJavaOptions", 
        "--add-opens java.base/java.nio=ALL-UNNAMED "
        "-Doracle.net.ns.level=FINE "
        "-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3 "
        "-Djdk.certpath.disabledAlgorithms=MD2,MD5 "  # Apenas MD2 e MD5 bloqueados
        "-Dcom.sun.net.ssl.checkRevocation=false "
        "-Djdk.tls.legacyAlgorithms= ")  # Permite algoritmos legados
```

#### Criar Arquivo java.security.custom

Crie um arquivo com configurações customizadas:

```properties
# java.security.custom
# Permite algoritmos adicionais (use com cuidado!)

# Desabilita verificação de tamanho mínimo de chave RSA
jdk.certpath.disabledAlgorithms=MD2,MD5

# Permite algoritmos legados (NÃO recomendado para produção)
jdk.tls.legacyAlgorithms=
```

**⚠️ Importante:** Esta solução reduz segurança. Use apenas temporariamente.

---

### Opção 2: Adicionar Certificado ao Truststore Java

Se o problema for certificado raiz/intermediário ausente:

#### 1. Exportar Certificado do Servidor

```bash
# No servidor SQL Server ou via navegador
# Conectar em https://EXEMPLO-SQL-INTEGRACAO.EXEMPLO.CORP:1433
# Exportar certificado do navegador
```

#### 2. Importar no Truststore Java

```bash
# No servidor onde Spark roda
# Localizar JAVA_HOME
echo $JAVA_HOME

# Importar certificado
keytool -import -alias sqlserver-exemplo-integracao \
    -file /caminho/certificado.cer \
    -keystore $JAVA_HOME/lib/security/cacerts \
    -storepass changeit  # Senha padrão (pode precisar alterar)

# OU criar truststore customizado
keytool -import -alias sqlserver-exemplo-integracao \
    -file /caminho/certificado.cer \
    -keystore /caminho/custom-truststore.jks \
    -storepass senha_customizada
```

#### 3. Configurar Spark para Usar Truststore Customizado

```python
.config("spark.driver.extraJavaOptions", 
        "--add-opens java.base/java.nio=ALL-UNNAMED "
        "-Doracle.net.ns.level=FINE "
        "-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3 "
        "-Djavax.net.ssl.trustStore=/caminho/custom-truststore.jks "
        "-Djavax.net.ssl.trustStorePassword=senha_customizada")
```

---

### Opção 3: Desabilitar Validação de Certificado (NÃO RECOMENDADO)

⚠️ **ATENÇÃO CRÍTICA:** Esta solução desabilita completamente a validação de certificados, tornando a conexão vulnerável a ataques man-in-the-middle. **NÃO use em produção!**

```python
.config("spark.driver.extraJavaOptions", 
        "--add-opens java.base/java.nio=ALL-UNNAMED "
        "-Doracle.net.ns.level=FINE "
        "-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3 "
        "-Djavax.net.ssl.trustStore=NONE "  # Desabilita validação
        "-Dcom.sun.net.ssl.checkRevocation=false "
        "-Dtrust_all_cert=true")  # Se suportado pelo driver
```

**NÃO RECOMENDADO** - Use apenas para testes em ambiente isolado.

---

## 📊 Comparação: Servidor vs Cliente

| Aspecto | Problema no Servidor | Problema no Cliente Java |
|---------|---------------------|--------------------------|
| **Onde resolver** | Servidor SQL Server | Ambiente Java do Spark |
| **Sintoma principal** | Erro mesmo com `encrypt=false` | Apenas Spark falha, outros clientes OK |
| **Solução ideal** | Corrigir certificado no servidor | Ajustar configurações Java |
| **Impacto segurança** | Nenhum (corrige problema) | Pode reduzir segurança (workaround) |
| **Permanência** | Solução definitiva | Solução temporária |

---

## 🔧 Implementação: Ajustar SparkManager para Problemas SSL

Se você identificar que o problema está no lado do Java, pode criar uma versão do SparkManager com configurações relaxadas:

### Exemplo: SparkManager com SSL Relaxado

```python
# Adicionar método alternativo no SparkManager
def generate_spark_session_ssl_relaxed(self) -> SparkSession:
    """
    Cria SparkSession com configurações SSL relaxadas.
    Use apenas para servidores com problemas de certificado conhecidos.
    """
    if self._spark is None:
        self._spark = (SparkSession.builder
                     .appName(self.app_name)
                     .master(self.mode)
                     .config("spark.driver.memory", self.driver_memory)
                     .config("spark.executor.memory", self.executor_memory)
                     .config("spark.executor.cores", str(self.executor_cores))
                     .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
                     .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
                     .config("spark.driver.extraJavaOptions", 
                             "--add-opens java.base/java.nio=ALL-UNNAMED "
                             "-Doracle.net.ns.level=FINE "
                             "-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3 "
                             "-Djdk.certpath.disabledAlgorithms=MD2,MD5 "  # Removido RC4,DES
                             "-Dcom.sun.net.ssl.checkRevocation=false "
                             "-Djdk.tls.legacyAlgorithms= ")  # Permite algoritmos legados
                     .config("spark.executor.extraJavaOptions", 
                             "--add-opens java.base/java.nio=ALL-UNNAMED "
                             "-Doracle.net.ns.level=FINE "
                             "-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3 "
                             "-Djdk.certpath.disabledAlgorithms=MD2,MD5 "
                             "-Dcom.sun.net.ssl.checkRevocation=false "
                             "-Djdk.tls.legacyAlgorithms= ")
                     .getOrCreate())
        
        self._spark.sparkContext.setLogLevel(self.log_level)
        self._configure_hadoop()
    
    return self._spark
```

---

## 🎯 Recomendação Final

### Para o Caso Específico: EXEMPLO-SQL-INTEGRACAO

**Diagnóstico recomendado:**

1. **Teste com sqlcmd:**
   ```bash
   sqlcmd -S EXEMPLO-SQL-INTEGRACAO.EXEMPLO.CORP -U usr_sql_capacity -P <senha> -Q "SELECT @@SERVERNAME"
   ```

2. **Se sqlcmd também falhar:**
   - ✅ Problema está no **servidor SQL Server**
   - ✅ Resolver no servidor (corrigir certificado)
   - ✅ Consulte: `.cursor/kb/sql-capacity/09-certificados-ssl.md`

3. **Se sqlcmd funcionar mas Spark não:**
   - ✅ Problema pode estar no **ambiente Java**
   - ✅ Tentar ajustar configurações Java (Opção 1 ou 2 acima)
   - ✅ Mas ainda assim, o ideal é corrigir o certificado no servidor

### Prioridade de Solução

1. **PRIMEIRO:** Tentar resolver no servidor SQL Server (solução definitiva)
2. **SEGUNDO:** Se não for possível corrigir servidor imediatamente, usar workaround Java (temporário)
3. **TERCEIRO:** Documentar problema e monitorar até correção definitiva

---

## 📝 Checklist de Diagnóstico

- [ ] Testei com `sqlcmd` ou outro cliente SQL
- [ ] Verifiquei versão do Java (`java -version`)
- [ ] Verifiquei configurações Java atuais no SparkManager
- [ ] Testei com `encrypt=false` (já implementado)
- [ ] Verifiquei se certificado do servidor está expirado
- [ ] Verifiquei se `ForceEncryption=1` no servidor
- [ ] Documentei qual é o problema (servidor vs cliente)

---

## Referências

- [Java Security Properties](https://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html)
- [JDK TLS Configuration](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html)
- [SQL Server SSL Configuration](https://docs.microsoft.com/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine)

---

*Documentação criada em Janeiro/2026*

