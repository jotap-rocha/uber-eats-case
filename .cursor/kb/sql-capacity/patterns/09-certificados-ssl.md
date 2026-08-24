# 🔒 Certificados SSL/TLS - Problemas de Conexão

> **Última atualização:** Janeiro/2026  
> **Arquivo relacionado:** `03-troubleshooting.md`

## Visão Geral

Alguns servidores SQL Server apresentam problemas de certificados SSL/TLS que impedem conexões seguras. Este documento lista os servidores conhecidos com esse problema e as soluções disponíveis.

---

## Servidores com problemas de certificado SSL

Documente os **seus** hosts afetados (exemplo ilustrativo — substitua pelo inventário real):

| Servidor (exemplo) | Ambiente | Observação |
|--------------------|----------|------------|
| `EXEMPLO-SRV-PRD-01` | PRODUÇÃO | Erro de certificado SSL |
| `EXEMPLO-SRV-INTEGRACAO` | PRODUÇÃO | Erro de certificado SSL |
| `EXEMPLO-SRV-SLA-01` | SLA | Erro de certificado SSL |
| `EXEMPLO-SRV-SLA-02` | SLA | Erro de certificado SSL |

---

## Sintomas

### Erros Comuns

```
javax.net.ssl.SSLHandshakeException: PKIX path building failed
javax.net.ssl.SSLException: Certificate doesn't match
javax.net.ssl.SSLPeerUnverifiedException: Certificate for <host> doesn't match
Connection reset by peer
Error: Certificates do not conform to algorithm constraints
```

**⚠️ Erro Especial: "Certificates do not conform to algorithm constraints"**

Este erro ocorre mesmo com `encrypt=false` e indica que:
- O servidor SQL Server está **forçando criptografia** no lado do servidor
- O certificado não está em conformidade com as restrições de algoritmo do Java
- **Não pode ser resolvido apenas do lado do cliente** - requer correção no servidor

### No Log do Job

```
ERROR - ❌ [X/Y] SERVIDOR.DOMINIO\MSSQLSERVER/msdb: Falha na leitura
⚠️  SERVIDOR.DOMINIO/msdb: Usando conexão SEM encrypt (fallback para problemas SSL)
```

---

## Solução Automática (Fallback)

O sistema implementa **fallback automático** quando detecta problemas SSL:

1. **Primeira tentativa:** Conexão com `encrypt=true` (padrão seguro)
2. **Se falhar:** Tenta automaticamente com `encrypt=false` (fallback)
3. **Log:** Registra no log quando usa o fallback

**⚠️ Limitação:** Se o servidor estiver **forçando criptografia** no lado do servidor (configuração `ForceEncryption=1`), o fallback para `encrypt=false` não funcionará. Neste caso, é necessário corrigir o certificado no servidor.

### Como Funciona no Código

O código em `src/jobs/*/SQLServerPerServerReader._build_jdbc_url()`:

```python
def _build_jdbc_url(self, source: Dict[str, str], use_encrypt: bool = True) -> str:
    """
    Constrói URL JDBC para um servidor.
    
    Se use_encrypt=False, desabilita encrypt (fallback para problemas SSL)
    """
    if use_encrypt:
        return f"jdbc:sqlserver://{host}:{port};databaseName={database};encrypt=true;trustServerCertificate=true"
    else:
        # Fallback: desabilita encrypt se houver problemas de SSL
        return f"jdbc:sqlserver://{host}:{port};databaseName={database};encrypt=false"
```

O sistema tenta automaticamente com `encrypt=false` quando há falha SSL.

---

## Solução Definitiva (Recomendada)

### ⭐ Opção 1: Adicionar Certificado ao Truststore Java (Cliente)

**Quando usar:** Quando SSMS funciona mas Spark/Java não, indicando problema no lado do cliente Java.

**Vantagens:**
- ✅ Não requer alteração no servidor SQL Server
- ✅ Resolve imediatamente
- ✅ Pode ser aplicado para múltiplos servidores

**Passos:**
1. Exportar certificado do servidor SQL Server (via SSMS ou PowerShell)
2. Transferir para servidor cliente onde Spark roda
3. Importar no cacerts Java usando script:
   ```bash
   bash scripts/import_sql_certificate.sh /tmp/exemplo-srv.cer sqlserver-exemplo-srv EXEMPLO-SRV-INTEGRACAO
   ```

