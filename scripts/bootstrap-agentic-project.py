#!/usr/bin/env python3
"""Aplica o template agentic/SDD em um projeto destino.

O script usa esta pasta como fonte, renderiza variaveis {{...}}, cria o agente expert do projeto e valida o resultado.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Iterable

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

BASES = ('.cursor', '.github', '.claude')
EXCLUDED_PARTS = {
    '.git',
    '.venv',
    'venv',
    '__pycache__',
    '.pytest_cache',
    '.mypy_cache',
    '.ruff_cache',
}
EXCLUDED_TOP_LEVEL = {'templates'}
TEXT_SUFFIXES = {
    '.md', '.mdc', '.txt', '.yaml', '.yml', '.json', '.py', '.sh', '.toml', '.ini', '.example', '.gitignore'
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Bootstrap agentic/SDD em um projeto destino.')
    parser.add_argument('--target', required=True, help='Diretorio raiz do projeto destino.')
    parser.add_argument('--project-name', required=True, help='Nome humano do projeto.')
    parser.add_argument('--project-slug', required=True, help='Slug usado em arquivos, ex: zabbix-services-availability.')
    parser.add_argument('--description', required=True, help='Descricao curta do projeto.')
    parser.add_argument('--stack', default='python,data-pipeline', help='Stack em lista separada por virgula.')
    parser.add_argument('--project-context', default='', help='Contexto de dominio em 1-3 paragrafos.')
    parser.add_argument('--agent-scope', default='', help='Escopo em bullets Markdown para o agente expert.')
    parser.add_argument('--install-command', default='pip install -r requirements.txt')
    parser.add_argument('--test-command', default='python scripts/validate-agent-router.py')
    parser.add_argument('--source', default=None, help='Raiz do template. Default: pasta pai deste script.')
    parser.add_argument('--force', action='store_true', help='Sobrescreve arquivos agentic existentes.')
    parser.add_argument('--dry-run', action='store_true', help='Mostra o que faria sem escrever arquivos.')
    parser.add_argument('--skip-validation', action='store_true', help='Nao roda validate-agentic-template ao final.')
    return parser.parse_args()


def source_root(args: argparse.Namespace) -> Path:
    if args.source:
        return Path(args.source).resolve()
    return Path(__file__).resolve().parents[1]


def variables(args: argparse.Namespace) -> dict[str, str]:
    project_context = args.project_context.strip() or args.description
    agent_scope = args.agent_scope.strip() or '- Regras de negocio e operacao deste repositorio.\n- Codigo-fonte, scripts, documentacao e fluxos SDD do projeto.'
    return {
        'PROJECT_NAME': args.project_name,
        'PROJECT_SLUG': args.project_slug,
        'PROJECT_DESCRIPTION': args.description,
        'PROJECT_CONTEXT': project_context,
        'PROJECT_AGENT_SCOPE': agent_scope,
        'STACK': args.stack,
        'INSTALL_COMMAND': args.install_command,
        'TEST_COMMAND': args.test_command,
    }


def should_skip(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    parts = rel.parts
    if not parts:
        return False
    if parts[0] in EXCLUDED_TOP_LEVEL:
        return True
    return any(part in EXCLUDED_PARTS for part in parts)


def is_text_candidate(path: Path) -> bool:
    if path.name in {'.cursorrules', '.gitignore'}:
        return True
    return path.suffix.lower() in TEXT_SUFFIXES


def render_text(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace('{{' + key + '}}', value)
        text = text.replace('{{ ' + key + ' }}', value)
    return sanitize_legacy_template_refs(text)


def sanitize_legacy_template_refs(text: str) -> str:
    """Remove resíduos do nome/caminho interno do repositório template."""
    legacy_name = 'data-agentic-ai-for-' + 'pipelines'
    legacy_path = '/datalake/workspace/fabiano/' + legacy_name
    replacements = {
        legacy_name: 'template-agentic-fonte',
        legacy_path: '/path/to/template-agentic-fonte',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def iter_source_files(root: Path) -> Iterable[Path]:
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        if should_skip(path, root):
            continue
        yield path


def write_file(target: Path, content: bytes, force: bool, dry_run: bool) -> str:
    existed = target.exists()
    if existed and not force:
        return 'skip-existing'
    if dry_run:
        return 'overwrite' if existed else 'write'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)
    return 'overwrite' if existed else 'write'


def copy_template(source: Path, target: Path, values: dict[str, str], force: bool, dry_run: bool) -> dict[str, int]:
    stats = {'write': 0, 'overwrite': 0, 'skip-existing': 0}
    for source_file in iter_source_files(source):
        rel = source_file.relative_to(source)
        target_file = target / rel
        if is_text_candidate(source_file):
            text = source_file.read_text(encoding='utf-8')
            rendered = render_text(text, values).encode('utf-8')
            action = write_file(target_file, rendered, force, dry_run)
        else:
            action = write_file(target_file, source_file.read_bytes(), force, dry_run)
        stats[action] = stats.get(action, 0) + 1
    return stats


def render_agent_template(source: Path, values: dict[str, str]) -> str:
    template = source / 'templates' / 'agent-expert.md.j2'
    if not template.exists():
        raise FileNotFoundError(f'Template de agente ausente: {template}')
    return render_text(template.read_text(encoding='utf-8'), values)


def ensure_project_agent(source: Path, target: Path, values: dict[str, str], dry_run: bool) -> None:
    agent_body = render_agent_template(source, values)
    slug = values['PROJECT_SLUG']
    for base in BASES:
        path = target / base / 'agents/domain' / f'{slug}-expert.md'
        if dry_run:
            print(f'[dry-run] criar agente: {path}')
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(agent_body.replace('.cursor/sdd/', f'{base}/sdd/'), encoding='utf-8')


def ensure_router_yaml(target: Path, values: dict[str, str], dry_run: bool) -> None:
    if yaml is None:
        raise RuntimeError('PyYAML e necessario para atualizar AGENT_ROUTER.yaml')

    slug = values['PROJECT_SLUG']
    for base in BASES:
        path = target / base / 'sdd/architecture/AGENT_ROUTER.yaml'
        data = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
        agents = data.setdefault('agents', [])
        agent_id = f'{slug}-expert'
        agent_file = f'{base}/agents/domain/{agent_id}.md'
        if not any(agent.get('id') == agent_id for agent in agents if isinstance(agent, dict)):
            agents.insert(0, {
                'id': agent_id,
                'file': agent_file,
                'roster_group': 'domain_platform',
                'specialty_en': f'Especialista no projeto {values["PROJECT_NAME"]}: {values["PROJECT_DESCRIPTION"]}',
            })

        hints = data.setdefault('intake_hints', [])
        if not any(hint.get('primary_agent_id') == agent_id for hint in hints if isinstance(hint, dict)):
            hints.insert(0, {
                'signals_pt': f'{values["PROJECT_NAME"]}, {slug}, dominio do projeto, regras de negocio, execucao, troubleshooting',
                'primary_agent_id': agent_id,
                'context_paths': ['CONTEXT.md', 'README.md', agent_file],
            })

        kb_reference = data.setdefault('kb_reference', [])
        if not any(item.get('kb_domain') == values['PROJECT_NAME'] for item in kb_reference if isinstance(item, dict)):
            kb_reference.insert(0, {
                'kb_domain': values['PROJECT_NAME'],
                'path': 'CONTEXT.md',
                'used_by_agent_ids': [agent_id],
            })

        if dry_run:
            print(f'[dry-run] atualizar router yaml: {path}')
            continue
        path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=120), encoding='utf-8')


def ensure_router_md(target: Path, values: dict[str, str], dry_run: bool) -> None:
    slug = values['PROJECT_SLUG']
    agent_id = f'{slug}-expert'
    for base in BASES:
        path = target / base / 'commands/core/router.md'
        if not path.exists():
            continue
        text = path.read_text(encoding='utf-8')
        expert_block = (
            '## Agente expert do repositório\n\n'
            f'Use este agente como primário quando a solicitação for específica do domínio `{slug}`.\n\n'
            '| Campo | Valor |\n'
            '|-------|--------|\n'
            f'| **Arquivo** | `{base}/agents/domain/{agent_id}.md` |\n'
            '| **Usar quando** | Dúvidas estritamente sobre o domínio, execução, configuração, troubleshooting e arquitetura deste projeto |\n'
            f'| **Sinais típicos** | {values["PROJECT_NAME"]}, {slug}, regras de negócio, scripts, configuração, logs, troubleshooting |\n\n'
        )
        text = replace_section(text, '## Agente expert do repositório', '---', expert_block)
        domain_line = f'- `{base}/agents/domain/{agent_id}.md`'
        if domain_line not in text and '### Exploration' in text:
            text = text.replace('### Exploration', domain_line + '\n\n### Exploration', 1)
        if dry_run:
            print(f'[dry-run] atualizar router md: {path}')
            continue
        path.write_text(text, encoding='utf-8')


def replace_section(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start = text.find(start_marker)
    if start == -1:
        return text
    end = text.find(end_marker, start)
    if end == -1:
        return text[:start] + replacement
    return text[:start] + replacement + text[end:]


def remove_case_duplicates(target: Path, dry_run: bool) -> None:
    for base in BASES:
        duplicate = target / base / 'CURSOR.md'
        if duplicate.exists():
            if dry_run:
                print(f'[dry-run] remover duplicidade: {duplicate}')
            else:
                duplicate.unlink()


def run_validation(target: Path, source: Path) -> int:
    validator = source / 'scripts/validate-agentic-template.py'
    cmd = [sys.executable, str(validator), '--root', str(target), '--mode', 'project']
    completed = subprocess.run(cmd, check=False)
    return completed.returncode


def main() -> int:
    args = parse_args()
    source = source_root(args)
    target = Path(args.target).resolve()
    values = variables(args)

    if not source.exists():
        print(f'Fonte inexistente: {source}', file=sys.stderr)
        return 2
    if not target.exists():
        print(f'Destino inexistente: {target}', file=sys.stderr)
        return 2

    stats = copy_template(source, target, values, force=args.force, dry_run=args.dry_run)
    ensure_project_agent(source, target, values, dry_run=args.dry_run)
    ensure_router_yaml(target, values, dry_run=args.dry_run)
    ensure_router_md(target, values, dry_run=args.dry_run)
    remove_case_duplicates(target, dry_run=args.dry_run)

    print(f'bootstrap-agentic-project: copiados/renderizados={stats}')

    if args.dry_run or args.skip_validation:
        return 0
    return run_validation(target, source)


if __name__ == '__main__':
    raise SystemExit(main())
