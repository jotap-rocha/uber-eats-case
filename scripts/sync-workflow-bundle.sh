#!/usr/bin/env bash
# Sincroniza .cursor/ (canônico) → install_dev_loop/workflow_bundle/ e assets/.
# Uso:
#   ./scripts/sync-workflow-bundle.sh           # sync + validate
#   ./scripts/sync-workflow-bundle.sh --dry-run # apenas mostra o que faria
#   ./scripts/sync-workflow-bundle.sh --no-validate

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CURSOR="${REPO_ROOT}/.cursor"
BUNDLE="${REPO_ROOT}/install_dev_loop/workflow_bundle/cursor"
ASSETS="${REPO_ROOT}/install_dev_loop/assets"
GUIDE_ROOT="${REPO_ROOT}/get_started/DEV_LOOP_Guia_Comandos.md"

DRY_RUN=0
RUN_VALIDATE=1

WORKFLOW_PATHS=(
  "commands/workflow-dev-loop"
  "agents/workflow-dev-loop"
  "sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml"
  "sdd/architecture/AGENT_ROUTER_DEVLOOP_FRAGMENT.yaml"
  "sdd/architecture/AGENT_ROUTER_DEVLOOP_MERGE.md"
  "sdd/dev-loop-runs"
  "rules/workflow-dev-loop-handoff.mdc"
)

usage() {
  cat <<'EOF'
sync-workflow-bundle.sh — espelha o workflow Dev Loop para o pacote de instalação

Opções:
  --dry-run       Mostra ações sem escrever arquivos
  --no-validate   Não executa scripts/validate-workflow-bundle.py ao final
  -h, --help      Esta ajuda

Fonte canônica:  .cursor/
Destinos:        install_dev_loop/workflow_bundle/cursor/
                 install_dev_loop/assets/dev/_index.md (__TREE__)
                 install_dev_loop/assets/DEV_LOOP_Guia_Comandos.md
EOF
}

log() {
  printf '%s\n' "$*"
}

run_rsync() {
  local src="$1"
  local dest="$2"
  local opts=(-a --delete)
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    opts+=(--dry-run -nv)
  fi
  rsync "${opts[@]}" "${src}/" "${dest}/"
}

run_cp() {
  local src="$1"
  local dest="$2"
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "  [dry-run] cp ${src} → ${dest}"
    return 0
  fi
  mkdir -p "$(dirname "${dest}")"
  cp -f "${src}" "${dest}"
}

sync_path() {
  local rel="$1"
  local src="${CURSOR}/${rel}"
  local dest="${BUNDLE}/${rel}"

  if [[ ! -e "${src}" ]]; then
    echo "sync-workflow-bundle: ausente no canônico: .cursor/${rel}" >&2
    exit 1
  fi

  if [[ -d "${src}" ]]; then
    log "  sync dir:  .cursor/${rel}/ → workflow_bundle/cursor/${rel}/"
    mkdir -p "$(dirname "${dest}")"
    run_rsync "${src}" "${dest}"
  else
    log "  sync file: .cursor/${rel} → workflow_bundle/cursor/${rel}"
    if [[ "${DRY_RUN}" -eq 0 ]]; then
      mkdir -p "$(dirname "${dest}")"
      cp -f "${src}" "${dest}"
    fi
  fi
}

sync_index_asset() {
  local src="${CURSOR}/dev/_index.md"
  local dest="${ASSETS}/dev/_index.md"

  if [[ ! -f "${src}" ]]; then
    echo "sync-workflow-bundle: ausente .cursor/dev/_index.md" >&2
    exit 1
  fi

  log "  asset:     .cursor/dev/_index.md → install_dev_loop/assets/dev/_index.md (.cursor → __TREE__)"
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    return 0
  fi
  mkdir -p "$(dirname "${dest}")"
  sed 's/\.cursor/__TREE__/g' "${src}" > "${dest}"
}

sync_guide_asset() {
  local dest="${ASSETS}/DEV_LOOP_Guia_Comandos.md"

  if [[ ! -f "${GUIDE_ROOT}" ]]; then
    echo "sync-workflow-bundle: ausente ${GUIDE_ROOT}" >&2
    exit 1
  fi

  log "  asset:     DEV_LOOP_Guia_Comandos.md → install_dev_loop/assets/"
  run_cp "${GUIDE_ROOT}" "${dest}"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      DRY_RUN=1
      RUN_VALIDATE=0
      ;;
    --no-validate)
      RUN_VALIDATE=0
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "sync-workflow-bundle: opção desconhecida: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
  shift
done

if [[ ! -d "${CURSOR}" ]]; then
  echo "sync-workflow-bundle: .cursor/ não encontrado em ${REPO_ROOT}" >&2
  exit 1
fi

mkdir -p "${BUNDLE}" "${ASSETS}/dev"

if [[ "${DRY_RUN}" -eq 1 ]]; then
  log "sync-workflow-bundle: [DRY RUN] a partir de ${REPO_ROOT}"
else
  log "sync-workflow-bundle: sincronizando a partir de ${REPO_ROOT}"
fi

for rel in "${WORKFLOW_PATHS[@]}"; do
  sync_path "${rel}"
done

sync_index_asset
sync_guide_asset

if [[ "${DRY_RUN}" -eq 1 ]]; then
  log ""
  log "sync-workflow-bundle: [DRY RUN] concluído (nenhum arquivo alterado)"
  exit 0
fi

log ""
log "sync-workflow-bundle: sincronização concluída"

if [[ "${RUN_VALIDATE}" -eq 1 ]]; then
  log "sync-workflow-bundle: validando paridade..."
  python3 "${REPO_ROOT}/scripts/validate-workflow-bundle.py"
fi
