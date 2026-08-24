# Agent Router

## Objetivo

Este arquivo define como selecionar o agente mais apropriado para cada solicitação dentro deste projeto.

O roteador deve sempre:

1. identificar a intenção principal do pedido
2. identificar o entregável principal esperado
3. escolher um agente primário
4. opcionalmente escolher agentes de apoio
5. instruir a abertura do arquivo do agente primário em `.claude/agents/`
6. manter a resposta consistente com o escopo do agente escolhido

---

## Idioma padrão

Sempre responder em **português brasileiro**, salvo se o usuário pedir explicitamente outro idioma.

---

## Manutenção deste roteador e do contexto (obrigatório ao evoluir o projeto)

### Atualizar **este** arquivo (`.claude/commands/core/router.md`)

Durante o desenvolvimento, **agentes e colaboradores** devem manter este roteador coerente com o repositório:

- registrar **novos agentes** ou remover entradas obsoletas na seção **Agentes registrados**
- ajustar **prioridades em solicitações mistas** e **combinações** quando surgirem fluxos ou domínios novos
- preencher ou revisar a seção **Agente expert do repositório** quando existir um especialista dedicado ao produto deste repo

**Objetivo:** o roteamento continuar preciso e o uso dos agentes, o melhor possível, à medida que o projeto muda.

### Alinhamento com outros artefatos do Cursor

Quando uma entrega alterar comandos, estrutura, convenções ou troubleshooting recorrente, atualize também (ou proponha atualização em PR):

| Arquivo | Finalidade |
|---------|------------|
| `.cursorrules` | Regras carregadas automaticamente na raiz |
| `.claude/CURSOR.MD` | Contexto ampliado do repositório |
| `CONTEXT.md` | Onboarding rápido na raiz |

**Definition of Done (processo do time):** toda entrega que mude **como o projeto é executado, navegado ou depurado** deve ir acompanhada de PR (ou commit na mesma entrega) atualizando pelo menos **`CONTEXT.md`** e, quando fizer sentido, **`.cursorrules`** e **`.claude/CURSOR.MD`**; se a mudança afetar **cadastro de agentes ou prioridades de roteamento**, atualize também **este `router.md`**. O objetivo é que humanos e assistente permaneçam alinhados ao repositório real, sem depender só dos lembretes nos arquivos dos agentes.

---

## Regra operacional obrigatória

Após selecionar o agente primário, deve-se:

1. abrir o arquivo markdown do agente primário dentro de `.claude/agents/`
2. usar esse arquivo como instrução principal de comportamento, escopo e estilo
3. consultar a knowledge base relevante em `.claude/kb/` quando aplicável
4. usar agentes de apoio apenas quando houver ganho claro

---

## Agente expert do repositório (opcional)

> **Personalize:** ao criar um agente focado no domínio do **produto** deste repositório, registre o caminho abaixo. Se ainda não existir, deixe o placeholder ou remova a linha da tabela até o arquivo existir.

| Campo | Valor |
|-------|--------|
| **Arquivo** | `.claude/agents/<pasta>/<nome>-expert.md` |
| **Usar quando** | Dúvidas estritamente sobre o pipeline, jobs, execução, logs, parâmetros e troubleshooting **específicos deste projeto** |
| **Sinais típicos** | `<ex.: nomes de jobs, pastas em scripts/, padrões de log, parâmetros CLI do produto>` |

Se nenhum agente expert estiver definido ou a pergunta for genérica (só Spark, só Python, etc.), siga as seções por **domínio técnico** abaixo.

---

## Princípios gerais de roteamento

- Sempre escolher **um agente primário**
- Agentes de apoio podem ser usados quando a tarefa envolver múltiplos domínios
- Preferir o agente **mais especializado** em vez de um agente genérico
- Em caso de ambiguidade, usar o **entregável principal** como critério de decisão
- Quando nenhum agente especializado se encaixar claramente, usar um agente da área `dev`
- Sempre referenciar o **caminho completo** do agente selecionado
- Se a solicitação for **claramente** sobre o produto deste repositório e existir **agente expert** registrado acima, escolhê-lo como primário

---

## Processo de decisão

Para cada solicitação:

