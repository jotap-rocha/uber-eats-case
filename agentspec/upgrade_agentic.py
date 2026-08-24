#!/usr/bin/env python3
"""
Upgrade / merge agentic — projeto destino já agentic + template mais completo.

Política padrão (preserva o destino):
  - Arquivos novos na fonte → copiados para o destino.
  - Arquivos idênticos → ignorados.
  - Arquivos diferentes → destino mantido; conflito registrado em .agentic-upgrade/.
  - AGENT_ROUTER.yaml e kb/_index.yaml → merge por chave/id (destino vence em duplicata).
  - Expert de domínio, PROMPTs em dev/tasks/, RUNs em sdd/ → nunca sobrescritos.

Uso:
    python3 agentspec/upgrade_agentic.py --target /path/to/projeto-local \\
        --source /path/to/template-agentic-fonte --dry-run

    python3 agentspec/upgrade_agentic.py --target /path/to/projeto --apply
"""
from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

PRIMARY_ECOSYSTEM = "cursor"
SUPPORTED_ECOSYSTEMS = ("cursor", "claude", "github")

SOURCE_EXCLUDE_ANYWHERE = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}

RUN_DIRS_KEEP_ONLY_TEMPLATE = (
    ("sdd", "reviews"),
    ("sdd", "data-pipeline-reviews"),
    ("sdd", "dev-loop-runs"),
)

DEV_TASKS_BOOTSTRAP = {
    "PROMPT_INIT_AGENTSPEC.md",
    "PROMPT_INIT_DEV_LOOP.md",
    "PROMPT_HELLO_WORLD.md",
    ".gitkeep",
}

ROOT_GUIDE_FILES = (
    "MANUAL_AGENTES.md",
    "HOW_TO_USE_AGENTS.md",
    "HOW_TO_MAKE_NEW_AGENT.md",
    "DEV_LOOP_Guia_Comandos.md",
    "SDD_Guia_Comandos.md",
    "AGENTIC_UPGRADE_Guia.md",
    "START_HERE.md",
)

SCRIPTS_TO_COPY = (
    "scripts/validate-agent-router.py",
    "scripts/validate-agentic-template.py",
    "scripts/enable-git-hooks.sh",
)

# Raiz: nunca sobrescrever conteúdo customizado do projeto
ROOT_PRESERVE_IF_EXISTS = frozenset(
    {
        "CONTEXT.md",
        "README.md",
        ".cursorrules",
        "CLAUDE.md",
    }
)

TEXT_SUFFIXES = {
    ".md",
    ".mdc",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".py",
    ".sh",
    ".toml",
    ".ini",
    ".example",
    ".gitignore",
}


@dataclass
class UpgradeStats:
    added: int = 0
    identical: int = 0
    preserved: int = 0
    conflict: int = 0
    merged_yaml: int = 0
    overwritten: int = 0
    conflicts: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "added": self.added,
            "identical": self.identical,
            "preserved": self.preserved,
            "conflict": self.conflict,
            "merged_yaml": self.merged_yaml,
            "overwritten": self.overwritten,
            "conflicts": self.conflicts,
        }


