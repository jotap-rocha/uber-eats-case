# Injeção de dependências e desacoplamento

> **Propósito:** Componentes não “fabricam” vizinhos acoplados; facilita testes e troca de implementações.
> **MCP Validated:** 2026-05-07

## Quando usar

- Qualquer serviço que hoje cria **logger**, **conexão** ou **cliente HTTP** no `__init__` com `import` concreto no meio da lógica.
- Jobs que precisam de **mesma lógica** em teste sem rede ou sem SQL Server.

## Princípio

**Quem compõe** (função `main`, factory `build_dependencies`) **instancia**; **quem executa** só recebe interfaces (`Protocol`, `typing.Callable`, ABC mínima). Configuração vem de **ambiente**, ficheiro ignorado pelo Git ou **vault** — nunca credencial versionada.

## Mau padrão

```python
class SyncService:
    def __init__(self) -> None:
        self._log = logging.getLogger(__name__)  # ok, mas...
        self._conn = pyodbc.connect(os.environ["RAW_CONN"])  # acoplado + segredo em env solto
```

## Bom padrão

```python
import logging
from typing import Protocol


class ConnectionFactory(Protocol):
    def __call__(self): ...


class SyncService:
    def __init__(
        self,
        logger: logging.Logger,
        connect: ConnectionFactory,
    ) -> None:
        self._log = logger
        self._connect = connect

    def run_once(self) -> int:
        self._log.info("sync_start")
        with self._connect() as conn:
            ...
        return 0
```

O **logger** pode ser `logging.getLogger(__name__)` no compositor e **passado** para serviços que precisem de contexto estável em testes (`assert logs`).

## Configuração

| Fonte | Uso |
|-------|-----|
| `os.environ` / `.env` (gitignored) | não sensível ou chaves para resolver segredo |
| Vault / OCI / Key Vault | produção |

## Veja também

- [../concepts/solid-scripts.md](../concepts/solid-scripts.md)
- [config-segredos.md](config-segredos.md)
- [repositorio-acesso-dados.md](repositorio-acesso-dados.md)
