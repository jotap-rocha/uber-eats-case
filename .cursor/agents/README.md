# Agents - Template Agentic SDD

Índice dos agentes em `.cursor/agents/`. Este diretório é parte do template agentic/SDD.

**Total: 76 agentes**

## Índice por pasta

### `ai-ml/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `ai-data-engineer` | [`ai-ml/ai-data-engineer.md`](ai-ml/ai-data-engineer.md) | Test automation expert for Python and Spark. Generates pytest unit tests, integration tests, and fixtures. Uses KB + … |
| `ai-prompt-specialist` | [`ai-ml/ai-prompt-specialist.md`](ai-ml/ai-prompt-specialist.md) | Expert Prompt Engineer for LLMs and multi-modal AI systems. Specializes in extraction, optimization, and structured o… |
| `crewai-builder` | [`ai-ml/crewai-builder.md`](ai-ml/crewai-builder.md) | Especialista em implementar equipas (crews) com o framework **CrewAI** em Python: Agent, Task, Crew, Process, tools e… |
| `genai-architect` | [`ai-ml/genai-architect.md`](ai-ml/genai-architect.md) | Elite GenAI Systems Architect specializing in multi-agent orchestration, agentic workflows, and production AI systems… |
| `llm-specialist` | [`ai-ml/llm-specialist.md`](ai-ml/llm-specialist.md) | Prompt engineering specialist and LLM expert. Masters structured prompting, chain-of-thought reasoning, and AI-powere… |

### `code-quality/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `code-cleaner` | [`code-quality/code-cleaner.md`](code-quality/code-cleaner.md) | Python code cleaning specialist. Removes excessive comments, applies DRY principles, and modernizes code. Uses KB + M… |
| `code-documenter` | [`code-quality/code-documenter.md`](code-quality/code-documenter.md) | Documentation specialist for creating comprehensive, production-ready documentation. Uses KB + MCP validation. Use PR… |
| `code-reviewer` | [`code-quality/code-reviewer.md`](code-quality/code-reviewer.md) | Expert code review specialist ensuring quality, security, and maintainability. Uses KB + MCP validation. Use PROACTIV… |
| `code-simplifier` | [`code-quality/code-simplifier.md`](code-quality/code-simplifier.md) | Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Focuses… |
| `dual-reviewer` | [`code-quality/dual-reviewer.md`](code-quality/dual-reviewer.md) | Dual AI code review specialist combining CodeRabbit + Cursor Code for maximum coverage. Uses CodeRabbit CLI for stati… |
| `python-developer` | [`code-quality/python-developer.md`](code-quality/python-developer.md) | Python code architect for data engineering and file parsing systems. Expert in clean code patterns, dataclasses, type… |
| `test-generator` | [`code-quality/test-generator.md`](code-quality/test-generator.md) | Test automation expert for Python and Spark. Generates pytest unit tests, integration tests, and fixtures. Uses KB + … |

