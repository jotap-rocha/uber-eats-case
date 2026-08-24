#!/usr/bin/env python3
"""
Agent Spec Installer — instalação greenfield do kit agentic/SDD + Dev Loop.

Copia apenas a estrutura necessária (`.cursor/`, guias, scripts de validação, SDD, KB e agentes)
para um projeto vazio, com substituição de variáveis {{PROJECT_*}}.

Uso típico (a partir deste repositório template):

    python3 agentspec/install_agentspec.py \\
        --target /path/to/projeto-vazio \\
        --project-name "Meu Pipeline" \\
        --project-slug meu-pipeline \\
        --description "Pipeline de dados batch em PySpark"

    python3 agentspec/install_agentspec.py --dry-run --target .

Requer fonte do template via --source (default: diretório pai de agentspec/).
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

SUPPORTED_ECOSYSTEMS = ("cursor", "claude", "github")
PRIMARY_ECOSYSTEM = "cursor"

# Pastas/arquivos na raiz do template que NÃO vão para o projeto destino
SOURCE_EXCLUDE_TOP = {
    "templates",
    "install_dev_loop",
    "agentspec",
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
}

SOURCE_EXCLUDE_ANYWHERE = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}

# Arquivos de guia na raiz do template copiados para o destino
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

DOCS_TO_COPY = (
    "docs/inventario-ambiente.md.example",
)

# Arquivos na raiz do template renderizados com {{PROJECT_*}} (fonte com placeholders)
GENERATED_FILES = {
    "CONTEXT.md": "CONTEXT.md",
    ".cursorrules": ".cursorrules",
    "README.md": "README.md",
    "docs/00-INDEX.md": "docs/00-INDEX.md",
}

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
    ".j2",
}

# Em .cursor/sdd: copiar só _template dentro destas pastas de RUN
RUN_DIRS_KEEP_ONLY_TEMPLATE = (
    ("sdd", "reviews"),
    ("sdd", "data-pipeline-reviews"),
    ("sdd", "dev-loop-runs"),
)

# Em .cursor/dev: manter só gitkeep + PROMPTs de bootstrap
DEV_TASKS_KEEP = {
    "PROMPT_INIT_AGENTSPEC.md",
    "PROMPT_INIT_DEV_LOOP.md",
    "PROMPT_UPGRADE_AGENTIC.md",
    "PROMPT_HELLO_WORLD.md",
    ".gitkeep",
}

RESET_DEV_DIRS = (
    ("dev", "progress"),
    ("dev", "logs"),
    ("dev", "examples"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Instala Agent Spec (SDD + Dev Loop + agentes/KB) em projeto greenfield.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python3 agentspec/install_agentspec.py --target /tmp/projeto \\
      --project-name "Data Lake" --project-slug data-lake \\
      --description "Ingestão e curadoria medallion"

  python3 agentspec/install_agentspec.py --target . --ecosystem all --force

  python3 agentspec/install_agentspec.py --source /path/to/template-repo --dry-run --target .
        """,
    )
    default_source = Path(__file__).resolve().parent.parent
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.cwd(),
        help="Diretório do projeto destino (default: diretório atual)",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=default_source,
        help="Raiz do repositório template (default: pai de agentspec/)",
    )
    parser.add_argument(
        "--ecosystem",
        choices=(*SUPPORTED_ECOSYSTEMS, "all"),
        default="all",
        help="Ecossistemas: all (default — .cursor + .claude + .github), ou cursor, claude, github",
    )
    parser.add_argument("--project-name", default="Meu Projeto", help="Nome do projeto")
    parser.add_argument("--project-slug", default="meu-projeto", help="Slug (kebab-case)")
    parser.add_argument(
        "--description",
        default="Projeto com Agent Spec instalado a partir do template agentic.",
        help="Descrição curta do projeto",
    )
    parser.add_argument(
        "--stack",
        default="python,data-pipeline,spark",
        help="Stack (lista separada por vírgula) para documentação",
    )
    parser.add_argument(
        "--install-command",
        default="# Defina o comando de setup do projeto",
        help="Comando de instalação exibido no README",
    )
    parser.add_argument(
        "--test-command",
        default="python3 scripts/validate-agent-router.py",
        help="Comando de validação exibido no README",
    )
    parser.add_argument(
        "--project-context",
        default="",
        help="Parágrafos de contexto de domínio para o agente expert",
    )
    parser.add_argument(
        "--agent-scope",
        default="",
        help="Bullets Markdown com escopo do agente expert",
    )
    parser.add_argument("--force", action="store_true", help="Sobrescrever arquivos existentes")
    parser.add_argument("--dry-run", action="store_true", help="Simular sem gravar")
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Não executar validate-agent-router / validate-agentic-template ao final",
    )
    return parser.parse_args()


