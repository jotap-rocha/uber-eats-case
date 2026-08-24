# Design — dl-2026-08-17-get-started

> **Fase:** design (Dev Loop L2) · **Agente:** the-planner
> **Requirements:** [`dl-2026-08-17-get-started_requirements.md`](dl-2026-08-17-get-started_requirements.md) (FR-001 a FR-008)
> **Confidence:** 0.90 (STANDARD) — requisitos claros e completos; risco residual é volume/repetição, não ambiguidade.

---

## 1. Overview

- **Propósito:** Executar a reorganização especificada em requirements — mover 10 `.md` da raiz para `get_started/`, corrigir todos os links afetados (raiz, `docs/`, os próprios arquivos movidos, mirrors `.cursor/`/`.claude/`/`.github/`) e os 3 scripts de tooling com paths hardcoded, terminando com ressincronização do bundle do instalador.
- **Escopo:** Puramente estrutural/textual (mover arquivos + editar referências). Sem lógica nova, sem dependências externas, sem decisão de arquitetura de sistema — por isso plano é uma **sequência de tarefas mecânicas verificáveis**, não uma arquitetura de componentes.
- **Constraints:** Reversível via git (usar `git mv` para preservar histórico); não tocar conteúdo além de paths/links; não tocar `.claude/worktrees/**`, `install_dev_loop/**` (exceto regenerar 2 assets via script), `agentspec/**`, `templates/*-generico.md` (fora de escopo — requirements seção 3).

---

## 2. Estratégia de execução

Ordem sequencial obrigatória — cada fase depende da anterior porque as fases 2-6 assumem que os arquivos já estão em `get_started/` para que os greps de verificação façam sentido:

```
FASE 1: Mover arquivos (FR-001)
   │
   ├──> FASE 2: Corrigir links — raiz (FR-003)
   ├──> FASE 3: Corrigir links — docs/00-INDEX.md (FR-004)
   ├──> FASE 4: Corrigir links — dentro dos arquivos movidos (FR-005)
   ├──> FASE 5: Corrigir links — mirrors .cursor/.claude/.github (FR-006)
   └──> FASE 6: Criar índice get_started/README.md + link a partir da raiz (FR-002)
                  │
                  ▼
        FASE 7: Corrigir scripts de tooling (FR-007)
                  │
                  ▼
        FASE 8: Ressincronizar bundle do instalador (FR-008)
                  │
                  ▼
        FASE 9: Verificação final (grep de saída + scripts de validação)
```

Fases 2-6 são independentes entre si (podem ser feitas em qualquer ordem relativa, todas dependem só da Fase 1) — no craft, serão tarefas sequenciais numeradas para rastreabilidade, mas sem dependência cruzada entre elas.

---

## 3. Tarefas planejadas (base para o craft)