**Documentação completa:** `docs/ssl-add-certificate-to-java-truststore.md`

**Status:** ✅ Script criado e pronto para uso

---

### Opção 2: Corrigir Certificado no Servidor SQL Server

Para resolver definitivamente o problema, é necessário corrigir o certificado no servidor SQL Server. Este guia detalha os passos para diagnóstico e correção.

---

## 🔍 Diagnóstico Passo a Passo

### Passo 1: Verificar Certificado Atual no SQL Server

```sql
-- Executar no servidor SQL Server (via SSMS)
-- Lista todos os certificados disponíveis
SELECT 
    name,
    certificate_id,
    pvt_key_encryption_type_desc,
    expiry_date,
    start_date,
    DATEDIFF(day, GETDATE(), expiry_date) AS dias_para_expiracao
FROM sys.certificates
WHERE name LIKE '%SSL%' 
   OR name LIKE '%TLS%' 
   OR name LIKE '%Encryption%'
   OR name LIKE '%Server%'
ORDER BY expiry_date DESC
```

**O que verificar:**
- ✅ Certificado existe e não está expirado
- ✅ Algoritmo de criptografia é compatível (RSA, SHA-256)
- ⚠️ Se expirado ou ausente, precisa renovar/instalar

### Passo 2: Verificar Certificado de Criptografia de Conexão

```sql
-- Verificar certificado usado para criptografia de conexão
SELECT 
    name,
    certificate_id,
    expiry_date,
    start_date,
    pvt_key_encryption_type_desc
FROM sys.certificates
WHERE name = '##MS_SQLResourceSigningCertificate##'
   OR name LIKE '%Server%'
   OR name LIKE '%Encryption%'
```

### Passo 3: Verificar se o Servidor Está Forçando Criptografia

#### Via SQL (Registro do Windows)

```sql
-- Verificar configuração de criptografia forçada
EXEC xp_instance_regread 
    @rootkey = 'HKEY_LOCAL_MACHINE',
    @key = 'SOFTWARE\Microsoft\Microsoft SQL Server\MSSQLServer\SuperSocketNetLib',
    @value_name = 'ForceEncryption'

-- Verificar porta e configurações de rede
EXEC xp_instance_regread 
    @rootkey = 'HKEY_LOCAL_MACHINE',
    @key = 'SOFTWARE\Microsoft\Microsoft SQL Server\MSSQLServer\SuperSocketNetLib\Tcp\IPAll',
    @value_name = 'TcpPort'
```

**Interpretação:**
- `ForceEncryption = 1`: Servidor **força** criptografia (todas as conexões devem usar SSL)
- `ForceEncryption = 0`: Servidor **permite** conexões sem criptografia

#### Via PowerShell (Alternativa)

```powershell
# Executar no servidor SQL Server (como Administrador)
# Verificar ForceEncryption
$regPath = "HKLM:\SOFTWARE\Microsoft\Microsoft SQL Server\MSSQLServer\SuperSocketNetLib"
$forceEncryption = (Get-ItemProperty -Path $regPath -Name "ForceEncryption" -ErrorAction SilentlyContinue).ForceEncryption

if ($forceEncryption -eq 1) {
    Write-Host "⚠️ ForceEncryption está HABILITADO (1)" -ForegroundColor Yellow
    Write-Host "   O servidor está forçando criptografia para todas as conexões"
} else {
    Write-Host "✅ ForceEncryption está DESABILITADO (0)" -ForegroundColor Green
    Write-Host "   O servidor permite conexões sem criptografia"
}
```

#### Via SQL Server Configuration Manager (GUI)

1. Abrir **SQL Server Configuration Manager**
2. Expandir **SQL Server Network Configuration**
3. Selecionar **Protocols for [INSTANCE_NAME]**
4. Clicar com botão direito em **TCP/IP** → **Properties**
5. Aba **Flags**:
   - Verificar valor de **ForceEncryption**
   - Se `Yes`, o servidor está forçando criptografia

### Passo 4: Verificar Certificado Instalado no Windows

