# Ambiente virtual
Depois de fazer o download do projeto por meio do Git Clone, será necessário criar o ambinete virtual.
1 - Verificar se possui o virtualenv instalado:
```
pip install virtualenv
```
2 - Criar ambiente virtual (ATENÇÃO A VERSÃO PYTHON DO PROJETO):
```
python3.9 -m venv .venv
```
3 - Ativar ambiente virtual:
```
source .venv/bin/activate
```
4 - Validar se o ambinete virtual está operacional:
```
pip list
```
5 - Em caso de warning ao fazer algum tipo de instalação pip no ambiente virtual criado, executar o comando abaixo:
```
python3.9 -m pip install --upgrade pip
```
# Bibliotecas do projeto
O Arquivo "requirements.txt" possui as bibliotecas necessárias para a execução do projeto. 
Basta fazer a execução das respectivas bibliotecas por meio da instrução abaixo:
```
pip install -r requirements.txt
```
# Ativando ambiente virtual Visual Code
Para utilizar o ambiente virtual no Visual Code, basta clicar no botão superior direito do seu projeto chamado "SELECT Kernel" e selecionar a pasta onde foi criada o ambiente .venv e buscar o executável python.
