# 01 — Regras de negócio

Etapa 1 do fluxo de modelagem: regras de negócio → adversarial → refinamento (opcional) → modelagem conceitual → lógica → física → regeração dos dados.

**Status:** regras fechadas após duas rodadas adversariais (levantamento via `/grill-with-docs`, 2026-10-18 e 2026-10-19).
Este documento descreve o negócio, não o banco. Qual tabela mora em qual banco é assunto da
[ADR 006](../../../docs/adr/006-inversao-de-dominios-entre-oracle-e-postgres.md).

## Atores

- **RN-01.** Os atores do negócio são **cliente**, **restaurante**, **motorista** e **plataforma** (cobra, repassa e arbitra).
  O **governo não é ator** do modelo: o imposto é um componente do pagamento (RN-09). Se a Gold vier a precisar de uma
  visão fiscal (imposto a recolher por período), a decisão é reaberta.

## Pedido, itens e restaurantes

- **RN-02.** Um pedido pertence a **exatamente um cliente**.
- **RN-03.** Um pedido pode ter itens de **mais de um restaurante**, no **máximo 2**, e os restaurantes têm de estar na
  **mesma cidade** (para facilitar a logística do entregador). "Restaurante" é a **unidade física de retirada**, e a cidade é uma
  **referência geográfica canônica** (identificador), nunca o nome em texto.
- **RN-04.** Um pedido tem **um ou mais itens**. Cada item referencia **um produto do cardápio de um restaurante**, com quantidade.
- **RN-05.** Para cada restaurante presente nos itens de um pedido existe um **atendimento** (um por restaurante e por pedido).
  O atendimento tem ciclo de vida próprio (em análise, aceito, em preparo, pronto para retirada e retirado; ou os terminais cancelado e rejeitado). O status do pedido é
  **derivado** dos atendimentos (RN-16).

## Motorista

- **RN-06.** Um pedido tem **no máximo um motorista**, mesmo com restaurantes diferentes. O motorista é atribuído quando o
  **primeiro atendimento fica pronto para retirada**: nesse momento o pedido ganha motorista. Nunca na criação, nem no aceite,
  de modo que não há viagem de ida a um restaurante que ainda está preparando. O "primeiro atendimento" é o **primeiro a
  ficar pronto**; em empate vale o de menor identificador. Se não há motorista disponível, o pedido **aguarda atribuição**.
- **RN-07.** O motorista pode ser **reatribuído** (por exemplo, se ele cancelar) enquanto **nenhum atendimento do pedido
  foi retirado**. A partir da **primeira retirada** em qualquer restaurante, o motorista fica travado no pedido; se ficar impossibilitado depois
  disso, o destino é o estado **não entregue** (RN-30). Depois de **3 desistências** de motoristas, a atribuição seguinte não
  pode mais ser desfeita antes da retirada (parâmetro do gerador).

## Cancelamento

- **RN-10.** O cancelamento é **parcial por atendimento**. Se um restaurante cancela ou rejeita o seu atendimento, os demais
  seguem e o pedido continua com os atendimentos restantes; o cliente recebe reembolso proporcional aos itens cancelados.
  Se **todos** os atendimentos forem cancelados ou rejeitados, o pedido inteiro passa a cancelado. Um cancelamento com decisão do
  cliente (pedido suspenso aguardando escolha) é uma evolução possível, fora do escopo atual.
- **RN-11.** Um pedido **só existe com o pagamento aprovado**. Pagamento recusado não gera pedido, então a plataforma
  não cancela pedido por recusa de pagamento.
- **RN-12.** O **cliente** só cancela um atendimento **até o status de análise** (inclusive). Depois do aceite do restaurante
  o cliente não cancela mais. Em ambos os casos de cancelamento do cliente há **devolução do pagamento** correspondente.
  A regra vale **por atendimento**: se o restaurante A ainda está em análise e o B já aceitou, o cliente cancela **só o A**.
  **Exceção:** depois do aceite, o cliente pode **solicitar o cancelamento legítimo** de um atendimento que está atrasado (para
  não ficar refém de um restaurante que não termina o preparo). O limite de atraso e o efeito no motorista estão na RN-28. A condição de atraso é **objetiva** (sem
  arbitragem), o cancelamento é registrado com o motivo **atraso do restaurante** e só é possível enquanto o atendimento está
  aceito ou em preparo: se o restaurante registrar pronto antes (RN-27), o cancelamento deixa de ser permitido.
