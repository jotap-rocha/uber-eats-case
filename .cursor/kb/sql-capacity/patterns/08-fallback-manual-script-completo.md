# Fallback Manual T-SQL - Script Completo (Todos os 7 Jobs)

> **Última atualização:** Janeiro/2026  
> **Uso:** Quando o pipeline não consegue conectar no servidor e é necessário executar manualmente

## Visão Geral

Este script executa todos os 7 jobs de uma vez só, gerando os comandos `INSERT INTO` prontos para copiar e colar no banco de destino.

### Quando usar?

- Servidor com problema de conectividade (firewall, porta bloqueada)
- Servidor fora do domínio padrão
- Necessidade de coleta urgente sem esperar correção de infraestrutura

### Destino dos dados

- **Servidor:** `sql-destino.EXEMPLO.CORP`
- **Banco:** `DatabaseCapacity`

---

## Opções de Fallback

| Opção | Descrição | Arquivo |
|-------|-----------|---------|
| **A - Separado** | Um script por job (executa individualmente) | `docs/job_table_mapping_and_fallback_inserts.md` |
| **B - Completo** | Todos os 7 jobs juntos (este arquivo) | Este documento |

---

## Instruções de Uso

1. **Conecte** no servidor de ORIGEM via SSMS
2. **Altere** a variável `@Esteira` conforme o ambiente:
   - `'PRODUÇÃO'` para PRD
   - `'HOMOLOGAÇÃO'` para HMG
   - `'DESENVOLVIMENTO'` para DSV
3. Pressione **`Ctrl+T`** (Results to Text)
4. **Execute** o script completo
5. **Copie TODOS** os INSERTs gerados
6. **Conecte** no destino: `sql-destino.EXEMPLO.CORP` → banco `DatabaseCapacity`
7. **Cole e execute** os INSERTs

---

## Script Completo - Todos os 7 Jobs

