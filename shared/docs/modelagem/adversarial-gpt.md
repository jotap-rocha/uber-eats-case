Revisão adversarial — uber-eats-case
Veredito: não congelaria essas regras para iniciar a modelagem conceitual. Existem problemas na máquina de estados, na semântica dos reembolsos e na relação entre atendimento, pedido e motorista. São decisões estruturais: se forem incorporadas incorretamente ao modelo físico, o pipeline analítico herdará as inconsistências.
A revisão considera os dois documentos anexados e o contexto declarado de dados sintéticos, três bancos de origem e arquitetura Bronze → Silver → Gold. Não estou presumindo informações que não aparecem neles.
1. As 10 falhas e riscos mais graves
1. [BLOQUEANTE] RN-16 — A derivação do status do pedido tem uma condição inalcançável
O problema: a regra 4 diz:
todos prontos ou já retirados → pedido pronto para retirada

A regra 5 diz:
todos retirados → pedido a caminho

Se as condições forem avaliadas na ordem apresentada, a regra 4 captura também o caso em que todos foram retirados. Portanto, a regra 5 nunca será executada.
Há ainda um problema mais profundo: a prioridade dada ao atendimento em análise pode fazer o pedido parecer estar em uma etapa anterior mesmo quando outro atendimento já foi retirado.
Cenário concreto:
Pedido com três restaurantes:
Restaurante	Status
A	Retirado
B	Em análise
C	Cancelado
Pela regra 2, o pedido fica em análise. Entretanto, o motorista já está com os itens de A.
Outro cenário:
Restaurante	Status
A	Retirado
B	Retirado
C	Cancelado
O pedido deveria estar a caminho, mas a regra 4 também atende à condição.
Além disso, RN-16 menciona entregue e concluído, mas não define quais eventos produzem essas transições. O status não está inteiramente derivado dos atendimentos.
Correção:
Definir uma máquina de estados formal, com precedência explícita e condições mutuamente exclusivas. Minha sugestão:
- Todos cancelados: cancelado.
- Algum atendimento em análise: em análise.
- Algum atendimento aceito ou preparando: em preparo.
- Todos os atendimentos ativos prontos e nenhum retirado: pronto para retirada.
- Todos os atendimentos ativos retirados: a caminho.
- Entrega confirmada: entregue.
- Encerramento administrativo: concluído.
Essa proposta ainda precisa resolver o caso misto de atendimento retirado com outro em análise. Minha recomendação é manter o status geral como em análise, mas apresentar separadamente o progresso de coleta e o de entrega. Assim, o status geral não precisa transmitir toda a informação operacional.
Entregue e concluído devem ter eventos e condições explícitos, independentes da máquina de estados dos atendimentos.
Importante: testar a tabela inteira de combinações possíveis, incluindo cancelados, e não apenas uma sequência feliz.

2. [BLOQUEANTE] RN-09, RN-19 e RN-21 — A decomposição monetária e o reembolso não fecham um contrato financeiro
O problema: há três regras relacionadas que não definem uma única fórmula de composição e devolução do pagamento.
RN-09 diz que o imposto é uma proporção do valor pago, embutida. RN-19 diz que o imposto está embutido nos componentes do pedido. RN-21 determina que o imposto acompanha proporcionalmente o reembolso dos itens e da taxa de serviço.
Não está definido se o imposto é um componente contábil de cada parcela ou uma decomposição posterior do total. Também não está definido como arredondar os valores.
Cenário concreto:
Pedido:
Componente	Valor
Itens A	R$ 33,33
Itens B	R$ 66,67
Taxa de entrega	R$ 9,99
Taxa de serviço	R$ 10,00
Total	R$ 119,99
O atendimento B é cancelado.
O reembolso deve considerar R$ 66,67 de itens e a parcela correspondente da taxa de serviço. Mas:
- Qual é a base de proporcionalidade da taxa de serviço?
- Como o imposto é extraído dos componentes?
- O imposto já está embutido nos R$ 66,67 e nos R$ 10,00?
- Como dividir os centavos?
- Se houver vários cancelamentos, a soma dos reembolsos será exatamente igual ao total reembolsável?
Se o imposto for adicionado novamente ao reembolso, haverá duplicação. Se for extraído de um componente já líquido, o cálculo pode devolver menos do que deveria.
Correção:
Criar uma decomposição monetária formal com valores em centavos inteiros ou NUMERIC, especificando:
1. Subtotal de itens por atendimento.
2. Taxa de serviço por pedido e sua alocação por atendimento.
3. Taxa de entrega por pedido.
4. Imposto embutido em cada componente.
5. Comissão do restaurante por atendimento.
6. Valor bruto recebido.
7. Valor líquido devido ao restaurante.
8. Valor retido pela plataforma.
9. Valores efetivamente reembolsados.
Estabelecer uma regra determinística de distribuição de centavos, com a seguinte invariante:
\[
\sum \text{reembolsos} \leq \text{valor efetivamente pago}
\]