- **RN-13.** Depois que o atendimento chega ao restaurante e é aceito, **só o restaurante** pode cancelá-lo (por exemplo,
  falta de insumo durante o preparo), **até o fim do preparo**: um atendimento já **pronto não pode mais ser cancelado**
  (qualquer problema depois disso é incidente após a retirada). O motorista nunca cancela atendimento: desistir só dispara reatribuição (RN-07).
- **RN-14.** Após a retirada pelo motorista, o cliente só obtém devolução **em caso de incidente** (atraso, item errado,
  item faltando etc.), com devolução do pagamento correspondente. O incidente é a entidade que motiva essa devolução.
  O **incidente tem desfecho**: a **plataforma o analisa e o marca como procedente ou improcedente** (aberto → em análise →
  procedente ou improcedente). Só o incidente **procedente** gera a devolução. A plataforma arbitra incidentes,
  mas **não cancela pedido por conta própria**. No incidente procedente o cliente recebe **estorno completo** e a **plataforma
  assume o prejuízo**: o restaurante continua recebendo o seu repasse. O incidente **aponta item(ns) e quantidade**: o estorno é
  completo desses itens, mais a taxa de serviço e o imposto proporcionais. A taxa de entrega só é devolvida quando o problema
  é a própria entrega. O incidente **não altera o estado operacional** do atendimento retirado: gera um ajuste financeiro.
  Regras do incidente: pode ser aberto até **24 horas** após a entrega (parâmetro); a quantidade reembolsada por item, somando
  todos os incidentes, nunca excede a quantidade comprada; um incidente decidido não é reaberto na v1. O **motivo** define o
  efeito na taxa de entrega: **item faltando, item errado e qualidade do alimento** não a devolvem; **atraso procedente,
  pedido não recebido e motorista impossibilitado** a devolvem.
- **RN-27.** Quando dois eventos concorrem sobre o mesmo atendimento ou o mesmo pedido (por exemplo, entregue e não entregue, ou o cliente cancela no mesmo instante em que o
  restaurante aceita), **vale o que a plataforma registrou primeiro**; o outro é recusado com aviso.
- **RN-34.** Se um restaurante **cancela ou rejeita** o seu atendimento, o cliente pode **cancelar o outro atendimento enquanto
  ele ainda não estiver pronto**, sem pedido suspenso (evita que o cliente fique obrigado a um atendimento menor e ao frete
  inteiro). Se os dois acabam cancelados, o reembolso é total (RN-21).

## Status do pedido e entrega

- **RN-16.** O status do pedido é **derivado** dos atendimentos **ativos** (não cancelados nem rejeitados). As condições abaixo são
  avaliadas **em ordem, e a primeira verdadeira vale** (assim são mutuamente exclusivas):
  1. nenhum atendimento ativo → pedido **cancelado**;
  2. todos os ativos retirados → pedido **a caminho** (a entrega começa aqui);
  3. algum ativo retirado (e nem todos) → pedido **em coleta**;
  4. todos os ativos prontos → pedido **pronto para retirada**;
  5. algum ativo pronto (e nem todos) → pedido **parcialmente pronto**;
  6. algum ativo em análise → pedido **em análise**;
  7. senão (todos aceitos ou em preparo) → pedido **em preparo**.
  A partir de **a caminho**, o estado do pedido segue **eventos do próprio pedido**, não dos atendimentos: **entregue** (o
  motorista finaliza), **concluído** (o cliente confirma ou passam 10 minutos, RN-24) ou **não entregue** (RN-30).
- **RN-17.** O motorista **vai recolher o primeiro atendimento** assim que ele está disponível e **aguarda** nos demais restaurantes
  enquanto ainda estiverem em preparo. A **entrega só começa quando todos os atendimentos ativos foram recolhidos**.
  O atendimento mais lento é, por definição, o gargalo do pedido.
  O tempo de espera do motorista em cada restaurante é um evento medido e atribuído ao restaurante.
- **RN-18.** Cada atendimento tem **status próprio, que muda de forma independente**, e o **cliente acompanha o status de
  cada atendimento** (incluindo a retirada de cada um), além do status geral do pedido. Os dois níveis têm histórico de
  transições.

## Entrega, conclusão e avaliação