1. identificar o **resultado principal** que o usuário quer
2. identificar o **domínio técnico principal**
3. escolher o agente mais especializado nesse domínio
4. se a tarefa cruzar domínios, escolher um agente primário e no máximo dois agentes de apoio
5. abrir o arquivo do agente primário selecionado
6. consultar KB relevante, se necessário
7. se a solicitação for claramente sobre o **produto/pipeline deste repo** e houver **agente expert** na tabela opcional, usá-lo como primário
8. se ainda houver dúvida, usar um agente de `dev`

---

## Agentes registrados

### AI/ML
- `.claude/agents/ai-ml/ai-data-engineer.md`
- `.claude/agents/ai-ml/ai-prompt-specialist.md`
- `.claude/agents/ai-ml/genai-architect.md`
- `.claude/agents/ai-ml/crewai-builder.md`
- `.claude/agents/ai-ml/llm-specialist.md`

### Code quality
- `.claude/agents/code-quality/code-cleaner.md`
- `.claude/agents/code-quality/code-documenter.md`
- `.claude/agents/code-quality/code-reviewer.md`
- `.claude/agents/code-quality/dual-reviewer.md`
- `.claude/agents/code-quality/python-developer.md`
- `.claude/agents/code-quality/test-generator.md`

### Communication
- `.claude/agents/communication/adaptive-explainer.md`
- `.claude/agents/communication/metting-analyst.md`
- `.claude/agents/communication/the-planner.md`

- `.claude/agents/communication/aide-slide-builder.md`
- `.claude/agents/communication/aide-slide-fixer.md`
- `.claude/agents/communication/aide-slide-planner.md`
- `.claude/agents/communication/aide-slide-reviewer.md`
- `.claude/agents/communication/icatu-slide-planner.md`
- `.claude/agents/communication/icatu-slide-builder.md`
- `.claude/agents/communication/icatu-slide-reviewer.md`
- `.claude/agents/communication/icatu-slide-fixer.md`

### Data engineering
- `.claude/agents/data-engineering/lakeflow-architect.md`
- `.claude/agents/data-engineering/lakeflow-expert.md`
- `.claude/agents/data-engineering/lakeflow-pipeline-builder.md`
- `.claude/agents/data-engineering/medallion-architect.md`
- `.claude/agents/data-engineering/spark-expert.md`
- `.claude/agents/data-engineering/spark-expert-on-premises.md`
- `.claude/agents/data-engineering/spark-performance-analyzer.md`
- `.claude/agents/data-engineering/spark-specialist.md`
- `.claude/agents/data-engineering/spark-streaming-architect.md`
- `.claude/agents/data-engineering/spark-troubleshooter.md`

### Dev
- `.claude/agents/dev/dev-loop-executor.md`
- `.claude/agents/dev/prompt-crafter.md`

### Domain
- `.claude/agents/domain/dataops-builder.md`
- `.claude/agents/domain/extraction-specialist.md`
- `.claude/agents/domain/function-developer.md`
- `.claude/agents/domain/infra-deployer.md`
- `.claude/agents/domain/pipeline-architect.md`
- `.claude/agents/domain/sql-capacity-expert.md`
- `.claude/agents/domain/key-oci-expert.md`
- `.claude/agents/domain/teams-notifications-expert.md`

### Exploration
- `.claude/agents/exploration/agent-architect.md`
- `.claude/agents/exploration/codebase-explorer.md`
- `.claude/agents/exploration/kb-architect.md`

### Workflow
- `.claude/agents/workflow/brainstorm-agent.md`
- `.claude/agents/workflow/build-agent.md`
- `.claude/agents/workflow/define-agent.md`
- `.claude/agents/workflow/design-agent.md`
- `.claude/agents/workflow/iterate-agent.md`
- `.claude/agents/workflow/ship-agent.md`

---

## Regras de seleção por domínio

# 1. Spark, PySpark, Databricks, Delta Lake, Lakeflow e pipelines

## Seleção principal

### Workflow estruturado: `/workflow-data-pipeline-review`
Usar quando o usuário pedir **review/auditoria de pipeline de dados por dimensões**: contratos, medallion, qualidade, idempotência, observabilidade, performance, segurança ou IA/ML/DataOps.

Referência: `.claude/commands/workflow-data-pipeline-review/workflow-data-pipeline-review.md`.