def variables(args: argparse.Namespace) -> dict[str, str]:
    project_context = args.project_context.strip() or args.description
    agent_scope = args.agent_scope.strip() or (
        "- Regras de negócio, execução e operação deste repositório.\n"
        "- Código, pipelines, documentação e fluxos SDD/Dev Loop do projeto."
    )
    return {
        "PROJECT_NAME": args.project_name,
        "PROJECT_SLUG": args.project_slug,
        "PROJECT_DESCRIPTION": args.description,
        "PROJECT_CONTEXT": project_context,
        "PROJECT_AGENT_SCOPE": agent_scope,
        "STACK": args.stack,
        "INSTALL_COMMAND": args.install_command,
        "TEST_COMMAND": args.test_command,
    }


def render_text(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
        text = text.replace("{{ " + key + " }}", value)
    return text


def is_text_file(path: Path) -> bool:
    if path.name in {".cursorrules", ".gitignore"}:
        return True
    return path.suffix.lower() in TEXT_SUFFIXES


def should_skip_cursor_file(rel: Path) -> bool:
    parts = rel.parts
    if not parts:
        return False
    # Canônico é CURSOR.MD; ignorar duplicata case-insensitive do template fonte
    if rel.name == "CURSOR.md":
        return True
    # MCP local é por máquina — instalar só o exemplo
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
            return parts[-1] not in DEV_TASKS_KEEP
        if parts[1] in {"progress", "logs"}:
            return parts[-1] != ".gitkeep"
        if parts[1] == "examples" and parts[-1] != "readme.md" and parts[-1] != ".gitkeep":
            return True

    return False


def write_bytes(
    dest: Path,
    content: bytes,
    *,
    force: bool,
    dry_run: bool,
) -> str:
    existed = dest.exists()
    if existed and not force:
        return "skip-existing"
    if dry_run:
        return "overwrite" if existed else "write"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(content)
    return "overwrite" if existed else "write"


def copy_cursor_tree(
    source: Path,
    target: Path,
    values: dict[str, str],
    *,
    ecosystem: str,
    force: bool,
    dry_run: bool,
) -> dict[str, int]:
    stats: dict[str, int] = {}
    src_cursor = source / ".cursor"
    dst_cursor = target / f".{ecosystem}"

    if not src_cursor.is_dir():
        raise FileNotFoundError(f"Fonte .cursor/ ausente: {src_cursor}")

    for src_file in src_cursor.rglob("*"):
        if not src_file.is_file():
            continue
        rel = src_file.relative_to(src_cursor)
        if should_skip_cursor_file(rel):
            continue

        dest_file = dst_cursor / rel
        rel_dest = f".{ecosystem}/{rel.as_posix()}"

        if is_text_file(src_file):
            text = src_file.read_text(encoding="utf-8")
            if ecosystem != PRIMARY_ECOSYSTEM:
                text = text.replace(".cursor/", f".{ecosystem}/")
                text = text.replace(".cursor", f".{ecosystem}")
            content = render_text(text, values).encode("utf-8")
        else:
            content = src_file.read_bytes()

        action = write_bytes(dest_file, content, force=force, dry_run=dry_run)
        stats[action] = stats.get(action, 0) + 1

    return stats


def copy_relative_file(
    source: Path,
    target: Path,
    rel: str,
    values: dict[str, str],
    *,
    force: bool,
    dry_run: bool,
) -> str:
    src = source / rel
    if not src.is_file():
        return "missing"
    dest = target / rel
    if is_text_file(src):
        content = render_text(src.read_text(encoding="utf-8"), values).encode("utf-8")
    else:
        content = src.read_bytes()
    return write_bytes(dest, content, force=force, dry_run=dry_run)


def install_generated_files(
    source: Path,
    target: Path,
    values: dict[str, str],
    *,
    force: bool,
    dry_run: bool,
) -> dict[str, int]:
    stats: dict[str, int] = {}
    for dest_rel, template_rel in GENERATED_FILES.items():
        src = source / template_rel
        if not src.is_file():
            continue
        action = write_bytes(
            target / dest_rel,
            render_text(src.read_text(encoding="utf-8"), values).encode("utf-8"),
            force=force,
            dry_run=dry_run,
        )
        stats[action] = stats.get(action, 0) + 1

    # CURSOR.MD canônico a partir do template genérico
    cursor_md_template = source / "templates" / "CURSOR.MD-generico.md"
    if cursor_md_template.is_file():
        text = render_text(cursor_md_template.read_text(encoding="utf-8"), values)
        action = write_bytes(
            target / ".cursor" / "CURSOR.MD",
            text.encode("utf-8"),
            force=force,
            dry_run=dry_run,
        )
        stats[action] = stats.get(action, 0) + 1

    return stats


def install_prompt_init(
    agentspec_dir: Path,
    target: Path,
    values: dict[str, str],
    ecosystems: tuple[str, ...],
    *,
    force: bool,
    dry_run: bool,
) -> None:
    prompt_src = agentspec_dir / "PROMPT_INIT_AGENTSPEC.md"
    if not prompt_src.is_file():
        return
    body = render_text(prompt_src.read_text(encoding="utf-8"), values)
    for ecosystem in ecosystems:
        dest = target / f".{ecosystem}" / "dev" / "tasks" / "PROMPT_INIT_AGENTSPEC.md"
        if ecosystem != PRIMARY_ECOSYSTEM:
            body_eco = body.replace(".cursor/", f".{ecosystem}/").replace(".cursor", f".{ecosystem}")
        else:
            body_eco = body
        write_bytes(dest, body_eco.encode("utf-8"), force=force, dry_run=dry_run)


def render_agent_expert(source: Path, values: dict[str, str]) -> str:
    template = source / "templates" / "agent-expert.md.j2"
    if not template.is_file():
        raise FileNotFoundError(f"Template de agente ausente: {template}")
    return render_text(template.read_text(encoding="utf-8"), values)


def ensure_domain_expert(
    source: Path,
    target: Path,
    values: dict[str, str],
    ecosystems: tuple[str, ...],
    *,
    force: bool,
    dry_run: bool,
) -> None:
    body = render_agent_expert(source, values)
    slug = values["PROJECT_SLUG"]
    for ecosystem in ecosystems:
        path = target / f".{ecosystem}" / "agents" / "domain" / f"{slug}-expert.md"
        text = body.replace(".cursor/", f".{ecosystem}/").replace(".cursor/sdd/", f".{ecosystem}/sdd/")
        write_bytes(path, text.encode("utf-8"), force=force, dry_run=dry_run)


def replace_section(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start = text.find(start_marker)
    if start == -1:
        return text + "\n\n" + replacement
    end = text.find(end_marker, start + len(start_marker))
    if end == -1:
        return text[:start] + replacement
    return text[:start] + replacement + text[end:]


def ensure_router_yaml(
    target: Path,
    values: dict[str, str],
    ecosystems: tuple[str, ...],
    *,
    dry_run: bool,
) -> None:
    if yaml is None:
        return

    slug = values["PROJECT_SLUG"]
    agent_id = f"{slug}-expert"
    for ecosystem in ecosystems:
        path = target / f".{ecosystem}" / "sdd" / "architecture" / "AGENT_ROUTER.yaml"
        if not path.is_file():
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        agents = data.setdefault("agents", [])
        agent_file = f".{ecosystem}/agents/domain/{agent_id}.md"
        if not any(isinstance(a, dict) and a.get("id") == agent_id for a in agents):
            agents.insert(
                0,
                {
                    "id": agent_id,
                    "file": agent_file,
                    "roster_group": "domain_platform",
                    "specialty_en": (
                        f'Especialista no projeto {values["PROJECT_NAME"]}: '
                        f'{values["PROJECT_DESCRIPTION"]}'
                    ),
                },
            )

        hints = data.setdefault("intake_hints", [])
        if not any(
            isinstance(h, dict) and h.get("primary_agent_id") == agent_id for h in hints
        ):
            hints.insert(
                0,
                {
                    "signals_pt": (
                        f'{values["PROJECT_NAME"]}, {slug}, domínio do projeto, '
                        "regras de negócio, execução, troubleshooting"
                    ),
                    "primary_agent_id": agent_id,
                    "context_paths": ["CONTEXT.md", "README.md", agent_file],
                },
            )

        if dry_run:
            print(f"[dry-run] atualizar {path}")
            continue
        path.write_text(
            yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=120),
            encoding="utf-8",
        )


def ensure_router_md(
    target: Path,
    values: dict[str, str],
    ecosystems: tuple[str, ...],
    *,
    dry_run: bool,
) -> None:
    slug = values["PROJECT_SLUG"]
    agent_id = f"{slug}-expert"
    expert_block = (
        "## Agente expert do repositório\n\n"
        f"Use este agente como primário quando a solicitação for específica do domínio `{slug}`.\n\n"
        "| Campo | Valor |\n"
        "|-------|--------|\n"
        f"| **Arquivo** | `{{ecosystem}}/agents/domain/{agent_id}.md` |\n"
        "| **Usar quando** | Dúvidas sobre domínio, execução, configuração, troubleshooting e arquitetura deste projeto |\n"
        f"| **Sinais típicos** | {values['PROJECT_NAME']}, {slug}, pipelines, jobs, logs, troubleshooting |\n\n"
    )

    for ecosystem in ecosystems:
        path = target / f".{ecosystem}" / "commands" / "core" / "router.md"
        if not path.is_file():
            continue
        block = expert_block.replace("{ecosystem}", f".{ecosystem}")
        text = path.read_text(encoding="utf-8")
        text = replace_section(text, "## Agente expert do repositório", "---", block)
        domain_line = f"- `{ecosystem}/agents/domain/{agent_id}.md`"
        if domain_line not in text and "### Exploration" in text:
            text = text.replace("### Exploration", domain_line + "\n\n### Exploration", 1)
        if dry_run:
            print(f"[dry-run] atualizar {path}")
            continue
        path.write_text(text, encoding="utf-8")


def mirror_ecosystem_from_cursor(
    target: Path,
    to_ecosystem: str,
    *,
    force: bool,
    dry_run: bool,
) -> dict[str, int]:
    """Copia .cursor/ → .claude/ ou .github/ com adaptação de paths (após install cursor)."""
    stats: dict[str, int] = {}
    src = target / ".cursor"
    dst = target / f".{to_ecosystem}"
    if not src.is_dir():
        return stats

    for src_file in src.rglob("*"):
        if not src_file.is_file():
            continue
        rel = src_file.relative_to(src)
        if should_skip_cursor_file(rel):
            continue
        dest_file = dst / rel
        rel_dest = f".{to_ecosystem}/{rel.as_posix()}"

        if is_text_file(src_file):
            text = src_file.read_text(encoding="utf-8")
            text = text.replace(".cursor/", f".{to_ecosystem}/")
            text = text.replace(".cursor", f".{to_ecosystem}")
            content = text.encode("utf-8")
        else:
            content = src_file.read_bytes()

        action = write_bytes(dest_file, content, force=force, dry_run=dry_run)
        stats[action] = stats.get(action, 0) + 1

    return stats


def ensure_claude_bridge(target: Path, values: dict[str, str], *, force: bool, dry_run: bool) -> None:
    claude_dir = target / ".claude"
    if not claude_dir.is_dir():
        return
    root_claude = target / "CLAUDE.md"
    body = (
        f"# {values['PROJECT_NAME']} — Claude Code\n\n"
        "Este repositório usa Agent Spec com fonte canônica em `.cursor/`.\n\n"
        f"- Contexto completo: `.claude/CLAUDE.md` ou `.claude/CURSOR.MD`\n"
        f"- Expert do domínio: `.claude/agents/domain/{values['PROJECT_SLUG']}-expert.md`\n"
        f"- Dev Loop: `/dev` e `/workflow-dev-loop`\n"
        f"- SDD: comandos em `.claude/commands/workflow/`\n"
    )
    write_bytes(root_claude, body.encode("utf-8"), force=force, dry_run=dry_run)

    claude_inner = claude_dir / "CLAUDE.md"
    cursor_md = claude_dir / "CURSOR.MD"
    if cursor_md.is_file() and not claude_inner.exists() and not dry_run:
        shutil.copy2(cursor_md, claude_inner)


def parse_ecosystems(choice: str) -> tuple[str, ...]:
    if choice == "all":
        return SUPPORTED_ECOSYSTEMS
    return (choice,)


def run_validations(
    target: Path,
    source: Path,
    ecosystems: tuple[str, ...],
) -> int:
    router_script = target / "scripts" / "validate-agent-router.py"
    template_script = source / "scripts" / "validate-agentic-template.py"
    code = 0

    if router_script.is_file():
        completed = subprocess.run(
            [sys.executable, str(router_script)],
            cwd=target,
            check=False,
        )
        if completed.returncode != 0:
            code = completed.returncode
    else:
        print("Aviso: scripts/validate-agent-router.py não encontrado no destino.", file=sys.stderr)

    # Validação completa exige espelhos .github e .claude (--ecosystem all)
    if len(ecosystems) < len(SUPPORTED_ECOSYSTEMS):
        if ecosystems == (PRIMARY_ECOSYSTEM,):
            print(
                "Info: validate-agentic-template omitido (padrão é --ecosystem all; "
                "reinstale com all para validar .github/ e .claude/)."
            )
        return code

    if template_script.is_file():
        completed = subprocess.run(
            [
                sys.executable,
                str(template_script),
                "--root",
                str(target),
                "--mode",
                "project",
            ],
            check=False,
        )
        if completed.returncode != 0 and code == 0:
            code = completed.returncode

    return code


def merge_stats(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, 0) + value
    return out


def print_report(
    target: Path,
    stats: dict[str, int],
    *,
    dry_run: bool,
    ecosystems: tuple[str, ...],
    values: dict[str, str],
) -> None:
    prefix = "[DRY RUN] " if dry_run else ""
    eco_label = ", ".join(f".{e}" for e in ecosystems)
    print(f"\n{prefix}Instalação Agent Spec → {target}")
    print(f"Ecossistemas: {eco_label}\n")
    for action, count in sorted(stats.items()):
        print(f"  {action}: {count}")

    print(
        f"""
Próximos passos:

  1. Abra o projeto no Cursor e leia `START_HERE.md` + `CONTEXT.md`.
  2. Execute o bootstrap no assistente:
     /dev tasks/PROMPT_INIT_AGENTSPEC.md
  3. Valide localmente:
     python3 scripts/validate-agent-router.py
  4. Inicie um ciclo Dev Loop (Nível 2):
     /workflow-dev-loop
     /devloop-init {values['PROJECT_SLUG']}-feature
  5. Para feature com rastreabilidade formal (Nível 3 SDD):
     /brainstorm  (ou consulte SDD_Guia_Comandos.md)

Agente expert: .cursor/agents/domain/{values['PROJECT_SLUG']}-expert.md
"""
    )


def install(
    *,
    source: Path,
    target: Path,
    agentspec_dir: Path,
    values: dict[str, str],
    ecosystems: tuple[str, ...],
    force: bool,
    dry_run: bool,
) -> dict[str, int]:
    stats: dict[str, int] = {}

    # 1) Árvore .cursor (sempre primária; espelhos derivam dela)
    stats = merge_stats(
        stats,
        copy_cursor_tree(
            source, target, values, ecosystem=PRIMARY_ECOSYSTEM, force=force, dry_run=dry_run
        ),
    )

    # 2) Espelhar .cursor → .claude / .github
    for eco in ecosystems:
        if eco == PRIMARY_ECOSYSTEM:
            continue
        stats = merge_stats(
            stats,
            mirror_ecosystem_from_cursor(target, eco, force=force, dry_run=dry_run),
        )

    # 3) Guias e scripts na raiz
    for rel in ROOT_GUIDE_FILES:
        action = copy_relative_file(source, target, rel, values, force=force, dry_run=dry_run)
        if action != "missing":
            stats[action] = stats.get(action, 0) + 1

    for rel in SCRIPTS_TO_COPY + DOCS_TO_COPY:
        action = copy_relative_file(source, target, rel, values, force=force, dry_run=dry_run)
        if action != "missing":
            stats[action] = stats.get(action, 0) + 1

    # docs/00-INDEX pode não existir ainda
    (target / "docs").mkdir(parents=True, exist_ok=True)

    stats = merge_stats(
        stats,
        install_generated_files(source, target, values, force=force, dry_run=dry_run),
    )

    install_prompt_init(agentspec_dir, target, values, ecosystems, force=force, dry_run=dry_run)
    ensure_domain_expert(source, target, values, ecosystems, force=force, dry_run=dry_run)
    ensure_router_yaml(target, values, ecosystems, dry_run=dry_run)
    ensure_router_md(target, values, ecosystems, dry_run=dry_run)

    if "claude" in ecosystems:
        ensure_claude_bridge(target, values, force=force, dry_run=dry_run)

    return stats


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    target = args.target.resolve()
    agentspec_dir = Path(__file__).resolve().parent
    ecosystems = parse_ecosystems(args.ecosystem)
    values = variables(args)

    if not source.is_dir():
        print(f"Erro: --source inexistente: {source}", file=sys.stderr)
        return 2
    if not target.exists():
        if args.dry_run:
            print(f"[dry-run] criaria diretório destino: {target}")
        else:
            target.mkdir(parents=True, exist_ok=True)
            print(f"Diretório destino criado: {target}")
    if not (source / ".cursor").is_dir():
        print(f"Erro: fonte sem .cursor/: {source / '.cursor'}", file=sys.stderr)
        return 2

    stats = install(
        source=source,
        target=target,
        agentspec_dir=agentspec_dir,
        values=values,
        ecosystems=ecosystems,
        force=args.force,
        dry_run=args.dry_run,
    )

    print_report(target, stats, dry_run=args.dry_run, ecosystems=ecosystems, values=values)

    if args.dry_run or args.skip_validation:
        return 0

    return run_validations(target, source, ecosystems)


if __name__ == "__main__":
    raise SystemExit(main())
