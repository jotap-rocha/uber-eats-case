# Pedido de revisão adversarial (2ª rodada) — regras de negócio do "uber-eats-case"

Você é um revisor sênior cético (modelagem de dados, plataformas de marketplace/delivery de comida, sistemas financeiros e engenharia de dados). Abaixo está a **versão refinada** das regras de negócio de uma plataforma de delivery com pedidos de até dois restaurantes, e o contexto de uso. Esta é a **segunda rodada** de revisão: uma primeira rodada já apontou falhas, e várias regras mudaram em resposta. Ainda NÃO existe modelo conceitual, lógico nem físico. Seu trabalho é **contestar as regras**, não elogiá-las.

## O que fazer

1. Liste as **10 falhas, lacunas ou riscos mais graves**, ordenados por severidade (bloqueante / alta / média / baixa). Para cada um: o que está errado ou faltando (cite o número da regra, por exemplo RN-16), um cenário concreto de falha e a correção sugerida.
2. **Priorize o que mudou** (listado no Documento 2). Procure em especial:
   - **Máquina de estados completa:** atendimento (7 estados), pedido (derivado), atribuição do motorista, incidente e pagamento. Existe estado inalcançável, transição faltando ou combinação sem destino? Verifique a tabela de transições e a tabela de derivação (as duas estão ao final do Documento 1) contra as regras.
   - **Combinações de tempo:** análise de 5 minutos, preparo estimado com 50% de tolerância, avaliação de 20 minutos, confirmação automática de 10 minutos. O que acontece quando dois limites se sobrepõem, ou quando um evento ocorre exatamente no limite?
   - **Aritmética do dinheiro:** reembolso proporcional com centavos, imposto embutido por componente, taxa de entrega devolvida ou não, repasse na retirada versus estorno, cancelamentos sucessivos, margem da plataforma. Tente montar um exemplo numérico com dois restaurantes que quebre a soma.
   - **Motorista atribuído quando o primeiro atendimento fica pronto** (RN-06): consequências para espera, reatribuição, indisponibilidade e múltiplas retiradas.
   - **Contradições e ambiguidades entre regras** (cite os pares, por exemplo "RN-12 x RN-28").
   - **Implicações para dados** (CDC de bancos relacionais, histórico de transições, reconstrução do estado): apenas o que as **regras** exigem; o contrato técnico de eventos será definido na modelagem.
   - **Testabilidade:** regras que parecem verificáveis mas só podem ser verificadas de forma tautológica.
3. Aponte explicitamente os itens **[confirmar]** do Documento 2 com que você discorda, e diga qual seria a decisão melhor.
4. Termine com: (a) as **3 decisões que, se erradas, mais custariam caro de reverter**; (b) o que você **não** conseguiu avaliar por falta de informação.

## Regras de resposta

- **Não repita** os achados já tratados (lista no Documento 2) a menos que a correção aplicada esteja errada ou incompleta; nesse caso, explique por quê.
- Seja específico e curto; sem elogios genéricos. Se algo estiver bom, não comente.
- Não invente fatos sobre o projeto; se precisar supor, diga "suposição".
- Responda em português do Brasil.

---

# DOCUMENTO 1 — Regras de negócio (versão refinada, 2026-10-19)

## Atores

- **RN-01.** Os atores do negócio são **cliente**, **restaurante**, **motorista** e **plataforma** (cobra, repassa e arbitra). O **governo não é ator** do modelo: o imposto é um componente do pagamento (RN-09). Se a Gold vier a precisar de uma visão fiscal (imposto a recolher por período), a decisão é reaberta.

## Pedido, itens e restaurantes

- **RN-02.** Um pedido pertence a **exatamente um cliente**.
- **RN-03.** Um pedido pode ter itens de **mais de um restaurante**, no **máximo 2**, e os restaurantes têm de estar na **mesma cidade** (para facilitar a logística do entregador).
- **RN-04.** Um pedido tem **um ou mais itens**. Cada item referencia **um produto do cardápio de um restaurante**, com quantidade.
- **RN-05.** Para cada restaurante presente nos itens de um pedido existe um **atendimento** (um por restaurante e por pedido). O atendimento tem ciclo de vida próprio (em análise, aceito, em preparo, pronto para retirada e retirado; ou os terminais cancelado e rejeitado). O status do pedido é **derivado** dos atendimentos (RN-16).

## Motorista

