# Pedido de revisão adversarial — regras de negócio do "uber-eats-case"

Você é um revisor sênior cético (modelagem de dados, plataformas de marketplace/delivery de comida, sistemas financeiros e engenharia de dados). Abaixo estão as **regras de negócio** de uma plataforma de delivery com pedidos de vários restaurantes, e o contexto de uso. Ainda NÃO existe modelo conceitual, lógico nem físico para estas regras: elas serão a base de todos. Seu trabalho é **contestar as regras**, não elogiá-las.

## O que fazer

1. Liste as **10 falhas, lacunas ou riscos mais graves**, ordenados por severidade (bloqueante / alta / média / baixa). Para cada um: o que está errado ou faltando (cite o número da regra, por exemplo RN-16), um cenário concreto de falha e a correção sugerida.
2. Procure em especial:
   - **Contradições e ambiguidades entre regras** (cite os pares, por exemplo "RN-12 x RN-14").
   - **Máquina de estados:** a derivação do status do pedido (RN-16) cobre todas as combinações de status de atendimentos? Existe combinação sem status (por exemplo, atendimentos em análise e já retirados ao mesmo tempo, ou cancelamento depois de prontos)? Há transições proibidas não declaradas?
   - **Dinheiro:** reembolso proporcional (taxa de serviço, imposto, arredondamento de centavos, soma das partes = total pago), taxa de entrega não reembolsada, reembolso por incidente (atendimento inteiro ou por item?), comissão e repasse do restaurante quando há cancelamento parcial.
   - **Motorista:** atribuição, liberação e reatribuição (RN-06, RN-07, RN-17), motorista esperando em um restaurante enquanto outro cancela, número de reatribuições, motorista indisponível.
   - **Incidente:** quem abre, prazo, incidente em pedido com cancelamento parcial, incidente por atendimento ou por pedido, reabertura, gorjeta depois de incidente.
   - **Concorrência e ordem de eventos:** o cliente cancela no mesmo instante em que o restaurante aceita; dois restaurantes mudam de estado ao mesmo tempo; evento duplicado ou fora de ordem; relógios diferentes entre os atores.
   - **Implicações para dados:** o que essas regras exigem de um pipeline de CDC e de uma camada analítica (histórico de transições, consistência entre o status do atendimento e o do pedido derivado, quais invariantes seriam testáveis).
   - **Escopo:** o que está nas regras mas deveria ser adiado, e o que não está e fará falta (por exemplo, avaliação, cupom, entrega malsucedida, pedido agendado).
   - **Testabilidade:** regras que parecem verificáveis mas não são, ou que só podem ser verificadas de forma tautológica.
3. Aponte explicitamente os itens marcados **[confirmar]** no Documento 2 com que você discorda, e diga qual seria a decisão melhor.
4. Termine com: (a) as **3 decisões que, se erradas, mais custariam caro de reverter** depois; (b) o que você **não** conseguiu avaliar por falta de informação.

## Regras de resposta

- Seja específico e curto; sem elogios genéricos. Se algo estiver bom, não comente.
- Não invente fatos sobre o projeto; se precisar supor, diga "suposição".
- Responda em português do Brasil.

---

# DOCUMENTO 1 — Regras de negócio (v. 2026-10-18)

## Atores

- **RN-01.** Os atores do negócio são **cliente**, **restaurante**, **motorista** e **plataforma** (cobra, repassa e arbitra). O **governo não é ator** do modelo: o imposto é um componente do pagamento (RN-09). Se a Gold vier a precisar de uma visão fiscal (imposto a recolher por período), a decisão é reaberta.

## Pedido, itens e restaurantes

- **RN-02.** Um pedido pertence a **exatamente um cliente**.
- **RN-03.** Um pedido pode ter itens de **mais de um restaurante**.
- **RN-04.** Um pedido tem **um ou mais itens**. Cada item referencia **um produto do cardápio de um restaurante**, com quantidade.
- **RN-05.** Para cada restaurante presente nos itens de um pedido existe um **atendimento** (um por restaurante e por pedido). O atendimento tem ciclo de vida próprio (aceite, preparo, pronto para retirada, retirado, cancelado). O status do pedido é **derivado** dos atendimentos (RN-16).

## Motorista