E, quando houver cancelamento integral:
\[
\text{reembolso acumulado} = \text{pagamento original}
\]

Não basta testar um único cancelamento. Testar cancelamentos parciais sucessivos em ordens diferentes.

3. [BLOQUEANTE] RN-10, RN-12 e RN-14 — Cancelamento e incidente misturam estados operacionais e financeiros
O problema: o documento trata cancelamento como uma operação por atendimento, inclusive depois da retirada mediante incidente procedente. Isso mistura dois acontecimentos diferentes:
- Interrupção do atendimento/fulfillment.
- Compensação financeira por problema com um pedido já entregue ou em trânsito.
Após a retirada, o restaurante já entregou os itens ao motorista. Não faz sentido necessariamente transformar o atendimento em cancelado por causa de um item faltando ou errado.
RN-14 também não define se o incidente se refere ao item, atendimento ou pedido.
Cenário concreto:
O pedido tem dois restaurantes. O motorista retirou os dois atendimentos e iniciou a entrega. O cliente informa que um item do restaurante A está errado.
A plataforma considera o incidente procedente.
O que acontece?
- O atendimento A muda de retirado para cancelado?
- O pedido deixa de estar a caminho?
- Os itens do restaurante B continuam sendo entregues?
- O cliente recebe reembolso integral de A?
- Apenas o item incorreto é reembolsado?
- Como fica a comissão do restaurante A?
A regra atual não responde.
Correção:
Separar três entidades/conceitos:
- Atendimento: ciclo operacional do restaurante.
- Incidente: reclamação e arbitragem.
- Ajuste financeiro: crédito, reembolso ou compensação produzida pela decisão.
O incidente procedente deve gerar um evento financeiro compensatório, sem necessariamente retroagir o estado operacional.
Também definir a granularidade mínima do incidente. Minha recomendação é permitir referência a item e atendimento, com possibilidade de um incidente abranger vários itens.
Definir ainda:
- Quem pode abrir o incidente.
- Prazo para abertura.
- Evidências necessárias.
- Possibilidade de reabertura.
- Quem pode alterar a decisão.
- Se um pedido admite vários incidentes.
- Se há limite de reembolso acumulado por item.
- Como o incidente afeta comissão e repasse.

4. [ALTA] RN-06, RN-07 e RN-17 — O ciclo de vida do motorista está incompleto
O problema: existe atribuição, liberação e reatribuição, mas não existe uma máquina de estados do próprio vínculo entre motorista e pedido.
A RN-06 atribui o motorista quando o primeiro atendimento é aceito. A RN-07 permite reatribuição antes da primeira retirada. A RN-17 prevê espera nos restaurantes.
Essas regras não contemplam adequadamente indisponibilidade, espera excessiva, cancelamento de atendimento durante a espera ou falha operacional após a primeira retirada.
Cenário concreto:
- Restaurante A aceita.
- Motorista M1 recebe o pedido.
- M1 chega ao restaurante A.
- A cancela antes da retirada.
- Restaurante B permanece preparando.
- M1 continua atribuído ao pedido?
Se for liberado, quem assume o acompanhamento de B? Se não for liberado, como o motorista fica esperando sem atendimento disponível?
Outro cenário: M1 retira A e sofre uma pane antes de retirar B. Pela RN-07, o motorista não pode mais ser substituído, pois já houve retirada. O pedido fica sem caminho operacional para terminar.
Correção:
Definir separadamente o estado da atribuição:
não atribuído → atribuído → deslocando → aguardando → coleta parcial → coleta completa → entrega → encerrado
E estados alternativos para liberação e reatribuição.
A RN-06 precisa responder explicitamente:
- Se há atendimentos ainda em análise, o motorista pode ser liberado?
- Se todos os atendimentos aceitos forem cancelados, mas houver atendimentos não aceitos, qual é o estado da atribuição?
- Quantas reatribuições são permitidas?
- O motorista pode recusar antes de aceitar?
- O motorista pode ficar indisponível depois de aceitar?
- O que acontece quando uma retirada já ocorreu e o motorista fica impossibilitado de continuar?
Também recomendo registrar cada atribuição como histórico independente. Não sobrescrever simplesmente driver_id no pedido.

