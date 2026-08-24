---
name: git-boas-praticas-versionamento
description: Guides Git version-control best practices for this repository — branch strategy, commit granularity and Conventional Commits messages, what never to do without explicit user approval (force-push, --no-verify, reset --hard, amend on shared commits), and how to handle uncommitted work at phase/task boundaries. Use during SDD workflow (build, ship) and Dev Loop workflow (execute, round, fixer) whenever code is about to be committed, a branch needs to be created, or a PR is being prepared. Also usable as a standalone reference to hand to teammates.
---

# Git — Boas Práticas de Versionamento

> Guia de referência para versionamento neste repositório. Cobre **quando** e **como** commitar,
> **estratégia de branch**, e **o que nunca fazer** sem decisão explícita do usuário — aplicável
> tanto dentro do fluxo SDD (`/build`, `/ship`) e Dev Loop (`/devloop-execute`, `/devloop-round`,
> `/devloop-fixer`), quanto como checklist para passar adiante a outras pessoas/times.

Este guia é **complementar** a [`.claude/commands/workflow/create-pr.md`](../../commands/workflow/create-pr.md),
que cobre a mecânica de criar o PR em si (passos, template de descrição, `gh pr create`). Aqui o foco é a
**disciplina de commit ao longo do trabalho**, antes de chegar no PR.

---

## Regra de ouro

**Nunca commitar, dar push ou executar operação destrutiva sem que o usuário tenha autorizado — explicitamente
ou pelo modo de execução escolhido.** Em Dev Loop, `--mode afk` é a autorização explícita para commit automático
por tarefa; `--mode hitl` (padrão) exige propor o commit e aguardar confirmação. Fora de um modo autônomo
explícito, sempre proponha o commit e espere a confirmação do usuário.

Antes de qualquer comando que possa descartar trabalho não commitado (`checkout`, `restore`, `reset`, `clean`),
rode `git status` primeiro.

---

## Estratégia de branch

- **Trunk-based com feature branches curtas.** Nunca commitar direto em `main`.
- Convenção de nome: `<type>/<slug-curto>` (mesmo padrão do `create-pr.md`):
  ```text
  feat/user-authentication
  fix/parser-null-handling
  refactor/agents-standardization
  chore/normalizar-hooks
  ```
- **SDD:** uma branch por feature, criada antes (ou no início) da fase **Build** — nome deriva do slug usado em
  `DEFINE_{FEATURE}.md` / `DESIGN_{FEATURE}.md`.
- **Dev Loop:** uma branch por `RUN_ID` (`.claude/sdd/dev-loop-runs/{RUN_ID}/`) — nome deriva do `RUN_ID`.
- Branch vive até o PR ser mergeado; não reaproveitar branch para trabalho não relacionado.

---

## Quando commitar (granularidade)

| Contexto | Momento do commit | Observação |
|----------|--------------------|------------|
| **SDD — Build** (`build-agent`) | Após cada arquivo do manifesto passar verificação (lint/tests), ou no mínimo ao fim da fase Build | Um commit por unidade lógica do manifesto, não um commit gigante no fim |
| **SDD — Ship** (`ship-agent`) | Antes de arquivar (mover para `archive/`), garantir que tudo está commitado | Ship não deve arquivar com working tree sujo |
| **Dev Loop — Execute, modo `hitl`** | Ao final de cada tarefa 🔴/🟡/🟢 verificada, **propor** o commit e pausar para revisão | Alinhado ao "pause for review" já existente no modo hitl |
| **Dev Loop — Execute, modo `afk`** | Commit automático a cada tarefa verificada (exit code 0) | `--mode afk` já é a autorização explícita do usuário para isso |
| **Dev Loop — Fixer** | Após implementar o escopo pedido e atualizar PROGRESS | Um commit por invocação do fixer, escopo = só o pedido no `task_ref` |
| **Dev Loop — Round** | Normalmente não commita (é revalidação) — só se corrigir algo diretamente | Se corrigir, mesma regra do fixer |

Princípio geral: **commits pequenos e frequentes, um por mudança logicamente completa e verificada** — nunca
acumular múltiplas tarefas/arquivos não relacionados num único commit.

---

## Mensagens de commit — Conventional Commits

Mesmo formato usado em `/create-pr`:

```text
<type>(<scope>): <descrição curta>

<corpo opcional — o que mudou e por quê>
```

| Type | Quando usar |
|------|-------------|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `refactor` | Reestruturação sem mudar comportamento |
| `docs` | Só documentação |
| `test` | Testes |
| `chore` | Manutenção, build, dependências |
| `style` | Formatação |
| `perf` | Performance |

Para tarefas de SDD/Dev Loop, o `scope` costuma ser o nome da feature ou do `RUN_ID`; a descrição curta reflete a
tarefa concluída (ex.: `feat(auth-login): adicionar validação de token JWT`).

Tabela completa e exemplos: [`create-pr.md` § Conventional Commits Reference](../../commands/workflow/create-pr.md).

---

## O que nunca fazer sem decisão explícita do usuário

- `git push --force` (especialmente em branch compartilhada ou `main`)
- `git reset --hard`, `git checkout .` / `git restore .`, `git clean -f` sem antes rodar `git status` e
  confirmar que não há trabalho em progresso sendo descartado
- `--no-verify`, `--no-gpg-sign`, `-c commit.gpgsign=false` (pular hooks/assinatura)
- `git commit --amend` em commit que já foi *pushed*/compartilhado
- `git branch -D` (delete forçado)
- Commitar segredos, `.env` real, ou inventário local de infraestrutura (ver `CLAUDE.md` deste repo)
- Se um hook de commit falhar: corrigir a causa raiz e criar um **novo** commit — nunca pular com `--no-verify`

Se algo aqui parecer necessário durante o trabalho, **pare e pergunte ao usuário** em vez de executar.

---

## Trabalho não commitado ao trocar de fase/task

Ao final de qualquer fase SDD ou tarefa Dev Loop, antes de seguir para a próxima:

1. `git status` — existe algo não commitado?
2. Se sim e for parte do escopo concluído → commitar (seguindo a tabela de granularidade acima).
3. Se for trabalho parcial/experimental que não deve virar commit ainda → `git stash push -u` (nunca descartar).
4. Nunca deixar a fase seguinte começar sobre um working tree com mudanças órfãs não rastreadas.

---

## Antes de abrir PR

Checklist mínimo (mecânica completa em [`create-pr.md`](../../commands/workflow/create-pr.md)):

```text
[ ] git log origin/main..HEAD --oneline — histórico de commits faz sentido sozinho?
[ ] Branch não é main/master
[ ] Todos os commits seguem Conventional Commits
[ ] Nada de segredo/.env real no diff
[ ] CONTEXT.md / .claude/CURSOR.MD atualizados se mudou como se roda/usa o projeto
```

---

## Referências

- `.claude/commands/workflow/create-pr.md` — mecânica de PR, template de descrição, branch/commit/push
- `.claude/agents/workflow/build-agent.md` — Fase 3 SDD
- `.claude/agents/workflow/ship-agent.md` — Fase 4 SDD
- `.claude/agents/dev/dev-loop-executor.md` — loop de execução Dev Loop (hitl/afk)
- `.claude/agents/workflow-dev-loop/devloop-fixer.md` — correção pontual pós-execução
- `CLAUDE.md` (raiz) — Git Safety Protocol da sessão (nunca pular hooks, nunca force-push sem pedido explícito)
