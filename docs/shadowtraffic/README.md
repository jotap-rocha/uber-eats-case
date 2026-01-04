# ShadowTraffic - Documentacao Tecnica

Gerador de dados sinteticos para popular Postgres (drivers, users) e MinIO (~20 streams de eventos JSON).

---

## Especificacoes Tecnicas

| Item | Valor |
|------|-------|
| **Imagem Docker** | `shadowtraffic/shadowtraffic:latest` |
| **Containers** | 3 geradores independentes |
| **Licenca** | Free Trial (requer cadastro) |
| **Configuracao** | Arquivos JSON em `gen/` |

---

## Geradores Ativos

### 1. gen-drivers (Postgres)

**Tabela**: `drivers`  
**Configuracao**: `gen/postgres/drivers.json`  
**Taxa**: ~200 registros/segundo

**Campos gerados**:
- UUID como ID
- Nomes completos (Faker)
- Emails e telefones realistas
- Tipos de veiculos (Car, Motorcycle, Bicycle, Scooter)
- Placas de veiculo
- Datas de registro
- Total de entregas e ganhos
- Avaliacoes medias
- Status (Active, Inactive, Banned)

### 2. gen-users (Postgres)

**Tabela**: `users`  
**Configuracao**: `gen/postgres/users.json`  
**Taxa**: ~200 registros/segundo

**Campos gerados** (30+ campos):
- UUID como ID
- Nomes, usernames, emails
- Telefones e enderecos completos
- Localizacao geografica (lat/lon)
- Preferencias (idioma, timezone)
- Assinatura (Free, Basic, Premium)
- Historico de pedidos e gastos
- Metodos de pagamento
- Timestamps de criacao/atualizacao

### 3. gen-minio (MinIO/S3)

**Bucket**: `uber-eats`  
**Configuracao**: `gen/minio/uber-eats.json`  
**Streams**: 20 tipos de eventos  
**Taxa**: ~500 eventos/segundo (total)

