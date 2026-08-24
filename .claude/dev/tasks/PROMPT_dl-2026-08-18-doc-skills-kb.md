# PROMPT: dl-2026-08-18-doc-skills-kb

> Gerado por prompt-crafter (via /devloop-phase craft) a partir de:
> `.claude/sdd/dev-loop-runs/dl-2026-08-18-doc-skills-kb/artifacts/dl-2026-08-18-doc-skills-kb_requirements.md`
> `.claude/sdd/dev-loop-runs/dl-2026-08-18-doc-skills-kb/artifacts/dl-2026-08-18-doc-skills-kb_design.md`

---

## Goal

Produzir `docs/GUIA_SKILLS_KB_SDD_DEVLOOP.md` — documento completo, autocontido, em pt-BR, cobrindo
a convenção Skill vs KB, o estudo de caso `git-boas-praticas-versionamento`, a integração ao SDD e
ao Dev Loop, um roteiro reutilizável de criação de Skill, e a portabilidade honesta entre Claude
Code, Cursor e GitHub Copilot — e indexá-lo em `docs/00-INDEX.md`.

---

## Quality Tier

**Tier:** production

| Tier | Expectations |
|------|--------------|
| `prototype` | Speed over perfection. Skip edge cases. Minimal tests. |
| `production` | Tests required. Best practices. Full verification. |
| `library` | Backward compatibility. Full documentation. API stability. |

---

## Context

Documentação pura — nenhum código de aplicação é alterado. As fontes de verdade a citar/consultar
já existem no repo (não recriar, apenas referenciar):

- `.claude/rules/skill-first.md` — critério de decisão Skill vs KB
- `.claude/skills/git-boas-praticas-versionamento/SKILL.md` — a skill construída nesta sessão
- `.claude/sdd/architecture/AGENT_ROUTER.yaml` (`skill_reference`, ~linha 612) — registro
- `.claude/agents/workflow/build-agent.md` (seção "4.1 Commit Progress")
- `.claude/agents/workflow/ship-agent.md` (seção "1.1 Verify Git State")
- `.claude/agents/dev/dev-loop-executor.md` (pseudocódigo + seção "Commits During Execution")
- `.claude/agents/workflow-dev-loop/devloop-fixer.md` (passo 3 "Commitar a correção")
- `.claude/commands/workflow/create-pr.md` (nota de cross-reference no topo)
- Commit `271a2e7` — `FEAT: adicionar skill git-boas-praticas-versionamento e ligar ao SDD/Devloop`
- Todas as edições acima existem replicadas em `.claude/`, `.cursor/` e `.github/` (mirror) — o
  documento deve mencionar isso, mas os exemplos de código/trecho no documento citam só o path
  `.claude/...` (é o path literal usado nas próprias referências cruzadas do repo, ver
  `.claude/rules/skill-first.md`).

Estrutura completa (10 seções) e o conteúdo pré-validado da seção de portabilidade estão em
`artifacts/dl-2026-08-18-doc-skills-kb_design.md` §3 e §4 — **usar esse conteúdo como base direta
da seção 9**, não reinventar a tabela de equivalências.

---

## Agentes (Dev Loop Executor)

