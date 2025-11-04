# Projeto Pipeline de Dados Uber Eats (Infra Local)

Este projeto simula a infraestrutura de dados local completa para a ingestão de dados do Uber Eats, usando Docker para orquestrar as fontes de dados e os geradores de dados do Shadow Traffic.

## 🚀 Infraestrutura (Tudo no Docker)
O `docker-compose.yml` gerencia:
* **`postgres-ubereats`**: Banco de dados PostgreSQL (Porta: 5432) para dados de `drivers` e `users`.
* **`minio-ubereats`**: Data Lake S3-compatível (API: 9000, Console: 9001) para dados de eventos (`uber-eats`).
* **`gen-drivers`**: Gerador do Shadow Traffic para a tabela `drivers`.
* **`gen-users`**: Gerador do Shadow Traffic para a tabela `users`.
* **`gen-minio`**: Gerador do Shadow Traffic para o bucket `uber-eats`.

## ⚙️ Painel de Controle (PowerShell)

Toda a automação é feita via scripts PowerShell na raiz do projeto.

### 1. Para Ligar a Fábrica de Dados
(Roda a infra e os geradores em background)
```powershell
.\start-all.ps1
