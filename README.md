# 🚀 Pipeline de Dados Uber Eats - Infraestrutura Local# Projeto Pipeline de Dados Uber Eats (Infra Local)



Simulação completa de infraestrutura de dados para o ecossistema Uber Eats, utilizando Docker para orquestração e **ShadowTraffic** para geração de dados sintéticos realistas.Este projeto simula a infraestrutura de dados local completa para a ingestão de dados do Uber Eats, usando Docker para orquestrar as fontes de dados e os geradores de dados do Shadow Traffic.



## 📋 Pré-requisitos## 🚀 Infraestrutura (Tudo no Docker)

O `docker-compose.yml` gerencia:

Antes de iniciar, certifique-se de ter instalado em sua máquina:* **`postgres-ubereats`**: Banco de dados PostgreSQL (Porta: 5432) para dados de `drivers` e `users`.

* **`minio-ubereats`**: Data Lake S3-compatível (API: 9000, Console: 9001) para dados de eventos (`uber-eats`).

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** (v20.10 ou superior)* **`gen-drivers`**: Gerador do Shadow Traffic para a tabela `drivers`.

- **PowerShell** (já incluso no Windows)* **`gen-users`**: Gerador do Shadow Traffic para a tabela `users`.

- **Licença ShadowTraffic** (necessária para os geradores de dados)* **`gen-minio`**: Gerador do Shadow Traffic para o bucket `uber-eats`.



## 🏗️ Arquitetura da Solução## ⚙️ Painel de Controle (PowerShell)



O projeto simula um ambiente de produção com múltiplas camadas de armazenamento:Toda a automação é feita via scripts PowerShell na raiz do projeto.



### Componentes da Infraestrutura### 1. Para Ligar a Fábrica de Dados

(Roda a infra e os geradores em background)

| Componente | Tecnologia | Porta | Descrição |```powershell

|------------|------------|-------|-----------|.\start-all.ps1

| **PostgreSQL** | `postgres:15` | 5432 | Banco relacional com tabelas `drivers` e `users` |
| **MinIO** | `minio/minio` | 9000 (API)<br>9001 (Console) | Data Lake S3-compatível para eventos |
| **ShadowTraffic Generators** | `shadowtraffic/shadowtraffic` | - | 3 geradores de dados sintéticos |

### Fluxo de Dados

```
ShadowTraffic Generators
    ├─► PostgreSQL (drivers, users)
    └─► MinIO S3 (orders, payments, GPS, events...)
```

## ⚙️ Configuração Inicial

### 1️⃣ Configure as Credenciais

Crie o arquivo de ambiente com suas credenciais:

```powershell
# Navegue até a pasta gen/
cd gen

# Copie o template
copy .env.template .env
```

### 2️⃣ Preencha o arquivo `.env`

Edite o arquivo `gen/.env` com suas credenciais:

```bash
# ShadowTraffic License (obrigatório)
LICENSE_ID=your-license-id
LICENSE_EMAIL=your-email@example.com
LICENSE_ORGANIZATION=your-org
LICENSE_EDITION=your-edition
LICENSE_EXPIRATION=yyyy-mm-dd
LICENSE_SIGNATURE=your-signature

# PostgreSQL (preenchido automaticamente)
POSTGRES_HOST=postgres-ubereats
POSTGRES_PORT=5432
POSTGRES_DB=ubereats_db
POSTGRES_USERNAME=usrUberEats
POSTGRES_PASSWORD=supersecret

