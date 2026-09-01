# BUILD REPORT: Unificação de Identidade Postgres×MinIO (Onda 2)

| Campo | Valor |
|-------|-------|
| **Feature** | UNIFICACAO_IDENTIDADE_POSTGRES_MINIO |
| **Input** | `.claude/sdd/features/DESIGN_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md` |
| **Data** | 2026-08-24 |

## Summary

| Métrica | Valor |
|---------|-------|
| Tasks de código/config | 10/10 completas (+ 5 arquivos de documentação/scripts auxiliares corrigidos além do manifesto original) |
| Arquivos criados | 2 (`gen/unified/uber-eats.json.template`, `pipeline/silver/ingestion_postgres_drivers.sql`) |
| Arquivos editados | 11 |
| Arquivos removidos | 5 (`gen/postgres/users.json(.template)`, `drivers.json(.template)`, `gen/minio/uber-eats.json`, 2 scripts Silver antigos de motorista) |
| Verificações estáticas | 6/6 passaram |
| Verificações de integração | **Pendentes — exigem execução manual do usuário** |

## Tasks executadas

| Task | Status | Notas |
|------|--------|-------|
| `sql/create_users_table.sql`: PK uuid→int | ✅ | |
| `sql/create_drivers_table.sql`: PK uuid→int + 5 campos novos | ✅ | `vehicle_make`, `vehicle_model`, `vehicle_year`, `license_number`, `city` |
| `gen/unified/uber-eats.json.template` (novo) | ✅ | Gerado programaticamente a partir dos 3 configs antigos, com validação automática de que nenhuma referência aos streams aposentados ficou para trás |
| Remover `gen/postgres/*`, `gen/minio/uber-eats.json` | ✅ | |
| `gen/setup-configs.ps1` | ✅ | Gera 1 arquivo unificado em vez de 2 |
| `docker-compose.yml` | ✅ | 3 serviços → 1 (`gen-unified`) |
| `pipeline/silver/ingestion_kafka_orders.sql` | ✅ | `cpf_usuario` → `id_usuario` |
| `pipeline/silver/ingestion_postgres_drivers.sql` (novo) | ✅ | Substitui os 2 scripts antigos — `silver_drivers` |
| Remover os 2 scripts Silver antigos de motorista | ✅ | |
| `docs/MODELO_CONCEITUAL_UBER_EATS.md` | ✅ | Zero pendências |

### Além do manifesto original (achados durante o Build)

Ao rastrear todas as referências aos 3 containers antigos, encontrei mais 5 arquivos que ficariam quebrados/desatualizados se não fossem corrigidos: `scripts/start-generators.ps1`, `scripts/stop-generators.ps1`, `scripts/start-all.ps1`, `scripts/reset-all.ps1`, `scripts/README.md`, `docs/automacao/README.md`, `docs/shadowtraffic/README.md` — todos atualizados para referenciar `gen-unified` em vez de `gen-drivers`/`gen-users`/`gen-minio`.

## Verificação estática (executada agora)

| ID | Verificação | Resultado |
|----|--------------|-----------|
| V-001 | Template unificado válido após substituição de placeholders | ✅ Pass — 19 generators (2 Postgres + 17 MinIO) |
| V-002 | Arquivos antigos removidos | ✅ Pass — 5/5 removidos |
| V-003 | `docker-compose.yml` com 1 único gerador | ✅ Pass |
| V-004 | Schema com PK `int` + campos novos | ✅ Pass |
| V-006 | Streams aposentados (`mssql/users`, `mongodb/users/`, `postgres/drivers/`) removidos do config | ✅ Pass — 0 ocorrências |
| — | Nenhum script Silver/Gold restante referencia `silver_drivers_profile`/`silver_drivers_performance` | ✅ Pass |

## Verificação de integração — PENDENTE (requer ambiente rodando)

Não tenho acesso para regenerar dados nem executar o pipeline Databricks a partir desta sessão. Passos manuais necessários, **nesta ordem**:

1. **Recriar o volume Postgres** (a migração de PK só se aplica em volume novo — `sql/*.sql` só roda no `docker-entrypoint-initdb.d` na primeira criação do volume):
   ```powershell
   docker-compose down -v
   ```
2. **Subir infraestrutura + gerador unificado:**
   ```powershell
   .\scripts\start-all.ps1
   ```
3. **Confirmar que só existe 1 container gerador** (`docker ps` deve mostrar `gen-unified`, não mais 3 containers `gen-*`).
4. **Verificar PK sequencial:**
   ```sql
   SELECT user_id FROM users LIMIT 5;   -- deve ser inteiro, não UUID
   SELECT driver_id FROM drivers LIMIT 5;
   ```
5. **Rodar pipeline Databricks completo** (Bronze → Silver → Gold).
6. **Joins de validação (Gold/Silver):**

| ID | Query | Esperado |
|----|-------|----------|
| V-005a | `SELECT COUNT(*) FROM silver_kafka_orders o LEFT JOIN silver_postgres_users u ON o.id_usuario=u.id_usuario WHERE u.id_usuario IS NULL` | 0 |
| V-005b | `SELECT COUNT(*) FROM silver_kafka_orders o LEFT JOIN silver_drivers d ON o.id_motorista=d.id_motorista WHERE d.id_motorista IS NULL` | 0 |
| V-007 | Comparar `end_lat/lon` de `silver_kafka_route` com `lat/lon` de `silver_postgres_users` | Correspondem a um usuário real |
| V-008 | `SHOW TABLES LIKE 'silver_drivers*'` | Só `silver_drivers` — não mais `silver_drivers_profile`/`silver_drivers_performance` |

**Risco técnico a observar:** o lookup cruzado Postgres↔MinIO (`connection: postgres` dentro de generators com `connection: minio`) está documentado oficialmente com um exemplo equivalente, mas **não foi testado neste projeto especificamente** — se a geração falhar, verificar a versão da imagem `shadowtraffic/shadowtraffic:latest` e os logs de `gen-unified`.

## Issues Encountered

Nenhum na parte de código/config. Os riscos técnicos (suporte real do ShadowTraffic à unificação; comportamento da migração de PK sobre volume existente) só são verificáveis rodando o ambiente de verdade.

## Pendências antes do commit

Conforme `.claude/skills/git-boas-praticas-versionamento/SKILL.md`, commit é proposto e aguarda confirmação. Sugestão de mensagem:

```text
feat(pipeline): unifica identidade de Usuário/Motorista entre Postgres e MinIO (Onda 2)

Consolida os 3 containers geradores (gen-drivers, gen-users, gen-minio) num
único processo ShadowTraffic com connections postgres+minio, permitindo
lookup cruzado real. Migra PK de Usuário/Motorista de UUID para int
sequencial; adiciona vehicle_make/model/year/license_number/city ao
Postgres real; aposenta mssql/users, mongodb/users, postgres/drivers do
MinIO; corrige destino da Entrega; reconcilia silver_drivers_profile e
silver_drivers_performance numa única tabela silver_drivers. Atualiza
docs/MODELO_CONCEITUAL_UBER_EATS.md com o estado final, sem pendências.
```

## Status: ⚠️ COMPLETE (código) — validação de integração pendente

**Não recomendo `/ship` ainda** — os Success Criteria do Define exigem confirmar 0 órfãos via join real no Gold e PK sequencial no Postgres, o que só o usuário pode executar (inclui recriar o volume Postgres, uma operação destrutiva que não executo sem autorização explícita). Após rodar os passos 1-6 acima, retomar com `/ship`.
