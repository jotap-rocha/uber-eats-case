# Scripts de Automação — Uber Eats Data Pipeline

Esta pasta contém todos os scripts PowerShell para orquestração da infraestrutura local (Docker).

---

## 📋 Índice de Scripts

### 🚀 Scripts de Inicialização

| Script | Descrição | Usa Licença? |
|--------|-----------|--------------|
| `start-all.ps1` | Sobe **tudo** (Infra + Geradores) | ✅ Sim |
| `start-infra.ps1` | Sobe **apenas** Postgres + MinIO | ❌ Não |
| `start-generators.ps1` | Sobe **apenas** ShadowTraffic | ✅ Sim |

### 🛑 Scripts de Parada

| Script | Descrição | Remove Dados? |
|--------|-----------|---------------|
| `stop-all.ps1` | Para **todos** os serviços | ❌ Não |
| `stop-infra.ps1` | Para **apenas** infra | ❌ Não |
| `stop-generators.ps1` | Para **apenas** geradores | ❌ Não |
| `reset-all.ps1` | **DESTRUTIVO**: Para tudo + deleta volumes | ✅ **SIM** |

---

## 🎯 Quando Usar Cada Script

### `start-all.ps1` — Setup Completo
**Use quando:**
- Primeira execução do projeto
- Precisa de dados sendo gerados continuamente
- Vai fazer uma demo/apresentação

**Exemplo:**
```powershell
.\scripts\start-all.ps1
```

---

### `start-infra.ps1` — Apenas Infraestrutura
**Use quando:**
- Quer economizar licença ShadowTraffic
- Desenvolvimento local (queries, pipelines)
- Já tem dados suficientes para testes

**Exemplo:**
```powershell
.\scripts\start-infra.ps1
```

**O que sobe:**
- ✅ PostgreSQL (porta 5432)
- ✅ MinIO (API: 9000 | Console: 9001)
- ✅ Bucket `uber-eats` criado automaticamente

**O que NÃO sobe:**
- ❌ Geradores ShadowTraffic

---

### `start-generators.ps1` — Apenas Geradores
**Use quando:**
- A infra **já está rodando** (`start-infra.ps1`)
- Precisa popular mais dados
- Quer ligar/desligar geradores sob demanda

**Exemplo:**
```powershell
# 1. Suba a infra primeiro
.\scripts\start-infra.ps1

# 2. Depois suba os geradores
.\scripts\start-generators.ps1
```

**Pré-requisito:** Postgres e MinIO devem estar rodando.

**O que sobe:**
- ✅ `gen-drivers` → Popula tabela `drivers`
- ✅ `gen-users` → Popula tabela `users`
- ✅ `gen-minio` → Gera eventos JSON no bucket `uber-eats`

---

### `stop-generators.ps1` — Economizar Licença
**Use quando:**
- Quer parar de gastar licença ShadowTraffic
- Dados já suficientes para testes
- Infra deve continuar rodando

**Exemplo:**
```powershell
.\scripts\stop-generators.ps1
```

**O que para:**
- ❌ Geradores ShadowTraffic

**O que permanece ativo:**
- ✅ PostgreSQL
- ✅ MinIO

---

### `stop-all.ps1` — Parar Tudo (Mantém Dados)
**Use quando:**
- Terminou o trabalho do dia
- Quer liberar recursos do Docker
- **NÃO quer apagar dados**

**Exemplo:**
```powershell
.\scripts\stop-all.ps1
```

**O que acontece:**
- Para todos os containers
- **Preserva volumes** (postgres_data, minio_data)
- Dados permanecem intactos

---

### `reset-all.ps1` — Reset Completo (DESTRUTIVO)
**Use quando:**
- Quer começar do zero
- Testes exigem ambiente limpo
- Algo deu errado e precisa formatar

**Exemplo:**
```powershell
.\scripts\reset-all.ps1
```

**⚠️ ATENÇÃO:**
- Para todos os containers
- **DELETA VOLUMES** permanentemente
- **APAGA TODOS OS DADOS** do Postgres e MinIO
- Remove arquivos `.json` gerados (secrets)

**Não tem volta!** Use com cuidado.

---

## 📊 Matriz de Decisão Rápida

| Situação | Script Recomendado |
|----------|-------------------|
| Primeira vez executando | `start-all.ps1` |
| Desenvolvimento local sem geradores | `start-infra.ps1` |
| Preciso de mais dados | `start-generators.ps1` |
| Economizar licença | `stop-generators.ps1` |
| Terminar o dia | `stop-all.ps1` |
| Algo deu errado | `reset-all.ps1` → `start-all.ps1` |

---

## 🔧 Requisitos

- Windows 10/11
- Docker Desktop rodando
- PowerShell 5.1+ (ou pwsh 7+)
- Arquivo `gen/.env` configurado (veja `gen/.env.template`)

---

## 💡 Dicas

1. **Sempre verifique o status dos containers:**
   ```powershell
   docker-compose ps
   ```

2. **Monitore logs de um serviço específico:**
   ```powershell
   docker-compose logs -f postgres-ubereats
   docker-compose logs -f gen-drivers
   ```

3. **Verificar se geradores estão ativos:**
   ```powershell
   docker-compose logs --tail=20 gen-drivers gen-users gen-minio
   ```

4. **Licença ShadowTraffic expirada?**
   - Renove em [shadowtraffic.io](https://shadowtraffic.io)
   - Atualize `gen/.env` com novas credenciais
   - Execute `.\scripts\reset-all.ps1` → `.\scripts\start-all.ps1`

---

## 🐛 Troubleshooting

### Erro: "License expired"
```powershell
# 1. Renove a licença
# 2. Atualize gen/.env
# 3. Reinicie os geradores
.\scripts\stop-generators.ps1
.\scripts\start-generators.ps1
```

### Erro: "Port already in use"
```powershell
# Verifique se há containers rodando
docker ps

# Para tudo e tente novamente
.\scripts\stop-all.ps1
.\scripts\start-all.ps1
```

### Containers "zumbis" (não param)
```powershell
# Reset forçado resolve isso
.\scripts\reset-all.ps1
```

---

**Dúvidas?** Consulte o `README.md` principal na raiz do projeto.

