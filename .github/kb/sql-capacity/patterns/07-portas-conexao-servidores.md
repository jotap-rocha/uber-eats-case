# Portas de Conexão - Servidores SQL Server PRD

> **Última atualização:** Janeiro/2026  
> **Arquivo de configuração:** `src/queries/queries_functions.py` → função `get_config_sources_query()`

## Visão Geral

A partir de Janeiro/2026, o projeto passou a usar **conexão direta por porta** ao invés de named instances. Isso elimina a dependência do SQL Browser Service e proporciona conexões mais rápidas e confiáveis.

### Estratégia de Conexão

| Método | Formato | Quando usar |
|--------|---------|-------------|
| **Named Instance** (antigo) | `servidor\instancia:1433` | Depende do SQL Browser |
| **Porta Direta** (novo) | `servidor:porta` | Conexão direta, sem SQL Browser |

## Mapeamento de portas — ambiente PRD (modelo)

> Substitua pelos **hosts e portas reais** da sua organização; mantenha a tabela atualizada junto de `CONTEXT.md` ou runbook interno.

### Instâncias nomeadas (exemplos)

| Servidor (exemplo) | Instância | Porta | Observação |
|--------------------|-----------|-------|------------|
| `EXEMPLO-SRV-CORP-01` | `INST_A` | **1539** | Instância nomeada |
| `EXEMPLO-SRV-CORP-01` | `INST_B` | **1536** | Instância nomeada |
| `EXEMPLO-SRV-APP-01` | `CM` | **54441** | Instância nomeada |
| `EXEMPLO-SRV-DW-01` | `DW01` | **1439** | Instância nomeada |

### Exceções — `MSSQLSERVER` com porta não padrão

| Servidor (exemplo) | Instância | Porta | Observação |
|--------------------|-----------|-------|------------|
| `EXEMPLO-SRV-LEGADO-01` | `MSSQLSERVER` | **1434** | Instância default com porta explícita |

### Instâncias default (`MSSQLSERVER`)

Quando não houver exceção no `CASE`, use normalmente a **porta 1433** (ajuste se o padrão local for outro).

## Código T-SQL do Mapeamento

O mapeamento é feito via `CASE WHEN` na função `get_config_sources_query()`:

```sql
CASE 
    -- Instâncias nomeadas com portas específicas (exemplos — alinhe ao seu inventário)
    WHEN RTRIM(LTRIM(INSTANCIA)) LIKE '%\INST_A' THEN 1539
    WHEN RTRIM(LTRIM(INSTANCIA)) LIKE '%\INST_B' THEN 1536
    WHEN RTRIM(LTRIM(INSTANCIA)) LIKE '%\CM' THEN 54441
    WHEN RTRIM(LTRIM(INSTANCIA)) LIKE '%\DW01' THEN 1439

    -- Exceção: host legado na porta 1434 mesmo com MSSQLSERVER
    WHEN RTRIM(LTRIM(INSTANCIA)) = 'EXEMPLO-SRV-LEGADO-01\MSSQLSERVER' THEN 1434

    ELSE 1433
END AS port
```

## URL JDBC Resultante

### Exemplo — instância nomeada

```
jdbc:sqlserver://EXEMPLO-SRV-CORP-01.EXEMPLO.CORP:1539;databaseName=msdb;encrypt=true;trustServerCertificate=true
```

### Exemplo — instância default

```
jdbc:sqlserver://EXEMPLO-SRV-PADRAO-01.EXEMPLO.CORP:1433;databaseName=msdb;encrypt=true;trustServerCertificate=true
```

### Exemplo — exceção de porta

```
jdbc:sqlserver://EXEMPLO-SRV-LEGADO-01.EXEMPLO.CORP:1434;databaseName=msdb;encrypt=true;trustServerCertificate=true
```

## Como Adicionar Nova Porta

1. Edite o arquivo `src/queries/queries_functions.py`
2. Localize a função `get_config_sources_query()`
3. Adicione uma nova linha no `CASE WHEN` antes do `ELSE`:

```sql
WHEN RTRIM(LTRIM(INSTANCIA)) LIKE '%\NOVA_INSTANCIA' THEN 1441
```

4. Atualize este documento de KB com a nova porta
5. Teste a conexão com o job 01:

```bash
bash scripts/PRD/run_prd__01_app_obter_info_sql_server__01.sh --instancia "SERVIDOR\NOVA_INSTANCIA"
```

## Domínios por servidor (modelo)

| Padrão de host (exemplo) | Domínio |
|--------------------------|---------|
| `EXEMPLO-SRV-GRP-IMP*` | `.EXEMPLO-ALT.CORP` |
| `EXEMPLO-SRV-EXT-01*` | `.EXEMPLO-ALT.CORP` |
| `EXEMPLO-SRV-PARCEIRO*` | `.EXEMPLO-OUTRO.CORP` |
| `EXEMPLO-SRV-SLA*` | Sem domínio |
| `EXEMPLO-SRV-IDENT*` | Sem domínio |
| Demais | `.EXEMPLO.CORP` |

## Troubleshooting

### Erro de conexão após mudança de porta

1. Verifique se a porta está correta no mapeamento
2. Confirme que a porta está liberada no firewall
3. Verifique se o SQL Server está escutando na porta correta:

```sql
-- Executar no SQL Server
SELECT local_tcp_port 
FROM sys.dm_exec_connections 
WHERE session_id = @@SPID
```

### Como descobrir a porta de uma instância

```sql
-- Via registro do Windows (executar no servidor)
EXEC xp_regread 
    @rootkey = 'HKEY_LOCAL_MACHINE',
    @key = 'SOFTWARE\Microsoft\Microsoft SQL Server\MSSQL15.INSTANCIA\MSSQLServer\SuperSocketNetLib\Tcp\IPAll',
    @value_name = 'TcpPort'
```

Ou via SQL Server Configuration Manager → SQL Server Network Configuration → Protocols → TCP/IP → IP Addresses → IPAll → TCP Port.