### `.claude/agents/data-engineering/spark-expert.md`
Usar para perguntas gerais sobre Spark e PySpark:
- transformação de dados
- leitura e escrita
- DataFrame API
- performance geral
- arquitetura Spark
- jobs batch

### `.claude/agents/data-engineering/spark-expert-on-premises.md`
Usar quando o foco incluir **PySpark neste repositório** combinado com cluster Spark **on-premises**, JDBC, integração com vault de secrets ou padrões operacionais locais descritos na KB ou no código (valores de host e layout: ver `CONTEXT.md`).

### `.claude/agents/data-engineering/spark-performance-analyzer.md`
Usar quando o foco principal for:
- tuning de performance Spark
- partitions
- shuffle
- skew
- cache
- broadcast join
- explain plan
- gargalos de execução

### `.claude/agents/data-engineering/spark-streaming-architect.md`
Usar quando a pergunta for sobre:
- streaming
- Structured Streaming
- ingestão contínua
- micro-batches
- checkpoints
- pipelines near-real-time

### `.claude/agents/data-engineering/spark-troubleshooter.md`
Usar quando o foco for:
- erro em execução Spark
- stack trace
- falha de job
- problema operacional
- debug de pipeline Spark

### `.claude/agents/data-engineering/spark-specialist.md`
Usar quando a pergunta for técnica de Spark, mas não estritamente de troubleshooting, performance ou streaming, e exigir visão especializada mais geral.

### `.claude/agents/data-engineering/lakeflow-architect.md`
Usar para:
- arquitetura com Lakeflow
- desenho conceitual
- organização de camadas e fluxos

### `.claude/agents/data-engineering/lakeflow-expert.md`
Usar para:
- dúvidas práticas e específicas sobre Lakeflow
- implementação, configuração e uso

### `.claude/agents/data-engineering/lakeflow-pipeline-builder.md`
Usar quando o usuário quer:
- construir pipeline
- gerar código/pipeline em Lakeflow
- receber estrutura pronta

### `.claude/agents/data-engineering/medallion-architect.md`
Usar para:
- Bronze / Silver / Gold
- arquitetura medalhão
- organização de camadas
- estratégia de qualidade e refino de dados

## Agentes de apoio comuns
- `.claude/agents/domain/pipeline-architect.md`
- `.claude/agents/domain/extraction-specialist.md`
- `.claude/agents/communication/adaptive-explainer.md`
- `.claude/agents/code-quality/python-developer.md`

---

# 2. Qualidade de código, refatoração, revisão e testes

## Seleção principal

### `.claude/agents/code-quality/code-cleaner.md`
Usar para:
- limpeza de código
- simplificação
- remoção de redundância
- melhoria de legibilidade

### `.claude/agents/code-quality/code-reviewer.md`
Usar para:
- review técnico
- avaliação de boas práticas
- identificar riscos e melhorias

### `.claude/agents/code-quality/dual-reviewer.md`
Usar quando quiser uma revisão mais crítica, comparativa ou em múltiplas perspectivas.

### `.claude/agents/code-quality/code-documenter.md`
Usar para:
- documentar código
- gerar comentários
- explicar módulos e funções

### `.claude/agents/code-quality/python-developer.md`
Usar para:
- desenvolvimento Python
- estruturação de classes/funções
- implementação
- boas práticas Python

### `.claude/agents/code-quality/test-generator.md`
Usar para:
- criar testes unitários
- criar testes de integração
- sugerir cenários de teste

## Agentes de apoio comuns
- `.claude/agents/exploration/codebase-explorer.md`
- `.claude/agents/communication/adaptive-explainer.md`

---

# 3. Comunicação, documentação, explicação e planejamento textual

## Seleção principal

### `.claude/agents/communication/adaptive-explainer.md`
Usar para:
- explicar conceitos técnicos
- adaptar linguagem ao público
- transformar conteúdo técnico em linguagem mais clara
- documentação explicativa

### `.claude/agents/communication/metting-analyst.md`
Usar para:
- resumo de reunião
- análise de atas
- organização de decisões e próximos passos

### `.claude/agents/communication/the-planner.md`
Usar para:
- organizar planos
- criar roadmap textual
- estruturar entregas, fases, cronogramas e próximos passos

### Slides HTML — AIDE (Formação) vs Icatu (corporativo)

