---
domain: cloud-resolution
topic: roles
---

# Papéis (roles) e roteamento papel → KB

Agentes e skills falam em **papel**, nunca em serviço. O `_index.yaml` liga papel + provider
ao domínio de KB que traz o serviço concreto.

## Papéis

| role | Responsabilidade | Exemplos de tarefa |
|---|---|---|
| `iac-provider` | Provider de IaC da nuvem: autenticação da ferramenta, backend de state remoto, recursos base | "sobe a infra", "configura o state remoto" |
| `warehouse` | Data warehouse analítico gerenciado | bulk load, MERGE/SCD2, pausar para economizar |
| `streaming` | Broker de eventos gerenciado com endpoint Kafka | criar tópico, conectar Kafka Connect, auth do cliente |
| `object-storage` | Data lake / object storage | layout de zonas, permissão mínima, acesso por identidade de serviço |
| `stream-processing` | Processamento contínuo gerenciado | job de stream, reference/side data, janela de tempo |

Papel novo = linha nova aqui + `role:` válido em KBs. Não crie papel para um único serviço
de um único provider — papel é capacidade, existe nas três nuvens.

## Roteamento no `_index.yaml`

Toda KB de serviço declara:

```yaml
  <provider>-<servico>:
    provider: azure | aws | gcp
    role: iac-provider | warehouse | streaming | object-storage | stream-processing
```

Algoritmo (agente ou skill):

1. Passo 0 → `provider` (ver `provider-resolution.md`).
2. Identifique o `role` da tarefa pela tabela acima.
3. Filtre os domínios do `_index.yaml` com `provider == P` e `role == R`.
4. **Exatamente 1** → abra o `index.md` dele e siga o learning path.
5. **0** → pare e diga: "não há KB para `{P}/{R}` — rode `kb-architect`". Não improvise
   a partir de conhecimento geral.
6. **>1** → pergunte ao usuário qual serviço o projeto usa e registre no `CLAUDE.md`.

## Composição de papéis

Tarefas reais cruzam papéis (ex.: conector que lê do `streaming` e grava no
`object-storage`). Resolva cada papel separadamente e abra as duas KBs — nunca uma KB
"combo".
