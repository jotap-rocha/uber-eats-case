# 011 — CDC na regeração: Debezium 3.7 e MongoDB em replica set

**Status:** Aceita  
**Data:** 2026-11-04  
**Autores:** time  
**Revisa:** a versão do Debezium do `docker-compose.yml` (3.0) e a decisão da Onda 3 "MongoDB sem CDC"
(`azure/docs/data-contract-cdc-azure.md`)

---

## Contexto

A fase F4 do [modelo físico](../../shared/docs/modelagem/04-modelo-fisico.md) fechou a captura das três fontes
regeneradas ([ADR 006](006-inversao-de-dominios-entre-oracle-e-postgres.md), decisão 4): Debezium no Postgres e no Oracle,
Airbyte no MongoDB. Duas escolhas de infraestrutura saíram dela e são caras de desfazer depois que os conectores
estiverem rodando:

1. **Versão do Debezium.** O projeto usa `quay.io/debezium/connect:3.0` e `debezium/server:3.0` (Docker Hub). O 3.0 é de
   2024, roda sobre Kafka Connect 3.x e não recebe mais correção (o projeto Debezium só corrige a série mais recente). O
   3.7 saiu no fim de setembro de 2026, sobre Kafka Connect 4.3, e as imagens novas só existem no `quay.io`. O `BOOLEAN`
   nativo do Oracle 23 segue sem suporte no 3.7, então esse não é o motivo da troca (o físico usa `NUMBER(1)` com o
   `NumberOneToBooleanConverter`).
2. **MongoDB sozinho.** O `mongo-ubereats` roda sem `--replSet`. O conector MongoDB do Airbyte exige replica set ou
   cluster shardado, **até para full refresh**: com o contêiner de hoje, nenhuma captura funciona.

A regeração recomeça os dois bancos relacionais do zero (ADR 006): não há offset, slot nem histórico de schema para
migrar. É o momento de menor custo para as duas mudanças.

## Decisão

1. **Debezium 3.7** em todo o projeto: `quay.io/debezium/connect:3.7` (`kafka-connect`, `kafka-connect-azure`) e
   `quay.io/debezium/server:3.7` (`debezium-server-postgres`, `debezium-server-oracle`), trocados na regeração.
2. **MongoDB em replica set de um nó** (`rs0`): `--replSet rs0 --bind_ip_all --oplogSizeMB 1024`, com `rs.initiate`
   idempotente no healthcheck (o entrypoint da imagem roda os scripts de init sem `--replSet`). Membro
   `mongo-ubereats:27017`; clientes fora da rede do compose usam `directConnection=true`.
3. **O Airbyte captura `restaurant_profiles` por change stream** (incremental CDC, modo *Lookup*), não por full refresh.
   O seed em Python ([ADR 009](009-simulador-cria-a-compra-numa-transacao.md), adendo) pode reescrever perfis, e o CDC
   entrega as mudanças e exclusões com `_ab_cdc_*`.

## Alternativas consideradas

- **Manter o 3.0.** Funciona com tudo o que a F4 precisa, mas fica numa série sem correções, e a troca futura exige
  testar compatibilidade de offsets e slots com dados em produção local. Descartada.
- **Debezium também no MongoDB** (no lugar do Airbyte). Poria o perfil no barramento, mas contraria a decisão 4 da
  ADR 006 sem ganho para uma coleção pequena. Descartada.
- **Replica set com full refresh no Airbyte.** O replica set é obrigatório de qualquer jeito; o full refresh releria a
  coleção inteira a cada sync e perderia as exclusões. Descartada.

## Consequências

**Positivas**

- Uma série do Debezium com suporte, testada na F4 contra o DDL da F1 e da F2 (3.7.0.Final).
- Imagens de uma origem só (`quay.io`).
- O MongoDB passa a ter histórico de mudança, como as outras fontes, e o contrato `cdc_*` cobre as três.

**Negativas**

- O `docker-compose.yml` muda em cinco serviços na regeração.
- Mais um processo de init no MongoDB (o `rs.initiate` no healthcheck) e o oplog ocupando até 1 GB na D:.
- Ligar autenticação no MongoDB depois passa a exigir `keyFile` (replica set com auth).

## Riscos

- Os nomes exatos dos metadados `_ab_cdc_*` do Airbyte para MongoDB ficam a confirmar na primeira sync.
- Kafka Connect 4.x remove APIs antigas: o `HdfsSinkConnector` da Fase 1 (Confluent) precisa ser conferido no worker 3.7
  antes da Fase 1.

## Gatilhos de revisão

- O Debezium lançar suporte ao `BOOLEAN` nativo do Oracle 23 (reabre a F2, decisão 2).
- O sink da Fase 1 não rodar no Kafka Connect 4.x.
- A captura do MongoDB passar para o barramento (Debezium ou Airbyte com destino Kafka).

## Impacto em SI/LGPD

Nenhum. Todo dado do projeto é sintético (ShadowTraffic e seed). As mudanças são de infraestrutura de captura e valem
na regeração; nenhuma operação destrutiva nos bancos atuais é concedida por esta ADR.

## Adendo (2026-11-04, implementação da F5.2)

O teste do init em contêiner descartável corrigiu dois pontos da decisão 2:

- A opção do oplog é **`--oplogSize 1024`** (MB). `--oplogSizeMB` não existe no `mongod` e impede o contêiner de subir.
- O entrypoint da imagem `mongo:7` só tira o `--replSet` do `mongod` temporário do init quando há usuário root
  (autenticação). Sem autenticação, o init roda em replica set não iniciado e nenhuma escrita passa. O `rs.initiate` vai
  para o próprio init (`shared/mongo/init/00_replica_set.js`, antes da coleção), com o membro **`localhost:27017`**, e o
  healthcheck só confere o primário. Clientes fora do compose continuam com `directConnection=true`.

Detalhe na F4.4 do [modelo físico](../../shared/docs/modelagem/04-modelo-fisico.md).
