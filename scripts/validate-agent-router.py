#!/usr/bin/env python3
"""Valida .cursor/sdd/architecture/AGENT_ROUTER.yaml (sintaxe, ids, arquivos de agente)."""
from __future__ import annotations

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ROUTER_PATH = os.path.join(
    REPO_ROOT, ".cursor", "sdd", "architecture", "AGENT_ROUTER.yaml"
)


def main() -> int:
    try:
        import yaml  # type: ignore
    except ImportError:
        print("Instale PyYAML: pip install pyyaml", file=sys.stderr)
        return 2

    with open(ROUTER_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    errors: list[str] = []
    agents = data.get("agents") or []
    ids = {a["id"] for a in agents if isinstance(a, dict) and "id" in a}

    for a in agents:
        if not isinstance(a, dict):
            continue
        aid = a.get("id")
        rel = a.get("file")
        if not aid or not rel:
            errors.append(f"agente sem id/file: {a}")
            continue
        path = os.path.join(REPO_ROOT, rel)
        if not os.path.isfile(path):
            errors.append(f"arquivo inexistente para {aid}: {rel}")

    for h in data.get("intake_hints") or []:
        if not isinstance(h, dict):
            continue
        pid = h.get("primary_agent_id")
        if pid and pid not in ids:
            errors.append(f"intake_hints.primary_agent_id desconhecido: {pid}")
        fb = h.get("primary_workflow")
        if fb and not isinstance(fb, dict):
            errors.append(f"primary_workflow inválido em signals_pt={h.get('signals_pt')!r}")

    fb = data.get("intake_fallback") or {}
    fb_id = fb.get("primary_agent_id")
    if fb_id and fb_id not in ids:
        errors.append(f"intake_fallback.primary_agent_id desconhecido: {fb_id}")

    contract = data.get("intake_contract") or {}
    if contract:
        required_step_ids = {
            "read_user_intent",
            "classify_one_line",
            "select_agents",
            "list_context_paths",
            "execute_agents_parallel",
            "synthesize_response",
            "optional_follow_up",
        }
        step_ids = {
            s.get("id")
            for s in (contract.get("steps") or [])
            if isinstance(s, dict) and s.get("id")
        }
        missing = required_step_ids - step_ids
        if missing:
            errors.append(
                f"intake_contract.steps faltando ids: {sorted(missing)}"
            )
        max_agents = contract.get("max_agents_parallel")
        if max_agents is not None and (
            not isinstance(max_agents, int) or max_agents < 1 or max_agents > 5
        ):
            errors.append(
                "intake_contract.max_agents_parallel deve ser inteiro entre 1 e 5"
            )
        if contract.get("mode") != "execute_and_synthesize":
            errors.append(
                'intake_contract.mode deve ser "execute_and_synthesize"'
            )

    if errors:
        print("validate-agent-router: FALHOU", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        return 1

    print(f"validate-agent-router: OK ({len(ids)} agentes, {len(data.get('intake_hints') or [])} hints)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
