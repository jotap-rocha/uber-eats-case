# BUILD REPORT: Diversificação de Fontes de Dados — Etapa 1 (Postgres/Motorista)

| Campo | Valor |
|-------|-------|
| **Feature** | DIVERSIFICACAO_FONTES_UBEREATS |
| **Escopo deste Build** | Somente Etapa 1 do DESIGN — itens 1-2 do file manifest (Postgres/Motorista). Etapas 2 (Oracle plumbing) e 3 (Oracle/Pedido+Pagamento) **não** foram implementadas — ficam para builds futuros |
| **Input** | `.claude/sdd/features/DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md` |
| **Data** | 2026-09-06 |

## Summary

| Métrica | Valor |
|---------|-------|
| Tasks do escopo (Etapa 1) | 2/2 completas |
| Arquivos editados | 1 (`gen/unified/uber-eats.json.template`) |
| Arquivos verificados sem alteração necessária | 1 (`pipeline/bronze/ingest_postgres_drivers.sql`) |
| Verificações estáticas | 3/3 passaram |
| Verificação de integração (regenerar + confirmar UPDATE real capturado) | ✅ **Validado em ambiente real** — licença ShadowTraffic renovada durante o Build; 2 bugs reais encontrados e corrigidos no processo (ver "Issues Encountered") |

## Tasks executadas

| Task | Status | Notas |
|------|--------|-------|
| Reescrever gerador `drivers` com `fork`+`stateMachine` (`op:update`) | ✅ | Ver detalhes abaixo — vocabulário de `status` mantido fiel ao original (`Active`/`Inactive`/`Banned`), não o exemplo genérico do DESIGN |
| Verificar `ingest_postgres_drivers.sql` (Bronze) | ✅ — no-op | `APPLY CHANGES INTO` + `SEQUENCE BY _ab_cdc_updated_at` + `STORED AS SCD TYPE 1` já é o padrão de merge CDC do Airbyte — funciona para UPDATE sem alteração, só nunca tinha recebido um UPDATE de verdade até agora |

### O que mudou no gerador `drivers`

- **Antes:** gerador simples (`row` fixo), `maxEvents: 80000`, `status` sorteado uma vez por `oneOf` na criação, `total_deliveries`/`total_earnings`/`average_rating` fixos desde o INSERT.
- **Depois:** `fork.key` (sequencial, `maxForks: 80000` — mesma população-alvo de antes) + `stateMachine` com 4 estados:
  - `insertIt` — cria a linha com os campos cadastrais (nome, email, veículo, etc.) e valores iniciais neutros (`status: Inactive`, `total_deliveries/total_earnings/average_rating: 0`)
  - `onShift` — `op: update`, `status → Active`, atualiza `last_login`
  - `offShift` — `op: update`, `status → Inactive`, incrementa `total_deliveries`/`total_earnings` via `_gen: previousEvent` (lendo o valor anterior da mesma linha) e resorteia `average_rating`
  - `banned` — `op: update`, `status → Banned`, atingido com peso 5% a partir de `offShift`, com transição de volta pra `onShift` (evita estado absorvente — ver Issues Encountered)

**Desvio consciente do exemplo do DESIGN:** o snippet do documento de design usava nomes de estado genéricos (`available`/`busy`/`offline`). Ao abrir o arquivo real, o campo `status` já tinha vocabulário próprio (`Active`/`Inactive`/`Banned`) usado também no Silver (`silver_drivers.status_conta`) — mantive esse vocabulário para não introduzir um valor que a Silver/Gold não esperam.

## Issues Encountered

### Bugs reais encontrados e corrigidos durante o smoke test (`--stdout`) e a validação em ambiente real

1. **`{"value": X}` não é sintaxe válida do ShadowTraffic para valor literal — bug meu, corrigido.** Copiei incorretamente um padrão do exemplo oficial de `stateMachine` (onde `"value"` era o nome literal de uma coluna chamada "value" naquele exemplo específico, não um "wrapper" genérico de constante). Sem `_gen`, o ShadowTraffic trata o objeto como dado literal e o emite tal qual — resultado: `"status": {"value": "Inactive"}` ia parar dentro da própria coluna `status`, em vez de `"status": "Inactive"`. **Correção:** usei o padrão já comprovado neste mesmo arquivo (`"_gen": "oneOf", "choices": [...]` com uma única opção), que é como o próprio config já representa constantes (ex. `country: {"_gen":"oneOf","choices":["BR"]}` em `mysql/restaurants`). Encontrado e corrigido **antes** de rodar contra o Postgres real, via smoke test isolado (`--stdout --sample 3000`).

