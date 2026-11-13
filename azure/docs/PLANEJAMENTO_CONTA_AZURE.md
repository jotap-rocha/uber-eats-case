# Planejamento da conta Azure (Fase 1, Warehouse primeiro)

**Status:** rascunho para aprovação (2026-11-11). Nada foi aberto nem aplicado.  
**Base:** [roadmap v2.2](../../shared/docs/ROADMAP_ARQUITETURA_MULTICLOUD.md), Fase 1, e [ADR 012](../../docs/adr/012-captura-dedicada-ao-kappa-na-fase-1.md).

Regra do projeto: a conta só é aberta com **todos os itens da seção 3 prontos** e com o acompanhamento do agente. Antes de qualquer `terraform apply` que crie recurso pago, o agente mostra o `plan` e a estimativa de custo e espera o "ok".

## 1. O que a Fase 1 (Warehouse) precisa

| Recurso | Para quê | Custo contínuo? |
|---|---|---|
| Resource group | Agrupa e permite destruir tudo de uma vez | Não |
| Storage account ADLS Gen2 (hierarchical namespace) | Bronze: arquivos do Debezium e do Airbyte | Só pelo volume armazenado |
| Synapse workspace + **Dedicated SQL Pool** (DW100c) | Warehouse (`COPY INTO` + `MERGE` para o SCD2) | **Sim, por hora ligado** |
| Service principal de deploy | Terraform e CLI sem usar a conta pessoal | Não |
| Budget alert | Aviso de gasto na assinatura | Não |

**Fora da Fase 1-Warehouse (só nas fases deles):** Event Hubs e Stream Analytics (Kappa, ADR 012), credencial do Unity Catalog (Lakehouse).

## 2. Estimativa de custo (preços de tabela, USD, consultados na Azure Retail Prices API em 2026-11-11)

| Item | Região | Preço |
|---|---|---|
| Synapse Dedicated, DW100c | `eastus2` | **US$ 1,20/h** |
| Synapse Dedicated, DW100c | `eastus` e `southcentralus` | US$ 1,51/h |
| Synapse Dedicated, DW100c | `brazilsouth` | US$ 2,42/h |
| Armazenamento do pool Synapse | `eastus2` | US$ 23/TB-mês |
| ADLS Gen2, camada Hot LRS | `eastus2` | US$ 0,0184/GB-mês |
| ADLS Gen2, camada Hot LRS | `brazilsouth` | US$ 0,0326/GB-mês |
| Event Hubs Standard (só na fase do Kappa) | `eastus` | US$ 0,03/h por throughput unit + US$ 0,028 por milhão de eventos |

**Recomendação de região: `eastus2`.** É a mais barata para o Synapse (a `brazilsouth`, que é o padrão no Terraform atual, custa o dobro). Os dados são sintéticos, então residência de dados não pesa. Antes de fixar, conferir no portal se o Synapse Dedicated está disponível na assinatura nessa região (cota).

**Cenários para o DW100c em `eastus2` (US$ 1,20/h):**

| Uso | Horas | Custo |
|---|---|---|
| Uma sessão de 3 h (liga, trabalha, pausa) | 3 | US$ 3,60 |
| 8 sessões de 3 h (cerca de 2 meses no ritmo de 3 h por semana) | 24 | US$ 28,80 |
| Esquecido ligado 24 h por dia | 24 por dia | **US$ 28,80 por dia (US$ 864 por mês)** |

O terceiro cenário é o risco real: **pausar o pool ao fim de toda sessão** é a regra de custo mais importante da fase. Pausado, só cobra o armazenamento (pequeno).

**Volume de dados:** o histórico tem ~400 mil pedidos em 28 tabelas, algo da ordem de poucos GB. No ADLS isso custa centavos por mês; no pool, centavos de armazenamento. O custo da fase é praticamente só as horas do DW100c.

**Teto de referência:** cerca de R$ 200 (a confirmar ao abrir a conta). Convertido pela cotação do dia, esse teto cobre da ordem de 30 horas de DW100c em `eastus2` (supondo dólar entre R$ 5 e R$ 6; conferir a cotação), ou seja, cerca de 10 sessões de 3 h se o pool nunca ficar ligado fora delas. Não sobra muito: o orçamento é apertado e a rotina de pausa é obrigatória.

