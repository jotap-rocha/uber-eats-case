# BUILD REPORT: Integração Skill ↔ KB (SDD, Dev Loop, vibecoding)

**Input:** `.claude/sdd/features/DESIGN_skill-kb-integration.md`
**Data:** 2026-08-17

## Resumo

14/14 arquivos do manifesto criados/editados com sucesso. Todos os 5 Acceptance Tests do
`DEFINE_skill-kb-integration.md` passaram na verificação objetiva. Nenhum bloqueio.

## Tasks Executadas

| # | File | Action | Status |
|---|------|--------|--------|
| 1 | `.cursor/rules/skill-first.mdc` | Create | ✅ |
| 2 | `.claude/rules/skill-first.md` | Create | ✅ |
| 3 | `.claude/rules/skill-first.mdc` | Create | ✅ |
| 4 | `.github/rules/skill-first.md` | Create | ✅ |
| 5 | `.github/rules/skill-first.mdc` | Create | ✅ |
| 6 | `.cursor/sdd/architecture/AGENT_ROUTER.yaml` | Edit | ✅ |
| 7 | `.claude/sdd/architecture/AGENT_ROUTER.yaml` | Edit | ✅ |
| 8 | `.github/sdd/architecture/AGENT_ROUTER.yaml` | Edit | ✅ |
| 9 | `.cursor/agents/workflow/brainstorm-agent.md` | Edit | ✅ |
| 10 | `.claude/agents/workflow/brainstorm-agent.md` | Edit | ✅ |
| 11 | `.github/agents/workflow/brainstorm-agent.md` | Edit | ✅ |
| 12 | `.cursor/agents/workflow/design-agent.md` | Edit | ✅ |
| 13 | `.claude/agents/workflow/design-agent.md` | Edit | ✅ |
| 14 | `.github/agents/workflow/design-agent.md` | Edit | ✅ |

## Desvio do plano (registrado durante execução, não durante design)

Os 2 primeiros `Edit` em `.cursor/agents/workflow/brainstorm-agent.md` e
`.github/agents/workflow/brainstorm-agent.md` falharam na primeira tentativa: o `old_string`
copiado do DESIGN assumia `.claude/CURSOR.MD`/`.claude/kb/_index.yaml`, mas esses mirrors usam o
prefixo próprio (`.cursor/CURSOR.MD`, `.github/kb/_index.yaml`). Corrigido na segunda tentativa
lendo o conteúdo real de cada arquivo antes de editar — comportamento esperado do padrão de
espelho (path muda, conteúdo estrutural é o mesmo), documentado aqui para não repetir a suposição
em builds futuros.

## Verificação (Testing Strategy do DESIGN)

| Test | Comando | Resultado |
|------|---------|-----------|
| AT-001 — 5 arquivos de rule existem | `ls .cursor/rules/skill-first.mdc .claude/rules/skill-first.{md,mdc} .github/rules/skill-first.{md,mdc}` | ✅ 5/5 listados |
| AT-002 — schema do router | `python scripts/validate-agent-router.py` | ✅ `OK (77 agentes, 32 hints)` |
| AT-002 — `skill_reference` presente 1x cada | `grep -c "^skill_reference:" <3 arquivos>` | ✅ 1, 1, 1 |
| AT-003 — brainstorm-agent cita Skills | `grep -l "SKILL.md" <3 mirrors>` | ✅ 3/3 |
| AT-004 — design-agent cita Skills | `grep -l "Skills disponíveis" <3 mirrors>` | ✅ 3/3 |
| AT-005 — nenhuma migração de KB | `git status --short -- '*/kb/*'` | ✅ vazio |

`git status` completo conferido: só os 14 arquivos do manifesto aparecem como `M`/`??`
relacionados a esta feature (mais os 3 documentos SDD desta mesma feature). Nenhum arquivo fora
do escopo foi tocado.

## Out of Scope confirmado (do DEFINE)

- Nenhuma migração de conteúdo de `.claude/kb/` para `.claude/skills/`
- Nenhuma validação nova em `scripts/validate-agent-router.py`
- Nenhuma edição nas fases do Dev Loop (`devloop-*.md`)
- Nenhuma estrutura de subpasta dedicada em `.claude/skills/`
- Nenhum campo de roteamento novo no `/intake`

## Rodada de correção pós-build (achada por verificação independente, antes do /ship)

Após o build inicial, o usuário pediu como validar se os processos realmente consideram
`.claude/skills/` antes do `/ship`. Em vez de só responder, disparei `@kb-architect` e
`@agent-architect` para uma verificação independente (fresh eyes, sem confiar nos relatórios
acima) dos 14 arquivos. Dois defeitos reais foram encontrados e corrigidos nesta rodada:

1. **Frontmatter ausente** em `.claude/rules/skill-first.md` e `.github/rules/skill-first.md` —
   quebrava o padrão que todo `.md` em `.claude/rules/`/`.github/rules/` replica o frontmatter do
   `.mdc` irmão (confirmado comparando com `app-security-kb.md`, que TEM frontmatter — o
   pressuposto inicial de que era "markdown puro" estava errado). **Corrigido**: frontmatter
   `description`/`globs`/`alwaysApply` adicionado aos 2 arquivos.
2. **Paths incorretos apontando para Skills "por mirror"** — a regra `skill-first` e o comentário
   de `skill_reference` em `.cursor/AGENT_ROUTER.yaml`/`.github/AGENT_ROUTER.yaml` sugeriam que
   novas Skills deveriam ir para `.cursor/skills/<nome>/SKILL.md` / `.github/skills/<nome>/SKILL.md`
   — só que **Skill não é espelhada por ferramenta como a KB é**: o Claude Code só descobre Skills
   em `.claude/skills/` (confirmado: `.claude/skills/` tem 41 skills completas, `.cursor/skills/`
   tem 39 — mirror manual incompleto que não é o que o harness escaneia — e `.github/skills/`
   **não existe**). O `Glob(.claude/skills/*/SKILL.md)` hardcoded nos 6 arquivos de agente
   (`brainstorm-agent.md`/`design-agent.md` × 3 mirrors) estava **certo desde o início** — o erro
   estava nas 5 rules + 2 comentários de router, que foram **corrigidos** para sempre apontar
   `.claude/skills/`, com nota explícita explicando o motivo (para não repetir a confusão).

Os dois agentes de verificação também confirmaram como não-problemas: `.claude/kb/` continua
intocado; `skill_reference` tem formato coerente com `kb_reference` nos 3 `AGENT_ROUTER.yaml`;
os arquivos de comando (`router.md`, `brainstorm.md`, `design.md`) não citam Skill diretamente,
mas isso é escopo intencional (eles referenciam os arquivos de agente, que sim citam).

Achado importante e **não corrigível por código**: não existe forma de validar automaticamente se
um agente LLM, numa execução real, de fato lê `.claude/skills/` antes de propor conteúdo de KB —
isso é comportamento em tempo de execução guiado por instrução em prosa, sem hook de CI. A única
validação possível para esse comportamento específico é um teste manual/observacional (rodar
`/brainstorm` numa feature descartável e observar a transcrição).

**Reverificação pós-fix:** frontmatter presente nos 5 rule files, `validate-agent-router.py`
continua `OK (77 agentes, 32 hints)`, nenhuma referência incorreta de path remanescente.

## Próximo passo

`.claude/sdd/features/DEFINE_skill-kb-integration.md` deve ser atualizado para
`✅ Complete (Built)` e o próximo comando é `/ship .claude/sdd/features/DEFINE_skill-kb-integration.md`.

## Status: ✅ Build Complete (com 1 rodada de correção pós-verificação independente)
