# 🔧 TrustManager Customizado para SSL - Solução Avançada

> **Última atualização:** Janeiro/2026  
> **Quando usar:** Quando todas as outras soluções falharam e o servidor força criptografia

## Visão Geral

Para casos extremos onde:
- ✅ SSMS funciona normalmente
- ❌ Spark/Java falha mesmo com todas as configurações relaxadas
- ❌ Servidor está forçando criptografia (`ForceEncryption=1`)
- ❌ Certificado não está em conformidade com restrições do Java

**Solução:** Criar um TrustManager customizado que aceita todos os certificados.

---

## ⚠️ Aviso de Segurança

Esta solução **desabilita completamente a validação de certificados SSL**, tornando a conexão vulnerável a ataques man-in-the-middle. 

**Use apenas:**
- ✅ Em ambientes internos/isolados
- ✅ Quando não há alternativa
- ✅ Como solução temporária até corrigir o certificado no servidor

**NÃO use:**
- ❌ Em ambientes públicos
- ❌ Com dados sensíveis sem criptografia adicional
- ❌ Como solução permanente

---

## 🛠️ Implementação: TrustManager Customizado

### Passo 1: Criar Classe Java TrustManager

Crie o arquivo `src/utils/TrustAllManager.java`:

```java
package src.utils;

import javax.net.ssl.X509TrustManager;
import java.security.cert.X509Certificate;

/**
 * TrustManager que aceita todos os certificados SSL.
 * ⚠️ ATENÇÃO: Desabilita validação de certificados - use apenas quando necessário!
 */
public class TrustAllManager implements X509TrustManager {
    
    @Override
    public void checkClientTrusted(X509Certificate[] chain, String authType) {
        // Aceita todos os certificados do cliente
    }
    
    @Override
    public void checkServerTrusted(X509Certificate[] chain, String authType) {
        // Aceita todos os certificados do servidor
    }
    
    @Override
    public X509Certificate[] getAcceptedIssuers() {
        return new X509Certificate[0];
    }
}
```

### Passo 2: Compilar a Classe Java

```bash
# No servidor onde Spark roda
cd "$REPO_ROOT"   # raiz do clone; defina REPO_ROOT ou use o diretório do projeto

# Compilar (ajuste JAVA_HOME se necessário)
$JAVA_HOME/bin/javac -d .venv/lib/python3.x/site-packages/pyspark/jars/ \
    src/utils/TrustAllManager.java

# OU compilar para JAR
$JAVA_HOME/bin/javac src/utils/TrustAllManager.java
$JAVA_HOME/bin/jar cf trust-all-manager.jar src/utils/TrustAllManager.class
```

### Passo 3: Configurar Spark para Usar TrustManager Customizado

**Opção A: Via propriedades Java (mais simples)**

Adicione ao `SparkManager`:

```python
.config("spark.driver.extraJavaOptions", 
        "--add-opens java.base/java.nio=ALL-UNNAMED "
        "-Doracle.net.ns.level=FINE "
        "-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3 "
        "-Djdk.certpath.disabledAlgorithms= "
        "-Dcom.sun.net.ssl.checkRevocation=false "
        "-Djdk.tls.legacyAlgorithms= "
        "-Djavax.net.ssl.trustStore=NONE "
        "-Djavax.net.ssl.keyStore=NONE "
        "-Dtrust_all_cert=true")
```

**Opção B: Via código Python (mais complexo, mas mais controle)**

Criar um módulo Python que configura o SSL context antes de criar o SparkSession.

---

## 🎯 Solução Alternativa: Usar Driver JDBC com Validação Desabilitada

O driver JDBC do SQL Server tem uma propriedade que pode ajudar:

### Modificar URL JDBC

```python
# Mesmo com encrypt=false, adicionar trustServerCertificate=true
jdbc_url = (
    f"jdbc:sqlserver://{host}:{port};"
    f"databaseName={database};"
    f"encrypt=false;"
    f"trustServerCertificate=true;"
    f"hostNameInCertificate=*"  # Aceita qualquer hostname
)
```

**Nota:** Isso já foi implementado no código atual.

---

## 📋 Checklist de Implementação

- [ ] Tentou todas as soluções anteriores (relaxar restrições Java)
- [ ] Confirmou que SSMS funciona (problema está no Java)
- [ ] Verificou que servidor força criptografia (`ForceEncryption=1`)
- [ ] Decidiu usar TrustManager customizado (última opção)
- [ ] Compilou classe Java TrustManager
- [ ] Configurou Spark para usar TrustManager
- [ ] Testou conexão
- [ ] Documentou uso temporário até correção do certificado

---

## 🔄 Reverter Quando Certificado For Corrigido

Quando o certificado do servidor for corrigido:

1. Remover TrustManager customizado
2. Restaurar configurações Java padrão
3. Testar conexão com validação normal
4. Atualizar documentação

---

*Documentação criada em Janeiro/2026*

