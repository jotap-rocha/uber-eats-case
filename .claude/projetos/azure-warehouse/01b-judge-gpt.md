# Revisão adversarial — 01-grill.md (GPT)

> Gerada manualmente pelo usuário no GPT em 2026-11-12, com o prompt da skill `adversarial-judge`.
> Consultiva, não bloqueante. A triagem e as decisões ficam no [01-grill.md](01-grill.md).
> Na colagem, o diagrama Mermaid veio como CSS renderizado; foi trocado aqui pela descrição do fluxo (3.2).
> As citações de fonte ("Microsoft Learn", "Airbyte Docs", "PyPI") vieram sem URL.

---

## 1. Suposições não verificadas ou provavelmente erradas

### 1.1. D14 — O ADF não garante, por si só, que o Synapse será pausado em qualquer cenário

A expressão "pausa sempre no fim, inclusive em erro" é mais forte do que a garantia descrita na arquitetura.

O ADF permite configurar caminhos de execução por sucesso, falha, conclusão e atividade ignorada. Isso ajuda a implementar uma rotina de encerramento, mas não equivale a uma garantia absoluta de execução do encerramento.

Há cenários que precisam ser tratados explicitamente:
- Falha na própria atividade que solicita a pausa.
- Cancelamento manual do pipeline.
- Timeout ou interrupção da execução.
- Indisponibilidade do serviço durante a tentativa de pausa.
- Falha de autenticação ou autorização da identidade gerenciada.
- Duas execuções concorrentes ou uma execução que ultrapassa a janela esperada.

A documentação da Microsoft confirma a existência dos caminhos condicionais do ADF, mas isso não significa que qualquer falha operacional assegure a execução da pausa.

Problema adicional: o documento diz que o ADF possui permissão para ligar e pausar o pool, mas não especifica exatamente qual mecanismo executará essas operações, qual API será chamada e quais permissões serão concedidas. Isso é parte central da decisão D14, não um detalhe de implementação.

Ajuste necessário: definir uma rotina de encerramento com tratamento explícito de falhas, timeout, cancelamento e confirmação do estado final do pool. Também deve existir uma verificação independente de recurso ligado fora da janela. Sem isso, a proteção depende de o próprio componente que pode falhar ser responsável por desligar o recurso.

### 1.2. D12 / D14 — O SLA D-1 às 08:00 não é sustentado pela orquestração descrita

O ADF começa verificando se existe uma pasta nova na landing. Entretanto, a ingestão é realizada anteriormente pelo Airbyte, em execução local, com janela própria. Não existe, na especificação, um mecanismo que garanta que a sincronização do Airbyte terminou antes de o ADF verificar a landing.

1. O horário de sincronização do Airbyte pode atrasar.
2. O ADF executa o gatilho diário.
3. O ADF não encontra a pasta esperada ou encontra arquivos ainda não finalizados.
4. A carga não acontece, ou acontece sobre um conjunto incompleto.
5. O compromisso de disponibilização às 08:00 deixa de ser cumprido.

A declaração de que a próxima carga recupera o pendente não resolve o atraso do fechamento financeiro.

Ajuste necessário: estabelecer um contrato de entrega entre Airbyte e ADF. Por exemplo, manifesto de lote com identificador, tabelas, arquivos, quantidade de registros, horário de início/fim e marcador de conclusão. O ADF só deve aceitar lotes comprovadamente finalizados. Além disso, é preciso esclarecer se o horário de 08:00 é um SLA de disponibilidade ou apenas um objetivo de execução em condições normais.

### 1.3. D7 / D9 — A garantia de recuperação sem perda e sem duplicidade é excessiva

A documentação do Airbyte descreve a entrega incremental como at-least-once: registros podem ser reenviados entre sincronizações. Portanto, a deduplicação precisa ser implementada e comprovada pelo consumidor, não presumida. O Postgres utiliza CDC; um evento de atualização ou exclusão não é equivalente a uma fotografia atual da linha.

O plano ainda não define: identificador único do evento CDC; ordenação de eventos para a mesma chave; tratamento de reentrega; tratamento de eventos atrasados; fronteira entre lotes consecutivos; como identificar um lote incompleto; como impedir que a mesma pasta seja aplicada duas vezes após uma falha parcial.

O critério de reprocessamento (apagar a pasta da stg e recarregar) cobre apenas uma parte do problema.

Ajuste necessário: definir a idempotência em torno de um identificador de evento e de um identificador de lote, com reconciliação entre estado do Airbyte, arquivos entregues e estado do Synapse.