```powershell
# Executar no servidor SQL Server (como Administrador)
# Listar certificados no repositório LocalMachine\Personal
Get-ChildItem -Path Cert:\LocalMachine\My | 
    Where-Object { $_.Subject -like "*SQL*" -or $_.Subject -like "*Server*" } |
    Select-Object Subject, Thumbprint, NotAfter, SignatureAlgorithm |
    Format-Table -AutoSize

# Verificar certificado específico por thumbprint (se conhecido)
# Get-ChildItem -Path Cert:\LocalMachine\My | Where-Object Thumbprint -eq "THUMBPRINT_AQUI"
```

**O que verificar:**
- ✅ Certificado existe no repositório
- ✅ Não está expirado (`NotAfter`)
- ✅ Algoritmo de assinatura é compatível (`SignatureAlgorithm` - deve ser SHA256 ou superior)

---

## 🛠️ Soluções e Correções

### Solução 1: Instalar/Atualizar Certificado SSL

#### Opção A: Via SQL Server Configuration Manager (Recomendado)

1. **Obter Certificado:**
   - Solicitar à equipe de infraestrutura um certificado SSL válido
   - Certificado deve:
     - Estar no formato `.pfx` ou `.cer`
     - Ter a chave privada (se `.pfx`)
     - Usar algoritmos compatíveis (RSA, SHA-256)
     - Não estar expirado

2. **Instalar no Windows:**
   ```powershell
   # Importar certificado .pfx (com chave privada)
   $certPassword = ConvertTo-SecureString -String "SENHA_DO_CERTIFICADO" -Force -AsPlainText
   Import-PfxCertificate -FilePath "C:\caminho\certificado.pfx" -CertStoreLocation Cert:\LocalMachine\My -Password $certPassword
   ```

3. **Configurar no SQL Server:**
   - Abrir **SQL Server Configuration Manager**
   - Expandir **SQL Server Network Configuration**
   - Selecionar **Protocols for [INSTANCE_NAME]**
   - Clicar com botão direito em **TCP/IP** → **Properties**
   - Aba **Certificate**:
     - Selecionar o certificado instalado no dropdown
   - Aba **Flags**:
     - **ForceEncryption**: `Yes` (se quiser forçar) ou `No` (se quiser permitir sem)
   - **Reiniciar serviço SQL Server** para aplicar mudanças

#### Opção B: Via T-SQL (Avançado)

```sql
-- Criar certificado a partir de arquivo (requer permissões elevadas)
CREATE CERTIFICATE CertificadoSSL
FROM FILE = 'C:\caminho\certificado.cer'
WITH PRIVATE KEY (
    FILE = 'C:\caminho\chave_privada.key',
    DECRYPTION BY PASSWORD = 'SENHA_DA_CHAVE'
);
```

### Solução 2: Desabilitar ForceEncryption (Temporário - NÃO Recomendado para Produção)

⚠️ **ATENÇÃO:** Esta solução desabilita a criptografia obrigatória, reduzindo a segurança. Use apenas como solução temporária enquanto o certificado é corrigido.

#### Via SQL Server Configuration Manager

1. Abrir **SQL Server Configuration Manager**
2. Expandir **SQL Server Network Configuration**
3. Selecionar **Protocols for [INSTANCE_NAME]**
4. Clicar com botão direito em **TCP/IP** → **Properties**
5. Aba **Flags**:
   - **ForceEncryption**: `No`
6. **Reiniciar serviço SQL Server**

#### Via PowerShell (Alternativa)

```powershell
# Executar como Administrador
$regPath = "HKLM:\SOFTWARE\Microsoft\Microsoft SQL Server\MSSQLServer\SuperSocketNetLib"
Set-ItemProperty -Path $regPath -Name "ForceEncryption" -Value 0

# Reiniciar serviço SQL Server
Restart-Service -Name "MSSQLSERVER"  # Ajustar nome se instância nomeada
```

#### Via T-SQL (Registro)

```sql
-- Desabilitar ForceEncryption (requer permissões elevadas)
EXEC xp_instance_regwrite 
    @rootkey = 'HKEY_LOCAL_MACHINE',
    @key = 'SOFTWARE\Microsoft\Microsoft SQL Server\MSSQLServer\SuperSocketNetLib',
    @value_name = 'ForceEncryption',
    @type = 'REG_DWORD',
    @value = 0

-- Reiniciar serviço necessário após mudança
```

### Solução 3: Atualizar Certificado para Algoritmos Compatíveis

Se o certificado existe mas usa algoritmos antigos (MD5, SHA-1), é necessário renovar com algoritmos modernos:

