# azure-warehouse — Grill & Requisitos

Grill (`/grill-with-docs`) em 2026-11-11 e 2026-11-12; estruturado pelo `harness-define` em 2026-11-12.
Escopo revisto pelo usuário em 2026-11-12: a modelagem do `dw` sai do planejamento agora (o usuário precisa ver o
dado primeiro) e volta como **etapa B** via `harness-iterate`. Ver [00-ideia.md](00-ideia.md).

## Contexto

### Problema

O Financeiro precisa de um número **oficial** (exato em centavos, reproduzível, fechado por período) para saber
quanto a plataforma ganhou de fato em cada dia, cidade e restaurante depois dos estornos, e quanto deve a cada
restaurante e motorista ([objetivos de negócio, seção 1](../../../shared/docs/OBJETIVOS_DE_NEGOCIO_POR_ARQUITETURA.md)).
Hoje esse dado só existe nos bancos operacionais locais (Postgres e Oracle), sem histórico de dimensões nem
fechamento por período. Este projeto leva o dado até um warehouse na Azure, com carga automática e controlada.

### Usuários

- **Financeiro (cliente de negócio, representado pelo `cliente-financeiro`):** quer margem, estornos, extratos de
  restaurante e motorista e a prova de que a conta fecha (RN-33).
- **Usuário do projeto (engenheiro, dono do portfólio):** opera sozinho, acompanha direto, precisa de custo
  previsível dentro do crédito de 30 dias e de nada ligado sem ele saber.

### Objetivos (MoSCoW)

Ordem (D23): tudo o que não depende de conta, **incluindo a etapa B**, fica pronto antes do cadastro; a conta só
abre com o código das três arquiteturas da Azure validado; os 30 dias são para `apply`, carga e conferência.

**MUST (antes da conta):**
- Prova local do Airbyte (D21): sync completo do histórico para destino local, sem cair por memória; formatos dos
  registros guardados para o contrato da `stg`.
- Terraform `azure/infra/base/` (resource group, ADLS com `landing`, budget 50/80/100%) e `azure/infra/warehouse/`
  (Synapse workspace + DW100c, ADF com pipeline, permissões mínimas), state remoto com lock, parametrizado por `env`,
  com `terraform validate` verde.
- Scripts SQL versionados em `azure/sql/` (schemas `stg`, `dw`, `ctl`; `COPY INTO` → `stg`; controle de lote e
  arquivo no `ctl`; qualidade com `ISJSON` e tabela de rejeitadas).
- Pipeline do ADF: liga o pool (REST + `Until`), carrega, **pausa sempre**; disparo manual; gatilho diário
  declarado e desligado (D20).
- Esteira `github-cd` pronta e testada com stub (D24).
- **Etapa B:** modelagem e scripts do `dw` (dimensões SCD2, fatos via `MERGE`/CTAS), desenhados olhando o dado local.
- Os três agentes-cliente criados (`cliente-financeiro`, `cliente-retencao`, `cliente-operacao`).
- ADR nova e invariantes do `CLAUDE.md` atualizados.

**MUST (com a conta):** teste do Synapse no primeiro dia (D19); `apply` de `base` e `warehouse` pela esteira;
Airbyte local → ADLS `landing` (Postgres por CDC, Oracle por `UPDATED_AT`), JSONL; 1 a 3 cargas disparadas pelo
usuário; veredito "resolve" do `cliente-financeiro`.

**SHOULD:** task de medição de volume após a geração do histórico (define as horas de DW100c da carga inicial).

**COULD:** atualizar o diagrama do Canva e o roadmap com as decisões.

### Out of Scope

- Lakehouse e Kappa da Azure (projetos `azure-lakehouse`, `azure-kappa`); AWS e GCP.
- MongoDB no Warehouse (D10); Debezium, Redpanda e sink no Warehouse (D7/D9).
- Consumo e visualização (Power BI, Genie, dashboards): a entrega termina no dado consultável por SQL.
- Alertas de falha do pipeline e de pool ligado (só o budget alert fica).
- Ambiente prd provisionado e a própria esteira de CD (projeto `github-cd`).
- Liquidação com datas e fluxo de caixa; visão fiscal (fora do escopo do cliente).
- Operação agendada: o gatilho diário existe desligado; a carga roda 1 a 3 vezes, manual (D20).

### Restrições

- **Custo:** free account (uma por pessoa: crédito e 30 dias servem às três arquiteturas da Azure), *spending
  limit* rígido, reserva de 25% intocada e teto de planejamento do Warehouse de US$ 20 (D23). DW100c a US$ 1,20/h
  em `eastus2` (a reconfirmar), cobrado por hora ativa. Todo `apply` pago só com `plan` + estimativa por hora e por
  dia + "ok" do usuário. Recurso contínuo nasce com budget. Pausa e destroy nunca automáticos, **exceto o ADF pausar
  o pool no fim da execução disparada pelo usuário** (D14, D20). O pool nunca é apagado durante o projeto (D19).
