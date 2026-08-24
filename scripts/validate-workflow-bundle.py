#!/usr/bin/env python3
"""Garante paridade entre .cursor/ canônico e install_dev_loop/workflow_bundle/."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CURSOR = REPO_ROOT / ".cursor"
BUNDLE = REPO_ROOT / "install_dev_loop" / "workflow_bundle" / "cursor"
ASSETS_INDEX = REPO_ROOT / "install_dev_loop" / "assets" / "dev" / "_index.md"

WORKFLOW_PATHS = (
    "commands/workflow-dev-loop",
    "agents/workflow-dev-loop",
    "sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml",
    "sdd/architecture/AGENT_ROUTER_DEVLOOP_FRAGMENT.yaml",
    "sdd/architecture/AGENT_ROUTER_DEVLOOP_MERGE.md",
    "sdd/dev-loop-runs",
    "rules/workflow-dev-loop-handoff.mdc",
)


def _read_normalized_index(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return text.replace("__TREE__", ".cursor")


def _compare_trees(rel: str, errors: list[str]) -> None:
    left = CURSOR / rel
    right = BUNDLE / rel
    if not left.exists():
        errors.append(f"ausente no canônico: .cursor/{rel}")
        return
    if not right.exists():
        errors.append(f"ausente no bundle: install_dev_loop/workflow_bundle/cursor/{rel}")
        return
    if left.is_file():
        if left.read_bytes() != right.read_bytes():
            errors.append(f"divergente: {rel}")
        return
    left_files = {p.relative_to(left) for p in left.rglob("*") if p.is_file()}
    right_files = {p.relative_to(right) for p in right.rglob("*") if p.is_file()}
    if left_files != right_files:
        only_left = left_files - right_files
        only_right = right_files - left_files
        if only_left:
            errors.append(f"extras só em .cursor/{rel}: {sorted(only_left)[:5]}")
        if only_right:
            errors.append(f"extras só no bundle/{rel}: {sorted(only_right)[:5]}")
    for name in sorted(left_files & right_files):
        lp, rp = left / name, right / name
        if lp.read_bytes() != rp.read_bytes():
            errors.append(f"divergente: {rel}/{name}")


def main() -> int:
    errors: list[str] = []
    if not CURSOR.is_dir():
        errors.append(f".cursor/ não encontrado em {REPO_ROOT}")
    if not BUNDLE.is_dir():
        errors.append(f"workflow_bundle não encontrado em {BUNDLE.parent}")

    for rel in WORKFLOW_PATHS:
        _compare_trees(rel, errors)

    if ASSETS_INDEX.is_file() and (CURSOR / "dev" / "_index.md").is_file():
        canon = (CURSOR / "dev" / "_index.md").read_text(encoding="utf-8")
        asset = _read_normalized_index(ASSETS_INDEX)
        if canon != asset:
            errors.append(
                "install_dev_loop/assets/dev/_index.md diverge de .cursor/dev/_index.md "
                "(após normalizar __TREE__ → .cursor)"
            )
    elif not ASSETS_INDEX.is_file():
        errors.append("ausente: install_dev_loop/assets/dev/_index.md")

    guide_asset = REPO_ROOT / "install_dev_loop" / "assets" / "DEV_LOOP_Guia_Comandos.md"
    guide_root = REPO_ROOT / "get_started" / "DEV_LOOP_Guia_Comandos.md"
    if guide_asset.is_file() and guide_root.is_file():
        if guide_asset.read_bytes() != guide_root.read_bytes():
            errors.append(
                "install_dev_loop/assets/DEV_LOOP_Guia_Comandos.md diverge da raiz"
            )
    elif not guide_asset.is_file():
        errors.append("ausente: install_dev_loop/assets/DEV_LOOP_Guia_Comandos.md")

    if errors:
        print("validate-workflow-bundle: FALHOU", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        f"validate-workflow-bundle: OK ({len(WORKFLOW_PATHS)} paths de workflow + assets)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
