# Revisão adversarial — 01-grill.md (Gemini)

> Gerada manualmente pelo usuário no Gemini em 2026-11-12, com o prompt da skill `adversarial-judge`.
> Consultiva, não bloqueante. A triagem (procede / já coberto / engano) e as decisões ficam no
> [01-grill.md](01-grill.md), seção "Revisão adversarial".
>
> A revisão do GPT trazida na mesma data era de **outro projeto** (um bot do Teams) e foi descartada.

---

Os recortes de escopo da D5 (landing comum desacoplada entre arquiteturas), D10 (exclusão do MongoDB) e a parametrização por ambiente via .tfvars (Pergunta 10 / D15) estão bem endereçados e não precisam de revisão. Todo o resto apresenta falhas estruturais, premissas frágeis ou lacunas operacionais críticas detalhadas abaixo.

## 1. Suposições não verificadas ou provavelmente erradas

**Elegibilidade e cota de Synapse Dedicated SQL Pool em Free Account (D1, D2, D3):** O plano assume que basta criar a Free Account e conferir cota na "1ª task pós-cadastro" em eastus2/eastus. Contas Free Trial da Azure aplicam restrições rígidas de cota e frequentemente bloqueiam o provisionamento de Synapse Dedicated SQL Pools (DW100c) por padrão, exigindo abertura de chamado no suporte para liberação de cota (a confirmar na documentação/portal no momento do cadastro, pois as regras de cota variam por região e oferta ativa). Se o suporte levar dias para aprovar ou negar para conta Free, o cronômetro de 30 dias já estará correndo sem você conseguir subir o recurso principal.

**Suporte a SAS Token com escopo de container no conector ADLS/Blob do Airbyte (D18, Pendentes):** O plano prevê usar um token SAS restrito apenas a escrita no container landing. Historicamente, o conector oficial destination-azure-blob-storage do Airbyte Open Source exige Account Name e Account Key (chave mestra da storage account) na configuração padrão e não aceita SAS Token ou Service Principal em todas as versões (a confirmar na documentação da versão exata do conector instalado no abctl). Se exigir a Account Key, a premissa de menor privilégio da D18 cai por terra.

**Contradição entre D15 e D18 na identidade do Airbyte:** A D15 manda provisionar um Service Principal para o Airbyte em azure/infra/base/, mas a D18 afirma que a única credencial usada pelo Airbyte será um token SAS. Um Service Principal não gera nem substitui um SAS de conta (que deriva da Account Key ou de User Delegation Key via Entra ID), e usar um Service Principal exigiria Client Secret ou certificado — o que contradiz a regra da D18 de "não haver segredo". Há um recurso morto na D15 ou indefinição real de autenticação.

**Comportamento de COPY INTO + OPENJSON + ERRORFILE no Synapse Dedicated SQL Pool (Restrições, Pergunta 9, T7):**

- (Certeza técnica sobre Synapse Dedicated): Diferente do Serverless SQL Pool, o COPY INTO do Synapse Dedicated não lê JSON nativamente. Ingerir JSONL como "texto" exige configurar FILE_TYPE = 'CSV' com delimitadores inexistentes no payload (ex.: 0x0b) jogando a linha inteira numa coluna string.
- (Certeza técnica): O parâmetro ERRORFILE do COPY INTO captura apenas erros de parsing do formato CSV (ex.: estouro de tamanho de coluna), nunca valida sintaxe JSON. Uma linha com JSON quebrado será carregada normalmente na stg e explodirá a query de OPENJSON em tempo de execução, violando a regra da Pergunta 9 de que JSON malformado deve apenas ser registrado sem bloquear a carga.
- (A confirmar limites exatos na documentação do Synapse Dedicated): Colunas VARCHAR(8000)/NVARCHAR(4000) truncam ou falham se um pedido JSONL com muitos itens ultrapassar esse limite; já o uso de VARCHAR(MAX) impede Clustered Columnstore Index (obrigando HEAP) e degrada severamente a memória do nó único do DW100c durante o OPENJSON.

