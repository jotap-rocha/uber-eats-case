-- Habilita ARCHIVELOG + supplemental logging na primeira inicializacao do
-- container Oracle -- pre-requisito do Debezium/LogMiner para capturar CDC.
-- Precisa ciclar a instancia (mount) para ligar archivelog; isso e seguro
-- aqui porque o gvenzl/oracle-free ainda esta no fluxo de inicializacao
-- (nao ha carga de aplicacao rodando ainda).

SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
ALTER DATABASE ARCHIVELOG;
ALTER DATABASE OPEN;

ALTER SYSTEM SET db_recovery_file_dest_size = 10G SCOPE=BOTH;

ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

ARCHIVE LOG LIST;
