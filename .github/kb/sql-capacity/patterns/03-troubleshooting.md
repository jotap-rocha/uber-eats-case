# 🔧 Troubleshooting — Pipeline SQL

## Diagnóstico Rápido

### Verificar Status de Execução

```bash
# Ver resumo do dia
grep "RESUMO\|Falhas:" logs/<job_name>/$(date +%Y-%m-%d).txt

# Contar sucessos e falhas
grep -c "✅" logs/<job_name>/$(date +%Y-%m-%d).txt  # Sucessos
grep -c "❌" logs/<job_name>/$(date +%Y-%m-%d).txt  # Falhas

# Listar servidores que falharam
grep "❌\|ERROR" logs/<job_name>/$(date +%Y-%m-%d).txt
```

---

## Erros Comuns e Soluções

### 1. "Falha na leitura" - Objeto SQL Ausente

**Sintoma:**
```
ERROR - ❌ [X/Y] SERVIDOR.DOMINIO\MSSQLSERVER/msdb: Falha na leitura
```

**Causa:** View ou function não existe no servidor fonte.

**Diagnóstico:**
1. Verificar se o servidor está acessível
2. Verificar se os objetos SQL existem no servidor

**Solução:**
1. Conectar no servidor SQL via SSMS
2. Executar o script apropriado de `src/queries/`:

| Job | Script |
|-----|--------|
| 01 | `11- create_vw_fn_sql_info.sql` |
| 02 | `08 - create_vw_fn_disk_space_info.sql` |
| 04 | `10 - create_vw_fn_size_rows_log.sql` |

3. Reexecutar o job para o servidor específico:
```bash
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR\MSSQLSERVER"
```

---

### 2. "Falha na leitura" - Firewall

**Sintoma:**
```
ERROR - ❌ [X/Y] SERVIDOR.DOMINIO\MSSQLSERVER/msdb: Falha na leitura
```
Com timeout ou connection refused.

**Causa:** Porta 1433 bloqueada entre cluster Spark e SQL Server.

**Diagnóstico:**
```bash
# Testar conectividade
telnet SERVIDOR.DOMINIO 1433

# Ou usar nc
nc -zv SERVIDOR.DOMINIO 1433
```

**Solução:**
1. Solicitar liberação de firewall para equipe de infraestrutura
2. Liberar porta 1433 do cluster Spark para o SQL Server
3. Testar conectividade novamente
4. Reexecutar o job

---

### 3. "Connection refused"

**Sintoma:**
```
Connection refused (Connection refused)
```

**Causa:** Serviço SQL Server não está rodando ou servidor offline.

**Solução:**
1. Verificar status do servidor
2. Verificar se o serviço SQL Server está ativo
3. Reiniciar serviço se necessário
4. Verificar se a instância está correta

---

### 4. "Login failed"

**Sintoma:**
```
Login failed for user 'usr_sql_capacity'
```

**Causa:** Usuário não existe ou credenciais incorretas.

**Solução:**
1. Criar usuário `usr_sql_capacity` no servidor fonte
2. Conceder permissões de leitura nas views/funções
3. Verificar credenciais no OCI Vault
4. Reexecutar o job

---

### 5. "Read timed out"

**Sintoma:**
```
Read timed out
```

**Causa:** Query demora muito para retornar.

**Solução:**
1. Verificar performance do servidor fonte
2. Verificar se há locks ou bloqueios
3. Usar fallback manual (INSERT direto)
4. Considerar aumentar timeout

---

### 6. Domínio Incorreto

**Sintoma:**
Servidor não encontrado mesmo existindo.

**Causa:** Domínio errado na conexão.

**Solução:**
Verificar domínios especiais:

| Padrão de host (exemplo) | Domínio / regra |
|---------------------------|-----------------|
| `EXEMPLO-SRV-GRP-A*` | `.EXEMPLO-ALT.CORP` |
| `EXEMPLO-SRV-SLA-01` | (sem domínio — conforme política local) |
| `EXEMPLO-SRV-GRP-B*` | `.EXEMPLO-OUTRO.CORP` |
| Demais | `.EXEMPLO.CORP` |