**Orquestração desacoplada entre Airbyte local e ADF (D12 vs D14, Pergunta 5):** A D12 diz que o Airbyte local fica desligado fora das janelas e define um ciclo sequencial (liga Airbyte → sync → desliga Airbyte → liga Synapse → pausa Synapse). Já a D14 entrega a parte da nuvem para um gatilho diário fixo do ADF de madrugada. Se o Airbyte local depende de janela manual/best-effort e fica desligado, quem inicia o passo 1? Pior: se o Airbyte estiver rodando no momento em que o gatilho diário do ADF disparar, o ADF verá arquivos recém-criados enquanto outras tabelas da mesma sync ainda estão sendo escritas, ingerindo uma carga parcial, marcando o ctl e perdendo dados silenciosamente.

**Pausa/retomada síncrona e nativa do pool pelo ADF (D14, D18):** (Certeza técnica sobre ADF) O ADF não possui atividade nativa para pausar/ligar Dedicated SQL Pool; isso exige atividade Web chamando a Azure Management REST API (resume/pause) via Managed Identity com permissão RBAC (SQL DB Contributor ou custom role com .../sqlPools/pause/action e resume/action), papel não especificado na D15. Além disso, essas chamadas REST são assíncronas (retornam 202 Accepted antes do pool mudar de estado, o que leva de 2 a 5 minutos). Sem um loop Until verificando o status Online antes da procedure e sem tratamento de erro em bloco (Upon Completion) para garantir o pause mesmo em falha intermediária, a carga quebrará ou deixará o pool ligado.

**Orçamento de tempo irreconciliável (Restrições, D1):** Dedicar "mais de 3 h por semana durante os 30 dias" (~12 a 16 horas no mês) para construir github-cd do zero (OIDC, environments), Terraform modularizado, estabilizar abctl com 31 tabelas, implementar COPY INTO + OPENJSON + qualidade + SCD2 + RN-33 ao centavo e ainda concluir azure-lakehouse e azure-kappa nos mesmos 30 dias é subestimar em 3x a 4x o esforço real de depuração de IAM/firewall/T-SQL na Azure.

## 2. Lacunas: o que o plano não cobre mas deveria

**Mapeamento de "pasta nova" vs. estrutura real de saída do Airbyte no ADLS (D12, D14, Especificação 3):** O plano trata a detecção de dados novos como "confere pasta nova na landing" e "ctl marca cada pasta". O conector ADLS/Blob do Airbyte particiona a saída por stream (31 pastas independentes: /{namespace}/{stream}/{ano}/{mês}/{dia}/...), e em cargas incrementais várias tabelas não terão arquivos novos num dado dia. O plano não especifica como o ctl rastreia 31 caminhos independentes nem como evita reprocessar arquivos antigos dentro de uma mesma partição diária caso haja mais de uma sync no dia.

**Deduplicação intra-batch e tratamento de DELETE no CDC do Postgres (Pergunta 1, D6, T4):** A stg recebe 1 linha por evento CDC (_ab_cdc_lsn, _ab_cdc_deleted_at), mas o plano não define a regra de consolidação antes da etapa B (ex.: ROW_NUMBER() particionado pela PK ordenado por LSN/sequência para resolver múltiplos UPDATEs na mesma janela) nem como eventos de exclusão (_ab_cdc_deleted_at IS NOT NULL) propagam para o dw sem corromper saldos financeiros.

**Perda de histórico intermediário e precisão temporal no Oracle (D7):** Ao trocar CDC por cursor UPDATED_AT nas tabelas CITIES, CUSTOMERS e DRIVERS, o plano aceita perder mudanças intermediárias entre syncs. Porém, DRIVERS e CITIES regem taxas e repasses de motoristas — que são exatamente o escopo financeiro do Warehouse. O plano não trata colisões de timestamp (dois updates no mesmo segundo no Oracle), dessincronia de relógio entre os containers Docker de Postgres e Oracle, nem o impacto disso nas junções temporais (AS OF) do SCD2 na etapa B.