### `.claude/agents/communication/aide-slide-builder.md`
Usar para:
- decks da **Formação AI Data Engineer** (paleta AIDE / Semana), lições `AL-*`, `PR-*`, pastas `presentation/l0-*` / `l1-*` com design system **aide-slides**.

### `.claude/agents/communication/icatu-slide-planner.md`
Usar para:
- **planear** apresentações Icatu antes do HTML: slide-map com tipos `slide--icatu-*`, chunks, padrões de layout e paleta oficial (KB `icatu-slides` + PDFs em `templates/ppts/ICATU/`); **não** gera HTML.

### `.claude/agents/communication/icatu-slide-builder.md`
Usar para:
- apresentações no **padrão visual Icatu** (KB `icatu-slides`, PDFs em `templates/ppts/ICATU/`, logo em `templates/ppts/ICATU/assets/`);
- trilhas ou comunicações internas quando o utilizador pedir explicitamente **Icatu**, **marca corporativa** ou ficheiros dessa KB — **não** misturar cyan/gold AIDE como identidade principal.

### `.claude/agents/communication/icatu-slide-reviewer.md`
Usar para:
- **revisão independente (read-only)** de HTML Icatu já gerado: paleta oficial, anti-vazamento AIDE, barra/logo, tipografia Roboto/Arial, motor de slides, pt-BR e checklist de conferência com os **PDFs** do template.

### `.claude/agents/communication/icatu-slide-fixer.md`
Usar para:
- aplicar **correções mecânicas** (diff mínimo) com base no relatório do `icatu-slide-reviewer`: hex/paleta, acentos PT, pequenos atributos CSS/JS — **sem** regerar o deck; escalar para `icatu-slide-builder` quando faltar estrutura (SlideEngine, barra completa, slides novos).

## Agentes de apoio comuns
- qualquer agente técnico primário, quando a saída precisar ser convertida em texto executivo ou documentação

---

# 4. IA, LLM, RAG, prompts e arquitetura GenAI

## Seleção principal

### `.claude/agents/ai-ml/llm-specialist.md`
Usar para:
- dúvidas sobre LLMs
- uso de modelos
- escolha de modelos
- integração com APIs de modelos

### `.claude/agents/ai-ml/genai-architect.md`
Usar para:
- arquitetura de soluções GenAI
- desenho de plataformas de IA
- agentes, RAG, componentes, segurança e integração

### `.claude/agents/ai-ml/crewai-builder.md`
Usar para:
- código e desenho **específicos do framework CrewAI** (Python): `Agent`, `Task`, `Crew`, `Process`, tools (`@tool`), `kickoff`, fluxos sequenciais ou hierárquicos
- quando o utilizador mencionar **CrewAI**, **crew**, **Task/Agent** no sentido da biblioteca — **não** substituir `dataops-builder` quando o foco for monitorização + LangFuse + GCP

### `.claude/agents/ai-ml/ai-prompt-specialist.md`
Usar para:
- criação e melhoria de prompts
- system prompts
- instruções para agentes
- otimização de prompting

### `.claude/agents/ai-ml/ai-data-engineer.md`
Usar para:
- pipelines de dados voltados para IA
- ingestão/preparo de dados para IA
- embeddings, bases vetoriais, integração dados + IA

## Agentes de apoio comuns
- `.claude/agents/data-engineering/spark-expert.md`
- `.claude/agents/exploration/kb-architect.md`
- `.claude/agents/workflow/design-agent.md`

---

# 5. Arquitetura de domínio, extração, DataOps e deploy

## Seleção principal

### `.claude/agents/domain/dataops-builder.md`
Usar para:
- práticas de DataOps
- automação de ciclo de dados
- esteiras de dados
- organização operacional

### `.claude/agents/domain/extraction-specialist.md`
Usar para:
- extração de dados
- conectividade com fontes
- ingestão
- captura de dados de sistemas externos

### `.claude/agents/domain/function-developer.md`
Usar para:
- criação de funções utilitárias
- componentes reutilizáveis
- lógica encapsulada

### `.claude/agents/domain/infra-deployer.md`
Usar para:
- deploy
- infraestrutura
- configuração de execução
- ambiente operacional

### `.claude/agents/domain/pipeline-architect.md`
Usar para:
- desenho de pipelines
- definição estrutural
- blueprint de processos e fluxos

