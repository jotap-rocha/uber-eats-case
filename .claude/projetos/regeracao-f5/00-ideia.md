# 00 — Ideia

Pipeline de dados de portfólio que simula um aplicativo de delivery (Uber Eats): fontes locais em Docker
(Postgres, Oracle, MongoDB), geração sintética (ShadowTraffic e um simulador de operação), CDC
(Debezium e Airbyte), Lakehouse e Warehouse nas três nuvens (Azure na Fase 1).

Esta pasta cobre a **regeração dos dados**: refazer as fontes do zero com o modelo aprovado
(ADR 006 a 013) para alimentar as fases de nuvem.

**Fontes (não duplicadas aqui):** [CONTEXT.md](../../../CONTEXT.md),
[roadmap multi-cloud](../../../shared/docs/ROADMAP_ARQUITETURA_MULTICLOUD.md),
[regras de negócio](../../../shared/docs/modelagem/01-regras-de-negocio.md).

**Tipo:** pipeline-local. **SI:** dado 100% sintético, ver [STATUS.md](STATUS.md).