# MinIO (preenchido automaticamente)
AWS_REGION=us-east-1
AWS_S3_FORCE_PATH_STYLE=true
AWS_ACCESS_KEY_ID=usrUberEats
AWS_SECRET_ACCESS_KEY=supersecret
```

> ⚠️ **Importante**: Apenas os campos de licença do ShadowTraffic precisam ser preenchidos manualmente. As credenciais de PostgreSQL e MinIO já estão configuradas para o ambiente local.

### 3️⃣ Retorne para a raiz do projeto

```powershell
cd ..
```

## 🚀 Executando o Ambiente

### Iniciar o Ambiente Completo

Execute o script que configura e inicia toda a infraestrutura:

```powershell
.\start-all.ps1
```

Este comando irá:
1. ✅ Injetar as credenciais do `.env` nos arquivos de configuração JSON
2. ✅ Iniciar PostgreSQL com tabelas criadas automaticamente
3. ✅ Iniciar MinIO com bucket `uber-eats` criado automaticamente
4. ✅ Iniciar os 3 geradores ShadowTraffic em paralelo

### Parar o Ambiente (Preservar Dados)

```powershell
.\stop-all.ps1
```

Os volumes Docker (`postgres_data`, `minio_data`) serão preservados.

### Resetar o Ambiente (Destruir Dados)

```powershell
.\reset-all.ps1
```

> ⚠️ **ATENÇÃO**: Este comando remove **TODOS** os volumes e dados gerados.

## 🔍 Acessando os Serviços

### PostgreSQL

```bash
Host: localhost
Port: 5432
Database: ubereats_db
Username: usrUberEats
Password: supersecret
```

**Tabelas disponíveis:**
- `public.drivers` - Dados dos motoristas
- `public.users` - Dados dos usuários

### MinIO Console (Interface Web)

Acesse: **http://localhost:9001**

```
Username: usrUberEats
Password: supersecret
```

**Bucket:** `uber-eats`

**Prefixos de dados:**
- `mssql/users/` - Dados de usuários (MSSQL)
- `mongodb/users/` - Dados complementares de usuários
- `postgres/drivers/` - Dados de motoristas
- `kafka/orders/` - Pedidos
- `kafka/payments/` - Pagamentos
- `kafka/status/` - Estados dos pedidos
- `kafka/gps/` - Rastreamento GPS
- `mysql/restaurants/` - Restaurantes
- `mysql/products/` - Produtos
- E muito mais...

## 📊 Estrutura do Projeto

```
uber-eats-case/
├── gen/                          # Configurações dos geradores
│   ├── .env                      # Credenciais (NÃO VERSIONAR)
│   ├── .env.template             # Template de credenciais
│   ├── setup-configs.ps1         # Script de injeção de segredos
│   ├── postgres/                 # Geradores PostgreSQL
│   │   ├── drivers.json.template
│   │   └── users.json.template
│   └── minio/                    # Geradores MinIO/S3
│       └── uber-eats.json.template
├── sql/                          # Scripts SQL
│   ├── create_drivers_table.sql
│   ├── create_users_table.sql
│   └── database-cdc-config.sql
├── docker-compose.yml            # Orquestração completa
├── start-all.ps1                 # Inicia tudo
├── stop-all.ps1                  # Para os containers
└── reset-all.ps1                 # Reseta o ambiente
```

## 🛠️ Geradores de Dados ShadowTraffic

### Características dos Dados Sintéticos

- **Localização**: Dados brasileiros (CPF, CNPJ, endereços, telefones)
- **Relacionamentos**: Lookups entre datasets (pedidos → usuários → pagamentos)
- **State Machines**: Ciclo de vida de pedidos realista
- **GPS Tracking**: Simulação de rotas de entrega com coordenadas
- **Event Streams**: Eventos de pagamento com fork de estados

### Configurações

Os geradores usam templates JSON que são processados pelo `setup-configs.ps1`:
- **Templates** (`.json.template`): Contêm placeholders para credenciais
- **Configs gerados** (`.json`): Arquivos finais com credenciais injetadas (git-ignored)

## 📝 Padrões de Commit

Este projeto utiliza commits semânticos:

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| `feat` | Nova funcionalidade | `feat: added order tracking generator` |
| `fix` | Correção de bug | `fix: adjusted timestamp format in orders` |
| `config` | Alteração de configuração | `config: updated MinIO credentials` |
| `docs` | Documentação | `docs: updated setup instructions` |
| `delete` | Remoção de código | `delete: removed deprecated tables` |

## 🆘 Troubleshooting

### Erro: "Docker not found"
- Verifique se o Docker Desktop está instalado e em execução

### Erro: "License validation failed"
- Confirme se as credenciais do ShadowTraffic no `.env` estão corretas

### Erro: "Port already in use"
- Verifique se as portas 5432, 9000 e 9001 estão livres
- Use `docker ps` para verificar containers em execução

### Dados não estão sendo gerados
- Execute `docker-compose logs gen-drivers` para verificar logs
- Confirme se o arquivo `gen/.env` foi criado corretamente

## 📄 Licença

Este projeto está sob a licença especificada no arquivo [LICENSE](./LICENSE).

---

**Desenvolvido para simulação de ambientes de Data Engineering** 🚀