### `.claude/agents/domain/sql-capacity-expert.md`
Usar para:
- solicitações do projeto `sql-capacity-prd`
- execução de jobs SQL Capacity em PRD
- troubleshooting SQL Server, conectividade e SSL/TLS
- fallback manual e recuperação operacional guiada pela KB `sql-capacity`

### `.claude/agents/domain/key-oci-expert.md`
Usar para:
- módulo `src/utils/key_oci.py`, `return_secret`, `resolve_credential_value`
- Oracle OCI Vault, OCIDs de secrets e leitura via `.config`
- autenticação OCI (`~/.oci/config`, Resource Principal) em jobs PySpark, notebooks e bridge MCP (`resolve_oci_mcp.py`)

### `.claude/agents/domain/teams-notifications-expert.md`
Usar para:
- orquestrar **alertas Microsoft Teams** em pipelines (falhas, avisos de negócio, tabelas a partir de DataFrame)
- escolher webhook (`URL_WEBHOOK_SENTINEL`, `URL_WEBHOOK_TRILHA_AUDITORIA_*`, DSV vs PRD)
- `pymsteams`, `%pip`, secrets e integração em jobs/notebooks Databricks
- KB: `.claude/kb/teams-notifications/`

## Agentes de apoio comuns
- `.claude/agents/data-engineering/spark-expert.md`
- `.claude/agents/data-engineering/lakeflow-pipeline-builder.md`
- `.claude/agents/workflow/design-agent.md`

---

# 6. Exploração de código e base de conhecimento

## Seleção principal

### `.claude/agents/exploration/codebase-explorer.md`
Usar para:
- entender o repositório
- localizar arquivos
- navegar no código
- descobrir onde algo está implementado
- explicar a estrutura do projeto

### `.claude/agents/exploration/kb-architect.md`
Usar para:
- organizar knowledge base
- estruturar `.claude/kb`
- definir taxonomia de conhecimento
- melhorar documentação de contexto para agentes

### `.claude/agents/exploration/agent-architect.md`
Usar para:
- criar um novo arquivo de agente (Markdown) em `.claude/agents/`
- refatorar, padronizar ou dividir agentes existentes
- definir `name`, `description`, `tools`, exemplos `<example>` e categoria de pasta
- atualizar `router.md`, `HOW_TO_USE_AGENTS.md` e espelhos (`.github/`, `.claude/`) quando política do time exigir

## Agentes de apoio comuns
- `.claude/agents/communication/adaptive-explainer.md`
- `.claude/agents/code-quality/code-documenter.md`

---

# 7. Fluxos de trabalho, definição, design e entrega de agentes/processos

## Seleção principal

### `.claude/agents/workflow/brainstorm-agent.md`
Usar para:
- ideação inicial
- levantamento de possibilidades
- exploração de opções

### `.claude/agents/workflow/define-agent.md`
Usar para:
- definição de escopo
- clarificação de objetivo
- delimitação de requisitos

### `.claude/agents/workflow/design-agent.md`
Usar para:
- desenho da solução
- modelagem da abordagem
- estruturação conceitual

### `.claude/agents/workflow/build-agent.md`
Usar para:
- construção prática
- transformar definição em implementação

### `.claude/agents/workflow/iterate-agent.md`
Usar para:
- refinamento
- melhoria incremental
- evolução de solução existente

### `.claude/agents/workflow/ship-agent.md`
Usar para:
- empacotar entrega
- preparar versão final
- checklist de entrega

## Agentes de apoio comuns
- qualquer agente técnico ou de comunicação, dependendo do objeto do workflow

---

# 8. Desenvolvimento genérico e fallback

## Seleção principal

### `.claude/agents/dev/dev-loop-executor.md`
Usar quando:
- a solicitação for genérica de desenvolvimento
- não houver especialista claramente melhor
- o usuário quiser executar um loop prático de análise → ajuste → validação

### `.claude/agents/dev/prompt-crafter.md`
Usar quando:
- o foco principal for montar instruções
- estruturar prompt para IDE, LLM ou agentes
- melhorar texto de comando operacional

---

## Regras de prioridade em solicitações mistas

Quando uma pergunta envolver mais de um domínio, usar estas prioridades:

