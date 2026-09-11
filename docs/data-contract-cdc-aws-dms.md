# Contrato de dados — CDC canônico, extensão AWS DMS (Fase 2)

> Extensão do contrato canônico de CDC já definido na Onda 3
> (`.claude/sdd/features/DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md`) para incluir o
> AWS DMS como 3ª ferramenta de ingestão, ao lado de Airbyte (Postgres/Onda 3) e
> Debezium/Kafka Connect (Oracle/Onda 3). Mandato DC-M04 do
> `DEFINE_INGESTAO_AWS_FASE2.md`.

## 1. Identificação

| Campo | Valor |
|-------|--------|
| **Domínio** | Ingestão AWS — Fase 2 (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`) |
| **Dataset** | Todas as tabelas replicadas via AWS DMS (Postgres, Oracle, MongoDB) para o S3/Bronze e/ou Kinesis |
| **Pipeline** | `infra/aws/fase2-ingestao/` (DMS batch + real-time) |

## 2. Mapeamento das 4 colunas canônicas

A Silver/consumo (Redshift, Athena, Lambda consumidor do Kappa) **nunca** lê os
campos nativos do DMS diretamente — só as 4 colunas canônicas abaixo, mesma
disciplina já estabelecida na Onda 3.

| Coluna canônica | Origem no DMS (S3 target) | Origem no DMS (Kinesis target) |
|---|---|---|
| `cdc_operation` | Coluna `Op` (`I`/`U`/`D`), habilitada via `include_op_for_full_load = true` | Campo `Op` no envelope JSON do registro Kinesis |
| `cdc_commit_ts` | Coluna de timestamp configurada via `timestamp_column_name` | Campo de timestamp equivalente no envelope JSON |
| `cdc_sequence` | Concatenação de `transaction_id` + `transaction_record_id`, habilitados via `include_transaction_details = true` | Mesmos campos, presentes no envelope JSON via `include_transaction_details = true` no endpoint Kinesis |
| `cdc_source_system` | Constante por task (`postgres-dms-aws`, `oracle-dms-aws`, `mongo-dms-aws`) | Mesma constante, aplicada na Lambda consumidora ou em transformação downstream |

## 3. Status de validação

🔶 **Não confirmado com teste real.** O mapeamento de `transaction_id`/`transaction_record_id`
para `cdc_sequence` é uma leitura da documentação da AWS sobre as extra connection
attributes do DMS (`IncludeTransactionDetails`), não uma validação empírica neste
projeto — mesmo tipo de risco que a Onda 3 teve com o LogMiner do Oracle antes do
Build real (ver `DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md`, seção "Correções
pós-teste real"). **Ação obrigatória no início do `/build` real (quando a conta AWS
for aberta):** rodar a task DMS batch da Etapa 1 contra uma amostra pequena, inspecionar
o arquivo Parquet/CSV gerado no S3 e confirmar que essas colunas existem com o
formato esperado antes de escrever qualquer MERGE/COPY definitivo em produção.

## 4. Política de evolução

Mesma política já registrada no contrato da Onda 3: mudança incompatível (nova
coluna canônica, mudança de tipo semântico) exige atualizar este documento e as
4 origens (Airbyte, Debezium, DMS) na mesma revisão — nunca uma ferramenta só.

## Histórico

| Versão | Data | Alteração |
|--------|------|-----------|
| 1.0 | 2026-09-10 | Documento inicial — extensão do contrato canônico da Onda 3 para o AWS DMS, criado no `/build` de `DESIGN_INGESTAO_AWS_FASE2.md` |
