# 015 — Orquestrador que pausa o pool e relógio da free account da Azure

**Status:** Aceita  
**Data:** 2026-11-12  
**Autores:** time  
**Revisa:** os invariantes de custo do `CLAUDE.md` "pausa e destroy nunca são automáticos" (ganha uma exceção) e
"(revisável) conta cloud só é aberta no início da fase correspondente" (fica mais restrito na Azure)

---

## Contexto

O Warehouse da Azure usa um Synapse Dedicated SQL Pool (DW100c, cerca de US$ 1,20/h em `eastus2`, cobrado por hora
ativa). A conta é uma **free account**: crédito de 30 dias e *spending limit* rígido. Duas regras do `CLAUDE.md`
batiam com o desenho que saiu do grill do `azure-warehouse` (D14, D19, D20 e D23 de
[01-grill.md](../../.claude/projetos/azure-warehouse/01-grill.md)):

1. **"Pausa nunca é automática."** O usuário quis um orquestrador com visão empresarial: a carga liga o pool, roda e
   desliga. Deixar o pool ligado à espera de uma pausa manual custaria crédito e contradiria o desenho.
2. **"Conta aberta no início da fase."** A free account é **uma por pessoa**: o crédito e os 30 dias servem às três
   arquiteturas da Azure (Warehouse, Lakehouse e Kappa). Abrir a conta para o Warehouse faria o relógio correr sobre as
   outras duas ainda por construir. Os dois revisores adversariais (Gemini e GPT) apontaram o tempo como o maior risco
   do plano.

Também pesou um relato de free account que só conseguiu criar o pool dedicado uma vez, mesmo depois de apagá-lo
([Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/532862/not-able-to-create-a-dedicated-sql-pool-2-time-und)).

## Decisão

1. **O Azure Data Factory é o orquestrador do Warehouse, declarado no Terraform**, e **pode ligar e pausar o pool**:
   - liga por atividade Web na REST API de gerenciamento, com *managed identity* e papel RBAC mínimo (ações
     `sqlPools/resume` e `sqlPools/pause`), e espera o pool ficar `Online` antes das procedures;
   - **pausa no fim de qualquer desfecho**, inclusive erro, e confirma o estado `Paused`.
2. **Exceção ao invariante "pausa nunca é automática", só para isso:** o ADF pausa o pool **no fim de uma execução que
   o usuário disparou**. O agente continua sem ligar, pausar ou disparar nada sozinho.
3. **O orquestrador é vitrine, não agenda:** a carga roda 1 a 3 vezes no projeto, **disparada manualmente pelo usuário**
   depois de ver o sync do Airbyte terminar. O gatilho diário existe no Terraform, **desligado**. O D-1 é objetivo de
   desenho, não meta operacional.
4. **O pool nunca é apagado durante o projeto**, só pausado; o `destroy` do warehouse fica para o fim. A primeira task
   depois do cadastro é o **teste do Synapse** (cria, testa, pausa). Se a criação for negada, o usuário abre chamado de
   cota; se negado ou mais de 3 dias, decide na hora entre converter para pagamento conforme o uso ou Azure SQL Database
   serverless.
5. **A conta Azure só abre quando o código das três arquiteturas da Azure estiver pronto e validado sem conta**
   (Terraform `validate`, scripts SQL, esteira com stub, prova local do Airbyte, modelagem do `dw`). Os 30 dias ficam
   para `apply`, carga e conferência.
6. **Reserva de 25% do crédito intocada.** O teto de planejamento do Warehouse é US$ 20; os de Lakehouse e Kappa saem do
   que sobrar.

## Alternativas consideradas

### Opção A — Pausa só manual, sem orquestrador ❌ Rejeitada

Preserva o invariante, mas a carga vira roteiro manual, o pool fica ligado enquanto o usuário não age e o desenho perde a
visão empresarial pedida.

### Opção B — ADF com pausa automática no fim da execução disparada ✅ Escolhida

O pool só fica ligado durante a carga, o desenho fica completo e versionado, e a exceção é estreita (um componente, um
momento).

### Opção C — Gatilho diário ativo, com manifesto de lote e pipeline "vigia" ❌ Rejeitada

Proposta na triagem dos revisores: um manifesto de lote evitaria a corrida entre o fim do sync e o gatilho, e um vigia
pausaria o pool esquecido. Com o disparo manual pós-sync, a corrida não existe, e o vigia ampliaria a pausa automática
sem necessidade.

### Opção D — Airflow local ❌ Rejeitada

Sem memória na máquina local (o Airbyte já ocupa o que sobra) e fora do ecossistema da Azure.

### Opção E — Abrir a conta no início da fase do Warehouse ❌ Rejeitada

O relógio de 30 dias correria sobre Lakehouse e Kappa ainda em construção.

## Consequências

### Positivas

- Pool ligado só durante a carga: poucas horas de Synapse no projeto inteiro.
- O desenho de produção (gatilho, pausa, controle de lote) fica versionado no Terraform.
- Os 30 dias de crédito não financiam desenvolvimento.

### Negativas / Tradeoffs

- O Warehouse fica amarrado ao andamento do `azure-lakehouse` e do `azure-kappa`: só vai para a nuvem quando os três
  estiverem prontos.
- O D-1 não é demonstrado em operação contínua, só no desenho.
- Ligar o pool por minutos paga a hora inteira.

### Riscos

- **A pausa do ADF falhar** (cancelamento, erro de autorização, serviço fora). Mitigação: o usuário acompanha a
  execução, o agente confere na checagem de fim de sessão, e o *spending limit* corta no limite.
- **Budget alerts com 8 a 24 h de atraso:** não servem como proteção imediata, só como aviso.
- **Synapse negado na free account:** coberto pelo item 4.

## Revisão

Esta ADR deve ser revisada se:

- o projeto passar a operar com carga agendada (o vigia volta à mesa);
- a conta deixar de ser free account (o relógio de 30 dias deixa de existir);
- o Synapse for trocado por outro serviço (item 4).