**Algoritmos Compatíveis:**
- ✅ RSA com SHA-256 ou superior
- ✅ ECDSA com SHA-256 ou superior
- ❌ MD5 (obsoleto, não suportado)
- ❌ SHA-1 (obsoleto, pode não funcionar)

**Processo:**
1. Solicitar novo certificado à equipe de infraestrutura
2. Especificar que deve usar SHA-256 ou superior
3. Instalar e configurar conforme Solução 1

### Solução 4: Verificar e Corrigir Cadeia de Confiança

```powershell
# Verificar cadeia de certificados
$cert = Get-ChildItem -Path Cert:\LocalMachine\My | Where-Object Subject -like "*SQL*"
$chain = New-Object System.Security.Cryptography.X509Certificates.X509Chain
$chain.Build($cert)

if ($chain.ChainStatus.Count -eq 0) {
    Write-Host "✅ Cadeia de certificados válida" -ForegroundColor Green
} else {
    Write-Host "⚠️ Problemas na cadeia de certificados:" -ForegroundColor Yellow
    $chain.ChainStatus | ForEach-Object {
        Write-Host "   - $($_.Status): $($_.StatusInformation)" -ForegroundColor Yellow
    }
}
```

**Problemas comuns:**
- Certificado raiz não está no repositório de autoridades confiáveis
- Certificado intermediário ausente
- Certificado revogado

**Correção:**
- Instalar certificados intermediários e raiz no repositório `Cert:\LocalMachine\CA`

---

## 📋 Checklist de Resolução

Use este checklist para resolver problemas de SSL:

- [ ] **Diagnóstico:**
  - [ ] Verificou certificado no SQL Server (`sys.certificates`)
  - [ ] Verificou `ForceEncryption` no registro
  - [ ] Verificou certificado no Windows (`Cert:\LocalMachine\My`)
  - [ ] Verificou cadeia de confiança

- [ ] **Identificação do Problema:**
  - [ ] Certificado expirado
  - [ ] Certificado ausente
  - [ ] Algoritmo incompatível
  - [ ] `ForceEncryption=1` sem certificado válido
  - [ ] Cadeia de confiança quebrada

- [ ] **Ação Corretiva:**
  - [ ] Solicitou novo certificado à infraestrutura (se necessário)
  - [ ] Instalou certificado no Windows
  - [ ] Configurou certificado no SQL Server Configuration Manager
  - [ ] Reiniciou serviço SQL Server
  - [ ] Testou conexão após correção

- [ ] **Validação:**
  - [ ] Testou conexão com script `test_sql_connection.py`
  - [ ] Verificou logs do pipeline
  - [ ] Confirmou que erro SSL não ocorre mais

---

## 🔧 Comandos Úteis para Troubleshooting

### Verificar Status do Serviço SQL Server

```powershell
# Status do serviço
Get-Service -Name "MSSQLSERVER"  # Ajustar para instância nomeada se necessário

# Reiniciar serviço
Restart-Service -Name "MSSQLSERVER"
```

### Verificar Porta e Configurações de Rede

```sql
-- Verificar porta TCP/IP
EXEC xp_instance_regread 
    @rootkey = 'HKEY_LOCAL_MACHINE',
    @key = 'SOFTWARE\Microsoft\Microsoft SQL Server\MSSQLServer\SuperSocketNetLib\Tcp\IPAll',
    @value_name = 'TcpPort'

-- Verificar se SQL Server está escutando
SELECT 
    local_net_address,
    local_tcp_port,
    state_desc
FROM sys.dm_exec_connections
WHERE session_id = @@SPID
```

### Testar Conexão do Próprio Servidor

```sql
-- Testar conexão local (deve funcionar sempre)
SELECT @@SERVERNAME, GETDATE()
```

---

## 📞 Contato e Suporte

Se o problema persistir após seguir este guia:

1. **Documente o problema:**
   - Erro exato (copiar mensagem completa)
   - Resultado dos comandos de diagnóstico
   - Versão do SQL Server
   - Versão do Java usado no Spark

2. **Solicite suporte à infraestrutura:**
   - Informe que o servidor está forçando criptografia
   - Solicite correção do certificado SSL
   - Forneça evidências do problema

3. **Workaround temporário (se necessário):**
   - Use fallback manual (INSERT direto)
   - Documente que o servidor precisa de correção
   - Monitore quando a correção for aplicada

---

