# Guia passo a passo — **DEV LOOP** (Nível 2)

Este documento é o **roteiro humano** para o **Nível 2 — Agentic Development (DEV LOOP)**. A especificação normativa dos comandos está em **[`.cursor/commands/dev/dev.md`](../.cursor/commands/dev/dev.md)**. Lista de agentes e exemplos com `@`: **[`HOW_TO_USE_AGENTS.md`](HOW_TO_USE_AGENTS.md)**.

---

## O que é o DEV LOOP neste repositório

- **Comando central:** `/dev` (roteia para `prompt-crafter` ou `dev-loop-executor`).
- **Artefatos:** `PROMPT_*.md` em `.cursor/dev/tasks/`, progresso em `.cursor/dev/progress/`, relatórios em `.cursor/dev/logs/`.
- **Não existe** CLI `/agent …` com flags; no Cursor use **slash commands** (`/dev`) e **referências `@`** aos arquivos em `.cursor/agents/`.

---

## Quando usar Dev Loop (L2) vs SDD (L3)

Use esta tabela para escolher o nível certo **antes** de abrir o chat:

| Cenário | Dev Loop (L2) | SDD (L3) |
|---------|:-------------:|:--------:|
| Construção de KB | ✅ | |
| Protótipos | ✅ | |
| Features isoladas (um componente) | ✅ | |
| Utilitários / parsers | ✅ | |
| Features multi-componente | | ✅ |
| Sistemas em produção | | ✅ |
| Projetos em equipe (rastreio formal) | | ✅ |
| Trilha de auditoria completa | | ✅ |

- **Dev Loop (L2):** `/dev` + `PROMPT_*.md` — ideal para entregas focadas, com requisitos e design leves em markdown.
- **SDD (L3):** `/brainstorm`, `/design`, `/build` — ver **[`SDD_Guia_Comandos.md`](SDD_Guia_Comandos.md)** quando precisar de specs, gates e auditoria de ponta a ponta.

---

## Workflow oficial (recomendado): `/workflow-dev-loop`

Para o mesmo fluxo com **RUN_ID**, manifest em disco e **handoff obrigatório** (`Próximo comando:`), use o workflow estruturado:

| Passo | Comando |
|-------|---------|
| Entrada | `/workflow-dev-loop` |
| Criar RUN | `/devloop-init <RUN_ID>` |
| Fases | `/devloop-phase <RUN_ID> gate` → `requirements` → `design` → `craft` → `prompt_review` |
| Executar | `/devloop-execute <RUN_ID>` (só após OK humano em `prompt_review`) |
| Encerrar | `/devloop-phase <RUN_ID> reflect` |
| Pós-execução | `/devloop-round`, `/devloop-fixer` |

Estado: `.cursor/sdd/dev-loop-runs/{RUN_ID}/` · Contrato: [`.cursor/sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml`](../.cursor/sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml) · Comandos: [`.cursor/commands/workflow-dev-loop/`](../.cursor/commands/workflow-dev-loop/)

---

## Fluxo passo a passo (manual ou via workflow)

Ordem canônica para uma feature no Dev Loop:

```text
1. meeting-analyst  →  salvar *requirements*.md
2. the-planner      →  salvar *design*.md (com base nos requirements)
3. /dev             →  craft a partir do design (+ requirements no contexto)
4. /dev tasks/PROMPT_*.md  →  executar o loop
```

Equivalente com workflow: `/devloop-phase` em cada linha acima (ver tabela na seção anterior).

**Convenção de nomes de arquivo** (pasta sugerida: `./design/` ou equivalente do projeto):

| Etapa | Sufixo no nome do arquivo | Exemplo |
|-------|---------------------------|---------|
| Requisitos | `*requirements*.md` | `./design/auth_login_requirements.md` |
| Design / plano | `*design*.md` | `./design/auth_login_design.md` |
| PROMPT executável | `PROMPT_*.md` em `.cursor/dev/tasks/` | `.cursor/dev/tasks/PROMPT_AUTH_LOGIN.md` |

> **Regra prática:** não pule para o `/dev` de execução sem ter **requirements** e **design** prontos, salvo tarefas triviais (hotfix de uma linha, ajuste de doc).

---

## Antes de começar

Alinhar o triângulo de contexto descrito em **[`START_HERE.md`](START_HERE.md)** (`CONTEXT.md`, `.cursorrules`, `docs/00-INDEX.md`) para o loop não divergir do produto real.