5. [ALTA] RN-03, RN-04, RN-05 e RN-23 — O modelo de catálogo não preserva a história comercial do pedido
O problema: RN-23 estabelece que o menu referencia o produto, e o produto carrega nome e preço. RN-04 estabelece que o item referencia o produto.
Não há regra dizendo que o pedido deve preservar o nome e o preço efetivamente contratados na compra.
Cenário concreto:
- O produto custa R$ 25 no momento da compra.
- O pedido é aprovado.
- O restaurante altera o preço para R$ 30.
- Uma consulta histórica ao pedido utiliza o preço atual do produto.
O pedido passa a parecer ter custado R$ 30, embora o cliente tenha pago R$ 25.
O mesmo vale para alteração de nome, remoção do produto ou associação incorreta a outro restaurante.
Correção:
O item do pedido precisa preservar um snapshot comercial:
- product_id original.
- restaurant_id.
- Nome do produto na compra.
- Preço unitário contratado.
- Quantidade.
- Total do item.
- Eventuais atributos e adicionais contratados.
O preço histórico não pode depender do cadastro atual do produto.
Também especificar quando um produto pode ser removido, desativado ou alterado sem afetar pedidos já aprovados.
Há outro risco relevante: os três bancos não possuem FK física. Portanto, a consistência entre produto, restaurante, menu e perfil precisa ser validada explicitamente na origem ou na Silver. Não é aceitável depender apenas de o gerador produzir registros coerentes.

6. [ALTA] RN-08, RN-11 e RN-15 — O ciclo de pagamento não cobre tentativas, aprovação e cancelamento concorrentes
O problema: RN-11 afirma que um pedido só existe depois do pagamento aprovado. RN-15 exige registrar tentativas recusadas sem pedido. RN-08 prevê um pagamento principal por pedido.
Isso ainda não define a relação entre tentativas de pagamento e o pagamento aprovado.
Cenário concreto:
1. Cliente inicia pagamento.
2. Primeira tentativa é recusada.
3. Segunda tentativa é aprovada.
4. A resposta de aprovação chega duas vezes por retry.
5. O gerador cria dois pedidos ou dois pagamentos.
Outro cenário:
- A aprovação acontece praticamente ao mesmo tempo que o cliente tenta cancelar.
- Um processo considera o pagamento aprovado.
- Outro considera o atendimento cancelado antes mesmo da criação do pedido.
Correção:
Separar:
- Tentativa de pagamento.
- Pagamento principal.
- Pedido.
- Evento de reembolso.
Definir que uma tentativa aprovada é associada ao pagamento e ao pedido correspondente, sem assumir que toda tentativa precisa estar ligada a pedido.
Criar invariantes:
- Uma aprovação comercial válida cria no máximo um pedido.
- Um pedido possui no máximo um pagamento principal.
- Tentativas recusadas nunca produzem reembolso.
- Um reembolso sempre referencia um pagamento aprovado.
- Soma dos reembolsos não excede o valor capturado.
- Eventos repetidos não criam novas aprovações, pedidos ou reembolsos.
A criação do pedido precisa ser protegida por idempotência.