### `communication/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `adaptive-explainer` | [`communication/adaptive-explainer.md`](communication/adaptive-explainer.md) | Master communicator that adapts explanations for any audience. Uses analogies, progressive disclosure, visuals, and c… |
| `aide-slide-builder` | [`communication/aide-slide-builder.md`](communication/aide-slide-builder.md) | Builds complete HTML slide decks for the Formacao AI Data Engineer using the AIDE design system. Reads lesson content… |
| `aide-slide-fixer` | [`communication/aide-slide-fixer.md`](communication/aide-slide-fixer.md) | Surgical correction agent for AIDE slide decks. Reads review reports from aide-slide-reviewer and applies targeted, m… |
| `aide-slide-planner` | [`communication/aide-slide-planner.md`](communication/aide-slide-planner.md) | Content architecture agent for AIDE slide decks. Decomposes lesson content into a structured slide-map before any HTM… |
| `aide-slide-reviewer` | [`communication/aide-slide-reviewer.md`](communication/aide-slide-reviewer.md) | Independent quality reviewer for AIDE slide decks. READ-ONLY — validates HTML presentations against 8 rule categories… |
| `icatu-slide-builder` | [`communication/icatu-slide-builder.md`](communication/icatu-slide-builder.md) | Constrói apresentações HTML em slides no padrão visual corporativo Icatu (paleta, tipografia Roboto, logo, geometrias… |
| `icatu-slide-fixer` | [`communication/icatu-slide-fixer.md`](communication/icatu-slide-fixer.md) | Agente de correção cirúrgica para decks HTML **marca Icatu**. Lê relatórios do icatu-slide-reviewer e aplica edições … |
| `icatu-slide-planner` | [`communication/icatu-slide-planner.md`](communication/icatu-slide-planner.md) | Agente de arquitetura de conteúdo para decks HTML **marca Icatu**. Decompõe briefings ou documentos num **slide-map**… |
| `icatu-slide-reviewer` | [`communication/icatu-slide-reviewer.md`](communication/icatu-slide-reviewer.md) | Revisor de qualidade independente para decks HTML **marca Icatu**. Somente LEITURA — valida o HTML contra a KB `icatu… |
| `metting-analyst` | [`communication/metting-analyst.md`](communication/metting-analyst.md) | Master communication analyst that transforms meeting notes, Slack threads, emails, and any communication into structu… |
| `the-planner` | [`communication/the-planner.md`](communication/the-planner.md) | Strategic AI architect that creates comprehensive implementation plans using real-time MCP intelligence. Uses KB + MC… |

### `data-engineering/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `airflow-dag-builder` | [`data-engineering/airflow-dag-builder.md`](data-engineering/airflow-dag-builder.md) | Gerar DAGs Airflow TaskFlow 2.11.x a partir do projeto e da KB airflow (medalhão, tags, Teams, permissões 314). |
| `big-data-cluster-expert` | [`data-engineering/big-data-cluster-expert.md`](data-engineering/big-data-cluster-expert.md) | Stack big data on-prem DATALAKE (311–314): Hadoop/YARN, Spark, Airflow 314, migration-hub, SSH, DAGs em `/DATALAKE/dags`. |
| `spark-cluster-migration-expert` | [`data-engineering/spark-cluster-migration-expert.md`](data-engineering/spark-cluster-migration-expert.md) | Migração operacional PySpark Standalone → YARN (311–314), portação de jobs, KB migration-hub. |
| `lakeflow-architect` | [`data-engineering/lakeflow-architect.md`](data-engineering/lakeflow-architect.md) | Databricks Lakeflow expert for building Medallion architecture pipelines. Creates Bronze/Silver/Gold layers with DLT.… |
| `lakeflow-expert` | [`data-engineering/lakeflow-expert.md`](data-engineering/lakeflow-expert.md) | Databricks Lakeflow (DLT) SME for pipeline development, CDC, data quality, and production deployment. Uses KB + MCP v… |
| `lakeflow-pipeline-builder` | [`data-engineering/lakeflow-pipeline-builder.md`](data-engineering/lakeflow-pipeline-builder.md) | Builds Databricks Lakeflow (DLT) pipelines for Medallion Architecture. Uses KB + MCP validation for production-ready … |
| `medallion-architect` | [`data-engineering/medallion-architect.md`](data-engineering/medallion-architect.md) | Seasoned Medallion Architecture expert with 10+ years of lakehouse experience. Provides strategic guidance, layer des… |
| `spark-expert` | [`data-engineering/spark-expert.md`](data-engineering/spark-expert.md) | Apache Spark SME focado em SparkSQL e PySpark para desenvolvimento de aplicações distribuídas, processamento de dados… |
| `spark-expert-on-premises` | [`data-engineering/spark-expert-on-premises.md`](data-engineering/spark-expert-on-premises.md) | Especialista PySpark para **repositórios** que rodam Spark on-premises (ex.: Standalone ou YARN), com integração típi… |
| `spark-performance-analyzer` | [`data-engineering/spark-performance-analyzer.md`](data-engineering/spark-performance-analyzer.md) | Spark performance analysis specialist for profiling, bottleneck detection, and optimization. Uses KB + MCP validation… |
| `spark-specialist` | [`data-engineering/spark-specialist.md`](data-engineering/spark-specialist.md) | Apache Spark SME for performance optimization, architecture design, and troubleshooting. Use PROACTIVELY when working… |
| `spark-streaming-architect` | [`data-engineering/spark-streaming-architect.md`](data-engineering/spark-streaming-architect.md) | Spark Structured Streaming expert for real-time pipelines, Kafka integration, and stream processing. Uses KB + MCP va… |
| `spark-troubleshooter` | [`data-engineering/spark-troubleshooter.md`](data-engineering/spark-troubleshooter.md) | Spark debugging and troubleshooting expert for resolving errors, failures, and production issues. Uses KB + MCP valid… |

### `databricks/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `databricks-data-engineer` | [`databricks/databricks-data-engineer.md`](databricks/databricks-data-engineer.md) | PySpark and Delta Lake specialist for batch ETL, medallion architecture, incremental loads, schema design, and Spark … |
| `databricks-genie-specialist` | [`databricks/databricks-genie-specialist.md`](databricks/databricks-genie-specialist.md) | Especialista em Databricks Genie Space (sala Genie): curadoria NL→SQL, knowledge store, instruções e exemplos SQL, Tr… |
| `databricks-ml-engineer` | [`databricks/databricks-ml-engineer.md`](databricks/databricks-ml-engineer.md) | MLflow, Mosaic AI Feature Store, and MLOps specialist for experiment tracking, model registry, feature engineering, m… |
| `databricks-pipeline-architect` | [`databricks/databricks-pipeline-architect.md`](databricks/databricks-pipeline-architect.md) | Lakeflow (DLT), Structured Streaming, Auto Loader, and Databricks Jobs specialist for declarative pipelines, event-dr… |
| `databricks-platform-engineer` | [`databricks/databricks-platform-engineer.md`](databricks/databricks-platform-engineer.md) | Databricks platform specialist for Unity Catalog governance, cluster management, security configuration, Databricks A… |
| `databricks-sql-analyst` | [`databricks/databricks-sql-analyst.md`](databricks/databricks-sql-analyst.md) | Databricks SQL specialist for SQL Warehouses, DBSQL dashboards, Delta SQL operations, query optimization, Lakehouse F… |

### `dev/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `big-data-orchestrator` | [`dev/big-data-orchestrator.md`](dev/big-data-orchestrator.md) | Orquestrador on-prem: spark-submit YARN, `config/spark.conf`, delegação entre especialistas Spark. |
| `python-project-architect` | [`dev/python-project-architect.md`](dev/python-project-architect.md) | Classificar projeto dados vs automação, layout OOP, KBs design-pipelines / design-automation. |
| `dev-loop-executor` | [`dev/dev-loop-executor.md`](dev/dev-loop-executor.md) | Dev Loop executor for Agentic Development (Level 2). Processes PROMPT_*.md files with verification loops, circuit bre… |
| `prompt-crafter` | [`dev/prompt-crafter.md`](dev/prompt-crafter.md) | Interactive PROMPT.md builder for Dev Loop (Agentic Development Level 2). Guides users through requirements gathering… |

### `domain/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `dataops-builder` | [`domain/dataops-builder.md`](domain/dataops-builder.md) | Autonomous DataOps specialist for building AI monitoring agents. Uses CrewAI for multi-agent orchestration, LangFuse … |
| `extraction-specialist` | [`domain/extraction-specialist.md`](domain/extraction-specialist.md) | LLM extraction expert for invoice document processing. Specializes in Gemini vision prompts, Pydantic output validati… |
| `function-developer` | [`domain/function-developer.md`](domain/function-developer.md) | Cloud Run function developer for the invoice processing pipeline. Builds Python serverless functions for image proces… |
| `infra-deployer` | [`domain/infra-deployer.md`](domain/infra-deployer.md) | Infrastructure deployment specialist for GCP serverless architectures. Uses Terraform modules and Terragrunt for mult… |
| `key-oci-expert` | [`domain/key-oci-expert.md`](domain/key-oci-expert.md) | Especialista no módulo `src/utils/key_oci.py` e no consumo de segredos do Oracle OCI Vault neste projeto. Use PROATIV… |
| `pipeline-architect` | [`domain/pipeline-architect.md`](domain/pipeline-architect.md) | Event-driven pipeline architect for GCP serverless data engineering. Designs Cloud Run functions, Pub/Sub topics, and… |
| `sql-capacity-expert` | [`domain/sql-capacity-expert.md`](domain/sql-capacity-expert.md) | Especialista no projeto **sql-capacity-prd** com foco em pipelines PySpark + SQL Server, execução em produção, troubl… |

### `exploration/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `agent-architect` | [`exploration/agent-architect.md`](exploration/agent-architect.md) | Especialista em projetar e implementar novos arquivos de agente Cursor (Markdown em `.cursor/agents/`). Use PROATIVAM… |
| `codebase-explorer` | [`exploration/codebase-explorer.md`](exploration/codebase-explorer.md) | Elite codebase analyst delivering Executive Summaries + Deep Dives. Use PROACTIVELY when exploring unfamiliar repos, … |
| `kb-architect` | [`exploration/kb-architect.md`](exploration/kb-architect.md) | Creates complete KB sections from scratch using MCP validation. EXECUTION-FOCUSED. Use PROACTIVELY when creating KB d… |

### `infra/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `web-edge-specialist` | [`infra/web-edge-specialist.md`](infra/web-edge-specialist.md) | Especialista na camada web na borda da aplicação — IIS (Windows), NGINX e Apache httpd (Linux): reverse proxy, TLS na… |

### `workflow/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `brainstorm-agent` | [`workflow/brainstorm-agent.md`](workflow/brainstorm-agent.md) | Collaborative exploration specialist for Phase 0 of SDD workflow. Use when starting a new feature with vague requirem… |
| `build-agent` | [`workflow/build-agent.md`](workflow/build-agent.md) | Implementation executor for Phase 3 of SDD workflow. Use when executing implementation from a DESIGN document, creati… |
| `define-agent` | [`workflow/define-agent.md`](workflow/define-agent.md) | Requirements extraction and validation specialist for Phase 1 of SDD workflow. Use when transforming brainstorm outpu… |
| `design-agent` | [`workflow/design-agent.md`](workflow/design-agent.md) | Architecture and technical specification specialist for Phase 2 of SDD workflow. Use when creating technical designs … |
| `iterate-agent` | [`workflow/iterate-agent.md`](workflow/iterate-agent.md) | Cross-phase document updater with cascade awareness. Use when changes are discovered during any SDD phase, when requi… |
| `ship-agent` | [`workflow/ship-agent.md`](workflow/ship-agent.md) | Feature archival and lessons learned specialist for Phase 4 of SDD workflow. Use when a feature build is complete, to… |

### `workflow-makeapp-review/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `makeapp-review-fixer` | [`workflow-makeapp-review/makeapp-review-fixer.md`](workflow-makeapp-review/makeapp-review-fixer.md) | Executa correções GUIADAS pelo usuário para findings de uma lane; atualiza código e OBRIGATORIAMENTE REVIEW_MANIFEST.… |
| `makeapp-review-init` | [`workflow-makeapp-review/makeapp-review-init.md`](workflow-makeapp-review/makeapp-review-init.md) | Inicia uma execução MakeApp Review: cria RUN_ID, REVIEW_MANIFEST.yaml e stubs lanes/ sob .cursor/sdd/reviews/{RUN_I… |
| `makeapp-review-lane` | [`workflow-makeapp-review/makeapp-review-lane.md`](workflow-makeapp-review/makeapp-review-lane.md) | Executa revisão de UMA lane por invocação (backend, frontend, security, databricks, performance, ui_ux): lê só CONTRA… |
| `makeapp-review-round` | [`workflow-makeapp-review/makeapp-review-round.md`](workflow-makeapp-review/makeapp-review-round.md) | Segunda passagem incremental: lê REVIEW_MANIFEST e pendências, reexecuta verificações rasas nas lanes não-pass ou afe… |

### `workflow-data-pipeline-review/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `data-pipeline-review-fixer` | [`workflow-data-pipeline-review/data-pipeline-review-fixer.md`](workflow-data-pipeline-review/data-pipeline-review-fixer.md) | Executa correções guiadas para findings de pipelines de dados e atualiza manifest, lanes e log. |
| `data-pipeline-review-init` | [`workflow-data-pipeline-review/data-pipeline-review-init.md`](workflow-data-pipeline-review/data-pipeline-review-init.md) | Inicia RUN de review de pipeline de dados com manifest e 11 stubs de lanes. |
| `data-pipeline-review-lane` | [`workflow-data-pipeline-review/data-pipeline-review-lane.md`](workflow-data-pipeline-review/data-pipeline-review-lane.md) | Revisa uma dimensão por invocação: contratos, medallion, qualidade, idempotência, observabilidade e mais. |
| `data-pipeline-review-round` | [`workflow-data-pipeline-review/data-pipeline-review-round.md`](workflow-data-pipeline-review/data-pipeline-review-round.md) | Revalida pendências e regressões após lanes ou fixers. |

### `workflow-dev-loop/`

| Agente | Ficheiro | Finalidade (resumo) |
|--------|----------|---------------------|
| `devloop-init` | [`workflow-dev-loop/devloop-init.md`](workflow-dev-loop/devloop-init.md) | Cria RUN L2 em `dev-loop-runs/{RUN_ID}/` com manifest, phases/ e artifacts/. |
| `devloop-phase` | [`workflow-dev-loop/devloop-phase.md`](workflow-dev-loop/devloop-phase.md) | Executa uma fase (gate → requirements → design → craft → prompt_review → reflect). |
| `devloop-execute` | [`workflow-dev-loop/devloop-execute.md`](workflow-dev-loop/devloop-execute.md) | Executa `PROMPT_{RUN_ID}.md` via dev-loop-executor após gate humano do PROMPT. |
| `devloop-round` | [`workflow-dev-loop/devloop-round.md`](workflow-dev-loop/devloop-round.md) | Revalida tarefas falhas após execução ou fixers. |
| `devloop-fixer` | [`workflow-dev-loop/devloop-fixer.md`](workflow-dev-loop/devloop-fixer.md) | Correção guiada de tarefa do PROMPT + atualização de estado do RUN. |

