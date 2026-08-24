# Padrão: uso de `return_secret` em jobs

## Objetivo

Padronizar consumo de credenciais e endpoints sem expor segredo em código.

## Padrão recomendado

```python
from src.utils import key_oci

dest_host = key_oci.return_secret("SQL_SERVER_HOSTNAME_DESTINATION")
dest_db = key_oci.return_secret("SQL_SERVER_DATABASE_CAPACITY_EVOLUTION")
dest_user = key_oci.return_secret("SQL_SERVER_USER_DESTINATION")
dest_pwd = key_oci.return_secret("SQL_SERVER_PASSWORD_DESTINATION")
```

## Onde já está aplicado

- `src/jobs/00_app_servidores_sql_apex.py`
- `src/jobs/01_app_obter_info_sql_server.py`
- `src/jobs/02..08`
- `src/jobs/10_app_obter_teste.py`

## Boas práticas

- Resolver secrets uma vez por contexto (evitar repetição desnecessária).
- Propagar mensagem de erro útil quando credencial crítica vier vazia.
- Nunca fazer `print(secret)` em logs.

## Anti-padrões

- Hardcode de usuário/senha/host.
- Ler `.config` diretamente em cada módulo de job.
- Tratar OCID sem passar por `key_oci`.

