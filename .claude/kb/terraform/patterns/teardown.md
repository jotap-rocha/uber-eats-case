---
domain: terraform
topic: teardown
---

# Teardown — não deixar crédito queimando

Conta free tier/crédito acaba rápido com recurso cobrado por hora esquecido ligado.
Regra do harness: **criar → testar → destruir ou pausar no mesmo dia**.

## Antes de criar

- Para cada recurso com custo por hora, a KB de serviço diz em "Custo e free tier" se ele
  **pausa** (mantém dado, para de cobrar compute) ou só **destrói**.
- Marque recursos com tag/label `ttl=<data>` e `owner=<pessoa>`.
- Configure budget e alerta de faturamento da conta (detalhe na KB `iac-provider`) — é o
  único guard-rail que funciona quando o agente não está rodando.

## Pausar vs destruir

| Situação | Ação |
|---|---|
| Recurso com dado que custa recriar (warehouse carregado) | Pausar, se o serviço suporta |
| Recurso sem estado ou recriável pelo código | Destruir |
| Fim do experimento | Destruir tudo, exceto o armazenamento do state |

## Destruir só uma parte

```bash
terraform plan -destroy -target=module.streaming -out=destroy.tfplan
terraform show -no-color destroy.tfplan     # mostrar e pedir acordo
terraform apply destroy.tfplan
```

## Destruir tudo

```bash
terraform plan -destroy -out=destroy.tfplan
terraform show -no-color destroy.tfplan     # mostrar e pedir acordo
terraform apply destroy.tfplan
```

`destroy` é irreversível: sempre `plan -destroy` + acordo explícito. O `agent-policies` do
harness pode exigir confirmação adicional.

## Checklist de fim de dia

- [ ] `terraform state list` — o que ainda existe?
- [ ] Recursos pausáveis pausados; o resto destruído
- [ ] Console de faturamento sem recurso inesperado cobrando
- [ ] HANDOFF/README atualizado com o que ficou ligado e por quê
