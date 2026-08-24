# 📖 Knowledge Base — Pipeline SQL (repositório)

> **Base de conhecimento de referência para pipelines PySpark + SQL Server.**  
> **Reuso em outro projeto:** hosts, portas, JDBC e nomes de servidor nos guias `patterns/` são **exemplos** — substitua pelos valores do **seu** ambiente. **Fonte de verdade recomendada:** copie [`docs/inventario-ambiente.md.example`](../../../docs/inventario-ambiente.md.example) para `docs/inventario-ambiente.md` (gitignored) e mantenha `CONTEXT.md` apontando para esse fluxo.

## Índice

| Arquivo | Descrição |
|---------|-----------|
| [01-architecture.md](01-architecture.md) | Arquitetura do projeto |
| [02-jobs-reference.md](02-jobs-reference.md) | Referência completa dos Jobs |
| [03-troubleshooting.md](03-troubleshooting.md) | Guia de resolução de problemas (inclui certificados SSL) |
| [04-execution-patterns.md](04-execution-patterns.md) | **🚀 Padrões de execução (inclui PRD)** |
| [05-sql-objects.md](05-sql-objects.md) | Objetos SQL necessários |
| [06-criacao-novo-pipeline.md](06-criacao-novo-pipeline.md) | **⭐ Guia para criar novo pipeline** |
| [07-portas-conexao-servidores.md](07-portas-conexao-servidores.md) | **🔌 Mapeamento de portas PRD** |
| [08-fallback-manual-script-completo.md](08-fallback-manual-script-completo.md) | **🛠️ Fallback Manual T-SQL (todos os jobs)** |
| [09-certificados-ssl.md](09-certificados-ssl.md) | **🔒 Problemas de certificados SSL/TLS (servidor)** |
| [10-ssl-java-configuration.md](10-ssl-java-configuration.md) | **☕ Configuração Java para SSL (cliente)** |

## Uso

Esta KB é consultada quando perguntas envolvem **pipelines SQL**, jobs, execução e troubleshooting deste domínio; o agente primário é definido pelo roteador em `.cursor/commands/core/router.md`.

### Buscar na KB

```bash
grep -r "termo" .cursor/kb/sql-capacity/
```

## Estrutura

```
.cursor/kb/sql-capacity/
├── 00-index.md                           # Este arquivo
├── 01-architecture.md                    # Arquitetura
├── 02-jobs-reference.md                  # Referência de Jobs
├── 03-troubleshooting.md                 # Troubleshooting
├── 04-execution-patterns.md              # 🚀 Padrões de execução (inclui PRD)
├── 05-sql-objects.md                     # Objetos SQL
├── 06-criacao-novo-pipeline.md           # ⭐ Guia para criar novo pipeline
├── 07-portas-conexao-servidores.md       # 🔌 Mapeamento de portas PRD
└── 08-fallback-manual-script-completo.md # 🛠️ Fallback Manual T-SQL
```

