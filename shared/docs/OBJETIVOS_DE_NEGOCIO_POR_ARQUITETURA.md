# Objetivos de negócio por arquitetura

**Status:** aceito pelo usuário em 2026-11-02. Fonte para o agente que assume o papel de **cliente** (dono do negócio) e
cobra os resultados de cada arquitetura.

Cada arquitetura do roadmap ([`ROADMAP_ARQUITETURA_MULTICLOUD.md`](ROADMAP_ARQUITETURA_MULTICLOUD.md)) resolve **um problema
de negócio diferente**, escolhido pelo que ela faz melhor. O mesmo problema se repete nas 3 nuvens, para que a comparação da
Fase 4 seja justa (mesma pergunta, implementação diferente).

As regras citadas (RN-xx) estão em [`modelagem/01-regras-de-negocio.md`](modelagem/01-regras-de-negocio.md).

---

## Visão geral: o mesmo negócio em três escalas de tempo

| Arquitetura | Problema de negócio | Horizonte | Quem pergunta | Em uma frase |
|---|---|---|---|---|
| **Warehouse** | Fechamento financeiro e conciliação de repasses | Dia / mês | Financeiro | **Fecha a conta** |
| **Lakehouse** | Retenção do cliente e qualidade percebida | Meses de histórico | Produto / CRM | **Entende o porquê** |
| **Kappa** | Torre de controle operacional por cidade | Minutos | Operação | **Age agora** |

O que separa as três não é a tecnologia, é a pergunta. Se uma entrega começar a responder a pergunta de outra (por exemplo,
o Kappa calculando margem financeira, ou o Warehouse tentando ser tempo real), ela saiu do escopo.

---

## 1. Warehouse: fechamento financeiro e conciliação de repasses

### Problema

"Quanto a plataforma ganhou **de fato** em cada dia, cidade e restaurante, depois dos estornos? E quanto devemos a cada
restaurante e a cada motorista?" O número precisa ser **oficial**: exato em centavos, reproduzível e fechado por período.

### Perguntas que o cliente faz

1. Qual foi a margem da plataforma ontem, por cidade? E no mês?
2. Quanto foi estornado no período, quanto a plataforma assumiu e por qual motivo (cancelamento, incidente procedente,
   motorista impossibilitado)?
3. Qual o extrato do restaurante X no mês: itens vendidos, comissão retida, repasse devido?
4. Qual o extrato do motorista Y: repasses de entrega e gorjetas recebidas?
5. Quais os 10 restaurantes que mais geram margem, e os 10 que mais geram estorno?
6. A conta fecha? Soma dos componentes = valor pago; soma dos reembolsos ≤ valor pago.

### Indicadores

| Indicador | Definição | RN |
|---|---|---|
| GMV | Soma dos valores pagos (itens + taxa de entrega + taxa de serviço), sem gorjeta | RN-19, RN-22 |
| Receita líquida de estornos | GMV − reembolsos | RN-08, RN-21 |
| Margem da plataforma por pedido | comissão + taxa de serviço + parcela da entrega − custo do meio de pagamento − estornos assumidos | RN-29 |
| Repasse devido ao restaurante | itens do atendimento retirado − comissão | RN-29 |
| Repasse devido ao motorista | parcela fixa da taxa de entrega (entregue ou cliente ausente) | RN-29 |
| Gorjetas | valor por motorista, fora do pagamento | RN-22 |
| Custo de estorno assumido | estornos de incidente procedente e de motorista impossibilitado | RN-14, RN-30 |
| Imposto embutido | por componente, decomposição do bruto | RN-09, RN-33 |

### Critérios de aceite (o cliente só aprova se)

- As invariantes da RN-33 são verificadas como teste e passam: soma dos reembolsos ≤ valor pago; cancelamento total
  reembolsa exatamente o pago; reembolsado por item ≤ valor alocado; o resultado não depende da ordem dos cancelamentos.
