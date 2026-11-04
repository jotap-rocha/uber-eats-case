# Handoff — uber-eats-case

> Gerado pelo install-harness em 2026-10-16. Atualize a cada handoff de sessão.

## Estado atual

Modelagem de dados: regras (RN-01 a RN-42), conceitual e **modelo logico L0 a L4 aprovados e mesclados na `main`** (PR #17, 2026-11-03), em `shared/docs/modelagem/`. ADRs 006 a 008 aceitas. Documentacao alinhada (links, avisos de obsoleto, roadmap 2.0). Oracle atual ainda tratado como producao; gerador nao religado. Branch de trabalho: `feat/modelo-fisico`.

## Proximos passos

1. **Modelo fisico** (`shared/docs/modelagem/04-modelo-fisico.md`), em fases com revisao por perguntas. **F0 aprovada** (2026-11-03; ADR 009: o simulador cria a compra numa transacao). **F1 aprovada** (2026-11-04; DDL Postgres, schema `ubereats`). MinIO fora do escopo (ADR 010, 2026-11-04; logica guardada em `shared/docs/minio/historico-geracao.md`). Proxima: F2 Oracle, F3 MongoDB, F4 CDC, F5 plano da regeracao.
2. **Regeracao dos dados do zero** (ADR 006/007/009): ShadowTraffic (cadastros, MongoDB) + simulador de operacao (compra e ciclo). Renovar a licenca do ShadowTraffic antes (vence por volta de 2026-11-07).
3. **Pipeline** (`shared/pipeline/`, hoje no modelo antigo): so depois do fisico e da regeracao.
