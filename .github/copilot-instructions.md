# Copilot Instructions for Uber Eats Data Pipeline

## Idioma / Language
**IMPORTANTE**: Sempre responda em **português brasileiro** (pt-BR). Todas as respostas, explicações e documentação devem ser em português.

## Architecture Overview

This is a **local data infrastructure simulation** for Uber Eats using Docker and ShadowTraffic generators. The system simulates a complete data ecosystem with multiple storage layers and realistic synthetic data flows.

### Core Components
- **PostgreSQL**: Structured data (`drivers`, `users` tables)  
- **MinIO**: S3-compatible data lake for event streams and JSON data
- **ShadowTraffic**: Synthetic data generators creating realistic business scenarios

## Key Workflows

### Environment Management
```powershell
.\start-all.ps1    # Start entire infrastructure (containers + generators)
.\stop-all.ps1     # Stop containers, preserve data volumes  
.\reset-all.ps1    # DESTRUCTIVE: Remove all data and volumes
```

### Configuration Setup
1. Copy `gen/.env.template` to `gen/.env` with your ShadowTraffic license
2. Run `gen/setup-configs.ps1` to populate JSON configs from templates
3. Template replacement uses placeholder patterns like `REPLACE_WITH_POSTGRES_HOST`

### Data Generation Pattern
Each generator targets specific storage:
- `gen-drivers` → PostgreSQL `drivers` table via `gen/postgres/drivers.json`
- `gen-users` → PostgreSQL `users` table via `gen/postgres/users.json`  
- `gen-minio` → MinIO bucket `uber-eats` via `gen/minio/uber-eats.json`

## Project-Specific Conventions

### ShadowTraffic Configuration Structure
- **Templates** (`.json.template`): Contain placeholder strings for credentials
- **Generated configs** (`.json`): Real configs with credentials injected, git-ignored
- **Lookups**: Data generators reference other datasets using `_gen: "lookup"` patterns
- **State machines**: Complex workflows like order status transitions use `stateMachine` generators

### Data Relationships
The `gen/minio/uber-eats.json.template` shows sophisticated cross-dataset relationships:
- Orders reference users via CPF lookup
- Payments fork from orders creating event streams  
- GPS data generates tracking points for delivery routes
- State machines model realistic business process flows

### Container Dependencies
- Generators depend on storage services (`depends_on` in docker-compose)
- MinIO generators require AWS-style environment variables for S3 compatibility
- PostgreSQL uses logical replication settings (`wal_level=logical`) for CDC scenarios

## Development Patterns

### File Organization
- `sql/`: Database schema definitions
- `gen/`: All ShadowTraffic configuration and templates
- Root scripts: PowerShell automation for Windows environment

### Credential Management
- Never commit `.env` files or generated `.json` configs
- Use template pattern with `REPLACE_WITH_*` placeholders
- Setup script handles credential injection across multiple config files

### Data Volume Strategy
- Named Docker volumes (`postgres_data`, `minio_data`) persist between runs
- `stop-all.ps1` preserves data, `reset-all.ps1` destroys everything
- Volume persistence enables incremental data generation testing

## Common Tasks

### Adding New Data Sources
1. Create template in `gen/{database}/new-source.json.template`
2. Add placeholder replacement logic to `setup-configs.ps1`  
3. Add new generator service to `docker-compose.yml`
4. Update environment variables in template if needed

### Debugging Data Generation
- Check container logs: `docker-compose logs gen-{service}`
- Verify MinIO data via web console: http://localhost:9001
- Connect to PostgreSQL: `localhost:5432` with credentials from docker-compose

### Extending ShadowTraffic Configs  
- Use `fork` for one-to-many relationships (orders → order items)
- Leverage `lookup` to maintain referential integrity across datasets
- Apply `stateMachine` for realistic business process modeling
- Use `vars` for calculated fields and complex expressions

## Padrões de Commit

Utilize **sempre** os seguintes padrões para mensagens de commit:

| Tipo     | Descrição                                                    | Exemplo                                              |
|----------|--------------------------------------------------------------|------------------------------------------------------|
| `feat`   | Adição de nova funcionalidade                                | `feat: added support for automatic backup`           |
| `fix`    | Correção de bug                                              | `fix: adjusted data normalization`                   |
| `revert` | Reversão de alteração anterior                               | `revert: reverted change to the bank schema`         |
| `delete` | Remoção de código, arquivo ou recurso                        | `delete: removed table [old_logs]`                   |
| `update` | Atualização de código existente (melhoria, ajuste, refatoração leve) | `update: updated database structure`        |
| `config` | Alteração de configuração ou ambiente (.env, CI/CD, etc.)    | `config: adjusted database connection in .env`       |
| `ci`     | Ajustes no pipeline de integração contínua                   | `ci: added migration step in the pipeline`           |
| `docs`   | Alterações na documentação                                   | `docs: documented table structure`                   |
| `test`   | Adição ou ajuste de testes automatizados                     | `test: added tests for ETL functions`                |

This project demonstrates production-like data engineering patterns with synthetic data, making it ideal for testing ETL pipelines, analytics, and data integration scenarios without real customer data.