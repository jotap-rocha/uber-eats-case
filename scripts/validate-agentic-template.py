#!/usr/bin/env python3
"""Valida um template/projeto agentic baseado em Cursor, GitHub Copilot e Claude.

Modos:
- template: permite variaveis {{PROJECT_*}} nos arquivos parametrizados.
- project: falha se ainda houver variaveis {{...}} em arquivos principais.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

BASES = ('.cursor', '.github', '.claude')
EXCLUDED_PARTS = {'.git', '.venv', 'venv', '__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache', 'templates', 'data-agentic-ai-for-pipelines'}
ALLOWED_TEMPLATE_VARIABLES = {
    'PROJECT_NAME',
    'PROJECT_SLUG',
    'PROJECT_DESCRIPTION',
    'PROJECT_CONTEXT',
    'PROJECT_AGENT_SCOPE',
    'STACK',
    'INSTALL_COMMAND',
    'TEST_COMMAND',
}
MAIN_FILES = (
    'README.md',
    'CONTEXT.md',
    '.cursorrules',
    'get_started/START_HERE.md',
    'get_started/SDD_Guia_Comandos.md',
    'docs/00-INDEX.md',
    '.cursor/CURSOR.MD',
    '.github/CURSOR.MD',
    '.github/copilot-instructions.md',
    '.claude/CURSOR.MD',
    '.claude/CLAUDE.md',
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Valida estrutura agentic/SDD.')
    parser.add_argument('--root', default='.', help='Raiz do template ou projeto a validar.')
    parser.add_argument('--mode', choices=('template', 'project'), default='template')
    return parser.parse_args()


def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.pdf', '.ico', '.zip', '.gz'}:
        return False
    try:
        path.read_text(encoding='utf-8')
        return True
    except UnicodeDecodeError:
        return False


def iter_text_files(root: Path) -> Iterable[Path]:
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(root).parts
        if any(part in EXCLUDED_PARTS for part in rel_parts):
            continue
        if is_text_file(path):
            yield path


def validate_no_duplicate_cursor(root: Path, errors: list[str]) -> None:
    for base in BASES:
        lower = root / base / 'CURSOR.md'
        upper = root / base / 'CURSOR.MD'
        if lower.exists():
            errors.append(f'{base}: remova duplicidade sensivel a case: {lower.relative_to(root)}')
        if not upper.exists():
            errors.append(f'{base}: arquivo canonico ausente: {upper.relative_to(root)}')


def validate_yaml_available(errors: list[str]) -> None:
    if yaml is None:
        errors.append('PyYAML nao esta instalado. Instale com: pip install pyyaml')


def validate_router(root: Path, base: str, errors: list[str]) -> None:
    if yaml is None:
        return
    router = root / base / 'sdd/architecture/AGENT_ROUTER.yaml'
    if not router.exists():
        errors.append(f'{base}: AGENT_ROUTER.yaml ausente')
        return

    data = yaml.safe_load(router.read_text(encoding='utf-8')) or {}
    agents = data.get('agents') or []
    ids = {agent.get('id') for agent in agents if isinstance(agent, dict) and agent.get('id')}

    for agent in agents:
        if not isinstance(agent, dict):
            errors.append(f'{base}: entrada invalida em agents: {agent!r}')
            continue
        agent_id = agent.get('id')
        file_path = agent.get('file')
        if not agent_id or not file_path:
            errors.append(f'{base}: agente sem id/file: {agent!r}')
            continue
        if not (root / file_path).exists():
            errors.append(f'{base}: arquivo de agente inexistente para {agent_id}: {file_path}')

    for hint in data.get('intake_hints') or []:
        if not isinstance(hint, dict):
            continue
        primary_id = hint.get('primary_agent_id')
        if primary_id and primary_id not in ids:
            errors.append(f'{base}: hint aponta para agente inexistente: {primary_id}')
        for context_path in hint.get('context_paths') or []:
            if not (root / context_path).exists():
                errors.append(f'{base}: context_path inexistente: {context_path}')

    fallback = data.get('intake_fallback') or {}
    fallback_id = fallback.get('primary_agent_id')
    if fallback_id and fallback_id not in ids:
        errors.append(f'{base}: fallback aponta para agente inexistente: {fallback_id}')


def validate_kb_index(root: Path, base: str, errors: list[str]) -> None:
    if yaml is None:
        return
    index = root / base / 'kb/_index.yaml'
    if not index.exists():
        errors.append(f'{base}: kb/_index.yaml ausente')
        return

    data = yaml.safe_load(index.read_text(encoding='utf-8')) or {}
    for domain_name, domain in (data.get('domains') or {}).items():
        domain_path = root / base / 'kb' / str(domain.get('path', ''))
        if not domain_path.exists():
            errors.append(f'{base}: dominio KB inexistente em _index.yaml: {domain_name} -> {domain.get("path")}')
            continue
        for entry_name, entry_path in (domain.get('entry_points') or {}).items():
            if not (domain_path / entry_path).exists():
                errors.append(f'{base}: entrypoint KB inexistente: {domain_name}.{entry_name} -> {domain.get("path")}{entry_path}')


def validate_placeholders(root: Path, mode: str, errors: list[str]) -> None:
    angle_re = re.compile(r'<NOME_DO_PROJETO>|<comando>|<dominio-a>|<dominio-b>|<seu-projeto>')
    var_re = re.compile(r'{{\s*([A-Z0-9_]+)\s*}}')

    for relative in MAIN_FILES:
        path = root / relative
        if not path.exists():
            errors.append(f'arquivo principal ausente: {relative}')
            continue
        text = path.read_text(encoding='utf-8')
        if angle_re.search(text):
            errors.append(f'{relative}: contem placeholder angular legado')
        variables = set(var_re.findall(text))
        unknown = variables - ALLOWED_TEMPLATE_VARIABLES
        if unknown:
            errors.append(f'{relative}: variaveis template desconhecidas: {sorted(unknown)}')
        if mode == 'project' and variables:
            errors.append(f'{relative}: projeto renderizado ainda contem variaveis: {sorted(variables)}')


def validate_old_template_names(root: Path, errors: list[str]) -> None:
    forbidden = 'data-agentic-ai-for-' + 'pipelines'
    ignored_prefixes = ('templates/',)
    for path in iter_text_files(root):
        rel = path.relative_to(root).as_posix()
        if rel.startswith(ignored_prefixes):
            continue
        if path.name in {'validate-agentic-template.py', 'COMO_TORNAR_PROJETO_AGENTIC.md', '.gitignore'}:
            continue
        if forbidden in path.read_text(encoding='utf-8', errors='ignore'):
            errors.append(f'{rel}: contem nome antigo do template fonte')


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []

    if not root.exists():
        print(f'Raiz inexistente: {root}', file=sys.stderr)
        return 2

    validate_yaml_available(errors)
    validate_no_duplicate_cursor(root, errors)
    validate_placeholders(root, args.mode, errors)
    validate_old_template_names(root, errors)

    for base in BASES:
        validate_router(root, base, errors)
        validate_kb_index(root, base, errors)

    if errors:
        print('validate-agentic-template: FALHOU', file=sys.stderr)
        for error in errors:
            print(f'- {error}', file=sys.stderr)
        return 1

    print(f'validate-agentic-template: OK ({args.mode})')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