### Prioridade 1
Se o entregável principal for um pipeline de dados, usar o agente de `data-engineering` ou `domain` mais específico, como:
- `.claude/agents/data-engineering/lakeflow-pipeline-builder.md`
- `.claude/agents/data-engineering/spark-expert.md`
- `.claude/agents/domain/pipeline-architect.md`

### Prioridade 2
Se o entregável principal for revisão, refatoração ou melhoria de código, usar:
- `.claude/agents/code-quality/code-cleaner.md`
- `.claude/agents/code-quality/code-reviewer.md`
- `.claude/agents/code-quality/python-developer.md`

### Prioridade 3
Se o entregável principal for texto, documentação, resumo, explicação adaptada ou planejamento textual, usar:
- `.claude/agents/communication/adaptive-explainer.md`
- `.claude/agents/communication/metting-analyst.md`
- `.claude/agents/communication/the-planner.md`

### Prioridade 4
Se o foco principal for IA, LLM, RAG, prompting ou arquitetura GenAI, usar:
- `.claude/agents/ai-ml/llm-specialist.md`
- `.claude/agents/ai-ml/genai-architect.md`
- `.claude/agents/ai-ml/crewai-builder.md`
- `.claude/agents/ai-ml/ai-prompt-specialist.md`
- `.claude/agents/ai-ml/ai-data-engineer.md`

### Prioridade 5
Se o foco principal for organizar o próprio processo de criação, desenho, iteração ou entrega, usar:
- `.claude/agents/workflow/design-agent.md`
- `.claude/agents/workflow/build-agent.md`
- `.claude/agents/workflow/iterate-agent.md`

### Prioridade 6
Se nada se encaixar claramente, usar:
- `.claude/agents/dev/dev-loop-executor.md`

**Nota:** se existir **agente expert do repositório** registrado no início deste arquivo e a pergunta for **claramente** sobre o produto deste repo, essa escolha tem precedência sobre as prioridades genéricas acima.

---

## Regras de agentes de apoio

Agentes de apoio só devem ser considerados quando agregarem valor claro.

### Combinações comuns

#### Spark pipeline + arquitetura
Primário:
- `.claude/agents/data-engineering/spark-expert.md`
ou
- `.claude/agents/data-engineering/lakeflow-pipeline-builder.md`

Apoio:
- `.claude/agents/domain/pipeline-architect.md`

#### Pipeline + documentação
Primário:
- agente técnico correspondente

Apoio:
- `.claude/agents/code-quality/code-documenter.md`
ou
- `.claude/agents/communication/adaptive-explainer.md`

#### GenAI + knowledge base
Primário:
- `.claude/agents/ai-ml/genai-architect.md`

Apoio:
- `.claude/agents/exploration/kb-architect.md`

#### CrewAI (código Python da biblioteca)
Primário:
- `.claude/agents/ai-ml/crewai-builder.md`

Apoio:
- `.claude/agents/ai-ml/genai-architect.md` (visão de sistema, se o âmbito for maior que CrewAI)
- `.claude/agents/domain/dataops-builder.md` (se o foco for DataOps + LangFuse + GCP)

#### Refatoração + testes
Primário:
- `.claude/agents/code-quality/code-cleaner.md`
ou
- `.claude/agents/code-quality/python-developer.md`

Apoio:
- `.claude/agents/code-quality/test-generator.md`

---

## Regras de ambiguidade

Se a solicitação estiver ambígua:

1. inferir o domínio pelo entregável principal
2. preferir o agente mais especializado
3. se ainda houver dúvida, usar:
   - `.claude/agents/dev/dev-loop-executor.md`

Se a solicitação mencionar:
- arquivo
- pasta
- onde está implementado
- estrutura do projeto
- navegar no repositório

priorizar:
- `.claude/agents/exploration/codebase-explorer.md`

Se a solicitação mencionar:
- criar prompt
- melhorar instrução
- system prompt
- prompt para agente
- prompt para Cursor

priorizar:
- `.claude/agents/dev/prompt-crafter.md`
ou
- `.claude/agents/ai-ml/ai-prompt-specialist.md`

Se a solicitação mencionar:
- criar agente Cursor
- novo arquivo em `.claude/agents`
- scaffold de agente
- registrar agente no router
- meta-agente ou agente que cria agente

priorizar:
- `.claude/agents/exploration/agent-architect.md`

Se a solicitação mencionar:
- CrewAI
- crewai
- `Agent` / `Task` / `Crew` / `Process` no sentido da biblioteca Python CrewAI

