USE [owshq-mssql-dev];

EXEC sys.sp_cdc_enable_db;

EXEC sys.sp_cdc_enable_table
  @source_schema = N'dbo',
  @source_name   = N'users',
  @role_name     = N'cdc_reader',
  @supports_net_changes = 1;

EXEC sys.sp_cdc_help_change_data_capture;