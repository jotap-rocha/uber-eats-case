#!/usr/bin/env bash
# Registra os hooks versionados em .githooks/ neste clone (uma vez por máquina).
# Não substitui a política de branch no GitHub — combina validação local + CI.
set -euo pipefail
ROOT="$(cd "$(dirname "${0}")/.." && pwd)"
cd "${ROOT}"
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit .githooks/pre-push 2>/dev/null || true
echo "OK: core.hooksPath=.githooks — pre-commit e pre-push ativos neste clone."
echo "    (Sem verificação automática de pastas; adicione linters ou testes nos hooks se quiser.)"