priorizar:
- `.claude/agents/ai-ml/crewai-builder.md`

Se a solicitação mencionar:
- sql-capacity-prd
- sql capacity
- jobs SQL Capacity
- troubleshooting SQL Server deste domínio

priorizar:
- `.claude/agents/domain/sql-capacity-expert.md`

Se a solicitação mencionar:
- `key_oci` ou `key_oci.py`
- OCI Vault / Vault de secrets Oracle
- OCID de secret / resolução de OCID em credencial
- `.config` / `DEFAULT.env` no contexto de secrets do projeto
- bridge MCP `resolve_oci_mcp` / `resolve_credential_value`

priorizar:
- `.claude/agents/domain/key-oci-expert.md`

---

## Regras operacionais por tipo de pedido

### Se o usuário quer diagnosticar erro
Priorizar agente de troubleshooting ou especialista operacional do domínio.

### Se o usuário quer criar algo novo
Priorizar agente builder, architect ou specialist do domínio.

### Se o usuário quer revisar algo existente
Priorizar code-reviewer, code-cleaner ou especialista do domínio.

### Se o usuário quer entender o projeto
Priorizar:
- `.claude/agents/exploration/codebase-explorer.md`

### Se o usuário quer organizar conhecimento
Priorizar:
- `.claude/agents/exploration/kb-architect.md`

### Se o usuário quer criar ou manter agentes (arquivos `.md` em `.claude/agents`)
Priorizar:
- `.claude/agents/exploration/agent-architect.md`

### Se o usuário quer transformar conteúdo técnico em material de comunicação
Priorizar:
- `.claude/agents/communication/adaptive-explainer.md`

---

## Saída esperada após roteamento

Depois de escolher o agente primário, a resposta deve:

1. respeitar o escopo do agente escolhido
2. usar a terminologia correta do domínio
3. trazer passos práticos quando a pergunta for operacional
4. trazer código quando a pergunta exigir implementação
5. trazer explicação clara quando a pergunta exigir entendimento
6. manter consistência com a knowledge base e com o contexto do projeto

---

## Exemplos de roteamento

### Exemplo 1
Pergunta:
"Meu job PySpark falhou com erro de serialização ao usar uma função UDF; como depurar?"

Agente primário:
- `.claude/agents/data-engineering/spark-troubleshooter.md`

Agente de apoio:
- `.claude/agents/data-engineering/spark-expert.md`

---

### Exemplo 2
Pergunta:
"quero criar um pipeline spark para ingestão incremental"

Agente primário:
- `.claude/agents/data-engineering/spark-expert.md`

Agente de apoio:
- `.claude/agents/domain/pipeline-architect.md`

---

### Exemplo 3
Pergunta:
"melhore esse texto para enviar ao gestor"

Agente primário:
- `.claude/agents/communication/adaptive-explainer.md`

---

### Exemplo 4
Pergunta:
"gere testes unitários para essa função em python"

Agente primário:
- `.claude/agents/code-quality/test-generator.md`

Agente de apoio:
- `.claude/agents/code-quality/python-developer.md`

---

### Exemplo 5
Pergunta:
"quero estruturar uma base de conhecimento para meus agentes no cursor"

Agente primário:
- `.claude/agents/exploration/kb-architect.md`

Agente de apoio:
- `.claude/agents/ai-ml/genai-architect.md`

---

### Exemplo 6
Pergunta:
"qual agente devo usar para desenhar um workflow de build e iteração?"

Agente primário:
- `.claude/agents/workflow/design-agent.md`

Agente de apoio:
- `.claude/agents/workflow/iterate-agent.md`

---

### Exemplo 7
Pergunta:
"quero criar um agente novo para revisar pipelines dbt"

Agente primário:
- `.claude/agents/exploration/agent-architect.md`

Agente de apoio (se o foco for o conteúdo técnico do pipeline no corpo do agente):
- agente de dados ou domínio equivalente ao stack (ex.: especialista do pipeline usado)

---

## Regra final

Se, após aplicar as regras acima, ainda houver dúvida sobre o agente primário, usar:

- `.claude/agents/dev/dev-loop-executor.md`

E **atualizar este roteador** quando um padrão de dúvida se repetir, registrando o agente correto na seção apropriada.
