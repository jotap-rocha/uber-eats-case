---
domain: terraform
topic: state
---

# State

## O que é

O state (`terraform.tfstate`) é o mapa entre o que está no código e o que existe na nuvem.
Sem ele o Terraform não sabe o que criou — e não consegue destruir.

## Local vs remoto

| | Local (`terraform.tfstate` no disco) | Remoto (backend da nuvem) |
|---|---|---|
| Uso | Experimento descartável de 1 pessoa | Qualquer coisa que dure mais que uma tarde |
| Lock | Não | Sim (evita 2 `apply` simultâneos) |
| Risco | Perder o arquivo = recursos órfãos cobrando | Backend precisa existir antes (bootstrap) |
| Contém segredo? | Pode conter (outputs, senhas geradas) | Idem — o backend precisa de acesso restrito |

Regra do harness: **remoto por padrão**. Como configurar o backend é específico do provider
→ `patterns/remote-state.md` da KB `role: iac-provider`.

## Bootstrap (o ovo e a galinha)

O bucket/container do state não pode ser criado pelo mesmo state que ele guarda. Opções:

1. Pasta `bootstrap/` com state **local**, que só cria o armazenamento do state; depois o
   resto da infra usa backend remoto.
2. Criar o armazenamento do state pela CLI da nuvem, uma vez, e documentar o comando.

Em ambos os casos: o recurso de state **não** entra no teardown diário.

## Lock

- Backend remoto com lock nativo é o padrão; nunca desligue o lock para "destravar".
- Lock preso após falha: `terraform force-unlock <LOCK_ID>` — só com acordo, depois de
  confirmar que nenhum outro `apply` está rodando.

## Drift

`terraform plan -refresh-only` mostra o que mudou fora do Terraform (console, CLI).
Decida: importar para o código ou reverter na nuvem. Não deixe drift acumular.