### 1.4. D6 / D7 — Há uma incompatibilidade concreta entre OPENJSON e Dedicated SQL Pool (bloqueador técnico)

OPENJSON no Azure Synapse é documentado para Serverless SQL Pool, não para Dedicated SQL Pool. COPY INTO no Dedicated suporta CSV, Parquet e ORC; não suporta FILE_TYPE = 'JSONL'. O arquivo pode ser tratado como texto delimitado, mas isso precisa ser implementado e testado.

Alternativas:
1. Manter Dedicated SQL Pool e usar JSON_VALUE/JSON_QUERY para extrair propriedades escalares, depois de carregar cada linha como texto. Não contar com OPENJSON.
2. Usar Serverless SQL Pool para explorar e interpretar JSONL, e outro mecanismo para materializar os dados no Dedicated.
3. Transformar JSONL em Parquet antes de carregar a stg no Dedicated.

### 1.5. D7 — O conector Oracle escolhido tem limitações relevantes para a proposta

Conector Oracle DB do Airbyte: Full Refresh sim; Incremental Append sim; captura de exclusões incrementais não; CDC não; LogMiner não. A documentação identifica o conector como tendo nível de suporte baixo e taxa de sucesso de sincronização baixa.

Uma linha removida do Oracle não será representada por um evento de exclusão. Se uma dimensão for atualizada três vezes entre sincronizações, o SCD2 receberá apenas a última versão.

Para tabelas pequenas, uma alternativa seria fazer snapshots completos periódicos e comparar as chaves entre snapshots para identificar exclusões. Se o histórico intermediário for obrigatório, será necessário um mecanismo de auditoria ou CDC verdadeiro na origem.

### 1.6. D15 / D18 — A estratégia de autenticação do Synapse pode não ser compatível com o Terraform proposto

Na documentação atual do recurso azurerm_synapse_workspace, a ausência da senha do administrador SQL está condicionada à configuração de Customer Managed Key. A propriedade azuread_authentication_only é uma configuração separada. A combinação precisa ser testada com a versão exata do provider. Possibilidades: manter uma credencial de administrador SQL para provisionamento, desabilitando depois a autenticação SQL e protegendo o segredo no state; ou outro mecanismo de provisionamento.

### 1.7. D7 / D13 — O contrato CDC canônico não está suficientemente definido

Falta o mapeamento exato entre os metadados reais do Airbyte (_ab_cdc_*) e o contrato (cdc_operation, cdc_commit_ts, cdc_sequence, cdc_source_system): qual metadado define a operação; como distinguir snapshot de alteração; qual campo ordena os eventos; como converter exclusão em tombstone; qual campo é o instante de vigência. A conversão r → c precisa preservar a diferença entre snapshot e mudança. Incluir exemplos de payloads reais e seus registros normalizados na stg.

## 2. Lacunas

### 2.1. D12 / D14 — Falta um contrato formal de lote

Campos sugeridos: batch_id, source_system, stream_name, started_at, completed_at, status, file_count, record_count, schema_version, checksum. O lote só pode ser consumido depois de publicado um marcador de conclusão.

### 2.2. D6 / D13 — A qualidade definida não é suficiente para um fluxo financeiro

A contagem pode fechar com repasse duplicado, estorno não capturado, evento no restaurante errado, eventos fora de ordem. Na etapa B, exigir reconciliação por origem, período e entidade (vendas, estornos, repasses, eventos por operação CDC, chaves distintas, duplicidades). Regras explícitas de precisão monetária (DECIMAL, escala, arredondamento, negativos); nada de FLOAT.

### 2.3. D12 / D13 — Não existe estratégia de recuperação de CDC

Se max_slot_wal_keep_size for excedido, o slot pode ser invalidado e a sync não se recupera sozinha (recriar slot e nova carga completa). Faltam: monitoramento do WAL retido, limite de tempo sem sync, procedimento de slot invalidado e de re-snapshot, reconciliação posterior.

### 2.4. D12 — O teste local do Airbyte deveria ser obrigatório

Antes da conta Azure: conexão Postgres com CDC, Oracle incremental por UPDATED_AT, escrita no destino, JSONL válido, recuperação após interrupção, reexecução sem perda de estado.

### 2.5. D14 / Out of Scope — Não há observabilidade operacional

Sem notificação, o fechamento pode deixar de ser atualizado sem ninguém saber. Sem essa observabilidade, o D-1 deve ser tratado como best-effort, não como SLA.

