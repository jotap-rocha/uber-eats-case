Revisão adversarial — uber-eats-case (2ª rodada)
Veredito: houve correções importantes, mas eu ainda não congelaria as regras para iniciar a modelagem lógica. A tabela de derivação pré-entrega melhorou bastante; os problemas mais graves agora estão nas fronteiras entre operação, tempo e dinheiro.
Há uma distinção importante: a máquina de estados dos atendimentos e a tabela de combinações do pedido são praticamente completas para o limite de dois restaurantes. Isso não significa que o ciclo de vida inteiro do pedido esteja fechado.
1. As 10 falhas, lacunas e riscos mais graves
1. [BLOQUEANTE] RN-16, RN-24 e RN-30 — A máquina de estados do pedido ainda não está completamente fechada
O que mudou e está resolvido: a tabela da RN-16 cobre as combinações dos cinco estados ativos, considerando um ou dois atendimentos. Também resolve corretamente a precedência entre retirado + análise e os demais estados mistos.
Não considero necessário reescrever essa tabela.
O problema restante: depois de a caminho, o pedido passa a depender de eventos próprios, mas não existe uma tabela formal de transições para essa segunda parte do ciclo.
Há ainda uma ambiguidade entre RN-24 e RN-30:
- RN-24 diz que, se houver problema na entrega e o cliente não receber, ele abre um incidente que marca falha na entrega.
- RN-30 define não entregue como estado terminal, com motivos específicos.
- RN-30 também diz que, se já estiver entregue, o pedido não muda de estado quando o cliente disser que não recebeu.
Cenário de falha:
O pedido está a caminho. O motorista chega ao endereço, não encontra o cliente e registra ausência. Simultaneamente, outro processo recebe uma confirmação de entrega.
Qual evento prevalece? O pedido fica não entregue ou entregue?
A RN-27 só estabelece precedência para eventos concorrentes sobre o mesmo atendimento. Não resolve a concorrência de eventos próprios do pedido.
Outro cenário: o motorista registra entregue, mas o cliente não recebe. O pedido permanece entregue, porém existe um incidente. Isso precisa ser inequivocamente diferente de uma entrega que falhou antes de ser registrada como entregue.
Correção:
Formalizar a segunda máquina de estados:
Estado atual	Próximo estado	Condição
A caminho	Entregue	Motorista finaliza com sucesso
A caminho	Não entregue	Falha registrada antes da entrega
Entregue	Concluído	Confirmação do cliente ou timeout de 10 min
Entregue	Concluído	Confirmação automática
Concluído	Outros estados	Proibido
Não entregue	Outros estados	Proibido
A confirmação manual e a automática devem ser duas causas da mesma transição, não duas transições diferentes.
Também definir explicitamente que reclamação posterior a entregue ou concluído produz incidente e ajuste financeiro, sem retroagir o estado operacional.
Resultado da verificação: a tabela de atendimentos está suficientemente coberta no escopo atual; o fechamento do pedido ainda não.
2. [BLOQUEANTE] RN-09, RN-19, RN-21 e RN-33 — O dinheiro ainda pode ser contado duas vezes
O problema: a regra diz simultaneamente que o imposto está embutido, que é armazenado por componente e que acompanha proporcionalmente o reembolso. Não está suficientemente explícito se o imposto informado no reembolso é uma decomposição do valor devolvido ou um valor adicional.
A regra dos centavos também não determina completamente a ordem de distribuição dos resíduos entre componentes e atendimentos.
Exemplo com dois restaurantes:
Suponha:
Componente	Valor
Itens do restaurante A	R$ 33,33
Itens do restaurante B	R$ 66,67
Taxa de serviço (10%)	R$ 10,00
Taxa de entrega	R$ 9,99
Total pago	R$ 119,99
A taxa de serviço é alocada em R$ 3,33 para A e R$ 6,67 para B.
Agora A é cancelado. O reembolso bruto correspondente é R$ 36,66, incluindo a parcela de imposto embutida nesse valor.
Suponha uma interpretação incorreta, mas possível na implementação, em que o sistema adiciona novamente o imposto proporcional de R$ 3,67. O primeiro reembolso passa a R$ 40,33.
Depois B é cancelado. O restante bruto, incluindo a taxa de entrega, é R$ 83,33. Acrescentando novamente R$ 8,33 de imposto, o segundo reembolso é R$ 91,66.
Resultado:
\[
40,33 + 91,66 = 131,99
\]

