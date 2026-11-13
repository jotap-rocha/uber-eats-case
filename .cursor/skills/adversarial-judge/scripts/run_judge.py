#!/usr/bin/env python3
"""Chama um modelo via OpenRouter para contestar um artefato de plano (grill/PRD).

Stdlib only -- sem dependencia pip, mesmo padrao do install_harness.py deste canonico.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = (
    "Voce e um revisor adversarial (segundo modelo, opiniao independente) de um plano de "
    "projeto de software. Seu unico trabalho e achar problema, nao validar. Leia o artefato "
    "abaixo e devolva uma critica estruturada e especifica -- nao elogios, nao resumo:\n\n"
    "1. Suposicoes nao verificadas ou provavelmente erradas\n"
    "2. Lacunas -- o que o plano nao cobre mas deveria\n"
    "3. Alternativas mais simples ou mais robustas que nao foram consideradas\n"
    "4. Riscos concretos (tecnicos, de seguranca, de escopo) que o plano ignora\n\n"
    "Seja direto e especifico -- cite a secao do artefato que voce esta contestando. Se o "
    "plano estiver genuinamente solido em algum ponto, diga em uma linha e siga adiante; nao "
    "gaste espaco validando o que ja esta bom."
)


def load_env_value(key: str) -> str | None:
    """Le uma env var; se ausente, tenta um .env (KEY=VALUE) na raiz do repo atual."""
    import os

    if os.environ.get(key):
        return os.environ[key]
    env_path = Path(".env")
    if not env_path.exists():
        return None
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line.startswith(f"{key}=") and not line.startswith("#"):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--artifact", required=True, help="Path do artefato a contestar (ex.: 01-grill.md)"
    )
    parser.add_argument(
        "--output", required=True, help="Path do arquivo de saida com a critica"
    )
    args = parser.parse_args()

    api_key = load_env_value("OPENROUTER_API_KEY")
    if not api_key:
        print(
            "OPENROUTER_API_KEY nao configurada (nem no ambiente, nem em .env). "
            "Crie uma em https://openrouter.ai/keys e exporte antes de rodar.",
            file=sys.stderr,
        )
        return 1

    model = load_env_value("OPENROUTER_JUDGE_MODEL")
    if not model:
        print(
            "OPENROUTER_JUDGE_MODEL nao configurada. Escolha um modelo em "
            "https://openrouter.ai/models e exporte "
            "(ex.: export OPENROUTER_JUDGE_MODEL=fornecedor/nome-do-modelo).",
            file=sys.stderr,
        )
        return 1

    artifact_path = Path(args.artifact)
    if not artifact_path.exists():
        print(f"Artefato nao encontrado: {artifact_path}", file=sys.stderr)
        return 1
    content = artifact_path.read_text()

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Artefato ({artifact_path.name}):\n\n{content}"},
        ],
    }
    req = urllib.request.Request(
        OPENROUTER_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        print(f"OpenRouter retornou erro {e.code}: {body}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"Falha de rede chamando OpenRouter: {e}", file=sys.stderr)
        return 1

    try:
        critique = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        print(f"Resposta inesperada da OpenRouter: {json.dumps(data)[:500]}", file=sys.stderr)
        return 1

    output_path = Path(args.output)
    output_path.write_text(
        f"# Revisão adversarial — {artifact_path.name}\n\n"
        f"> Gerada via OpenRouter (`{model}`) — consultivo, não bloqueante. "
        f"Você decide o que incorporar.\n\n{critique}\n"
    )
    print(critique)
    return 0


if __name__ == "__main__":
    sys.exit(main())