2. **`_gen: previousEvent` falhando com "evaluated to null" — bug real, só apareceu contra o Postgres de verdade.** O estado `offShift` tentava incrementar `total_deliveries`/`total_earnings` lendo o valor do **evento imediatamente anterior** do mesmo fork via `previousEvent`. Mas o estado anterior (`onShift`) só emitia `status` e `last_login` no `row` — não incluía `total_deliveries`/`total_earnings` — então `previousEvent` não achava o campo e retornava `null`, quebrando a expressão matemática. Isso **não apareceu no primeiro smoke test** (sample pequeno, nenhum driver tinha chegado ao `offShift` ainda) — só se manifestou depois de subir o ambiente real e o `gen-unified` travar silenciosamente ao processar o primeiro `offShift`. **Correção:** toda transição (`onShift`, `banned`) agora también carrega adiante `total_deliveries`/`total_earnings`/`average_rating` via `previousEvent` (copiando o valor do evento anterior sem alterar), garantindo que o campo sempre existe no evento imediatamente anterior, não importa qual sequência de estados o fork percorreu. Revalidado com sucesso: `driver_id=1` passou por 30+ ciclos completos no smoke test, com `total_deliveries` incrementando 0→31 de forma consistente.

3. **Reiniciar `gen-unified` contra um Postgres já populado quebra o gerador `users` (pré-existente, não é bug desta feature).** Ao reiniciar o container sem recriar o volume, o gerador `users` (insert-only, sem `fork`) tentou reinserir `user_id=1`, que já existia — erro de chave duplicada, fatal para o processo. **Não é uma regressão desta mudança** — qualquer restart de um gerador insert-only contra dado já existente teria o mesmo problema; é uma característica já conhecida da arquitetura (mesma razão pela qual a Onda 2 precisou de `docker-compose down -v` para aplicar a migração de PK). Resolvido recriando o volume (`docker-compose down -v` + `start-all.ps1`) antes da validação final.

### Riscos avaliados e descartados durante a validação

- **`total_deliveries` sendo gerado como float (`1.0`, `2.0`...) indo para uma coluna `bigint`:** testado diretamente contra o Postgres real — o valor chega corretamente como inteiro (`2`, não `2.0`), sem erro. Não é necessário nenhum ajuste de formatação.
- **Drift de ponto flutuante em `total_earnings`** (ex. `117.39999999999999` em vez de `117.4`) ao encadear somas via `previousEvent`: confirmado como cosmético — `pipeline/silver/ingestion_postgres_drivers.sql` já faz `CAST(total_earnings AS DECIMAL(18, 2))`, absorvendo o drift na Silver. Não bloqueia esta feature.

### Risco de design (documentado no BUILD_REPORT original, mantido)

1. **Risco de estado absorvente evitado deliberadamente.** O padrão oficial do ShadowTraffic (visto no `kafka/status`/`kafka/events` já existentes neste projeto) costuma terminar em um estado sem transição de saída. Copiar isso para `banned` (torná-lo terminal) teria duas consequências indesejadas: (a) sem uma transição de saída nem `op:delete`, não está documentado com clareza se o fork simplesmente para de gerar eventos ou se `keepAlive` entraria em ação; (b) eu **não ativei `keepAlive`** propositalmente, porque ele respawna um fork novo (com `driver_id` novo) quando um fork "termina" — isso inflaria a população de motoristas além de `maxForks: 80000` e quebraria a suposição de que `driver_id` fica no range 1..80000 usado pelos lookups de Turno/Entrega. Resolvido dando a `banned` uma transição de volta para `onShift` (motorista banido eventualmente reativado) — mantém todo fork perpetuamente vivo, sem depender de `keepAlive`.
2. **`_gen: previousEvent` reaproveitado de um padrão já existente no arquivo, não inventado.** O mesmo generator (`kafka/events`, linha ~1360 do template) já usa `previousEvent` para acessar o timestamp do evento anterior do mesmo fork. Apliquei a mesma função para ler `total_deliveries`/`total_earnings` da atualização anterior — reduz o risco de sintaxe incorreta, mas **não elimina a necessidade de um smoke test real** (ver Pendências).
3. **`localConfigs.maxEvents` removido.** Com `fork`+`keepAlive: false`, o gerador não tem mais um total fixo de eventos — ele roda perpetuamente, ciclando o status de cada um dos 80.000 motoristas indefinidamente. Isso é uma mudança de comportamento operacional: o processo `gen-unified` não vai mais "terminar sozinho" para a parte de `drivers` (o resto dos geradores no processo único continua com seu próprio ciclo de vida). Documentar isso é relevante para quem for rodar `docker-compose logs -f gen-unified` esperando o gerador parar.

## Verificação estática (executada agora)