O total devolvido excede os R$ 119,99 pagos.
O exemplo não afirma que essa seja a intenção da regra: demonstra que o contrato precisa impedir expressamente essa interpretação.
Outro problema numérico: com quatro componentes de R$ 0,05, R$ 0,05, R$ 0,01 e R$ 0,05, a 10% sobre o valor bruto, o imposto total é R$ 0,016, arredondado para R$ 0,02. Arredondar individualmente os impostos dos componentes pode produzir R$ 0,03. É necessário distribuir o resíduo de um centavo.
Correção:
- Imposto é decomposição do valor bruto, nunca acréscimo ao valor bruto reembolsado.
- Definir matematicamente a base da alíquota embutida: percentual sobre o valor bruto pago ou sobre o valor antes do imposto.
- Calcular e distribuir centavos com ordem determinística.
- Congelar a alocação original da taxa de serviço e do imposto por atendimento/componente.
- Não recalcular percentuais sobre o saldo remanescente em cada cancelamento.
- Garantir também o limite por item e quantidade, não somente o limite global do pagamento.
A invariante de RN-33 precisa ser complementada por:
\[
\text{reembolsado acumulado por item}
\leq
\text{valor originalmente alocado ao item}
\]

E a soma dos componentes financeiros deve fechar exatamente no valor capturado.
3. [ALTA] RN-25 e RN-29 — O pagamento do motorista contradiz o tratamento de cliente ausente
O problema: RN-29 diz que o motorista recebe uma parcela fixa da taxa de entrega, devida quando o pedido é entregue.
RN-25 diz que, se o cliente estiver ausente, o dinheiro permanece com a plataforma, o motorista e o restaurante. Mas, nesse cenário, o pedido termina em não entregue, não em entregue.
As duas regras não determinam o mesmo resultado financeiro.
Cenário concreto:
- Dois restaurantes têm seus atendimentos retirados.
- O motorista percorre a rota.
- O cliente está ausente.
- O pedido fica não entregue.
O motorista recebe sua parcela da taxa de entrega?
Pela RN-29, não. Pela interpretação natural da RN-25, sim.
Há outro problema na RN-30: suponha que o motorista retire A, mas fique impossibilitado antes de retirar B. O pedido recebe estorno total. A repassa para o motorista? E B mantém repasse sem ter ocorrido retirada?
Correção:
Separar os gatilhos financeiros:
Evento	Restaurante	Motorista
Atendimento retirado	Repasse daquele atendimento devido	Parcela de entrega ainda não devida
Pedido entregue	Mantém repasse	Parcela de entrega devida
Cliente ausente após tentativa válida	Mantém repasse	Parcela de tentativa de entrega devida
Motorista impossibilitado	Mantém somente repasses já adquiridos	Sem parcela de entrega concluída, salvo compensação específica
Incidente procedente após entrega	Mantém repasse	Mantém parcela de entrega
Minha decisão para a v1 seria pagar ao motorista a parcela normal por entrega concluída e também por tentativa comprovada frustrada por ausência do cliente. Na impossibilidade do próprio motorista, não pagaria a parcela de entrega concluída; eventual compensação seria outro componente, explicitamente modelado.
O repasse do restaurante deve ser adquirido por atendimento efetivamente retirado. Não se deve pagar pelo atendimento B se ele nunca foi retirado.
Também há uma lacuna de nomenclatura na RN-29: "devido na retirada" deve significar obrigação reconhecida, não necessariamente dinheiro liquidado, pois o fluxo de caixa está fora do escopo.
4. [ALTA] RN-06 e RN-17 — A nova regra de atribuição do motorista contradiz a regra de espera
O problema: RN-06 diz que o motorista só é atribuído quando o primeiro atendimento fica pronto, evitando deslocamento até restaurante que ainda prepara o pedido.
Mas RN-17 diz que ele recolhe o primeiro atendimento e aguarda nos demais restaurantes enquanto ainda estão em preparo.
A segunda regra pode exigir justamente o deslocamento que a primeira pretende evitar.
Cenário concreto:
- A fica pronto às 12h10.
- O motorista é atribuído e retira A.
- B continua em preparo até 12h30.
O motorista deve ir imediatamente para B e aguardar lá? Nesse caso, está viajando até um restaurante ainda em preparo. Deve esperar em A? Deve ir somente quando B ficar pronto?
Outra situação: A e B ficam prontos praticamente ao mesmo tempo. Qual é a ordem de coleta?
Correção:
Definir explicitamente:
1. O primeiro atendimento significa o primeiro a ficar pronto, não o primeiro da lista do pedido.
2. Em empate de disponibilidade, estabelecer desempate determinístico.
3. Se B ainda estiver em preparo, o motorista não deve se deslocar até B. Deve aguardar em local definido ou receber uma nova instrução de rota quando B ficar pronto.
4. Definir a disponibilidade de motoristas. Se nenhum estiver disponível, o pedido aguarda atribuição; não se pode garantir motorista instantaneamente sem essa premissa.
5. Definir o que acontece se o motorista ficar indisponível depois da primeira retirada. A RN-07 impede reatribuição normal nesse ponto, portanto a RN-30 precisa ser o destino operacional explícito.
A regra atual também não estabelece limite de reatribuições antes da primeira retirada. Para o gerador, isso pode produzir uma quantidade arbitrária de trocas de motorista.
5. [ALTA] RN-27 e RN-28 — Os prazos não têm fronteiras temporais suficientemente precisas
O problema: existem quatro relógios relevantes:
- 5 minutos para análise.
- Tempo estimado de preparo + 50%.
- 20 minutos para avaliação.
- 10 minutos para confirmação automática.
A existência dos limites não define como funcionam as fronteiras nem como são iniciados.
Cenário concreto — análise:
Um atendimento é enviado ao restaurante às 12h00.
Às 12h05, exatamente, o restaurante tenta aceitar enquanto o processo automático tenta rejeitar.
RN-27 diz que vale o primeiro evento registrado. Porém, se o processo automático estiver atrasado, o restaurante pode conseguir aceitar às 12h05min10s antes de o evento de rejeição ser efetivamente registrado.
Isso viola a intenção de um prazo máximo de cinco minutos.
Cenário concreto — preparo:
O preparo estimado é de 20 minutos. Com tolerância de 50%, o limite é de 30 minutos.
Não está definido se os 30 minutos começam em aceito ou em em preparo. Também não está definido se o restaurante pode alterar a estimativa depois do aceite.
Correção:
Definir:
Relógio	Início recomendado	Regra de fronteira
Análise	Atendimento enviado ao restaurante	Aceite antes do deadline; rejeição automática a partir dele
Preparo	Aceite do restaurante, se a estimativa significar tempo até ficar pronto	Cancelamento elegível a partir do deadline
Avaliação	Finalização da rota	Até 20 minutos, com limite exclusivo ou inclusivo explícito
Confirmação	Finalização da rota	Uma única confirmação, manual ou automática
Minha recomendação é congelar o tempo estimado de preparo no aceite. Se o gerador precisar medir exclusivamente o tempo de cozinha, deverá existir um evento específico de início do preparo e outro limite para o período entre aceite e início.
RN-27 deve ser aplicada como serialização da decisão sobre o atendimento, mas a validação do prazo precisa ocorrer no próprio comando. Não basta esperar que um agendador registre o timeout.
Também falta decidir se uma ocorrência de incidente nos últimos minutos antes da confirmação automática impede ou não o encerramento automático. Eu manteria o incidente independente: o pedido pode ser concluído enquanto a arbitragem financeira continua aberta.
6. [ALTA] RN-12, RN-13 e RN-28 — O cancelamento legítimo por atraso não está definido como operação completa
O problema: o documento utiliza a expressão "solicitar o cancelamento legítimo", mas a tabela de transições trata isso como cancelamento direto pelo cliente.
Também não está descrito o que acontece quando o limite de atraso é atingido, mas o atendimento fica pronto praticamente ao mesmo tempo.
Cenário concreto:
- Atendimento aceito às 12h00.
- Limite de atraso calculado para 12h30.
- Às 12h30, o cliente solicita cancelamento.
- O restaurante registra pronto simultaneamente.
O resultado depende da precedência dos eventos. Se o pronto for registrado primeiro, a transição para cancelado é proibida. Se o cancelamento for registrado primeiro, o restaurante não pode tornar o atendimento ativo novamente.
Isso é coerente com a RN-27, mas falta explicitar o contrato temporal.
Outro problema: a tolerância de 50% não informa qual duração original será usada se os tempos estimados variarem entre restaurantes ou forem alterados durante o atendimento.
Correção:
Tratar o cancelamento legítimo como uma operação imediata, permitida somente quando:
- A condição de atraso está satisfeita.
- O atendimento ainda está aceito ou em preparo.
- O evento não foi precedido por pronto, retirado ou outro terminal.
Não exigir arbitragem humana. A condição é objetiva.
O pedido do cliente deve ser registrado com motivo específico atraso_do_restaurante, para não ser confundido com o cancelamento normal durante análise.
A RN-28 deve estabelecer o prazo a partir de um timestamp e de uma estimativa imutáveis para aquela execução do atendimento.
7. [ALTA] RN-14, RN-30 e RN-33 — Incidentes e reembolsos ainda permitem reivindicações duplicadas
O problema: a RN-14 agora define item e quantidade, o que resolve a principal lacuna da primeira rodada. Mas o limite de RN-33 continua sendo global, por pagamento.
Ele não impede sozinho que o mesmo item seja reembolsado duas vezes em incidentes diferentes.
Cenário concreto:
Uma compra contém duas unidades de um item de R$ 20.
- Incidente 1: uma unidade faltando, procedente, reembolso de R$ 20.
- Incidente 2: duas unidades erradas, procedente, reembolso de R$ 40.
O acumulado é R$ 60 para um item cuja linha totaliza R$ 40.
A soma pode continuar inferior ao valor total do pedido, portanto a invariante global não detecta o erro.
Correção:
- Limitar a quantidade total reembolsada por item à quantidade comprada.
- Registrar a quantidade já compensada por item.
- Impedir sobreposição de reivindicações em incidentes simultâneos.
- Definir o prazo para abertura de incidente.
- Definir se um incidente pode ser reaberto.
- Definir se vários incidentes podem ser abertos para o mesmo atendimento.
- Registrar a decisão financeira separadamente do resultado operacional.
Outro ponto: RN-14 diz que o incidente procedente gera estorno completo dos itens apontados, mais taxa de serviço e imposto proporcionais. Falta esclarecer se o cliente pode ter um incidente procedente com compensação parcial em situações de qualidade ou atraso. Se não puder, isso deve ser uma limitação expressa.
8. [ALTA] RN-08, RN-11 e RN-15 — A aprovação única ainda não equivale a uma compra única
O problema: RN-15 diz que cada tentativa aprovada gera no máximo um pedido. Isso não garante que uma mesma intenção de compra não gere dois pedidos.
Cenário concreto:
O cliente tenta pagar um pedido. O primeiro pagamento demora a responder. Ele faz uma segunda tentativa. Por uma condição simulada, ambas são aprovadas.
Cada tentativa aprovada gera um pedido. O cliente recebe duas compras, embora pretendesse fazer apenas uma.
Outro caso: o mesmo evento de aprovação é processado duas vezes.
Correção:
Definir uma entidade ou identificador de intenção de compra (checkout), ao qual pertencem as tentativas.
Invariantes:
- Uma intenção de compra gera no máximo um pedido.
- Uma intenção gera no máximo um pagamento principal capturado.
- Uma tentativa aprovada não pode ser consumida duas vezes.
- Tentativas recusadas podem coexistir com uma tentativa posteriormente aprovada.
- A repetição de uma aprovação não gera pedido adicional.
Isso não exige implementar um provedor de pagamentos real. É necessário mesmo no gerador sintético.
9. [MÉDIA] RN-28 — O cálculo do prazo prometido não representa necessariamente a rota real
O problema: o prazo prometido é definido como:
maior tempo estimado de preparo + deslocamento + folga
Para um pedido com dois restaurantes, isso não está suficientemente determinado.
Cenário concreto:
- A fica pronto em 10 minutos.
- B fica pronto em 30 minutos.
- O motorista coleta A e precisa ir até B.
- A distância entre A e B é relevante.
- Depois de B, ainda existe o deslocamento até o cliente.
Se o deslocamento utilizado for apenas a distância de um restaurante ao cliente, o indicador poderá ignorar a viagem entre restaurantes. Se incluir uma distância total, ainda falta o ponto inicial do motorista e a ordem da rota.
Além disso, se cada restaurante recebe a estimativa de preparo em momentos diferentes, o maior número de minutos não necessariamente representa o horário absoluto em que o último atendimento estará pronto.
Correção:
O cálculo deveria utilizar horários previstos de disponibilidade:
\[
T_i = \text{aceite}_i + \text{tempo estimado}_i
\]

