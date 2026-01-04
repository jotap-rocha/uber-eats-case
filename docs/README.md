# Documentacao Tecnica - Uber Eats Data Pipeline

Documentacao completa para provisionar o ambiente local.

---

## Componentes

| Componente | Documentacao | Descricao |
|------------|--------------|-----------|
| **Automacao** | [automacao/README.md](automacao/README.md) | Scripts PowerShell e Docker Compose |
| **PostgreSQL** | [postgres/README.md](postgres/README.md) | Banco OLTP (drivers, users) |
| **MinIO** | [minio/README.md](minio/README.md) | Data Lake S3 (eventos JSON) |
| **ShadowTraffic** | [shadowtraffic/README.md](shadowtraffic/README.md) | Gerador de dados sinteticos |
| **Airbyte** | [airbyte/README.md](airbyte/README.md) | Ferramenta de ingestao |

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

## Ordem de Leitura

1. [automacao/README.md](automacao/README.md) - Scripts e comandos basicos
2. [postgres/README.md](postgres/README.md) - Configurar PostgreSQL
3. [minio/README.md](minio/README.md) - Configurar MinIO
4. [shadowtraffic/README.md](shadowtraffic/README.md) - Gerar dados sinteticos
5. [airbyte/README.md](airbyte/README.md) - Configurar ingestao

---

## Links

- Repositorio: https://github.com/jotap-rocha/uber-eats-case
- ShadowTraffic: https://shadowtraffic.io
- Airbyte: https://airbyte.com
- Databricks: https://community.cloud.databricks.com
- MinIO: https://min.io/docs
