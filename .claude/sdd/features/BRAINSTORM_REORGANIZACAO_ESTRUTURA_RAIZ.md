# BRAINSTORM: Reorganização da Estrutura de Pastas da Raiz

**Data:** 2026-09-21
**Origem:** Pedido direto do usuário via `/devloop-phase` → gate decidiu `escalate_sdd` (ver
`.claude/sdd/dev-loop-runs/reorg-estrutura-raiz/phases/gate.md`) → `/brainstorm`.
**Status:** ✅ Ready for Define

---

## Initial Idea

Organizar a estrutura de pastas na raiz do projeto, agrupando assuntos semelhantes para reduzir a
dispersão atual (raiz hoje tem ~40 entradas de topo), seguindo boas práticas de mercado. Pedido
aberto — usuário pediu análise e sugestões, não uma solução pré-definida.

## Contexto do projeto observado

- Pipeline de dados multi-cloud (portfolio): ingestão AWS (Fase 2 — DMS/Kinesis/DataSync/Lambdas),
  Azure (Fase 1 — Event Hubs/ADLS/Synapse) e GCP (Fase 3 — Datastream/Dataflow/BigQuery), todas
  convergindo para um Lakehouse Databricks comum (Bronze → Silver → Gold, Unity Catalog).
- `docs/`, `infra/`, `sql/`, `src/`, `tests/` já tinham subpastas por nuvem (`aws/`, `azure/`,
  `gcp/`) — a dispersão está na raiz, não dentro dessas pastas.
- Havia trabalho não commitado (`git status`) concentrado exatamente nas partes Azure/GCP em
  andamento: `src/azure`, `infra/azure`, `docs/azure`, `docs/gcp`, `sql/gcp`, `tests/gcp`,
  `requirements-gcp.txt`, `deploy/`, além de `pipeline/bronze/*.sql` e `docker-compose.yml`.
- Pastas de ferramental agentic (`agentspec/`, `.agentspec-test/`, `get_started/`,
  `install_dev_loop/`, `templates/`) não são sobre dados/nuvem — são meta do próprio formato
  agentic do repositório.

## Discovery Questions & Answers

| # | Pergunta | Resposta | Impacto |
|---|----------|----------|---------|
| 1 | Critério principal de agrupamento do topo | **Por nuvem (aws/azure/gcp) no topo** — inverte a hierarquia atual | Define o eixo principal: `aws/`, `azure/`, `gcp/` viram agrupadores de topo, cada um com `docs/infra/sql/src/tests` por dentro |
| 2 | Onde fica o que é comum às 3 nuvens (pipeline Databricks, gen/, mongo/, scripts/, docs comuns) | **Pasta `shared/` ao lado de aws/azure/gcp** | Cria 4º agrupador de topo para o cross-cloud |
| 3 | Onde ficam as pastas de ferramental agentic (agentspec/, get_started/, install_dev_loop/, templates/) | **Ficam soltas na raiz, fora do reagrupamento** | Escopo do reorg não toca ferramental agentic |
| 4 | Quando a movimentação física (git mv) deve acontecer, dado trabalho não commitado nas mesmas pastas | **Só depois de commitar/`/ship`ar o trabalho em andamento** (Azure Fase 1 / GCP Fase 3) | `/build` deste reorg fica agendado para depois do ship do trabalho em curso — não misturar refactor estrutural com commit de feature |
| 5 | Referência de estrutura de mercado a seguir | Post do LinkedIn (config/, data/, docs/, etl/, pipelines/, src/, tests/ — genérico, sem multi-cloud/lakehouse) — usuário autorizou adotar só o que fizer sentido | Aproveitado: raiz limpa com só config/docs essenciais; `/config` centralizado. Descartado: `/data` local (não se aplica — dados vivem no Lakehouse/MinIO, não no repo) e `etl/`/`pipelines/` como nomes de topo (o eixo aqui é nuvem, não estágio) |
| 6 (follow-up) | Escopo e formato de `config/` | **`config/` único na raiz, com subpastas `aws/azure/gcp/shared` dentro** | 5º agrupador de topo; `docker-compose.yml`/`databricks.yml` continuam na raiz (convenção das ferramentas) mas passam a referenciar arquivos dentro de `config/` |
| 7 (follow-up) | Config inclui dependências (`requirements-*.txt`) e scripts de registro de conector? | **Não** — config é só dado de conexão/ambiente; dependências ficam junto do código da nuvem; scripts de automação não são config | Duas fronteiras claras: config ≠ dependências, config ≠ script executável |
| 8 (follow-up) | Abrangência do princípio "scripts executáveis ficam em `scripts/`" | **Vale para todo o repositório, exceto `agentspec/` e `install_dev_loop/`; organizados por assunto dentro de `scripts/`** | `scripts/` vira 6º agrupador de topo (paralelo a `config/`), com subpastas por assunto (`scripts/debezium/`, `scripts/generators/`, etc.) |