Depois, calcular a rota considerando:
- Localização inicial do motorista.
- Deslocamento até o primeiro restaurante.
- Deslocamento entre restaurantes.
- Espera pelo atendimento ainda não pronto.
- Tempo de retirada.
- Deslocamento do último restaurante até o cliente.
- Folga fixa.
Para o gerador, pode-se simplificar a geografia, mas a fórmula precisa ter essas premissas explícitas.
Sem isso, a Gold poderá calcular duração observada da entrega, mas não avaliar corretamente cumprimento do prazo prometido.
10. [MÉDIA] RN-22 e RN-26 — A regra da gorjeta pode invalidar um pagamento já liquidado
O problema: RN-22 diz que a gorjeta já está liquidada e não é estornada. RN-26 diz que ela é desconsiderada quando a avaliação do motorista é 3 ou menor.
Não está definido o que ocorre se a gorjeta for registrada antes da avaliação.
Cenário concreto:
- O cliente paga R$ 10 de gorjeta.
- A gorjeta fica registrada como liquidada.
- Dois minutos depois, o cliente dá nota 2 ao motorista.
- A regra manda desconsiderar a gorjeta, mas RN-22 proíbe o estorno.
É uma contradição financeira e temporal.
Correção:
A regra de elegibilidade deve ser verificada antes da liquidação da gorjeta.
Minha recomendação:
- Avaliação e gorjeta têm o mesmo prazo absoluto de 20 minutos após o fim da rota.
- O cliente pode avaliar ou pular a avaliação.
- Se registrar nota de 1 a 3 para o motorista antes da gorjeta, ela não será oferecida.
- Se não avaliar, poderá dar gorjeta.
- Uma gorjeta já liquidada nunca será invalidada retroativamente.
Também definir um valor mínimo positivo, limite máximo e precisão monetária para a gorjeta. "Valor livre" não é uma validação suficiente.
Para os indicadores de qualidade, avaliações opcionais não devem ser tratadas como nota zero quando ausentes. A Gold precisa mostrar quantidade de avaliações e média, evitando apresentar médias de amostras muito pequenas como indicador confiável.
2. Itens [confirmar] — minhas decisões
São sete itens. Minha posição é a seguinte:
Item	Decisão	Minha avaliação
1. RN-26 — Gorjeta na janela de 20 min e nota do motorista	Reformular	A mesma janela absoluta faz sentido, mas a nota precisa ser conhecida antes da liquidação da gorjeta.
2. RN-28 — Atraso = estimativa + 50%, sem arbitragem	Aprovar com ressalva	Concordo com o limite objetivo e sem arbitragem humana. Falta definir quando começa o relógio.
3. RN-30 — Pagamento ao motorista quando impossibilitado	Decidir: não recebe a parcela normal	A remuneração por entrega não foi adquirida. Eventual compensação deve ser outro evento.
4. RN-21 × RN-14 — Devolução da taxa de entrega	Reformular	A distinção entre problema de item e problema de entrega é correta, mas precisa de classificação objetiva.
5. RN-29 — Repasse ao restaurante na retirada	Aprovar parcialmente	Somente o atendimento efetivamente retirado gera repasse devido.
6. RN-26 — Avaliação somente de atendimento retirado	Aprovar	É a condição correta para não avaliar restaurante cujo pedido foi cancelado ou rejeitado.
7. RN-16 — Status depois de a caminho e em coleta	Aprovar com ressalva	A derivação pré-entrega funciona; os eventos posteriores precisam de uma máquina de estados própria.
Decisões mais detalhadas
Item 1 — RN-26: gorjeta e avaliação
Minha decisão é utilizar o mesmo deadline absoluto de 20 minutos após a finalização da rota, sem obrigar o cliente a gastar primeiro os 20 minutos avaliando.
Fluxo:
- Cliente pode avaliar ou pular a avaliação.
- Nota do motorista igual ou inferior a 3 impede uma nova gorjeta.
- Nota ausente não impede gorjeta.
- Gorjeta liquidada não é invalidada retroativamente por uma avaliação posterior.
Assim, a ordem das ações não produz contradição.
Item 2 — RN-28: atraso
Concordo com a tolerância de 50%, mas recomendo usar accepted_at como início do relógio na v1.
Nesse caso, a estimativa deve significar tempo previsto entre aceite e atendimento pronto, não somente tempo de cozinha.
A fórmula fica:
\[
deadline = accepted\_at + estimativa \times 1,5
\]

