# MinIO - Documentacao Tecnica

Data Lake S3-compatible para eventos JSON (orders, gps, payments, status, ratings e mais 15+ streams).

---

## Especificacoes Tecnicas

| Item | Valor |
|------|-------|
| **Imagem Docker** | `minio/minio:latest` |
| **API Port** | `9000` |
| **Console Port** | `9001` |
| **Root User** | `usrUberEats` |
| **Root Password** | `supersecret` |
| **Volume** | `minio_data` (persistente) |
| **Bucket Principal** | `uber-eats` |

---

## URLs de Acesso

### Console Web (Interface Grafica)
```
URL: http://localhost:9001
Usuario: usrUberEats
Senha: supersecret
```

### API S3 (Para aplicacoes)
```
Endpoint: http://localhost:9000
Access Key: usrUberEats
Secret Key: supersecret
Region: us-east-1
```

---

## Estrutura do Bucket

O bucket `uber-eats` contem eventos organizados por prefixo (pasta):

```
uber-eats/
├── mssql/users/           # Dados de usuarios (MSSQL)
├── mongodb/users/         # Dados de usuarios (MongoDB)
├── postgres/drivers/      # Dados de motoristas
├── kafka/orders/          # Pedidos
├── kafka/payments/        # Pagamentos
├── kafka/events/          # Eventos de pagamento
├── kafka/route/           # Rotas de entrega
├── kafka/gps/             # Localizacao GPS em tempo real
├── kafka/status/          # Status dos pedidos
├── kafka/shift/           # Turnos dos motoristas
├── kafka/receipts/        # Recibos
├── kafka/search/          # Buscas de usuarios
├── mysql/restaurants/     # Restaurantes
├── mysql/products/        # Produtos do menu
├── mysql/ratings/         # Avaliacoes
├── mysql/menu/            # Secoes do menu
├── postgres/inventory/    # Estoque
├── mongodb/items/         # Itens dos pedidos
├── mongodb/recommendations/ # Recomendacoes
└── mongodb/support/       # Tickets de suporte
```

**Total**: ~20 streams de dados diferentes!

---

## Como Acessar

### 1. Via Console Web (MinIO UI)

1. Abra no browser: `http://localhost:9001`
2. Login:
   - **Username**: `usrUberEats`
   - **Password**: `supersecret`
3. Navegue pelo bucket `uber-eats`

### 2. Via MinIO Client (mc)

```powershell
# Configurar alias
docker exec minio-ubereats mc alias set local http://localhost:9000 usrUberEats supersecret

# Listar buckets
docker exec minio-ubereats mc ls local/

# Listar arquivos do bucket
docker exec minio-ubereats mc ls local/uber-eats/ --recursive

# Ver conteudo de um arquivo
docker exec minio-ubereats mc cat local/uber-eats/kafka/orders/<arquivo>.json
```

### 3. Via AWS CLI (S3 Compatible)

```powershell
# Instale o AWS CLI primeiro: https://aws.amazon.com/cli/

# Configure
aws configure
# AWS Access Key ID: usrUberEats
# AWS Secret Access Key: supersecret
# Default region name: us-east-1

# Listar buckets
aws s3 ls --endpoint-url http://localhost:9000

# Listar arquivos
aws s3 ls s3://uber-eats/ --endpoint-url http://localhost:9000 --recursive

# Download de arquivo
aws s3 cp s3://uber-eats/kafka/orders/file.json . --endpoint-url http://localhost:9000
```

### 4. Via Python (boto3)

```python
import boto3
from botocore.client import Config

# Configurar cliente S3
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='usrUberEats',
    aws_secret_access_key='supersecret',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

# Listar objetos no bucket
response = s3.list_objects_v2(Bucket='uber-eats', Prefix='kafka/orders/')
for obj in response.get('Contents', []):
    print(obj['Key'])

# Ler um arquivo JSON
obj = s3.get_object(Bucket='uber-eats', Key='kafka/orders/file.json')
data = obj['Body'].read().decode('utf-8')
print(data)
```

---

## Formato dos Dados

### Exemplo: Pedido (Order)

```json
{
  "order_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "user_key": "123.456.789-00",
  "restaurant_key": "12.345.678/0001-90",
  "rating_key": "uuid-rating",
  "driver_key": "AB1234567",
  "order_date": "2025-01-04 15:30:45.123456",
  "total_amount": 85.50,
  "payment_key": "uuid-payment",
  "dt_current_timestamp": "2025-01-04 15:30:45.123"
}
```

### Exemplo: GPS Tracking

