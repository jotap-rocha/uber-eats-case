# dl-2026-08-18-doc-skills-kb — Requisitos

> **Gerado:** 2026-08-18 | **Fonte:** histórico desta sessão (não é reunião — extração adaptada às
> seções aplicáveis do framework `meeting-analyst`)
> **Confiança:** ALTA (0.95) — fonte é a própria conversa onde as decisões foram tomadas e
> implementadas nesta mesma sessão; sem ambiguidade de autoria.

## Executive Summary

| Aspecto | Detalhes |
|---------|----------|
| **Projeto** | Documento de referência único sobre a convenção Skill vs KB e sua integração ao SDD e ao Dev Loop |
| **Problema de negócio** | O repositório ganhou uma convenção nova (Skill vs KB) e um primeiro exemplo real (`git-boas-praticas-versionamento`) ligado aos fluxos SDD/Dev Loop, mas isso só existe espalhado em regras, agentes e histórico de conversa — falta um documento único e consultável |
| **Solução** | Consolidar em um só artefato: o critério de decisão, a mecânica de descoberta (nativa no Claude Code), o exemplo concreto construído, os pontos de integração no SDD/Dev Loop, e a portabilidade para Cursor/GitHub Copilot |
| **Prazo crítico** | Nenhum explícito |

## 1. Key Decisions (consolidado desta sessão)

| # | Decisão | Origem | Status |
|---|---------|--------|--------|
| D1 | Skill = procedimento repetível ("como fazer X"); KB = conceito/contrato ("o que é verdade sobre X") | `.claude/rules/skill-first.md` (já existente) | Aprovado |
| D2 | Skills vivem **só** em `.claude/skills/` — nunca espelhadas em `.cursor/skills/` ou `.github/skills/`; descoberta é nativa do Claude Code, diferente da KB (que É espelhada nas 3 árvores) | `.claude/rules/skill-first.md` | Aprovado |
| D3 | Criar a primeira Skill própria do projeto: `git-boas-praticas-versionamento`, com prefixo de domínio (`git-`) para não colidir com o bundle vendor Databricks/MLflow já presente em `.claude/skills/` | Turno 2 desta sessão | Implementado |
| D4 | Escopo da skill: **amplo** — inclui granularidade de commit por fase SDD/Dev Loop, Conventional Commits, estratégia de branch e regras de PR/review (mesmo havendo alguma sobreposição com `create-pr.md`, que documenta a mecânica de PR) | AskUserQuestion, resposta do usuário | Aprovado |
| D5 | Integração ativa: além do `SKILL.md`, editar os agentes existentes (`build-agent`, `ship-agent`, `dev-loop-executor`, `devloop-fixer`) para referenciarem a skill no ponto certo do fluxo, e registrar em `AGENT_ROUTER.yaml` `skill_reference` | AskUserQuestion, resposta do usuário | Aprovado e implementado |
| D6 | `AGENT_ROUTER.yaml` e os agentes `.md` são **mirror** — mesma edição replicada em `.claude/`, `.cursor/` e `.github/` (só variando o prefixo de árvore nas auto-referências) | Descoberto ao inspecionar `.claude/CLAUDE.md` ("fonte canônica é `.cursor/`") e confirmado via diff entre as três árvores | Aplicado nas 18 edições feitas |
| D7 | Regra de ouro da skill: nunca commitar/push/operação destrutiva sem autorização — em Dev Loop, `--mode afk` já é essa autorização explícita; `hitl` exige propor e aguardar confirmação | Alinhado ao Git Safety Protocol global da sessão | Documentado na skill |
| D8 | Todo o trabalho acima foi commitado num único commit (`271a2e7`, `FEAT: adicionar skill git-boas-praticas-versionamento e ligar ao SDD/Devloop`) após validação (`validate-agent-router.py` OK, `install_dev_loop.py --dry-run` sem regressão) | Turno 3 desta sessão | Concluído |

## 2. Requirements (para o documento a ser escrito)