- O valor de um pedido antigo **não muda** quando o produto ou o restaurante mudam depois (preço congelado, RN-32;
  dimensões com histórico, SCD2).
- Um extrato de restaurante e um de motorista conferem com a soma dos repasses do período.
- O mesmo período, consultado duas vezes, devolve o mesmo número.

### Fora do escopo

Liquidação com datas (D+1, D+30) e fluxo de caixa (RN-29 diz que repasse é obrigação reconhecida). Visão fiscal de imposto a
recolher (RN-01 reabre a decisão se for preciso).

---

## 2. Lakehouse: retenção do cliente e qualidade percebida

### Problema

"Por que o cliente para de pedir?" Entender quais experiências ruins (atraso, cancelamento parcial, incidente, restaurante
mal avaliado) antecedem o abandono, e quais restaurantes são a causa. Exige cruzar todos os domínios num histórico longo e
granular, inclusive dado semiestruturado (cardápio no MongoDB) e texto livre (comentário da avaliação).

### Perguntas que o cliente faz

1. De cada 100 clientes que fizeram o primeiro pedido em um mês, quantos voltaram em 30, 60 e 90 dias?
2. Quem teve atraso, incidente procedente ou cancelamento parcial volta menos do que quem não teve? Quanto menos?
3. Quais restaurantes têm a pior qualidade percebida, e isso aparece na nota, no cancelamento ou no atraso?
4. O que os comentários das avaliações ruins dizem? (temas: atraso, frio, item errado, embalagem...)
5. Quais clientes estão em risco de abandono hoje?
6. Seção ou destaque do cardápio tem relação com a nota do restaurante?

### Indicadores

| Indicador | Definição | RN |
|---|---|---|
| Recompra por coorte | % de clientes da coorte com novo pedido em 30/60/90 dias | RN-02 |
| Churn | cliente sem pedido há N dias (N é parâmetro) | — |
| Score de qualidade do restaurante | taxa de cancelamento, rejeição e atraso + média e **quantidade** de notas; avaliação ausente nunca conta como zero | RN-26 |
| Experiência ruim por pedido | atraso sobre o prazo prometido, cancelamento parcial, incidente procedente, não entregue | RN-10, RN-14, RN-28, RN-30 |
| Tema do comentário | classificação do texto livre da avaliação | RN-26 |
| Espera do motorista por restaurante | chegada → retirada, atribuída ao restaurante | RN-17 |

### Critérios de aceite

- As coortes fecham: todo cliente com pedido pertence a exatamente uma coorte (mês do primeiro pedido).
- A comparação "com experiência ruim × sem experiência ruim" mostra diferença de recompra (ver premissa do gerador abaixo).
- O score de qualidade mostra média **e** quantidade de avaliações, e não penaliza restaurante sem avaliação.
- É possível responder "como estava o pedido X no momento Y" (histórico de transições, RN-18).

### Etapa opcional

Modelo de risco de churn (tabela de features por cliente + modelo). É extensão, não critério de aceite: na AWS e na GCP não
há Databricks, e o custo de reproduzir lá é maior.

### Premissa do dado sintético

Se o gerador sorteia pedidos ao acaso, a análise de churn não encontra causa nenhuma. O gerador precisa de um **parâmetro**
que reduza a chance de o cliente voltar depois de atraso, incidente ou cancelamento parcial. Isso não é regra de negócio, é
premissa explícita do dado: o cliente deve saber que o efeito foi plantado e medir se o pipeline o recupera.

### Fora do escopo

Cupom e promoção (alavanca clássica de retenção): mexeriam na composição do valor (RN-19), na distribuição (RN-29) e no
rateio de estorno (RN-33). Fica como evolução.

---

## 3. Kappa: torre de controle operacional por cidade

### Problema

"Onde a operação está quebrando **agora**?" Detectar em minutos, por cidade, falta de motorista, restaurante que não
responde e pedido que vai estourar o prazo, a tempo de agir antes do cliente cancelar ou abrir incidente. Lê só do
barramento (Event Hub, Kinesis, Pub/Sub), nunca do storage batch.