```json
{
  "gps_id": "uuid-gps",
  "order_id": "uuid-order",
  "lat": -23.561234,
  "lon": -46.654321,
  "speed_kph": 15,
  "direction_deg": 90,
  "duration_ms": 1500,
  "accuracy_m": 10.5,
  "altitude": 750.0,
  "timestamp": "2025-01-04 15:31:00.000",
  "dt_current_timestamp": "2025-01-04 15:31:00.000"
}
```

### Exemplo: Pagamento

```json
{
  "payment_id": "uuid-payment",
  "order_key": "uuid-order",
  "amount": 85.50,
  "currency": "BRL",
  "method": "Card",
  "provider": "Stripe",
  "card_brand": "Visa",
  "card_last4": "1234",
  "status": "succeeded",
  "platform_fee": 4.25,
  "provider_fee": 2.50,
  "tax_amount": 8.55,
  "net_amount": 70.20,
  "timestamp": "2025-01-04 15:30:50.000"
}
```

---

## Monitoramento e Logs

### Ver Logs do MinIO

```powershell
# Logs em tempo real
docker-compose logs -f minio-ubereats

# Ultimas 50 linhas
docker logs minio-ubereats --tail 50
```

### Verificar Health Check

```powershell
docker inspect minio-ubereats --format='{{.State.Health.Status}}'

# Ou via API
curl http://localhost:9000/minio/health/live
```

### Estatisticas do Bucket

```powershell
# Via mc (MinIO Client)
docker exec minio-ubereats mc du local/uber-eats
```

---

## Backup e Restore

### Backup do Bucket

```powershell
# Backup completo via mc
docker exec minio-ubereats mc mirror local/uber-eats /backup/uber-eats

# Ou via AWS CLI
aws s3 sync s3://uber-eats/ ./backup/uber-eats/ --endpoint-url http://localhost:9000
```

### Restore

```powershell
# Restore via mc
docker exec minio-ubereats mc mirror /backup/uber-eats local/uber-eats

# Ou via AWS CLI
aws s3 sync ./backup/uber-eats/ s3://uber-eats/ --endpoint-url http://localhost:9000
```

---

## Configuracoes Avancadas

### Politicas de Acesso (Bucket Policy)

Por padrao, o bucket `uber-eats` esta configurado com acesso publico para facilitar o desenvolvimento:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {"AWS": ["*"]},
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::uber-eats/*"]
    }
  ]
}
```

### Versionamento (Desabilitado)

O versionamento esta desabilitado para economizar espaco. Para habilitar:

```powershell
docker exec minio-ubereats mc version enable local/uber-eats
```

### Lifecycle Policies

Para deletar arquivos antigos automaticamente:

```json
{
  "Rules": [
    {
      "Expiration": {
        "Days": 30
      },
      "ID": "DeleteOldFiles",
      "Status": "Enabled"
    }
  ]
}
```

---

## Integracao com Databricks

O MinIO sera usado como:
- **External Location** no Unity Catalog
- **Source** para Auto Loader (cloudFiles)
- **Landing Zone** para dados brutos

Configuracao no Databricks:

```python
# Configurar credenciais
spark.conf.set("fs.s3a.endpoint", "http://localhost:9000")
spark.conf.set("fs.s3a.access.key", "usrUberEats")
spark.conf.set("fs.s3a.secret.key", "supersecret")
spark.conf.set("fs.s3a.path.style.access", "true")

# Ler dados
df = spark.read.json("s3a://uber-eats/kafka/orders/")
display(df)
```

---

## Troubleshooting

### Console nao abre (porta 9001)

```powershell
# Verificar se a porta esta em uso
netstat -ano | findstr "9001"

# Ou mude a porta no docker-compose.yml
```

### Erro "Access Denied"

```powershell
# Verifique as credenciais
docker exec minio-ubereats mc admin info local
```

### Bucket nao aparece

```powershell
# Recrie o bucket
docker exec minio-ubereats mc mb local/uber-eats --ignore-existing
docker exec minio-ubereats mc policy set public local/uber-eats
```

---

## Performance e Otimizacao

### Compressao

Os arquivos JSON **nao estao comprimidos** por padrao. Para otimizar:

```powershell
# Use formato Parquet (mais eficiente)
# Ou comprima os JSONs:
gzip kafka/orders/*.json
```

### Particionamento

Organize os dados por data para queries mais eficientes:

```
uber-eats/
├── kafka/orders/
│   ├── year=2025/
│   │   ├── month=01/
│   │   │   ├── day=04/
│   │   │   │   └── orders.json
```

---

## Links

- MinIO: https://min.io/docs/minio/linux/index.html
- AWS CLI S3: https://docs.aws.amazon.com/cli/latest/reference/s3/
- boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