**Precisão decimal na serialização JSONL (Problema, Pergunta 9):** O requisito exige fechamento exato em centavos. Dependendo da configuração de tipagem do conector Airbyte, colunas NUMERIC/DECIMAL podem ser serializadas como float no JSON (introduzindo erro de ponto flutuante antes mesmo de tocar o ADLS) ou como string. Não há nenhuma regra de validação ou casting explícito para DECIMAL(18,2)/DECIMAL(18,4) prevista na entrada da stg.

**Política de retenção/limpeza da stg (D6, Especificação 6–9):** O plano classifica a stg como "transitória", mas marca retenção/expiração como N/A. Se a stg nunca for truncada, o DW100c acumulará 1 ano de histórico + deltas diários duplicando o espaço cobrado mesmo com o pool pausado; se for truncada a cada execução, não há mecanismo definido para reprocessar uma janela sem reingerir da landing.

**Abertura dinâmica de firewall do Synapse para o runner do GitHub Actions (Pendentes, D17):** O item em Pendentes cita "sqlcmd do runner e o firewall do Synapse", mas o plano ignora como um GitHub-hosted runner (IP dinâmico) alcançará o endpoint SQL do Synapse se o firewall estiver fechado. Automatizar a abertura/fechamento temporário de regra de firewall no workflow (az synapse workspace firewall-rule) exige permissões adicionais na identidade OIDC do GitHub que não estão listadas na D15.

**Definição de corte temporal (UTC vs. Brasília) para o fechamento D-1 (Pergunta 5):** Os bancos Docker, os metadados _ab_cdc_* do Airbyte e o trigger do ADF operam por padrão em UTC, enquanto o SLA de negócio exige fechamento D-1 até 08:00 (Brasília, UTC-3). O plano não define qual campo determina a data contábil do pedido nem como tratar eventos de fim de dia (ex.: pedido criado às 23:55 BRT ingerido às 01:30 BRT) para não contaminar o fechamento do dia seguinte.

## 3. Alternativas mais simples ou mais robustas que não foram consideradas

**Substituir o Airbyte (abctl) por dlt (data load tool) ou extrator Python leve (D7, D9, D12):** O próprio plano registra que o abctl já sofreu OOM (exit 137) nos ~9,7 GB de RAM do Docker local porque sobe um cluster Kubernetes (kind) com pods Java/Debezium pesados. Usar dlt ou um script Python (psycopg2 + oracledb + azure-storage-blob) roda com menos de 300 MB de RAM, suporta carga incremental por cursor/LSN, grava direto no ADLS com SAS Token ou Service Principal sem depender de limitações de conectores do Airbyte, e elimina o risco de travar a máquina local.

**Gravar em Parquet na landing em vez de JSONL (D5, Restrições, T7):** O plano escolheu JSONL para tolerar evolução de schema e teve que criar o contorno de ler JSONL via CSV + OPENJSON no Synapse Dedicated. Tanto o Airbyte quanto o dlt escrevem Parquet nativamente no ADLS. O COPY INTO do Synapse Dedicated SQL Pool lê Parquet nativamente com mapeamento explícito de colunas (ignorando colunas novas automaticamente e falhando se uma coluna esperada sumir, atendendo exatamente à Pergunta 9), preserva tipos DECIMAL exatos sem risco de float JSON e elimina o custo de CPU/memória do OPENJSON.