- **RN-06.** Um pedido tem **no máximo um motorista**, mesmo com restaurantes diferentes. O motorista é atribuído na **primeira aceitação**: assim que o primeiro restaurante aceita o seu atendimento, o pedido ganha motorista. Nunca na criação. Se todos os atendimentos aceitos forem depois cancelados pelo restaurante antes de qualquer retirada, o motorista é liberado (consequência da RN-07, a confirmar).
- **RN-07.** O motorista pode ser **reatribuído** (por exemplo, se ele cancelar) enquanto **nenhum atendimento do pedido foi retirado**. A partir da **primeira retirada** em qualquer restaurante, o motorista fica travado no pedido.

## Cancelamento

- **RN-10.** O cancelamento é **parcial por atendimento**. Se um restaurante cancela ou rejeita o seu atendimento, os demais seguem e o pedido continua com os atendimentos restantes; o cliente recebe reembolso proporcional aos itens cancelados. Se **todos** os atendimentos forem cancelados, o pedido inteiro passa a cancelado. Um cancelamento com decisão do cliente (pedido suspenso aguardando escolha) é uma evolução possível, fora do escopo atual.
- **RN-11.** Um pedido **só existe com o pagamento aprovado**. Pagamento recusado não gera pedido, então a plataforma não cancela pedido por recusa de pagamento.
- **RN-12.** O **cliente** só cancela um atendimento **até o status de análise** (inclusive). Depois do aceite do restaurante o cliente não cancela mais. Em ambos os casos de cancelamento do cliente há **devolução do pagamento** correspondente. A regra vale **por atendimento**: se o restaurante A ainda está em análise e o B já aceitou, o cliente cancela **só o A**.
- **RN-13.** Depois que o atendimento chega ao restaurante e é aceito, **só o restaurante** pode cancelá-lo (por exemplo, falta de insumo durante o preparo). O motorista nunca cancela atendimento: desistir só dispara reatribuição (RN-07).
- **RN-14.** Após a retirada pelo motorista, o cliente pode cancelar **apenas em caso de incidente** (atraso, item errado, item faltando etc.), com devolução do pagamento correspondente. O incidente é a entidade que motiva esse cancelamento. O **incidente tem desfecho**: a **plataforma o analisa e o marca como procedente ou improcedente** (aberto → em análise → procedente ou improcedente). Só o incidente **procedente** gera o cancelamento e a devolução. A plataforma arbitra incidentes, mas **não cancela pedido por conta própria**.

## Status do pedido e entrega

- **RN-16.** O status do pedido é **derivado** dos atendimentos **não cancelados**, avançando no ritmo do mais atrasado:
  1. todos cancelados → pedido cancelado;
  2. algum em análise → pedido em análise;
  3. nenhum em análise e ao menos um aceito ou em preparo → pedido em preparo;
  4. todos prontos ou já retirados → pedido pronto para retirada;
  5. todos retirados → pedido a caminho (a entrega começa aqui);
  6. entregue, depois concluído.
- **RN-17.** O motorista **vai recolher o primeiro atendimento** assim que ele está disponível e **aguarda** nos demais restaurantes enquanto ainda estiverem em preparo. A **entrega só começa quando todos os atendimentos não cancelados foram recolhidos**. O atendimento mais lento é, por definição, o gargalo do pedido.
- **RN-18.** Cada atendimento tem **status próprio, que muda de forma independente**, e o **cliente acompanha o status de cada atendimento** (incluindo a retirada de cada um), além do status geral do pedido. Os dois níveis têm histórico de transições.

## Pagamento e imposto

- **RN-08.** Um pedido tem **um pagamento principal**. Reembolso é um **evento posterior ligado ao pagamento**, não outro pagamento.
- **RN-15.** Toda **tentativa de pagamento recusada é registrada**, mesmo sem gerar pedido. A tentativa pertence a um cliente e guarda valor, motivo da recusa e momento. Não está ligada a um pedido, porque o pedido não chegou a existir.
- **RN-09.** O imposto é um **componente do pagamento** (junto de taxa da plataforma, taxa do meio de pagamento e valor líquido). O imposto é calculado por uma **alíquota única** (percentual fixo, parâmetro do gerador) sobre o valor pago, embutida, e acompanha o reembolso na mesma proporção. É uma **simplificação deliberada do modelo**: no Brasil a tributação real varia por tipo de operação e por local (por exemplo ICMS estadual e ISS municipal), e isso não é reproduzido.

## Restaurante e cardápio

- **RN-23.** **Todo restaurante tem perfil** (cardápio e horários); restaurante sem perfil não recebe pedido. O **menu é só apresentação** dos produtos do restaurante e **referencia o produto** (`product_id`), que carrega nome e preço.

## Valor do pedido e reembolso

