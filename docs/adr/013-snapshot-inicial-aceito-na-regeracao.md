# 013 — Snapshot inicial aceito na regeração (conectores depois da carga)

**Status:** Aceita  
**Data:** 2026-11-10  
**Autores:** time  
**Revisa:** a decisão 5 da F4.0 do [modelo físico](../../shared/docs/modelagem/04-modelo-fisico.md) ("conector registrado
depois do DDL e antes da carga, todo evento chega como `c`") e a ordem dos passos 4, 5, 10 e 11 da F5.3. Complementa a
[ADR 011](011-cdc-debezium-3-7-e-replica-set-no-mongodb.md)

---

## Contexto

A F5.3 mandava subir Redpanda e Kafka Connect e registrar os conectores **antes de qualquer carga**, para que todo evento
da regeração chegasse ao CDC como `c`, com `ts_ms` e posição de log reais, e para validar o `source.txId` de cada compra
em todos os tópicos.

Na execução apareceram duas forças contrárias:

1. **Memória.** A máquina de desenvolvimento roda a VM do Docker com ~7 GB e já passa de 90% de uso. Os três bancos usam
   ~2,8 GB; Redpanda e Kafka Connect somariam mais ~2,5 GB durante todo o histórico (~2 h) e a carga em lote.
2. **O caso de uso real.** O CDC costuma ser ligado num sistema que **já tem dados**; o snapshot inicial é o caminho normal,
   não uma exceção. A [ADR 012](012-captura-dedicada-ao-kappa-na-fase-1.md) já adota esse modelo para o Kappa (registra o
   conector na fase dele, com snapshot inicial das suas tabelas).

O contrato canônico da Bronze já trata `r` como `c` (F4.0), então o snapshot não quebra nenhum consumidor.

## Decisão

1. **A carga (cadastros, catálogo, perfis) e o histórico do simulador rodam com os conectores desligados.** Redpanda e Kafka
   Connect só sobem depois do gate da carga.
2. **Os conectores Postgres e Oracle são registrados depois**, com `snapshot.mode=initial`: o que já está no banco chega como
   `r` e, dali em diante, o log traz `c`, `u` e `d`.
3. **O simulador em tempo real roda depois dos conectores.** Só esse trecho gera eventos `c` com `source.txId` por compra.
4. **O gate da regeração se divide em dois.** A parte do banco (`python -m simulator.gate`, T1 a T19) roda antes dos
   conectores. A checagem "compra no CDC com o mesmo `source.txId` em todos os tópicos" roda depois, sobre uma janela ao
   vivo do simulador.
5. **Ordem de execução da F5.3:** 0, 1, 2, 3, 6, 7, 8, 10 (só o histórico), 11 (parte do banco), 4, 5, 10 (tempo real),
   11 (parte do CDC), 9, 12. Os números dos passos são mantidos.
6. **A Silver não usa o `ts_ms` de um `r` como hora de negócio.** Todas as linhas de um snapshot têm o `ts_ms` do momento do
   snapshot; a hora real de cada fato está nas colunas das tabelas.

## Alternativas consideradas

- **Manter a ordem original (conectores antes da carga).** Valida o CDC sobre o histórico inteiro, mas mantém Redpanda e
  Kafka Connect ligados durante a carga, o que a máquina não sustenta hoje. Rejeitada.
- **Reduzir o heap dos dois serviços e manter a ordem original.** Baixaria o custo para ~3 GB, mas deixaria o CDC lento
  durante a rajada do histórico e ainda disputaria memória com o ShadowTraffic e o simulador. Rejeitada.
- **Rodar a carga sem Kafka e nunca capturar o histórico.** Faria o Bronze começar sem as linhas existentes. Rejeitada:
  o snapshot inicial resolve exatamente isso.

## Consequências

**Positivas**

- O histórico e a carga em lote rodam com ~2,8 GB, sem Redpanda e sem Kafka Connect.
- O slot do Postgres não retém WAL durante o histórico; o risco do `max_slot_wal_keep_size=4GB` some nesse trecho.
- O fluxo fica igual ao de ligar o CDC num sistema com dados, que é o caso real e o do Kappa.

**Negativas**

- O histórico entra como `r`, todos com o mesmo `ts_ms`. Só o que o simulador gera depois dos conectores tem `ts_ms` e
  `source.txId` reais.
- O volume do histórico **não** é exercitado como fluxo de eventos; o comportamento do Debezium sob rajada só aparece na
  janela ao vivo.
- O snapshot do Oracle e do Postgres roda uma vez, com o histórico completo; leva mais tempo que um registro com tabelas
  vazias.

**Riscos**

- O Oracle gera archivelog sem consumidor enquanto não há conector. O volume é pequeno (só cadastros), mas conferir o tamanho
  de `$ORACLE_HOME/dbs/arch` antes do passo 5.
- Recriar o contêiner do Oracle com o conector registrado obriga a novo snapshot (já previsto na F5.10).

## Revisão

Esta ADR deve ser revisada se:

- o snapshot do histórico completo demorar ou pesar a ponto de inviabilizar o registro dos conectores;
- a máquina ganhar memória suficiente para manter o CDC ligado durante toda a carga;
- a Bronze passar a depender do `ts_ms` do evento para ordenar fatos do histórico.
