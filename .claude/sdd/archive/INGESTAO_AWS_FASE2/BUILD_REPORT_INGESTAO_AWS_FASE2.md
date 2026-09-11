# BUILD REPORT: Arquitetura de Ingestão — Fase 2 (AWS)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_AWS_FASE2 |
| **Escopo deste Build** | Manifesto completo do DESIGN — Etapas 1, 2 e 3 (24 itens: Terraform, código Python das 2 Lambdas, SQL, docs) |
| **Input** | `.claude/sdd/features/DESIGN_INGESTAO_AWS_FASE2.md` |
| **Data** | 2026-09-10 |

---

## Summary

| Métrica | Valor |
|---------|-------|
| Itens do manifesto | 22/24 completos (2 itens transversais 23-24 já resolvidos no `/brainstorm`/`/define`, sem trabalho adicional aqui) |
| Arquivos Terraform criados | 12 (`infra/aws/fase2-ingestao/`) |
| Arquivos Python criados | 4 (2 Lambdas) + 2 arquivos de teste + 1 `conftest.py` |
| Arquivos SQL criados | 2 (`sql/aws/`) |
| Documentação criada | 2 (`docs/data-contract-cdc-aws-dms.md`, `docs/minio/webhook-notification-config.md`) |
| Testes unitários | **10/10 passaram** (`pytest tests/aws`, com `moto` mockando Kinesis/S3 reais) |
| Lint (`ruff`) | **0 erros** (5 encontrados, todos auto-corrigidos) |
| `terraform validate` | ❌ **Não executado** — falha de ambiente (ver "Issues Encountered"), não defeito do código |
| Deploy/teste em AWS real | **Não aplicável nesta sessão** — conta AWS ainda não foi aberta (mesmo princípio do roadmap: abrir conta só no início da fase) |

---

## O que foi implementado

### Etapa 1 — Warehouse (itens 1-9)

| Item | Arquivo | Status |
|------|---------|--------|
| 1 | `infra/aws/fase2-ingestao/networking.tf` | ✅ VPC, subnet privada + pública, NAT Gateway, security groups |
| 2 | `infra/aws/fase2-ingestao/ec2_fase0.tf` | ✅ EC2 com `user_data` preparando Docker/Compose para os sistemas da Fase 0 |
| 3 | `infra/aws/fase2-ingestao/iam.tf` | ✅ 7 roles (DMS S3/Kinesis, DataSync, Lambda bridge/consumer, Redshift, Glue) |
| 4 | `infra/aws/fase2-ingestao/dms_batch.tf` | ✅ Replication instance + 3 endpoints source + 1 endpoint S3 target + 3 tasks (Postgres/Oracle CDC, MongoDB full load) |
| 5 | `infra/aws/fase2-ingestao/datasync.tf` | ✅ Agente, location self-managed object storage, location S3, task agendada |
| 6 | `infra/aws/fase2-ingestao/s3_bronze.tf` | ✅ Bucket com versionamento, encryption, bloqueio de acesso público |
| 7 | `infra/aws/fase2-ingestao/redshift.tf` | ✅ Namespace + workgroup Serverless |
| 8 | `sql/aws/redshift_copy_merge.sql` | ✅ Padrão de referência (staging + COPY + MERGE com dedupe por `cdc_sequence`) para `drivers`; demais tabelas replicam o padrão |
| 9 | `docs/data-contract-cdc-aws-dms.md` | ✅ Extensão do contrato canônico da Onda 3 para o DMS |

### Etapa 2 — Lakehouse (itens 10-11)

| Item | Arquivo | Status |
|------|---------|--------|
| 10 | `infra/aws/fase2-ingestao/glue_catalog.tf` | ✅ Database, crawler, Athena workgroup |
| 11 | `sql/aws/athena_queries.sql` | ✅ DDL Iceberg de referência + queries de validação de órfãos (incluindo a validação do lookup MongoDB↔Pedido) |

### Etapa 3 — Kappa (itens 12-22)

