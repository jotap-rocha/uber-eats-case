# Automacao - Scripts e Docker Compose

Scripts PowerShell para gerenciar a infraestrutura local.

---

## Scripts Disponiveis

```
scripts/
├── start-all.ps1          # Inicia tudo (infra + geradores)
├── start-infra.ps1        # Apenas Postgres + MinIO
├── start-generators.ps1   # Apenas ShadowTraffic
├── stop-all.ps1          # Para tudo
├── stop-generators.ps1    # Para geradores
└── reset-all.ps1         # Reset DESTRUTIVO (apaga dados)
```

---

## Comandos Basicos

### Iniciar Ambiente

```powershell
# Tudo de uma vez
.\scripts\start-all.ps1

# Apenas infra (sem geradores)
.\scripts\start-infra.ps1
```

### Adicionar Geradores

```powershell
# Pre-requisito: infra rodando
.\scripts\start-generators.ps1
```

### Parar Ambiente

```powershell
# Para tudo (preserva dados)
.\scripts\stop-all.ps1

# Para apenas geradores
.\scripts\stop-generators.ps1
```

### Reset Completo

```powershell
# ⚠️ APAGA TODOS OS DADOS!
.\scripts\reset-all.ps1
```

---

## Verificar Status

```powershell
# Listar containers
docker-compose ps

# Ver logs
docker-compose logs -f postgres-ubereats
docker-compose logs -f gen-drivers

# Ver recursos
docker stats
```

---

## Servicos no Docker Compose

| Servico | Descricao | Porta |
|---------|-----------|-------|
| `postgres-ubereats` | PostgreSQL 15 | 5432 |
| `minio-ubereats` | MinIO (Data Lake) | 9000/9001 |
| `gen-drivers` | Gerador (drivers) | - |
| `gen-users` | Gerador (users) | - |
| `gen-minio` | Gerador (eventos) | - |

---

## Troubleshooting

### Script bloqueado (ExecutionPolicy)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Porta em uso

```powershell
netstat -ano | findstr "5432"
netstat -ano | findstr "9000"
```

### Containers nao param

```powershell
.\scripts\reset-all.ps1
```

---

## Links

- Docker Compose: https://docs.docker.com/compose/
- PowerShell: https://docs.microsoft.com/powershell/