| # | Tarefa | Prioridade | Depende de | Verificação objetiva |
|---|--------|-----------|------------|----------------------|
| T1 | Criar `get_started/` e mover os 10 arquivos com `git mv` (lista completa em requirements §1.2) | 🔴 crítico | — | `git status` mostra 10 renames `R` para `get_started/<arquivo>`; `ls get_started/` lista os 10 arquivos; `ls *.md` na raiz mostra só `README.md`, `CLAUDE.md`, `CONTEXT.md` |
| T2 | Atualizar `README.md` (raiz): link `START_HERE.md` → `get_started/START_HERE.md`; texto `SDD_Guia_Comandos.md` → `get_started/SDD_Guia_Comandos.md`; adicionar linha apontando para `get_started/README.md` | 🔴 crítico | T1 | `grep -n "START_HERE\|SDD_Guia_Comandos\|get_started" README.md` mostra os 3 caminhos atualizados |
| T3 | Atualizar `CONTEXT.md` (raiz): `START_HERE.md`, `DEV_LOOP_Guia_Comandos.md`, `SDD_Guia_Comandos.md` → prefixo `get_started/` | 🔴 crítico | T1 | `grep -n "get_started/" CONTEXT.md` retorna 3 linhas |
| T4 | Atualizar `docs/00-INDEX.md`: 5 links (`../START_HERE.md`, `../DEV_LOOP_Guia_Comandos.md`, `../SDD_Guia_Comandos.md`, `../HOW_TO_USE_AGENTS.md`, `../AGENTIC_UPGRADE_Guia.md`) → inserir `get_started/` após `../` | 🔴 crítico | T1 | `grep -n "\.\./get_started/" docs/00-INDEX.md` retorna 5 linhas; `grep -nE "\.\./(START_HERE|DEV_LOOP_Guia_Comandos|SDD_Guia_Comandos|HOW_TO_USE_AGENTS|AGENTIC_UPGRADE_Guia)\.md" docs/00-INDEX.md` retorna vazio |
| T5 | Corrigir links de saída em `get_started/DEV_LOOP_Guia_Comandos.md` (10 alvos, ver requirements FR-005) — adicionar `../` antes de `.cursor/...` | 🔴 crítico | T1 | `grep -n "](\.\./\.cursor" get_started/DEV_LOOP_Guia_Comandos.md` cobre os alvos; `grep -n "](\.cursor" get_started/DEV_LOOP_Guia_Comandos.md` retorna vazio (sem `../` restante) |
| T6 | Corrigir links de saída em `get_started/AGENTIC_UPGRADE_Guia.md` (7 alvos: `agentspec/`, `docs/`, `.cursor/kb/...`) | 🔴 crítico | T1 | `grep -nE "\]\((agentspec|docs|\.cursor)/" get_started/AGENTIC_UPGRADE_Guia.md` — todos com `../` prefixado |
| T7 | Corrigir links de saída em `get_started/HOW_TO_USE_AGENTS.md` (17 alvos: `.cursor/...`, `.claude/CLAUDE.md`, `CLAUDE.md`→`../CLAUDE.md`, `.github/copilot-instructions.md`, `.cursorrules`→`../.cursorrules`, `CONTEXT.md`→`../CONTEXT.md`) | 🔴 crítico | T1 | `grep -nE "\]\((\.cursor|\.claude|\.github)/" get_started/HOW_TO_USE_AGENTS.md` todos com `../`; `grep -n "](CLAUDE.md)\|](\.cursorrules)\|](CONTEXT.md)" get_started/HOW_TO_USE_AGENTS.md` retorna vazio |
| T8 | Corrigir links de saída em `get_started/HOW_TO_MAKE_NEW_AGENT.md` (5 alvos: `.cursor/...`, `docs/GUIA_CRIACAO_AGENTE_PROJETO.md`) | 🔴 crítico | T1 | `grep -nE "\]\((\.cursor|docs)/" get_started/HOW_TO_MAKE_NEW_AGENT.md` todos com `../` |
| T9 | Criar `get_started/README.md` (índice: tabela arquivo/descrição/quando usar dos 10 arquivos, padrão `docs/00-INDEX.md`) | 🟡 importante | T1 | Arquivo existe; tem 10 linhas de tabela, uma por arquivo movido |
| T10 | Atualizar 2 arquivos `devloop-phase.md` + 2 `workflow-dev-loop.md` (`.claude`, `.cursor`, `.github` = 6 arquivos) — link `../../../DEV_LOOP_Guia_Comandos.md` → `../../../get_started/DEV_LOOP_Guia_Comandos.md` | 🔴 crítico | T1 | `grep -rn "\.\./\.\./\.\./DEV_LOOP_Guia_Comandos\.md" .cursor .claude .github` retorna vazio; `grep -rn "\.\./\.\./\.\./get_started/DEV_LOOP_Guia_Comandos\.md" .cursor .claude .github` retorna 6 linhas |
| T11 | Atualizar 3 `agent-architect.md` (`.cursor`, `.claude`, `.github`) — links `../../../HOW_TO_MAKE_NEW_AGENT.md`, `../../../HOW_TO_USE_AGENTS.md` (2x cada), `../../../MANUAL_AGENTES.md` → prefixo `get_started/` | 🔴 crítico | T1 | `grep -rnE "\.\./\.\./\.\./(HOW_TO_MAKE_NEW_AGENT|HOW_TO_USE_AGENTS|MANUAL_AGENTES)\.md" .cursor .claude .github \| grep -v get_started` retorna vazio |
| T12 | Atualizar 3 `create-pr.md` (`.cursor`, `.claude`, `.github`) — link `../../../HOW_TO_USE_AGENTS.md` → `../../../get_started/HOW_TO_USE_AGENTS.md` | 🟡 importante | T1 | `grep -rn "\.\./\.\./\.\./HOW_TO_USE_AGENTS\.md" .cursor .claude .github` retorna vazio |
| T13 | Atualizar `.cursor/dev/_index.md` — link `` [`DEV_LOOP_Guia_Comandos.md`](../../DEV_LOOP_Guia_Comandos.md) `` → `../../get_started/DEV_LOOP_Guia_Comandos.md` (só `.cursor/`; `.claude/` e `.github/` não têm essa seção — drift pré-existente, fora de escopo) | 🟡 importante | T1 | `grep -n "get_started/DEV_LOOP_Guia_Comandos" .cursor/dev/_index.md` retorna 1 linha |
| T14 | Corrigir `scripts/sync-workflow-bundle.sh` linha 14 (`GUIDE_ROOT`) | 🔴 crítico | T1 | `grep -n "GUIDE_ROOT=" scripts/sync-workflow-bundle.sh` mostra `get_started/DEV_LOOP_Guia_Comandos.md` |
| T15 | Corrigir `scripts/validate-workflow-bundle.py` linha 80 (`guide_root`) | 🔴 crítico | T1 | `grep -n "guide_root =" scripts/validate-workflow-bundle.py` mostra `"get_started" / "DEV_LOOP_Guia_Comandos.md"` |
| T16 | Corrigir `scripts/validate-agentic-template.py` `MAIN_FILES` (`START_HERE.md`, `SDD_Guia_Comandos.md`) | 🔴 crítico | T1 | `grep -n "get_started/START_HERE.md\|get_started/SDD_Guia_Comandos.md" scripts/validate-agentic-template.py` retorna 2 linhas |
| T17 | Rodar `scripts/sync-workflow-bundle.sh --dry-run` para conferir, depois sem `--dry-run` (regenera `install_dev_loop/assets/DEV_LOOP_Guia_Comandos.md` e `assets/dev/_index.md`) | 🔴 crítico | T1, T14, T15 | Script termina com "sincronização concluída" e roda `validate-workflow-bundle.py` internamente sem erro |
| T18 | Rodar `python3 scripts/validate-workflow-bundle.py` e `python3 scripts/validate-agent-router.py` isoladamente | 🔴 crítico | T17, T16 | Ambos saem com código 0 / "OK" |
| T19 | Verificação final ampla: grep pelo nome de cada um dos 10 arquivos movidos em toda a árvore, excluindo diretórios fora de escopo (`.git`, `.claude/worktrees`, `install_dev_loop`, `agentspec`, `templates`), checando que toda ocorrência restante já tem `get_started/` no path ou é menção textual sem link (aceitável, ver FR-005) | 🟡 importante | T2-T13 | Nenhuma ocorrência de link real (`](...NOME.md)`) sem `get_started/` fora dos diretórios excluídos |