### Perguntas que o cliente faz

1. Em cada cidade, nos últimos 5 minutos: quantos pedidos abertos e quantos motoristas livres?
2. Quais entregas estão aguardando motorista, e há quanto tempo?
3. Quais atendimentos estão perto dos 5 minutos de análise (vão ser rejeitados automaticamente)?
4. Quais atendimentos já passaram do tempo estimado + 50% (o cliente já pode cancelar)?
5. Quais pedidos vão estourar o prazo prometido de entrega?
6. Em quais restaurantes os motoristas estão esperando mais agora?

### Indicadores

| Indicador | Definição | RN |
|---|---|---|
| Oferta × demanda por cidade | pedidos abertos ÷ motoristas livres, janela de 5 min | RN-06, RN-35, RN-36 |
| Entregas aguardando atribuição | quantidade e tempo de espera | RN-06 |
| Atendimentos em risco de rejeição | em análise há mais de X min do limite de 5 | RN-28 |
| Atendimentos atrasados | acima do estimado + 50% de tolerância | RN-12, RN-28 |
| Pedidos em risco de prazo | tempo decorrido próximo do prazo prometido | RN-28 |
| Espera do motorista no restaurante | chegada sem retirada, em andamento | RN-17 |

### Critérios de aceite

- Os indicadores usam o **tempo do evento** (quando aconteceu), não o tempo de chegada no barramento, e tratam evento
  atrasado.
- Um atraso injetado no gerador aparece no painel em poucos minutos (o cliente define o limite aceitável).
- Nenhum dado vem do storage batch, exceto o dado de referência do restaurante (cópia do MongoDB), como o roadmap prevê.
- Os eventos de status vêm do histórico de transições (RN-18), não de comparação de fotos da tabela.

### Fora do escopo

Agir de volta na operação (reatribuir motorista, mudar preço). O Kappa **produz o sinal**; quem age é a operação.
Posição do motorista e distância (RN-35 deixa quilometragem fora da v1).

---

## Lacunas nas regras que estes objetivos expõem

Propostas, **ainda não formalizadas** como RN. A modelagem (L1a, L2) está com outro agente; formalizar segue
`/grill-with-docs` e, se afetar o modelo, ADR.

| # | Lacuna | Afeta | Proposta |
|---|---|---|---|
| 1 | Comissão é percentual fixo (RN-29): o histórico do restaurante não muda nada no dinheiro | Warehouse | Comissão por **plano do restaurante**, que muda no tempo; o repasse usa o plano vigente na compra (modelo real de planos com percentuais diferentes). |
| 2 | O valor da taxa de entrega não tem regra (RN-19 só diz que existe) | Warehouse, Kappa | Taxa base por cidade, congelada na compra. Opcional: multiplicador de demanda, que o Kappa calcula como sinal sem aplicar. |
| 3 | "Disponível" = turno aberto (RN-06): motorista em entrega conta como oferta | Kappa | Disponível = turno aberto **e** sem atribuição vigente (uma entrega por vez). |
| 4 | Recompra sem relação com a experiência | Lakehouse | Parâmetro do gerador (ver premissa do dado sintético na seção 2). |
| 5 | Cupom e promoção | Lakehouse | Fora da v1. |

---

## Como o agente-cliente usa este documento

- Fala como **dono do negócio**: pergunta em linguagem de negócio (as listas "Perguntas que o cliente faz"), não em termos
  de tecnologia.
- Aprova ou recusa uma entrega pelos **critérios de aceite** da arquitetura correspondente, pedindo a evidência (consulta,
  número, teste).
- Cobra que cada arquitetura responda **só a sua pergunta**; se uma entrega invadir o problema de outra, aponta.
- Não decide regra de negócio sozinho: uma lacuna nova vira proposta para o usuário, não regra.
- Todo dado é sintético; mesmo assim não pede nem exibe registros crus de clientes e motoristas (só contagens e agregados).
