# 016 — Promoção dsv → prd por tag, com aprovação humana

**Status:** Aceita  
**Data:** 2026-11-12  
**Autores:** time  
**Revisa:** o invariante do `CLAUDE.md` "promoção por `main` única + GitHub Actions + Environments: merge na `main` faz
deploy no dsv da nuvem afetada; o job de prd exige aprovação do usuário"

---

## Contexto

O projeto trabalha com dois ambientes **na nuvem**, `dsv` e `prd`. O ambiente local serve só para desenvolver código.
A esteira de CD ainda não existe. No grill do `azure-warehouse` (D17 e D24 de
[01-grill.md](../../.claude/projetos/azure-warehouse/01-grill.md)), o usuário trouxe uma recomendação de mercado
(tag dispara o prd, GitHub Environments com aprovação manual). Dois pontos do invariante atual não fechavam:

1. **Merge na `main` aplica no dsv sozinho.** Isso contradiz outro invariante: "antes de `terraform apply` que crie ou
   escale recurso pago, mostrar o `plan` e a estimativa e esperar o ok". Na free account, um merge distraído pode ligar
   recurso pago.
2. **O prd sair do mesmo gatilho da `main`** não dá um ponto de release nomeado nem um rollback claro.

Restrições: repositório **público** (logs de Actions legíveis por qualquer pessoa), usuário **solo** e free account com
crédito único.

## Decisão

1. **GitHub Environments `dsv` e `prd`**, com os mesmos nomes de secret e variável e valores diferentes. Workflows
   idênticos; o ambiente muda só por configuração.
2. **dsv:** disparado pelo merge na `main` (filtrado por `paths:` da nuvem afetada). **Enquanto durar a free account, o
   environment `dsv` também exige aprovação do usuário**: o PR mostra o `plan` e a estimativa por hora e por dia (da API
   pública de preços da Azure), e aprovar é o "ok" do invariante de custo. Revisável.
3. **prd:** disparado por **tag `vX.Y.Z`**, só se o commit da tag estiver na `main`; o job pausa até a aprovação do
   usuário. O agente **nunca aprova**.
4. **Autenticação na nuvem por OIDC desde o primeiro dia**, sem segredo de longa duração no GitHub. IDs de subscription,
   tenant e client cadastrados como secret para ficarem mascarados nos logs.
5. **A esteira só aplica estrutura** (Terraform, tabelas, procedures, pipelines); nunca carrega dado, para que erro de
   dado não apareça em log público.
6. **Plano B só para o dsv:** se a esteira falhar durante os 30 dias da free account, `apply` local com `plan`,
   estimativa e "ok" do usuário (o invariante de custo atual), registrado como exceção. O prd sai **só** pela esteira.
7. **`prevent_self_review` desligado** (usuário solo; ligado, ele não conseguiria aprovar). Volta a ser ligado quando
   entrar uma segunda pessoa.
8. A esteira é construída no projeto próprio `github-cd`, com stub de deploy, **antes** de abrir a conta (ADR 015).

## Alternativas consideradas

### Opção A — Invariante atual: merge na `main` aplica no dsv e dispara o prd com aprovação ❌ Rejeitada

Aplica recurso pago no dsv sem o "ok" de custo e não nomeia a release.

### Opção B — Branches por ambiente (`dev`, `prd`) ❌ Rejeitada

Código divergente entre ambientes; o projeto já decidiu código único parametrizado por ambiente.

### Opção C — Tag para o prd, aprovação no prd e no dsv, OIDC ✅ Escolhida

Release nomeada com rollback pela tag anterior, custo aprovado antes de cada apply e nenhum segredo de longa duração
num repositório público.

### Opção D — Só `apply` local, sem esteira ❌ Rejeitada como caminho normal

É o estado atual e fica como plano B do dsv; sem esteira não há promoção controlada para o prd.

## Consequências

### Positivas

- Nenhum apply pago sem o "ok" do usuário, nem pela esteira.
- Release em prd rastreável por tag, com rollback nomeado.
- Sem token de longa duração no GitHub.

### Negativas / Tradeoffs

- Aprovação manual também no dsv: um clique a mais por deploy enquanto durar a free account.
- Mais um projeto (`github-cd`) antes de abrir a conta.
- Com `prevent_self_review` desligado e admin podendo contornar regras, a aprovação é guarda-corpo, não cadeado.

### Riscos

- **Runner do GitHub sem acesso ao endpoint SQL do Synapse** (IP variável, firewall). A resolver na arquitetura
  (regra temporária no job, com a permissão na identidade OIDC).
- **Log público expondo infraestrutura:** mitigado por secrets mascarados e pela esteira que não carrega dado.

## Revisão

Esta ADR deve ser revisada se:

- a conta deixar de ser free account (a aprovação no dsv pode cair);
- entrar uma segunda pessoa no projeto (`prevent_self_review` e aprovações de PR sobem);
- o repositório deixar de ser público.