- **RN-24.** O pedido é **entregue** quando o motorista finaliza a entrega, e **concluído** quando o cliente recebe e **confirma**. Se o cliente não confirmar, a entrega é **confirmada automaticamente
  10 minutos depois** de o motorista finalizar a rota.
  Se houver problema na entrega e o cliente não recebe, ele abre um **incidente** que marca **falha na entrega**.
- **RN-25.** Se o motorista e o restaurante cumpriram a sua parte e o **cliente não retira o pedido**, não há devolução: o
  dinheiro permanece com a plataforma, o motorista e o restaurante.
- **RN-26.** Depois da entrega o cliente pode **avaliar** o **motorista** (uma avaliação por pedido) e cada **restaurante** (uma
  avaliação por atendimento). A avaliação é **opcional**, com **nota de 1 a 5** e **comentário livre opcional** (campo que abre
  espaço para classificação por ML ou LLM no futuro). O prazo máximo para avaliar é de **20 minutos** após a finalização da
  entrega. Em seguida o cliente escolhe dar **gorjeta** (RN-22) ou não. A gorjeta independe da avaliação, **exceto** quando a
  nota dada ao motorista é **3 ou menor**: nesse caso a **opção de gorjeta não é oferecida**. Uma gorjeta já dada nunca é
  invalidada depois. O cliente pode pular a avaliação e dar gorjeta. Avaliação e gorjeta compartilham o mesmo prazo de 20 minutos
  (limite inclusivo). Em pedido **não entregue** (RN-30), as
  avaliações e a gorjeta são desconsideradas.
  A avaliação do restaurante só existe para atendimento **retirado** de pedido entregue. Na Gold, a qualidade do restaurante
  considera também a **taxa de cancelamento, rejeição e atraso**, e avaliação ausente **nunca conta como zero** (mostrar
  quantidade e média).
- **RN-30.** Um pedido que não consegue ser entregue termina no estado terminal **não entregue**, com um **motivo**:
  - **cliente ausente** (registrado pelo motorista): **sem devolução**, conforme a RN-25;
  - **motorista impossibilitado** de continuar depois de recolher (registrado pela plataforma): **estorno total** ao cliente,
    assumido pela plataforma; o restaurante mantém o repasse dos atendimentos já retirados.
  Se o pedido já foi marcado como entregue e o cliente diz que não recebeu, o estado não muda: o incidente da RN-14 gera só o
  ajuste financeiro, e é improcedente se o cliente estava ausente. Na Gold, o incidente procedente de falha na entrega conta como falha
  logística, embora o estado do pedido permaneça entregue.

## Limites de tempo

Os valores abaixo são **parâmetros do gerador** (ajustáveis sem mudar as regras).

- **RN-28.** Limites de tempo do processo:
  - **Análise:** o restaurante tem **5 minutos**, contados do envio do atendimento ao restaurante, para responder. O prazo é
    validado no próprio comando: um aceite depois do limite é recusado. Passado o limite, o atendimento é **rejeitado automaticamente**,
    com estorno dos itens.
  - **Preparo:** cada atendimento tem um **tempo estimado até ficar pronto**, fixado no aceite e imutável, e o relógio começa no **aceite**. Passando do estimado mais **50% de tolerância**, o
    atendimento está **atrasado** e o cliente pode **solicitar o cancelamento legítimo** (RN-12).
  - **Prazo prometido de entrega:** maior tempo estimado entre os atendimentos, mais o deslocamento da rota (restaurante → restaurante, quando há dois, e último restaurante → cliente, distância ÷
    velocidade média), mais uma folga fixa. É o prazo usado para medir "entrega no prazo".
  - **Confirmação automática:** 10 minutos após o fim da rota (RN-24). Um incidente aberto nesse intervalo não impede a
    conclusão automática. A confirmação manual e a automática são **duas causas da mesma transição**.
  - **Fronteiras:** todo limite é validado no próprio comando, não só por um agendador; no limite exato vale a RN-27.
  - **Motorista no cancelamento por atraso:** se não resta atendimento a recolher, é **liberado**; se já recolheu outro atendimento, **segue com
    o que tem** e entrega só esse (a taxa de entrega não é devolvida, RN-21).

## Pagamento e imposto

- **RN-08.** Um pedido tem **um pagamento principal**. Reembolso é um **evento posterior ligado ao pagamento**, não outro pagamento.
- **RN-15.** **Toda tentativa de pagamento é registrada**, aprovada ou recusada. A tentativa pertence a uma **intenção de compra (checkout)** de um cliente e guarda valor,
  resultado, motivo da recusa (se houver) e momento. A tentativa **recusada** não tem pedido, porque o pedido não chegou a
  existir. A tentativa **aprovada** gera o **pagamento** e o **pedido**, e uma intenção de compra gera **no máximo um** pedido e um pagamento principal, mesmo que a aprovação seja repetida.
