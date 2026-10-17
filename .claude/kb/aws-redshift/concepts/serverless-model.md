---
domain: aws-redshift
topic: serverless-model
---

# Modelo do Redshift Serverless

## Namespace × workgroup

| Objeto | Contém | Analogia Synapse |
|---|---|---|
| **Namespace** | dados (managed storage), schemas, usuários, IAM roles associadas, KMS, snapshots | o banco do Dedicated Pool |
| **Workgroup** | compute (RPU), rede (VPC/subnets/SG), endpoint, limites de uso | o "DWU" do pool |

1 namespace ↔ 1 workgroup. Destruir o workgroup derruba o endpoint (os dados ficam no
namespace); destruir o namespace apaga os dados (ofereça snapshot final se precisar).

## RPU (Redshift Processing Unit)

- 1 RPU = 16 GB de memória.
- **Base capacity:** RPU usado para servir queries. Faixa **4–512** (até 1024 em algumas
  regiões). Valores: 4, ou múltiplos de 8 a partir de 8. Default **128**.
- **Max capacity:** teto de escala automática — o freio contra picos.
- Escala automática em degraus: 4→8 (passo 4), 8→512 (passo 8), 512→1024 (passo 32).

### Base 4 RPU (entrada barata)

- Até 32 TB de managed storage; recomendado ≤ 100 colunas por tabela; 64 GB de memória.
- Disponível só em algumas regiões (ex.: us-east-1/2, us-west-1/2, ap-south-1,
  ap-southeast-1/2, ap-northeast-1, eu-west-1, eu-north-1) — confira `<REGION>`.
- Depois de escalar acima de 4, **não volta sozinho para 4** — ajuste manual.
- VACUUM boost só ≥ 8 RPU.

Recomendação de lab: **base 8**, max 16 (ou base 4 se a região suportar e o volume for pequeno).

## Price-performance target (AI-driven scaling)

Ativo por padrão em workgroups novos, em **Balanced**. Para lab, "Optimizes for cost"
reduz escala agressiva. `max_capacity` e usage limits são **sempre** respeitados,
independentemente do slider. AWS recomenda o recurso para base entre 8 e 512.

## Cobrança

- Por segundo, mínimo 60 s, só enquanto há trabalho (queries, COPY, manutenção
  disparada por carga). Ocioso = sem RPU-hora.
- Storage gerenciado cobrado à parte (GB-mês), inclusive snapshots.

## Rede e acesso

- Workgroup vive em subnets privadas (recomendado ≥ 3 AZs); `publicly_accessible = false`.
- Clientes: Query Editor v2 (IAM), JDBC/ODBC via VPN/bastion, Data API
  (`aws redshift-data execute-statement`) — útil em pipeline sem driver.

```bash
aws redshift-data execute-statement --workgroup-name <PROJETO>-wg \
  --database analytics --sql "select count(*) from dw.dim_cliente"
```

## IAM roles do namespace

- `iam_roles` lista as roles que o Redshift pode assumir (trust `redshift.amazonaws.com`,
  e para serverless também `redshift-serverless.amazonaws.com` — **a validar** se ambas
  são necessárias na sua conta).
- `default_iam_role_arn` habilita `IAM_ROLE default` no SQL — o código não carrega ARN.
