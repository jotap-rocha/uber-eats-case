---
domain: azure-synapse
topic: dedicated-pool
---

# Dedicated SQL Pool — arquitetura que afeta o código

## Workspace vs "formerly SQL DW"

| Variante | Como reconhecer | Impacto |
|---|---|---|
| Dedicated pool **em Synapse workspace** | criado via `azurerm_synapse_sql_pool` / `az synapse sql pool` | padrão desta KB |
| Dedicated pool (formerly SQL DW) | servidor lógico SQL, `azurerm_mssql_database` com SKU DW | cmdlets/CLI diferentes; MSI precisa de ACL no lake |

## MPP: 60 distribuições

Toda tabela é fatiada em 60 distribuições. O nó de controle quebra a query; os nós de
compute (quantidade depende do DWU) processam as fatias. Movimento de dados entre
distribuições (*data movement*, `ShuffleMove`/`BroadcastMove`) é o custo dominante.

| Distribuição | Como espalha | Use para |
|---|---|---|
| `HASH(col)` | hash da coluna | fatos grandes; dimensões alvo de MERGE com INSERT |
| `ROUND_ROBIN` | rotativo | staging (carga mais rápida, join mais caro) |
| `REPLICATE` | cópia completa em cada nó | dimensões pequenas muito juntadas |

Escolha da coluna HASH: alta cardinalidade, distribuição uniforme, usada em join/MERGE,
**não** atualizada (atualizar chave de distribuição é caro e teve bug em builds antigos).

## Índices

| Tipo | Quando |
|---|---|
| Clustered Columnstore (CCI) — default | fatos e dimensões > ~60 M linhas; compressão e scan |
| `HEAP` | staging carregado e descartado |
| Clustered rowstore | dimensão pequena com lookup pontual |

CCI precisa de ~1 M linhas por rowgroup por distribuição para comprimir bem: com 60
distribuições, tabela < ~60 M linhas pode ficar melhor como HEAP/rowstore.

## DWU e recursos

- `DW100c` é o menor nível: 1 nó de compute para as 60 distribuições, pouca memória
  por query, **concorrência baixa** (poucas queries simultâneas) — ok para lab.
- Escalar: `az synapse sql pool update --performance-level DW200c` (desconecta sessões).
- Resource classes (`smallrc`, `largerc`, ...) e workload groups controlam memória por
  query; carga grande em DW100c pode precisar de `largerc` para o usuário de carga.

## O que muda em relação ao SQL Server

- Sem chaves estrangeiras impostas; `PRIMARY KEY`/`UNIQUE` só `NOT ENFORCED`.
- `IDENTITY` não garante valores contíguos nem ordem.
- `UPDATE ... FROM` com join tem restrições → MERGE é o caminho idiomático.
- `CTAS` (`CREATE TABLE AS SELECT`) é a forma mais rápida de reescrever tabelas e mudar
  distribuição.
- Estatísticas: `AUTO_CREATE_STATISTICS` ligado, mas `UPDATE STATISTICS` após carga
  grande evita plano ruim.

## Quando o pool está pausado

- Nenhuma conexão SQL funciona (erro de banco indisponível) — pipelines devem
  `resume` + aguardar `Online` antes de carregar.
- Resume leva minutos; dados e objetos são preservados.
- Pause/resume também aplica atualizações de build pendentes (útil para MERGE fixes).