- **RN-09.** O imposto é um **componente do pagamento** (junto de taxa da plataforma, taxa do meio de pagamento e valor líquido).
  O imposto é calculado por uma **alíquota única** (percentual fixo, parâmetro do gerador) sobre o valor pago, embutida, e
  acompanha o reembolso na mesma proporção. É uma **simplificação deliberada do modelo**: no Brasil a tributação real varia
  por tipo de operação e por local (por exemplo ICMS estadual e ISS municipal), e isso não é reproduzido.

## Restaurante e cardápio

- **RN-23.** **Todo restaurante tem perfil** (cardápio e horários); restaurante sem perfil não recebe pedido. O **menu é só
  apresentação** dos produtos do restaurante e **referencia o produto** (`product_id`), que carrega nome e preço.

## Valor do pedido e reembolso

- **RN-19.** O valor pago pelo cliente é composto por: **itens** (preço × quantidade, por atendimento), **taxa de entrega**,
  e **taxa de serviço** (cobrada pela plataforma, percentual sobre os itens). A gorjeta **não** compõe o valor do pedido (RN-22). O **imposto está embutido**
  nesses valores, não é somado ao total. A **comissão do restaurante** não é paga pelo cliente: é uma retenção da plataforma
  sobre os itens do restaurante, que aparece só no repasse.
- **RN-20.** A **taxa de entrega é uma só por pedido**, nunca rateada entre restaurantes (o rateio penalizaria o restaurante
  mais distante e beneficiaria o mais próximo).
- **RN-21.** No cancelamento parcial, o reembolso cobre os **itens do atendimento cancelado** mais a **taxa de serviço
  proporcional**; o imposto acompanha na mesma proporção. A **taxa de entrega não é reembolsada** enquanto houver ao menos um
  atendimento a entregar. Se **todos** os atendimentos forem cancelados, o reembolso é **total**, incluindo a taxa de entrega.
- **RN-22.** Existe **gorjeta**, opcional, em **valor livre**, paga **no final** (depois da entrega) e **direto ao motorista**.
  É um valor **à parte do pedido**: não entra no pagamento do pedido (RN-08), não passa por reembolso de itens e a plataforma
  não retém parte dela. Há **no máximo uma gorjeta por pedido**, e **só para pedidos entregues**, e não é oferecida se a nota do motorista for 3 ou menor (RN-26). O valor tem **mínimo positivo e máximo**, definidos como parâmetros. A gorjeta é um registro de
  valor já liquidado: não se modela recusa nem cancelamento dela, e ela **não é estornada**, nem em incidente procedente.

## Distribuição do dinheiro

Percentuais e valores são **parâmetros do gerador**. A liquidação com datas (D+1, D+30) fica fora do escopo: o repasse é um
evento com valor devido e momento, sem fluxo de caixa.

- **RN-29.** Distribuição do valor de um pedido:
  - **Restaurante:** recebe os itens do seu atendimento menos a **comissão** (percentual fixo). O repasse é devido **na retirada**
    do atendimento, e só de atendimento **efetivamente retirado**; "devido" é obrigação reconhecida, não dinheiro liquidado.
  - **Motorista:** recebe uma **parcela fixa da taxa de entrega**, devida quando o pedido é **entregue** ou quando a entrega não se completa por **cliente ausente** (tentativa válida); **não** é
    devida se o motorista fica impossibilitado (RN-30). O restante da taxa fica
    com a plataforma. A gorjeta (RN-22) é à parte e direta ao motorista.
  - **Plataforma:** fica com a comissão, a taxa de serviço e a parte da taxa de entrega que não vai ao motorista.
  - **Custo do meio de pagamento:** percentual sobre o valor pago, **custo da plataforma**, **não devolvido** em estorno.
  - **Incidente procedente** (RN-14): a plataforma arca com o estorno; restaurante e motorista mantêm o que têm a receber.
  - **Cliente ausente** (RN-25): restaurante e motorista mantêm o que têm a receber; sem devolução.
  - **Margem da plataforma por pedido** = comissão + taxa de serviço + parcela da entrega − custo do meio de pagamento − estornos
    assumidos.

