# Pipeline Databricks - Delta Live Tables (Lakeflow)

Scripts de processamento de dados para o Databricks Lakehouse utilizando Delta Live Tables (DLT) no Lakeflow.

---

## Visao Geral

Esta pasta contém os scripts Python/SQL que implementam a **Arquitetura Medalhão** no Databricks:

```
Bronze Layer → Silver Layer → Gold Layer
(Raw)         (Cleaned)       (Aggregated)
```

Os scripts serão anexados ao **Lakeflow (Delta Live Tables)** para criar pipelines de transformação com:
- **Auto Loader**: Ingestão incremental de dados
- **CDC (Change Data Capture)**: Captura de mudanças do PostgreSQL
- **Expectations**: Qualidade de dados
- **Unity Catalog**: Governança e linhagem

---

## Estrutura Planejada

```
pipeline/
├── bronze/
│   ├── bronze_drivers.py       # Ingestão de drivers (CDC)
│   ├── bronze_users.py         # Ingestão de users (CDC)
│   └── bronze_events.py        # Ingestão de eventos JSON (Auto Loader)
├── silver/
│   ├── silver_drivers.py       # Limpeza e transformação
│   ├── silver_users.py         # Limpeza e transformação
│   └── silver_orders.py        # Flatten de JSONs + enriquecimento
└── gold/
    ├── gold_kpis.py            # Métricas de negócio
    ├── gold_driver_stats.py    # Estatísticas de motoristas
    └── gold_user_behavior.py   # Comportamento de usuários
```

---

## Status

🚧 **Em desenvolvimento**

Os scripts serão desenvolvidos seguindo a documentação em:
- `.claude/kb/how_construct_dlt.md` - Tutorial DLT, CDC e Auto Loader
- `.claude/kb/project_architecture.md` - Arquitetura end-to-end

---

## Como Usar (Futuro)

### 1. Anexar Scripts no Lakeflow

1. Acesse o Databricks Workspace
2. Navegue até **Lakeflow (Delta Live Tables)**
3. Crie um novo pipeline
4. Anexe os scripts desta pasta
5. Configure:
   - **Target**: `main.uber_eats`
   - **Storage**: External Location no Unity Catalog
   - **Cluster**: Serverless (recomendado)

### 2. Executar Pipeline

```python
# Via Databricks CLI (futuro)
databricks pipelines create --settings pipeline-config.json
databricks pipelines start --pipeline-id <id>
```

---

## Referências

- Delta Live Tables: https://docs.databricks.com/delta-live-tables/
- Auto Loader: https://docs.databricks.com/ingestion/auto-loader/
- Unity Catalog: https://docs.databricks.com/data-governance/unity-catalog/
- Arquitetura Medalhão: https://www.databricks.com/glossary/medallion-architecture

---

## Proximos Passos

1. Desenvolver scripts Bronze (ingestão)
2. Desenvolver scripts Silver (transformação)
3. Desenvolver scripts Gold (agregação)
4. Criar configuração de pipeline (JSON)
5. Testar no Databricks Community
6. Documentar expectations e testes de qualidade

