# 🗃️ Objetos SQL Necessários — Pipeline SQL

## Visão Geral

Alguns jobs requerem objetos SQL específicos nos servidores fonte para funcionar corretamente.

| Job | Requer Objetos? | Script |
|-----|-----------------|--------|
| 00 | Não | - |
| 01 | **Sim** | `11- create_vw_fn_sql_info.sql` |
| 02 | **Sim** | `08 - create_vw_fn_disk_space_info.sql` |
| 03 | Não | (usa DMVs do sistema) |
| 04 | **Sim** | `10 - create_vw_fn_size_rows_log.sql` |
| 05 | Não | (usa DMVs do sistema) |
| 06 | Não | (usa DMVs do sistema) |
| 07 | Não | (usa DMVs do sistema) |

---

## Usuário Necessário

### usr_sql_capacity

Todos os servidores fonte devem ter o usuário `usr_sql_capacity` com:
- Login no SQL Server
- Acesso ao banco `msdb`
- Permissão para executar as functions e views criadas
- Permissão de leitura nas DMVs do sistema

---

## Job 01 - Script 11

### Arquivo
`src/queries/11- create_vw_fn_sql_info.sql`

### Objetos Criados
- Certificado para assinatura de código
- Login baseado no certificado
- Function `fn_SQL_Info()`
- View `vw_sql_info`

### Como Executar

1. Conectar no servidor SQL via SSMS
2. Abrir o arquivo `src/queries/11- create_vw_fn_sql_info.sql`
3. Executar o script completo
4. Verificar se os objetos foram criados:

```sql
-- Verificar function
SELECT * FROM sys.objects WHERE name = 'fn_SQL_Info'

-- Verificar view
SELECT * FROM sys.views WHERE name = 'vw_sql_info'

-- Testar a view
SELECT TOP 5 * FROM dbo.vw_sql_info
```

---

## Job 02 - Script 08

### Arquivo
`src/queries/08 - create_vw_fn_disk_space_info.sql`

### Objetos Criados
- Function para informações de disco
- View `vw_disk_space_info`

### Como Executar

1. Conectar no servidor SQL via SSMS
2. Abrir o arquivo `src/queries/08 - create_vw_fn_disk_space_info.sql`
3. Executar o script completo
4. Verificar se os objetos foram criados:

```sql
-- Verificar view
SELECT * FROM sys.views WHERE name LIKE '%disk%'

-- Testar a view
SELECT TOP 5 * FROM dbo.vw_disk_space_info
```

---

## Job 04 - Script 10

### Arquivo
`src/queries/10 - create_vw_fn_size_rows_log.sql`

### Objetos Criados
- Function para tamanho e linhas
- View `vw_size_rows_log`

### Como Executar

1. Conectar no servidor SQL via SSMS
2. Abrir o arquivo `src/queries/10 - create_vw_fn_size_rows_log.sql`
3. Executar o script completo
4. Verificar se os objetos foram criados:

```sql
-- Verificar view
SELECT * FROM sys.views WHERE name LIKE '%size%'

-- Testar a view
SELECT TOP 5 * FROM dbo.vw_size_rows_log
```

---

## Checklist de Criação de Objetos

Para cada novo servidor SQL fonte:

- [ ] Criar usuário `usr_sql_capacity`
- [ ] Conceder permissões no banco `msdb`
- [ ] Executar script `11- create_vw_fn_sql_info.sql`
- [ ] Executar script `08 - create_vw_fn_disk_space_info.sql`
- [ ] Executar script `10 - create_vw_fn_size_rows_log.sql`
- [ ] Testar as views
- [ ] Executar jobs de teste

---

## Diagnóstico de Objetos Ausentes

### Erro Comum
```
ERROR - ❌ [X/Y] SERVIDOR\MSSQLSERVER/msdb: Falha na leitura
```

### Verificar no Servidor

```sql
-- Verificar se as views existem
SELECT name FROM sys.views 
WHERE name IN ('vw_sql_info', 'vw_disk_space_info', 'vw_size_rows_log')

-- Verificar se as functions existem
SELECT name FROM sys.objects 
WHERE type = 'FN' 
AND name LIKE '%SQL_Info%' OR name LIKE '%disk%' OR name LIKE '%size%'

-- Verificar permissões do usuário
SELECT dp.name, dp.type_desc, o.name AS object_name, p.permission_name
FROM sys.database_principals dp
JOIN sys.database_permissions p ON dp.principal_id = p.grantee_principal_id
JOIN sys.objects o ON p.major_id = o.object_id
WHERE dp.name = 'usr_sql_capacity'
```

---

## Localização dos Scripts

```
src/queries/
├── 08 - create_vw_fn_disk_space_info.sql   # Job 02
├── 10 - create_vw_fn_size_rows_log.sql     # Job 04
├── 11- create_vw_fn_sql_info.sql           # Job 01
└── ... (outros scripts)
```

---

## Permissões Necessárias

### Para o usuário usr_sql_capacity

```sql
-- Permissões básicas
USE msdb;
CREATE USER [usr_sql_capacity] FOR LOGIN [usr_sql_capacity];
GRANT SELECT ON SCHEMA::dbo TO [usr_sql_capacity];

-- Permissões para DMVs
USE master;
GRANT VIEW SERVER STATE TO [usr_sql_capacity];
GRANT VIEW ANY DEFINITION TO [usr_sql_capacity];
```

### Para executar os scripts de criação

Necessário ter permissão de:
- `db_owner` no banco `msdb` (para criar objetos)
- `CONTROL SERVER` (para criar certificados e logins)

---

## Rollback (Se Necessário)

### Remover Objetos Criados

```sql
-- Script 11
DROP VIEW IF EXISTS dbo.vw_sql_info;
DROP FUNCTION IF EXISTS dbo.fn_SQL_Info;
-- (certificado e login precisam ser removidos manualmente)

-- Script 08
DROP VIEW IF EXISTS dbo.vw_disk_space_info;

-- Script 10
DROP VIEW IF EXISTS dbo.vw_size_rows_log;
```

---

## Suporte

Se os objetos não puderem ser criados:
1. Verificar permissões do usuário DBA
2. Consultar equipe de banco de dados
3. Usar fallback manual (INSERT direto)