## Referências Adicionais

- [Microsoft Docs - Enable Encrypted Connections](https://docs.microsoft.com/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine)
- [Microsoft Docs - Certificate Requirements](https://docs.microsoft.com/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine#certificate-requirements)
- [SQL Server Configuration Manager](https://docs.microsoft.com/sql/tools/configuration-manager/sql-server-configuration-manager)

---

## Verificação de Conexão

### Testar Conexão Manual

```bash
# Testar conectividade básica
telnet SERVIDOR.DOMINIO 1433

# Testar com sqlcmd (se disponível)
sqlcmd -S SERVIDOR.DOMINIO -U usr_sql_capacity -P <senha> -Q "SELECT @@VERSION"
```

### Verificar no Log do Job

```bash
# Verificar se o servidor está usando fallback SSL
grep "SERVIDOR" logs/01_app_obter_info_sql_server/$(date +%Y-%m-%d).txt | grep -i "encrypt\|ssl"

# Verificar se há erros de certificado
grep -i "certificate\|ssl\|tls" logs/01_app_obter_info_sql_server/$(date +%Y-%m-%d).txt
```

---

## Impacto

### Segurança

⚠️ **Atenção:** Quando o fallback é usado (`encrypt=false`), a conexão **não é criptografada**. Isso significa:
- Dados trafegam em texto plano
- Vulnerável a interceptação
- Não recomendado para ambientes de produção críticos

### Performance

- Fallback sem encrypt pode ser ligeiramente mais rápido
- Mas a diferença é mínima e não compensa a perda de segurança

---

## Recomendações

1. **Prioridade Alta:** Corrigir certificados nos servidores listados
2. **Monitoramento:** Verificar logs regularmente para novos servidores com problema
3. **Documentação:** Atualizar esta lista quando novos servidores forem identificados
4. **Comunicação:** Informar equipe de infraestrutura sobre servidores com problemas

---

## Adicionar Novo Servidor à Lista

Se identificar um novo servidor com problema de certificado SSL:

1. Adicionar na tabela "Servidores com Problemas de Certificado SSL" acima
2. Documentar o erro específico encontrado
3. Informar equipe de infraestrutura
4. Monitorar se o problema persiste após correção

---

## Onde Resolver o Problema?

### ⚠️ Questão Importante: Servidor vs Cliente

O erro "Certificates do not conform to algorithm constraints" pode ter **duas causas**:

1. **Problema no Servidor SQL Server** (mais comum - 90% dos casos)
   - Certificado do servidor usa algoritmos incompatíveis
   - Servidor está forçando criptografia (`ForceEncryption=1`)
   - **Resolve no servidor SQL Server**

2. **Problema no Ambiente Java** (menos comum - 10% dos casos)
   - Restrições muito rígidas do Java
   - Certificados raiz ausentes no truststore
   - **Pode ser ajustado no lado do cliente**

### Como Diagnosticar

```bash
# Teste 1: Verificar se outros clientes conectam
sqlcmd -S SERVIDOR.DOMINIO -U usuario -P senha -Q "SELECT @@SERVERNAME"

# Se sqlcmd FUNCIONAR mas Spark NÃO:
# → Problema está no ambiente Java (lado cliente)
# → Consulte: 10-ssl-java-configuration.md

# Se sqlcmd TAMBÉM FALHAR:
# → Problema está no servidor SQL Server (lado servidor)
# → Resolver conforme este guia (09-certificados-ssl.md)
```

### Recomendação

**SEMPRE tente resolver no servidor primeiro** (solução definitiva e segura).  
Use ajustes no Java apenas como **workaround temporário** enquanto o servidor é corrigido.

**Consulte também:** [Configuração Java para SSL](10-ssl-java-configuration.md) - Guia completo sobre ajustes no lado do cliente

---

## Referências

- [Troubleshooting Guide](03-troubleshooting.md) - Guia completo de troubleshooting
- [Configuração Java para SSL](10-ssl-java-configuration.md) - **⭐ Guia sobre ajustes no lado do cliente Java**
- [Microsoft Docs - SQL Server Encryption](https://docs.microsoft.com/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine)
- [SQL Server Configuration Manager - Certificates](https://docs.microsoft.com/sql/relational-databases/security/encryption/enable-encrypted-connections-to-the-database-engine)

---

*Documentação criada em Janeiro/2026*