```sql
-- =====================================================================
-- FALLBACK MANUAL T-SQL - SCRIPT COMPLETO (7 JOBS)
-- =====================================================================
-- INSTRUÇÕES:
-- 1. Conecte no servidor de ORIGEM via SSMS
-- 2. Altere @Esteira conforme o ambiente (PRODUÇÃO, HOMOLOGAÇÃO, etc.)
-- 3. Pressione Ctrl+T (Results to Text)
-- 4. Execute este script completo
-- 5. Copie TODOS os INSERTs gerados
-- 6. Conecte no DESTINO: sql-destino.EXEMPLO.CORP → DatabaseCapacity
-- 7. Cole e execute os INSERTs
-- =====================================================================
-- VALORES VÁLIDOS PARA @Esteira:
-- PRODUÇÃO, HOMOLOGAÇÃO, DESENVOLVIMENTO, TESTE, QUERY, SLA, PARALELO, ANÁLISE, SANDBOX
-- =====================================================================

DECLARE @Esteira VARCHAR(128) = 'PRODUÇÃO';  -- ⚠️ ALTERE CONFORME O AMBIENTE

-- =====================================================================
-- JOB 01 - DatabaseSQLServerInfo
-- =====================================================================
PRINT '-- ========== JOB 01 - DatabaseSQLServerInfo =========='

SELECT 
    CONCAT(
        'INSERT INTO [dbo].[DatabaseSQLServerInfo] ',
        '([Servidor], [Esteira], [Instancia], [IP_Address], [Database_Name], ',
        '[compatibility_level], [compatibility_level_dsc], [Version], ',
        '[SQL_Server_Version], [ProductLevel], [Edition], [ProductVersion], ',
        '[collation_name], [Size_GBs], [DATA_CARGA_UTC], [DATA_CARGA_FORMATADA], ',
        '[CollectionTime], [DESCRICAO_QUERY]) VALUES (',
        '''', Servidor COLLATE DATABASE_DEFAULT, ''', ',
        '''', @Esteira COLLATE DATABASE_DEFAULT, ''', ',
        '''', (@@SERVERNAME + '\' + @@SERVICENAME) COLLATE DATABASE_DEFAULT, ''', ',
        '''', ISNULL(IP_Address, '') COLLATE DATABASE_DEFAULT, ''', ',
        '''', REPLACE([Database_Name] COLLATE DATABASE_DEFAULT, '''', ''''''), ''', ',
        [compatibility_level], ', ',
        '''', ISNULL(compatibility_level_dsc, '') COLLATE DATABASE_DEFAULT, ''', ',
        '''', REPLACE(ISNULL(CAST([Version] AS VARCHAR(300)), ''), '''', '''''') COLLATE DATABASE_DEFAULT, ''', ',
        '''', ISNULL(SQL_Server_Version, '') COLLATE DATABASE_DEFAULT, ''', ',
        '''', ISNULL(ProductLevel, '') COLLATE DATABASE_DEFAULT, ''', ',
        '''', ISNULL(Edition, '') COLLATE DATABASE_DEFAULT, ''', ',
        '''', ISNULL(ProductVersion, '') COLLATE DATABASE_DEFAULT, ''', ',
        '''', ISNULL(collation_name, '') COLLATE DATABASE_DEFAULT, ''', ',
        ISNULL(CAST(Size_GBs AS VARCHAR(20)), 'NULL'), ', ',
        'GETUTCDATE(), ',
        'GETDATE(), ',
        '''', CONVERT(VARCHAR(23), CollectionTime, 121), ''', ',
        '''', 'Informações Sql Server' COLLATE DATABASE_DEFAULT, ''');'
    ) AS InsertCommand
FROM master.dbo.vw_sql_info;

-- =====================================================================
-- JOB 02 - DatabaseServerDiskSpaceInfo
-- =====================================================================
PRINT '-- ========== JOB 02 - DatabaseServerDiskSpaceInfo =========='

SELECT CONCAT(
    'INSERT INTO [dbo].[DatabaseServerDiskSpaceInfo] ',
    '([Servidor], [Instancia], [Esteira], [Montagem], [Volume], [Total_GB], ',
    '[Espaço_Disponível_GB], [Espaço_Disponível_%], [Espaço_em_uso_%], ',
    '[DATA_CARGA_UTC], [DATA_CARGA_FORMATADA], [CollectionTime], [DESCRICAO_QUERY]) VALUES (',
    '''', CAST(@@SERVERNAME AS VARCHAR(128)), ''', ',
    '''', @@SERVERNAME + '\' + @@SERVICENAME, ''', ',
    '''', @Esteira, ''', ',
    '''', VS.volume_mount_point, ''', ',
    '''', ISNULL(VS.logical_volume_name, ''), ''', ',
    CAST(CAST(VS.total_bytes AS DECIMAL(19,2)) / 1024 / 1024 / 1024 AS DECIMAL(10,2)), ', ',
    CAST(CAST(VS.available_bytes AS DECIMAL(19,2)) / 1024 / 1024 / 1024 AS DECIMAL(10,2)), ', ',
    CAST((CAST(VS.available_bytes AS DECIMAL(19,2)) / CAST(VS.total_bytes AS DECIMAL(19,2)) * 100) AS DECIMAL(10,2)), ', ',
    CAST((100 - CAST(VS.available_bytes AS DECIMAL(19,2)) / CAST(VS.total_bytes AS DECIMAL(19,2)) * 100) AS DECIMAL(10,2)), ', ',
    'GETUTCDATE(), GETDATE(), ',
    '''', CONVERT(VARCHAR(23), GETDATE(), 121), ''', ',
    '''', 'Informações de Disco SQL Server', ''');'
) AS InsertCommand
FROM sys.master_files AS MF
CROSS APPLY sys.dm_os_volume_stats(MF.database_id, MF.file_id) AS VS
WHERE CAST(VS.available_bytes AS DECIMAL(19,2)) / CAST(VS.total_bytes AS DECIMAL(19,2)) * 100 < 100;

-- =====================================================================
-- JOB 03 - DatabaseServerCpuMemoryInfo
-- =====================================================================
PRINT '-- ========== JOB 03 - DatabaseServerCpuMemoryInfo =========='

SELECT CONCAT(
    'INSERT INTO [dbo].[DatabaseServerCpuMemoryInfo] ',
    '([Servidor], [Esteira], [Instancia], [Logical_CPU_Count], [Hyperthread_Ratio], ',
    '[Physical_CPU_Count], [Physical_Memory_MB], ',
    '[DATA_CARGA_UTC], [DATA_CARGA_FORMATADA], [CollectionTime], [DESCRICAO_QUERY]) VALUES (',
    '''', CAST(@@SERVERNAME AS VARCHAR(30)), ''', ',
    '''', @Esteira, ''', ',
    '''', @@SERVERNAME + '\' + @@SERVICENAME, ''', ',
    cpu_count, ', ',
    hyperthread_ratio, ', ',
    cpu_count/hyperthread_ratio, ', ',
    physical_memory_kb/1024, ', ',
    'GETUTCDATE(), GETDATE(), ',
    '''', CONVERT(VARCHAR(23), GETDATE(), 121), ''', ',
    '''', 'Informações de CPU e Memória SQL Server', ''');'
) AS InsertCommand
FROM sys.dm_os_sys_info;

-- =====================================================================
-- JOB 04 - DataBaseSQLServerSizeRowsLogs
-- =====================================================================
PRINT '-- ========== JOB 04 - DataBaseSQLServerSizeRowsLogs =========='

SELECT CONCAT(
    'INSERT INTO [dbo].[DataBaseSQLServerSizeRowsLogs] ',
    '([Servidor], [Instancia], [Esteira], [name], [DatabaseName], [size], [SizeMB], [type_desc], ',
    '[DATA_CARGA_UTC], [DATA_CARGA_FORMATADA], [CollectionTime], [DESCRICAO_QUERY]) VALUES (',
    '''', CAST(@@SERVERNAME AS VARCHAR(30)) COLLATE DATABASE_DEFAULT, ''', ',
    '''', (@@SERVERNAME + '\' + @@SERVICENAME) COLLATE DATABASE_DEFAULT, ''', ',
    '''', @Esteira COLLATE DATABASE_DEFAULT, ''', ',
    '''', CAST(a.name AS VARCHAR(128)) COLLATE DATABASE_DEFAULT, ''', ',
    '''', CAST(b.name AS VARCHAR(128)) COLLATE DATABASE_DEFAULT, ''', ',
    CAST(size AS BIGINT), ', ',
    CAST(CAST(size AS BIGINT)*8/1024 AS BIGINT), ', ',
    '''', CAST(type_desc AS VARCHAR(64)) COLLATE DATABASE_DEFAULT, ''', ',
    'GETUTCDATE(), GETDATE(), ',
    '''', CONVERT(VARCHAR(23), GETDATE(), 121), ''', ',
    '''', 'Informações de Tamanho de Databases SQL Server' COLLATE DATABASE_DEFAULT, ''');'
) AS InsertCommand
FROM sys.master_files a 
INNER JOIN sys.databases b ON a.database_id = b.database_id;

-- =====================================================================
-- JOB 05 - DatabaseWindowsInfo
-- =====================================================================
PRINT '-- ========== JOB 05 - DatabaseWindowsInfo =========='

SELECT CONCAT(
    'INSERT INTO [dbo].[DatabaseWindowsInfo] ',
    '([Servidor], [Esteira], [Instancia], [host_platform], [host_distribution], ',
    '[DATA_CARGA_UTC], [DATA_CARGA_FORMATADA], [CollectionTime], [DESCRICAO_QUERY]) VALUES (',
    '''', @@SERVERNAME, ''', ',
    '''', @Esteira, ''', ',
    '''', @@SERVERNAME + '\' + @@SERVICENAME, ''', ',
    '''', SUBSTRING(@@VERSION, CHARINDEX('Windows',@@VERSION,0), 7), ''', ',
    '''', REPLACE(SUBSTRING(@@VERSION, CHARINDEX('Windows',@@VERSION,0), 100), '''', ''''''), ''', ',
    'GETUTCDATE(), GETDATE(), ',
    '''', CONVERT(VARCHAR(23), GETDATE(), 121), ''', ',
    '''', 'Informações do Windows SQL Server', ''');'
) AS InsertCommand;

-- =====================================================================
-- JOB 06 - DataBaseSqlServerAdvancedInfo
-- =====================================================================
PRINT '-- ========== JOB 06 - DataBaseSqlServerAdvancedInfo =========='

SELECT 
    CONCAT(
        'INSERT INTO [dbo].[DataBaseSqlServerAdvancedInfo] ',
        '([Servidor], [Esteira], [Instancia], [cpu_count], [hyperthread_ratio], ',
        '[max_workers_count], [sqlserver_start_time], [Ad Hoc Distributed Queries], ',
        '[xp_cmdshell], [optimize for ad hoc workloads], [backup compression default], ',
        '[blocked process threshold (s)], [default trace enabled], [clr enabled], ',
        '[max server memory (MB)], [min server memory (MB)], [max degree of parallelism], ',
        '[cost threshold for parallelism], [max text repl size (B)], [show advanced options], ',
        '[DATA_CARGA_UTC], [DATA_CARGA_FORMATADA], [CollectionTime], [DESCRICAO_QUERY]) VALUES (',
        '''', CAST(@@SERVERNAME AS VARCHAR(30)) COLLATE DATABASE_DEFAULT, ''', ',
        '''', @Esteira COLLATE DATABASE_DEFAULT, ''', ',
        '''', (@@SERVERNAME + '\' + @@SERVICENAME) COLLATE DATABASE_DEFAULT, ''', ',
        '''', CAST(A.cpu_count AS VARCHAR(30)), ''', ',
        '''', CAST(A.hyperthread_ratio AS VARCHAR(30)), ''', ',
        A.max_workers_count, ', ',
        '''', CONVERT(VARCHAR(23), A.sqlserver_start_time, 121), ''', ',
        '''', ISNULL(CAST(B.[Ad Hoc Distributed Queries] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[xp_cmdshell] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[optimize for ad hoc workloads] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[backup compression default] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[blocked process threshold (s)] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[default trace enabled] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[clr enabled] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[max server memory (MB)] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[min server memory (MB)] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[max degree of parallelism] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[cost threshold for parallelism] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[max text repl size (B)] AS VARCHAR(30)), ''), ''', ',
        '''', ISNULL(CAST(B.[show advanced options] AS VARCHAR(30)), ''), ''', ',
        'GETUTCDATE(), ',
        'GETDATE(), ',
        '''', CONVERT(VARCHAR(23), GETDATE(), 121), ''', ',
        '''', 'Informações avançadas dos servidores SQL Server (pipeline)' COLLATE DATABASE_DEFAULT, ''');'
    ) AS InsertCommand
FROM sys.dm_os_sys_info A
CROSS JOIN (
    SELECT 
        MAX(CASE WHEN name = 'Ad Hoc Distributed Queries' THEN value_in_use END) AS [Ad Hoc Distributed Queries],
        MAX(CASE WHEN name = 'xp_cmdshell' THEN value_in_use END) AS [xp_cmdshell],
        MAX(CASE WHEN name = 'optimize for ad hoc workloads' THEN value_in_use END) AS [optimize for ad hoc workloads],
        MAX(CASE WHEN name = 'backup compression default' THEN value_in_use END) AS [backup compression default],
        MAX(CASE WHEN name = 'blocked process threshold (s)' THEN value_in_use END) AS [blocked process threshold (s)],
        MAX(CASE WHEN name = 'default trace enabled' THEN value_in_use END) AS [default trace enabled],
        MAX(CASE WHEN name = 'clr enabled' THEN value_in_use END) AS [clr enabled],
        MAX(CASE WHEN name = 'max server memory (MB)' THEN value_in_use END) AS [max server memory (MB)],
        MAX(CASE WHEN name = 'min server memory (MB)' THEN value_in_use END) AS [min server memory (MB)],
        MAX(CASE WHEN name = 'max degree of parallelism' THEN value_in_use END) AS [max degree of parallelism],
        MAX(CASE WHEN name = 'cost threshold for parallelism' THEN value_in_use END) AS [cost threshold for parallelism],
        MAX(CASE WHEN name = 'max text repl size (B)' THEN value_in_use END) AS [max text repl size (B)],
        MAX(CASE WHEN name = 'show advanced options' THEN value_in_use END) AS [show advanced options]
    FROM sys.configurations
) B;

-- =====================================================================
-- JOB 07 - DataBaseSqlServerDatabaseAdvancedInfo
-- =====================================================================
PRINT '-- ========== JOB 07 - DataBaseSqlServerDatabaseAdvancedInfo =========='

SELECT CONCAT(
    'INSERT INTO [dbo].[DataBaseSqlServerDatabaseAdvancedInfo] ',
    '([Servidor], [Esteira], [Instancia], [database_id], [DatabaseName], ',
    '[user_name], [create_date], [recovery_model_desc], [state_desc], ',
    '[compatibility_level], [IsCaseSensitive], [is_trustworthy_on], ',
    '[Collation_Name], [LastFullBackup], [LastDiffBackup], [LastLogBackup], ',
    '[IsCDCEnable], [DATA_CARGA_UTC], [DATA_CARGA_FORMATADA], ',
    '[CollectionTime], [DESCRICAO_QUERY]) VALUES (',
    '''', CAST(@@SERVERNAME AS VARCHAR(30)) COLLATE DATABASE_DEFAULT, ''', ',
    '''', @Esteira COLLATE DATABASE_DEFAULT, ''', ',
    '''', (@@SERVERNAME + '\' + @@SERVICENAME) COLLATE DATABASE_DEFAULT, ''', ',
    db.database_id, ', ',
    '''', REPLACE(db.name COLLATE DATABASE_DEFAULT, '''', ''''''), ''', ',
    '''', ISNULL(suser_sname(db.owner_sid), '') COLLATE DATABASE_DEFAULT, ''', ',
    CASE WHEN db.create_date IS NULL THEN 'NULL' 
         ELSE CONCAT('''', CONVERT(VARCHAR(23), db.create_date, 121), '''') END, ', ',
    '''', ISNULL(db.recovery_model_desc COLLATE DATABASE_DEFAULT, ''), ''', ',
    '''', ISNULL(db.state_desc COLLATE DATABASE_DEFAULT, ''), ''', ',
    db.compatibility_level, ', ',
    CAST(CAST(CHARINDEX(N'_CS_', db.collation_name) AS bit) AS VARCHAR(1)), ', ',
    CAST(CAST(db.is_trustworthy_on AS INT) AS VARCHAR(1)), ', ',
    '''', ISNULL(db.collation_name COLLATE DATABASE_DEFAULT, ''), ''', ',
    CASE WHEN t.LastFullBackup IS NULL THEN 'NULL' 
         ELSE CONCAT('''', CONVERT(VARCHAR(23), t.LastFullBackup, 121), '''') END, ', ',
    CASE WHEN t.LastDiffBackup IS NULL THEN 'NULL' 
         ELSE CONCAT('''', CONVERT(VARCHAR(23), t.LastDiffBackup, 121), '''') END, ', ',
    CASE WHEN t.LastLogBackup IS NULL THEN 'NULL' 
         ELSE CONCAT('''', CONVERT(VARCHAR(23), t.LastLogBackup, 121), '''') END, ', ',
    '''', CASE WHEN db.is_cdc_enabled = 1 THEN 'CDC' ELSE '0' END, ''', ',
    'GETUTCDATE(), GETDATE(), ',
    '''', CONVERT(VARCHAR(23), GETDATE(), 121), ''', ',
    '''', 'Informações sobre SQL Server e Servidores' COLLATE DATABASE_DEFAULT, ''');'
) AS InsertCommand
FROM master.sys.databases db
OUTER APPLY (
    SELECT
        MAX(CASE WHEN b.type = 'D' THEN b.backup_finish_date END) AS LastFullBackup,
        MAX(CASE WHEN b.type = 'I' THEN b.backup_finish_date END) AS LastDiffBackup,
        MAX(CASE WHEN b.type = 'L' THEN b.backup_finish_date END) AS LastLogBackup
    FROM msdb.dbo.backupset b
    WHERE b.database_name = db.name
) t;

PRINT '-- ========== FIM DOS SCRIPTS =========='
```