- **RN-19.** O valor pago pelo cliente é composto por: **itens** (preço × quantidade, por atendimento), **taxa de entrega** e **taxa de serviço** (cobrada pela plataforma, percentual sobre os itens). A gorjeta **não** compõe o valor do pedido (RN-22). O **imposto está embutido** nesses valores, não é somado ao total. A **comissão do restaurante** não é paga pelo cliente: é uma retenção da plataforma sobre os itens do restaurante, que aparece só no repasse.
- **RN-20.** A **taxa de entrega é uma só por pedido**, nunca rateada entre restaurantes (o rateio penalizaria o restaurante mais distante e beneficiaria o mais próximo).
- **RN-21.** No cancelamento parcial, o reembolso cobre os **itens do atendimento cancelado** mais a **taxa de serviço proporcional**; o imposto acompanha na mesma proporção. A **taxa de entrega não é reembolsada** enquanto houver ao menos um atendimento a entregar. Se **todos** os atendimentos forem cancelados, o reembolso é **total**, incluindo a taxa de entrega.
- **RN-22.** Existe **gorjeta**, opcional, em **valor livre**, paga **no final** (depois da entrega) e **direto ao motorista**. É um valor **à parte do pedido**: não entra no pagamento do pedido (RN-08), não passa por reembolso de itens e a plataforma não retém parte dela. Há **no máximo uma gorjeta por pedido**, e **só para pedidos entregues**. A gorjeta é um registro de valor já liquidado: não se modela recusa nem cancelamento dela.

---

# DOCUMENTO 2 — Contexto e itens a confirmar

## Contexto de uso

- **Projeto:** pipeline de engenharia de dados de portfólio que simula um aplicativo de delivery. **Todo dado é sintético** (gerado por um gerador de eventos); não há dado pessoal real.
- **Para que servem as regras:** definem (1) o gerador de dados, (2) o modelo conceitual, lógico e físico dos bancos transacionais de origem e (3) uma arquitetura medalhão (Bronze → Silver → Gold) alimentada por captura de mudanças (CDC). A Gold serve indicadores de delivery, como tempo em cada etapa, cumprimento de prazo de entrega, receita da plataforma, margem por pedido e qualidade por restaurante e por motorista.
- **Origens:** três bancos (dois relacionais com domínios separados: pedido e catálogo de um lado, pessoas de outro; e um banco de documentos para o perfil do restaurante). Não há chave estrangeira física: a integridade entre entidades é lógica.
- **Fora de escopo declarado:** governo como ator; tributação real por local e operação; múltiplas moedas; cancelamento com decisão do cliente (pedido suspenso); recusa de gorjeta; entrega malsucedida como processo próprio.

## Estado atual do dado (contradiz as regras e será regenerado)

- O gerador atribui o motorista na criação do pedido (contradiz RN-06).
- Cada pedido tem um único restaurante (contradiz RN-03).
- Existem pagamentos `pending` e `failed` ligados a pedido (contradiz RN-11 e RN-15).
- Não há atendimento nem cancelamento. Todo pedido percorre: criado → em análise → aceito → preparando → pronto para retirada → retirado → a caminho → entregue → concluído.
- O perfil de restaurante cobre menos restaurantes que o cadastro, e o menu não referencia produto (contradiz RN-23).

## Itens a confirmar

Pontos que foram propostos e aceitos em linhas gerais, mas sem verificação de todos os detalhes:

1. **[confirmar] RN-06:** a liberação do motorista quando todos os atendimentos aceitos são cancelados antes da retirada.
2. **[confirmar] RN-16:** a tabela de derivação do status do pedido. O princípio ("no ritmo do mais atrasado") foi aceito; cada linha e as combinações mistas não foram verificadas.
3. **[confirmar] RN-21:** a proporcionalidade da taxa de serviço e do imposto no reembolso parcial, e a regra de que a taxa de entrega não é reembolsada no cancelamento parcial.
4. **[confirmar] RN-14:** a devolução por incidente procedente cobre o atendimento inteiro, o pedido inteiro ou só o item afetado? **Não foi definido.**
5. **[confirmar] RN-12:** "até a análise (inclusive)" inclui o estado inicial do pedido (recém-criado)? E o que acontece com o reembolso quando o cliente cancela um atendimento mas há tentativas de pagamento prévias?
6. **[confirmar] RN-17:** o que significa "disponível" para o atendimento a ser recolhido (pronto) e o que acontece se o motorista chega antes de o atendimento estar pronto.