## Regras transversais (da revisão adversarial)

- **RN-31.** O motorista de um pedido tem **histórico de atribuições**: cada atribuição, liberação e reatribuição é registrada com
  o momento. O motorista atual do pedido não substitui o histórico.
- **RN-32.** O item do pedido **guarda o nome do produto e o preço unitário da compra**. Alterar ou desativar o produto depois
  não muda pedidos já aprovados. O item guarda também o **identificador do
  produto**, o **restaurante vendedor**, a quantidade e o total contratado.
- **RN-33.** Valores monetários são exatos em **centavos**. O arredondamento é determinístico: cada parcela é calculada e **a
  última absorve a diferença**, de modo que a soma das partes é sempre o total. O imposto é guardado **por componente** (item,
  taxa de serviço, taxa de entrega). Invariantes: a soma dos reembolsos nunca excede o valor pago; o cancelamento de todos os
  atendimentos reembolsa exatamente o pagamento original; o reembolsado acumulado por item nunca excede o valor alocado a ele.
  O imposto é **decomposição** do valor bruto (alíquota efetiva sobre o valor bruto de cada componente), **nunca um acréscimo** ao
  reembolso. A alocação original por atendimento e componente é **congelada na compra** e não é recalculada a cada cancelamento.
  O resultado financeiro final **não depende da ordem** dos cancelamentos.

## Tabelas de referência

Atendimento, transições permitidas (qualquer outra é inválida; o terminal não volta a estado ativo):

| De | Para | Quem |
|---|---|---|
| em análise | aceito | restaurante |
| em análise | rejeitado | restaurante, ou automático após 5 minutos (RN-28) |
| em análise | cancelado | cliente (RN-12) |
| aceito | em preparo | restaurante |
| aceito, em preparo | cancelado | restaurante (RN-13), cliente por atraso (RN-12, RN-28), ou cliente quando o outro atendimento foi cancelado ou rejeitado pelo restaurante (RN-34) |
| em preparo | pronto | restaurante |
| pronto | retirado | motorista |
| pronto, retirado | cancelado | **não permitido** (RN-13, RN-14) |

Pedido com **dois atendimentos**, derivação do status (RN-16). Nas linhas de um só ativo, o outro está cancelado ou rejeitado.

| Atendimentos | Status do pedido |
|---|---|
| ambos cancelados/rejeitados | cancelado |
| um ativo: em análise | em análise |
| um ativo: aceito ou em preparo | em preparo |
| um ativo: pronto | pronto para retirada |
| um ativo: retirado | a caminho |
| análise + análise, análise + aceito, análise + preparo | em análise |
| análise + pronto | parcialmente pronto |
| análise + retirado | em coleta |
| aceito/preparo + aceito/preparo | em preparo |
| aceito/preparo + pronto | parcialmente pronto |
| aceito/preparo + retirado | em coleta |
| pronto + pronto | pronto para retirada |
| pronto + retirado | em coleta |
| retirado + retirado | a caminho |

Pedido, transições depois de **a caminho** (dirigidas por eventos do pedido, não pelos atendimentos). Reclamação posterior a
entregue ou concluído gera incidente e ajuste financeiro, sem mudar o estado.

| De | Para | Condição |
|---|---|---|
| a caminho | entregue | o motorista finaliza a entrega |
| a caminho | não entregue | falha registrada antes da entrega (RN-30) |
| entregue | concluído | confirmação do cliente **ou** confirmação automática (mesma transição, duas causas) |
| concluído, não entregue | qualquer | **proibido** (terminais) |

## Pendências

- Estado atual do dado, a corrigir na regeração: o gerador atribui motorista na criação do pedido (contradiz RN-06), modela
  um único restaurante por pedido (contradiz RN-03), gera pagamentos `pending`/`failed` ligados a pedido (contradiz RN-11 e
  RN-15), não tem atendimento nem cancelamento, e o seed do perfil tem 500 fixo e menu sem `product_id` (contradiz RN-23).
- **Decisões abertas:** nenhuma de regra de negócio. O comentário livre da avaliação exige, na geração, um gerador de texto
  sintético (por exemplo, frases por faixa de nota).
- **Próxima etapa:** regras fechadas após duas rodadas adversariais; seguir para a modelagem conceitual (exploratória), que
  deve partir de `MODELO_CONCEITUAL_UBER_EATS.md` (entidades já existentes: recibo, turno,
  incidente, avaliação, entrega).
