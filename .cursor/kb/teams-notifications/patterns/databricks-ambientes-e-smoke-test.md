# Padrão: Teams em pipelines Databricks — ambientes (DSV/PRD) e smoke test

> **Confiança:** 0.95  
> **Macro:** aplicável a **qualquer** projeto Databricks com Asset Bundle (DAB).  
> **Referência:** implementação Varonis (`@guard_dlt_step`, `teams_notify`, `notebooks/smoke_test_teams_notification.py`).  
> **Relacionado:** [falha-de-pipeline.md](falha-de-pipeline.md), [databricks/patterns/pipeline-failure-teams-no-retry.md](../../databricks/patterns/pipeline-failure-teams-no-retry.md)

## Objetivos

1. Alertar **Microsoft Teams** quando o pipeline **para** por erro (sem retry silencioso).
2. Mensagem **acionável** para o analista: camada, processo, tabela, erro, trecho de código.
3. **DSV ≠ PRD**: webhook e catálogo corretos por target do bundle.
4. **Smoke test** reproduzível por ambiente antes de forçar falha real.

---

## Política: sem retry no Job

| Regra | Configuração |
|-------|----------------|
| Falhou → **parar** | `max_retries: 0` no **job** e em **cada task** |
| Sem loop de reexecução | `retry_on_timeout: false` (recomendado) |
| Reprocessar só **manual** | Nova run após correção |

```yaml
# databricks.yml — variável reutilizável
variables:
  job_task_max_retries:
    description: 0 = falha uma vez, sem reexecutar task
    default: 0

resources:
  jobs:
    meu_job:
      tasks:
        - task_key: run_dlt
          max_retries: ${var.job_task_max_retries}
          pipeline_task:
            pipeline_id: ${resources.pipelines.meu_dlt.id}
```

**Onde validar no UI:** Workflows → Job → Task → **Max retries = 0**.

DLT pode ter retries internos de Spark; o que importa para operação é **não** re-disparar o job inteiro em loop.

---

## Alternar ambiente (DSV / PRD)

### 1. Deploy por target

```bash
./scripts/bundle_deploy.sh -t dev    # DSV
./scripts/bundle_deploy.sh -t prd    # PRD
```

### 2. Bundle — variáveis por target

```yaml
variables:
  teams_webhook_env_var:
    default: URL_WEBHOOK_MEU_PROJETO_DSV

targets:
  dev:
    variables:
      teams_webhook_env_var: URL_WEBHOOK_MEU_PROJETO_DSV
      teams_webhook_secret_key: url_webhook_meu_projeto_dsv
  prd:
    variables:
      teams_webhook_env_var: URL_WEBHOOK_MEU_PROJETO_PRD
      teams_webhook_secret_key: url_webhook_meu_projeto_prd

resources:
  pipelines:
    meu_dlt:
      configuration:
        varonis.teams_webhook_env_var: ${var.teams_webhook_env_var}
        varonis.teams_env_file_path: ${workspace.file_path}/files/.env
```

Convénção Icatu: sufixo `_DSV` / `_PRD` na variável `.env` (ver [references/chaves-webhook-env.md](../references/chaves-webhook-env.md)).

### 3. Onde fica a URL

| Ambiente | Opção recomendada | Path típico no workspace |
|----------|-------------------|-------------------------|
| DSV | `.env` importado + smoke | `.../dataflow-dsv/dev/files/.env` |
| PRD | **Secret** Databricks + opcional `.env` | `.../dataflow-prd/prd/files/.env` |

**DLT serverless:** workers podem **não** ler `/Workspace/.../files/.env` — resolver webhook no **driver** ao iniciar o pipeline (cache) ou usar **secret scope**.

### 4. O que **não** governa o DLT em produção

- `.config` local e `VARONIS_ENV` — só notebooks/testes locais.
- `spark.conf.set("varonis.*")` em notebook — **não** propaga para pipeline DLT; só `pipeline.configuration` no bundle.

---

## Mensagem de erro Teams — campos obrigatórios

O card vermelho deve permitir ao analista ir direto ao ponto:

| Campo | Exemplo | Notas |
|-------|---------|--------|
| **Camada (medallion)** | `bronze`, `silver`, `gold` | Passo DLT |
| **Processo** | `ingestao_cloudfiles_raw` | Nome lógico da etapa |
| **Tabela** | `varonis.bronze.tb_x` | FQCN Unity Catalog |
| **Ambiente / catálogo** | `prd` · `varonisprd` | Target do bundle |
| **Função / ficheiro** | `bronze_arquivos_sensiveis` em `dlt_medallion_pipeline.py` | Onde corrigir |
| **Origem no código** | `bronze_ingest.py:42` · `read_raw()` | Frame do pacote no traceback |
| **Erro** | `FileNotFoundError: Pasta RAW inexistente...` | Tipo + mensagem |
| **Traceback** | últimos ~3200 caracteres | Trecho, não dump infinito |
| **Run tags** (opcional) | `jobRunId`, `updateId` | Tags Databricks |

Após enviar Teams → **`raise`** a mesma exceção (fail-fast).

---

## Smoke test por ambiente

### Objetivo

Validar **webhook + pymsteams** sem falhar o pipeline de produção.

### Checklist

```text
[ ] Deploy -t dev ou -t prd no workspace correto
[ ] Importar .env para .../dev/files/.env OU .../prd/files/.env (chave _DSV ou _PRD)
[ ] Executar notebook smoke_test_teams_notification (serverless)
[ ] Print: perfil=dsv|prd, teams env var=URL_WEBHOOK_*_DSV|_PRD
[ ] Diagnóstico: environment e catalog alinhados ao perfil
[ ] Card verde no canal correto (send_failure_sample=false por default)
[ ] Opcional: card vermelho de amostra (mesmo layout do DLT)
```

### Widgets recomendados

| Widget | Uso |
|--------|-----|
| `varonis_profile` (ou `deployment_profile`) | `dsv` \| `prd` \| vazio (auto pelo path do bundle / `URL_WEBHOOK_*_PRD` no override) |
| `teams_env_file` | vazio = `.../files/.env` ao lado do `src` |
| `send_failure_sample` | `false` = só ping verde |

### API Python (smoke)

Passar o perfil explicitamente evita `environment: dsv` no diagnóstico quando o notebook não tem `spark.conf` do bundle:

```python
diag = diagnose_teams_config(spark, deployment_profile="prd")
run_teams_smoke(spark, deployment_profile="prd", include_failure_sample=False)
```

Critérios de sucesso no JSON do diagnóstico:

| Campo | DSV | PRD |
|-------|-----|-----|
| `webhook_source` | `...#URL_WEBHOOK_*_DSV` | `...#URL_WEBHOOK_*_PRD` |
| `environment` | `dsv` | `prd` |
| `catalog` | ex. `varonis` | ex. `varonisprd` |

### Armadilhas (PRD a usar DSV)

| Sintoma | Causa | Correção |
|---------|--------|----------|
| Webhook DSV em workspace PRD | `src` em `.../dev/files/src` | Deploy `-t prd`, import `.env` em `.../prd/files/` |
| `environment: dsv` no diagnóstico | Fallback `.config` default | Passar `deployment_profile=prd` ou widget `varonis_profile=prd` |
| `spark_conf varonis.*` vazio no smoke | Normal em notebook | Esperado; DLT tem conf após deploy |

### Comando import `.env` (exemplo PRD)

```bash
databricks workspace import .env \
  "/Workspace/Users/SEU_USER/.bundle/meu-projeto-prd/prd/files/.env" \
  --file-type AUTO --overwrite --profile <profile_prd>
```

---

## Implementação mínima (novo projeto)

1. Copiar padrão [pipeline-failure-teams-no-retry.md](../../databricks/patterns/pipeline-failure-teams-no-retry.md) no `databricks.yml` (`max_retries: 0`).
2. Módulo `teams_notify` com `PipelineFailureContext` + `notify_pipeline_failure`.
3. Decorator ou `try/except` por etapa medallion → Teams → `raise`.
4. Notebook smoke + `.env.example` com chaves `_DSV` / `_PRD`.
5. Agente `@teams-notifications-expert` + esta KB.

---

## Checklist de entrega

```text
[ ] job_task_max_retries = 0 em todas as tasks
[ ] targets dev/prd com teams_webhook_env_var distintos
[ ] Card de falha com camada, processo, tabela, código, erro
[ ] Smoke test documentado e testado em DSV e PRD
[ ] Sem URL de webhook no Git
```