---

## Passo 1 — Requisitos (`meeting-analyst`)

**Agente:** `meeting-analyst` — [`.cursor/agents/communication/metting-analyst.md`](../.cursor/agents/communication/metting-analyst.md)

No chat, inclua o agente com `@` e peça um artefato com **sufixo `requirements`** no nome do arquivo:

```text
@.cursor/agents/communication/metting-analyst.md

Analise ./reunioes/reuniao01.txt e salve os requisitos consolidados em
./design/minha_feature_requirements.md
(decisões, requisitos funcionais/não funcionais, itens de ação e fora de escopo).
```

Ajuste caminhos aos seus arquivos. O assistente executa o papel do agente; não há comando `/agent meeting-analyst analyze …` neste repositório.

**Saída esperada:** um único markdown de requisitos versionável (ex.: `auth_login_requirements.md`).

---

## Passo 2 — Design e plano (`the-planner`)

**Agente:** `the-planner` — [`.cursor/agents/communication/the-planner.md`](../.cursor/agents/communication/the-planner.md)

Com o arquivo `*requirements*.md` do passo anterior, organize a implementação e salve com **sufixo `design`**:

```text
@.cursor/agents/communication/the-planner.md

Com base em ./design/minha_feature_requirements.md, produza o plano de implementação
(arquitetura, tarefas, riscos, verificações) e salve em
./design/minha_feature_design.md.
```

**Saída esperada:** `*design*.md` referenciando explicitamente o `*requirements*.md` de origem.

Para desenho no fluxo **SDD (Nível 3)** (specs formais, ADRs, gates), prefira **`/design`** e o **`design-agent`** — ver [`.cursor/commands/workflow/design.md`](../.cursor/commands/workflow/design.md) e a tabela **L2 vs L3** acima.

---

## Passo 3 — Craft com `/dev` (a partir do design)

O conceito do Dev Loop na execução é o comando **`/dev`**. Para features reais, **não** comece só com uma frase solta: tenha **`requirements`** e **`design`** e use o **design** como entrada principal do craft.

**Agente:** `prompt-crafter` — [`.cursor/agents/dev/prompt-crafter.md`](../.cursor/agents/dev/prompt-crafter.md)

**Forma recomendada (com design + requirements):**

```text
@./design/minha_feature_design.md
@./design/minha_feature_requirements.md

/dev "Gere o PROMPT executável (.cursor/dev/tasks/PROMPT_*.md) implementando
estritamente o design anexado; use os requirements como fonte de verdade para escopo."
```

O assistente valida o escopo, pode pedir esclarecimentos pontuais e gera `.cursor/dev/tasks/PROMPT_*.md`.

**Atalho (tarefas pequenas):** descrição em linguagem natural sem artefatos prévios — use só quando a tabela **L2 vs L3** indicar Dev Loop e o escopo for mínimo:

```text
/dev "Implementar utilitário X com verificação Y"
```

**Alternativa:** `@.cursor/agents/dev/prompt-crafter.md` com os mesmos anexos `@` de `*design*.md` e `*requirements*.md`.

**Manual:** copiar template e editar:

```bash
cp .cursor/dev/templates/PROMPT_TEMPLATE.md \
   .cursor/dev/tasks/PROMPT_MINHA_FEATURE.md
```

*(Se a pasta ainda não existir, crie-a ou deixe o primeiro `/dev` criar a estrutura conforme o assistente.)*

---

## Passo 3.1 — Escolha de agentes: o PROMPT é quem manda

Os arquivos de **reunião** e **design** (e o `CONTEXT.md`) são **insumos** para o craft; **não** existe um classificador automático que, só por anexá-los, escolha “engenharia de dados” ou “Medallion” no momento em que você roda `/dev tasks/PROMPT_*.md`.