**Avaliar Azure SQL Database (S0 ou Serverless) em vez de Synapse Dedicated SQL Pool DW100c (D2, D6, D14):** Para o volume de um projeto de portfólio (1 ano de dados sintéticos), a arquitetura MPP de 60 distribuições do DW100c gera overhead em tabelas pequenas, exige gestão de distribuição (HASH/REPLICATE), leva minutos para pausar/ligar e cobra armazenamento de snapshots mesmo pausado. Um Azure SQL Database Serverless (ou S0 fixo a ~US$ 15/mês) executa OPENJSON e MERGE transacional muito mais rápido nesse volume, sem precisar construir state machine REST no ADF para pausar/ligar o banco. (Válido apenas se o uso de Synapse Dedicated não for um requisito inegociável de vitrine de portfólio).

**Disparar a carga da nuvem via GitHub Actions pós-sync em vez de gatilho cego no ADF (D12, D14, D17):** Como a extração já ocorre localmente sob controle do usuário/agendador local e o projeto já exige esteira no GitHub Actions (github-cd), disparar o workflow de carga via API do GitHub (workflow_dispatch) ao final do sync local elimina o ADF do Terraform, acaba com a race condition entre janela local e gatilho da nuvem, e garante que o Synapse só seja ligado quando houver um lote completo e fechado na landing.

## 4. Riscos concretos (técnicos, de segurança, de custo, de escopo) que o plano ignora

**Risco Técnico — OOM recorrente no backfill e crescimento descontrolado de WAL no Postgres (Restrições, D7, D12):** Fazer o snapshot inicial (backfill de 1 ano) de 28 tabelas do Postgres via Debezium embarcado no abctl dentro de 9,7 GB de RAM compartilhada com o Oracle (2,3 GB) tem altíssima chance de repetir o exit 137. Além disso, como o Airbyte ficará desligado entre janelas (D12), o replication slot criado no Postgres continuará retendo segmentos de WAL no disco local durante qualquer atividade no banco; se o Airbyte falhar por alguns dias, o disco local enche.

**Risco de Custo — Queima invisível do crédito de 30 dias antes do alerta disparar (D1, D3, D4, D14):**

- (A confirmar detalhes na documentação de billing do Synapse): No Synapse Dedicated SQL Pool, cada ciclo de resume incorre em cobrança mínima por bloco de hora, e os backups/restore points automáticos do pool continuam gerando cobrança de armazenamento mesmo com o compute pausado. Ligar e pausar o pool repetidamente durante os testes de desenvolvimento da esteira e do ADF pode consumir dezenas de horas faturadas em poucos dias.
- (Certeza técnica sobre Azure Cost Management): Os alertas de Budget da Azure têm latência de 8 a 24 horas para processar o consumo. Se um bug no loop do ADF deixar o DW100c ligado ou em ciclos repetidos, o spending limit cortará a assinatura inteira antes que o e-mail de alerta de 80% seja enviado.

**Risco de Segurança — Vazamento de dados em logs públicos e SAS Token no terraform.tfstate (Restrições, Pergunta 4, D15, D18):**

- Como o repositório e os logs de execução do GitHub Actions são públicos, qualquer falha de parsing em sqlcmd ou OPENJSON durante a esteira pode imprimir no log público a linha de dados que causou o erro (expondo registros de customers/drivers, contrariando a Pergunta 4).
- Se o token SAS da D18 for gerado via Terraform (azurerm_storage_account_sas), a assinatura secreta ficará gravada em texto claro no terraform.tfstate remoto, exigindo controle estrito de acesso ao container de state e rotação manual periódica para não quebrar o Airbyte local quando expirar.

**Risco de Escopo e Bloqueio — Dependência circular de cronograma com github-cd (D1, D17, Pendentes):** Condicionar o primeiro terraform apply do azure-warehouse à entrega completa de outro projeto (github-cd, com subagente, 3 skills e OIDC) cria um gargalo crítico. Qualquer atraso no github-cd paralisa a validação real na Azure, comprimindo a janela útil dos 30 dias da Free Account e ameaçando a execução das outras duas arquiteturas (azure-lakehouse e azure-kappa) que compartilham o mesmo crédito.