- **RN-06.** Um pedido tem **no máximo um motorista**, mesmo com restaurantes diferentes. O motorista é atribuído quando o **primeiro atendimento fica pronto para retirada**: nesse momento o pedido ganha motorista. Nunca na criação, nem no aceite, de modo que não há viagem de ida a um restaurante que ainda está preparando.
- **RN-07.** O motorista pode ser **reatribuído** (por exemplo, se ele cancelar) enquanto **nenhum atendimento do pedido foi retirado**. A partir da **primeira retirada** em qualquer restaurante, o motorista fica travado no pedido.

## Cancelamento

- **RN-10.** O cancelamento é **parcial por atendimento**. Se um restaurante cancela ou rejeita o seu atendimento, os demais seguem e o pedido continua com os atendimentos restantes; o cliente recebe reembolso proporcional aos itens cancelados. Se **todos** os atendimentos forem cancelados ou rejeitados, o pedido inteiro passa a cancelado. Um cancelamento com decisão do cliente (pedido suspenso aguardando escolha) é uma evolução possível, fora do escopo atual.
- **RN-11.** Um pedido **só existe com o pagamento aprovado**. Pagamento recusado não gera pedido, então a plataforma não cancela pedido por recusa de pagamento.
- **RN-12.** O **cliente** só cancela um atendimento **até o status de análise** (inclusive). Depois do aceite do restaurante o cliente não cancela mais. Em ambos os casos de cancelamento do cliente há **devolução do pagamento** correspondente. A regra vale **por atendimento**: se o restaurante A ainda está em análise e o B já aceitou, o cliente cancela **só o A**. **Exceção:** depois do aceite, o cliente pode **solicitar o cancelamento legítimo** de um atendimento que está atrasado (para não ficar refém de um restaurante que não termina o preparo). O limite de atraso e o efeito no motorista estão na RN-28.
- **RN-13.** Depois que o atendimento chega ao restaurante e é aceito, **só o restaurante** pode cancelá-lo (por exemplo, falta de insumo durante o preparo), **até o fim do preparo**: um atendimento já **pronto não pode mais ser cancelado** (qualquer problema depois disso é incidente após a retirada). O motorista nunca cancela atendimento: desistir só dispara reatribuição (RN-07).
- **RN-14.** Após a retirada pelo motorista, o cliente só obtém devolução **em caso de incidente** (atraso, item errado, item faltando etc.), com devolução do pagamento correspondente. O incidente é a entidade que motiva essa devolução. O **incidente tem desfecho**: a **plataforma o analisa e o marca como procedente ou improcedente** (aberto → em análise → procedente ou improcedente). Só o incidente **procedente** gera a devolução. A plataforma arbitra incidentes, mas **não cancela pedido por conta própria**. No incidente procedente o cliente recebe **estorno completo** e a **plataforma assume o prejuízo**: o restaurante continua recebendo o seu repasse. O incidente **aponta item(ns) e quantidade**: o estorno é completo desses itens, mais a taxa de serviço e o imposto proporcionais. A taxa de entrega só é devolvida quando o problema é a própria entrega. O incidente **não altera o estado operacional** do atendimento retirado: gera um ajuste financeiro.
- **RN-27.** Quando dois eventos concorrem sobre o mesmo atendimento (por exemplo, o cliente cancela no mesmo instante em que o restaurante aceita), **vale o que a plataforma registrou primeiro**; o outro é recusado com aviso.

## Status do pedido e entrega

- **RN-16.** O status do pedido é **derivado** dos atendimentos **ativos** (não cancelados nem rejeitados). As condições abaixo são avaliadas **em ordem, e a primeira verdadeira vale** (assim são mutuamente exclusivas):
  1. nenhum atendimento ativo → pedido **cancelado**;
  2. todos os ativos retirados → pedido **a caminho** (a entrega começa aqui);
  3. algum ativo retirado (e nem todos) → pedido **em coleta**;
  4. todos os ativos prontos → pedido **pronto para retirada**;
  5. algum ativo pronto (e nem todos) → pedido **parcialmente pronto**;
  6. algum ativo em análise → pedido **em análise**;
  7. senão (todos aceitos ou em preparo) → pedido **em preparo**.

  A partir de **a caminho**, o estado do pedido segue **eventos do próprio pedido**, não dos atendimentos: **entregue** (o motorista finaliza), **concluído** (o cliente confirma ou passam 10 minutos, RN-24) ou **não entregue** (RN-30).
