# Architecture Decision Records

Registro de decisões arquiteturais significativas deste projeto.

Criadas via `/new-adr` (skill `.claude/skills/new-adr/`). ADRs são **imutáveis**: uma decisão
revista não é editada — ganha uma ADR nova que a substitui.

## Decisões

| # | Título | Status | Data |
|---|---|---|---|
| [001](001-sincronia-de-contexto-no-fechamento.md) | Sincronia de contexto no fechamento do fluxo | Aceita | 2026-08-05 |
| [002](002-pacote-e-keyvault-cloud-dual-install.md) | Pacote E keyvault-cloud + skill dual + install vault | Aceita | 2026-08-12 |
| [003](003-kernel-agent-policies-dual-runtime.md) | Kernel agent-policies dual-runtime (deny/ask + foundation) | Aceita | 2026-08-13 |
| [004](004-kernel-evidence-gate.md) | Kernel evidence-gate (collect/check + foundation) | Aceita | 2026-08-13 |
| [005](005-kernel-fluxo-events.md) | Kernel fluxo-events (telemetria live SDD) | Aceita | 2026-08-13 |
| [006](006-inversao-de-dominios-entre-oracle-e-postgres.md) | Inversão de domínios entre Oracle e Postgres (pedido e catálogo no Postgres) | Aceita | 2026-10-18 |
| [007](007-estoque-por-movimentos-e-gerador-hibrido.md) | Estoque por ficha técnica e movimentos, com gerador híbrido | Aceita (fronteira do gerador revista pela 009) | 2026-11-02 |
| [008](008-historico-de-status-em-tabelas-de-transicao.md) | Histórico de status em tabelas de transição, não só em CDC | Aceita | 2026-11-02 |
| [009](009-simulador-cria-a-compra-numa-transacao.md) | O simulador de operação cria a compra numa transação | Aceita (`kafka/gps` revisto pela 010) | 2026-11-03 |
| [010](010-minio-fora-do-escopo-da-geracao.md) | MinIO fora do escopo da geração e do modelo | Aceita | 2026-11-04 |
