---
domain: gcp-managed-kafka
topic: cluster-sizing-cost
---

# Cluster: dimensionamento, rede e custo

## Capacidade

- O cliente define **vCPU total** e **memória total**; o serviço decide brokers e
  distribuição em 3 zonas.
- **Mínimo 3 vCPU.** Memória entre **1 e 8 GiB por vCPU** (3 vCPU → 3 a 24 GiB).
- Referência do Google: ~1 vCPU ≈ 20 MiB/s de publish e 80 MiB/s de consumo.
- Scale up/down sem recriar; `rebalance_config.mode = "AUTO_REBALANCE_ON_SCALE_UP"`
  redistribui réplicas (impacto temporário de performance).
- `kafka_version` default `3.7.x` (o provider aceita versões mais novas, ex. `4.x`).

## Rede

- Cluster é exposto **dentro de VPC**: 1–10 subnets, uma por rede, mesma região do cluster.
  IPs de bootstrap/brokers e DNS (`*.managedkafka.<GCP_PROJECT_ID>.cloud.goog`) são criados
  automaticamente nessas subnets.
- Cliente precisa estar numa rede conectada (VM, GKE, Dataflow worker, Cloud Run com VPC
  egress). De fora: VPN/Interconnect.
- Subnet de outro projeto exige permissão para o service agent do Kafka.
- Acesso público com `allowed_source_ip_ranges` existe no provider Terraform
  (`public_cluster_config`) — tratar como exceção, **a validar** por região/GA.

## Custo (modelo)

| Componente | Como cobra |
|---|---|
| Compute | DCU-hora; ≈ 0,6 DCU/vCPU + 0,1 DCU/GiB; ~US$ 0,09/DCU-h em `us-central1` (**a validar**) |
| Storage | Por GiB-mês dos dados retidos (disco dos brokers / storage) — **a validar** |
| Rede | Transferência entre zonas (~US$ 0,01/GiB citado) |
| Connect cluster | Recurso separado, cobrado por hora; CUD não se aplica |
| CMEK | Custo de Cloud KMS à parte |

Exemplos (só compute, ordem de grandeza):

| Config | DCU | US$/h | US$/mês (730 h) |
|---|---|---|---|
| 3 vCPU / 3 GiB (mínimo) | 2,1 | ~0,19 | ~140 |
| 3 vCPU / 12 GiB | 3,0 | ~0,27 | ~200 |

## Terraform

```hcl
data "google_project" "this" {}

resource "google_managed_kafka_cluster" "lab" {
  cluster_id = "<CLUSTER>"
  location   = var.region
  capacity_config {
    vcpu_count   = 3
    memory_bytes = 3221225472   # 3 GiB
  }
  gcp_config {
    access_config {
      network_configs {
        subnet = "projects/${data.google_project.this.number}/regions/${var.region}/subnetworks/default"
      }
    }
  }
  rebalance_config { mode = "AUTO_REBALANCE_ON_SCALE_UP" }
  labels = { env = "lab" }
}
```

`deletion_policy = "PREVENT"` só em produção; em lab deixe o default (`DELETE`) para o
`terraform destroy` funcionar no fim do dia.

## Regra de custo

Não existe pausa. Cluster criado = cobrança contínua. Destruir no mesmo dia.
