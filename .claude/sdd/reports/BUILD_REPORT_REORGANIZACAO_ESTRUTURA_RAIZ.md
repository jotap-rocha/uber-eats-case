# BUILD REPORT: Reorganização da Estrutura de Pastas da Raiz

| Campo | Valor |
|-------|-------|
| **Feature** | REORGANIZACAO_ESTRUTURA_RAIZ |
| **Escopo deste Build** | Manifesto completo do DESIGN — Etapas 1-6 (42 itens + 12 ADRs) |
| **Input** | `.claude/sdd/features/DESIGN_REORGANIZACAO_ESTRUTURA_RAIZ.md` |
| **Branch** | `refactor/reorganizacao-estrutura-raiz` (dedicada, não mergeada em `main`) |
| **Data** | 2026-09-27 |

---

## Summary

| Métrica | Valor |
|---------|-------|
| Etapas concluídas | 6/6 |
| Commits nesta branch | 7 (docs SDD, Etapa 1, fix de path perdido, Etapas 2-5, este relatório) |
| Arquivos movidos (`git mv`, rename detection preservado) | ~120 |
| Arquivos de conteúdo editados (paths corrigidos) | ~100 |
| `requirements.txt` (raiz) | Removido (ADR-02, vazio, sem consumidor) |
| Bugs reais encontrados e corrigidos além do manifesto original | 6 recursos Terraform com `path.module` quebrado (AWS/Azure/GCP); 9 scripts PowerShell com `$PSScriptRoot`/`repoRoot` quebrado; 1 commit da Etapa 2 que perdeu 5 edições por `git add` com pathspec inválido (corrigido em commit separado) |
| `docker compose config --quiet` | ✅ exit 0 |
| `python scripts/tooling/validate-agent-router.py` | ✅ OK (77 agentes, 32 hints) |
| `pytest azure/tests` | ✅ 6/6 |
| `pytest gcp/tests` | ✅ 4/4 (+3 erros de dependência ausente `google-cloud-pubsub`, pré-existente) |
| `pytest aws/tests` | ⚠️ Não coletável — `boto3` ausente no ambiente, pré-existente (mesma limitação do `BUILD_REPORT_INGESTAO_AWS`) |
| `databricks bundle validate` | ⚠️ Condicional (ADR-07) — bundle parseia e resolve corretamente; falha só na autenticação (403, token/perfil), pré-existente |
| `terraform validate` | ❌ Não executado — CLI não disponível neste ambiente (mesma limitação dos builds Azure/GCP); path corrigido por inspeção manual de profundidade |
| `git log --follow` | ✅ Histórico preservado (testado em `shared/pipeline/bronze/ingest_oracle_orders.sql`) |
| `git check-ignore -v` (5 paths de segredo real) | ✅ Todos protegidos |
| Raiz do repositório | ✅ Só os 6 agrupadores + ferramental agentic + allowlist de config de ferramenta (confirmado por `ls`) |

---

## O que foi implementado, por etapa

### Etapa 1 — `scripts/` em subpastas (commits `9e604f1`, `6b42c8d`)

| Item do manifesto | Status |
|---|---|
| `scripts/{infra,shadowtraffic,all,tooling,ingestion,lib}/` criadas, 19 scripts + 3 `debezium/register-*.ps1` movidos | ✅ |
| `Get-RepoRoot` adicionado a `scripts/lib/shadowtraffic-common.ps1` (ADR-12) | ✅ |
| 59 consumidores dos 7 scripts de tooling agentic (git hooks, `CLAUDE.md`, `CURSOR.MD` ×3, `intake.md` ×3, `PROMPT_*.md`, KB) | ✅ 27 arquivos reais editados (o resto eram menções em registros históricos, fora de escopo) |
| Correção de profundidade `$PSScriptRoot`/`repoRoot` em 9 scripts que mudaram de nível | ✅ |

**Achado durante o build:** o `git add -A` com pathspec incluindo `requirements.txt` (já staged por `git rm`) retornou `fatal: pathspec did not match`, o que abortou o `add` das 5 correções de path em `aws/gcp/azure tests` feitas na Etapa 2 — a rename ficou (staged pelo próprio `git mv`), a edição de conteúdo não. Corrigido em commit `6b42c8d` separado, revalidado com `pytest`.

### Etapa 2 — `aws/`, `azure/`, `gcp/` (commits `b10cd22`, `6b42c8d`)

