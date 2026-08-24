# Guia — Skills + KB integradas ao SDD e ao Dev Loop

> Como o repositório passou a ter uma convenção formal de **Skill** (procedimento) vs **KB**
> (conhecimento), o primeiro exemplo real construído com ela, e os pontos exatos onde isso foi
> ligado ao **SDD** e ao **Dev Loop**. Escrito para ser lido de forma autocontida, sem precisar da
> conversa original que gerou este trabalho.

**Fonte machine-readable da convenção:** [`.claude/rules/skill-first.md`](../.claude/rules/skill-first.md)
**Registro de Skills próprias do projeto:** [`.claude/sdd/architecture/AGENT_ROUTER.yaml`](../.claude/sdd/architecture/AGENT_ROUTER.yaml) (`skill_reference`)

---

## 1. Por que este documento existe

Este repositório já tinha dois mecanismos de contexto persistente para agentes: **KB**
(`.claude/kb/`, `.cursor/kb/`, `.github/kb/`) e, mais recentemente, um bundle vendor de **Skills**
(`.claude/skills/`) trazido por integrações Databricks/MLflow. Faltava uma convenção explícita de
**quando usar qual**, e o repositório ainda não tinha nenhuma Skill **própria** do projeto — nem um
exemplo de como ligá-la aos fluxos estruturados que já existem (**SDD** e **Dev Loop**).

Esta sessão de trabalho resolveu as duas coisas: formalizou o critério de decisão e construiu o
primeiro caso real — uma Skill de boas práticas de versionamento Git, ligada em quatro pontos do
SDD/Dev Loop. Este documento consolida o que foi feito, para ser consultado sem depender da
conversa onde isso foi decidido.

---

## 2. Duas fontes de conhecimento: Skill vs KB

### 2.1 Critério de decisão

A regra vive em [`.claude/rules/skill-first.md`](../.claude/rules/skill-first.md) e resume-se a uma
pergunta:

| Pergunta | Se SIM → | Local |
|----------|----------|-------|
| É um procedimento repetível, "como fazer X" (passo a passo acionável)? | **Skill** | `.claude/skills/<nome>/SKILL.md` |
| É contexto, conceito, contrato ou "o que é verdade sobre X"? | **KB** | `.claude/kb/<dominio>/...` |

