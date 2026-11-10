# 02 — PRD

Neste projeto os modelos aprovados fazem o papel de PRD. Não há cópia: a fonte é única.

| Camada | Documento |
|---|---|
| Regras de negócio (RN-01 a RN-42) | [01-regras-de-negocio.md](../../../shared/docs/modelagem/01-regras-de-negocio.md) |
| Modelo conceitual | [02-modelo-conceitual.md](../../../shared/docs/modelagem/02-modelo-conceitual.md) |
| Modelo lógico (L0 a L4) | [03-modelo-logico.md](../../../shared/docs/modelagem/03-modelo-logico.md) |
| Modelo físico (F0 a F5) e **ordem da regeração (F5.3)** | [04-modelo-fisico.md](../../../shared/docs/modelagem/04-modelo-fisico.md) |

**Escopo deste projeto:** a F5.2 (implementação do simulador, seeds, checks e init) e a F5.3 (execução da
regeração), com a ordem ajustada pela [ADR 013](../../../docs/adr/013-snapshot-inicial-aceito-na-regeracao.md).

**Fora do escopo:** refazer o `shared/pipeline/` (Bronze, Silver, Gold) e as fases de nuvem. Entram como
projetos próprios depois da regeração.