| O que acontece | Detalhe |
|----------------|---------|
| **Executor (`dev-loop-executor`)** | Segue o **`PROMPT_*.md`**: executa tarefas na ordem e, quando o arquivo estiver escrito no padrão do repositório, pode **invocar agentes nomeados** nas linhas de tarefa (veja padrões em [`.cursor/agents/dev/dev-loop-executor.md`](../.cursor/agents/dev/dev-loop-executor.md), seção *Task Patterns* / *Agent Invocation*). |
| **Quem define os agentes** | O **conteúdo do PROMPT** — em geral gerado no craft com instruções claras. Se o PROMPT disser apenas “implementar pipeline” sem citar agentes, o loop não “adivinha” que deve usar `medallion-architect` ou `spark-expert-on-premises`. |
| **Prompt-crafter** | Você deve **pedir explicitamente** no craft (“cada tarefa de desenho de camadas deve referenciar `@medallion-architect` em …; jobs Spark on-prem com `@spark-expert-on-premises` …”). Nomes alinhados a [`HOW_TO_USE_AGENTS.md`](HOW_TO_USE_AGENTS.md) e ao `name:` no frontmatter de cada `.md` em `.cursor/agents/`. |
| **Ajuda para escolher antes do craft** | Opcional: comando **`/core/agent`** ou leitura de [`.cursor/commands/core/router.md`](../.cursor/commands/core/router.md) — depois **incorpore** a escolha no texto do PROMPT. |

**Antes de executar:** revise o `PROMPT_*.md` gerado e confira se as tarefas críticas citam os agentes certos (ou anexe o arquivo no chat e peça um ajuste pontual).

---

## Passo 4 — Execução — DEV LOOP (executor)

**Agente:** `dev-loop-executor` — [`.cursor/agents/dev/dev-loop-executor.md`](../.cursor/agents/dev/dev-loop-executor.md)

```text
/dev tasks/PROMPT_NOME.md
```

**Opções úteis:**

| Uso | Exemplo |
|-----|---------|
| Listar PROMPTs conhecidos | `/dev --list` |
| Validar sem executar | `/dev tasks/PROMPT_X.md --dry-run` |
| Retomar sessão | `/dev tasks/PROMPT_X.md --resume` |
| Modo autônomo (sem pausas) | `/dev tasks/PROMPT_X.md --mode afk` |
| Limite de iterações | `/dev tasks/PROMPT_X.md --max 20` |

---

## 5. Acompanhar progresso e auditoria

Não há subcomandos `/dev status` ou `/dev logs` neste repositório. O estado fica nos arquivos:

| Local | O quê |
|-------|--------|
| `.cursor/dev/progress/PROGRESS_*.md` | Tarefas concluídas, decisões, retomada (`--resume`) |
| `.cursor/dev/logs/LOG_*.md` | Relatório de execução ao finalizar |

**Edição de tarefas:** dentro do próprio `PROMPT_*.md` (checklist) ou novo craft com `/dev "…"` — não existem comandos `/task add|revise|approve` aqui.

---

## 6. Depois do loop (não é parte do `/dev`)

- **Testes / lint / build:** siga os comandos em **`CONTEXT.md`** e **`README.md`** do projeto.
- **Implementação SDD (Nível 3)** a partir de um DESIGN: comando **`/build`** — [`.cursor/commands/workflow/build.md`](../.cursor/commands/workflow/build.md) — é outro fluxo (Spec-Driven), não substitui o `/dev`.

---

## Exemplo prático: pipeline Medallion (Raw → Bronze → Silver → Gold)

Este roteiro aplica o mesmo encadeamento dos itens 1–4 deste guia a um **pipeline de dados em camadas**. Os caminhos de arquivo são exemplos: adapte ao seu repositório. Para aprofundar padrões Medallion no Cursor, você pode reforçar o contexto com **`@.cursor/agents/data-engineering/medallion-architect.md`** (e, se for Spark on-prem, **`@.cursor/agents/data-engineering/spark-expert-on-premises.md`**).

### Cenário

Implementar um fluxo que: **ingere dados na camada raw/landing**, materialize **Bronze** (histórico fiel ou quase bruto), refine **Silver** (modelo de domínio, limpeza, chaves) e publique **Gold** (métricas e visões analíticas), com **qualidade, governança e operação** explícitas no `PROMPT_*.md`.

**Lembrete:** reunião + design **não** selecionam agentes sozinhos; o **PROMPT** gerado no Passo C (e revisado no C′) **deve nomear** `medallion-architect`, `spark-expert-on-premises`, etc., conforme a **§ 3.1 Escolha de agentes** neste guia.

### Passo A — Reunião → requisitos (`meeting-analyst`)

Use [`.cursor/agents/communication/metting-analyst.md`](../.cursor/agents/communication/metting-analyst.md) para transformar notas em um documento com sufixo **`requirements`** (ex.: `./design/pipeline_medallion_requirements.md`). Peça explicitamente:

- **Fontes:** sistemas, donos, volume e crescimento esperado, janela de carga (batch/streaming), SLA de disponibilidade.
- **Dados:** grain esperado, chaves naturais, PII, retenção legal, timezone e moeda.
- **Consumo:** quem usa Gold (BI, API, ML), latência aceitável, formatos de saída.
- **Restrições:** orquestrador (Airflow, Databricks Jobs, etc.), cluster Spark, custo, ambientes (dev/hml/prd).

### Passo B — Plano e arquitetura (`the-planner`)

Com [`.cursor/agents/communication/the-planner.md`](../.cursor/agents/communication/the-planner.md), gere o arquivo com sufixo **`design`** (ex.: `./design/pipeline_medallion_design.md`) cobrindo:

| Tema | O que não deixar vago |
|------|------------------------|
| **Raw/Landing** | Layout de paths, particionamento por ingestão, imutabilidade vs reprocessamento, metadados de ingestão (run_id, source_ts). |
| **Bronze** | Espelho do source + colunas técnicas; estratégia de deduplicação/late data; formato de tabela (Delta/Iceberg/Hive). |
| **Silver** | Modelo de entidades, regras de negócio, SCD (tipo 1/2), integridade referencial e testes de grain. |
| **Gold** | Fatos/dimensões ou wide tables, agregações, métricas oficiais, desempenho de consulta. |
| **Qualidade** | Regras por camada (completude, unicidade, ranges), quem é notificado em falha. |
| **Segurança** | Classificação de dados, mascaramento/tokenização, permissões por camada. |

### Passo C — Craft do `PROMPT_*.md` (`prompt-crafter`)

Inclua no contexto do chat **`@…_requirements.md`** e **`@…_design.md`** e use **`/dev "Gere PROMPT_…"`** (ou `@prompt-crafter`) pedindo um PROMPT que:

1. Liste **tarefas ordenadas por risco** (ex.: primeiro contratos e raw; depois silver; por último gold e otimização).
2. Para cada tarefa, defina **verificação objetiva** (comando, teste ou assert) — alinhado ao executor do Dev Loop.
3. **Nomeie agentes por tarefa** — não basta descrever o pipeline no design: o **PROMPT** precisa deixar explícito **qual** agente executa **qual** parte (ver **§ 3.1 Escolha de agentes** neste guia).

**Input mínimo para o prompt-crafter:** requisitos consolidados + design técnico + (recomendado) trechos de **`CONTEXT.md`** e convenções de pastas do projeto.

**Exemplo de instrução extra ao prompt-crafter (cole adaptando):**

```text
No PROMPT_*.md, inclua tarefas que invoquem explicitamente:
- @medallion-architect (ou o arquivo @.cursor/agents/data-engineering/medallion-architect.md)
  para decisões de camadas Raw/Bronze/Silver/Gold e contratos entre camadas;
- @spark-expert-on-premises para jobs PySpark, JDBC, vault, alinhados ao CONTEXT.md;
- @python-developer para módulos Python reutilizáveis e testes;
- @test-generator onde houver suíte de testes obrigatória.

Cada tarefa deve ser verificável (comando ou teste). Evite tarefas genéricas sem agente quando o risco for arquitetural ou de plataforma.
```

**Opcional antes do craft:** se não tiver certeza da lista de agentes, uma conversa com **`/core/agent`** (“pipeline Medallion on-prem com Spark”) pode sugerir papéis; depois **copie** essa escolha para a instrução acima.

### Passo C′ — Revisar o `PROMPT_*.md` antes de executar

1. Abra o arquivo gerado em `.cursor/dev/tasks/PROMPT_*.md`.
2. Confira se **tarefas de arquitetura Medallion** citam `medallion-architect` e se **Spark/on-prem** citam `spark-expert-on-premises` (ou o agente que o time padronizar).
3. Se faltar, edite o markdown ou peça ao assistente: “Ajuste o PROMPT para incluir `@medallion-architect` nas tarefas X e Y.”
4. Só então rode o executor (Passo D).

### Passo D — Executar o loop

```text
/dev tasks/PROMPT_PIPELINE_MEDALLION.md --dry-run
/dev tasks/PROMPT_PIPELINE_MEDALLION.md
```