Na prática: uma KB descreve fatos e contratos de domínio ("como funciona autorização RBAC/ABAC
neste projeto"). Uma Skill descreve um procedimento que alguém — humano ou agente — segue passo a
passo para produzir um resultado ("como versionar corretamente durante o Dev Loop").

### 2.2 Tabela comparativa

| Aspecto | Skill | KB |
|---------|-------|----|
| **Localização** | Só `.claude/skills/<nome>/SKILL.md` | Mirrorada em `.claude/kb/`, `.cursor/kb/`, `.github/kb/` |
| **Descoberta** | Nativa/automática (Claude Code lê `name`/`description` do frontmatter) | Deliberada — um agente ou regra faz `Read()` explícito de um path |
| **Registro** | Informativo, em `AGENT_ROUTER.yaml` → `skill_reference` (não afeta a descoberta) | `AGENT_ROUTER.yaml` → `kb_reference` + `.claude/kb/_index.yaml` |
| **Convenção de nome** | Prefixo de domínio obrigatório (evita colidir com o bundle vendor) | Nome de domínio livre |
| **Migração entre os dois** | Decisão caso a caso, nunca automática | — |

---

## 3. Como a descoberta funciona (mecanismo nativo do Claude Code)

Isto é o ponto mais importante para não confundir Skill com os outros mecanismos do repositório: a
descoberta de Skill é **nativa do Claude Code**, não uma convenção que o projeto inventou. O Claude
Code varre `.claude/skills/*/SKILL.md`, lê `name` e `description` do frontmatter, e decide sozinho
quando oferecer aquela Skill numa conversa — sem que nenhum agente ou regra precise apontar
explicitamente para ela.

É exatamente por isso que a regra em `skill-first.md` é categórica: **Skill nunca é espelhada** em
`.cursor/skills/` ou `.github/skills/` — porque só o Claude Code tem esse mecanismo de descoberta;
criar cópias noutras árvores não faria nada além de duplicar arquivo (ver §9 para o detalhe de
Cursor e Copilot).

A KB funciona ao contrário: não há descoberta automática nenhuma — um agente só "sabe" de uma KB
porque uma regra (`.claude/rules/*.md`) ou o próprio arquivo do agente contém um `Read()` explícito
apontando para `.claude/kb/<dominio>/index.md`. Por isso a KB **precisa** ser mirrorada nas três
árvores: cada árvore só enxerga o que está fisicamente dentro dela.

---

## 4. Estudo de caso: a skill `git-boas-praticas-versionamento`

### 4.1 O que ela cobre

Primeira Skill própria do projeto:
[`.claude/skills/git-boas-praticas-versionamento/SKILL.md`](../.claude/skills/git-boas-praticas-versionamento/SKILL.md)

Nasceu de um pedido simples — "quero uma skill de git para boas práticas de versionamento, usada no
SDD e no Dev Loop" — e, depois de alinhar escopo com o usuário, cobre:

- **Estratégia de branch** — trunk-based, `<type>/<slug>`, uma branch por feature (SDD) ou por
  `RUN_ID` (Dev Loop)
- **Granularidade de commit por contexto** — tabela específica para build/ship (SDD) e
  execute/fixer/round em modo `hitl` vs `afk` (Dev Loop)
- **Conventional Commits** — mesmo formato usado em `create-pr.md`, sem duplicar a tabela completa
- **Regra de ouro** — nunca commitar, dar push ou rodar operação destrutiva sem autorização
  explícita do usuário ou do modo de execução escolhido
- **O que nunca fazer sem decisão explícita** — `push --force`, `--no-verify`, `reset --hard`,
  `amend` em commit compartilhado, `branch -D`, segredos no diff
- **Trabalho não commitado ao trocar de fase/task** — sempre `git status` antes de continuar
- **Checklist antes de abrir PR** — remete para `create-pr.md` (ver §7)

### 4.2 Onde vive e como foi registrada

A Skill vive só em `.claude/skills/git-boas-praticas-versionamento/SKILL.md` — nunca em
`.cursor/skills/` nem `.github/skills/`, seguindo §3. O nome carrega o prefixo de domínio `git-`
para nunca colidir com o bundle vendor Databricks/MLflow já presente em `.claude/skills/`.

O registro é em `AGENT_ROUTER.yaml` → `skill_reference` (mirrorado nas três árvores, porque o
`AGENT_ROUTER.yaml` em si é KB-like e É mirrorado — só a Skill em si que não é):

```yaml
skill_reference:
- skill_name: git-boas-praticas-versionamento
  path: .claude/skills/git-boas-praticas-versionamento/SKILL.md
  used_by_agent_ids:
  - build-agent
  - ship-agent
  - dev-loop-executor
  - devloop-fixer
```

Esse registro é **informativo** — documenta quem consome a Skill — mas não é o que faz o Claude
Code descobri-la; isso já acontece via frontmatter, como explicado em §3.

---

## 5. Integração ao SDD (Fases 3 e 4)

O SDD (Nível 3) já tinha um `build-agent` (Fase 3 — implementação) e um `ship-agent` (Fase 4 —
arquivamento), mas nenhum dos dois falava de commit em nenhum momento do processo — o build ia
direto de "executar tarefas" para "gerar relatório", e o ship arquivava sem checar o estado do git.

### 5.1 `build-agent` — passo 4.1 "Commit Progress"

Arquivo: [`.claude/agents/workflow/build-agent.md`](../.claude/agents/workflow/build-agent.md)

Inserido entre o passo "4. Execute Each Task" e o passo "5. Full Validation":

> Após cada arquivo (ou grupo de arquivos relacionados) verificado com sucesso, commitar seguindo
> o guia `.claude/skills/git-boas-praticas-versionamento/SKILL.md` — granularidade por unidade
> lógica do manifesto, mensagem em Conventional Commits (`feat`, `fix`, `refactor`...). Propor o
> commit e aguardar confirmação do usuário, salvo modo de execução explicitamente autônomo.

### 5.2 `ship-agent` — passo 1.1 "Verify Git State"

Arquivo: [`.claude/agents/workflow/ship-agent.md`](../.claude/agents/workflow/ship-agent.md)

Inserido logo após o passo "1. Verify Completion", antes de criar a estrutura de arquivo:

> Antes de arquivar, garantir que não há trabalho da feature sem commit... Se houver mudanças
> pertencentes à feature ainda não commitadas, propor um commit final (Conventional Commits) e
> aguardar confirmação antes de prosseguir. Nunca arquivar com working tree sujo.

---

## 6. Integração ao Dev Loop

### 6.1 `dev-loop-executor` — commit por tarefa (`hitl` vs `afk`)

Arquivo: [`.claude/agents/dev/dev-loop-executor.md`](../.claude/agents/dev/dev-loop-executor.md)

Esta era a lacuna mais concreta encontrada: a documentação do Dev Loop (`_index.md`) já dizia, na
tabela de modos de execução, que `afk` significa **"commit per task"** — mas o pseudocódigo do loop
principal do executor nunca chamava nada parecido com commit. O passo "Update state" ia direto de
marcar a tarefa concluída para decidir se pausava (`hitl`) ou continuava (`afk`), sem nunca tocar
em git.

Correção aplicada no `Core Loop (Pseudocode)`, logo após `write_progress(progress)`:

```text
# Commit (see .claude/skills/git-boas-praticas-versionamento/SKILL.md)
if mode == "afk":
    git_commit_task(task)          # autonomous — --mode afk is the user's explicit authorization
else:
    propose_commit_task(task)      # hitl — wait for user confirmation before committing
```

E uma seção nova, `## Commits During Execution`, com a tabela de comportamento por modo e a regra
de mensagem (Conventional Commits, `scope` = nome do PROMPT/RUN).

A lógica por trás da distinção `hitl`/`afk` não é nova — é a mesma regra de ouro da Skill (§4.1):
`--mode afk` **é** a autorização explícita do usuário para agir autonomamente (ele escolheu esse
modo na hora de rodar `/dev` ou `/devloop-execute`); em `hitl` (o padrão), o commit é proposto e
aguarda confirmação, exatamente como qualquer outra ação do modo humano-no-loop.

### 6.2 `devloop-fixer` — passo 3 "Commitar a correção"

Arquivo: [`.claude/agents/workflow-dev-loop/devloop-fixer.md`](../.claude/agents/workflow-dev-loop/devloop-fixer.md)

O processo original ia de "2. Implementar só o escopo pedido" direto para "3. Atualizar PROGRESS".
Passo novo inserido entre os dois:

> **Commitar** a correção (Conventional Commits — ver
> `.claude/skills/git-boas-praticas-versionamento/SKILL.md`); propor e aguardar confirmação do
> usuário, salvo modo de execução explicitamente autônomo.

(`devloop-round` não recebeu edição — é revalidação, normalmente não produz mudanças de código por
si só; se um round corrigir algo diretamente, a mesma regra do fixer se aplica por analogia.)

---

## 7. Relação com `create-pr.md`

O comando [`.claude/commands/workflow/create-pr.md`](../.claude/commands/workflow/create-pr.md) já
existia e já cobria **a mecânica de abrir um PR**: passos de `git checkout -b`, `git commit`,
`git push`, `gh pr create`, template de descrição, e a tabela completa de Conventional Commits.

A Skill não duplica isso — ela cobre a **disciplina de commit durante o trabalho**, antes de chegar
no PR: granularidade por fase/tarefa, quando propor vs commitar direto, o que nunca fazer. O
`create-pr.md` agora tem uma nota no topo apontando para a Skill:

> Para a disciplina de commit **antes** de chegar aqui (granularidade, quando commitar em cada fase
> SDD/Dev Loop, o que nunca fazer sem autorização explícita), ver
> `.claude/skills/git-boas-praticas-versionamento/SKILL.md`.

Em resumo: **Skill = disciplina contínua durante o trabalho. `create-pr.md` = o momento de abrir o
PR.** Um alimenta o outro (histórico de commits limpo e granular facilita a geração de PR), mas são
documentos com responsabilidades diferentes.

---

## 8. Como criar uma Skill nova neste repositório

Roteiro reutilizável — o mesmo que orientou a criação da `git-boas-praticas-versionamento`:

1. **Confirme que é mesmo Skill, não KB.** Aplique a pergunta de §2.1. Se a resposta for "conceito
   ou contrato", vá para `.claude/kb/<dominio>/` em vez disso.
2. **Escolha o nome com prefixo de domínio.** Nunca um nome genérico — sempre `<dominio>-<acao>`,
   ex.: `sql-capacity-criar-pipeline`, `teams-notificar-falha`, `git-boas-praticas-versionamento`.
   Isso evita colisão com o bundle vendor Databricks/MLflow que já ocupa `.claude/skills/`.
3. **Crie o arquivo só em `.claude/skills/<nome>/SKILL.md`.** Frontmatter mínimo: `name` e
   `description` — a `description` é o que o Claude Code usa para auto-descoberta/acionamento,
   então precisa ser específica e cobrir os gatilhos reais de uso.
4. **Use o meta-skill `skill-creator`** (já disponível no bundle vendor, `.claude/skills/skill-creator/`)
   para o fluxo de rascunho → prompts de teste → avaliação → iteração → otimização da `description`.
5. **Registre em `AGENT_ROUTER.yaml`** → `skill_reference` (nas três árvores, já que o arquivo
   `AGENT_ROUTER.yaml` em si é mirrorado — ver §2.2):
   ```yaml
   skill_reference:
     - skill_name: <nome>
       path: .claude/skills/<nome>/SKILL.md
       used_by_agent_ids: [...]   # ou used_by_roster_groups: [...]
   ```
6. **Valide:** `python3 scripts/validate-agent-router.py`
7. **Ligue a Skill aos fluxos que realmente vão usá-la** — se for para SDD e/ou Dev Loop, edite os
   agentes relevantes (`build-agent`, `ship-agent`, `dev-loop-executor`, `devloop-fixer`, etc.) para
   referenciar o path literal `.claude/skills/<nome>/SKILL.md` no ponto certo do processo deles —
   isso é o que faz a Skill ser **usada**, não só descoberta por acaso. Replique cada edição nas
   três árvores (`.claude/`, `.cursor/`, `.github/`), já que os arquivos de agente são mirror.
8. **Não migre KB existente "de graça".** Se surgir a tentação de mover conteúdo já existente de KB
   para Skill, trate como decisão caso a caso — não como consequência automática desta convenção.

---

## 9. Portabilidade: Claude Code, Cursor e GitHub Copilot

Esta seção existe porque **o pedido explícito era deixar isto claro**: o processo acima foi
desenhado para o Claude Code, mas o repositório é usado também no Cursor e no GitHub Copilot — e é
importante não prometer uma paridade automática que não existe.

### 9.1 O que é mecanismo nativo vs convenção do projeto

| Ferramenta | Mecanismo nativo mais próximo de "Skill" | Descoberta | Estado real neste repo |
|------------|-------------------------------------------|-------------|--------------------------|
| **Claude Code** | Skill (`SKILL.md`) | Automática, por `description` no frontmatter | Nativo — é para onde toda Skill própria do projeto é escrita (`.claude/skills/`) |
| **Cursor** | Project Rules (`.cursor/rules/*.mdc`), modo "Agent Requested" (usa `description` para decidir quando incluir a regra) | Semiautomática — análoga em espírito à Skill (decide por descrição), mas é outro mecanismo (regra, não "skill") | `.cursor/skills/` existe hoje só como **mirror do bundle vendor** (Databricks/MLflow); não é onde Skills próprias do projeto devem ir — ver §2.1/§3 |
| **GitHub Copilot** | `.github/copilot-instructions.md` (sempre incluído no contexto) + `.github/instructions/*.instructions.md` (`applyTo` por glob) + prompt files (`.github/prompts/*.prompt.md`, invocação manual tipo slash command) | Instructions: automática (sempre-on ou por path). Prompt files: manual | `.github/copilot-instructions.md` já existe neste repo, mas hoje é um **ponteiro fino** ("fonte canônica é `.cursor/`, use `.github/` como espelho") — não replica automaticamente o conteúdo de uma Skill |

### 9.2 Tabela de equivalências práticas

| O que você quer fazer | Claude Code | Cursor | GitHub Copilot |
|------------------------|-------------|--------|-----------------|
| Procedimento descoberto automaticamente por assunto | Skill (`.claude/skills/`) | Rule "Agent Requested" (`.cursor/rules/*.mdc`) | Não há equivalente automático por assunto — mais perto é uma instruction com `applyTo` por caminho de arquivo |
| Procedimento sempre carregado | KB referenciado por regra sempre-on, ou `.claude/CLAUDE.md` | Rule "Always Apply" | `.github/copilot-instructions.md` |
| Procedimento invocado manualmente | Slash command (`.claude/commands/`) | Comando/`@` manual | Prompt file (`.github/prompts/*.prompt.md`) |

### 9.3 Limitações honestas (o que NÃO é automático hoje)

O que é **de fato automático** neste repositório é só a descoberta nativa de Skill no Claude Code.
Para Cursor e Copilot, a "portabilidade" hoje significa **o conteúdo estar disponível e legível**
nas árvores mirror (`.cursor/`, `.github/`) — os agentes `.md`, o `AGENT_ROUTER.yaml`, as regras em
`.claude/rules/` (mirroradas como `.cursor/rules/*.mdc` e `.github/rules/*.md`), e os arquivos de
entrada `.cursorrules` / `.github/copilot-instructions.md` — e **não** uma migração automática do
mecanismo de descoberta em si.

Concretamente, para a Skill `git-boas-praticas-versionamento`:

- **No Claude Code:** funciona hoje, nativamente, sem nenhuma ação extra.
- **No Cursor:** o conteúdo pode ser adaptado para uma `.cursor/rules/git-boas-praticas.mdc` (modo
  "Agent Requested", com `description` equivalente) para ganhar descoberta semiautomática
  parecida — isso **não existe ainda**, seria trabalho adicional caso o time queira essa paridade.
- **No GitHub Copilot:** o conteúdo pode virar uma seção em `.github/copilot-instructions.md` (sempre
  ativo, mais pesado) ou um `.github/prompts/git-boas-praticas.prompt.md` (invocação manual, mais
  leve) — também **não existe ainda**.

Em todos os casos, o texto-fonte (`SKILL.md`) já está pronto para servir de base a essa adaptação —
só a forma final e o mecanismo de carregamento mudam por ferramenta.

---

## 10. Referências e changelog desta sessão

Arquivos criados ou editados nesta sessão de trabalho, todos já commitados (commit `271a2e7`,
`FEAT: adicionar skill git-boas-praticas-versionamento e ligar ao SDD/Devloop`):

| Arquivo | O que mudou |
|---------|-------------|
| `.claude/skills/git-boas-praticas-versionamento/SKILL.md` | Criado |
| `.claude/sdd/architecture/AGENT_ROUTER.yaml` (×3 árvores) | `skill_reference` populado |
| `.claude/agents/workflow/build-agent.md` (×3) | Passo 4.1 "Commit Progress" |
| `.claude/agents/workflow/ship-agent.md` (×3) | Passo 1.1 "Verify Git State" |
| `.claude/agents/dev/dev-loop-executor.md` (×3) | Commit no pseudocódigo + seção "Commits During Execution" |
| `.claude/agents/workflow-dev-loop/devloop-fixer.md` (×3) | Passo 3 "Commitar a correção" |
| `.claude/commands/workflow/create-pr.md` (×3) | Nota de cross-reference no topo |

("×3 árvores" = mesma edição replicada em `.claude/`, `.cursor/` e `.github/`, variando só o
prefixo de auto-referência de cada árvore — ver §2.2 sobre por que KB/agentes são mirrorados e
Skill não.)

**Outras referências:**

- [`.claude/rules/skill-first.md`](../.claude/rules/skill-first.md) — convenção Skill vs KB
- [`.claude/skills/git-boas-praticas-versionamento/SKILL.md`](../.claude/skills/git-boas-praticas-versionamento/SKILL.md) — texto completo da Skill
- [`.claude/commands/workflow/create-pr.md`](../.claude/commands/workflow/create-pr.md) — mecânica de PR
- [`.claude/sdd/dev-loop-runs/dl-2026-08-18-doc-skills-kb/`](../.claude/sdd/dev-loop-runs/dl-2026-08-18-doc-skills-kb/) — RUN do Dev Loop que produziu este documento (requirements, design, PROMPT)