def parse_args() -> argparse.Namespace:
    default_source = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="Upgrade/merge do kit agentic: preserva destino, traz novidades do template.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  # Auditar (não grava)
  python3 agentspec/upgrade_agentic.py --target /path/projeto --dry-run

  # Aplicar merge
  python3 agentspec/upgrade_agentic.py --target /path/projeto --apply

  # Forçar sobrescrita de conflitos (exceto expert e PROMPTs locais)
  python3 agentspec/upgrade_agentic.py --target /path/projeto --apply --force
        """,
    )
    parser.add_argument("--target", type=Path, required=True, help="Projeto destino (já agentic)")
    parser.add_argument(
        "--source",
        type=Path,
        default=default_source,
        help="Template fonte (default: pai de agentspec/)",
    )
    parser.add_argument(
        "--ecosystem",
        choices=(*SUPPORTED_ECOSYSTEMS, "all"),
        default="cursor",
        help="Árvore a atualizar (default: cursor). Use all para espelhar após merge em .cursor/",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Gravar alterações (sem isso, apenas relatório / dry-run)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Alias explícito de não --apply")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Sobrescrever arquivos em conflito (exceto preserve_paths)",
    )
    parser.add_argument(
        "--no-merge-router",
        action="store_true",
        help="Não fazer merge de AGENT_ROUTER.yaml",
    )
    parser.add_argument(
        "--no-merge-kb-index",
        action="store_true",
        help="Não fazer merge de kb/_index.yaml (domains)",
    )
    parser.add_argument(
        "--report-json",
        type=Path,
        default=None,
        help="Gravar relatório JSON (mesmo em dry-run)",
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Não rodar validate-agent-router ao final",
    )
    return parser.parse_args()


def is_text_file(path: Path) -> bool:
    if path.name in {".cursorrules", ".gitignore"}:
        return True
    return path.suffix.lower() in TEXT_SUFFIXES


def should_skip_source_cursor(rel: Path) -> bool:
    parts = rel.parts
    if not parts:
        return False
    if rel.name == "CURSOR.md":
        return True
    if rel.name == "mcp.json":
        return True
    if any(part in SOURCE_EXCLUDE_ANYWHERE for part in parts):
        return True

    if parts[0] == "sdd" and len(parts) >= 2:
        for run_prefix in RUN_DIRS_KEEP_ONLY_TEMPLATE:
            if parts[:2] == run_prefix and "_template" not in parts:
                return True

    if parts[0] == "dev" and len(parts) >= 2:
        if parts[1] == "tasks":
            return False
        if parts[1] in {"progress", "logs"}:
            return parts[-1] != ".gitkeep"
        if parts[1] == "examples" and parts[-1] not in {"readme.md", ".gitkeep"}:
            return True

    return False


def is_preserve_path(rel_posix: str) -> bool:
    """Caminhos que nunca são sobrescritos pelo template."""
    if rel_posix in ROOT_PRESERVE_IF_EXISTS:
        return True
    if rel_posix.startswith("agents/domain/") and rel_posix.endswith("-expert.md"):
        return True
    if rel_posix.startswith("dev/tasks/"):
        name = Path(rel_posix).name
        if name not in DEV_TASKS_BOOTSTRAP:
            return True
    if "/sdd/reviews/" in rel_posix and "_template" not in rel_posix:
        return True
    if "/sdd/data-pipeline-reviews/" in rel_posix and "_template" not in rel_posix:
        return True
    if "/sdd/dev-loop-runs/" in rel_posix and "_template" not in rel_posix:
        return True
    if rel_posix.startswith("dev/progress/") and not rel_posix.endswith(".gitkeep"):
        return True
    if rel_posix.startswith("dev/logs/") and not rel_posix.endswith(".gitkeep"):
        return True
    return False


def merge_dict_shallow(dest: dict, src: dict) -> dict:
    out = dict(dest)
    for key, value in src.items():
        if key not in out:
            out[key] = value
    return out


def merge_list_by_key(
    dest_list: list,
    src_list: list,
    key_fn: Callable[[Any], Any],
) -> tuple[list, int]:
    """Destino vence em id duplicado; entradas novas da fonte são acrescentadas."""
    merged = []
    seen: set[Any] = set()
    added = 0

    for item in dest_list or []:
        if not isinstance(item, dict):
            merged.append(item)
            continue
        kid = key_fn(item)
        if kid is None:
            merged.append(item)
            continue
        seen.add(kid)
        merged.append(item)

    for item in src_list or []:
        if not isinstance(item, dict):
            continue
        kid = key_fn(item)
        if kid is None or kid in seen:
            continue
        merged.append(item)
        seen.add(kid)
        added += 1

    return merged, added


def hint_key(hint: dict) -> str | None:
    if hint.get("primary_agent_id"):
        return str(hint["primary_agent_id"])
    wf = hint.get("primary_workflow") or {}
    if isinstance(wf, dict) and wf.get("slash"):
        return str(wf["slash"])
    signals = hint.get("signals_pt")
    if signals:
        return str(signals)[:80]
    return None


def merge_agent_router(dest_path: Path, src_path: Path) -> tuple[dict[str, int], list[str]]:
    stats = {"merged_yaml": 0}
    notes: list[str] = []
    if yaml is None:
        notes.append("PyYAML ausente: merge de AGENT_ROUTER.yaml ignorado.")
        return stats, notes

    dest_data = yaml.safe_load(dest_path.read_text(encoding="utf-8")) or {}
    src_data = yaml.safe_load(src_path.read_text(encoding="utf-8")) or {}
    added_total = 0

    dest_data["roster_groups"] = merge_dict_shallow(
        dest_data.get("roster_groups") or {},
        src_data.get("roster_groups") or {},
    )

    for list_key, key_fn in (
        ("agents", lambda a: a.get("id")),
        ("intake_hints", hint_key),
        ("kb_reference", lambda k: k.get("kb_domain") or k.get("path")),
    ):
        if list_key not in src_data and list_key not in dest_data:
            continue
        merged, added = merge_list_by_key(
            dest_data.get(list_key) or [],
            src_data.get(list_key) or [],
            key_fn,
        )
        dest_data[list_key] = merged
        added_total += added

    if added_total:
        dest_path.write_text(
            yaml.safe_dump(dest_data, allow_unicode=True, sort_keys=False, width=120),
            encoding="utf-8",
        )
        stats["merged_yaml"] = 1
        notes.append(f"AGENT_ROUTER.yaml: +{added_total} entrada(s) da fonte (destino preservado em duplicatas).")

    return stats, notes


def merge_kb_index(dest_path: Path, src_path: Path) -> tuple[dict[str, int], list[str]]:
    stats = {"merged_yaml": 0}
    notes: list[str] = []
    if yaml is None:
        return stats, notes

    dest_data = yaml.safe_load(dest_path.read_text(encoding="utf-8")) or {}
    src_data = yaml.safe_load(src_path.read_text(encoding="utf-8")) or {}

    dest_domains = dest_data.setdefault("domains", {})
    src_domains = src_data.get("domains") or {}
    added = 0
    for key, value in src_domains.items():
        if key not in dest_domains:
            dest_domains[key] = value
            added += 1

    if added:
        dest_path.write_text(
            yaml.safe_dump(dest_data, allow_unicode=True, sort_keys=False, width=120),
            encoding="utf-8",
        )
        stats["merged_yaml"] = 1
        notes.append(f"kb/_index.yaml: +{added} domínio(s) KB da fonte.")

    return stats, notes


def record_conflict(
    staging: Path,
    rel: str,
    src: Path,
    dest: Path,
    *,
    apply: bool,
    dry_run: bool,
) -> None:
    incoming = staging / "incoming" / rel
    if apply and not dry_run:
        incoming.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, incoming)
        if dest.is_file():
            preserved = staging / "preserved" / rel
            preserved.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(dest, preserved)


def sync_file(
    src: Path,
    dest: Path,
    rel_posix: str,
    *,
    apply: bool,
    force: bool,
    staging: Path,
    stats: UpgradeStats,
) -> None:
    if not dest.exists():
        if apply:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
        stats.added += 1
        return

    if filecmp.cmp(src, dest, shallow=False):
        stats.identical += 1
        return

    if is_preserve_path(rel_posix):
        stats.preserved += 1
        return

    if force and apply:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        stats.overwritten += 1
        return

    stats.conflict += 1
    stats.conflicts.append(rel_posix)
    record_conflict(staging, rel_posix, src, dest, apply=apply, dry_run=not apply)


def iter_cursor_files(source_cursor: Path) -> Iterable[tuple[Path, Path]]:
    for src in source_cursor.rglob("*"):
        if not src.is_file():
            continue
        rel = src.relative_to(source_cursor)
        if should_skip_source_cursor(rel):
            continue
        yield rel, src


def upgrade_ecosystem_tree(
    source: Path,
    target: Path,
    ecosystem: str,
    *,
    apply: bool,
    force: bool,
    merge_router: bool,
    merge_kb_index_flag: bool,
    staging: Path,
) -> UpgradeStats:
    stats = UpgradeStats()
    src_cursor = source / ".cursor"
    dst_root = target / f".{ecosystem}"

    if not src_cursor.is_dir():
        raise FileNotFoundError(f"Fonte .cursor/ ausente: {src_tree}")

    for rel, src_file in iter_cursor_files(src_cursor):
        rel_posix = rel.as_posix()
        dest_file = dst_root / rel

        if rel_posix == "sdd/architecture/AGENT_ROUTER.yaml" and merge_router:
            if dest_file.is_file() and src_file.is_file():
                if apply:
                    mstats, _ = merge_agent_router(dest_file, src_file)
                    stats.merged_yaml += mstats.get("merged_yaml", 0)
                else:
                    stats.merged_yaml += 1
            elif not dest_file.is_file():
                sync_file(src_file, dest_file, rel_posix, apply=apply, force=force, staging=staging, stats=stats)
            continue

        if rel_posix == "kb/_index.yaml" and merge_kb_index_flag:
            if dest_file.is_file() and src_file.is_file():
                if apply:
                    mstats, _ = merge_kb_index(dest_file, src_file)
                    stats.merged_yaml += mstats.get("merged_yaml", 0)
                else:
                    stats.merged_yaml += 1
            elif not dest_file.is_file():
                sync_file(src_file, dest_file, rel_posix, apply=apply, force=force, staging=staging, stats=stats)
            continue

        if ecosystem != PRIMARY_ECOSYSTEM and is_text_file(src_file):
            text = src_file.read_text(encoding="utf-8")
            text = text.replace(".cursor/", f".{ecosystem}/").replace(".cursor", f".{ecosystem}")
            tmp = staging / "_tmp" / rel_posix
            if apply:
                tmp.parent.mkdir(parents=True, exist_ok=True)
                tmp.write_text(text, encoding="utf-8")
                sync_file(tmp, dest_file, rel_posix, apply=True, force=force, staging=staging, stats=stats)
            else:
                if dest_file.is_file() and dest_file.read_text(encoding="utf-8") == text:
                    stats.identical += 1
                elif not dest_file.is_file():
                    stats.added += 1
                elif is_preserve_path(rel_posix):
                    stats.preserved += 1
                else:
                    stats.conflict += 1
                    stats.conflicts.append(rel_posix)
            continue

        sync_file(src_file, dest_file, rel_posix, apply=apply, force=force, staging=staging, stats=stats)

    return stats


def copy_root_guides(
    source: Path,
    target: Path,
    *,
    apply: bool,
    force: bool,
    staging: Path,
    stats: UpgradeStats,
) -> None:
    for name in ROOT_GUIDE_FILES + SCRIPTS_TO_COPY:
        src = source / name
        if not src.is_file():
            continue
        dest = target / name
        rel = name
        if name in ROOT_PRESERVE_IF_EXISTS and dest.exists():
            stats.preserved += 1
            continue
        sync_file(src, dest, rel, apply=apply, force=force, staging=staging, stats=stats)


def mirror_ecosystem_from_cursor(target: Path, ecosystem: str, *, apply: bool, force: bool, staging: Path) -> UpgradeStats:
    """Espelha .cursor/ → .{ecosystem}/ para paths que faltam ou em conflito com política espelho."""
    stats = UpgradeStats()
    src = target / ".cursor"
    dst = target / f".{ecosystem}"
    if not src.is_dir():
        return stats

    for rel, src_file in iter_cursor_files(src):
        rel_posix = rel.as_posix()
        dest_file = dst / rel
        if rel_posix in {"sdd/architecture/AGENT_ROUTER.yaml", "kb/_index.yaml"}:
            continue
        if ecosystem != PRIMARY_ECOSYSTEM and is_text_file(src_file):
            text = src_file.read_text(encoding="utf-8")
            text = text.replace(".cursor/", f".{ecosystem}/").replace(".cursor", f".{ecosystem}")
            tmp = staging / "_mirror_tmp" / rel_posix
            if apply:
                tmp.parent.mkdir(parents=True, exist_ok=True)
                tmp.write_text(text, encoding="utf-8")
                sync_file(tmp, dest_file, rel_posix, apply=True, force=force, staging=staging, stats=stats)
            else:
                if not dest_file.is_file():
                    stats.added += 1
                elif dest_file.read_text(encoding="utf-8") == text:
                    stats.identical += 1
                elif is_preserve_path(rel_posix):
                    stats.preserved += 1
                else:
                    stats.conflict += 1
                    stats.conflicts.append(f".{ecosystem}/{rel_posix}")
            continue
        sync_file(src_file, dest_file, rel_posix, apply=apply, force=force, staging=staging, stats=stats)

    return stats


def assess_target(target: Path) -> dict[str, Any]:
    cursor = target / ".cursor"
    report: dict[str, Any] = {
        "has_cursor": cursor.is_dir(),
        "has_cursorrules": (target / ".cursorrules").is_file(),
        "has_context": (target / "CONTEXT.md").is_file(),
        "agent_count": 0,
        "command_dirs": [],
        "missing_workflows": [],
    }
    router = cursor / "sdd/architecture/AGENT_ROUTER.yaml"
    if router.is_file() and yaml is not None:
        data = yaml.safe_load(router.read_text(encoding="utf-8")) or {}
        report["agent_count"] = len(data.get("agents") or [])

    for wf in (
        "workflow-dev-loop",
        "workflow-data-pipeline-review",
        "workflow-makeapp-review",
    ):
        path = cursor / "commands" / wf
        if not path.is_dir():
            report["missing_workflows"].append(wf)
        else:
            report["command_dirs"].append(wf)

    if (cursor / "commands" / "intake.md").is_file():
        report["has_intake"] = True
    else:
        report["has_intake"] = False

    return report


def write_upgrade_report(
    target: Path,
    staging: Path,
    assessment: dict[str, Any],
    stats: UpgradeStats,
    notes: list[str],
    *,
    apply: bool,
) -> Path:
    staging.mkdir(parents=True, exist_ok=True)
    report_path = staging / "UPGRADE_REPORT.md"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    mode = "APLICADO" if apply else "DRY-RUN (simulação)"

    lines = [
        f"# Relatório de upgrade agentic — {mode}",
        "",
        f"Gerado em: {ts}",
        f"Destino: `{target}`",
        "",
        "## Avaliação do destino (antes)",
        "",
        f"- `.cursor/`: {'sim' if assessment.get('has_cursor') else '**não**'}",
        f"- Agentes no roteador: {assessment.get('agent_count', 0)}",
        f"- `/intake`: {'sim' if assessment.get('has_intake') else 'não'}",
        f"- Workflows ausentes: {', '.join(assessment.get('missing_workflows') or []) or 'nenhum detectado'}",
        "",
        "## Resumo da operação",
        "",
        f"| Métrica | Quantidade |",
        f"|---------|------------|",
        f"| Arquivos novos | {stats.added} |",
        f"| Idênticos (ignorados) | {stats.identical} |",
        f"| Preservados (política) | {stats.preserved} |",
        f"| Conflitos (destino mantido) | {stats.conflict} |",
        f"| YAML merge (router/KB) | {stats.merged_yaml} |",
        f"| Sobrescritos (--force) | {stats.overwritten} |",
        "",
    ]

    if notes:
        lines.extend(["## Notas de merge", ""] + [f"- {n}" for n in notes] + [""])

    if stats.conflicts:
        lines.extend(
            [
                "## Conflitos (revisão manual ou PROMPT)",
                "",
                "O destino foi **mantido**. Cópias para comparação em:",
                f"- `{staging / 'incoming'}` — versão do template",
                f"- `{staging / 'preserved'}` — versão que permanece no projeto",
                "",
            ]
        )
        for rel in sorted(stats.conflicts)[:80]:
            lines.append(f"- `{rel}`")
        if len(stats.conflicts) > 80:
            lines.append(f"- … e mais {len(stats.conflicts) - 80}")
        lines.extend(
            [
                "",
                "No assistente:",
                "```",
                "/dev tasks/PROMPT_UPGRADE_AGENTIC.md",
                "```",
                "",
            ]
        )

    if apply:
        report_path.write_text("\n".join(lines), encoding="utf-8")
    else:
        report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def merge_stats(a: UpgradeStats, b: UpgradeStats) -> UpgradeStats:
    out = UpgradeStats()
    for field_name in ("added", "identical", "preserved", "conflict", "merged_yaml", "overwritten"):
        setattr(out, field_name, getattr(a, field_name) + getattr(b, field_name))
    out.conflicts = a.conflicts + b.conflicts
    return out


def parse_ecosystems(choice: str) -> tuple[str, ...]:
    if choice == "all":
        return SUPPORTED_ECOSYSTEMS
    return (choice,)


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    target = args.target.resolve()
    apply = args.apply and not args.dry_run
    dry_run = not apply

    if not source.is_dir():
        print(f"Erro: --source inexistente: {source}", file=sys.stderr)
        return 2
    if not target.is_dir():
        print(f"Erro: --target inexistente: {target}", file=sys.stderr)
        return 2
    if not (source / ".cursor").is_dir():
        print(f"Erro: fonte sem .cursor/: {source}", file=sys.stderr)
        return 2

    staging = target / ".agentic-upgrade"
    if apply:
        shutil.rmtree(staging, ignore_errors=True)

    assessment = assess_target(target)
    ecosystems = parse_ecosystems(args.ecosystem)
    merge_router = not args.no_merge_router
    merge_kb = not args.no_merge_kb_index

    total = UpgradeStats()
    notes: list[str] = []

    if PRIMARY_ECOSYSTEM in ecosystems:
        total = upgrade_ecosystem_tree(
            source,
            target,
            PRIMARY_ECOSYSTEM,
            apply=apply,
            force=args.force,
            merge_router=merge_router,
            merge_kb_index_flag=merge_kb,
            staging=staging,
        )
        copy_root_guides(source, target, apply=apply, force=args.force, staging=staging, stats=total)
    else:
        for eco in ecosystems:
            total = merge_stats(
                total,
                upgrade_ecosystem_tree(
                    source,
                    target,
                    eco,
                    apply=apply,
                    force=args.force,
                    merge_router=merge_router and eco == PRIMARY_ECOSYSTEM,
                    merge_kb_index_flag=merge_kb and eco == PRIMARY_ECOSYSTEM,
                    staging=staging,
                ),
            )

    for eco in ecosystems:
        if eco == PRIMARY_ECOSYSTEM:
            continue
        if PRIMARY_ECOSYSTEM in ecosystems:
            total = merge_stats(
                total,
                mirror_ecosystem_from_cursor(
                    target, eco, apply=apply, force=args.force, staging=staging
                ),
            )

    report_path = write_upgrade_report(target, staging, assessment, total, notes, apply=apply)

    prefix = "[DRY-RUN] " if dry_run else ""
    print(f"\n{prefix}Upgrade agentic → {target}")
    print(f"Fonte: {source}\n")
    for key, val in total.as_dict().items():
        if key != "conflicts":
            print(f"  {key}: {val}")
    print(f"\nRelatório: {report_path}")

    if args.report_json:
        payload = {
            "target": str(target),
            "source": str(source),
            "apply": apply,
            "assessment": assessment,
            "stats": total.as_dict(),
            "notes": notes,
        }
        args.report_json.parent.mkdir(parents=True, exist_ok=True)
        args.report_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"JSON: {args.report_json}")

    if apply and not args.skip_validation:
        router_script = target / "scripts" / "validate-agent-router.py"
        if router_script.is_file():
            import subprocess

            completed = subprocess.run([sys.executable, str(router_script)], cwd=target, check=False)
            if completed.returncode != 0:
                print("Aviso: validate-agent-router falhou — revise conflitos e merge manual.", file=sys.stderr)
                return completed.returncode

    print("\nGuia: AGENTIC_UPGRADE_Guia.md (raiz do template)")
    if dry_run:
        print("Para aplicar: adicione --apply ao comando acima")
    else:
        print("Próximo passo sugerido:")
        print("  /dev tasks/PROMPT_UPGRADE_AGENTIC.md")
        if total.conflicts:
            print("  Revise conflitos em .agentic-upgrade/incoming/ vs preserved/")
        print("  /intake — priorizar conflitos ou lacunas pós-upgrade (ver guia)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