Se preferirem medir o tempo exclusivamente de preparo, será necessário um evento separado de início da preparação e outra regra para o tempo entre aceite e início.
Item 3 — RN-30: motorista impossibilitado
Minha decisão: não pagar a parcela normal de entrega quando o próprio motorista fica impossibilitado de completar a operação.
Não confundir isso com cliente ausente: nesse caso, houve uma tentativa válida de entrega, e a remuneração do motorista pode ser adquirida.
Uma compensação por coleta já realizada seria outro evento, com valor e condições próprios.
Item 4 — RN-21 × RN-14: quando devolver a taxa de entrega
Definiria uma classificação explícita:
Ocorrência	Devolução da taxa de entrega
Item faltando	Não
Item errado	Não
Problema de qualidade do alimento	Não
Atraso de entrega reconhecido como procedente	Conforme política explícita
Pedido perdido durante a entrega	Sim
Motorista impossibilitado de concluir a entrega	Sim
Cliente ausente	Não
A classificação deve ser determinada pelo motivo do incidente, não por uma interpretação livre do atendente da plataforma.
Item 5 — RN-29: repasse na retirada
Concordo com o gatilho da retirada, mas ele é por atendimento, não pelo pedido.
Para dois restaurantes, um repasse pode estar devido e o outro ainda não.
O incidente procedente não desfaz um repasse já adquirido. Já um atendimento não retirado não pode receber repasse somente porque outro restaurante teve sua parte coletada.
Item 6 — RN-26: avaliação do restaurante
Aprovo, com uma precisão: a avaliação só fica disponível depois de o pedido ter sido entregue. Dentro de um pedido entregue, somente os atendimentos efetivamente retirados podem receber avaliação.
Item 7 — RN-16: status de pedido
Aprovo a derivação proposta. Particularmente, em coleta para um atendimento retirado e outro ainda em análise é coerente com a regra operacional.
A ressalva é que a transição de a caminho para entregue, concluído ou não entregue não deve ser tratada como simples continuação da mesma derivação. É uma segunda máquina, dirigida pelos eventos do pedido.
Markdown colado.md

