# MinIO - Data Lake S3

Data Lake local para eventos JSON (~20 streams).

---

## Credenciais

```
Console: http://localhost:9001
API: http://localhost:9000
User: usrUberEats
Password: supersecret
Bucket: uber-eats
```

---

## Estrutura do Bucket

```
uber-eats/
├── kafka/orders/      # Pedidos
├── kafka/payments/    # Pagamentos
├── kafka/gps/         # Tracking GPS
├── kafka/status/      # Status dos pedidos
├── mysql/restaurants/ # Restaurantes
├── mysql/products/    # Produtos
├── mysql/ratings/     # Avaliacoes
├── mongodb/items/     # Itens dos pedidos
└── ... (~20 streams)
```

---

## Como Acessar

### Console Web

1. Abra: `http://localhost:9001`
2. Login: `usrUberEats` / `supersecret`
3. Navegue pelo bucket `uber-eats`

### MinIO Client (mc)

```powershell
# Listar buckets
docker exec minio-ubereats mc ls local/

# Listar arquivos
docker exec minio-ubereats mc ls local/uber-eats/ --recursive

# Ver arquivo
docker exec minio-ubereats mc cat local/uber-eats/kafka/orders/<arquivo>.json
```

### AWS CLI

```powershell
# Listar
aws s3 ls s3://uber-eats/ --endpoint-url http://localhost:9000 --recursive

# Download
aws s3 cp s3://uber-eats/kafka/orders/file.json . --endpoint-url http://localhost:9000
```

---

## Exemplo de Dados

### Pedido (Order)

```json
{
  "order_id": "uuid",
  "user_key": "123.456.789-00",
  "restaurant_key": "12.345.678/0001-90",
  "driver_key": "AB1234567",
  "order_date": "2025-01-04 15:30:45",
  "total_amount": 85.50
}
```

---

## Troubleshooting

### Console nao abre

```powershell
docker logs minio-ubereats
netstat -ano | findstr "9001"
```

### Bucket nao aparece

```powershell
docker exec minio-ubereats mc mb local/uber-eats --ignore-existing
```

---

## Links

- MinIO: https://min.io/docs/minio/linux/index.html
- AWS CLI: https://docs.aws.amazon.com/cli/latest/reference/s3/