## 3. Pré-requisitos (todos prontos antes de abrir a conta)

**Decisões do usuário**
- [ ] Região: `eastus2` (recomendada) ou outra.
- [ ] Teto de gasto em R$ e o limite de alerta (sugestão: alertas em 50%, 80% e 100%).
- [ ] Tipo de conta: *free account* (crédito inicial com validade de 30 dias e limite de gasto automático) ou pay-as-you-go com budget. Conferir no cadastro o valor do crédito para o Brasil e quais serviços ele cobre (Synapse Dedicated e ADLS), porque não achei a lista oficial.
- [ ] Cartão de crédito (a conta exige) e telefone para verificação. Só uma conta com crédito por pessoa.

**Ferramentas locais**
- [ ] Azure CLI (`az`), Terraform, `sqlcmd` instalados e versão registrada.
- [ ] `az login` com MFA na conta nova.

**Antes do primeiro `apply`**
- [ ] Registrar os *resource providers* necessários (`Microsoft.Synapse`, `Microsoft.Storage`; `Microsoft.EventHub` e `Microsoft.StreamAnalytics` só na fase do Kappa).
- [ ] Criar o service principal de deploy com o papel mínimo no resource group (`Contributor`) e guardar o segredo fora do git (`.tfvars` e `.env` ignorados).
- [ ] Estado remoto do Terraform num storage account separado e barato (backend `azurerm`), com *lock*.
- [ ] Budget alert criado **primeiro** pelo Terraform (`azurerm_consumption_budget_subscription`), antes de qualquer recurso pago.
- [ ] Padrão de nomes e tags (`projeto=uber-eats`, `fase=1`, `ambiente=dsv`).
- [ ] Conectividade: o Debezium e o Airbyte locais gravam no ADLS por internet de saída (não precisa de VPN nem porta aberta na máquina local).

## 4. Terraform existente (`azure/infra/fase1-ingestao/`) precisa de ajuste

O que existe foi escrito para o desenho antigo (v1.9). Para o Warehouse:
- **Manter:** `resource_group.tf`, `storage_account.tf`, `synapse.tf` (DW100c), `service_principal.tf`.
- **Separar para a fase do Kappa:** `event_hubs.tf` e `stream_analytics.tf`.
- **Separar para a fase do Lakehouse:** `unity_catalog_credential.tf` e as variáveis do Databricks.
- **Remover:** as variáveis do Airbyte/Postgres para o Event Hubs (`postgres_replication_password`, `eventhub_namespace_connection_string`), que são do desenho superado.
- **Mudar:** `azure_location` de `brazilsouth` para a região decidida; adicionar o budget e o backend remoto.
- Estrutura sugerida: `azure/infra/warehouse/`, `azure/infra/kappa/`, `azure/infra/lakehouse/`, com módulos pequenos e `terraform destroy` independente por pasta.

## 5. Rotina de cada sessão com custo

1. Abrir a sessão: `az login` (se expirou), `terraform plan` e conferir o que sobe.
2. Ligar (*resume*) o pool só quando for usar.
3. Trabalhar.
4. **Pausar o pool** (ou destruir, se a sessão acabou de vez) e listar o que está rodando. O agente lembra e pergunta; nunca deixa passar em silêncio, e `destroy` e *pause* nunca são automáticos.

## 6. Ordem proposta e pontos abertos

1. Fechar as decisões da seção 3 (comigo).
2. Spike do sink Kafka Connect para o ADLS (só leitura de docs e teste local, **sem conta**).
3. Abrir a conta; budget e estado remoto primeiro.
4. Terraform do Warehouse (ADLS, Synapse, pool pausado).
5. Carregar o Bronze e rodar `COPY INTO` e `MERGE`.

Pontos que seguem abertos: o sink até o ADLS, o acesso do Databricks Free Edition ao ADLS (Lakehouse) e o problema de negócio do Kappa (ver roadmap, Fase 1).
