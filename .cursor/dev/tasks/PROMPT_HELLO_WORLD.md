# PROMPT: HELLO_WORLD

> Primeiro PROMPT especifico deste repositorio para validar o Dev Loop no ecossistema Cursor sem depender de uma aplicacao externa.

---

## Goal

Criar uma nota de smoke test em `.cursor/dev/examples/HELLO_WORLD_RUN.md` e validar que os comandos nativos do repositório continuam funcionando.

---

## Quality Tier

**Tier:** production

---

## Context

Este repositório é um template/kit de agentes e workflows para Cursor, Claude Code e GitHub Copilot. A raiz não possui manifesto de aplicação (`pyproject.toml`, `package.json`, `Makefile`) nem suite de testes própria; os comandos de verificação disponíveis hoje são:

- `python3 scripts/validate-agent-router.py` para validar o roteador de agentes.
- `python3 install_dev_loop/install_dev_loop.py --dry-run --target .` para validar o instalador do Dev Loop sem alterar o projeto.

---

## Agentes (Dev Loop Executor)

| Etapa / necessidade | Agente (papel) | Caminho |
|---------------------|----------------|---------|
| Confirmar comandos e contexto do repo | dev-loop-executor | `@.cursor/agents/dev/dev-loop-executor.md` |
| Ajustar documentação curta | code-documenter | `@.cursor/agents/code-quality/code-documenter.md` |
| Revisar consistencia final | code-reviewer | `@.cursor/agents/code-quality/code-reviewer.md` |

---

## Tasks (Prioritized)

### 🔴 RISKY (Do First)

- [ ] `@.cursor/agents/dev/dev-loop-executor.md` — Confirmar que o repositório continua sem suite de teste de aplicação e usar apenas verificações nativas do kit. Verify: `python3 scripts/validate-agent-router.py`

### 🟡 CORE

- [ ] `@.cursor/agents/code-quality/code-documenter.md` — Criar ou atualizar `.cursor/dev/examples/HELLO_WORLD_RUN.md` com objetivo, comandos executados, resultado esperado e próximo comando `/dev`. Verify: `test -f .cursor/dev/examples/HELLO_WORLD_RUN.md`
- [ ] `@.cursor/agents/dev/dev-loop-executor.md` — Validar o instalador do Dev Loop em modo dry-run. Verify: `python3 install_dev_loop/install_dev_loop.py --dry-run --target .`

### 🟢 POLISH (Do Last)

- [ ] `@.cursor/agents/code-quality/code-reviewer.md` — Revisar se a nota criada usa caminhos relativos corretos e não introduz segredo, dependência ou comando destrutivo. Verify: `python3 scripts/validate-agent-router.py`

---

## Exit Criteria

- [ ] Nota de smoke test existe: `test -f .cursor/dev/examples/HELLO_WORLD_RUN.md`
- [ ] Roteador de agentes valida: `python3 scripts/validate-agent-router.py`
- [ ] Instalador Dev Loop valida em dry-run: `python3 install_dev_loop/install_dev_loop.py --dry-run --target .`

---

## Progress

**Status:** NOT_STARTED

| Iteration | Timestamp | Task Completed | Key Decision | Files Changed |
|-----------|-----------|----------------|--------------|---------------|
| - | - | - | - | - |

---

## Config

```yaml
mode: hitl
quality_tier: production
max_iterations: 10
max_retries: 2
circuit_breaker: 3
small_steps: true
feedback_loops:
  - python3 scripts/validate-agent-router.py
  - python3 install_dev_loop/install_dev_loop.py --dry-run --target .
```

---

## Notes

Este PROMPT serve como primeiro exercício seguro do Dev Loop neste projeto: ele altera apenas documentação em `.cursor/dev/examples/` e usa comandos de validação já presentes no repositório.

---

## References

- [Dev Loop Documentation](../_index.md)
- [PROMPT Template](../templates/PROMPT_TEMPLATE.md)
- [Dev Loop Executor](../../agents/dev/dev-loop-executor.md)
