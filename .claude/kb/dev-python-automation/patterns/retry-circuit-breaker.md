# Retries e resiliência em IO (SQL Server / rede)

> **Propósito:** Lidar com timeouts transitórios, deadlocks e indisponibilidade sem corromper estado.
> **MCP Validated:** 2026-05-06

## Quando usar

- Chamadas de rede ao servidor DB atrás de load balancer.
- Jobs longos onde **deadlock** ou **timeout** ocasional é esperado.

## Implementação

1. **Classificar** exceções: retentáveis (`OperationalError`, timeout, deadlock victim) vs permanentes (syntax, permissão).
2. **Backoff exponencial** com jitter; limitar tentativas máximas.
3. **Idempotência:** antes de retries em escritas, garantir que reexecutar o mesmo passo não duplica efeitos (chaves naturais, `MERGE`, estados).

```python
import random
import time
import logging

logger = logging.getLogger(__name__)


def with_retries(fn, *, attempts: int = 3, base_delay_s: float = 0.5):
    last_exc = None
    for n in range(attempts):
        try:
            return fn()
        except TransientDbError as e:
            last_exc = e
            delay = base_delay_s * (2**n) + random.random() * 0.1
            logger.warning("db_retry", extra={"attempt": n + 1, "delay": delay})
            time.sleep(delay)
    raise last_exc
```

Bibliotecas como **`tenacity`** ou **`circuitbreaker`** (já usada em projetos internos) reduzem boilerplate; alinhe política ao time.

## Configuração

| Parâmetro | Notas |
|-----------|-------|
| `attempts` | 3–5 típico para batch noturno |
| `circuit breaker` | Abrir após N falhas para não martelar DB em incidente |

## Armadilhas

- Retry em **meio de transação** sem rollback claro — pode manter locks.
- Retry infinito — mascara incidente e amplifica carga.

## Veja também

- [../concepts/logging-exit-codes.md](../concepts/logging-exit-codes.md)
- [config-segredos.md](config-segredos.md)