- **RN-17.** O motorista **vai recolher o primeiro atendimento** assim que ele está disponível e **aguarda** nos demais restaurantes enquanto ainda estiverem em preparo. A **entrega só começa quando todos os atendimentos ativos foram recolhidos**. O atendimento mais lento é, por definição, o gargalo do pedido.
- **RN-18.** Cada atendimento tem **status próprio, que muda de forma independente**, e o **cliente acompanha o status de cada atendimento** (incluindo a retirada de cada um), além do status geral do pedido. Os dois níveis têm histórico de transições.

## Entrega, conclusão e avaliação

- **RN-24.** O pedido é **entregue** quando o motorista finaliza a entrega, e **concluído** quando o cliente recebe e **confirma**. Se o cliente não confirmar, a entrega é **confirmada automaticamente 10 minutos depois** de o motorista finalizar a rota. Se houver problema na entrega e o cliente não recebe, ele abre um **incidente** que marca **falha na entrega**.
- **RN-25.** Se o motorista e o restaurante cumpriram a sua parte e o **cliente não retira o pedido**, não há devolução: o dinheiro permanece com a plataforma, o motorista e o restaurante.
- **RN-26.** Depois da entrega o cliente pode **avaliar** o **motorista** (uma avaliação por pedido) e cada **restaurante** (uma avaliação por atendimento). A avaliação é **opcional**, com **nota de 1 a 5** e **comentário livre opcional**. O prazo máximo para avaliar é de **20 minutos** após a finalização da entrega. Em seguida o cliente escolhe dar **gorjeta** (RN-22) ou não. A gorjeta independe da avaliação, **exceto** quando a nota dada ao motorista é **3 ou menor**: nesse caso a gorjeta é desconsiderada. Em pedido **não entregue** (RN-30), as avaliações e a gorjeta são desconsideradas.
- **RN-30.** Um pedido que não consegue ser entregue termina no estado terminal **não entregue**, com um **motivo**:
  - **cliente ausente** (registrado pelo motorista): **sem devolução**, conforme a RN-25;
  - **motorista impossibilitado** de continuar depois de recolher (registrado pela plataforma): **estorno total** ao cliente, assumido pela plataforma; o restaurante mantém o repasse.

  Se o pedido já foi marcado como entregue e o cliente diz que não recebeu, o estado não muda: o incidente da RN-14 gera só o ajuste financeiro, e é improcedente se o cliente estava ausente.

## Limites de tempo

Os valores abaixo são **parâmetros do gerador** (ajustáveis sem mudar as regras).

- **RN-28.** Limites de tempo do processo:
  - **Análise:** o restaurante tem **5 minutos** para responder. Passado o limite, o atendimento é **rejeitado automaticamente**, com estorno dos itens.
  - **Preparo:** cada atendimento tem um **tempo estimado de preparo**. Passando do estimado mais **50% de tolerância**, o atendimento está **atrasado** e o cliente pode **solicitar o cancelamento legítimo** (RN-12).
  - **Prazo prometido de entrega:** maior tempo estimado de preparo entre os atendimentos, mais o deslocamento (distância ÷ velocidade média), mais uma folga fixa. É o prazo usado para medir "entrega no prazo".
  - **Confirmação automática:** 10 minutos após o fim da rota (RN-24).
  - **Motorista no cancelamento por atraso:** se não resta atendimento a recolher, é **liberado**; se já recolheu outro atendimento, **segue com o que tem** e entrega só esse (a taxa de entrega não é devolvida, RN-21).

## Pagamento e imposto

- **RN-08.** Um pedido tem **um pagamento principal**. Reembolso é um **evento posterior ligado ao pagamento**, não outro pagamento.
- **RN-15.** **Toda tentativa de pagamento é registrada**, aprovada ou recusada. A tentativa pertence a um cliente e guarda valor, resultado, motivo da recusa (se houver) e momento. A tentativa **recusada** não tem pedido, porque o pedido não chegou a existir. A tentativa **aprovada** gera o **pagamento** e o **pedido**, e uma aprovação gera **no máximo um** pedido.
- **RN-09.** O imposto é um **componente do pagamento** (junto de taxa da plataforma, taxa do meio de pagamento e valor líquido). O imposto é calculado por uma **alíquota única** (percentual fixo, parâmetro do gerador) sobre o valor pago, embutida, e acompanha o reembolso na mesma proporção. É uma **simplificação deliberada do modelo**: no Brasil a tributação real varia por tipo de operação e por local (por exemplo ICMS estadual e ISS municipal), e isso não é reproduzido.

## Restaurante e cardápio