## Approaches Explored

### Approach A: Cloud-first no topo + `shared/` + `config/` + `scripts/` ⭐ Selecionada

**O que faz:** 6 agrupadores de topo — `aws/`, `azure/`, `gcp/` (código/infra/docs/sql/tests
específicos de cada nuvem), `shared/` (Databricks Lakehouse + fontes on-prem comuns: `pipeline/`,
`mongo/`, `sql/oracle`, `gen/`, docs comuns), `config/` (só dado de conexão/ambiente, subdividido
por nuvem), `scripts/` (toda automação operacional, organizada por assunto). Ferramental agentic
(`agentspec/`, `get_started/`, `install_dev_loop/`, `templates/`) e arquivos de configuração de
ferramenta na raiz (`docker-compose.yml`, `databricks.yml`, `README.md` etc.) ficam inalterados.

**Pros:**
- Reflete o eixo que mais importa neste portfolio (comparar 3 estratégias de ingestão cloud lado a
  lado) — quem abre o repo vê imediatamente "aqui está AWS, aqui Azure, aqui GCP, aqui o que é
  comum".
- Config centralizada — muda conexão sem procurar em 5 pastas diferentes (dor que o usuário
  apontou explicitamente).
- Scripts centralizados por assunto — elimina scripts soltos em `debezium/`, `gen/`, `deploy/`.
- `debezium/` e `deploy/` como pastas soltas deixam de existir — seu conteúdo (config, scripts)
  passa a viver onde já é esperado (`config/`, `scripts/`).

**Cons:**
- Maior blast radius: praticamente todo path de infra/código/docs/sql/tests muda — exige atualizar
  referências em `docker-compose.yml`, DAGs, scripts, links de documentação e nos próprios arquivos
  agentic (`CONTEXT.md`, `.claude/CURSOR.MD`, router).
- Rompe a convenção comum de `src/`/`tests/`/`docs/` únicos na raiz (familiar para quem já viu
  outros repos Python) — trade-off aceito conscientemente pelo usuário em favor do eixo multi-cloud.

### Approach B: Function-first (manter `src/infra/sql/tests/docs`, só arrumar as pontas soltas)

**O que faz:** Mantém `src/`, `infra/`, `sql/`, `tests/`, `docs/` como estão hoje (já com
subdivisão aws/azure/gcp por dentro); cria só um `shared/` (ou `tooling/`) para as pastas
realmente soltas (`debezium/`, `gen/`, `mongo/`, `deploy/`, `templates/`).

**Por que não foi escolhida:** Diff bem menor e mais seguro, mas não resolve a dor central que o
usuário validou nas perguntas 1 e 6 — comparar as 3 nuvens continuaria exigindo abrir 5 pastas
diferentes, e não centraliza config. Descartada explicitamente na pergunta 1.

## Features Removed (YAGNI)

