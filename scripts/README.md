# Scripts de Automacao - Uber Eats Data Pipeline

Esta pasta contem todos os scripts PowerShell para orquestracao da infraestrutura local (Docker).

---

## Indice de Scripts

### Scripts de Inicializacao

| Script | Descricao | Usa Licenca? |
|--------|-----------|--------------|
| `start-infra.ps1` | Sobe **apenas** Postgres + MinIO | Nao |
| `start-generators.ps1` | Sobe **apenas** ShadowTraffic | Sim |
| `start-all.ps1` | Sobe **tudo** (Infra + Geradores) | Sim |

### Scripts de Parada

| Script | Descricao | Remove Dados? |
|--------|-----------|---------------|
| `stop-infra.ps1` | Para **apenas** infra | Nao |
| `stop-generators.ps1` | Para **apenas** geradores | Nao |
| `stop-all.ps1` | Para **todos** os servicos | Nao |
| `reset-all.ps1` | **DESTRUTIVO**: Para tudo + deleta volumes | **SIM** |

---

## Quando Usar Cada Script

### `start-all.ps1` - Setup Completo
**Use quando:**
- Primeira execucao do projeto
- Precisa de dados sendo gerados continuamente
- Vai fazer uma demo/apresentacao

**Exemplo:**
```powershell
.\scripts\start-all.ps1
```

---

### `start-infra.ps1` - Apenas Infraestrutura
**Use quando:**
- Quer economizar licenca ShadowTraffic
- Desenvolvimento local (queries, pipelines)
- Ja tem dados suficientes para testes

**Exemplo:**
```powershell
.\scripts\start-infra.ps1
```

---

### `start-generators.ps1` - Apenas Geradores
**Use quando:**
- A infra **ja esta rodando** (`start-infra.ps1`)
- Precisa popular mais dados
- Quer ligar/desligar geradores sob demanda

**Exemplo:**
```powershell
# 1. Suba a infra primeiro
.\scripts\start-infra.ps1

# 2. Depois suba os geradores
.\scripts\start-generators.ps1
```

---

### `stop-generators.ps1` - Economizar Licenca
**Use quando:**
- Quer parar de gastar licenca ShadowTraffic
- Dados ja suficientes para testes
- Infra deve continuar rodando

**Exemplo:**
```powershell
.\scripts\stop-generators.ps1
```

---

### `stop-all.ps1` - Parar Tudo (Mantem Dados)
**Use quando:**
- Terminou o trabalho do dia
- Quer liberar recursos do Docker
- **NAO quer apagar dados**

**Exemplo:**
```powershell
.\scripts\stop-all.ps1
```

---

### `reset-all.ps1` - Reset Completo (DESTRUTIVO)
**Use quando:**
- Quer comecar do zero
- Testes exigem ambiente limpo
- Algo deu errado e precisa formatar

**Exemplo:**
```powershell
.\scripts\reset-all.ps1
```

**ATENCAO:**
- Para todos os containers
- **DELETA VOLUMES** permanentemente
- **APAGA TODOS OS DADOS** do Postgres e MinIO
- Remove arquivos `.json` gerados (secrets)

**Nao tem volta!** Use com cuidado.

---

## Matriz de Decisao Rapida

| Situacao | Script Recomendado |
|----------|-------------------|
| Primeira vez executando | `start-all.ps1` |
| Desenvolvimento local sem geradores | `start-infra.ps1` |
| Preciso de mais dados | `start-generators.ps1` |
| Economizar licenca | `stop-generators.ps1` |
| Terminar o dia | `stop-all.ps1` |
| Algo deu errado | `reset-all.ps1` -> `start-all.ps1` |

---

## Requisitos

- Windows 10/11
- Docker Desktop rodando
- PowerShell 5.1+ (ou pwsh 7+)
- Arquivo `gen/.env` configurado (veja `gen/.env.template`)

---

## Dicas

1. **Sempre verifique o status dos containers:**
   ```powershell
   docker-compose ps
   ```

2. **Monitore logs de um servico especifico:**
   ```powershell
   docker-compose logs -f postgres-ubereats
   docker-compose logs -f gen-drivers
   ```

3. **Verificar se geradores estao ativos:**
   ```powershell
   docker-compose logs --tail=20 gen-drivers gen-users gen-minio
   ```

4. **Licenca ShadowTraffic expirada?**
   - Renove em [shadowtraffic.io](https://shadowtraffic.io)
   - Atualize `gen/.env` com novas credenciais
   - Execute `.\scripts\reset-all.ps1` -> `.\scripts\start-all.ps1`

---

## Troubleshooting

### Erro: "License expired"
```powershell
# 1. Renove a licenca
# 2. Atualize gen/.env
# 3. Reinicie os geradores
.\scripts\stop-generators.ps1
.\scripts\start-generators.ps1
```

### Erro: "Port already in use"
```powershell
# Verifique se ha containers rodando
docker ps

# Para tudo e tente novamente
.\scripts\stop-all.ps1
.\scripts\start-all.ps1
```

### Containers "zumbis" (nao param)
```powershell
# Reset forcado resolve isso
.\scripts\reset-all.ps1
```

---

**Duvidas?** Consulte o `README.md` principal na raiz do projeto.