3. Implicações para modelo de dados e CDC
Não vou antecipar decisões técnicas de transporte, ordenação ou infraestrutura de CDC, pois o próprio documento deixa isso para a modelagem.
Mas as regras já exigem preservação de algumas informações.
Informação necessária	Justificativa de negócio
Histórico de transições dos atendimentos	RN-18 e RN-16
Histórico de transições do pedido	RN-16 e RN-24
Histórico das atribuições do motorista	RN-31
Timestamps de aceite, preparo e pronto	RN-28 e métricas operacionais
Timestamps de retirada por atendimento	RN-17 e RN-29
Finalização da rota e confirmação	RN-24 e RN-26
Todas as tentativas de pagamento	RN-15
Ajustes financeiros e reembolsos	RN-14, RN-21 e RN-33
Incidentes e respectivas decisões	RN-14
Estimativa original de preparo	RN-28
Prazo prometido originalmente	RN-28
Avaliação e gorjeta	RN-22 e RN-26
Um ponto particularmente importante: histórico derivado
Como o pedido deriva seu estado dos atendimentos antes de a caminho, a Silver precisa conseguir reconstruir a situação dos dois atendimentos no mesmo instante lógico.
Exemplo:
- A ficou pronto às 12h10.
- B ficou pronto às 12h12.
- A foi retirado às 12h15.
- B foi retirado às 12h20.
O pedido deve apresentar:
- Até 12h10: conforme o estado dos atendimentos.
- Depois de 12h10: parcialmente pronto, se B ainda não estiver pronto.
- Depois de 12h15: em coleta.
- Depois de 12h20: a caminho.
Não é suficiente consultar os dois últimos status encontrados na origem. É necessário reconstruir a sequência histórica.
Lacunas residuais da primeira rodada
Há duas correções anteriores que considero incompletas:
RN-32 — Snapshot do produto.
Nome e preço unitário foram incorporados, mas eu também preservaria no item:
- Identidade original do produto.
- Identidade do restaurante/estabelecimento que vendeu o produto.
- Quantidade e total contratado.
Sem a identidade do restaurante preservada, uma alteração posterior na associação do produto pode comprometer a interpretação histórica.
RN-03 — Mesma cidade.
A restrição de mesma cidade precisa usar uma referência geográfica canônica. Não usaria comparação de nomes textuais de cidades.
Também definiria se restaurante significa a marca ou uma unidade física. Para logística, o que importa é a unidade de retirada.
Markdown colado.md
 Markdown colado.md


