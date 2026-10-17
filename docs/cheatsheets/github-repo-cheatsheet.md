# GitHub — baseline do repositório (1 página)

Rule: `.claude/rules/github-repo.md` · Script: `scripts/setup-github-repo.sh` · Contrato de
branch/título: `git-hygiene.yaml`.

## Estado detectado no canônico (antes) → baseline alvo (depois)

| Item | Antes | Depois |
|---|---|---|
| PR obrigatório na `main` | sim (0 aprovações) | sim (0 aprovações — solo) |
| Force-push / delete da `main` | bloqueados | bloqueados |
| Status check obrigatório | nenhum (CI `testes-windows` não bloqueava) | `pytest` |
| Histórico linear | não | sim |
| Conversas resolvidas | não | sim |
| `enforce_admins` | desligado | desligado (solo; ligar em time) |
| Merge | squash + merge commit + rebase | **só squash** (título/corpo do PR) |
| Apagar branch após merge | desligado | ligado |
| Template de PR | `.github/pull_request_template.md` | idem |
| CI | `.github/workflows/testes-windows.yml` (PR + push `main`) | idem |
| Lint/tipos | sem `pyproject.toml` | `pyproject.toml` (ruff 100 col, mypy) |

## Convenções (repo, não servidor)

- Branch `feat|fix|chore/escopo-kebab` · PR `tipo(escopo): resumo` (≤ 72) · commits livres.
- Fonte única: `git-hygiene.yaml`; githooks locais em `.githooks/` (bootstrap em `scripts/`).

## Aplicar num projeto

```bash
scripts/setup-github-repo.sh                           # dry-run
scripts/setup-github-repo.sh --apply --check pytest    # após acordo; --check = nome do job do CI
```

Equivalente manual: Settings → Branches → rule da default (Require PR, Require status checks,
Linear history, Conversation resolution) e Settings → General → Pull Requests (só Squash,
"Automatically delete head branches").

## Armadilhas

- Marcar um check como obrigatório **antes** de ele rodar uma vez trava todos os merges.
- Nome do check = nome do **job** (`jobs.<id>` ou `name:`), não do workflow.
- O token do `gh` precisa de permissão de admin no repositório para `--apply`.
- §1.3: sem `enforce_admins`, o dono contorna; hooks/rules locais não impedem de fato.