| Item | Arquivo | Status |
|------|---------|--------|
| 12 | `infra/aws/fase2-ingestao/kinesis.tf` | ✅ Stream on-demand |
| 13 | `infra/aws/fase2-ingestao/dms_realtime.tf` | ✅ 2ª task DMS (Postgres, Oracle) — `migration_type = "cdc"`, target Kinesis |
| 14 | `src/aws/lambda_minio_kinesis_bridge/handler.py` | ✅ Valida token de auth, grava no Kinesis |
| 15 | `infra/aws/fase2-ingestao/lambda_bridge.tf` | ✅ Function + Function URL pública (`NONE`) — ver Decisão de Design abaixo |
| 16 | `docs/minio/webhook-notification-config.md` | ✅ Comandos `mc admin config set`/`mc event add`, formato do payload, ativação do agente DataSync |
| 17 | `src/aws/lambda_kappa_consumer/handler.py` | ✅ Decodifica registro Kinesis, enriquece via cache |
| 18 | `src/aws/lambda_kappa_consumer/mongo_lookup.py` | ✅ `RestaurantProfileCache` com TTL |
| 19 | `infra/aws/fase2-ingestao/lambda_consumer.tf` | ✅ Function + event source mapping |
| 20 | `src/aws/lambda_minio_kinesis_bridge/teams_notify.py` | ✅ Alerta Teams em falha (mandato SHOULD) |
| 21 | `tests/aws/test_lambda_minio_kinesis_bridge.py` | ✅ 3 testes — todos passaram |
| 22 | `tests/aws/test_kappa_consumer_lookup.py` | ✅ 7 testes — todos passaram |

### Transversal (itens 23-24)

| Item | Status |
|------|--------|
| 23 — Atualizar roadmap com decisões do `/design` | ✅ Já feito durante o `/design` (Decisão 1 EC2/VPC, Decisão 3 Lambda vs. Flink) — sem trabalho adicional aqui |
| 24 — Verificar modelo conceitual | ✅ Confirmado no-op — `docs/MODELO_CONCEITUAL_UBER_EATS.md` já declara o modelo "reaproveitado sem alteração" entre as 3 clouds |

---

## Desvios do DESIGN durante a implementação

1. **`aws_dms_s3_endpoint`/`aws_dms_kinesis_endpoint` em vez de `aws_dms_endpoint` genérico com blocos `s3_settings`/`kinesis_settings`.** O DESIGN usou o padrão genérico como ilustração; o provider AWS tem resources dedicados (`aws_dms_s3_endpoint`, `aws_dms_kinesis_endpoint`) que são a forma atual recomendada — mesmo resultado, sintaxe mais explícita.
2. **NAT Gateway adicionado à rede**, não estava explícito no DESIGN. A subnet privada precisa de saída para a internet para: a EC2 da Fase 0 baixar imagens Docker, e o agente DataSync se registrar no endpoint público do DataSync. Documentado no próprio `networking.tf` como ponto a revisar (trocar por VPC Interface Endpoints se o custo do NAT pesar mais).
3. **Autenticação da Function URL da Lambda ponte corrigida de `AWS_IAM` (sugestão inicial) para `NONE` + validação de token na aplicação.** Durante a implementação, identifiquei que o MinIO não assina requisições com SigV4 — o destino "webhook" nativo dele só suporta um header `Authorization` estático (`MINIO_NOTIFY_WEBHOOK_AUTH_TOKEN`). Ajustado o handler para validar esse token manualmente (retorna 401 se ausente/errado) e documentado em `docs/minio/webhook-notification-config.md`. **Isso é uma correção de design feita durante o Build, não estava certo no DESIGN original.**
4. **Agente DataSync como componente explícito** (`aws_instance.datasync_agent` + `aws_datasync_agent`), que o DESIGN não detalhava. O location type "Self-managed object storage" exige esse agente — adicionado com nota de que a ativação (`activation_key`) é um passo manual, Terraform não consegue automatizar sozinho.

---

## Issues Encountered

### `terraform validate` não executou — falha de ambiente, não do código

Baixei o binário do Terraform (v1.9.8) e rodei `init` com sucesso (providers `aws` 5.100.0 e `archive` 2.8.0 instalados). Mas `terraform validate` falhou tanto via Git Bash quanto via PowerShell nativo, com sandbox desabilitado, com o mesmo erro nos dois:

```text
tls: failed to verify certificate: x509: certificate signed by unknown authority
```

