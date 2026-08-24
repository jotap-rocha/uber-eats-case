O que é a extensão Databricks para o Visual Studio Code?
A extensão Databricks para o Visual Studio Code permite que o senhor se conecte ao espaço de trabalho remoto Databricks a partir do Visual Studio Code ou do Cursor no computador de desenvolvimento local. Você pode então:

Defina, implante e execute Bundles ativos Databricks para aplicar padrões CI/CD e práticas recomendadas aos seus Jobs LakeFlow , pipeline declarativo LakeFlow Spark e Stacks MLOps usando a interface do Visual Studio Code. Consulte O que são pacotes Databricks ativos? e recurso de extensão de pacotes ativosDatabricks.
execução local Python arquivos de código do Visual Studio Code em Databricks clustering ou serverless compute em seu espaço de trabalho remoto. Consulte a execução de um arquivo Python em um clustering.
execução local Python arquivos de código (.py) e Python, R, Scala, e SQL Notebook (.py, .ipynb, .r, .scala, e .sql) do Visual Studio Code como LakeFlow Jobs em seu espaço de trabalho remoto. Consulte executar um arquivo Python como um trabalho.
Defina e configure seu ambiente de depuração e o Databricks Connect usando uma lista de verificação simples que aciona caixas de diálogo de seleção. Consulte Depurar código usando o Databricks Connect para a extensão do Databricks para o Visual Studio Code.
Depurar o Notebook célula por célula no Visual Studio Code com Databricks Connect. Veja a execução e a depuração de células do Notebook com Databricks Connect usando a extensão Databricks para o Visual Studio Code.
Sincronize o código local que o senhor desenvolve no Visual Studio Code com o código em seu espaço de trabalho remoto. Consulte Sincronizar sua workspace pasta com o Databricks
nota
A extensão Databricks para o Visual Studio Code oferece suporte à execução de R, Scala e SQL Notebook como trabalho automatizado, mas não oferece nenhum suporte mais profundo para essas linguagens no Visual Studio Code.

Começar
Para começar a usar a extensão Databricks para o Visual Studio Code:

Instale a extensão.
Crie um novo projeto Databricks ou converta um projeto existente do Visual Studio Code.
Configure seu projeto facilmente usando a interface do usuário da extensão Databricks.
execução de algum código Python como parte da extensão tutorial.
Depure seu código usando a integração do Databricks Connect.
Teste seu código usando pytest. Veja a execução de testes Python usando a extensão Databricks para Visual Studio Code.
Criar um novo projeto Databricks
Uma vez instalada a extensão, o senhor pode criar um novo projeto Databricks usando a extensão Databricks para o Visual Studio Code:

Inicie o Visual Studio Code.
Clique no ícone Databricks na barra lateral do Visual Studio Code para abrir a extensão.
Clique em Criar um novo projeto .
Na paleta de comandos , selecione um host e um método de autenticação para o projeto. Consulte Configurar autorização para a extensão Databricks para Visual Studio Code.
Em Provide a path to a folder where you would want your new project to be , digite o caminho para uma pasta no computador de desenvolvimento local onde deseja criar o projeto ou clique em Open folder selection dialog e selecione o caminho para a pasta do projeto.
Para usar o padrão na inicialização do projeto Databricks view, use as setas para cima e para baixo para selecionar um padrão de projeto e pressione Enter . Para obter informações sobre o padrão de projeto de pacote, consulte Databricks ativo Bundle project padrão.
Digite um nome exclusivo para este projeto para o projeto ou deixe o nome do projeto default como my_project e pressione Enter .
Escolha se deseja adicionar um esboço (amostra) Notebook, um esboço (amostra) Delta Live Tables pipeline, ou um esboço (amostra) Python pacote ao projeto, ou qualquer combinação desses esboços (amostras).
Pressione qualquer key para fechar o editor Databricks Project Init tab.
Em Selecione o projeto que você deseja abrir , escolha o projeto que você acabou de criar.
Abra um projeto existente do Databricks ativo Bundles
Um projeto Databricks ativo Bundles tem um arquivo databricks.yml na pasta raiz do projeto. Consulte Databricks ativo Bundle configuration. Se o senhor quiser usar a extensão com um projeto existente do Databricks ativo Bundles:

Inicie o Visual Studio Code. No menu principal, clique em Arquivo > Abrir pasta e navegue até o diretório que contém seu projeto de pacote.

Clique no ícone Databricks na barra lateral do Visual Studio Code para abrir e começar a usar o recurso da extensão.

Se a extensão Databricks para o Visual Studio Code descobrir mais de um projeto Databricks ativo Bundles na pasta atual, ela permitirá que o senhor escolha abrir um projeto ou criar um arquivo de configuração de projeto na pasta raiz.

Abrir o projeto Databricks existente

Se o senhor escolheu um projeto, na paleta de comandos , selecione o projeto Databricks ativo Bundles existente.
Se você criar uma configuração na pasta raiz, essa pasta se tornará um projeto de pacote.
Selecione um host e um método de autenticação para o projeto. Consulte Configurar autorização para a extensão Databricks para Visual Studio Code.

nota
Se o senhor abrir um projeto criado usando a extensão Databricks para o Visual Studio Code v1, a migração será tentada automaticamente usando a autenticação existente do projeto e a configuração workspace. O botão de migração só estará disponível se a migração automática falhar.

Alternar entre projetos do Databricks
A extensão Databricks para o Visual Studio Code permite que o senhor tenha vários projetos Databricks dentro do Visual Studio Code workspace e alterne facilmente entre eles. Com seu projeto de vários pacotes aberto no Visual Studio Code workspace:

Clique no ícone Databricks na barra lateral do Visual Studio Code para abrir a extensão.

Clique em Pasta local para selecionar o projeto a ser usado pela extensão.

Seletor de pasta local

nota
As ações de execução só estão disponíveis para arquivos no pacote ativo.

Converter um projeto em um projeto Databricks
Se o senhor tiver um projeto existente que deseja converter em um projeto da Databricks:

Inicie o Visual Studio Code. No menu principal, clique em Arquivo > Abrir pasta e navegue até seu projeto para abri-lo.
Clique no ícone Databricks na barra lateral do Visual Studio Code para abrir a extensão.
Clique em Criar configuração .
Na paleta de comandos , selecione um host e um método de autenticação para o projeto. Consulte Configurar autorização para a extensão Databricks para Visual Studio Code.