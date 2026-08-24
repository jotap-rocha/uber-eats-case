# Referência de chaves de configuração

## Chaves mais usadas com `return_secret`

### Destino SQL Server

- `SQL_SERVER_HOSTNAME_DESTINATION`
- `SQL_SERVER_PORT_DESTINATION`
- `SQL_SERVER_USER_DESTINATION`
- `SQL_SERVER_PASSWORD_DESTINATION`
- `SQL_SERVER_DATABASE_CAPACITY`
- `SQL_SERVER_DATABASE_CAPACITY_EVOLUTION`
- `SQL_SERVER_CAPACITY_USER`
- `SQL_SERVER_CAPACITY_PASS`

### Oracle/APEX (job 00)

- `ORACLE_HOSTNAME_APEXPRD_SCAN`
- `ORACLE_PORT_APEXPRD`
- `ORACLE_SERVICE_NAME_APEXPRD`
- `ORACLE_USER_REPOCORP_PRD`
- `ORACLE_PASSWORD_REPOCORP_PRD`

### Notificação

- `URL_WEBHOOK`

## Observações

- Esta lista reflete uso recorrente em `src/jobs/` e notebook EDA.
- Pode existir chave adicional por ambiente; validar no `.config` do projeto.

