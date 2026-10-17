# Repositório GitHub (baseline de PR, merge e proteção)

Regra **transversal** para projetos versionados no **GitHub**. Complementa `git-hygiene.md`
(que é agnóstico de SCM): aqui fica o que só existe no servidor. Se o remote for Azure Repos,
a mesma ideia vale via branch policies (ver `docs/cheatsheets/scm-pr-hibrido.md`).

Detalhe, racional e comandos: `docs/cheatsheets/github-repo-cheatsheet.md`.

## Baseline

1. **PR obrigatório na branch default** — nada de push direto; sem force-push nem delete.
2. **CI obrigatório** — workflow em `.github/workflows/` roda o gate (`ruff` + `mypy` + `pytest`)
   em `pull_request` e `push` na default; o nome do job vira o *required check*.
3. **Squash merge apenas** — título do squash = título do PR (`tipo(escopo): resumo`);
   desligar merge commit e rebase merge. Histórico linear.
4. **Apagar a branch após o merge** — `delete_branch_on_merge`.
5. **Conversas resolvidas** antes do merge. Aprovações: 0 em projeto solo; subir para ≥1 com time.
6. **Template de PR** em `.github/pull_request_template.md` (checklist de `git-hygiene`).
7. **Qualidade versionada** — `pyproject.toml` com config de `ruff`/`mypy` (sem config, o gate
   roda com regras implícitas e diverge entre máquinas).

## Quando o projeto é instalado / GitHub detectado

Se `git remote get-url origin` aponta para `github.com` e a baseline não está aplicada:

1. **Cheque** (read-only): `scripts/setup-github-repo.sh` (dry-run) e
   `gh api repos/{owner}/{repo}/branches/{default}/protection`.
2. **Oriente** o usuário: explique cada item acima e que o check só existe após 1 execução do CI.
3. **Só aplique com acordo explícito**: `scripts/setup-github-repo.sh --apply`. Mexe em
   configuração do repositório (outward-facing) — nunca rodar por conta própria.
4. Se não houver workflow de CI, ofereça criar um (mínimo: checkout, setup-python, `pip install`,
   `ruff check .`, `mypy`, `pytest -q`) **antes** de marcar o check como obrigatório — um check
   obrigatório que nunca roda trava todo merge.

## Limites (§1.3)

- `enforce_admins` fica **desligado** em projeto solo: o dono consegue contornar. Sem ele, a
  proteção é guarda-corpo, não cadeado. Em time, ligue.
- Branch protection exige repo público ou plano pago em repo privado.
- Hooks locais e esta rule não substituem a configuração do servidor — e vice-versa.