4. Testabilidade: onde os testes podem enganar
Eu exigiria os seguintes grupos de testes.
Área	Teste necessário	Principal risco
RN-16	Todas as combinações de um e dois atendimentos ativos	Implementação e teste repetirem a mesma lógica errada
RN-27/RN-28	Antes, exatamente no limite e depois do limite	Dependência de horário e execução do agendador
RN-21/RN-33	Todas as ordens possíveis de cancelamento parcial	Arredondamento e duplicação
RN-14	Incidentes sobre quantidades parcialmente reembolsadas	Reembolso duplicado
RN-29/RN-30	Um ou dois atendimentos, retirada parcial e não entrega	Repasse indevido
RN-15	Repetição de aprovação e múltiplas tentativas aprovadas	Pedido duplicado
RN-22/RN-26	Todas as ordens de avaliação e gorjeta	Gorjeta liquidada e posteriormente invalidada
RN-28	Diferentes tempos de preparo e rotas	Indicador de pontualidade artificial
Três riscos de testes tautológicos
1. Status derivado
Não calcular o resultado esperado pela mesma função que calcula o status real.
A tabela de referência da RN-16 deve ser usada como oráculo independente.
2. Reembolso
Não testar simplesmente se a soma calculada pelo sistema é igual à soma calculada por outra função que utiliza o mesmo algoritmo.
Usar exemplos monetários manuais, incluindo R$ 0,01, R$ 0,05, divisões não exatas e dois cancelamentos sucessivos.
3. Margem da plataforma
Não validar margem somando novamente as mesmas colunas usadas para calculá-la.
Criar exemplos com distribuição financeira esperada, considerando comissão, serviço, entrega, custo de pagamento, repasses e reembolsos.
Uma propriedade particularmente importante:
Cancelar A e depois B deve produzir o mesmo resultado financeiro final que cancelar B e depois A, desde que ambas as sequências sejam operacionalmente permitidas e os eventos não tenham efeitos temporais diferentes.

