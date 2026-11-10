# 03 — Harness

O harness deste projeto já existe e não foi gerado para ele: é o `.claude/` do repositório, com as
decisões abaixo registradas nas fontes originais.

- **Invariantes e convenções:** [CLAUDE.md](../../../CLAUDE.md) (ambientes, dados, ShadowTraffic, custo,
  segurança) e [.claude/CLAUDE.md](../../CLAUDE.md).
- **Rules transversais:** [.claude/rules/](../../rules/) — `definicao-de-pronto`, `seguranca`,
  `git-hygiene`, `github-repo`, `estilo-codigo`, `testes`.
- **Agente de domínio:** `uber-eats-case-expert`; apoio: `iac-engineer`, `cloud-data-engineer`.
- **Skills do projeto:** `shadowtraffic-adicionar-generator-seguro`, `shadowtraffic-ajustar-geracao`,
  `shadowtraffic-renovar-licenca`. Falta a skill de operação do simulador (task 18).
- **Gate:** `/validar` (ruff, mypy, pytest). Neste projeto o código está em `shared/gen`, ver a seção
  "Neste projeto" em [.claude/commands/validar.md](../../commands/validar.md).
- **Evidências:** `python -m config.evidence_gate`, manifestos em `evidencias/` desta pasta e uma linha por task em
  [metrics/entregas.jsonl](../../../metrics/entregas.jsonl).