7. [ALTA] RN-16, RN-17 e RN-18 — O histórico de eventos não tem contrato temporal para o CDC
O problema: a arquitetura pretende capturar mudanças de três bancos independentes, mas as regras não especificam como ordenar acontecimentos, tratar duplicações e reconstruir o estado correto.
RN-18 promete histórico das transições dos dois níveis. RN-16 deriva o pedido dos atendimentos. Isso exige consistência temporal entre a origem e o cálculo derivado.
Cenário concreto:
Dois restaurantes alteram seus atendimentos quase simultaneamente:
- A passa de preparando para pronto.
- B passa de análise para aceito.
O CDC recebe a mudança de B antes da mudança de A, embora o acontecimento tenha ocorrido na ordem inversa.
Se o pipeline derivar o pedido usando apenas a ordem de chegada, poderá registrar uma sequência artificial de status.
Outro cenário: o mesmo evento chega duas vezes após uma falha e duplica a transição.
Correção:
Definir um contrato comum de eventos com, no mínimo:
- event_id globalmente único.
- aggregate_id.
- aggregate_version ou sequência por entidade.
- occurred_at.
- recorded_at.
- Identificação da origem.
- Tipo do evento.
- Versão do schema.
- Identificador da transação de origem, quando disponível.
Não usar timestamp como único mecanismo de ordenação.
Na Silver:
- Deduplicar eventos.
- Identificar lacunas de sequência.
- Tratar eventos atrasados.
- Preservar histórico de estados.
- Recalcular o status do pedido a partir dos atendimentos válidos em cada instante.
- Registrar divergências de integridade referencial.
A Gold deve consumir uma representação temporal consistente, não simplesmente o último status encontrado em cada tabela.

8. [ALTA] RN-01, RN-09, RN-19 e RN-22 — Não há definição suficiente para receita e margem da plataforma
O problema: o contexto declara indicadores de receita da plataforma e margem por pedido, mas as regras financeiras não definem integralmente os fluxos envolvidos.
A RN-19 define comissão sobre os itens, taxa de serviço e taxa de entrega. RN-09 menciona taxa do meio de pagamento. RN-22 define gorjeta direta ao motorista.
Entretanto, não está definido:
- Quanto a plataforma efetivamente recebe.
- Quanto repassa ao restaurante.
- Qual parcela da taxa de entrega é destinada ao motorista.
- Se existe remuneração adicional ao motorista.
- Como os custos do meio de pagamento entram na margem.
- Como cancelamentos afetam comissão.
- Como incidentes afetam repasses já calculados.
- Quando ocorre liquidação financeira.
Cenário concreto:
Um pedido de R$ 100 tem comissão de 20%, taxa de serviço de R$ 5 e taxa de entrega de R$ 10.
A plataforma registra receita de R$ 25? R$ 15? R$ 5?
Depende da interpretação da taxa de entrega, da remuneração do motorista e do tratamento da comissão. O modelo não permite responder com segurança.
Correção:
Criar um contrato explícito de distribuição financeira por pedido e atendimento:
\[
\text{pagamento capturado}
=
\text{componentes cobrados do cliente}
\]

E, separadamente:
\[
\text{margem da plataforma}
=
\text{receitas reconhecidas}
-
\text{custos atribuíveis}
\]

Definir as categorias que compõem cada lado, a competência, a liquidação e os efeitos dos reembolsos.
A RN-01 pode manter o governo fora do modelo operacional, como decisão de escopo. Mas o imposto simulado precisa ser identificado como componente sintético, não apresentado como apuração fiscal real.

9. [MÉDIA] RN-14, RN-16 e RN-17 — Não existe encerramento operacional garantido
O problema: a entrega começa quando todos os atendimentos não cancelados foram retirados, mas não existe processo definido para entrega malsucedida. O contexto declara essa funcionalidade fora do escopo, embora a máquina de estados exija os estados entregue e concluído.
Também não está definida uma condição temporal para um restaurante que demora indefinidamente.
Cenário concreto:
- A está retirado.
- B foi aceito, mas nunca fica pronto.
- O motorista aguarda B.
- O cliente não pode cancelar B porque já foi aceito.
- O restaurante não cancela.
- O pedido nunca chega a caminho.
O sistema pode manter um pedido em preparo indefinidamente.
Outro caso: o pedido está a caminho, mas o motorista não encontra o cliente. Não existe transição prevista.
Correção:
Mesmo que entrega malsucedida permaneça fora da v1, definir um estado terminal de exceção ou uma regra explícita de encerramento.
Para Gold, também é necessário definir:
- O que significa entrega no prazo.
- Qual é o prazo prometido.
- Quando começa a contagem.
- Quando termina.
- Como tratar pedidos parcialmente cancelados.
- Como tratar pedidos nunca entregues.
Sem prazo prometido, é possível medir duração da entrega, mas não cumprimento de prazo.