Nenhuma delegação a agente especialista é necessária — decisão registrada em
`artifacts/dl-2026-08-18-doc-skills-kb_design.md` §5 ("redação direta a partir do design já
validado"). Todas as tarefas abaixo são diretas (sem prefixo `@`).

---

## Tasks (Prioritized)

### 🔴 RISKY (Do First)

- [x] Escrever `docs/GUIA_SKILLS_KB_SDD_DEVLOOP.md` completo, seguindo **exatamente** a estrutura
  de 10 seções definida em `artifacts/dl-2026-08-18-doc-skills-kb_design.md` §3:
  1. Por que este documento existe
  2. Duas fontes de conhecimento: Skill vs KB (2.1 critério `skill-first.md`; 2.2 tabela
     comparativa descoberta/localização/mirror/quando usar)
  3. Como a descoberta funciona (mecanismo nativo do Claude Code — Skill por `description` no
     frontmatter, automática; KB é leitura deliberada)
  4. Estudo de caso: `git-boas-praticas-versionamento` (4.1 o que cobre; 4.2 onde vive + registro
     em `AGENT_ROUTER.yaml` `skill_reference`)
  5. Integração ao SDD (5.1 build-agent passo 4.1; 5.2 ship-agent passo 1.1) — citar arquivo e
     trecho real, não paráfrase genérica
  6. Integração ao Dev Loop (6.1 dev-loop-executor commit por tarefa hitl vs afk; 6.2
     devloop-fixer passo 3)
  7. Relação com `create-pr.md` (o que cada um cobre, sem duplicar)
  8. Como criar uma Skill nova neste repositório — roteiro reutilizável (critério de decisão,
     nome com prefixo de domínio, local `.claude/skills/` apenas, uso do skill-creator, registro
     em `AGENT_ROUTER.yaml`, validação)
  9. Portabilidade: Claude Code, Cursor e GitHub Copilot — usar **diretamente** a tabela e a
     conclusão de `design.md` §4 (mecanismo nativo real vs convenção do projeto; limitações
     honestas — não prometer paridade automática que não existe)
  10. Referências e changelog desta sessão (lista de arquivos tocados + commit `271a2e7`)

  Verify: `test -f docs/GUIA_SKILLS_KB_SDD_DEVLOOP.md`

### 🟡 CORE

- [x] Adicionar entrada para o novo documento em `docs/00-INDEX.md`, seção "Guias do projeto"
  (mesmo padrão das entradas existentes, ex. `GUIA_CRIACAO_AGENTE_PROJETO.md`)
  Verify: `grep -q "GUIA_SKILLS_KB_SDD_DEVLOOP" docs/00-INDEX.md`

### 🟢 POLISH (Do Last)

- [x] Revisar auto-contenção: nenhuma frase do tipo "nesta sessão"/"conversamos" sem contexto
  suficiente para quem lê o documento pela primeira vez sem ter visto a conversa original
  (verificação manual — sem comando objetivo)

---

## Exit Criteria

- [x] Documento existe: `test -f docs/GUIA_SKILLS_KB_SDD_DEVLOOP.md`
- [x] Indexado: `grep -q "GUIA_SKILLS_KB_SDD_DEVLOOP" docs/00-INDEX.md`
- [x] Agent router validates: `python3 scripts/validate-agent-router.py`
- [x] Dev Loop installer dry-run succeeds: `python3 install_dev_loop/install_dev_loop.py --dry-run --target .`
- [x] Documento cobre as 10 seções da estrutura definida em `design.md` §3 (checagem manual)

---

## Progress

**Status:** COMPLETE

| Iteration | Timestamp | Task Completed | Key Decision | Files Changed |
|-----------|-----------|----------------|--------------|---------------|
| 1 | 2026-08-18T00:15:30Z | Escrever documento | Seção 9 usa conteúdo pré-validado do design | `docs/GUIA_SKILLS_KB_SDD_DEVLOOP.md` |
| 2 | 2026-08-18T00:16:10Z | Indexar | Padrão da tabela "Guias do projeto" | `docs/00-INDEX.md` |
| 3 | 2026-08-18T00:16:40Z | Revisão de auto-contenção | Sem mudanças necessárias | — |

---

## Config

```yaml
mode: hitl                # hitl (human-in-loop) | afk (autonomous)
quality_tier: production
max_iterations: 10
max_retries: 3
circuit_breaker: 3
small_steps: true
feedback_loops:
  - python3 scripts/validate-agent-router.py
  - python3 install_dev_loop/install_dev_loop.py --dry-run --target .
```

---

## Notes

- Requisito de maior prioridade do usuário: deixar explícito que o processo foi **desenhado para
  o Claude Code**, mas é **usável no Cursor e no GitHub Copilot** — isso é a Task 🔴 RISKY, seção 9,
  e não pode ficar diluído ou genérico.
- Constraint: não duplicar o conteúdo integral do `SKILL.md` — o documento resume/referencia.
- `mode: hitl` porque é conteúdo textual de julgamento editorial (não código com verificação
  puramente objetiva); revisão humana entre tarefas é apropriada.

---

## References

- `.claude/sdd/dev-loop-runs/dl-2026-08-18-doc-skills-kb/artifacts/dl-2026-08-18-doc-skills-kb_requirements.md`
- `.claude/sdd/dev-loop-runs/dl-2026-08-18-doc-skills-kb/artifacts/dl-2026-08-18-doc-skills-kb_design.md`