| Item do manifesto | Status |
|---|---|
| `src/{cloud}`, `infra/{cloud}`, `sql/{cloud}`, `tests/{cloud}`, `docs/{cloud}` (quando existia), `requirements-{cloud}.txt` movidos | ✅ |
| `docs/data-contract-cdc-*.md`, `docs/minio/*-{azure,gcp}.md` movidos para `{cloud}/docs/` | ✅ |
| `requirements.txt` (raiz) removido (ADR-02) | ✅ |
| Testes de `aws/gcp` reescritos (`parents[2] / "src" / cloud` → `parents[2] / cloud / "src"`) | ✅ — **desvio do DESIGN**: a sugestão original (`parents[1]`) estava errada; a profundidade real não muda entre `tests/{cloud}/` e `{cloud}/tests/` (mesmo número de segmentos), só a ordem `src/{cloud}` → `{cloud}/src` — confirmado por inspeção antes de aplicar |

### Etapa 3 — `shared/` (commit `8bcae8f`)

| Item do manifesto | Status |
|---|---|
| `pipeline/`, `gen/` (incl. `.env` real, não rastreado), `mongo/init/`, `sql/oracle/` (intacto), `sql/create_{users,drivers}_table.sql` movidos | ✅ |
| `sql/cdc configure/database-cdc-config.sql` → `shared/sql/legacy/` + `README.md` novo (ADR-03) | ✅ |
| Docs genéricos + `PENDENCIAS-DOCKER-RESOURCES.md` → `shared/docs/` (ADR-10) | ✅ |
| `.gitignore` atualizado no mesmo commit (ADR-08): 4 regras reancoradas + 1 nova (`shared/gen/gcp-credentials.json`) | ✅ |
| 9 scripts que resolviam `gen/.env`\|`gen/unified`\|`gen/setup-configs.ps1` corrigidos | ✅ |
| `docker-compose.yml` | Intencionalmente **não** editado — corrigido de uma vez na Etapa 5, conforme sequenciamento do DEFINE |

### Etapa 4 — `config/{aws,azure,gcp,shared}/` (commit `1b87bb6`)

| Item do manifesto | Status |
|---|---|
| Templates Debezium + `hadoop-conf` movidos de `debezium/` (raiz, agora extinta) para `config/{cloud}/` | ✅ |
| `application.properties` do Debezium Server GCP movido de `gcp/src/debezium_server_*/` para `config/gcp/debezium-server/` (ADR-06) | ✅ |
| `deploy/autossh/*.service` → `config/gcp/deploy/autossh/` (`deploy/` extinta) | ✅ |
| 3 scripts `register-*.ps1` + 2 pontos em `azure/tests` + 1 comentário em `azure/src` corrigidos | ✅ |
| `.gitignore`: nova regra `config/azure/hadoop-conf/core-site.xml` (ADR-08) | ✅ |

### Etapa 5 — Referências (commit `0d8972d`)

| Item do manifesto | Status |
|---|---|
| `docker-compose.yml`: todos os mounts/`env_file` pendentes das Etapas 3-4 | ✅ |
| **Achado não previsto no DESIGN**: 6 recursos Terraform (`aws`/`azure`/`gcp`) com `${path.module}/../../../src|sql/{cloud}/...` — quebrariam em `terraform plan` real | ✅ Corrigido (`path.module` continua 3 níveis até a raiz; só o alvo mudou de `src/{cloud}` para `{cloud}/src`) |
| `CONTEXT.md`, `README.md`, `CLAUDE.md` + `.claude/CLAUDE.md`, `.cursorrules`, `CURSOR.MD` ×3, `router.md` (sem path literal, confirmado) | ✅ |
| KB `shadowtraffic` (9 arquivos, só em `.claude/` — não é espelhada), 3 `SKILL.md` shadowtraffic | ✅ |
| KB `data-engineering-practices`/`project_architecture`/`sql-capacity` (espelhados ×3), `AGENT_ROUTER.yaml` `intake_hints` (espelhado ×3) | ✅ |
| Referências cruzadas dentro de `aws/azure/gcp` (`.tf`, `.py`, `.md`) para o layout antigo | ✅ |

### Etapa 6 — Anomalias + validação final (este relatório)

| Item | Resultado |
|---|---|
| `gen/unified/uber-eats.json;C` | Confirmado inexistente (`git ls-files` vazio) — já estava resolvido antes do `/build` |
| `__pycache__/` versionado | Confirmado não versionado — já estava resolvido antes do `/build` |
| Validação final | Ver tabela de Summary acima |

---

## Acceptance Tests (DEFINE v1.1)