10. [MÉDIA] RN-05, RN-16 e RN-18 — A testabilidade está baseada demais no estado final e pouco nas transições válidas
O problema: uma máquina de estados que calcula corretamente o status final pode aceitar transições impossíveis ou produzir histórico inconsistente.
O documento menciona históricos, mas não define um conjunto completo de transições permitidas.
Cenário concreto:
Um atendimento transita:
retirado → em análise
O sistema atualiza o status e o pedido passa a em análise.
O cálculo de status geral pode estar funcionando conforme as condições definidas, mas a transição operacional é absurda.
Outro caso:
cancelado → pronto para retirada
Um evento atrasado pode causar essa regressão se não houver controle de versão ou validade.
Correção:
Definir uma tabela de transições:
Estado atual	Próximo estado	Permitido?
Em análise	Aceito	Sim
Em análise	Cancelado	Sim
Aceito	Preparando	Sim
Aceito	Cancelado	Sim
Preparando	Pronto	Sim
Preparando	Cancelado	Sim
Pronto	Retirado	Sim
Retirado	Cancelado	Não como transição operacional normal
Cancelado	Qualquer estado ativo	Não
A tabela é inicial: ainda precisa especificar rejeição, cancelamento pelo cliente e exceções administrativas.
Os testes devem validar tanto transições válidas quanto inválidas, estados derivados e histórico reconstruído.
Não usar a própria implementação da máquina de estados como oráculo dos testes.
2. Contradições e ambiguidades entre regras
Além dos dez riscos, estes são os conflitos que eu exigiria resolver antes da modelagem.
Regras	Problema	Decisão necessária
RN-16 (4) × RN-16 (5)	Todos retirados também satisfaz a condição anterior de todos prontos ou retirados.	Tornar as condições mutuamente exclusivas e dar precedência explícita à entrega iniciada.
RN-06 × RN-07	Liberação após cancelamento dos atendimentos aceitos não esclarece como ficam atendimentos ainda em análise.	Definir quando uma atribuição deixa de ser necessária e quando uma nova atribuição é disparada.
RN-10 × RN-14	Cancelar todos os atendimentos pode cancelar o pedido, mas incidentes podem cancelar atendimentos já retirados.	Não confundir cancelamento operacional com reembolso após retirada.
RN-12 × RN-13	Após o aceite, o cliente perde a possibilidade de cancelar, mesmo antes da retirada.	Confirmar que essa restrição é intencional e definir exceções.
RN-08 × RN-15	Pagamento principal está ligado ao pedido; tentativas recusadas não estão. O vínculo da tentativa aprovada não está definido.	Definir a relação entre tentativa aprovada, pagamento capturado e pedido.
RN-09 × RN-19 × RN-21	Imposto é calculado sobre o pagamento, está embutido nos componentes e acompanha proporcionalmente o reembolso.	Definir uma única decomposição contábil para impedir dupla contabilização.
RN-06 × RN-17	Motorista é atribuído no aceite, mas a coleta acontece quando o atendimento fica pronto.	Separar atribuição, deslocamento, chegada e disponibilidade para retirada.
RN-20 × RN-21	Existe uma taxa de entrega única, mas sua devolução depende da situação dos atendimentos.	Definir a política de devolução também quando a coleta ou entrega já começou.
RN-16 × RN-18	Status geral é derivado, mas seu histórico também deve existir.	Definir se o histórico geral é armazenado ou reconstruído e como são tratados eventos atrasados.
RN-19 × RN-22	Gorjeta é posterior à entrega e fora do pagamento principal.	Definir a relação da gorjeta com pedidos parcialmente entregues e com pedidos que tiveram incidentes.
Markdown colado.md
 Markdown colado.md

