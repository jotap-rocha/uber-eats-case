# Scripts de Automação — Uber Eats Data Pipeline

Scripts PowerShell para orquestrar a infraestrutura Docker local do projeto, mais um punhado de
scripts Python/Bash de suporte ao repositório agentic (validação, sync, bootstrap). Agrupados por
o que cada um liga/desliga — veja o índice abaixo para ir direto à categoria que precisa.

---

## Índice

1. [Infraestrutura base (bancos)](#1-infraestrutura-base-bancos)
2. [Ferramentas específicas sob demanda](#2-ferramentas-específicas-sob-demanda)
3. [Geração de dados — ShadowTraffic](#3-geração-de-dados--shadowtraffic)
4. [Tudo de uma vez](#4-tudo-de-uma-vez)
5. [Destrutivo](#5-destrutivo)
6. [Validação (repositório agentic/SDD)](#6-validação-repositório-agenticsdd)
7. [Outros utilitários](#7-outros-utilitários)
8. [Matriz de decisão rápida](#matriz-de-decisão-rápida)
9. [Requisitos e troubleshooting](#requisitos)

---

## 1. Infraestrutura base (bancos)

Sobe/derruba só os 4 bancos que tudo o resto depende: Postgres, Oracle, MinIO e Mongo. Não usa
licença do ShadowTraffic.

| Script | O que faz |
|--------|-----------|
| `infra/start-infra.ps1` | Liga o Docker Desktop se necessário, copia `shared/gen/.env` para a raiz e sobe `postgres-ubereats`, `oracle-ubereats`, `minio-ubereats`, `mongo-ubereats`. Base obrigatória antes de qualquer outro script desta lista. |
| `infra/stop-infra.ps1` | Para os 4 bancos (`docker-compose stop`), preservando os volumes. Avisa que ShadowTraffic e ingestão/CDC vão falhar se ainda estiverem rodando sem os bancos — desligue-os antes com os scripts da seção 2 e 3. |

```powershell
.\scripts\infra\start-infra.ps1
# ... trabalho local (queries, pipelines) ...
.\scripts\infra\stop-infra.ps1
```

---

## 2. Ferramentas específicas sob demanda

Ligam **uma peça isolada** da fábrica de dados — ingestão/CDC ou Airbyte — sem mexer nos bancos
nem no gerador. Requer a infra (seção 1) já de pé.

| Script | O que faz |
|--------|-----------|
| `infra/toggle-ingestion.ps1 on\|off\|status` | Liga/desliga a camada de ingestão: Redpanda + Kafka Connect (registra o connector Debezium Oracle se ainda não existir) + Airbyte (chama `start-airbyte.ps1`/`stop-airbyte.ps1` internamente, mesma pasta). `status` mostra o estado dos três e do connector. |
| `infra/start-airbyte.ps1` | Liga só o container `airbyte-abctl-control-plane` (abctl/kind), quando for configurar sources/destinations ou disparar um sync manual. UI em `http://localhost:8000`. |
| `infra/stop-airbyte.ps1` | Desliga o Airbyte. Ele não faz parte do `start-all.ps1`/`stop-all.ps1` porque consome bastante RAM/CPU e não precisa ficar de pé o tempo todo. Configuração de sources/destinations é preservada. |

```powershell
.\scripts\infra\start-infra.ps1
.\scripts\infra\toggle-ingestion.ps1 on
# ... configura/roda sync no Airbyte ...
.\scripts\infra\toggle-ingestion.ps1 off
```

---

## 3. Geração de dados — ShadowTraffic

> ⚠️ **Use sempre `toggle-shadowtraffic.ps1`, exceto em ambiente 100% novo.** As tabelas usam IDs
> sequenciais fixos no template (`shared/gen/unified/uber-eats.json.template`). Religar do zero com dado
> já existente colide PK (`ORA-00001`/`duplicate key`) e **já travou o pipeline inteiro** (17
> streams, 99% CPU, zero linhas novas) — ver
> `.claude/kb/shadowtraffic/patterns/restart-seguro-startingFrom.md` e a skill
> `shadowtraffic-ajustar-geracao`.

| Script | O que faz |
|--------|-----------|
| `shadowtraffic/toggle-shadowtraffic.ps1 on\|off\|status` | **Caminho seguro** para ligar/desligar o gerador (`gen-unified`). No `on`: espera os bancos ficarem healthy, lê o `MAX(id)`/`COUNT(*)` real de `users`/`drivers`/`orders`/`payments`/`restaurants`, injeta segredos (`gen\setup-configs.ps1`), recalcula `startingFrom` no `uber-eats.json` **gerado** (nunca no template) e só então sobe o container. Também liga/desliga o loop de report (`shadowtraffic-report-loop.ps1`, mesma pasta). `status` mostra se está ativo e a contagem por tabela. |
| `shadowtraffic/start-generators.ps1` | Sobe `gen-unified` **do zero**, sem recalcular `startingFrom`. Só seguro logo após `docker-compose down -v` + infra nova (tabelas vazias). Requer infra já rodando. |
| `shadowtraffic/stop-generators.ps1` | Para só `gen-unified` (`docker-compose stop`), sem tocar no loop de report nem recalcular nada. Prefira `toggle-shadowtraffic.ps1 off`, que também encerra o loop de report. |
| `shadowtraffic/shadowtraffic-report-loop.ps1` | **Uso interno** — não rodar diretamente. Escreve um snapshot por tabela em `logs/shadowtraffic-report.log` a cada hora enquanto `gen-unified` estiver ativo; iniciado/encerrado automaticamente pelo `toggle-shadowtraffic.ps1`. |
| `lib/shadowtraffic-common.ps1` | **Biblioteca interna** (dot-source), não é um script executável — funções compartilhadas de leitura de `.env`, contagem Postgres/Oracle e espera de healthcheck, usadas por `toggle-shadowtraffic.ps1`, `toggle-ingestion.ps1` e o report loop. |

```powershell
.\scripts\infra\start-infra.ps1
.\scripts\shadowtraffic\toggle-shadowtraffic.ps1 on
.\scripts\shadowtraffic\toggle-shadowtraffic.ps1 status
# ...
.\scripts\shadowtraffic\toggle-shadowtraffic.ps1 off
```

Licença expirada? Veja a skill `shadowtraffic-renovar-licenca` (atualiza `shared/gen/.env` e religa sem
colidir PK — não use `reset-all.ps1` só por causa da licença).

---

## 4. Tudo de uma vez

| Script | O que faz |
|--------|-----------|
| `all/start-all.ps1` | Liga literalmente tudo, delegando para os scripts das seções 1–3 em vez de duplicar comandos: `start-infra.ps1` → `toggle-ingestion.ps1 on` → `toggle-shadowtraffic.ps1 on`. Uso típico: primeira execução do projeto ou demo. No dia a dia, prefira ligar só a categoria necessária. |
| `all/stop-all.ps1` | `docker-compose down` — para todos os containers do compose, preservando volumes/dados. Airbyte (fora do compose) não é afetado; pare-o com `stop-airbyte.ps1` se estiver rodando. |

```powershell
.\scripts\all\start-all.ps1
# ... demo/apresentação ...
.\scripts\all\stop-all.ps1
```

---

## 5. Destrutivo

| Script | O que faz |
|--------|-----------|
| `infra/reset-all.ps1` | **Apaga tudo.** Força a parada de containers zumbis, roda `docker-compose down -v` (destrói os volumes `postgres_data`/`minio_data`/etc.) e remove o `shared/gen/unified/uber-eats.json` gerado (continha segredos). **Não tem volta.** Use só para recomeçar do zero ou quando algo travou de vez (ex.: colisão de PK que nem o `toggle-shadowtraffic.ps1` resolve). |

```powershell
.\scripts\infra\reset-all.ps1
.\scripts\all\start-all.ps1   # ambiente 100% novo — start-generators.ps1 também seria seguro aqui
```

---

## 6. Validação (repositório agentic/SDD)

Não mexem em infraestrutura de dados — validam a estrutura do repositório agentic (`.cursor/`,
`.claude/`, `.github/`) e o Dev Loop.

| Script | O que faz |
|--------|-----------|
| `tooling/validate-agent-router.py` | Valida `.cursor/sdd/architecture/AGENT_ROUTER.yaml`: sintaxe YAML, ids únicos de agentes e se cada `agents[].file` referenciado existe de fato. |
| `tooling/validate-agentic-template.py` | Valida um template ou projeto agentic (Cursor + GitHub Copilot + Claude). Modo `template` permite variáveis `{{PROJECT_*}}`; modo `project` falha se ainda houver `{{...}}` não substituído nos arquivos principais. |
| `tooling/validate-workflow-bundle.py` | Garante paridade entre `.cursor/` (canônico) e `install_dev_loop/workflow_bundle/cursor/` para os paths do Workflow Dev Loop — usado depois de `sync-workflow-bundle.sh`. |

```bash
python3 scripts/tooling/validate-agent-router.py
python3 scripts/tooling/validate-agentic-template.py --mode project
python3 scripts/tooling/validate-workflow-bundle.py
```

---

## 7. Outros utilitários

Scripts de suporte ao repositório agentic e à integração com Databricks — não fazem parte do
ciclo diário de ligar/desligar dados.

| Script | O que faz |
|--------|-----------|
| `tooling/bootstrap-agentic-project.py` | Aplica o template agentic/SDD deste repositório em um **projeto destino**: renderiza variáveis `{{...}}`, cria o agente expert do projeto e valida o resultado com `validate-agentic-template.py`. |
| `tooling/sync-workflow-bundle.sh` | Sincroniza `.cursor/` (fonte canônica) → `install_dev_loop/workflow_bundle/cursor/` e `assets/`. Aceita `--dry-run` e `--no-validate`. |
| `tooling/enable-git-hooks.sh` | Registra os hooks versionados em `.githooks/` neste clone (`git config core.hooksPath .githooks`) — roda uma vez por máquina. Complementa a política de branch do GitHub, não substitui. |
| `tooling/databricks-mcp-auth.ps1` | Obtém um token OAuth (client credentials) do workspace Databricks configurado, a partir de `DATABRICKS_SP_CLIENT_ID`/`DATABRICKS_SP_CLIENT_SECRET` no ambiente, e imprime o header `Authorization: Bearer ...` em JSON — usado para autenticar chamadas ao MCP `databricks-sql`. |

---

## Matriz de decisão rápida

| Situação | Script recomendado |
|----------|--------------------|
| Primeira vez executando o projeto | `start-all.ps1` |
| Desenvolvimento local, sem gerar dado novo | `start-infra.ps1` |
| Preciso que o gerador volte a rodar (já tem dado) | `toggle-shadowtraffic.ps1 on` |
| Ambiente 100% novo, tabelas vazias | `start-generators.ps1` |
| Economizar licença do ShadowTraffic | `toggle-shadowtraffic.ps1 off` |
| Vou configurar/rodar sync no Airbyte | `toggle-ingestion.ps1 on` (ou só `start-airbyte.ps1`) |
| Terminei de usar o Airbyte | `stop-airbyte.ps1` |
| Terminar o dia | `stop-all.ps1` |
| Licença expirada | skill `shadowtraffic-renovar-licenca` |
| Pipeline travado por colisão de PK / algo irrecuperável | `reset-all.ps1` → `start-all.ps1` |
| Mudei algo em `.cursor/` e preciso validar o router/template | seção 6 |

---

## Requisitos

- Windows 10/11, Docker Desktop rodando (`start-infra.ps1` tenta iniciá-lo sozinho).
- PowerShell 5.1+ (ou `pwsh` 7+).
- `shared/gen/.env` preenchido a partir de `shared/gen/.env.template` (credenciais Postgres/Oracle/Mongo e
  licença ShadowTraffic).
- Scripts Python (seção 6/7) precisam de `pyyaml` (`pip install pyyaml`).

## Dicas

```powershell
docker-compose ps                              # status de todos os containers
docker-compose logs -f gen-unified             # log do gerador
docker-compose logs -f postgres-ubereats       # log de um serviço específico
.\scripts\shadowtraffic\toggle-shadowtraffic.ps1 status  # contagem por tabela + estado do gerador
.\scripts\infra\toggle-ingestion.ps1 status              # estado de Redpanda/Kafka Connect/Airbyte + connector
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|-----------------|------|
| `ORA-12514`/`ORA-01109` logo após religar | Healthcheck do Oracle passou "healthy" antes do listener/PDB estarem realmente prontos para conexão — condição transitória, já tratada com retry em `lib/shadowtraffic-common.ps1`. | Normal ver 1–3 avisos de retry; se persistir, `docker logs oracle-ubereats`. |
| `ORA-00001`/`duplicate key` e pipeline travado (17 streams, CPU alta, zero linhas novas) | `start-generators.ps1` foi usado com dado já existente, religando com `startingFrom` desatualizado. | `toggle-shadowtraffic.ps1 off` → `on` (recalcula os IDs). Se não resolver: `reset-all.ps1`. |
| "License expired" nos logs do `gen-unified` | Licença trial do ShadowTraffic venceu (`shared/gen/.env`). | Skill `shadowtraffic-renovar-licenca`. |
| "Port already in use" | Containers de uma execução anterior ainda de pé. | `docker ps` para conferir, depois `stop-all.ps1` → `start-all.ps1`. |
| Containers "zumbis" que não param | Estado inconsistente do compose. | `reset-all.ps1` (destrutivo). |

---

**Dúvidas?** Consulte o `README.md` principal na raiz do projeto e `CONTEXT.md`.