- **RN-23.** **Todo restaurante tem perfil** (cardápio e horários); restaurante sem perfil não recebe pedido. O **menu é só apresentação** dos produtos do restaurante e **referencia o produto** (`product_id`), que carrega nome e preço.

## Valor do pedido e reembolso

- **RN-19.** O valor pago pelo cliente é composto por: **itens** (preço × quantidade, por atendimento), **taxa de entrega** e **taxa de serviço** (cobrada pela plataforma, percentual sobre os itens). A gorjeta **não** compõe o valor do pedido (RN-22). O **imposto está embutido** nesses valores, não é somado ao total. A **comissão do restaurante** não é paga pelo cliente: é uma retenção da plataforma sobre os itens do restaurante, que aparece só no repasse.
- **RN-20.** A **taxa de entrega é uma só por pedido**, nunca rateada entre restaurantes (o rateio penalizaria o restaurante mais distante e beneficiaria o mais próximo).
- **RN-21.** No cancelamento parcial, o reembolso cobre os **itens do atendimento cancelado** mais a **taxa de serviço proporcional**; o imposto acompanha na mesma proporção. A **taxa de entrega não é reembolsada** enquanto houver ao menos um atendimento a entregar. Se **todos** os atendimentos forem cancelados, o reembolso é **total**, incluindo a taxa de entrega.
- **RN-22.** Existe **gorjeta**, opcional, em **valor livre**, paga **no final** (depois da entrega) e **direto ao motorista**. É um valor **à parte do pedido**: não entra no pagamento do pedido (RN-08), não passa por reembolso de itens e a plataforma não retém parte dela. Há **no máximo uma gorjeta por pedido**, e **só para pedidos entregues**, e é desconsiderada se a nota do motorista for 3 ou menor (RN-26). A gorjeta é um registro de valor já liquidado: não se modela recusa nem cancelamento dela, e ela **não é estornada**, nem em incidente procedente.

## Distribuição do dinheiro

Percentuais e valores são **parâmetros do gerador**. A liquidação com datas (D+1, D+30) fica fora do escopo: o repasse é um evento com valor devido e momento, sem fluxo de caixa.

- **RN-29.** Distribuição do valor de um pedido:
  - **Restaurante:** recebe os itens do seu atendimento menos a **comissão** (percentual fixo). O repasse é devido **na retirada** do atendimento.
  - **Motorista:** recebe uma **parcela fixa da taxa de entrega**, devida quando o pedido é **entregue**. O restante da taxa fica com a plataforma. A gorjeta (RN-22) é à parte e direta ao motorista.
  - **Plataforma:** fica com a comissão, a taxa de serviço e a parte da taxa de entrega que não vai ao motorista.
  - **Custo do meio de pagamento:** percentual sobre o valor pago, **custo da plataforma**, **não devolvido** em estorno.
  - **Incidente procedente** (RN-14): a plataforma arca com o estorno; restaurante e motorista mantêm o que têm a receber.
  - **Cliente ausente** (RN-25): restaurante e motorista mantêm o que têm a receber; sem devolução.
  - **Margem da plataforma por pedido** = comissão + taxa de serviço + parcela da entrega − custo do meio de pagamento − estornos assumidos.

## Regras transversais

- **RN-31.** O motorista de um pedido tem **histórico de atribuições**: cada atribuição, liberação e reatribuição é registrada com o momento. O motorista atual do pedido não substitui o histórico.
- **RN-32.** O item do pedido **guarda o nome do produto e o preço unitário da compra**. Alterar ou desativar o produto depois não muda pedidos já aprovados.
- **RN-33.** Valores monetários são exatos em **centavos**. O arredondamento é determinístico: cada parcela é calculada e **a última absorve a diferença**, de modo que a soma das partes é sempre o total. O imposto é guardado **por componente** (item, taxa de serviço, taxa de entrega). Invariantes: a soma dos reembolsos nunca excede o valor pago; o cancelamento de todos os atendimentos reembolsa exatamente o pagamento original.

## Tabelas de referência

Atendimento, transições permitidas (qualquer outra é inválida; o terminal não volta a estado ativo):

| De | Para | Quem |
|---|---|---|
| em análise | aceito | restaurante |
| em análise | rejeitado | restaurante, ou automático após 5 minutos (RN-28) |
| em análise | cancelado | cliente (RN-12) |
| aceito | em preparo | restaurante |
| aceito, em preparo | cancelado | restaurante (RN-13) ou cliente por atraso (RN-12, RN-28) |
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

---

# DOCUMENTO 2 — Contexto, o que mudou e itens a confirmar

## Contexto de uso

