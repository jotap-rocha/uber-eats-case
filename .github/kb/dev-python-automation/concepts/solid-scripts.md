# SOLID em automação — evitar “espaguete”

> **Propósito:** Estruturar jobs para mudanças localizadas, extensão sem quebrar o núcleo e testes com substituição segura.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Visão geral

**SOLID** aplica-se a *qualquer* tamanho de módulo: o objetivo é **uma responsabilidade por unidade**, **abstrações estáveis** e **dependências invertidas**. Em automação, isso evita funções que leem DB, aplicam regra de negócio e enviam notificação no mesmo bloco.

## Princípios (visão generalizada)

| Princípio | Significado | Na prática |
|-----------|--------------|-------------|
| **S** — *Single Responsibility* | Um motivo para mudar por função/classe coerente | Ler repositório, transformar dados e notificar = **três** unidades (ou mais finas), não uma função monolítica |
| **O** — *Open/Closed* | Aberto a extensão, fechado a modificação desnecessária | Novo destino (fila, outro SMTP) = **nova implementação** de um `Protocol` ou subclasse, sem editar o núcleo cheio de `if tipo == ...` |
| **L** — *Liskov Substitution* | Subtipos honram o contrato da base | *Fakes* e implementações reais intercambiáveis sem surpresas para quem consome a interface |
| **I** — *Interface Segregation* | Interfaces pequenas | `ReadableStore` vs `WritableStore` em vez de um “Deus” com 20 métodos |
| **D** — *Dependency Inversion* | Depender de abstrações, não de concretos acoplados | Serviços recebem portas (`Protocol`), *loggers*, *repos* e *config* **injetados** — ver [injecao-dependencias.md](../patterns/injecao-dependencias.md) |

## Acoplamento a evitar

- **Caminhos e imports frágeis:** evitar depender de `sys.path` mutado ou de pastas fixas “mágicas”; preferir **pacote instalável** e imports normais (ver [estrutura-modulos-job.md](estrutura-modulos-job.md)).
- **Instanciar tudo dentro do “meio”:** quem orquestra monta dependências; quem executa só usa interfaces.

## Exemplo mínimo (DIP + SRP)

```python
from typing import Protocol


class RowStore(Protocol):
    def fetch_batch(self, limit: int) -> list[dict]: ...
    def mark_processed(self, ids: list[int]) -> None: ...


def process_pending(store: RowStore, limit: int = 100) -> int:
    rows = store.fetch_batch(limit)
    ...
    return len(rows)
```

## Relacionado

- [repositorio-acesso-dados.md](../patterns/repositorio-acesso-dados.md)
- [tipagem-fronteiras.md](tipagem-fronteiras.md)
