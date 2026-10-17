---
domain: azure-adls-gen2
topic: hns-rbac-acl
---

# HNS, RBAC e ACL

## O que o namespace hierárquico (HNS) muda

| Sem HNS (Blob) | Com HNS (ADLS Gen2) |
|---|---|
| "pasta" = prefixo de nome | diretório é objeto real |
| rename de pasta = copiar + apagar cada blob | rename/delete de diretório **atômico** (O(1)) |
| só RBAC/SAS | RBAC **+ ACL POSIX** por arquivo/diretório |
| driver `wasbs://` | driver **ABFS** `abfss://` otimizado (Hadoop/Spark) |

Rename atômico é o que torna commit de jobs Spark/Hadoop seguro e rápido.

- HNS é definido **na criação** (`is_hns_enabled`); mudar no Terraform recria a conta.
  Migração in-place de conta existente existe pelo portal, mas é irreversível.
- Alguns recursos do Blob têm suporte parcial com HNS (ex.: certas features de
  versionamento/lifecycle) — conferir a matriz oficial antes de depender (**a validar**).

## Duas camadas de autorização

1. **RBAC (Azure)** — roles de dados no escopo conta/container:
   `Storage Blob Data Reader | Contributor | Owner`.
2. **ACL (POSIX)** — `r w x` para owner, owning group, usuários/grupos nomeados (por
   object ID do Entra), `other`, mais `mask` e ACL **default** (herdada por filhos novos).

### Ordem de avaliação

1. Se a identidade tem **role RBAC de dados** que concede a operação → **permitido**
   (ACL nem é consultada).
2. Senão, avalia a **ACL** do caminho.
3. Senão → negado.

Consequência: dar `Storage Blob Data Contributor` na **conta** anula qualquer restrição
por ACL. Para isolar zonas, o escopo do RBAC deve ser o **container**, e ACL serve para
granularidade abaixo disso (ex.: um SP só escreve em `bronze/vendas/`).

### ACL na prática

- Para ler `/silver/vendas/2026/arquivo.parquet` a identidade precisa de `--x`
  (execute) em **cada diretório pai** + `r--` no arquivo.
- ACL **default** só afeta itens criados **depois**; itens existentes exigem aplicação
  recursiva (`az storage fs access update-recursive`).
- Use **grupos** do Entra nas ACLs, não SPs individuais — evita reprocessar ACL ao
  trocar de identidade.
- Setar ACL exige `Storage Blob Data Owner` ou ser owner do item.

## Contributor ≠ acesso a dados

`Contributor`/`Owner` (ARM) gerencia a conta e, **com shared key habilitado**, pode
listar a account key — o que dá acesso total. Com `shared_access_key_enabled = false`,
só roles de dados (ou ACL) abrem os dados. Por isso o padrão desta KB é desligar shared
key.

## Identidades típicas no projeto

| Consumidor | Identidade | Escopo sugerido |
|---|---|---|
| Spark/Databricks (fora do Azure ou Free Edition) | Service Principal | Contributor em bronze/silver; Reader em gold, conforme o job |
| Kafka Connect / Event Hubs Capture | SP / MI do namespace | Contributor em bronze |
| Synapse (COPY INTO) | MI do workspace | Reader/Contributor em silver/gold |
| Stream Analytics (reference data/output) | MI do job | Reader no container de referência; Contributor no de saída |
| Humano (dev) | usuário Entra | Contributor temporário em lab |