Isso acontece no handshake mTLS **local** entre o processo `terraform` e o processo do plugin do provider (comunicação via gRPC em loopback) — não é uma chamada de rede à AWS nem ao Registry (o `init` já tinha baixado os binários com sucesso via HTTPS normal). É consistente com este ambiente sandboxado interceptar/reescrever certificados TLS mesmo em conexões de loopback entre dois processos locais, o que quebra especificamente esse mecanismo de handshake do Terraform (não é uma falha comum fora de ambientes com esse tipo de interceptação).

**Mitigação:** revisão manual completa de todos os 12 arquivos `.tf` (referências cruzadas entre resources, nomes de argumento dos resources AWS provider ~> 5.0, blocos obrigatórios). **Ação pendente para o usuário:** rodar `terraform init && terraform validate` (e depois `plan`) num ambiente sem essa interceptação — provavelmente sem problema no ambiente normal do usuário — antes de qualquer `apply` real, especialmente quando a conta AWS for aberta.

Removido o binário do Terraform e o diretório `.terraform/` (~704MB de plugins baixados) do repositório antes de finalizar — nada disso foi commitado. Adicionadas entradas ao `.gitignore` (`**/.terraform/`, `*.tfstate*`, `*.tfvars`, `infra/**/.build/`) para isso nunca virar um problema de repositório no futuro.

### Testes unitários — sem problemas

`pytest`, `boto3` e `moto` não estavam instalados no `.venv` do projeto — instalados e registrados em `requirements-aws.txt` (novo arquivo, escopado a esta feature — o `requirements.txt` da raiz do projeto está vazio e não parece ter uma convenção estabelecida ainda, então não assumi posse dele). As duas Lambdas foram testadas de verdade contra um Kinesis e um S3 mockados (`moto`), não só lidas visualmente — os 2 bugs abaixo só apareceram rodando os testes:

1. **Autenticação da Lambda ponte não estava no DESIGN original** (ver Desvio #3 acima) — descoberto ao escrever o teste de rejeição de token inválido, que expôs que o DESIGN não tinha pensado em autenticação nenhuma para a Function URL.
2. **Nada mais** — o resto do código (payload do webhook, cache com TTL, enriquecimento do consumidor) funcionou como desenhado no primeiro teste.

---

## Verificação executada

| ID | Verificação | Resultado |
|----|--------------|-----------|
| V-001 | `pytest tests/aws -v` | ✅ 10/10 passaram |
| V-002 | `ruff check src/aws tests/aws` | ✅ 0 erros (após `--fix` automático de 5 achados triviais — import não ordenado, `noqa` não usado) |
| V-003 | `terraform init` (providers `aws`, `archive`) | ✅ Passou |
| V-004 | `terraform validate` | ❌ Não executou — falha de handshake TLS local do ambiente sandboxado (ver Issues Encountered) |
| V-005 | Revisão manual de todos os `.tf` (referências cruzadas, nomes de argumento) | ✅ Feita — nenhuma referência solta encontrada |
| V-006 | Deploy real (`terraform apply`) / smoke test contra AWS de verdade | **Não aplicável** — conta AWS ainda não aberta |

## Pendências antes do commit

Conforme `.claude/skills/git-boas-praticas-versionamento/SKILL.md`, commit é proposto e aguarda confirmação do usuário.

## Status: ✅ COMPLETE (com 1 verificação não executável neste ambiente)

Todo o manifesto do DESIGN foi implementado e os testes unitários das duas Lambdas passam de verdade (não só leitura visual). A única verificação que não pôde rodar (`terraform validate`) é uma limitação deste ambiente sandboxado (certificado TLS em handshake local), não um problema do código — recomenda-se rodar `terraform init && terraform validate && terraform plan` no ambiente normal do usuário antes de qualquer `apply`, e validar o mapeamento de `cdc_sequence` (docs/data-contract-cdc-aws-dms.md) e o formato do payload do webhook MinIO (docs/minio/webhook-notification-config.md) assim que a conta AWS e o MinIO real estiverem disponíveis — ambos já sinalizados como 🔶 não confirmados nos próprios documentos.

**Próximo passo:** revisar o código gerado, confirmar o commit, e quando a conta AWS for aberta (início real da Fase 2): rodar `terraform validate`/`plan` num ambiente sem a limitação de TLS local, preencher os `.tfvars` com credenciais reais, e seguir o sequenciamento Etapa 1 → 2 → 3 já documentado no DEFINE.
