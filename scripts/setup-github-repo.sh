#!/usr/bin/env bash
# Aplica a baseline de repositório GitHub (ver .claude/rules/github-repo.md).
# Idempotente. Padrão = dry-run (só mostra); --apply grava na API (exige acordo explícito).
# Uso: scripts/setup-github-repo.sh [--apply] [--repo owner/nome] [--check pytest] [--branch main]
set -euo pipefail

APPLY=0; REPO=""; CHECK="pytest"; BRANCH=""
while [ $# -gt 0 ]; do
  case "$1" in
    --apply) APPLY=1 ;;
    --repo) REPO="$2"; shift ;;
    --check) CHECK="$2"; shift ;;
    --branch) BRANCH="$2"; shift ;;
    -h|--help) sed -n '2,5p' "$0"; exit 0 ;;
    *) echo "argumento desconhecido: $1" >&2; exit 2 ;;
  esac
  shift
done

command -v gh >/dev/null || { echo "gh CLI não encontrado (https://cli.github.com)" >&2; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "gh não autenticado: rode 'gh auth login'" >&2; exit 1; }
[ -n "$REPO" ] || REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
[ -n "$BRANCH" ] || BRANCH=$(gh repo view "$REPO" --json defaultBranchRef -q .defaultBranchRef.name)

PROTECTION=$(cat <<JSON
{
  "required_status_checks": {"strict": false, "contexts": ["$CHECK"]},
  "enforce_admins": false,
  "required_pull_request_reviews": {"required_approving_review_count": 0,
    "dismiss_stale_reviews": false, "require_code_owner_reviews": false},
  "restrictions": null,
  "required_linear_history": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_conversation_resolution": true
}
JSON
)

echo "repo=$REPO branch=$BRANCH check=$CHECK"
echo "1) proteção de $BRANCH: PR obrigatório, check '$CHECK', histórico linear, sem force-push/delete, conversas resolvidas"
echo "2) repo: só squash merge (título e corpo do PR), apagar branch após merge"

if [ "$APPLY" -ne 1 ]; then
  echo "[dry-run] nada alterado. Rode com --apply após acordo explícito."
  exit 0
fi

echo "$PROTECTION" | gh api -X PUT "repos/$REPO/branches/$BRANCH/protection" --input - >/dev/null
gh api -X PATCH "repos/$REPO" \
  -F allow_squash_merge=true -F allow_merge_commit=false -F allow_rebase_merge=false \
  -F delete_branch_on_merge=true \
  -f squash_merge_commit_title=PR_TITLE -f squash_merge_commit_message=PR_BODY >/dev/null
echo "[ok] baseline aplicada em $REPO"
echo "Nota: o check '$CHECK' só aparece depois de rodar 1x no CI (ver .github/workflows/)."