Use **`--resume`** se a sessão interromper; acompanhe `.cursor/dev/progress/` e `.cursor/dev/logs/`.

### Checklist de engenharia de dados (não esquecer na elaboração)

Use esta lista ao revisar o `requirements`, o `design` e o `PROMPT_*.md` (ou peça ao assistente para mapear cada item a uma tarefa verificável).

**Ingestão e Raw**

- Contrato com a fonte (schema evolution, breaking changes, CDC vs snapshot).
- Idempotência e reprocessamento (mesma janela reexecutada sem duplicar negócio).
- Particionamento e nomes de path previsíveis (`year/month/day` ou `ingestion_date`).
- Metadados: `ingested_at`, `source_system`, `batch_id` / `watermark`.

**Bronze**

- Preservar histórico conforme política (append-only vs snapshots).
- Tipagem explícita na leitura; tratar nulls e formatos estranhos sem “perder” linha silenciosamente.
- Deduplicação e ordem de eventos se houver múltiplas entregas.

**Silver**

- Grain documentado por tabela; chaves surrogate vs naturais.
- Regras de limpeza e padronização (datas, moedas, códigos).
- SCD e “última versão” para consumo; testes de integridade entre entidades.
- PII: minimização, mascaramento ou segregação antes de Gold público.

**Gold**

- Definição única de métricas (nome, fórmula, dimensões permitidas) — evitar KPIs divergentes.
- Agregações alinhadas ao uso (BI vs API); materialização vs view.
- Compatibilidade com SLA de consulta (particionamento, Z-order/bloom onde aplicável).

**Qualidade e testes**

- Regras declaradas (Great Expectations, `assert` em job, DQ em SQL) **por camada**.
- Dados sintéticos ou subset para dev; testes de regressão em mudanças de schema.

**Operação e observabilidade**

- Retry, timeout, circuit breaker onde couber; alertas em falha de SLA ou drift de volume.
- Logs estruturados sem dados sensíveis; rastreio de `run_id` ponta a ponta.

**Governança e compliance**

- Ownership, catálogo de dados, lineage (origem → Gold).
- Retenção, LGPD/GDPR e bases legais quando houver dados pessoais.

**Performance e custo (especialmente Spark/lake)**

- Evitar shuffle desnecessário; reparticionar com critério; tamanho alvo de arquivo.
- Broadcast joins só quando seguro; skew e salting se necessário.

---

## Referência rápida do fluxo

**Com workflow (preferido):**

```text
0. /workflow-dev-loop
1. /devloop-init <RUN_ID>
2. /devloop-phase <RUN_ID> gate
3. /devloop-phase <RUN_ID> requirements → design → craft → prompt_review
4. /devloop-execute <RUN_ID>
5. /devloop-phase <RUN_ID> reflect
6. /devloop-round | /devloop-fixer (se necessário)
```

**Manual (sem RUN):**

```text
0. Escolher L2 (Dev Loop) vs L3 (SDD) — tabela no início deste guia
1. @meeting-analyst → salvar *requirements*.md
2. @the-planner → salvar *design*.md (a partir dos requirements)
3. @design + @requirements → /dev "Gere PROMPT_…" (ver Passo 3)
4. /dev tasks/PROMPT_*.md [--dry-run | --resume | --mode afk]
5. Acompanhar .cursor/dev/progress/ e .cursor/dev/logs/
```

Para um passo a passo aplicado a **Raw/Bronze/Silver/Gold**, veja neste documento a seção **Exemplo prático: pipeline Medallion (Raw → Bronze → Silver → Gold)**.

---

## Ver também

| Recurso | Caminho |
|---------|---------|
| Comando `/dev` (oficial) | `.cursor/commands/dev/dev.md` |
| Executor: tarefas e invocação de agentes | `.cursor/agents/dev/dev-loop-executor.md` |
| Lista de agentes e nomes | `HOW_TO_USE_AGENTS.md` |
| Roteamento opcional (`/core/agent`) | `.cursor/commands/core/router.md`, `.cursor/commands/core/agent.md` |
| Visão Nível 2 / pastas | `.cursor/dev/_index.md` (se existir) |
| Espectro Nível 1–3 | Seção *Development Spectrum* em `dev.md` |
| Onboarding | `START_HERE.md` |

---

*Este guia complementa o fluxo oficial; em caso de divergência, prevalecem `dev.md` e o comportamento atual do Cursor no repositório.*
