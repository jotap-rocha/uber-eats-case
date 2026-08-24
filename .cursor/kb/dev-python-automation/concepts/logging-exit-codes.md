# Erros, exceções de domínio, *fail fast* e logging

> **Propósito:** Falhas compreensíveis, logs acionáveis e integração limpa com schedulers.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Visão geral

Combine **exceções específicas do domínio**, validação **no início** das funções (*fail fast*) e **`logging`** com níveis semânticos. **`print`** em produção dificulta agregação e rotação. **Códigos de saída** explícitos comunicam sucesso vs falha ao orquestrador.

## Exceções de domínio

Crie hierarquias finas para erros **esperados** e distintos (config inválida, timeout de DB, violação de regra de negócio). Isso permite `except ConfigurationError:` sem apanhar `KeyboardInterrupt`.

```python
class JobError(Exception):
    """Base para falhas do job."""


class DatabaseConnectionError(JobError):
    ...
```

## Fail fast

Valide pré-condições e entradas **logo no início** da função pública; se algo for inválido, **lance** (ou retorne erro controlado) **antes** de abrir conexões ou efeitos colaterais.

## Níveis de log (semântica operacional)

| Nível | Uso típico |
|-------|------------|
| `DEBUG` | Detalhe para diagnóstico local (evitar dados sensíveis) |
| `INFO` | Fluxo normal: início/fim de passo, contagens |
| `WARNING` | Anomalia recuperável, retry, degradação |
| `ERROR` | Falha que exige intervenção ou aborta o job |

Bibliotecas como **loguru** ou **structlog** podem substituir ou envolver `logging` se o time padronizar — mantenha **níveis** e **contexto** (ex.: `extra={}`) equivalentes.

## Códigos de saída

```python
import logging
import sys

logger = logging.getLogger(__name__)

EXIT_OK = 0
EXIT_CONFIG = 2
EXIT_DB = 3


def main() -> int:
    try:
        ...
    except ConfigurationError:
        logger.exception("invalid_configuration")
        return EXIT_CONFIG
    except Exception:
        logger.exception("unhandled_failure")
        return EXIT_DB
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
```

## Erros comuns

### Errado

```python
print("done")
sys.exit()  # sempre 0
```

### Certo

```python
logger.info("job_finished", extra={"processed": n})
return EXIT_OK
```

## Relacionado

- [retry-circuit-breaker.md](../patterns/retry-circuit-breaker.md)
- [injecao-dependencias.md](../patterns/injecao-dependencias.md)