**Tipos de eventos**:
1. **mssql/users/** - Usuarios (origem MSSQL)
2. **mongodb/users/** - Usuarios (origem MongoDB)
3. **postgres/drivers/** - Motoristas
4. **kafka/orders/** - Pedidos
5. **kafka/payments/** - Pagamentos
6. **kafka/events/** - Eventos de pagamento (state machine)
7. **kafka/route/** - Rotas de entrega
8. **kafka/gps/** - GPS tracking (20 pontos por rota)
9. **kafka/status/** - Status dos pedidos (8 estados)
10. **kafka/shift/** - Turnos dos motoristas
11. **kafka/receipts/** - Recibos
12. **kafka/search/** - Buscas de usuarios
13. **mysql/restaurants/** - Restaurantes
14. **mysql/products/** - Produtos do menu
15. **mysql/ratings/** - Avaliacoes
16. **mysql/menu/** - Secoes do menu
17. **postgres/inventory/** - Estoque
18. **mongodb/items/** - Itens dos pedidos (10k forks)
19. **mongodb/recommendations/** - Recomendacoes
20. **mongodb/support/** - Tickets de suporte

---

## Configuracao

### Arquivos de Configuracao

```
gen/
├── .env                    # Credenciais (NUNCA commite!)
├── .env.template           # Template para copiar
├── setup-configs.ps1       # Script de injecao de secrets
├── postgres/
│   ├── drivers.json.template    # Template (com placeholders)
│   ├── users.json.template      # Template (com placeholders)
│   ├── drivers.json             # Gerado (com secrets)
│   └── users.json               # Gerado (com secrets)
└── minio/
    └── uber-eats.json      # Config do MinIO (sem secrets)
```

### Arquivo .env

Crie o arquivo `gen/.env` a partir do template:

```powershell
copy gen\.env.template gen\.env
notepad gen\.env
```

**Variaveis obrigatorias**:

```ini
# PostgreSQL
POSTGRES_HOST=postgres-ubereats
POSTGRES_PORT=5432
POSTGRES_DB=ubereats_db
POSTGRES_USERNAME=usrUberEats
POSTGRES_PASSWORD=supersecret

# MinIO/S3
AWS_REGION=us-east-1
AWS_S3_FORCE_PATH_STYLE=true
AWS_ACCESS_KEY_ID=usrUberEats
AWS_SECRET_ACCESS_KEY=supersecret

# ShadowTraffic License (obtenha em https://shadowtraffic.io)
LICENSE_ID=seu-license-id
LICENSE_KEY=sua-license-key
LICENSE_EMAIL=seu-email@example.com
LICENSE_OWNER=Seu Nome
```

### Obter Licenca ShadowTraffic

1. Acesse: https://shadowtraffic.io
2. Cadastre-se para obter Free Trial
3. Copie as credenciais para `gen/.env`

---

## Parametros de Geracao

### maxEvents

Define quantos registros serao gerados:

```json
{
  "localConfigs": {
    "maxEvents": 80000,  // Total de registros a gerar
    "throttleMs": 20     // Delay entre registros (ms)
  }
}
```

**Valores atuais**:
- `gen-drivers`: 80.000 eventos
- `gen-users`: 80.000 eventos
- `gen-minio`: Infinito (ate parar manualmente)

### throttleMs

Controla a velocidade de geracao:
- **10ms**: ~100 registros/segundo (muito rapido)
- **20ms**: ~50 registros/segundo (recomendado)
- **50ms**: ~20 registros/segundo (lento)
- **100ms**: ~10 registros/segundo (muito lento)

---

## Como Usar

### Iniciar Geradores

```powershell
# Apenas geradores (infra deve estar rodando)
.\scripts\start-generators.ps1

# Ou tudo de uma vez
.\scripts\start-all.ps1
```

### Parar Geradores

```powershell
# Para geradores (mantem infra)
.\scripts\stop-generators.ps1

# Para tudo
.\scripts\stop-all.ps1
```

### Monitorar Geracao

```powershell
# Ver logs em tempo real
docker-compose logs -f gen-drivers gen-users gen-minio

# Verificar contagem no Postgres
docker exec postgres-ubereats psql -U usrUberEats -d ubereats_db -c "SELECT 'drivers', COUNT(*) FROM drivers UNION ALL SELECT 'users', COUNT(*) FROM users;"

# Verificar arquivos no MinIO
docker exec minio-ubereats mc ls local/uber-eats/ --recursive
```

---

## Troubleshooting

### Erro: "License expired"

```powershell
# 1. Renove a licenca em https://shadowtraffic.io
# 2. Atualize gen/.env com as novas credenciais
# 3. Reinicie os geradores:
.\scripts\stop-generators.ps1
.\scripts\start-generators.ps1
```

### Erro: "Connection refused" (Postgres)

```powershell
# Verifique se o Postgres esta rodando
docker ps | findstr postgres

# Inicie a infra primeiro
.\scripts\start-infra.ps1

# Depois os geradores
.\scripts\start-generators.ps1
```

### Geradores param sozinhos

Isso e normal! Quando atingem `maxEvents`, eles finalizam automaticamente.

```powershell
# Verificar logs
docker logs gen-drivers --tail 20

# Deve mostrar: "Done" no final
```

### Geracao muito lenta

```powershell
# Diminua o throttleMs nos templates:
# gen/postgres/drivers.json.template
# gen/postgres/users.json.template

# De: "throttleMs": 50
# Para: "throttleMs": 10

# Regenere as configs e reinicie:
.\gen\setup-configs.ps1
.\scripts\stop-generators.ps1
.\scripts\start-generators.ps1
```

---

## Performance e Otimizacao

### Ajustar Velocidade

Para gerar **mais rapido**:

```json
{
  "localConfigs": {
    "maxEvents": 100000,
    "throttleMs": 10  // Mais rapido
  }
}
```

Para gerar **mais devagar** (economizar recursos):

```json
{
  "localConfigs": {
    "maxEvents": 100000,
    "throttleMs": 100  // Mais devagar
  }
}
```

### Consumo de Recursos

| Geradores | CPU | RAM |
|-----------|-----|-----|
| 1 gerador | ~5% | 512 MB |
| 2 geradores | ~10% | 1 GB |
| 3 geradores | ~15% | 1.5 GB |

**Recomendacao**: Se tiver menos de 16 GB RAM, gere dados em etapas:

```powershell
# 1. Gere apenas Postgres
.\scripts\start-generators.ps1
# Aguarde finalizar...

# 2. Pare e gere apenas MinIO (se necessario)
.\scripts\stop-generators.ps1
docker-compose up -d gen-minio
```

---

## Estrutura dos Dados Gerados

### Relacionamentos

Os dados tem **relacionamentos realistas**:

```
users (mssql/users/)
  |
  +-- orders (kafka/orders/) [via CPF]
        |
        +-- items (mongodb/items/) [via order_id]
        +-- payments (kafka/payments/) [via order_id]
        +-- route (kafka/route/) [via order_id]
              |
              +-- gps (kafka/gps/) [20 pontos por rota]
        +-- status (kafka/status/) [8 estados por pedido]
        +-- receipts (kafka/receipts/)

drivers (postgres/drivers/)
  |
  +-- orders (kafka/orders/) [via license_number]
  +-- shift (kafka/shift/) [turnos]

restaurants (mysql/restaurants/)
  |
  +-- products (mysql/products/) [via restaurant_id]
  +-- ratings (mysql/ratings/) [via CNPJ]
  +-- menu (mysql/menu/) [secoes]
```

### State Machines

Alguns eventos usam **maquinas de estado**:

**Payment Events** (kafka/events/):
```
created → authorized → captured → succeeded → settled → closed
                                     ↓
                                  refunded → closed
```

**Order Status** (kafka/status/):
```
Order Placed → In Analysis → Accepted → Preparing → 
Ready for Pickup → Picked Up → Out for Delivery → 
Delivered → Completed
```

---

## Customizacao

### Adicionar Novos Campos

Edite os templates em `gen/postgres/*.json.template`:

```json
{
  "row": {
    "new_field": {
      "_gen": "string",
      "expr": "#{Lorem.word}"
    }
  }
}
```

**Geradores Faker disponiveis**:
- `#{Name.firstName}`, `#{Name.lastName}`, `#{Name.fullName}`
- `#{Internet.emailAddress}`, `#{Internet.userName}`, `#{Internet.url}`
- `#{PhoneNumber.phoneNumber}`
- `#{Address.streetAddress}`, `#{Address.city}`, `#{Address.state}`
- `#{Company.name}`, `#{Job.title}`
- `#{Lorem.sentence}`, `#{Lorem.paragraph}`
- `#{Commerce.productName}`, `#{Commerce.price}`

### Mudar Quantidade de Eventos

```json
{
  "localConfigs": {
    "maxEvents": 200000,  // Dobrar para 200k
    "throttleMs": 20
  }
}
```

Depois:

```powershell
.\gen\setup-configs.ps1
.\scripts\stop-generators.ps1
.\scripts\start-generators.ps1
```

---

## Links

- ShadowTraffic: https://shadowtraffic.io
- Docs: https://docs.shadowtraffic.io
- Faker: https://www.datafaker.net/documentation/expressions/

