# STATUS — azure-warehouse

**Projeto:** Warehouse da Azure (Fase 1 do roadmap multi-cloud): conta, recursos e integrações do
Synapse Dedicated, com ingestão pelo Airbyte até o ADLS. Um dos 9 projetos `{cloud}-{arquitetura}`
(`azure-lakehouse`, `azure-kappa`, `aws-*`, `gcp-*` ganham processos próprios)  
**Slug:** azure-warehouse (era `azure-fase1`; renomeado em 2026-11-12)  
**Iniciado em:** 2026-11-11  
**Tipo:** pipeline cloud (Synapse Dedicated SQL Pool + ADLS; Airbyte local)  
**Fase atual:** 1 concluída; ADRs 014, 015 e 016 aceitas e `CLAUDE.md` atualizado (2026-11-13). Próximo: PRD (`harness-design`)

## SI assessment

Nível **a**, confirmado pelo usuário em 2026-11-12 (o `codebase-explorer` foi dispensado por ele): dado 100% sintético. Sem PII real e sem `[AVISO_LGPD]`. Bancos locais tratados como produção;
o agente nunca escreve em PRD. Credenciais Azure só fora do git. Detalhes nos invariantes do `CLAUDE.md`.

## Git

- Branch: `feat/planejamento-conta-azure` (decisão do usuário: não abrir outra)
- Tronco: `main`; nada de SDD direto nele

## Guardas de custo desta fase

- Nada de abrir conta nem `terraform apply` antes dos pré-requisitos da seção 3 do
  [planejamento](../../../azure/docs/PLANEJAMENTO_CONTA_AZURE.md) e com o usuário acompanhando.
- Todo `apply` de recurso pago: `plan` + estimativa por hora e por dia, e esperar o "ok".
- Recurso contínuo nasce com budget alert. Fim de sessão: listar o que roda e perguntar se pausa ou destrói.

## Checklist de fases

| Fase | Artefato | Estado |
|---|---|---|
| 0 | [00-ideia.md](00-ideia.md) | ok (2026-11-11) |
| 1 | [01-grill.md](01-grill.md) + revisão adversarial ([Gemini](01b-judge-gemini.md), [GPT](01b-judge-gpt.md)) | ok (2026-11-12) |
| 1b | ADRs [014](../../../docs/adr/014-ingestao-batch-pelo-airbyte-e-debezium-so-no-kappa.md), [015](../../../docs/adr/015-orquestrador-e-relogio-da-free-account-azure.md), [016](../../../docs/adr/016-promocao-dsv-prd-por-tag-e-aprovacao.md) + invariantes do `CLAUDE.md` | ok (2026-11-13) |
| 2 | 02-prd.md | pendente |
| 3 | 03-harness.md | pendente |
| 4 | 04-tasks-index.md | pendente |
| 5 | build | pendente |
| 6 | 05-retro.md | ao fim (`harness-ship`) |
