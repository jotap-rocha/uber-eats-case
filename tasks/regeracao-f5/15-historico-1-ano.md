# Histórico de 1 ano de operação simulada

**Status:** done (aprovada em 2026-11-10; waivers: ac1 em 2026-11-14, ac2 em 2026-11-20)  
**Blocked by:** tasks/regeracao-f5/14-limpar-operacao-e-refazer-restock.md

## What to build

Rodar `run-simulator.ps1 -Days 365 -Seed 42` (executado pelo usuário), só histórico, sem conectores.

## Acceptance criteria

- [x] `ac1` `orders` com o volume esperado da simulação de 1 ano e `ultimo_pedido` próximo de agora. Revisado em 2026-11-14: a faixa original de 250 a 330 mil estava desatualizada; o real foi 400.743 e o usuário aceitou.
- [x] `ac2` Log sem `falha em` e sem parada por erro do banco.

## Notes

- Resultado: orders = deliveries = payments = 400.743; último pedido 2026-11-12 08:33:20; 3.365.174 ações.
- O primeiro `collect` do ac2 falhou por ambiente (`!` no cmd do Windows), não por conteúdo; refeito com Python. Log sem `falha em`.
- O traceback do topo do `logs/simulator.log` é de uma tentativa de 10/11 (`TRACKING_SALT_ORDER` ausente), anterior à execução válida.