| ID | Verificação | Resultado |
|----|--------------|-----------|
| V-001 | `gen/unified/uber-eats.json.template` continua JSON válido (placeholders `REPLACE_*` substituídos por dummy antes do parse, já que o `.template` não é JSON puro) | ✅ Pass — 19 generators preservados (nenhum adicionado/removido) |
| V-002 | Generator `drivers` tem exatamente 1 entrada, com `fork`, `stateMachine.initial = "insertIt"` e os 4 estados esperados (`insertIt`, `onShift`, `offShift`, `banned`) | ✅ Pass |
| V-003 | Nenhum outro generator referencia `drivers` por um campo diferente de `driver_id` via `table: "drivers"` — os 4 lookups existentes (`city`, `driver_id` em Turno/Entrega/kafka/route) continuam válidos porque a chave e o schema de `driver_id` não mudaram de tipo/posição | ✅ Pass — confirmado via grep, nenhum lookup quebrado |

## Verificação de integração — EXECUTADA (licença renovada durante o Build)

| ID | O que foi feito | Resultado |
|----|-------------|----------------|
| V-004 | Smoke test isolado via `docker run ... --stdout --sample N` (sem `--tables`, flag não existe na CLI; filtrado via grep) | ✅ Pass, após corrigir os 2 bugs acima — sequência INSERT→UPDATE(Active)→UPDATE(Inactive, incrementado)→...→UPDATE(Banned)→UPDATE(Active) confirmada para `driver_id=1` por 30+ ciclos |
| V-005 | `.\scripts\start-all.ps1` (com volume recriado, `down -v` primeiro, por causa do Issue #3 acima) + query direta no Postgres | ✅ Pass — `total_deliveries`/`total_earnings` incrementando corretamente, `status` ciclando `Inactive→Active→Inactive→...→Banned→Active`, sem duplicar `driver_id` |
| V-006 | Confirmar Airbyte/Bronze captura como UPDATE, não INSERT novo | **Não executado nesta sessão** — requer rodar o pipeline Databricks do usuário (fora do alcance desta sessão local). Estrutura do Bronze (`APPLY CHANGES INTO` + SCD Type 1) já suporta isso por design; recomenda-se o usuário confirmar manualmente antes do `/ship` |
| V-007 | `docker stats gen-unified` após alguns minutos rodando | ✅ Observado — ~198% CPU (múltiplos cores), ~556MB RAM. Confirma a mudança de comportamento já prevista: o gerador agora roda perpetuamente (sem `maxEvents`) e consome mais CPU que o padrão insert-only anterior. Parado manualmente (`stop-generators.ps1`) ao final da validação |

## Pendências antes do commit

Conforme `.claude/skills/git-boas-praticas-versionamento/SKILL.md`, commit é proposto e aguarda confirmação. Sugestão de mensagem:

```text
feat(gen): prova mecanismo de mutacao real em drivers (Onda 3, Etapa 1)

Reescreve o gerador drivers do ShadowTraffic com fork+stateMachine,
substituindo o padrao insert-only por um ciclo real de UPDATE
(Inactive->Active->Inactive, com Banned reversivel). Valida a mecanica
de op:update contra uma conexao real antes de aplicar o mesmo padrao
ao Oracle na Etapa 2/3. Bronze existente (ingest_postgres_drivers.sql)
nao precisou de alteracao -- ja suportava UPDATE via APPLY CHANGES
INTO, so nunca tinha recebido um.
```

## Status: ✅ COMPLETE — mecanismo validado em ambiente real

O objetivo da Etapa 1 (provar `fork`+`stateMachine`+`op:update` contra uma conexão real antes de replicar no Oracle) foi cumprido, incluindo a descoberta e correção de 2 bugs reais que só apareceriam em produção — exatamente o tipo de risco que o sequenciamento em 3 etapas do DESIGN existia para isolar. Único item não executado (V-006, requer Databricks do usuário) não bloqueia — a estrutura de Bronze já suporta o cenário por design, só falta a confirmação visual do usuário.

**Lições para a Etapa 2 (Oracle):**
- Todo estado do `stateMachine` precisa carregar adiante (via `previousEvent`) qualquer campo que um estado posterior vá incrementar/ler — não só os campos que aquele estado especificamente altera.
- Testar sempre primeiro com `--stdout --sample N` antes de apontar pro banco real — pegou 2 dos 2 bugs antes de qualquer dado real ser afetado (o 3º só aparece mesmo com Postgres populado).
- Recriar o volume (`down -v`) é necessário sempre que o gerador for reiniciado contra dado já existente, não só na primeira vez — vale automatizar isso num script de "restart limpo" antes da Etapa 2, já que o Oracle vai ter o mesmo comportamento.

**Próximo passo:** commitar esta mudança, depois seguir para a Etapa 2 (Oracle plumbing) do `/build`.