- **Máquina local:** Docker com ~9,7 GB; Oracle usa 2,3 GB; Airbyte (`abctl`) já caiu por memória. Airbyte só em
  janela, com o simulador desligado.
- **Fontes:** histórico de 1 ano em geração; o agente não roda o simulador nem toca nas tabelas de operação do
  Postgres durante a geração. Bancos locais tratados como produção.
- **Segurança:** repo público, logs de CI públicos; segredos fora do git; nunca escrever em PRD.
- **Synapse:** `COPY INTO` lê CSV, Parquet e ORC; JSONL entra como texto (CSV com delimitador inexistente) e é
  aberto com `OPENJSON` (a testar na D19; plano B `JSON_VALUE`).
- **Equipe:** uma pessoa, mais de 3 h por semana.

## Pipeline — 10 perguntas respondidas

1. **Fontes:** Postgres local (28 tabelas, domínio Pedido e catálogo) por CDC do Airbyte (replicação lógica, slot
   próprio) e Oracle local (3 tabelas: `CITIES`, `CUSTOMERS`, `DRIVERS`) por cursor incremental `UPDATED_AT`
   mantido por trigger. Frequência: syncs em janela (D12), destino ADLS `landing` em JSONL. MongoDB fora (D10).
2. **Schema:** conhecido e documentado no [modelo físico](../../../shared/docs/modelagem/04-modelo-fisico.md)
   (F1 Postgres, F2.2 Oracle). Pode mudar: a landing em JSON aceita a mudança e a carga para a `stg` falha de forma
   controlada (regra bloqueante) até o script SQL ser ajustado.
3. **Volume:** não medido agora (histórico de 1 ano em geração; os bancos não são consultados durante a geração).
   Vira task de medição logo após a geração. Backfill: a primeira sync do Airbyte traz o histórico inteiro.
4. **Sensibilidade/PII:** dado 100% sintético (SI nível a). Sem `[AVISO_LGPD]`. Não imprimir registros crus de
   `customers`/`drivers` em logs, docs ou PRs.
5. **SLA:** **D-1 como objetivo de desenho**, não meta operacional (D20): em produção, gatilho diário de madrugada
   e fechamento de D-1 até as 08:00 (Brasília). Neste projeto o gatilho fica desligado e a carga roda 1 a 3 vezes,
   disparada pelo usuário depois do sync; o `ctl` garante que uma carga nova recupera o pendente sem duplicar.
   Custo: ~1 h de DW100c por carga (≈ US$ 1,20).
6. **Consumidores do Gold:** nenhum consumidor nesta solução. A entrega são tabelas do `dw` consultáveis por SQL no
   Synapse; o `cliente-financeiro` julga pelas consultas e pelos números conferidos.
7. **Owner/Notificação:** o usuário, sem alertas de pipeline nem de pool ligado. Mantido o budget de 50/80/100%. A
   proteção contra pool esquecido é a pausa em qualquer desfecho do ADF, o *spending limit* e a checagem de fim de
   sessão do agente.
8. **Ambiente:** cloud, Azure, Synapse Dedicated SQL Pool + ADLS Gen2 + ADF; Airbyte local. dsv provisionado aqui,
   prd depois (D17). Migrar de ambiente = mudar `.tfvars`; a mesma arquitetura em AWS/GCP é outro projeto com stack
   nativa (D11).
9. **Qualidade:** **bloqueante** (a carga falha e o `ctl` não marca o lote): arquivo ilegível ou erro do
   `COPY INTO`; schema mudou (coluna esperada sumiu, envelope `_airbyte_data` diferente); contagem landing ≠ `stg` +
   rejeitadas; rejeitadas acima de 1% das linhas do lote; soma das colunas monetárias na `stg` ≠ soma na origem.
   **Só registra:** linha com problema (JSON quebrado detectado por `ISJSON`, PK nula) vai para a tabela de
   rejeitadas e a contagem fica no `ctl`. RN-33, chave órfã e extratos são testes do `dw` (etapa B).
10. **Portabilidade:** dsv → prd só por variável (`env` no `.tfvars`, nomes com sufixo, ex.
    `rg-ubereats-warehouse-dsv`), nunca por edição de nome no código. Critério: `terraform plan` com `env=prd` roda
    sem mudar código (local, sem apply).

## Medallion Gates — validação (adaptado: Warehouse é Kimball)