---

## Pré-requisitos no Servidor de Origem

### Job 01 - Requer view `vw_sql_info`

Se a view não existir, o Job 01 falhará. Verifique:

```sql
SELECT * FROM master.dbo.vw_sql_info
```

Se não existir, execute o script: `src/queries/11- create_vw_fn_sql_info.sql`

### Jobs 02 a 07 - Não requerem objetos especiais

Usam apenas DMVs e tabelas de sistema nativas do SQL Server.

---

## Troubleshooting

### Erro de Collation

Se aparecer erro de collation, todas as queries já incluem `COLLATE DATABASE_DEFAULT` para evitar conflitos.

### View não encontrada

```
Invalid object name 'master.dbo.vw_sql_info'
```

**Solução:** Criar a view no servidor de origem antes de executar o fallback.

### Timeout

Se o script demorar muito, execute job por job usando os scripts separados em `docs/job_table_mapping_and_fallback_inserts.md`.

---

## Referências

- **Scripts separados por job:** `docs/job_table_mapping_and_fallback_inserts.md`
- **Troubleshooting geral:** `.cursor/kb/sql-capacity/03-troubleshooting.md`
- **Portas de conexão:** `.cursor/kb/sql-capacity/07-portas-conexao-servidores.md`

---

*Documento criado em: 19/01/2026*