3. Decisões sobre os seis itens [confirmar]
Aqui estão minhas decisões específicas.
1. RN-06 — Liberação do motorista
Reformular
A liberação deve acontecer quando:
- Nenhum atendimento já foi retirado.
- Todos os atendimentos aceitos que justificavam a atribuição foram cancelados.
- Não existe outra coleta ativa que exija aquele motorista.
Minha decisão: liberar o motorista mesmo que existam atendimentos ainda em análise. Se um deles for aceito posteriormente, uma nova atribuição será necessária.
Não manter um motorista preso a um pedido sem atendimento aceito ativo.
Também precisa existir uma regra para o caso de dois atendimentos serem aceitos praticamente ao mesmo tempo.
2. RN-16 — Derivação do status
Rejeitar tabela atual
O problema não é apenas corrigir a ordem das condições. É necessário separar:
- Status operacional do pedido.
- Progresso de coleta.
- Progresso de entrega.
- Situação financeira de cancelamentos e reembolsos.
Minha decisão: o status geral pode representar o estágio mais atrasado da operação, mas não deve esconder que já existem atendimentos retirados. Os estados de entrega precisam ser definidos separadamente.
Exigir uma tabela verdade com todas as combinações válidas de atendimentos.
3. RN-21 — Reembolso proporcional
Reformular
Concordo com a ideia de uma única taxa de entrega, sem rateá-la entre restaurantes. Discordo de usar apenas a quantidade de atendimentos restantes como critério suficiente para devolvê-la.
Minha decisão:
- Itens cancelados: reembolso integral dos itens correspondentes.
- Taxa de serviço: devolver a parcela atribuível aos itens cancelados, com alocação de centavos determinística.
- Imposto: componente decomposto do valor reembolsado, não um acréscimo independente.
- Taxa de entrega: manter quando a operação de entrega efetivamente prosseguir; devolver quando não houver prestação de entrega por cancelamento integral anterior ao início desse serviço.
- Incidente depois do início da entrega: seguir política específica de compensação, sem assumir automaticamente que toda a taxa é reembolsável.
A regra precisa tratar cancelamentos sucessivos e garantir que nenhum centavo seja devolvido duas vezes.
4. RN-14 — Incidente e abrangência do reembolso
Bloqueante para modelagem
Não escolheria o atendimento inteiro como unidade obrigatória de reembolso.
Minha decisão: incidente pode referenciar um ou mais itens, sempre vinculado ao atendimento e ao pedido. A decisão da plataforma especifica o escopo e valor aprovado.
Um item faltando não deve produzir automaticamente o cancelamento de todos os itens do restaurante.
Também não permitiria transformar um atendimento retirado em cancelado apenas por causa de um reembolso.
5. RN-12 — Estado inicial e pagamentos anteriores
Aprovar com precisão
Minha decisão:
- O estado inicial do atendimento é em análise.
- O cliente pode cancelá-lo nesse estado.
- O aceite do restaurante encerra essa possibilidade.
- O reembolso só incide sobre um pagamento efetivamente aprovado e capturado.
- Tentativas recusadas jamais geram reembolso.
Existe, porém, uma lacuna: pagamentos pendentes podem ser aprovados posteriormente. O modelo precisa definir o comportamento de uma aprovação tardia, inclusive quando o cliente já abandonou a operação.
Não criaria um reembolso artificial para uma tentativa recusada.
6. RN-17 — Disponibilidade e espera
Aprovar após definição
Minha decisão:
- Atendimento disponível para retirada = atendimento no estado pronto.
- Registrar ready_at.
- Registrar separadamente driver_arrived_at e picked_up_at.
- Se o motorista chegar antes de o restaurante ficar pronto, o estado é aguardando, não retirado.
- O motorista pode realizar retiradas parciais, mas o pedido somente entra em a caminho quando todos os atendimentos ativos tiverem sido retirados.
Também é necessário esclarecer se o motorista vai primeiro ao restaurante cujo atendimento ficou pronto primeiro ou se existe uma sequência de coleta planejada.
A frase "aguarda nos demais restaurantes" não é suficiente para determinar a operação.
Markdown colado.md

