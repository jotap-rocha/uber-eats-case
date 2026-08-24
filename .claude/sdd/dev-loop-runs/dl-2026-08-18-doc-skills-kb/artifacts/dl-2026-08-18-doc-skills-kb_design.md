# dl-2026-08-18-doc-skills-kb — Design

> Baseado em: `artifacts/dl-2026-08-18-doc-skills-kb_requirements.md` (FR-001..FR-006, NFR-001/002,
> C-001, R1, Q1). Papel adotado: `the-planner` (adaptado — "Document Architecture", não sistema de
> software).

## 1. Overview

| Item | Detalhes |
|------|----------|
| **Propósito** | Documento único, autocontido, que explica a convenção Skill vs KB e como ela foi implementada e ligada ao SDD e ao Dev Loop nesta sessão |
| **Escopo** | Convenção Skill vs KB · estudo de caso `git-boas-praticas-versionamento` · pontos de integração exatos no SDD/Dev Loop · roteiro "como criar uma Skill" · portabilidade Claude Code / Cursor / GitHub Copilot |
| **Fora de escopo** | Reescrever o conteúdo integral do `SKILL.md` (apenas referenciar) · qualquer nova implementação de código · KB de domínio técnico (Spark, Databricks etc.) |
| **Constraint (C-001)** | Documento resume e referencia, não duplica, o `SKILL.md` |

## 2. Decisão de local e indexação (resolve Q1)

| Decisão | Escolha | Alternativas rejeitadas |
|---------|---------|---------------------------|
| Path do documento | `docs/GUIA_SKILLS_KB_SDD_DEVLOOP.md` | `.claude/sdd/dev-loop-runs/.../artifacts/` (rejeitado: artefato do RUN é temporário/interno, não é para consulta pública); `get_started/` (rejeitado: `get_started/` é onboarding de primeiro contato, este documento é referência aprofundada pós-onboarding) |
| Indexação | Nova linha em `docs/00-INDEX.md`, seção "Guias do projeto" | — |
| Convenção de nome | `GUIA_*` maiúsculo, consistente com `GUIA_CRIACAO_AGENTE_PROJETO.md`, `DEV_LOOP_Guia_Comandos.md` já existentes | — |

## 3. Estrutura final do documento (Table of Contents)

```text
# Skills + KB — Integração ao SDD e ao Dev Loop

1. Por que este documento existe
2. Duas fontes de conhecimento: Skill vs KB
   2.1 Critério de decisão (skill-first.md)
   2.2 Tabela comparativa (descoberta, localização, mirror, quando usar)
3. Como a descoberta funciona (mecanismo nativo do Claude Code)
4. Estudo de caso: a skill git-boas-praticas-versionamento
   4.1 O que ela cobre
   4.2 Onde vive e como foi registrada (AGENT_ROUTER.yaml skill_reference)
5. Integração ao SDD (Fases 3 e 4)
   5.1 build-agent — passo 4.1 Commit Progress
   5.2 ship-agent — passo 1.1 Verify Git State
6. Integração ao Dev Loop
   6.1 dev-loop-executor — commit por tarefa (hitl vs afk)
   6.2 devloop-fixer — passo 3 Commitar a correção
7. Relação com create-pr.md (sem duplicar conteúdo)
8. Como criar uma Skill nova neste repositório (roteiro reutilizável)
9. Portabilidade: Claude Code, Cursor e GitHub Copilot
   9.1 O que é mecanismo nativo vs convenção deste projeto
   9.2 Tabela de equivalências
   9.3 Limitações honestas (o que NÃO é automático hoje)
10. Referências e changelog desta sessão
```

Mapeamento requisito → seção: FR-001→§2, FR-002→§2.2/§3, FR-003→§4-6, FR-004→§9 (P0),
FR-005→§8, FR-006→§4.2. NFR-001/002 aplicam ao documento inteiro.

## 4. Conteúdo pré-validado da §9 (Portabilidade) — mitiga R1

Levantamento feito nesta fase de design para não deixar a seção mais sensível (R1: risco de
overclaim de portabilidade) para inferência na hora do craft:

| Ferramenta | Mecanismo nativo mais próximo de "Skill" | Descoberta | Estado real neste repo |
|------------|-------------------------------------------|-------------|--------------------------|
| **Claude Code** | Skill (`SKILL.md`) | Automática, por `description` no frontmatter | Nativo — é para onde a skill nova foi escrita (`.claude/skills/`) |
| **Cursor** | Project Rules (`.cursor/rules/*.mdc`), modo "Agent Requested" (usa `description` para decidir quando incluir) | Semiautomática — análoga em espírito à Skill, mas é outro mecanismo (regra, não "skill") | `.cursor/skills/` existe hoje só como **mirror do bundle vendor** (Databricks/MLflow), não é descoberta nativa do Cursor; não é onde Skills próprias do projeto devem ir (`skill-first.md`) |
| **GitHub Copilot** | `.github/copilot-instructions.md` (sempre incluído) + `.github/instructions/*.instructions.md` (`applyTo` por glob) + prompt files (`.github/prompts/*.prompt.md`, invocação manual) | Instruções: automática por path/sempre-on. Prompt files: manual (equivalente a slash command) | `.github/copilot-instructions.md` já existe neste repo — hoje é um **ponteiro fino** ("fonte canônica é `.cursor/`, use `.github/` como espelho"), não replica o conteúdo da skill automaticamente |

**Conclusão honesta para §9.3:** o que é **de fato automático** é só a descoberta nativa de Skill no
Claude Code. Para Cursor e Copilot, a "portabilidade" hoje é **o conteúdo estar disponível** (mirror
manual de `AGENT_ROUTER.yaml` e dos agentes `.md` nas três árvores, mais os arquivos de entrada
`.cursorrules` / `.github/copilot-instructions.md`), não uma migração automática do mecanismo de
Skill em si. O documento deve dizer isso claramente, sem prometer paridade que não existe.

## 5. Task Breakdown (para a fase `craft`)

| # | Prioridade | Tarefa | Agente | Verificação |
|---|------------|--------|--------|-------------|
| T1 | 🔴 RISKY | Escrever `docs/GUIA_SKILLS_KB_SDD_DEVLOOP.md` completo seguindo a estrutura da §3, usando o conteúdo pré-validado da §4 para a seção 9 | (direto) | `test -f docs/GUIA_SKILLS_KB_SDD_DEVLOOP.md` |
| T2 | 🟡 CORE | Adicionar entrada em `docs/00-INDEX.md` (seção "Guias do projeto") apontando para o novo documento | (direto) | `grep -q "GUIA_SKILLS_KB_SDD_DEVLOOP" docs/00-INDEX.md` |
| T3 | 🟢 POLISH | Revisão de auto-contenção: nenhuma referência a "esta conversa"/"nesta sessão" sem contexto suficiente para quem lê pela primeira vez | (direto) | Revisão manual (sem comando de verificação objetivo) |

Sem necessidade de delegação a agente especialista (`@agent`) — é redação direta a partir do design
já validado; `python-developer`, `test-generator` etc. não se aplicam a este RUN.

## 6. Riscos (herdados + mitigação aplicada)

| # | Risco | Mitigação |
|---|-------|-----------|
| R1 | Overclaim de portabilidade Cursor/Copilot | Resolvido nesta fase — §4 acima já é o texto-base da seção 9.3, com limitações explícitas |

## 7. Success Criteria

Idêntico a `requirements.md` §7 — FR-001..FR-006 cobertos, documento autocontido, seção 9 tecnicamente precisa (validada nesta fase).

## Next Steps

```text
1. craft — prompt-crafter gera PROMPT_dl-2026-08-18-doc-skills-kb.md a partir deste design (T1-T3)
2. prompt_review — aprovação humana explícita
3. execute — /dev escreve docs/GUIA_SKILLS_KB_SDD_DEVLOOP.md + atualiza docs/00-INDEX.md
4. reflect — DEVLOOP_SUMMARY.md
```