- **Checklist T1–T8:**
  - T1 entidades: Postgres 28 + Oracle 3 (lista em [00-ideia.md](00-ideia.md), sem `restaurant_profiles`). ✔
  - T2 colunas: DDL no modelo físico (F1, F2.2). ✔
  - T3 `_source_system`: `postgres-ubereats`, `oracle-ubereats` (coluna `cdc_source_system`). ✔
  - T4 formato-fonte: registros Airbyte em JSONL com envelope `_airbyte_data` (+ `_ab_cdc_*` no Postgres). ✔
  - T5 camada-alvo: `stg` (etapa A) e `dw` (etapa B) no Synapse. ✔
  - T7 JSON aninhado: sim, o envelope do Airbyte; a landing guarda o JSON fiel e a `stg` abre com `OPENJSON`. ✔
  - T8 Genie/NL: não (sem consumidor). ✔
- **Camada-alvo:** Kimball (`stg` → `dw`, com `ctl`). Bronze/Silver/Gold **N/A**: medalhão é do Lakehouse (D6).
- **Contrato dual:** contrato canônico de CDC (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`,
  `cdc_source_system`) nasce na `stg`, com `r` → `c`; ODCS N/A nesta etapa.
- **Gates B1–B4, S1–S8, G1–G7:** N/A (sem medalhão). O equivalente da normalização é a `stg`; o da camada
  analítica, o `dw` da etapa B.
- **Semântica/ontologia:** N/A.

## Vault / secrets cloud

- Usa cofre cloud?: **não** (confirmado pelo usuário em 2026-11-12).
- Provedor: N/A (default sugerido era Azure Key Vault).
- Motivo: nenhum serviço na nuvem precisa ler segredo (D18): OIDC, *managed identity* e autenticação Entra. O único
  segredo (token SAS do Airbyte) fica na máquina local, fora do git.

## Nuvem pública

- Nuvem: **azure** (o `CLAUDE.md` declara `cloud: azure, aws, gcp`; este projeto usa `azure`).
- Free tier/crédito: **sim** (free account, 30 dias). **Pausa/teardown vira requisito:** o pool fica pausado fora
  da carga (ADF); ao fim de cada sessão com recurso caro ligado, o agente lista o que roda e pergunta se pausa ou
  destrói.

## Especificações implícitas detectadas

- **2 Concorrência:** pipeline do ADF com concorrência 1; a execução seguinte espera. O usuário só dispara depois
  de ver o sync terminar (D20), o que elimina a corrida Airbyte × ADF.
- **3 Idempotência:** o `ctl` controla lote e arquivo por tabela; reprocessar apaga o lote da `stg` e recarrega,
  com o mesmo resultado. O Airbyte entrega *at-least-once*: a deduplicação por chave e posição do log é do `dw`.
- **4 Autorização:** só o usuário dispara (portal ou CLI); o gatilho diário existe desligado; o agente nunca.
  Permissões mínimas por identidade (Synapse lê a landing; ADF liga/pausa o pool e executa as procedures).
- **10 Mudança de contrato externo:** schema da origem mudou → carga falha, `ctl` não marca, o usuário ajusta o
  script SQL pela esteira e a execução seguinte recupera o lote.
- **1 Falha de dependência:** Airbyte local fora do ar: não há lote, o usuário não dispara. Esteira fora do ar:
  `apply` local com "ok" (D24). Synapse negado na free account: D19.
- **5 PII:** coberta pela pergunta 4.
- **9 Ciclo de vida:** landing mantida inteira durante o projeto e removida no fim; slot de replicação só enquanto
  há sync previsto (D22).
- **6, 7, 8:** N/A — projeto pessoal sem usuário final, sem rate limit, sem UI.

## Critérios de sucesso mensuráveis

**Etapa A:**
- Prova local do Airbyte termina o sync completo do histórico sem exit 137 (D21).
- `terraform validate` verde em `base` e `warehouse` antes da conta; `plan` com `env=prd` roda sem mudar código.
- Esteira `github-cd` com T1 a T8 verdes (stub) antes da conta (D24).
- Teste do Synapse no primeiro dia: pool criado, `OPENJSON` e autenticação só Entra testados, pool **pausado** (D19).
- Budget com alertas em 50/80/100% criado junto com o primeiro recurso pago.
- Uma execução do ADF disparada pelo usuário: liga o pool, carrega a `stg`, marca o `ctl` e termina com o pool
  **pausado**, inclusive num teste com erro forçado; sem lote novo: termina **sem ligar** o pool.
- Execução repetida sobre o mesmo lote: contagem da `stg` igual à da primeira execução (sem duplicidade).
- Contagem landing = `stg` + rejeitadas por tabela; rejeitadas ≤ 1%; soma monetária da `stg` = soma na origem.
- Pool pausado fora das cargas (verificado no fim de cada sessão).
- Gasto do Warehouse ≤ US$ 20, com a reserva de 25% do crédito intocada (D23).

**Etapa B (critérios do cliente; o desenho do `dw` sai antes da conta, D23):** invariantes da RN-33 passam como teste;
pedido antigo não muda de valor após mudança de produto/restaurante (SCD2); extratos de restaurante e motorista
conferem com a soma dos repasses; o mesmo período consultado duas vezes devolve o mesmo número; veredito "resolve"
do `cliente-financeiro`.

## Decisões do grill

| # | Pergunta | Decisão | Motivo |
|---|---|---|---|
| D1 | Tipo de conta | **Free account** (crédito de 30 dias, *spending limit* rígido) | Sem verba pessoal para PAYG. O teto rígido é a única proteção contra recurso esquecido ligado. Durante os 30 dias o usuário dedica mais que 3 h por semana para fechar as 3 arquiteturas |
| D2 | Região | **`eastus2`**; plano B `eastus` | DW100c a US$ 1,20/h (vs 2,42 em `brazilsouth`); dado sintético, sem residência. Cota e disponibilidade do Synapse Dedicated conferidas na 1ª task pós-cadastro |
| D3 | Teto de gasto | **O crédito da free account** (valor confirmado no cadastro, não assumido) | O *spending limit* é o teto rígido; o limite prático passa a ser o calendário de 30 dias |
| D4 | Alertas | Budget do Terraform em **50%, 80% e 100% do crédito** | Aviso antecipado para pausar antes de o *spending limit* desligar os recursos no meio de uma carga |
| D5 | Ponto de partida das arquiteturas | **Landing comum no ADLS, em JSON bruto**, para Warehouse e Lakehouse; cada arquitetura "desenrola do lado dela", **sem depender das outras**. O Kappa lê só do Event Hubs; da landing usa só a cópia do perfil de restaurante (*reference data*) | Cada arquitetura resolve um problema de negócio próprio com o que faz de melhor (`OBJETIVOS_DE_NEGOCIO_POR_ARQUITETURA.md`). O usuário rejeitou o Warehouse lendo o medalhão: criaria dependência do Databricks (Free Edition no ADLS ainda não provado) e exigiria cópia em Parquet, porque o Synapse Dedicated não lê Delta. Landing em JSON aceita mudança de schema |
| D6 | Camadas do Warehouse | **Kimball**, três schemas no Synapse: `stg` (staging transitória, 1 linha por evento CDC, onde nascem os `cdc_*` com `r` → `c`), `dw` (data mart financeiro: dimensões SCD2 e fatos via `MERGE`), `ctl` (controle das pastas da landing já carregadas). Sem medalhão no Synapse | Medalhão é padrão de lakehouse; DW segue staging → data marts. Inmon descartado: uma camada 3FN a mais repetiria o Postgres para um processo só. O `ctl` existe porque o `COPY INTO` do Synapse não lembra arquivos já lidos (recarga duplica) |
| D7 | Ingestão até a landing (Warehouse) | **Airbyte para as fontes do Warehouse.** Postgres: CDC (replicação lógica, slot próprio do Airbyte). Oracle: **sem CDC**, incremental por cursor `UPDATED_AT` (as 3 tabelas têm a coluna mantida por trigger, F2.2). Destino: ADLS, JSONL. **Sem Debezium, Redpanda nem sink no Warehouse** (a pergunta do "carteiro" deixa de existir) | O motivo do Debezium no Postgres (captura única no barramento, ADR 006 decisão 4) caiu com a ADR 012. No Oracle o Debezium só existia por ser o único CDC aberto; Pessoas são tabelas pequenas e o SCD2 sai no Synapse comparando versões. Custo aceito: mudanças intermediárias entre duas syncs se perdem (só a última versão chega), e a vigência da versão é o `updated_at`, não o commit. **Revisa a ADR 006 (decisão 4) → ADR nova.** O conector Debezium dedicado do Kappa (ADR 012) não muda |
| D8 | Escopo deste projeto | **Só o Warehouse da Azure.** A visão macro segue 3 nuvens × 3 arquiteturas; cada combinação é um projeto `{cloud}-{arquitetura}` (`azure-warehouse`, `azure-lakehouse`, `azure-kappa`, `aws-*`, `gcp-*`). Slug renomeado de `azure-fase1` | Decisão do usuário (2026-11-12) |
| D9 | Debezium no projeto | **Warehouse e Lakehouse, em qualquer nuvem, ingerem só pelo Airbyte.** O Debezium fica restrito ao Kappa (conector dedicado da ADR 012), a confirmar no processo de cada Kappa | Oracle tem tabelas pequenas com marca d'água (`updated_at`); Postgres tem CDC no próprio Airbyte. O Airbyte é lote (sync de minutos), então não atende ao Kappa, que precisa do evento no barramento em segundos. **Revisa a ADR 006 (decisão 4) de forma mais ampla que D7 → entra na mesma ADR nova** |
| D10 | MongoDB no Warehouse | **Fora.** O Warehouse ingere só Postgres (28 tabelas) e Oracle (3) | O perfil de restaurante (cardápio, horários) não responde nenhuma pergunta do fechamento financeiro; tira uma conexão, uma pasta da landing e o JSON aninhado mais trabalhoso da staging |
| D11 | Ingestão do Warehouse e do Lakehouse por nuvem **(revisável)** | Azure: **Airbyte**. AWS: **DMS**. GCP: **Datastream**. Debezium só no Kappa (D9) | Usar o serviço nativo de cada nuvem conta para o portfólio. Revisável: se DMS ou Datastream complicarem demais, o Airbyte volta como opção para simplificar |
| D12 | Onde e quando o Airbyte roda | **Local (`abctl`), ligado só em janelas de sync, com o simulador desligado.** Ciclo da carga: (1) liga o Airbyte; (2) sync para o ADLS; (3) desliga o Airbyte; (4) liga o Synapse e roda `COPY INTO` + procedures; (5) pausa o Synapse | Fontes locais (a Fase 0 não migra); Airbyte Cloud exigiria expor os bancos e cobra por volume. Memória: o Docker tem ~9,7 GB, o Oracle usa 2,3 GB e o `abctl` caiu com exit 137 em 2026-11-12. O Synapse só fica ligado no passo 4. Se faltar memória mesmo assim: parar outros processos locais e aumentar a memória do Docker, a avaliar |
| D13 | Lógica da carga no Synapse | **Scripts SQL versionados e numerados em `azure/sql/`** (schemas, tabelas, procedures de `stg` → `dw`, controle no `ctl`), idempotentes, aplicados com `sqlcmd` | Invariante do `CLAUDE.md` para o que roda dentro do serviço; custo zero e tudo no git. Quem dispara esses scripts é o orquestrador (D14) |
| D14 | Orquestração | **Azure Data Factory**, pipeline declarado no **Terraform**. O Airbyte cuida dos passos 1 a 3 com o agendador dele; o ADF cuida do passo 4: gatilho diário confere se há pasta nova na landing; sem novidade, termina sem ligar o Synapse; com novidade, liga o pool, chama as procedures da D13 e **pausa sempre no fim, inclusive em erro**. **Exceção à regra "pause nunca é automático", só para o orquestrador:** o ADF pode ligar e pausar o pool; o agente continua sem fazer isso sozinho. Travas: gatilho nasce desligado (o usuário liga), pausa em qualquer desfecho, budget alerts e *spending limit* | Visão empresarial: carga não é manual. ADF é a referência de orquestração na Azure, custa centavos (~US$ 1 por 1.000 execuções de atividade) e é versionável no Terraform. Airflow local descartado por memória. Synapse Pipelines: suporte no Terraform a confirmar na arquitetura. **Vai para a ADR nova.** Autorização confirmada pelo usuário em 2026-11-12 |
| D15 | Layout do Terraform | **Separado por nuvem e por arquitetura.** `azure/infra/base/` (resource group, ADLS com `landing`, *service principal* do Airbyte, budget 50/80/100%) e `azure/infra/warehouse/` (Synapse workspace + DW100c, ADF com pipeline, permissões mínimas: Synapse lê a landing; ADF liga/pausa o pool e executa as procedures). State remoto com lock num storage account próprio (passo de *bootstrap*), um state por pasta; `warehouse` lê os outputs da `base`. `azurerm` 4.x nas pastas novas. A pasta antiga `azure/infra/fase1-ingestao/` fica **congelada como referência** e é **removida** quando Warehouse, Lakehouse e Kappa da Azure estiverem fechados; o mesmo vale para a infra antiga de AWS e GCP | A infra antiga é da primeira visão do projeto e mistura as três arquiteturas (e o MinIO). Separar permite destruir uma arquitetura sem derrubar a landing. Validado com `terraform validate` antes da conta (D1); `plan`/`apply` só após o cadastro, com estimativa e "ok" |
| D16 | Agentes-cliente | **Três subagentes de negócio, um por problema**, em `.claude/agents/domain/`: `cliente-financeiro` (Warehouse: fechamento financeiro e conciliação de repasses), `cliente-retencao` (Lakehouse: retenção do cliente e qualidade percebida; Produto/CRM) e `cliente-operacao` (Kappa: torre de controle operacional por cidade). Cada um lê só a sua seção de `OBJETIVOS_DE_NEGOCIO_POR_ARQUITETURA.md`, vale nas três nuvens e é **somente leitura** (Read, Grep, Glob). Entra em três momentos: após o PRD (cada pergunta tem caminho no desenho?), após o `/to-tasks` (alguma pergunta sem task?) e no fim do build (veredito "resolve / resolve parcialmente / não resolve" sobre as evidências). O veredito "resolve" é critério de aceite da última task; complementa `revisor-codigo` e evidence-gate, não substitui. Os três nascem juntos na fase do `/harness-architect` (via `agent-creator`, com teste de redundância e registro no roteador, e `validate-agent-router.py`); neste projeto só o `cliente-financeiro` atua | Cada arquitetura responde um problema e um público diferentes (Financeiro, Produto/CRM, Operação). Criar os três juntos mantém o mesmo molde; só leitura impede que o juiz implemente a própria obra |
| D17 | Ambientes e deploy | **Só o dsv é provisionado aqui**, na nuvem; o código é parametrizado por `env` (Terraform, SQL, ADF) para o prd ser outro `.tfvars` e outro state. **O deploy no dsv sai pela esteira do projeto `github-cd`** (GitHub Environments `dsv`/`prd`, OIDC com a Azure, prd por tag `vX.Y.Z` com aprovação do usuário e, enquanto durar a free account, **aprovação também no `dsv`**: o PR mostra `plan` + estimativa e aprovar é o "ok" do invariante de custo; revisável). A esteira é pré-requisito da task de `terraform apply`. O Airbyte local fica fora da esteira (D12) | dsv e prd são ambientes de nuvem; o local só desenvolve código. Um prd ligado dividiria o crédito único da free account. A tag para o prd e a aprovação no dsv **mudam o invariante de promoção do `CLAUDE.md` → ADR** |
| D18 | Segredos | **Sem Azure Key Vault**: não haver segredo na nuvem. GitHub → Azure por OIDC; ADF → Synapse/ADLS por *managed identity*; Synapse só com autenticação Entra (sem senha de admin SQL). Única credencial: token SAS do Airbyte local, só escrita no container `landing`, validade curta, guardado no Airbyte local e, se o usuário quiser, na pasta local de segredos dele, sempre fora do git | Repo público e free account: identidade no lugar de senha elimina o que vazaria. Key Vault volta à mesa se algum serviço na nuvem precisar ler segredo (Lakehouse/Kappa) |

Consequência de D1: tudo o que não depende de conta (Terraform validado, scripts, esteira com stub, agentes-cliente)
fica pronto **antes** do cadastro; os 30 dias são para `apply` e integração.

## Revisão adversarial (2026-11-12)

Dois revisores externos, rodados manualmente pelo usuário: [Gemini](01b-judge-gemini.md) e [GPT](01b-judge-gpt.md).
Triagem do agente, com conferência em documentação onde o ponto pesava.

### Correções aceitas (sem decisão nova; entram no PRD)

- **D15:** sai o *service principal* do Airbyte (contradizia a D18). Entra o papel RBAC mínimo do ADF para
  ligar/pausar o pool (ações `sqlPools/resume` e `sqlPools/pause`) e o acesso dele como usuário do banco.
- **D18:** o SAS do Airbyte precisa listar, ler, escrever e apagar no container `landing` (exigência do conector,
  [docs](https://docs.airbyte.com/integrations/destinations/azure-blob-storage)); é gerado pelo usuário via `az`,
  **fora do Terraform** (não vai para o state). O Synapse nasce com senha SQL aleatória gerada pelo Terraform (só no
  state, ninguém usa) e logo em seguida com autenticação só Entra; a senha opcional no `azurerm` não está confirmada.
- **Qualidade:** o `ERRORFILE` não valida JSON. JSON quebrado é detectado por `ISJSON()` no SQL e vai para uma
  tabela de rejeitadas; o limite de 1% vale sobre ela. `COPY INTO` carrega cada linha JSONL como texto (CSV com
  delimitador inexistente) numa `stg` em HEAP. `OPENJSON` é suportado no pool dedicado segundo a Microsoft
  ([Learn](https://learn.microsoft.com/en-us/training/modules/understand-data-warehouse-developer-features-of-azure-synapse-analytics/8-work-json-data-sql-pools)),
  mas é testado no "teste do Synapse" (D19); se falhar, `JSON_VALUE`.
- **ADF:** ligar/pausar por atividade Web na REST API de gerenciamento com *managed identity*; loop `Until` até o
  pool ficar `Online` antes das procedures; pausa no caminho "ao concluir" e confirmação do estado `Paused` no fim.
- **`ctl`:** controla **lote e arquivo por tabela** (o Airbyte grava uma pasta por stream), não "pasta".
- **Centavos:** critério de aceite novo: soma das colunas monetárias na `stg` = soma na origem, por tabela, no lote.
- **Fuso:** tudo em UTC na `stg`; o D-1 é calculado em `America/Sao_Paulo` no `dw`.
- **D-1 às 08:00:** é **objetivo**, não SLA (best-effort, Airbyte local e sem alertas).
- **Oracle:** o conector não captura exclusões e tem nível de suporte baixo. O SCD2 do Oracle tem **granularidade
  por sync** (declarado, não "histórico fiel"); impacto no dinheiro nulo porque os valores ficam congelados no
  pedido (RN-32). Confirmar no simulador se há `DELETE` em `CITIES`/`CUSTOMERS`/`DRIVERS`; se houver, *full refresh*
  periódico das três tabelas pequenas detecta o que sumiu.
- **Contrato CDC:** o mapeamento `_ab_cdc_*` → `cdc_*` já está no modelo físico (F4.6); os exemplos reais de
  payload saem do teste local do Airbyte.
- **Retenção:** landing mantida inteira durante o projeto (é a fonte de reprocessamento; volume pequeno) e removida
  no fim; a `stg` guarda o lote; a regra exata entra no PRD.
- **CI e dados:** a esteira só aplica estrutura (tabelas, procedures); nunca carrega dado, então erro de dado não
  vai para log público. A carga roda no ADF (logs privados).
- **Custo do `plan`:** a estimativa por hora e por dia sai da API pública de preços da Azure e vai anexada à
  aprovação (escopo do `github-cd`). Preço do DW100c reconfirmado antes do apply. O pool cobra **por hora ativa**:
  ligar por minutos paga a hora.
- **State:** acesso restrito (RBAC) no storage do state, um state por ambiente, nenhum output sensível, versionamento
  do blob para recuperação.
- **Budget:** alertas têm 8 a 24 h de atraso; a proteção real é a pausa do ADF e a checagem de fim de sessão.

### Contestado e mantido

- **Três agentes-cliente (D16):** o GPT sugere só o `cliente-financeiro`. Mantido por decisão do usuário (custo baixo).
- **Parquet na landing:** o conector Azure Blob do Airbyte só grava CSV ou JSONL.
- **Azure SQL Database no lugar do Synapse:** o Synapse Dedicated é invariante; fica como plano B da D19.
- **Gatilho pelo GitHub Actions no lugar do ADF:** o ADF fica (D14); a ideia de só disparar com lote completo entra
  na decisão sobre o fim do sync.

### Decisões novas

| # | Pergunta | Decisão | Motivo |
|---|---|---|---|
| D19 | E se o Synapse não subir na free account? | **Primeira task pós-cadastro = "teste do Synapse":** cria workspace e pool DW100c, testa `OPENJSON` e autenticação só Entra, pausa (~1 h cobrada, ≈ US$ 1,20). **O pool nunca é apagado durante o projeto, só pausado** (o `destroy` do warehouse fica para o fim). Se a criação for negada: chamado de cota no mesmo dia; se negado ou mais de 3 dias, o usuário decide na hora entre converter para PAYG (mantém o crédito, perde o *spending limit*) ou Azure SQL Database serverless (muda o invariante) | Relato de free account que só criou o pool uma vez ([Q&A](https://learn.microsoft.com/en-us/answers/questions/532862/not-able-to-create-a-dedicated-sql-pool-2-time-und)); cota sobe por chamado. Confirmar no primeiro dia protege os 30 dias. Usuário de acordo em 2026-11-12 |
| D20 | Uso real do orquestrador | **O ADF existe para mostrar o desenho; a carga roda 1 a 3 vezes no projeto, disparada manualmente pelo usuário depois de ver o sync do Airbyte terminar** (o agente nunca dispara). Pipeline completo no Terraform (liga o pool, carrega, controla o lote no `ctl`, pausa sempre); **gatilho diário declarado no Terraform, mas desligado**. O D-1 passa a ser **objetivo de desenho** (como seria em produção), não meta operacional. Sem manifesto de lote, sem script de ciclo e sem pipeline "vigia". A exceção da D14 (ADF pausa sozinho) fica só para o fim da execução disparada pelo usuário | Decisão do usuário: o orquestrador é vitrine, não agenda. Disparo manual pós-sync elimina a corrida Airbyte × ADF apontada pelos revisores; o usuário acompanha a execução e o agente confere na checagem de fim de sessão. Poucas horas de Synapse no projeto inteiro. Usuário de acordo em 2026-11-12 |
| D21 | Airbyte ou dlt | **Fica o Airbyte, com prova local obrigatória (MUST) antes de abrir a conta:** sync completo do histórico (Postgres por CDC, Oracle por `UPDATED_AT`) para um destino local JSON do próprio Airbyte, sem conta Azure. Passa se terminar sem cair por memória; guarda os formatos dos registros (estrutura e metadados `_ab_cdc_*`, nunca linhas de `customers`/`drivers`) para o contrato da `stg`. Se cair: parar outros contêineres e aumentar a memória do Docker; se cair de novo, troca para o **dlt** (decisão registrada). Roda só depois do fim da geração do histórico; criar slot e publicação no Postgres exige confirmação do usuário na hora | Airbyte é ferramenta de mercado e já é a escolha da Azure (D11); com 1 a 3 syncs (D20) a memória só aperta em poucas janelas. A prova antecipa o maior risco (exit 137 em 2026-11-12) a custo zero. Usuário de acordo em 2026-11-12 |
| D22 | Slot de replicação e WAL do Postgres | **Slot só existe enquanto há sync previsto.** O slot da prova (D21) é removido depois dela; um novo é criado logo antes do primeiro sync real e removido depois do último. Sem teto `max_slot_wal_keep_size` por ora. Antes da prova, conferência só de leitura do espaço livre do Docker. Criar e remover slot e publicação: cada operação com "ok" do usuário na hora | O usuário não vai gerar carga contínua: no máximo cerca de uma semana de operações entre syncs, então o WAL retido fica pequeno. O risco real era slot esquecido por semanas, e a remoção resolve. Revisável: se a janela entre syncs crescer, entra o teto. Usuário de acordo em 2026-11-12 |
| D23 | Relógio de 30 dias e reserva de crédito | **(1) A conta Azure só abre quando o código das três arquiteturas da Azure** (`azure-warehouse`, `azure-lakehouse`, `azure-kappa`) **estiver pronto e validado sem conta** (Terraform `validate`, scripts, esteira, prova do Airbyte); os 30 dias ficam para `apply`, carga e conferência. **(2) A etapa B (modelagem do `dw`) é feita antes da conta**, olhando o dado no Postgres e no Oracle locais depois do fim da geração. **(3) Reserva de 25% do crédito intocada**; teto de planejamento do Warehouse de **US$ 20** (~10 h de Synapse no projeto, com o teste da D19 e as 1 a 3 cargas, mais armazenamento e ADF); os tetos de Lakehouse e Kappa saem do que sobrar | A free account é uma por pessoa: crédito e 30 dias servem às três arquiteturas da Azure. Os dois revisores apontaram o tempo como irreconciliável; tirar o desenvolvimento e a modelagem do relógio resolve. Amarra este projeto ao andamento dos outros dois da Azure. Usuário de acordo em 2026-11-12 |
| D24 | A esteira trava o primeiro `apply`? | **A esteira (`github-cd`) é o caminho normal do deploy e entra nos pré-requisitos da D23:** pronta e testada (T1 a T8, com stub) antes de a conta abrir. **Plano B só para o dsv:** se a esteira falhar durante os 30 dias, `apply` local com `plan`, estimativa por hora e por dia e "ok" do usuário (regra atual do `CLAUDE.md`), registrado como exceção; a esteira é consertada depois. O prd sai só pela esteira | Gargalo apontado pelo Gemini; com a D23 a esteira é construída fora do relógio, e o plano B impede que um problema de OIDC ou firewall trave a carga. Usuário de acordo em 2026-11-12 |

## Pendentes

- ADR nova via `/new-adr`: D7/D9/D11 (revisa a decisão 4 da ADR 006); D14 + D20 (ADF pausa o pool no fim da
  execução disparada pelo usuário); D17 + D24 (prd por tag, aprovação no dsv, plano B de `apply` local); D23 (conta
  só abre com as três arquiteturas da Azure prontas). Depois, atualizar os invariantes de custo, de promoção e de
  abertura de conta no `CLAUDE.md`.
- Projeto `github-cd` (esteira, subagente `cicd-engineer`, skills `github-configurar-environment`,
  `github-configurar-oidc-nuvem`, `github-promover-release`): pré-requisito da abertura da conta (D23, D24).
- A confirmar na arquitetura: suporte do Synapse Pipelines no Terraform (vs ADF); `sqlcmd` do runner e o firewall
  do Synapse (regra temporária no job, com a permissão na identidade OIDC); senha opcional do Synapse no `azurerm`.
- Confirmar no simulador se há `DELETE` em `CITIES`/`CUSTOMERS`/`DRIVERS` (decide o *full refresh* periódico).
- Impacto de D7/D9 no `regeracao-f5` (tasks 17 e 18) e na ADR 013: decisão do usuário.
- Fora deste projeto (D8): Databricks Free Edition no ADLS; tabelas e event hubs do Kappa.

## Próximo passo

Registrar a ADR (`/new-adr`) e rodar `harness-design` para gerar o PRD e montar o harness.