| ID | Requisito | Tipo | Prioridade | Origem |
|----|-----------|------|------------|--------|
| FR-001 | Explicar o critério de decisão Skill vs KB (`skill-first.md`) com exemplos | Funcional | P0 | Pedido do usuário |
| FR-002 | Explicar a mecânica de descoberta: Skill é nativa/auto-descoberta só em `.claude/skills/`; KB é leitura deliberada e é espelhada nas 3 árvores | Funcional | P0 | Pedido do usuário + regra já existente |
| FR-003 | Documentar o exemplo concreto construído nesta sessão (`git-boas-praticas-versionamento`) como estudo de caso: conteúdo, registro em `AGENT_ROUTER.yaml`, pontos de integração exatos (arquivo + trecho) em `build-agent`, `ship-agent`, `dev-loop-executor`, `devloop-fixer`, `create-pr.md` | Funcional | P0 | Pedido do usuário ("o que fizemos") |
| FR-004 | **Deixar explícito que o processo foi desenhado para o Claude Code**, mas é utilizável também no **Cursor** e no **GitHub Copilot** — explicar o que é nativo de cada ferramenta e o que precisa de adaptação (ex.: Cursor não tem "Skill" nativa; Copilot usa outro mecanismo de instruções) | Funcional | **P0 — pedido explícito do usuário** | Pedido explícito do usuário |
| FR-005 | Incluir um roteiro reutilizável "como criar uma Skill nova neste repo" (passo a passo já dado ao usuário via `/intake`, nesta sessão) | Funcional | P1 | Consistência com resposta anterior desta sessão |
| FR-006 | Referenciar `AGENT_ROUTER.yaml` (`skill_reference`) como fonte única de registro de Skills próprias | Funcional | P1 | Convenção do repo |
| NFR-001 | Documento em português brasileiro, Markdown, com headers/tabelas consistentes com o padrão do repo (`docs/*.md`) | Não-funcional | P0 | Convenção do repo (`CLAUDE.md`) |
| NFR-002 | Autocontido o suficiente para ser lido sem precisar reabrir esta conversa — é um artefato para "passar adiante" | Não-funcional | P0 | Padrão já aplicado à skill (`SKILL.md`) |
| C-001 | Não reimplementar nem duplicar o conteúdo integral do `SKILL.md` — o documento referencia/resume, não substitui | Constraint | — | Evitar deriva entre fontes |

## 3. Blockers & Risks

| # | Tipo | Descrição | Impacto | Mitigação |
|---|------|-----------|---------|-----------|
| R1 | Risco | Cursor e GitHub Copilot não têm um conceito nativo idêntico a "Skill" do Claude Code — descrever a portabilidade de forma imprecisa poderia confundir quem for aplicar noutra ferramenta | MED | Documento vai diferenciar claramente **o que é mecanismo nativo do Claude Code** (auto-discovery de `.claude/skills/`) de **o que é convenção do projeto, portável por design** (KB mirror, `AGENT_ROUTER.yaml`, regras em `.claude/rules/` que também vivem em `.cursor/rules/*.mdc` e `.github/`) |

## 4. Architecture & Technical Decisions

```text
COMPONENTE: Skill (Claude Code)
+- Localização: .claude/skills/<nome>/SKILL.md (nunca mirror)
+- Descoberta: nativa via frontmatter name/description
+- Registro: AGENT_ROUTER.yaml -> skill_reference (informativo, não afeta discovery)

COMPONENTE: KB (.claude/kb, .cursor/kb, .github/kb)
+- Localização: mirrorada nas 3 árvores
+- Descoberta: leitura deliberada (Read explícito por agente/regra)
+- Registro: .claude/kb/_index.yaml

COMPONENTE: Integração SDD/Dev Loop
+- SDD: build-agent (passo 4.1 commit), ship-agent (passo 1.1 verify git state)
+- Dev Loop: dev-loop-executor (commit por tarefa hitl/afk), devloop-fixer (passo 3 commit)
+- Todos referenciam a skill por path literal `.claude/skills/.../SKILL.md`, não por link
  relativo — evita quebra ao ler a partir de .cursor/ ou .github/
```

## 5. Open Questions

| # | Pergunta | Contexto | Prioridade |
|---|----------|----------|------------|
| Q1 | Nome final do arquivo do documento e onde indexá-lo — proposta: `docs/GUIA_SKILLS_KB_SDD_DEVLOOP.md` + entrada em `docs/00-INDEX.md` | Segue o padrão de `GUIA_CRIACAO_AGENTE_PROJETO.md`, `DEV_LOOP_Guia_Comandos.md` já existentes em `docs/`/`get_started/` | MED — decidir na fase `design` |

## 6. Next Steps

```text
IMEDIATO (esta execução):
1. design — the-planner define estrutura final, seções e path do documento
2. craft — prompt-crafter gera PROMPT_dl-2026-08-18-doc-skills-kb.md
3. prompt_review — aprovação humana explícita
4. execute — /dev escreve o documento
5. reflect — DEVLOOP_SUMMARY.md
```

## 7. Metrics & Success Criteria

| Métrica | Alvo |
|---------|------|
| FR-001..FR-006 cobertos no documento final | 6/6 |
| Documento lido de forma autocontida (sem depender desta conversa) | Sim |
| Seção de portabilidade Cursor/Copilot presente e tecnicamente correta | Sim |

---

**Seções N/A para este RUN** (fonte não é reunião/comunicação multi-pessoa): *Action Items com owners*,
*Implicit Signals & Sentiment*, *Stakeholders & Roles/RACI* — não há múltiplos participantes/atribuições
de pessoas a extrair; todas as decisões acima têm um único "owner" (esta sessão de trabalho).
