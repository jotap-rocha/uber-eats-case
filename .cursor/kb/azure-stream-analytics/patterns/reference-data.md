---
domain: azure-stream-analytics
topic: reference-data
---

# Pattern — reference-data (lookup em ADLS/Blob com `{date}/{time}`)

Reference data = dataset finito, estático ou que muda devagar (cadastro de lojas,
produtos, sensores), carregado **em memória** pelo job para enriquecer o stream.
Fontes suportadas: **Blob Storage, ADLS Gen2, Azure SQL Database**.

## 1. Regras do blob (o que mais quebra em produção)

| Regra | Consequência se ignorar |
|---|---|
| Blobs de reference são **imutáveis** — nunca sobrescrever | job não percebe a mudança |
| Nova versão = **novo blob** com `{date}/{time}` **maior** que o último | blob "no passado" é ignorado para sempre |
| Ordem vem do **nome** (`{date}/{time}`), não do Last Modified | upload atrasado com nome antigo não vale |
| Job só procura o blob quando o relógio alcança o `{date}/{time}` do nome | publicar **antes** do horário efetivo |
| Varredura a cada ~1 minuto | pequena latência na troca |
| No start, usa o blob mais recente **≤ start time** | sem blob → "Initializing input without a valid reference data blob" |
| Path sem blob → job espera indefinidamente | conferir path antes do start |
| Só CSV/JSON, UTF-8, **sem compressão** | `.csv.gz` não carrega |

## 2. Layout no lake

Container dedicado `reference` (ver KB `azure-adls-gen2`, `zone-layout`):

```
reference/lojas/2026-10-16/06-00/lojas.csv
reference/lojas/2026-10-16/18-00/lojas.csv
reference/lojas/2026-10-17/06-00/lojas.csv
```

Path pattern: `lojas/{date}/{time}/lojas.csv` · date `yyyy-MM-dd` · time `HH-mm`.

Reference estática (nunca muda): path fixo `lojas/lojas.csv`, sem tokens — e ainda
assim nunca sobrescrever; mudar = trocar o path no input (com job parado).

## 3. Terraform (Managed Identity)

```hcl
resource "azurerm_stream_analytics_job" "job" {
  name                = "<JOB>"
  resource_group_name = azurerm_resource_group.base.name
  location            = azurerm_resource_group.base.location
  sku_name            = "StandardV2"
  streaming_units     = 3                        # 1/3 SU V2 (a validar)
  compatibility_level = "1.2"
  identity { type = "SystemAssigned" }
  transformation_query = file("${path.module}/query.asaql")
}

resource "azurerm_role_assignment" "asa_ref_reader" {
  scope                = "${azurerm_storage_account.lake.id}/blobServices/default/containers/reference"
  role_definition_name = "Storage Blob Data Reader"
  principal_id         = azurerm_stream_analytics_job.job.identity[0].principal_id
}

resource "azurerm_stream_analytics_reference_input_blob" "lojas" {
  name                      = "ref-lojas"          # alias usado na query
  stream_analytics_job_name = azurerm_stream_analytics_job.job.name
  resource_group_name       = azurerm_resource_group.base.name
  storage_account_name      = azurerm_storage_account.lake.name
  storage_container_name    = "reference"
  path_pattern              = "lojas/{date}/{time}/lojas.csv"
  date_format               = "yyyy-MM-dd"
  time_format               = "HH-mm"
  authentication_mode       = "Msi"              # sem storage_account_key
  serialization {
    type            = "Csv"
    encoding        = "UTF8"
    field_delimiter = ","
  }
}
```

Valores aceitos de `time_format` no provider (`HH`, `HH-mm`, `HH/mm`…) — **a validar**
no `plan`; o portal lista os formatos suportados.

## 4. Query

```sql
WITH enriquecido AS (
    SELECT p.pedido_id, p.loja_id, p.valor, p.criado_em,
           r.regiao, r.formato
    FROM [pedidos-eh] p TIMESTAMP BY p.criado_em
    LEFT OUTER JOIN [ref-lojas] r          -- LEFT: loja nova ainda sem reference não some
      ON p.loja_id = r.loja_id
)
SELECT regiao, COUNT(*) AS pedidos, SUM(valor) AS receita,
       System.Timestamp() AS janela_fim
INTO [saida-adls]
FROM enriquecido
GROUP BY regiao, TumblingWindow(minute, 5)
```

- Reference join **não** usa `DATEDIFF`.
- Tipos do CSV chegam como string: `CAST(r.loja_id AS bigint)` se o stream for numérico
  (ou garantir mesmo tipo dos dois lados).
- Várias references: uma por etapa `WITH` (join reference × reference não é permitido).

## 5. Publicar nova versão (job batch)

```bash
TS_DATE=$(date -u +%Y-%m-%d); TS_TIME=$(date -u -d '+5 min' +%H-%M)   # efetivo daqui a 5 min (GNU date)
az storage blob upload --account-name <STORAGE_ACCOUNT> --auth-mode login \
  -c reference -n "lojas/${TS_DATE}/${TS_TIME}/lojas.csv" -f ./lojas.csv
```

- Publicar com horário efetivo um pouco **no futuro** dá tempo de o job descobrir e
  carregar antes de valer.
- `TS_TIME` precisa casar com o `time_format` do input (granularidade de minuto aqui).
- Orquestração recorrente: Data Factory / pipeline Synapse / Airflow gerando o blob.
- Apagar versões antigas que não serão mais reprocessadas (evita listar muitos blobs),
  mantendo as necessárias para restart/reprocesso.

## 6. Tamanho e memória

| SU (escala V1) | Reference recomendada |
|---|---|
| 1 | ≤ 50 MB |
| 3 | ≤ 150 MB |
| 6+ | ≤ 5 GB |

Em SU V2: 1 SU V2 ≈ 6 SU V1 (mapeamento de tamanho por V2 **a validar**). Ideal < 300 MB;
acima disso usar **SQL Database** com *delta query*. Cada reference join mantém uma cópia
em memória (× partições com `PARTITION BY`) — observar SU%.

## 7. Diagnóstico

- Logs de diagnóstico do job: `Loaded new reference data from <blob path>` confirma troca.
- Activity/diagnostic log com "Initializing input without a valid reference data blob"
  → nenhum blob ≤ start time.
- Teste da query no portal com amostra da reference antes de iniciar (sem custo de SU
  contínuo).

## Checklist

- [ ] Container `reference` com MI do job como `Storage Blob Data Reader`
- [ ] Path pattern + date/time format idênticos ao nome gerado pelo job batch
- [ ] Nenhum overwrite; nova versão sempre com `{date}/{time}` maior
- [ ] Blob inicial existe antes do primeiro start
- [ ] `LEFT OUTER JOIN` quando chave pode faltar na reference
- [ ] Job parado ao fim da sessão (`az stream-analytics job stop`)