- **Projeto:** pipeline de engenharia de dados de portfólio que simula um aplicativo de delivery. **Todo dado é sintético** (gerado por um gerador de eventos); não há dado pessoal real.
- **Para que servem as regras:** definem (1) o gerador de dados, (2) o modelo conceitual, lógico e físico dos bancos transacionais de origem e (3) uma arquitetura medalhão (Bronze → Silver → Gold) alimentada por captura de mudanças (CDC). A Gold serve indicadores de delivery, como tempo em cada etapa, entrega no prazo, receita da plataforma, margem por pedido e qualidade por restaurante e por motorista.
- **Origens:** dois bancos relacionais com domínios separados (pedido e catálogo de um lado, pessoas de outro) e um banco de documentos para o perfil do restaurante. Não há chave estrangeira física: a integridade entre entidades é lógica.
- **Fora de escopo declarado:** governo como ator; tributação real por local e operação; múltiplas moedas; liquidação com datas (fluxo de caixa); cancelamento com decisão do cliente (pedido suspenso); recusa de gorjeta; cupons e descontos; pedido agendado.

## O que mudou desde a 1ª rodada (para você focar)

- RN-03: máximo de 2 restaurantes, mesma cidade.
- RN-05: atendimento com sete estados, separando **rejeitado** de **cancelado**.
- RN-06: motorista atribuído quando o **primeiro atendimento fica pronto** (antes: no aceite).
- RN-12 e RN-28: cliente pode pedir cancelamento de atendimento **atrasado**; limites de tempo (análise 5 min, preparo +50%, avaliação 20 min, confirmação automática 10 min).
- RN-13: restaurante só cancela até o fim do preparo (atendimento pronto não cancela).
- RN-14: incidente por **item e quantidade**, estorno completo, plataforma assume o prejuízo, sem mudar o estado do atendimento.
- RN-15: toda tentativa de pagamento registrada; RN-16: derivação reescrita com condições exclusivas e dois novos status; RN-24 e RN-30: conclusão, entrega e estado "não entregue"; RN-26: avaliação de motorista e restaurante, com regra da gorjeta; RN-29: distribuição do dinheiro; RN-31 a RN-33: regras transversais.

## Achados da 1ª rodada já tratados (não repetir)

- Condições 4 e 5 da derivação sobrepostas: corrigido (RN-16, ordem de precedência).
- Cancelamento após retirada misturado com ajuste financeiro: corrigido (RN-14).
- Histórico de atribuições do motorista, snapshot de preço e nome no item, toda tentativa de pagamento registrada, regra de centavos: incorporados (RN-31, RN-32, RN-15, RN-33).
- Motorista refém de restaurante atrasado: tratado por timeouts e cancelamento legítimo (RN-28, RN-12).
- Compensação de deslocamento ao motorista: **descartada** (o motorista só é atribuído quando há algo pronto, e atendimento pronto não cancela).
- Contrato técnico de eventos do CDC (ids, ordenação, deduplicação) e tratamento na Bronze/Silver/Gold: **adiado para a modelagem**, não é regra de negócio.
- Gorjeta mantida no escopo; imposto por alíquota única é simplificação deliberada; liquidação com datas está fora do escopo.

## Itens a confirmar

Pontos propostos e aceitos em linhas gerais, sem verificação de todos os detalhes:

1. **[confirmar] RN-26:** a gorjeta segue a mesma janela de 20 minutos da avaliação; a regra "nota 3 ou menor" refere-se à nota dada ao **motorista**.
2. **[confirmar] RN-28:** "atrasado" = preparo estimado + 50% de tolerância, e o cliente cancela sem arbitragem da plataforma.
3. **[confirmar] RN-30:** no estado "não entregue" por **motorista impossibilitado**, o estorno é total e assumido pela plataforma; não está definido se o motorista recebe a parcela da taxa de entrega nesse caso.
4. **[confirmar] RN-21 x RN-14:** a taxa de entrega só é devolvida quando o problema é a própria entrega; a regra do que é "problema de entrega" não foi detalhada.
5. **[confirmar] RN-29:** repasse ao restaurante devido **na retirada**, mesmo se depois o pedido virar "não entregue" ou houver incidente.
6. **[confirmar] RN-26:** a avaliação de restaurante só existe para atendimento **retirado** (não para cancelado ou rejeitado).
7. **[confirmar] RN-16:** o estado do pedido após "a caminho" depende só de eventos do pedido; o status "em coleta" cobre o caso em que um atendimento está retirado e o outro ainda em análise.