4. Implicações para o modelo de dados e o pipeline CDC
Aqui está um ponto importante: este projeto não está modelando apenas um aplicativo. Está gerando dados que serão usados para demonstrar engenharia de dados.
As decisões sobre histórico e ordenação dos eventos precisam nascer nas regras de negócio.
Modelo transacional
Eu não começaria o modelo conceitual com uma entidade única de pedido contendo diversos campos de status.
No mínimo, esperaria identificar os seguintes conceitos:
Conceito	Responsabilidade
Pedido	Agrupa a compra do cliente
Item do pedido	Registra o produto, preço e quantidade contratados
Atendimento	Representa a operação de um restaurante no pedido
Tentativa de pagamento	Registra cada tentativa, aprovada ou recusada
Pagamento	Registra o valor capturado
Reembolso	Registra cada devolução vinculada ao pagamento
Incidente	Registra a reclamação e sua arbitragem
Atribuição de motorista	Mantém histórico de atribuições e liberações
Transição de status	Preserva o histórico operacional
Gorjeta	Registra pagamento independente do pedido
Isso não é uma sugestão de tabelas físicas definitivas. É a separação conceitual que as regras exigem.
Bronze
A Bronze deve preservar os acontecimentos originais, com identificação da origem.
Não descartaria:
- Eventos duplicados.
- Eventos atrasados.
- Registros com referências inválidas.
- Eventos de exclusão.
- Alterações de estado.
- Divergências entre fontes.
A Bronze é a camada de preservação da evidência, não de correção silenciosa.
Silver
A Silver precisa resolver os principais problemas sem perder rastreabilidade:
1. Deduplicação por identificador de evento.
2. Ordenação por sequência da entidade, não apenas timestamp.
3. Reconstrução dos históricos de pedido e atendimento.
4. Integridade lógica entre cliente, restaurante, produto, perfil e menu.
5. Reconciliação entre pagamento, reembolso e total do pedido.
6. Derivação do status do pedido usando os estados válidos dos atendimentos.
7. Identificação de transições proibidas.
Recomendação importante: não calcule status do pedido simplesmente selecionando o último registro de cada atendimento. É necessário reconstruir o estado de cada atendimento no mesmo ponto temporal antes de derivar o status geral.
Gold
A Gold precisa ter contratos claros para seus indicadores.
Indicador	Risco atual
Tempo de análise	Início e fim ainda precisam de eventos inequívocos
Tempo de preparo	Aceite e início do preparo podem ser eventos diferentes
Tempo de coleta	Existem retiradas independentes por atendimento
Tempo de entrega	Início definido, mas conclusão precisa de evento próprio
Entrega no prazo	Não existe prazo prometido definido
Receita da plataforma	Falta contrato de composição da receita
Margem por pedido	Falta definição dos custos e repasses
Qualidade por restaurante	Não existe avaliação nem indicador formal de qualidade
Qualidade por motorista	Mesma lacuna da avaliação e dos critérios de qualidade
Markdown colado.md
Invariantes que eu exigiria
Estas são algumas invariantes que deveriam orientar tanto os bancos quanto os testes:
ID	Invariante
INV-01	Todo pedido tem exatamente um cliente.
INV-02	Todo item pertence a exatamente um pedido e um restaurante.
INV-03	Todo atendimento corresponde a um único par pedido/restaurante.
INV-04	A soma dos itens dos atendimentos corresponde ao subtotal de itens do pedido.
INV-05	O pedido possui no máximo um pagamento principal capturado.
INV-06	Tentativas recusadas não produzem pagamentos nem reembolsos.
INV-07	A soma dos reembolsos não excede o valor capturado.
INV-08	A decomposição monetária fecha exatamente em centavos.
INV-09	Um atendimento cancelado não volta a um estado operacional ativo.
INV-10	Não existe retirada anterior à disponibilidade do atendimento.
INV-11	Não existe entrega iniciada antes da coleta de todos os atendimentos ativos.
INV-12	A primeira retirada bloqueia a reatribuição normal do motorista.
INV-13	Um atendimento retirado não é cancelado retroativamente por um incidente.
INV-14	O status derivado do pedido corresponde aos atendimentos válidos no mesmo instante.
INV-15	Todo incidente decidido tem um desfecho e um escopo financeiro identificável.
INV-16	Todo item mantém o preço contratado independentemente do catálogo atual.
Esses IDs são propostas para discussão, não identificadores existentes no projeto.