| ID | Resultado |
|----|-----------|
| AT-001 | ⚠️ Não executado nesta sessão — rodar `.\scripts\infra\start-infra.ps1` / `.\scripts\shadowtraffic\toggle-shadowtraffic.ps1 status` sobe Docker Desktop e containers reais; fora do escopo de `/build` (side effect real, não é "verificação"). Sintaxe PowerShell dos 2 scripts validada via `PSParser` |
| AT-002 | ✅ `docker compose config --quiet` exit 0, sem path antigo |
| AT-003 | ✅ Reescopado (ADR-07): `databricks.yml` não referenciava `pipeline/`, nenhuma edição necessária nele; comentário em `docker-compose.yml` e árvore em `pipeline/README.md` corrigidos; `databricks bundle validate` resolve o bundle e falha só na autenticação (pré-existente) |
| AT-004 | ✅ `pytest azure/tests gcp/tests` — mesma taxa de sucesso (100% do que é coletável); `aws/tests` não coletável por dependência ausente, idêntico ao build original |
| AT-005 | ✅ `python scripts/tooling/validate-agent-router.py` — OK |
| AT-006 | ✅ Varredura grep final sem ocorrência real fora do escopo documentado na Etapa 5 |
| AT-007 | ✅ `git log --follow` preserva histórico |
| AT-008 | ✅ `find config -name "*.py" -o -name "*.sh" -o -name "*.ps1" -o -name "requirements*.txt"` vazio |
| Novo (ADR-08) | ✅ `git check-ignore -v` confirma os 5 paths de segredo protegidos |

---

## Desvios do DESIGN

1. **Profundidade dos testes (Etapa 2)**: o DESIGN sugeria `parents[2] → parents[1]`; a inspeção real mostrou que a profundidade não muda (mesmo número de segmentos entre `tests/{cloud}/` e `{cloud}/tests/`), só a ordem do alvo. Aplicado `parents[2]` com `{cloud}/src` em vez de `src/{cloud}`.
2. **6 recursos Terraform não estavam no manifesto original** (`aws/infra/fase2-ingestao/lambda_{bridge,consumer}.tf`, `azure/infra/fase1-ingestao/stream_analytics.tf`, `gcp/infra/fase3-ingestao/{bigquery,cloud_function_bridge,dataproc}.tf`) — encontrados só durante a Etapa 5 ao procurar por `path.module.*\.\./\.\./\.\./`. Corrigidos com a mesma lógica de profundidade inalterada.
3. **Commit da Etapa 2 perdeu 5 edições de conteúdo** por causa de um `git add -A` com pathspec que incluía um arquivo já resolvido (`requirements.txt`) — o `add` abortou antes de re-estagear as edições feitas depois do `git mv`. Corrigido em commit separado imediatamente após, revalidado.
4. **Bug de duplo prefixo `shared/shared/`** introduzido por `sed` com duas substituições sobrepostas (`.json.template` e `.json` na mesma expressão) em ~10 arquivos de KB/docs — encontrado e corrigido antes do commit da Etapa 5 (nunca chegou a ser commitado).

## Fora de escopo (decisão consciente)

`agentspec/`, `install_dev_loop/`, `get_started/`, `templates/*-generico.md` (ferramental agentic genérico — serve outros projetos, não deve referenciar a estrutura específica deste repo); `scripts/tooling/validate-agentic-template.py` (lista de nomes de arquivo convencionais usada contra qualquer projeto); `BRAINSTORM_REORGANIZACAO_ESTRUTURA_RAIZ.md` e `DESIGN`/`BUILD_REPORT` de outras features (registro histórico imutável, ADR-09); `.claude/dev/tasks/PROMPT_dl-*`, `logs/`, `progress/` (Dev Loop runs concluídos); `proximos-passos.md` (gitignored, notas pessoais).

## Próximo passo

Branch `refactor/reorganizacao-estrutura-raiz` pronta para revisão manual. **Não foi feito push nem aberto PR** (fora da autorização desta sessão). Sugestão:

```bash
git push -u origin refactor/reorganizacao-estrutura-raiz
gh pr create --title "refactor: reorganiza estrutura da raiz por trilha de nuvem" ...
```

Após merge, recomenda-se rodar `/pipeline-review-init` (já sinalizado como SHOULD no DEFINE) para confirmar que a relocação não alterou comportamento, e `/ship .claude/sdd/features/DEFINE_REORGANIZACAO_ESTRUTURA_RAIZ.md` para arquivar a feature.
