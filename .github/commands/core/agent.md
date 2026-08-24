# /core/agent

Use este comando para rotear automaticamente a solicitação do usuário para o agente mais apropriado do projeto.

## Objetivo

Este comando deve executar o seguinte fluxo:

1. analisar a solicitação do usuário
2. consultar `.github/commands/core/router.md`
3. selecionar o agente primário mais apropriado
4. abrir e seguir o arquivo markdown do agente selecionado em `.github/agents/`
5. consultar a knowledge base relevante em `.github/kb/`, quando aplicável
6. usar agentes de apoio apenas se houver ganho claro
7. responder em conformidade com o escopo, comportamento e estilo do agente selecionado

---

## Regras obrigatórias

- Sempre consultar `.github/commands/core/router.md` antes de responder
- Sempre escolher um agente primário
- Sempre abrir o arquivo do agente primário selecionado
- Sempre usar o conteúdo do agente como instrução principal
- Consultar a KB relevante quando o domínio exigir
- Usar agentes de apoio somente quando necessário
- Responder em português brasileiro, salvo se o usuário pedir outro idioma
- Quando o projeto evoluir (novos agentes, novas prioridades), **atualizar** `.github/commands/core/router.md` para refletir a mudança

---

## Fluxo operacional

### Etapa 1 — roteamento
Leia `.github/commands/core/router.md` e determine:

- intenção principal
- entregável principal
- agente primário
- agentes de apoio, se necessário

### Etapa 2 — carregamento do agente
Abra o arquivo do agente primário selecionado em `.github/agents/`.

Use esse arquivo para definir:

- papel
- escopo
- comportamento
- estilo de resposta
- ações prioritárias

### Etapa 3 — carregamento de conhecimento
Se o agente ou o router indicarem necessidade de knowledge base:

- consulte `.github/kb/_index.yaml`
- carregue o domínio relevante em `.github/kb/`
- priorize KB específica do domínio antes de usar contexto genérico

### Etapa 4 — resposta
Responda com base em:

- router
- agente primário
- KB relevante
- contexto do projeto em `.github/CURSOR.MD` (se existir)

---

## Formato interno de decisão

Antes de responder, determine internamente:

- agente primário selecionado
- motivo da escolha
- KB consultada
- agentes de apoio, se houver

Não é necessário exibir isso ao usuário, a menos que o usuário peça explicitamente para mostrar a decisão de roteamento.

---

## Quando usar este comando

Use este comando quando o usuário quiser:

- uma resposta automática com o agente correto
- roteamento inteligente entre agentes
- uma entrada única para o ecossistema multiagente
- evitar escolher manualmente um agente específico

---

## Exemplos de uso

### Exemplo 1
```text
/core/agent como otimizar um join grande que está gerando muito shuffle no Spark?
```

### Exemplo 2
```text
/core/agent revise este módulo Python focando em segurança e testes.
```

---

## Manutenção

Ao longo do desenvolvimento, alinhe **router**, **agentes** e **documentação de contexto**:

| Artefato | Quando atualizar |
|----------|------------------|
| `.github/commands/core/router.md` | Novos `.md` em `.github/agents/`, mudança de prioridades ou de “agente expert” do repo |
| `.cursorrules`, `.github/CURSOR.MD`, `CONTEXT.md` | Mudança de comandos, estrutura ou convenções usadas no dia a dia |
