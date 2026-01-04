# Documentacao Completa - Uber Eats Data Pipeline

Este diretorio contem toda a documentacao tecnica e guias de provisionamento do projeto **Uber Eats Data Pipeline**.

---

## Indice de Documentacao

### Componentes da Infraestrutura

| Componente | Descricao | Documentacao |
|------------|-----------|--------------|
| **PostgreSQL** | Banco OLTP para dados transacionais | [postgres/README.md](postgres/README.md) |
| **MinIO** | Data Lake S3-compatible para eventos | [minio/README.md](minio/README.md) |
| **ShadowTraffic** | Gerador de dados sinteticos | [shadowtraffic/README.md](shadowtraffic/README.md) |
| **Airbyte** | Ferramenta de ingestao de dados | [airbyte/README.md](airbyte/README.md) |
| **Automacao** | Scripts PowerShell e Docker Compose | [automacao/README.md](automacao/README.md) |

---

## Ordem de Leitura

1. **[automacao/README.md](automacao/README.md)** - Scripts e Docker Compose
2. **[postgres/README.md](postgres/README.md)** - PostgreSQL
3. **[minio/README.md](minio/README.md)** - MinIO (Data Lake)
4. **[shadowtraffic/README.md](shadowtraffic/README.md)** - Geradores de dados
5. **[airbyte/README.md](airbyte/README.md)** - Ingestao de dados

---

## Inicio Rapido

```powershell
# 1. Clone o repositorio
git clone https://github.com/jotap-rocha/uber-eats-case.git
cd uber-eats-case

# 2. Configure credenciais
copy gen\.env.template gen\.env
notepad gen\.env

# 3. Inicie a infraestrutura
.\scripts\start-all.ps1

# 4. Verifique o status
docker-compose ps
```

---

## Links

- Repositorio: https://github.com/jotap-rocha/uber-eats-case
- ShadowTraffic: https://shadowtraffic.io
- Airbyte: https://airbyte.com
- Databricks: https://community.cloud.databricks.com
- MinIO: https://min.io/docs