Se o resultado depender arbitrariamente da ordem de processamento, há um problema de alocação de centavos ou de cálculo de reembolso.

5. As três decisões que mais custariam caro de reverter
1. Separação entre pedido, atendimento, atribuição e incidentes.
A modelagem precisa representar ciclos de vida independentes, mas relacionados. Misturá-los em uma tabela de pedido com vários campos de status tornaria muito difícil reconstruir a operação.
2. Distribuição financeira e reconhecimento de receita.
É preciso fechar primeiro quando comissão, repasse do restaurante, parcela do motorista, taxa de serviço e reembolsos são adquiridos. Isso define a estrutura financeira e os indicadores da Gold.
3. Semântica temporal e cálculo de prazo.
Os relógios de análise, preparo, coleta, entrega, avaliação e confirmação precisam ter origens e limites definidos. Alterar essas definições depois significa recalcular históricos e modificar os indicadores apresentados.

6. O que não consegui avaliar por falta de informação
Não recebi o modelo conceitual, os esquemas das três origens nem a implementação do gerador. Portanto, não consegui verificar:
1. Se o identificador do restaurante representa marca ou unidade física.
2. Como os bancos relacionais e documental identificam a mesma entidade.
3. Se os horários e distâncias do gerador são consistentes com as rotas.
4. Se a estimativa de preparo tem valores e origem temporal definidos no gerador.
5. Se existe uma entidade de checkout ou intenção de pagamento.
6. Como são definidos os percentuais de comissão, imposto, serviço, pagamento e entrega.
7. Como a plataforma identifica uma tentativa válida de entrega quando o cliente está ausente.
8. Como é representada a impossibilidade do motorista após uma retirada parcial.
9. Como são calculados os indicadores de qualidade por restaurante e motorista.
10. Se a modelagem consegue preservar versões históricas do perfil, cardápio e produto.
Também não avaliei a adequação fiscal da simplificação do imposto. Ela foi declarada deliberadamente fictícia, portanto não estou tratando sua divergência da legislação brasileira como defeito do projeto.

Conclusão
Minha recomendação é fechar cinco contratos antes da modelagem lógica:
1. Estados do pedido depois de a caminho, incluindo a concorrência entre entrega e não entrega.
2. Distribuição financeira e regras de remuneração nas situações de sucesso, ausência, cancelamento e impossibilidade do motorista.
3. Fórmula única de reembolso, incluindo a decomposição do imposto e a alocação determinística dos centavos.
4. Relógios de análise, preparo, atraso, entrega, avaliação e confirmação, com timestamps de referência e limites exatos.
5. Regras de coleta e atribuição do motorista quando os restaurantes ficam prontos em momentos diferentes.
Minha avaliação final: eu permitiria avançar para um modelo conceitual exploratório, mas não congelaria o modelo lógico ou físico. Os maiores riscos restantes já não são a estrutura básica de pedidos e atendimentos: são as exceções operacionais e a conservação financeira nos caminhos alternativos.