# Phase: **gate** — Gate L2 vs L3

**Run:** `reorg-estrutura-raiz`
**Manifest:** estado canônico em `../DEVLOOP_MANIFEST.yaml` (`phases.gate.status`).

## Cenário

Pedido do usuário: reorganizar a estrutura de pastas na **raiz** do repositório, agrupando assuntos
semelhantes para reduzir a dispersão atual, com sugestões alinhadas a boas práticas de mercado.

Estado atual da raiz (`ls -la`, 2026-09-21): ~40 entradas de topo, incluindo pastas soltas
`debezium/`, `deploy/`, `docs/`, `gen/`, `get_started/`, `infra/`, `install_dev_loop/`, `logs/`,
`mongo/`, `pipeline/`, `scripts/`, `sql/`, `src/`, `templates/`, `tests/`, `agentspec/`,
`.agentspec-test/`, além de arquivos soltos (`docker-compose.yml`, `databricks.yml`, `LICENSE`,
`proximos-passos.md`, `README.md`, `requirements.txt`, `requirements-aws.txt`, `requirements-gcp.txt`,
`CONTEXT.md`, `CLAUDE.md`). Várias dessas pastas já têm subdivisão por nuvem (`docs/azure`,
`docs/gcp`, `infra/azure`, `infra/gcp`, `src/azure`, `src/gcp`, `sql/azure`, `sql/gcp`,
`tests/azure`, `tests/gcp` — conforme `git status`), evidenciando arquitetura multi-cloud
(AWS Fase 2, Azure Fase 1, GCP Fase 3) em paralelo.

## Avaliação — tabela `l2_vs_l3_gate`

| Critério L2 (`use_dev_loop_when`) | Aplica? |
|---|---|
| kb_building | Não |
| prototypes | Não |
| single_component_features | **Não** — mudança toca quase toda a raiz |
| utilities_parsers | Não |

| Critério L3/SDD (`use_sdd_when`) | Aplica? |
|---|---|
| multi_component_features | **Sim** — docs, infra, deploy, pipeline, sql, src, tests, debezium, gen, scripts |
| production_systems | **Sim** — projeto simula produção (Bronze/Silver/Gold, DLT, Unity Catalog) |
| team_projects_full_audit | Parcial — portfolio individual, mas com contratos operacionais documentados |
| full_audit_trail_required | **Sim** — reorganização de pastas exige rastrear referências (paths em `docker-compose.yml`, DAGs, scripts de deploy, CI) para não quebrar contratos existentes |

## Decisão

**`escalate_sdd`**

**Justificativa:** Reorganizar a raiz do repositório não é uma feature de componente único —
afeta caminhos referenciados por `docker-compose.yml`, `databricks.yml`, scripts de infra
(`infra/azure`, `infra/gcp`), pipelines (`pipeline/bronze`, `pipeline/silver`), Debezium
connectors e possivelmente CI. Um mapeamento incorreto de paths pode quebrar contratos
operacionais existentes (regra de "preservar contratos operacionais" em `.claude/CLAUDE.md`).
Este é exatamente o tipo de decisão de arquitetura que se beneficia do ciclo SDD completo
(brainstorm → define → design → build), com auditoria e reversibilidade, em vez do Dev Loop L2.

Além disso, o pedido do usuário ("analise e me dê sugestões") é uma exploração colaborativa de
opções — o próprio propósito da fase de **Brainstorm** do SDD, não uma tarefa de implementação
já definida.

## Próximo passo recomendado

- `/brainstorm` — explorar opções de agrupamento de pastas (ex.: `infra/{aws,azure,gcp}`,
  `docs/{cloud}`, consolidar `sql/`+`src/`+`tests/` por domínio ou por camada, mover
  `get_started/`, `install_dev_loop/`, `templates/` para um agrupador `dev/` ou `tooling/`, etc.)
  e validar com o usuário antes de qualquer `git mv`.
- Ver `SDD_Guia_Comandos.md` para a sequência completa `/brainstorm` → `/define` → `/design` → `/build`.

## Bloqueios / pendências

| Item | Severidade | Resumo |
|------|------------|--------|
| Escopo multi-componente | Alta | Gate decidiu escalar para SDD; RUN L2 não avança além de `gate` |
