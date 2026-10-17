---
domain: terraform
topic: plan-apply-with-agreement
---

# Ciclo plan → acordo → apply

Fluxo padrão do `iac-engineer`. Nenhum passo que muda a nuvem roda sem o usuário ver o
`plan` e dizer "pode".

## Pré-requisitos

1. Terraform instalado na versão de `required_version`
   (`terraform version`; instalação: gerenciador de pacotes do SO ou `tfenv`/`tfswitch`).
2. CLI da nuvem autenticada — comando específico em `patterns/provider-auth.md` da KB
   `role: iac-provider`.
3. Backend de state existente (`concepts/state.md` → bootstrap).

## Passos

```bash
cd infra/envs/dev
terraform fmt -recursive -check   # falhou → terraform fmt -recursive
terraform init                    # baixa providers, conecta no backend
terraform validate
terraform plan -out=tfplan        # salva o plano exato que será aplicado
terraform show -no-color tfplan   # mostrar ao usuário
```

**Pare aqui.** Mostre ao usuário, em linguagem simples:

- quantos recursos `create` / `update` / `destroy`;
- qualquer `destroy` ou `replace` (`-/+`) — destaque, é perda de dado possível;
- custo estimado por hora/mês dos recursos novos (seção "Custo e free tier" da KB de serviço).

Só com o "pode" explícito:

```bash
terraform apply tfplan            # aplica exatamente o plano mostrado
```

Nunca `terraform apply -auto-approve` fora de CI. Plano mudou (novo `plan`)? Peça acordo de novo.

## Depois do apply

- `terraform output` — anote endpoints; segredos ficam `sensitive`.
- Registre no README/HANDOFF do projeto o que está ligado e o horário do teardown previsto.

## Falhas comuns

| Sintoma | Causa provável | Ação |
|---|---|---|
| Erro de autenticação no `init`/`plan` | Login da CLI expirado | Refazer login (KB `iac-provider`) |
| `Error acquiring the state lock` | Outro apply ou lock órfão | Confirmar e só então `force-unlock` com acordo |
| API/serviço não habilitado | Conta nova sem o serviço ativado | Habilitar via recurso Terraform, não pelo console |
| Quota / região sem capacidade | Limite de conta gratuita | Trocar região ou SKU; nunca pedir aumento sem acordo |
