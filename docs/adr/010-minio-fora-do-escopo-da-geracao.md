# 010 — MinIO fora do escopo da geração e do modelo

**Status:** Aceita  
**Data:** 2026-11-04  
**Autores:** time  
**Revisa:** a lista de fontes da Fase 0 (ADR 006) e o papel do ShadowTraffic na [ADR 009](009-simulador-cria-a-compra-numa-transacao.md) (decisão 2, `kafka/gps`)

---

## Contexto

O MinIO era o data lake local onde o ShadowTraffic gravava eventos em JSONL, no bucket `uber-eats`, com 8 prefixos que
simulavam origens (`kafka/`, `mysql/`, `mongodb/`). O Airbyte o copiava para o lake de cada nuvem e a notificação de bucket
alimentava o barramento do Kappa.

O [modelo lógico](../../shared/docs/modelagem/03-modelo-logico.md) já tinha tirado quatro desses arquivos (`kafka/shift`,
`kafka/route`, `mysql/ratings` e `mongodb/support`), que viraram tabelas no Postgres. Na F1 do modelo físico apareceu que outros
três (`mysql/menu`, `mongodb/recommendations`, `kafka/search`) não tinham destino, e o único que ficava, `kafka/gps`, não é
usado por nenhuma regra (RN-01 a RN-42):

| Arquivo | Situação |
|---|---|
| `mysql/menu` | Coberto pelo cardápio do perfil no MongoDB (`menu_items[].section`, RN-23) |
| `mongodb/recommendations`, `kafka/search` | Eventos de comportamento sem regra de negócio |
| `kafka/gps` | Rastreio sem regra que o consuma |

## Decisão

1. **O MinIO sai do escopo da Fase 0 por agora.** Nenhum arquivo do bucket faz parte do modelo nem da regeração. O
   ShadowTraffic fica só com os cadastros (Oracle e Postgres); o MongoDB passou a um seed em Python (adendo da ADR 009). Os 8 geradores com
   `connection: minio` saem do template na regeração.
2. **A lógica fica guardada** em [`shared/docs/minio/historico-geracao.md`](../../shared/docs/minio/historico-geracao.md):
   arquivos, campos, distribuições, formato e a ligação com o modelo novo, o suficiente para voltar a gerar no futuro.
3. **Nada é apagado agora.** O contêiner `minio-ubereats`, o volume `minio_data` e o código das trilhas de nuvem que lê o
   MinIO (Airbyte, notificação de bucket, pontes Lambda e Cloud Function, DataSync, Storage Transfer, Stream Analytics) ficam
   como estão. Cada trilha revê a sua parte quando a fase da nuvem for retomada. Apagar o volume continua exigindo
   confirmação (o MinIO segue tratado como produção).
4. **Fontes da Fase 0:** Postgres, Oracle e MongoDB. O Kappa passa a ler só os tópicos de CDC (Debezium) do Postgres e do
   Oracle.

## Alternativas consideradas

- **A. Manter só `kafka/gps`**, ligado a `delivery_id` (como previa a L1b, decisão 13). Mantém o MinIO vivo por um arquivo
  sem regra que o use, com o custo de operar mais uma fonte e mais um gerador. Descartada por agora.
- **B. Manter os três arquivos de comportamento** (busca, recomendação, GPS) para análise de funil e Kappa. Exige regras novas
  (`/grill-with-docs`) antes da regeração e atrasa o caminho físico → regeração → pipeline. Descartada por agora; é o ponto
  de partida se o MinIO voltar.

## Consequências

**Positivas**

- Uma fonte e uma ferramenta a menos na Fase 0 (sem Airbyte para MinIO); o template fica só com os cadastros.
- O modelo físico perde a parte de MinIO da F3, que fica só com o MongoDB.

**Negativas**

- O portfólio perde, por agora, dado semiestruturado em object storage e o caso "evento de arquivo" do Kappa.
- O código das trilhas de nuvem que lê o MinIO fica parado e desalinhado com o escopo até a fase ser retomada.
- Documentos antigos (roadmap, SDD das trilhas, KBs) ainda citam o MinIO como fonte; valem as decisões desta ADR.

## Gatilhos de revisão

- Uma regra de negócio nova que use busca, recomendação ou rastreio (por exemplo, prazo prometido calculado pelo GPS).
- A trilha Kappa de alguma nuvem precisar de uma fonte de eventos além do CDC.