5. Escopo: o que adiar e o que está faltando
O que eu adiaria
1. Gorjeta (RN-22).
É um fluxo financeiro separado, posterior à entrega e sem recusa ou cancelamento. Para o primeiro modelo de delivery, adiciona complexidade sem ajudar a validar o núcleo de pedidos, atendimentos, pagamentos e reembolsos.
2. Incidentes com arbitragem completa (RN-14).
Não eliminaria incidentes do domínio, mas deixaria a arbitragem complexa para uma etapa posterior. Primeiro implementaria a estrutura básica de ocorrência e ajuste financeiro.
3. Tributação simulada detalhada (RN-09).
Manteria um campo sintético para fins didáticos, desde que não seja confundido com apuração fiscal real. Não tentaria construir um sistema tributário fictício excessivamente elaborado antes de estabilizar os fluxos financeiros.
4. Reatribuições complexas e exceções de logística.
O fluxo normal de atribuição e coleta deve existir. Pane, substituição depois da coleta e operações excepcionais podem entrar em uma segunda versão.
O que está faltando
Funcionalidade	Prioridade	Motivo
Prazo prometido de entrega	Alta	Necessário para calcular entrega no prazo
Endereço de entrega	Alta	Necessário para caracterizar a operação de entrega
Entrega malsucedida	Alta	Sem isso, existem pedidos que nunca chegam a um estado terminal
Remuneração do motorista	Alta	Necessária para calcular margem realista
Liquidação e repasse ao restaurante	Alta	Necessária para determinar quando a obrigação financeira é cumprida
Descontos e cupons	Média	Afetam valor pago, receita e reembolso
Disponibilidade de produtos	Média	Produto pode deixar de estar disponível após entrar no pedido
Avaliação de restaurante e motorista	Média	Necessária caso qualidade seja definida por avaliações
Pedido agendado	Baixa	Pode ser adiado sem comprometer a primeira versão
Avaliação de atendimento	Média	Permite medir qualidade além dos tempos operacionais
Um detalhe: avaliação e qualidade não são sinônimos. É possível medir qualidade operacional sem avaliações, mas os indicadores precisam ser explicitamente definidos.
Também recomendo decidir se o cliente pode fazer outro pedido enquanto existe um pedido anterior ainda em andamento. Isso pode importar para a simulação de volume e comportamento.

6. As três decisões que mais custariam caro reverter
1. Separação entre pedido, atendimento, item e estados derivados.
Essa é a fundação do modelo. Uma relação inadequada entre pedido e atendimento comprometerá os dados operacionais e a Gold inteira.
2. Contrato financeiro: pagamento, decomposição, comissão, repasse e reembolso.
É muito caro corrigir posteriormente um modelo em que receita bruta, receita da plataforma, obrigação com restaurantes, impostos e reembolsos estão misturados.
3. Contrato temporal e histórico de eventos.
A origem será distribuída em três bancos, sem FKs físicas. Se não existir uma estratégia de identificação, ordenação, deduplicação e reconstrução histórica, a CDC e as camadas analíticas ficarão vulneráveis a inconsistências difíceis de detectar.

7. O que não consegui avaliar por falta de informação
Não recebi o modelo conceitual, lógico ou físico, nem a implementação do gerador. Portanto, não consegui verificar:
- Se os IDs são globalmente únicos entre os três bancos.
- Como o banco documental do perfil de restaurante se relaciona com os bancos relacionais.
- Se o CDC será baseado em WAL, timestamps, polling ou outro mecanismo.
- Se existe transactional outbox.
- Se os eventos de transição são persistidos na origem ou reconstruídos a partir de snapshots.
- Se existe histórico de preços de produtos.
- Como os repasses serão efetivamente liquidados.
- Como são calculadas as taxas de comissão e serviço.
- Qual é o algoritmo de geração de eventos simultâneos.
- Se o gerador consegue produzir eventos atrasados, duplicados e fora de ordem.
- Se as três origens terão relógios simulados independentes.
- Quais são as regras concretas de prazo de entrega e qualidade.
Também não consegui avaliar a qualidade dos dados atuais além das contradições declaradas no documento. A lista de discrepâncias descreve o estado antigo do gerador, mas não permite verificar se a regeneração proposta resolve todas as inconsistências. Markdown colado.md


Conclusão
Minha recomendação é não avançar diretamente para a modelagem física.
Antes, faria uma rodada curta de fechamento de regras com quatro entregáveis:
1. Tabela verdade da RN-16, incluindo combinações mistas e cancelamentos.
2. Máquina de estados completa, separando pedido, atendimento, atribuição do motorista, incidente e pagamento.
3. Tabela financeira, com exemplos numéricos de compra, cancelamento parcial, cancelamento integral e incidente após retirada.
4. Contrato de eventos CDC, especificando identificação, ordenação, duplicação, histórico e reconstrução temporal.
O problema mais perigoso seria construir um pipeline tecnicamente correto que reproduzisse fielmente regras de negócio contraditórias. Nesse cenário, Bronze, Silver e Gold poderiam estar funcionando perfeitamente enquanto os indicadores finais estariam errados.