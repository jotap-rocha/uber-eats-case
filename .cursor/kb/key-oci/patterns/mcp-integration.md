# Padrão: integração com MCP

## Cenário

O MCP local (`mcp/capacity-database`) pode receber valores em OCID no `.config`/env e precisa resolver antes de conectar ao SQL Server.

## Arquitetura atual

1. Node (`src/config.js`) monta lote de credenciais.
2. Se `MCP_OCI_RESOLVE` estiver habilitado, chama `applyOciCredentialValues`.
3. Bridge Python (`scripts/resolve_oci_mcp.py`) executa `resolve_credential_value` por campo.
4. Retorna JSON resolvido para Node concluir conexão.

## Benefícios

- Reuso da mesma lógica de segredos dos jobs.
- Suporte a valor literal e OCID no mesmo fluxo.
- Menos risco de divergência entre pipeline e MCP.

## Variáveis relevantes

- `MCP_CONFIG_FILE`
- `MCP_CONFIG_SECTION`
- `MCP_OCI_RESOLVE`
- `MCP_PYTHON`
- `MCP_SQL_HOST`, `MCP_SQL_USER`, `MCP_SQL_PASSWORD`, `MCP_SQL_DATABASE`, `MCP_SQL_PORT`

## Pontos de atenção

- CWD e `PYTHONPATH` devem apontar para raiz do projeto para import de `src.utils.key_oci`.
- Erro em um campo interrompe resolução com exit code `2` no bridge.