| Feature considerada | Motivo da remoção | Volta depois? |
|---|---|---|
| `/data` local (do template do LinkedIn) | Projeto não versiona dados localmente — vivem no Lakehouse/MinIO | Não |
| `etl/` / `pipelines/` como nomes de agrupador de topo | Eixo escolhido é nuvem, não estágio ETL; `shared/pipeline/` já cobre o Bronze/Silver/Gold | Não |
| Mover `docker-compose.yml`/`databricks.yml` para dentro de `config/` | Ferramentas (`docker compose`, Databricks CLI) esperam esses arquivos na raiz por padrão; mover exigiria flags extras no dia a dia sem ganho claro | Reavaliar se surgir necessidade real |
| Reorganizar `agentspec/`/`install_dev_loop/` junto com o resto | São ferramental do formato agentic, ciclo de vida e dono diferentes do pipeline de dados | Fica fora de propósito, não é "depois" |
| Fazer o `git mv` já nesta sessão | Há trabalho não commitado (Azure Fase 1 / GCP Fase 3) nas mesmas pastas — misturar refactor estrutural com commit de feature em andamento é anti-padrão de versionamento | Sim — assim que o trabalho em curso for commitado/`/ship`ado |
| `.env` ativo sair 100% da raiz | Docker Compose carrega `.env` da raiz por padrão; mover exige `--env-file` ou symlink — detalhe fino demais para o brainstorm | Decidir no `/design` |

## Validações incrementais realizadas

1. **Seção 1 (formato do topo, 4 agrupadores)** → usuário pediu para incluir `config/` → ajustado.
2. **Seção 1 revisada (5 agrupadores + fronteiras de config)** → usuário confirmou fronteiras e
   pediu para fechar `scripts/` como princípio geral → ajustado (6º agrupador).
3. **Seção 2 (mapeamento completo pasta a pasta)** → usuário confirmou: "Fechado".

## Anomalias observadas (não fazem parte do escopo de mapeamento, mas devem virar tarefa no `/define`)

- `gen/unified/uber-eats.json;C` — nome de arquivo com aparência de artefato/typo (não `.json`
  puro); confirmar se é lixo antes de mover.
- `__pycache__/` versionado em `tests/aws`, `tests/azure`, `src/aws`, `src/azure` — deveria estar
  no `.gitignore`; confirmar e remover do controle de versão.
- Documentação e arquivos agentic que citam paths antigos (`CONTEXT.md` tabela "Estrutura
  principal", `.claude/CURSOR.MD`, `.claude/commands/core/router.md`, `README.md`) precisam ser
  atualizados após o `git mv` — regra já prevista em `.claude/CLAUDE.md` ("Atualize documentação
  quando mudar execução, troubleshooting ou arquitetura").

## Draft Requirements (para `/define`)

**Escopo (in):**
- Criar 6 agrupadores de topo: `aws/`, `azure/`, `gcp/`, `shared/`, `config/`, `scripts/`.
- `git mv` de todo o conteúdo mapeado na Seção 2 (ver tabela completa na conversa / a ser
  detalhada em `DEFINE`), preservando histórico do Git.
- Atualizar toda referência quebrada: `docker-compose.yml`, `databricks.yml`, scripts que chamam
  paths antigos, links em `docs/`, `CONTEXT.md`, `.claude/CURSOR.MD`, router de agentes.
- Resolver as anomalias listadas acima antes ou durante o `git mv`.
- Critério de pronto: `python3 scripts/validate-agent-router.py` (ou seu novo path) passa; nenhum
  path antigo remanescente em referências ativas; `docker compose config` e `databricks bundle
  validate` (se aplicável) continuam funcionando.

**Escopo (out):**
- Não mexer em `agentspec/`, `.agentspec-test/`, `get_started/`, `install_dev_loop/`, `templates/`.
- Não mover `docker-compose.yml`/`databricks.yml` para fora da raiz.
- Não alterar lógica de pipeline, Terraform ou código de aplicação — só localização de arquivos.
- Não centralizar o `.env` ativo (fica decisão fina de `/design`).

**Constraint de execução:** este reorg só deve ser implementado (`/build`) depois que o trabalho
não commitado atual (Azure Fase 1 / GCP Fase 3, visível no `git status`) for commitado ou
`/ship`ado — evita misturar refactor estrutural com commit de feature em andamento.

**Quality tier:** production (é um portfolio que simula produção; caminho de rollback deve existir
— idealmente branch dedicada + PR revisável, dado o blast radius).

---

## Status: ✅ Ready for Define

**Próximo comando:** `/define .claude/sdd/features/BRAINSTORM_REORGANIZACAO_ESTRUTURA_RAIZ.md`