---

### 7. Erro de Certificado SSL/TLS

**Sintoma:**
```
javax.net.ssl.SSLHandshakeException: PKIX path building failed
javax.net.ssl.SSLException: Certificate doesn't match
Connection reset by peer
```

**Causa:** Problemas com certificados SSL/TLS no servidor SQL Server. Alguns servidores têm certificados expirados, inválidos ou não confiáveis.

**Servidores com problema de certificado (exemplo — liste os reais no runbook interno):**

| Servidor (exemplo) | Observação |
|--------------------|------------|
| `EXEMPLO-SRV-PRD-01` | Erro de certificado SSL |
| `EXEMPLO-SRV-INTEGRACAO` | Erro de certificado SSL |
| `EXEMPLO-SRV-SLA-01` | Erro de certificado SSL |
| `EXEMPLO-SRV-SLA-02` | Erro de certificado SSL |

**Solução Temporária:**
O código já implementa fallback automático que desabilita `encrypt` quando há problemas SSL. Se o problema persistir:

1. **Verificar se o fallback automático está funcionando:**
   - O sistema tenta primeiro com `encrypt=true`
   - Se falhar, tenta automaticamente com `encrypt=false`
   - Verifique os logs para confirmar qual modo está sendo usado

2. **Solução Definitiva (Recomendada):**
   - Solicitar à equipe de infraestrutura para corrigir o certificado SSL no servidor
   - Renovar ou instalar certificado válido no SQL Server
   - Verificar se o certificado está na cadeia de confiança

3. **Verificar Certificado no Servidor:**
   ```sql
   -- Executar no servidor SQL Server
   SELECT 
       name,
       certificate_id,
       pvt_key_encryption_type_desc,
       expiry_date
   FROM sys.certificates
   WHERE name LIKE '%SSL%' OR name LIKE '%TLS%'
   ```

4. **Teste de Conexão:**
   ```bash
   # Testar conexão com encrypt desabilitado (se necessário)
   # O código já faz isso automaticamente como fallback
   ```

**Nota:** O sistema já implementa fallback automático para conexões sem encrypt quando há problemas SSL. Se o problema persistir mesmo com o fallback, é necessário corrigir o certificado no servidor.

---

## Fluxo de Troubleshooting

```
1. Verificar log do dia
   ↓
2. Identificar servidores com erro
   ↓
3. Classificar tipo de erro
   ├── Objeto ausente → Executar script SQL
   ├── Firewall → Solicitar liberação
   ├── Timeout → Fallback manual ou ajustar timeout
   └── Login → Verificar usuário e permissões
   ↓
4. Aplicar solução
   ↓
5. Reexecutar job para servidores específicos
   ↓
6. Verificar sucesso no log
```

---

## Reexecução de Servidores Específicos

### Um Servidor

```bash
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR\MSSQLSERVER"
```

### Múltiplos Servidores

```bash
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR1\MSSQLSERVER" \
  --instancia "SERVIDOR2\MSSQLSERVER" \
  --instancia "SERVIDOR3\MSSQLSERVER"
```

### Com Sobrescrita de Log

```bash
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR\MSSQLSERVER" \
  --overwrite-log
```

---

## Fallback Manual

Se o job não conseguir ler do servidor, use INSERT manual:

1. Conectar no servidor fonte via SSMS
2. Executar query de fallback (ver `docs/job_table_mapping_and_fallback_inserts.md`)
3. Copiar os comandos INSERT gerados
4. Executar no banco de destino

---

## Verificação Pós-Correção

```bash
# Verificar se o servidor agora está OK
grep "SERVIDOR" logs/<job_name>/$(date +%Y-%m-%d).txt | tail -5

# Verificar resumo geral
grep "RESUMO" logs/<job_name>/$(date +%Y-%m-%d).txt | tail -1
```

---

## Contato para Suporte

1. Verifique os logs detalhados
2. Consulte a documentação em `docs/`
3. Verifique a Wiki do projeto
4. Entre em contato com a equipe de desenvolvimento