### 2.6. D6 / D13 — Falta definir retenção e ciclo de vida da landing

Retenção de arquivos processados, rejeitados, lotes incompletos, manifestos e logs; se pasta processada pode ser removida.

### 2.7. D15 / D17 — Falta fechar a segurança do Terraform state e do runner

Quem lê e modifica o state, acesso do GitHub Actions, outputs sensíveis, recuperação do state, separação dsv/prd. Conectividade do runner ao endpoint SQL.

### 2.8. D16 — Os três agentes são escopo adicional

Para um projeto de uma pessoa, não colocaria os três como MUST da etapa A.

### 2.9. D17 — A estratégia de custo do terraform plan está incompleta

O plan não dá estimativa monetária; é preciso mecanismo adicional (preços, ferramenta, cálculo) anexado à aprovação, com margem de segurança.

## 3. Alternativas

### 3.1. D6 — Usar Serverless para inspecionar os dados antes de provisionar o Dedicated

Serverless lê JSONL com OPENROWSET e OPENJSON, cobra por volume processado; Dedicated só quando a etapa B precisar.

### 3.2. D12 / D14 — Um único fluxo de orquestração

Fluxo proposto (diagrama original em Mermaid): agendador local → dispara sync do Airbyte → aguarda conclusão → sync concluída? Não: registra falha e notifica. Sim: publica manifesto do lote → dispara pipeline do ADF → resume do Synapse → carrega e valida a stg → pausa o Synapse → confirma lote processado. Um script Python local controla o ciclo pela API do Airbyte. Não resolve a máquina local desligada (D-1 segue best-effort).

### 3.3. D7 — Diferenciar estratégia de histórico para Postgres e Oracle

Postgres: CDC com eventos brutos, posição de log, deduplicação e exclusões. Oracle: snapshot periódico com comparação de chaves, ou tabela de auditoria por trigger, ou CDC verdadeiro. Não chamar de SCD2 historicamente fiel o que recebe só a última versão entre syncs.

### 3.4. D16 — Criar apenas o agente necessário ao projeto

### 3.5. D17 — Separar a primeira entrega da automação completa de deploy

1. Terraform validado e infra provisionada por execução manual aprovada. 2. Deploy automatizado em dsv com OIDC e state remoto. 3. Promoção para prd por tag e aprovação.

### 3.6. D13 — Não tornar MERGE uma decisão irreversível

Comparar MERGE, UPDATE + INSERT e CTAS com o volume real.

## 4. Riscos

### 4.1. Risco financeiro — D1, D3, D4, D14 (alto)

Budget só alerta (latência de 8 a 24 h); spending limit pode desabilitar a assinatura inteira. Pausado, o compute para de cobrar mas o armazenamento continua. O Dedicated cobra por hora ativa e pelo maior nível de computação em cada hora: ligar e pausar em minutos não significa pagar só os minutos. Não usar os US$ 200 como orçamento operacional: definir reserva e cenários de backfill, operação diária, falha e reprocessamento. Reconfirmar o preço de US$ 1,20/h antes de provisionar.

### 4.2. Risco técnico — perda do slot de replicação (D7 / D12)

### 4.3. Risco técnico — pool permanecer ligado (D14)

Não deixar a proteção financeira depender exclusivamente do ADF.

### 4.4. Risco de segurança — identidades inconsistentes (D15 / D18)

Service principal do Airbyte na D15 vs SAS na D18. Faltam permissões exatas do SAS, renovação, revogação, garantia de não aparecer em log.

### 4.5. Risco de segurança — exposição do Terraform state (D15 / D17)

RBAC restrito, Entra/OIDC, estados separados, sem outputs sensíveis, backup do state.

### 4.6. Risco de escopo — ambição vs capacidade (D1, D8, D16, D17)

~12 h em quatro semanas. Prioridade rígida: 1. Airbyte local; 2. ADLS recebendo JSONL; 3. um lote completo validado; 4. Synapse carregando a stg; 5. pool comprovadamente pausado; 6. só depois as demais tabelas, automações e agentes.

### 4.7. Risco de escopo funcional — a etapa A não resolve o problema financeiro

O cliente-financeiro não pode emitir veredito definitivo antes da etapa B.

**Conclusão do revisor:** três pontos exigem resolução antes do harness-design: (1) D6/D7 parsing do JSONL no Dedicated; (2) D12/D14 contrato de conclusão do lote e garantia de pausa; (3) D7 exclusões no Oracle e versões intermediárias no SCD2.
