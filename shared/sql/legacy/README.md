# Legado — CDC SQL Server

`database-cdc-config.sql` é T-SQL de SQL Server (`sp_cdc_enable_db`/`sp_cdc_enable_table`
sobre `owshq-mssql-dev`), não Postgres genérico. Não há serviço MSSQL no `docker-compose.yml`
nem consumidor ativo deste script no pipeline atual — mantido aqui como registro órfão/legado
(ADR-03 do `DESIGN_REORGANIZACAO_ESTRUTURA_RAIZ.md`), não como CDC comum às 3 nuvens.