**Nota sobre agentes `@`:** esta é uma tarefa 100% mecânica de edição de texto/paths e execução de scripts já existentes — não há necessidade de invocar um agente de domínio (`@spark-expert...`, `@medallion-architect` etc.). O `dev-loop-executor` executa diretamente via `Read`/`Edit`/`Bash` (`git mv`, `grep`, scripts). Isso será explicitado no craft para não gerar expectativa de agente que não se aplica.

---

## 4. Riscos (herdados de requirements + adicionados)

| Risco | Impacto | Probabilidade | Mitigação |
|---|---|---|---|
| Esquecer algum link em meio a ~19 tarefas | Médio | Média | T19 (verificação final ampla) é obrigatória e cobre toda a árvore, não só os locais já mapeados |
| `git mv` em ambiente Windows/PowerShell via Bash tool ter comportamento inesperado com paths | Baixo | Baixa | Preferir `git mv` (bash) em vez de mover manualmente + `git add`; validar com `git status` logo após T1 |
| Rodar `sync-workflow-bundle.sh` antes de T14/T15 corrigidos aponta para arquivo inexistente e falha | Alto se ordem não for respeitada | Baixa (ordem já definida) | T17 declarado como dependente explícito de T14+T15 no craft |
| `validate-agentic-template.py` rodar em modo `project` vs `template` pode já falhar por outros motivos pré-existentes (fora desta RUN) | Baixo | Baixa | T18 reporta resultado; se falha for por motivo não relacionado ao FR desta RUN, documentar em `phases/execute.md` e não bloquear, mas não é esperado dado o escopo |

---

## 5. Critérios de aceite do design

- [x] Design referencia requirements (FR-001 a FR-008 mapeados em T1-T19)
- [x] Tarefas com dependência e verificação objetiva explícitas
- [x] Ordem de execução justificada (Fase 1 é bloqueante para todas as demais; T17/T18 dependem de T14/T15)
- [x] Riscos e mitigação documentados

---

## 6. Próximo passo

Fase `craft`: transformar T1-T19 em `PROMPT_dl-2026-08-17-get-started.md` com tarefas 🔴→🟡→🟢, cada uma com verificação objetiva (copiar as da tabela acima) e sem necessidade de agentes `@` de domínio.
