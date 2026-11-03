# Handoff — uber-eats-case

> Gerado pelo install-harness em 2026-10-16. Atualize a cada handoff de sessão.

## Estado atual

Modelagem de dados: regras (RN-01 a RN-42), conceitual e **modelo logico L0 a L4 aprovados**, em `shared/docs/modelagem/`. Branch `feat/modelo-logico` com 12 commits a frente da `main`, **sem push**. ADRs 006 a 008 aceitas. Oracle atual ainda tratado como producao; gerador nao religado.

## Próximos passos

1. Abrir a PR da `feat/modelo-logico` (com acordo do usuario).
2. Modelo fisico: DDL Postgres, Oracle e MongoDB; decimal e fuso no Debezium; onde calcular o codigo de rastreio; local do arquivo de parametros; guarda do simulador contra atendimento sem itens.
3. Regeracao dos dados (ADR 006/007): ShadowTraffic + simulador de operacao. A licenca trial vence por volta de 2026-11-07.
