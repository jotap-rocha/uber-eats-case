# Legado — CDC SQL Server

`database-cdc-config.sql` é T-SQL de SQL Server (`sp_cdc_enable_db`/`sp_cdc_enable_table`
sobre `owshq-mssql-dev`), não Postgres genérico. Não há serviço MSSQL no `docker-compose.yml`
nem consumidor ativo deste script no pipeline atual — mantido aqui como registro órfão/legado
(ADR-03 do `DESIGN_REORGANIZACAO_ESTRUTURA_RAIZ.md`), não como CDC comum às 3 nuvens.

# Legado — init do modelo antigo (até a regeração)

`postgres/` (`users`, `drivers`) e `oracle/` (`restaurants`, `products`, `inventory`, `orders`, `payments`,
`order_items`, `receipts`) são os scripts de init do modelo anterior à [ADR 006](../../../docs/adr/006-inversao-de-dominios-entre-oracle-e-postgres.md).
Saíram das pastas de init na implementação da F5.2 do [modelo físico](../../docs/modelagem/04-modelo-fisico.md); o seed
antigo do MongoDB está em `shared/mongo/legacy/`. Ficam como registro: o banco atual (anterior à regeração) foi criado
por eles.
